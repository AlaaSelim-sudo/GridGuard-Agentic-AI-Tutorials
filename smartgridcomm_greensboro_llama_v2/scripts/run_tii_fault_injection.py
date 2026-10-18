"""Run a controlled fail-closed validation campaign on SMART-DS Greensboro.

This experiment is intentionally separate from the optimizer benchmark.  It
injects one known condition at a time into the real GridGuard verification
node and records whether the candidate is rejected before simulation, rejected
after simulation, or authorized for the deterministic commit node.

The electrical positive and negative controls use OpenDSS snapshots from the
Greensboro ``uhs20_1247`` restoration case.  Readback mismatch/unavailable
conditions are deterministic software-in-the-loop injections; they do not
claim hardware-in-the-loop or field cyber-resilience.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator


ROOT = Path(__file__).resolve().parents[1]
VENDORED_DEPS = ROOT / "tmp" / "gridguard_deps"
sys.path.insert(0, str(VENDORED_DEPS))
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
os.environ.setdefault("GRIDGUARD_HEADLESS", "1")

import OPRO_Optimizer as gridguard  # noqa: E402
from build_smartds_feeder_compat import build_overlay, sha256  # noqa: E402


CASE_DIR = ROOT / "SMARTDS_GSO_solar_extreme_batt_high_peak_opendss" / "uhs20_1247"
SOURCE_MASTER = CASE_DIR / "Master.dss"
STORAGE_FILE = CASE_DIR / "uhs20_1247--udt8894" / "Storage.dss"
FAULT_LINE = "l(r:udt8894-uhs20_1247)_disconnect"
TIE_LINE = "elbswitch(r:udt8894-udt9916)u_82773"
FLEET_ID = "udt8894_battery_fleet"


class FixedCandidatePolicy:
    """Deterministically emits one injected bundle through the planner interface."""

    model = "deterministic-fault-injection"
    seed = 1701
    candidate_source = "CONTROLLED_INJECTION"
    actor_type = "deterministic"

    def __init__(self, candidate: dict[str, Any]):
        self.candidate = candidate
        self.call_records: list[dict[str, Any]] = []

    def chat(self, **_kwargs: Any) -> str:
        return json.dumps({"candidates": [self.candidate]})


@dataclass(frozen=True)
class FaultScenario:
    scenario_id: str
    layer: str
    description: str
    candidate: dict[str, Any]
    expected_certified: bool
    expected_failure_prefixes: tuple[str, ...] = ()
    telemetry_patch: dict[str, Any] | None = None
    readback_injection: str | None = None


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def storage_names(path: Path) -> list[str]:
    pattern = re.compile(r"^\s*new\s+storage\.([^\s]+)", re.IGNORECASE)
    names = [
        match.group(1)
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if (match := pattern.match(line))
    ]
    if not names:
        raise RuntimeError(f"No storage devices parsed from {path}")
    return names


def finite_json(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): finite_json(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [finite_json(item) for item in value]
    if isinstance(value, float):
        return value if value == value and abs(value) != float("inf") else None
    return value


def compact_metrics(snapshot: gridguard.SnapshotResult) -> dict[str, Any]:
    metrics = gridguard.summarize_metrics(
        snapshot, gridguard.V_MIN_PU_DEFAULT, gridguard.V_MAX_PU_DEFAULT
    )
    metrics["switching_effort"] = 0
    metrics.update(gridguard.action_burden([]))
    metrics["objective"] = gridguard.objective(metrics)
    return finite_json(metrics)


def build_config(fleet: list[str]) -> gridguard.GridGuardConfig:
    return gridguard.GridGuardConfig(
        steps=1,
        k_candidates=1,
        max_actions=2,
        llm_samples=1,
        explore_temp=0.0,
        guardrail_start_stuck=0,
        max_stuck=1,
        allow_switch=True,
        allow_pv=False,
        allow_load=False,
        allow_var_gen=False,
        prefer_utility_first=False,
        vargen_after_stuck=99,
        pv_after_stuck=99,
        load_after_stuck=99,
        fast_llm=True,
        show_meta_prompt=False,
        teaching_notes=False,
        extra_instruction="Controlled validation and cyber-physical fault injection.",
        # A fixed deterministic policy uses the ordinary planner interface;
        # no external model is called.
        enable_llm_candidates=True,
        enable_physics_fallback=False,
        enable_portfolio_seeds=False,
        enable_scored_memory=False,
        enable_verifier_feedback=True,
        enable_critic=False,
        allow_recovered_solve=False,
        certificate_mode="relative_safe_improvement",
        voltage_severity_tolerance_pu=1e-5,
        max_line_loading_tolerance_pct=0.10,
        thermal_severity_tolerance_pct_sum=0.50,
        restoration_tolerance_kw=0.10,
        max_physical_actions=500,
        storage_fleets={FLEET_ID: fleet},
        restoration_ties=[TIE_LINE],
    )


def base_state(
    current_snapshot: gridguard.SnapshotResult,
    current_metrics: dict[str, Any],
    reference_snapshot: gridguard.SnapshotResult,
    reference_metrics: dict[str, Any],
    main_dss: Path,
    candidate: dict[str, Any],
    scenario_id: str,
) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    return {
        "case": {
            "label": f"TII-CONTROLLED-{scenario_id}",
            "folder": str(CASE_DIR),
            "main_dss": str(main_dss),
        },
        "base_cmds": ["set controlmode=off", f"Open Line.{FAULT_LINE}"],
        "state_cmds": [],
        "operating_state_id": gridguard.operating_state_fingerprint([]),
        "evaluated_fingerprints": {},
        "vmin": gridguard.V_MIN_PU_DEFAULT,
        "vmax": gridguard.V_MAX_PU_DEFAULT,
        "telemetry": {
            "source": "OpenDSS controlled fault-injection campaign",
            "timestamp_utc": now,
            "timestamp_mode": "external",
            "max_age_s": 300.0,
            "trusted": True,
            "quarantined_devices": [f"line.{FAULT_LINE}"],
            "expected_topology_hash": current_snapshot.topology_hash,
        },
        "admissible_controls": current_snapshot.devices,
        "candidate_actions": [candidate],
        "current_snapshot": current_snapshot,
        "baseline_snapshot": current_snapshot,
        "security_reference_snapshot": reference_snapshot,
        "current_metrics": current_metrics,
        "baseline_metrics": dict(current_metrics),
        "security_reference_metrics": reference_metrics,
        "recent_evals": [],
        "simulation_outputs": [],
        "violation_summaries": [current_metrics],
        "feedback_history": [],
        "meta_prompt_snapshots": [],
        "agent_trace": [],
        "verification_results": [],
        "evaluation_history": [],
        "best_so_far": [],
        "history": [],
        "iteration": 0,
        "stuck": 0,
        "total_candidates": 0,
        "candidate_slots_allocated": 1,
        "llm_candidate_objects_returned": 0,
        "llm_parse_valid_candidates": 0,
        "historical_duplicates_filtered": 0,
        "certified_candidates": 0,
        "invalid_candidates": 0,
        "rejected_candidates": 0,
        "switching_effort": 0,
        "first_certified_iteration": None,
    }


def safe_candidate() -> dict[str, Any]:
    return {
        "name": "known_safe_tie_plus_fleet_41pct",
        "source": "CONTROL",
        "reasoning": "Known physics-certified Greensboro restoration control.",
        "actions": [
            {"type": "switch_line", "line": TIE_LINE, "op": "close"},
            {
                "type": "storage_fleet_setpoint",
                "fleet": FLEET_ID,
                "state": "CHARGING",
                "pct_kw": 41,
            },
        ],
    }


def blind_tie_candidate() -> dict[str, Any]:
    return {
        "name": "executable_but_thermally_regressive_blind_tie",
        "source": "NEGATIVE_CONTROL",
        "reasoning": "Topology-only pickup that is known to create a new overload.",
        "actions": [{"type": "switch_line", "line": TIE_LINE, "op": "close"}],
    }


def scenarios() -> list[FaultScenario]:
    safe = safe_candidate()
    return [
        FaultScenario(
            "known_safe_control", "control",
            "Known physics-certified tie plus storage-fleet dispatch.",
            safe, True,
        ),
        FaultScenario(
            "unknown_action_schema", "schema",
            "Unsupported raw-command action object.",
            {"name": "unknown_schema", "source": "INJECTION", "actions": [
                {"type": "raw_dss", "command": "Edit Vsource.source pu=1.10"}
            ]},
            False, ("action[0]:unknown_type:raw_dss",),
        ),
        FaultScenario(
            "unknown_device", "admissibility",
            "Well-formed DER action targeting a device absent from the catalog.",
            {"name": "unknown_device", "source": "INJECTION", "actions": [
                {"type": "der_setpoint", "device": "PVSystem.NOT_IN_CATALOG", "pct_pmpp": 50}
            ]},
            False, ("action[0]:unknown_der:",),
        ),
        FaultScenario(
            "unsafe_vsource_attempt", "admissibility",
            "Attempt to route a source-voltage edit through the DER schema.",
            {"name": "unsafe_vsource", "source": "INJECTION", "actions": [
                {"type": "der_setpoint", "device": "Vsource.source", "kw": 1}
            ]},
            False, ("action[0]:unknown_der:Vsource.source",),
        ),
        FaultScenario(
            "stale_telemetry", "cyber",
            "Valid control evaluated against an expired external snapshot.",
            safe, False, ("cyber:stale_telemetry:",),
            telemetry_patch={
                "timestamp_utc": "2000-01-01T00:00:00+00:00",
                "timestamp_mode": "external",
                "max_age_s": 1.0,
            },
        ),
        FaultScenario(
            "untrusted_telemetry", "cyber",
            "Valid control with the telemetry trust bit revoked.",
            safe, False, ("cyber:telemetry_untrusted",),
            telemetry_patch={"trusted": False},
        ),
        FaultScenario(
            "quarantined_target", "cyber",
            "Switch command aimed at the explicitly quarantined faulted line.",
            {"name": "quarantined_target", "source": "INJECTION", "actions": [
                {"type": "switch_line", "line": FAULT_LINE, "op": "close"}
            ]},
            False, ("action[0]:cyber_quarantined:",),
        ),
        FaultScenario(
            "topology_hash_mismatch", "cyber",
            "Valid control paired with a forged expected-topology fingerprint.",
            safe, False, ("cyber:topology_mismatch",),
            telemetry_patch={"expected_topology_hash": "INJECTED-MISMATCH"},
        ),
        FaultScenario(
            "actuation_readback_mismatch", "actuation",
            "Post-solve actuator state differs from the requested state.",
            safe, False, ("cyber:actuation_mismatch:",),
            readback_injection="mismatch",
        ),
        FaultScenario(
            "actuation_readback_unavailable", "actuation",
            "Post-solve actuator state cannot be observed.",
            safe, False, ("cyber:actuation_unavailable:",),
            readback_injection="unavailable",
        ),
        FaultScenario(
            "physical_thermal_regression", "physics",
            "Executable blind tie closure restores load but creates an overload.",
            blind_tie_candidate(), False, ("security:thermal_regression",),
        ),
    ]


def _has_prefix(failures: list[str], prefix: str) -> bool:
    return any(str(failure).startswith(prefix) for failure in failures)


def failure_family(failure: str) -> str:
    text = str(failure)
    if text.startswith("action["):
        detail = text.split(":", 1)[1] if ":" in text else text
        if detail.startswith("cyber_"):
            return "cyber"
        if detail.startswith(("unknown_", "inadmissible_", "line_not_")):
            return "admissibility"
        return "schema"
    return text.split(":", 1)[0] if text else "unknown"


def injected_readback(mode: str) -> Callable[..., tuple[list[dict[str, Any]], list[str]]]:
    if mode not in {"mismatch", "unavailable"}:
        raise ValueError(mode)

    def readback(actions_any: Any, _snapshot: Any, **_kwargs: Any):
        actions = gridguard.sanitize_actions(actions_any)
        target = gridguard._action_target(actions[0]) if actions else "unknown"
        record = {
            "action_index": 0,
            "type": actions[0].get("type", "") if actions else "",
            "target": target,
            "requested": "controlled_request",
            "observed": "injected_different_value" if mode == "mismatch" else None,
            "source": f"controlled_fault_injection:{mode}",
            "status": mode,
        }
        return [record], [f"cyber:actuation_{mode}:action[0]:{target.lower()}"]

    return readback


@contextmanager
def patched_verifier_dependencies(
    compile_replay: Callable[..., gridguard.SnapshotResult],
    readback_replacement: Callable[..., tuple[list[dict[str, Any]], list[str]]] | None,
) -> Iterator[None]:
    original_compile = gridguard.compile_and_solve
    original_readback = gridguard.verify_post_solve_actuation
    gridguard.compile_and_solve = compile_replay
    if readback_replacement is not None:
        gridguard.verify_post_solve_actuation = readback_replacement
    try:
        yield
    finally:
        gridguard.compile_and_solve = original_compile
        gridguard.verify_post_solve_actuation = original_readback


def evaluate_scenario(
    config: gridguard.GridGuardConfig,
    scenario: FaultScenario,
    current_snapshot: gridguard.SnapshotResult,
    current_metrics: dict[str, Any],
    reference_snapshot: gridguard.SnapshotResult,
    reference_metrics: dict[str, Any],
    main_dss: Path,
    compile_replay: Callable[..., gridguard.SnapshotResult],
) -> dict[str, Any]:
    state = base_state(
        current_snapshot, current_metrics, reference_snapshot, reference_metrics,
        main_dss, scenario.candidate, scenario.scenario_id,
    )
    state["telemetry"].update(scenario.telemetry_patch or {})
    replacement = (
        injected_readback(scenario.readback_injection)
        if scenario.readback_injection else None
    )
    started = time.perf_counter()
    with patched_verifier_dependencies(compile_replay, replacement):
        engine = gridguard.GridGuardEngine(
            llm=FixedCandidatePolicy(scenario.candidate),
            translator=gridguard.ActionTranslator(),
            config=config,
            progress=lambda _message: None,
            step_done=lambda _record: None,
        )
        final_state = engine.run(state)
    elapsed_ms = 1000.0 * (time.perf_counter() - started)

    records = final_state.get("evaluation_history") or []
    record = records[0] if records else {}
    trace_nodes = [str(item.get("node")) for item in final_state.get("agent_trace", [])]
    # The finalize node intentionally does not append another trace record, but
    # route="done" is its returned terminal state.
    if final_state.get("route") == "done":
        trace_nodes.append("finalize")
    committed = len(final_state.get("history", [])) > 1
    authorized = "accept" in trace_nodes
    failures = [str(item) for item in record.get("failure_modes") or []]
    certified = bool(record.get("certified"))
    expected_prefixes_observed = all(
        _has_prefix(failures, prefix) for prefix in scenario.expected_failure_prefixes
    )
    expected_disposition_observed = certified == scenario.expected_certified
    detected = bool(expected_prefixes_observed and expected_disposition_observed)
    expected_reject = not scenario.expected_certified
    return finite_json({
        "scenario_id": scenario.scenario_id,
        "layer": scenario.layer,
        "description": scenario.description,
        "expected_disposition": "certify" if scenario.expected_certified else "reject",
        "observed_disposition": "certify" if certified else "reject",
        "detected": detected,
        "expected_failure_prefixes": list(scenario.expected_failure_prefixes),
        "failure_modes": failures,
        "failure_families": sorted({failure_family(item) for item in failures}),
        "simulated": bool(record.get("simulated")),
        "pre_simulation_rejection": not bool(record.get("simulated")),
        "authorized_for_commit": authorized,
        "commit_node_executed": committed,
        "unsafe_commit": bool(expected_reject and committed),
        "false_reject": bool(scenario.expected_certified and not certified),
        "supervisory_action_count": record.get("supervisory_action_count"),
        "physical_action_count": record.get("physical_action_count"),
        "readback_checks": len(record.get("actuation_readback") or []),
        "new_voltage_violation_count": record.get("new_voltage_violation_count"),
        "new_line_overload_count": record.get("new_line_overload_count"),
        "candidate_voltage_severity": (record.get("metrics") or {}).get("v_severity"),
        "candidate_thermal_severity": (
            record.get("metrics") or {}
        ).get("thermal_severity_pct_sum"),
        "candidate_served_load_kw": (record.get("metrics") or {}).get("served_load_kw"),
        "evaluation_elapsed_ms": elapsed_ms,
        "langgraph_trace": trace_nodes,
        "run_record_path": final_state.get("run_path"),
    })


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    controls = [row for row in rows if row["expected_disposition"] == "certify"]
    hazards = [row for row in rows if row["expected_disposition"] == "reject"]
    layer_rows: list[dict[str, Any]] = []
    for layer in sorted({row["layer"] for row in rows}):
        items = [row for row in rows if row["layer"] == layer]
        layer_rows.append({
            "layer": layer,
            "cases": len(items),
            "detected": sum(bool(row["detected"]) for row in items),
            "detection_rate": sum(bool(row["detected"]) for row in items) / len(items),
            "pre_simulation_rejections": sum(
                bool(row["pre_simulation_rejection"]) for row in items
            ),
        })
    return finite_json({
        "scenario_count": len(rows),
        "hazard_case_count": len(hazards),
        "hazards_detected": sum(bool(row["detected"]) for row in hazards),
        "hazard_detection_rate": (
            sum(bool(row["detected"]) for row in hazards) / len(hazards)
            if hazards else None
        ),
        "safe_control_count": len(controls),
        "false_reject_count": sum(bool(row["false_reject"]) for row in controls),
        "false_reject_rate": (
            sum(bool(row["false_reject"]) for row in controls) / len(controls)
            if controls else None
        ),
        "unsafe_commit_count": sum(bool(row["unsafe_commit"]) for row in rows),
        "pre_simulation_rejection_count": sum(
            bool(row["pre_simulation_rejection"]) for row in hazards
        ),
        "post_simulation_rejection_count": sum(
            not bool(row["pre_simulation_rejection"]) for row in hazards
        ),
        "by_layer": layer_rows,
    })


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    flattened: list[dict[str, Any]] = []
    for row in rows:
        item = dict(row)
        for key, value in list(item.items()):
            if isinstance(value, (dict, list, tuple)):
                item[key] = json.dumps(value, sort_keys=True)
        flattened.append(item)
    fields = sorted({key for row in flattened for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(flattened)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir", type=Path,
        default=ROOT / "output" / "tii_fault_injection_v1",
    )
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    fleet = storage_names(STORAGE_FILE)
    overlay = build_overlay(SOURCE_MASTER)
    main_dss = Path(overlay["compatibility_master"])
    original_compile = gridguard.compile_and_solve
    canonical_snapshots: dict[str, gridguard.SnapshotResult] = {}
    canonical_commands = {
        "pre_contingency": ["set controlmode=off"],
        "outage": ["set controlmode=off", f"Open Line.{FAULT_LINE}"],
        "blind_tie_close": [
            "set controlmode=off", f"Open Line.{FAULT_LINE}",
            f"Edit Line.{TIE_LINE} enabled=yes",
        ],
        # Keep this last so actual readback for the positive control observes
        # precisely the state represented by the replayed safe snapshot.
        "tie_plus_fleet_41pct": [
            "set controlmode=off", f"Open Line.{FAULT_LINE}",
            f"Edit Line.{TIE_LINE} enabled=yes",
            *[
                f"Edit Storage.{name} DispMode=EXTERNAL State=CHARGING %Charge=41"
                for name in fleet
            ],
        ],
    }
    for label, commands in canonical_commands.items():
        print(f"[fault-suite] solving canonical state: {label}", flush=True)
        canonical_snapshots[label] = original_compile(
            label, str(CASE_DIR), str(main_dss), commands,
            gridguard.V_MIN_PU_DEFAULT, gridguard.V_MAX_PU_DEFAULT,
            recover_on_failure=False,
        )
    canonical_metrics = {
        label: compact_metrics(snapshot)
        for label, snapshot in canonical_snapshots.items()
    }
    (output_dir / "canonical_states.json").write_text(
        json.dumps(canonical_metrics, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    def compile_replay(
        _case_label: str,
        _case_folder: str,
        _dss_path: str,
        commands: list[str],
        _vmin: float,
        _vmax: float,
        recover_on_failure: bool = False,
    ) -> gridguard.SnapshotResult:
        if recover_on_failure:
            raise AssertionError("Fault-injection protocol requires strict no-recovery solves")
        command_text = "\n".join(commands).lower()
        if f"line.{TIE_LINE}".lower() in command_text:
            if "%charge=41" in command_text:
                return canonical_snapshots["tie_plus_fleet_41pct"]
            return canonical_snapshots["blind_tie_close"]
        return canonical_snapshots["outage"]

    config = build_config(fleet)
    gridguard.RUN_DIR = output_dir / "raw"
    gridguard.RUN_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for scenario in scenarios():
        print(f"[fault-suite] scenario={scenario.scenario_id}", flush=True)
        row = evaluate_scenario(
            config,
            scenario,
            canonical_snapshots["outage"],
            canonical_metrics["outage"],
            canonical_snapshots["pre_contingency"],
            canonical_metrics["pre_contingency"],
            main_dss,
            compile_replay,
        )
        rows.append(row)

    summary = summarize(rows)
    run_payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "scope": (
            "Software-in-the-loop controlled injections on OpenDSS SMART-DS Greensboro; "
            "readback mismatch/unavailable are deterministic interface faults, not field attacks."
        ),
        "case": "SMART-DS Greensboro uhs20_1247 parent substation",
        "source_master": str(SOURCE_MASTER),
        "source_master_sha256": sha256(SOURCE_MASTER),
        "redirected_source_tree_sha256": overlay["redirected_source_tree_sha256"],
        "compatibility_master": str(main_dss),
        "compatibility_master_sha256": overlay["compatibility_master_sha256"],
        "gridguard_core_sha256": file_sha256(ROOT / "OPRO_Optimizer.py"),
        "runner_sha256": file_sha256(Path(__file__).resolve()),
        "fault_line": FAULT_LINE,
        "alternate_tie": TIE_LINE,
        "fleet_id": FLEET_ID,
        "fleet_device_count": len(fleet),
        "certificate": {
            "mode": "pre-contingency-relative safe improvement",
            "voltage_severity_tolerance_pu": config.voltage_severity_tolerance_pu,
            "max_line_loading_tolerance_pct": config.max_line_loading_tolerance_pct,
            "thermal_severity_tolerance_pct_sum": config.thermal_severity_tolerance_pct_sum,
            "restoration_tolerance_kw": config.restoration_tolerance_kw,
            "solver_recovery_allowed": config.allow_recovered_solve,
        },
        "summary": summary,
        "trials": rows,
    }
    run_payload = finite_json(run_payload)
    (output_dir / "fault_injection_results.json").write_text(
        json.dumps(run_payload, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    with (output_dir / "fault_injection_trials.jsonl").open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, allow_nan=False) + "\n")
    write_csv(output_dir / "fault_injection_trials.csv", rows)
    write_csv(output_dir / "fault_injection_summary_by_layer.csv", summary["by_layer"])
    (output_dir / "fault_injection_summary.json").write_text(
        json.dumps(summary, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "output_dir": str(output_dir),
        "scenario_count": summary["scenario_count"],
        "hazard_detection_rate": summary["hazard_detection_rate"],
        "false_reject_count": summary["false_reject_count"],
        "unsafe_commit_count": summary["unsafe_commit_count"],
    }, indent=2), flush=True)
    return 0 if summary["hazards_detected"] == summary["hazard_case_count"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
