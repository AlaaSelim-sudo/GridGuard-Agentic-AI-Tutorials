"""Run the Greensboro uhs20 outage-restoration benchmark.

The benchmark compares topology-only restoration with coordinated switching
and an allowlisted storage-fleet macro-action.  Candidate certification uses a
saved pre-contingency security envelope, while improvement is scored from the
outage state.  Every stochastic search method receives the same supervisory
action, candidate-simulation, and iteration budgets.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import re
import statistics
import sys
import time
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[1]
VENDORED_DEPS = ROOT / "tmp" / "gridguard_deps"
sys.path.insert(0, str(VENDORED_DEPS))
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
os.environ.setdefault("GRIDGUARD_HEADLESS", "1")

import OPRO_Optimizer as gridguard  # noqa: E402
from build_smartds_feeder_compat import build_overlay, sha256  # noqa: E402
from run_tii_benchmark import bootstrap_ci, ollama_metadata, warm_ollama_model  # noqa: E402


CASE_DIR = (
    ROOT / "SMARTDS_GSO_solar_extreme_batt_high_peak_opendss" / "uhs20_1247"
)
SOURCE_MASTER = CASE_DIR / "Master.dss"
STORAGE_FILE = CASE_DIR / "uhs20_1247--udt8894" / "Storage.dss"
FAULT_LINE = "l(r:udt8894-uhs20_1247)_disconnect"
TIE_LINE = "elbswitch(r:udt8894-udt9916)u_82773"
CRITICAL_RECLOSER = "recloser_disswitch(r:udt5179-udt6452)u_85430"
FLEET_ID = "udt8894_battery_fleet"
METHODS = (
    "no_action",
    "random_screen",
    "llm_no_memory",
    "opro_no_critic",
    "gridguard_llm",
    "physics_seed",
    "gridguard_hybrid",
)


class NoopPolicy:
    model = "deterministic-no-llm"
    seed = None
    candidate_source = "NONE"
    actor_type = "deterministic"

    def chat(self, **_kwargs: Any) -> str:
        return '{"candidates": []}'


class RandomRestorationPolicy:
    model = "seeded-random-restoration"
    candidate_source = "RANDOM"
    actor_type = "seeded_random"

    def __init__(self, seed: int, k_candidates: int):
        self.seed = int(seed)
        self.k_candidates = int(k_candidates)
        self.rng = random.Random(seed)
        self.call_index = 0

    def chat(self, system: str, user_text: str, **_kwargs: Any) -> str:
        self.call_index += 1
        if "Constraint Critic Agent" in system:
            return json.dumps({
                "diagnosis": "Random search has no critic.", "avoid": [],
                "next_focus": [], "repair_instruction": "Continue random search.",
            })
        match = re.search(r"<JSON>(.*?)</JSON>", user_text, flags=re.S)
        context = json.loads(match.group(1)) if match else {}
        pools = context.get("EXACT_TARGET_POOLS") or {}
        ties = list(pools.get("open_switches") or [])
        fleets = list(pools.get("storage_fleets") or [])
        if not ties:
            return '{"candidates": []}'
        tie = TIE_LINE if TIE_LINE in ties else ties[0]
        fleet = str((fleets[0] if fleets else {}).get("fleet", FLEET_ID))
        candidates = []
        for index in range(self.k_candidates):
            actions: list[dict[str, Any]] = [
                {"type": "switch_line", "line": tie, "op": "close"}
            ]
            if self.rng.random() >= 0.20 and fleets:
                state = self.rng.choice(["CHARGING", "DISCHARGING", "IDLING"])
                fleet_action: dict[str, Any] = {
                    "type": "storage_fleet_setpoint", "fleet": fleet, "state": state,
                }
                if state != "IDLING":
                    fleet_action["pct_kw"] = self.rng.choice([20, 40, 60, 80, 100])
                actions.append(fleet_action)
            candidates.append({
                "name": f"random_restore_{self.call_index}_{index}",
                "actions": actions,
                "reasoning": "Seeded random supervisory restoration action.",
            })
        return json.dumps({"candidates": candidates})


def storage_names(path: Path) -> list[str]:
    pattern = re.compile(r"^\s*new\s+storage\.([^\s]+)", re.IGNORECASE)
    names = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        match = pattern.match(line)
        if match:
            names.append(match.group(1))
    if not names:
        raise RuntimeError(f"No storage devices parsed from {path}")
    return names


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def line_loading(snapshot: gridguard.SnapshotResult, line: str) -> float | None:
    frame = snapshot.line_df
    if frame is None or frame.empty:
        return None
    rows = frame[frame["line"].astype(str).str.lower() == line.lower()]
    if rows.empty:
        return None
    value = rows.iloc[0].get("%norm")
    try:
        number = float(value)
        return number if number == number else None
    except Exception:
        return None


def state_record(
    label: str,
    main_dss: Path,
    commands: list[str],
) -> tuple[dict[str, Any], gridguard.SnapshotResult]:
    started = time.perf_counter()
    snapshot = gridguard.compile_and_solve(
        label, str(CASE_DIR), str(main_dss), commands,
        gridguard.V_MIN_PU_DEFAULT, gridguard.V_MAX_PU_DEFAULT,
        recover_on_failure=False,
    )
    metrics = gridguard.summarize_metrics(
        snapshot, gridguard.V_MIN_PU_DEFAULT, gridguard.V_MAX_PU_DEFAULT
    )
    metrics["critical_recloser_loading_pct"] = line_loading(snapshot, CRITICAL_RECLOSER)
    metrics["elapsed_seconds"] = time.perf_counter() - started
    return metrics, snapshot


def method_policy(method: str) -> dict[str, bool]:
    if method == "no_action":
        return dict(llm=False, physics=False, memory=False, feedback=False, critic=False)
    if method == "random_screen":
        return dict(llm=True, physics=False, memory=False, feedback=False, critic=False)
    if method == "llm_no_memory":
        return dict(llm=True, physics=False, memory=False, feedback=False, critic=False)
    if method == "opro_no_critic":
        return dict(llm=True, physics=False, memory=True, feedback=True, critic=False)
    if method == "gridguard_llm":
        return dict(llm=True, physics=False, memory=True, feedback=True, critic=True)
    if method == "physics_seed":
        return dict(llm=False, physics=True, memory=True, feedback=True, critic=False)
    if method == "gridguard_hybrid":
        return dict(llm=True, physics=True, memory=True, feedback=True, critic=True)
    raise ValueError(method)


def make_policy(method: str, seed: int, k_candidates: int, model: str) -> Any:
    if method in {"no_action", "physics_seed"}:
        return NoopPolicy()
    if method == "random_screen":
        return RandomRestorationPolicy(seed, k_candidates)
    os.environ["OLLAMA_MODEL"] = model
    return gridguard.LLMClient(seed=seed)


def run_method(
    method: str,
    seed: int,
    main_dss: Path,
    output_dir: Path,
    fleet: list[str],
    security_reference: dict[str, Any],
    security_reference_snapshot: gridguard.SnapshotResult,
    outage_metrics: dict[str, Any],
    steps: int,
    k_candidates: int,
    model: str,
) -> dict[str, Any]:
    policy = method_policy(method)
    llm = make_policy(method, seed, k_candidates, model)
    gridguard.RUN_DIR = output_dir / "raw"
    gridguard.RUN_DIR.mkdir(parents=True, exist_ok=True)
    config = gridguard.GridGuardConfig(
        steps=steps,
        k_candidates=k_candidates,
        max_actions=2,
        llm_samples=1,
        explore_temp=0.65,
        guardrail_start_stuck=0,
        max_stuck=steps,
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
        extra_instruction=(
            f"Restore the isolated udt8894 service area. The faulted line {FAULT_LINE} is "
            f"quarantined. The approved alternate tie is {TIE_LINE}; coordinate pickup with "
            f"the allowlisted {FLEET_ID} macro when needed."
        ),
        enable_llm_candidates=policy["llm"],
        enable_physics_fallback=policy["physics"],
        enable_portfolio_seeds=False,
        enable_scored_memory=policy["memory"],
        enable_verifier_feedback=policy["feedback"],
        enable_critic=policy["critic"],
        allow_recovered_solve=False,
        certificate_mode="relative_safe_improvement",
        voltage_severity_tolerance_pu=1e-5,
        max_line_loading_tolerance_pct=0.10,
        thermal_severity_tolerance_pct_sum=0.50,
        restoration_tolerance_kw=0.10,
        max_physical_actions=500,
        storage_fleets={FLEET_ID: fleet},
        restoration_ties=[TIE_LINE],
        restoration_watch_lines=[CRITICAL_RECLOSER],
        restoration_probe_pct_kw=40.0,
        restoration_target_loading_pct=99.5,
    )
    label = f"TII-RESTORE-{method}-s{seed}"
    engine = gridguard.GridGuardEngine(
        llm=llm,
        translator=gridguard.ActionTranslator(),
        config=config,
        progress=lambda message: print(f"[{method}/s{seed}] {message}", flush=True),
        step_done=lambda _record: None,
    )
    started = time.perf_counter()
    final_state = engine.run({
        "case": {"label": label, "folder": str(CASE_DIR), "main_dss": str(main_dss)},
        "base_cmds": ["set controlmode=off", f"Open Line.{FAULT_LINE}"],
        "vmin": gridguard.V_MIN_PU_DEFAULT,
        "vmax": gridguard.V_MAX_PU_DEFAULT,
        "security_reference_metrics": security_reference,
        "security_reference_snapshot": security_reference_snapshot,
        "telemetry": {
            "source": "OpenDSS restoration benchmark",
            "trusted": True,
            "quarantined_devices": [f"line.{FAULT_LINE}"],
            "timestamp_mode": "offline_batch",
            "max_age_s": 300,
        },
    })
    elapsed = time.perf_counter() - started
    record_path = Path(final_state["run_path"])
    record = json.loads(record_path.read_text(encoding="utf-8"))
    final = record.get("final") or {}
    research = record.get("research_metrics") or {}
    history = (record.get("history") or [])[1:]
    ledger = record.get("candidate_evaluation_ledger") or []
    # Accepted actions persist in ``base_cmds`` across iterations, while each
    # history row records only the newly accepted supervisory bundle.  Scan the
    # complete accepted trajectory so the report does not lose the adaptive
    # fleet setpoint when a later PV/storage refinement is also certified.
    accepted_supervisory_actions = [
        action
        for item in history
        for action in (item.get("supervisory_actions") or [])
        if isinstance(action, dict)
    ]
    accepted_fleet_pct_kw = next((
        float(action["pct_kw"])
        for action in accepted_supervisory_actions
        if isinstance(action, dict)
        and action.get("type") == "storage_fleet_setpoint"
        and action.get("pct_kw") is not None
    ), None)
    accepted_watch_loading_pct = next((
        float(evidence["loading_pct"])
        for item in reversed(history)
        for evidence in (item.get("line_loading_evidence") or [])
        if isinstance(evidence, dict)
        and str(evidence.get("line", "")).lower() == CRITICAL_RECLOSER.lower()
        and evidence.get("loading_pct") is not None
    ), None)
    adaptive_history = [item for item in history if item.get("repair_derivation")]
    adaptive_watch_loading_pct = next((
        float(evidence["loading_pct"])
        for item in reversed(adaptive_history)
        for evidence in (item.get("line_loading_evidence") or [])
        if isinstance(evidence, dict)
        and str(evidence.get("line", "")).lower() == CRITICAL_RECLOSER.lower()
        and evidence.get("loading_pct") is not None
    ), None)
    adaptive_repair_records = [
        item for item in ledger if item.get("repair_derivation")
    ]
    candidate_metrics = [
        item.get("metrics") or {} for item in ledger
        if item.get("simulated") and item.get("metrics")
    ]
    best_restored = max(
        candidate_metrics,
        key=lambda item: float(item.get("served_load_kw", 0.0)),
        default={},
    )
    return {
        "method": method,
        "seed": seed,
        "elapsed_seconds": elapsed,
        "accepted_iterations": len(history),
        "run_success": bool(history),
        "certified_candidate_rate": research.get("certified_candidate_rate"),
        "certified_per_allocated_slot": research.get("certified_per_allocated_slot"),
        "candidate_slots_allocated": research.get("candidate_slots_allocated"),
        "simulated_candidates": research.get("candidate_bundles_simulated"),
        "pre_simulation_rejections": research.get("pre_simulation_rejection_count"),
        "unsafe_commits": research.get("unsafe_commit_count"),
        "llm_calls": research.get("llm_call_count"),
        "llm_prompt_tokens": research.get("llm_prompt_tokens"),
        "llm_output_tokens": research.get("llm_output_tokens"),
        "accepted_fleet_pct_kw": accepted_fleet_pct_kw,
        "accepted_critical_recloser_loading_pct": accepted_watch_loading_pct,
        "adaptive_repair_critical_recloser_loading_pct": adaptive_watch_loading_pct,
        "adaptive_repair_candidates_simulated": len(adaptive_repair_records),
        "adaptive_repair_accepted": bool(adaptive_history),
        "restored_load_kw": float(final.get("served_load_kw", 0.0))
        - float(outage_metrics.get("served_load_kw", 0.0)),
        "restored_load_pct": 100.0 * (
            float(final.get("served_load_kw", 0.0))
            - float(outage_metrics.get("served_load_kw", 0.0))
        ) / max(1e-9, float(security_reference.get("served_load_kw", 0.0))
            - float(outage_metrics.get("served_load_kw", 0.0))),
        "final_violating_buses": final.get("viol_buses"),
        "final_voltage_severity": final.get("v_severity"),
        "final_overloaded_lines": final.get("over_lines"),
        "final_thermal_severity": final.get("thermal_severity_pct_sum"),
        "final_max_line_pct": final.get("max_line_pct"),
        "final_losses_kw": final.get("losses_kw"),
        "best_evaluated_restored_load_kw": (
            float(best_restored.get("served_load_kw", 0.0))
            - float(outage_metrics.get("served_load_kw", 0.0))
            if best_restored else 0.0
        ),
        "rejection_taxonomy": research.get("rejection_taxonomy", {}),
        "record_path": str(record_path),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    flattened = []
    for row in rows:
        item = dict(row)
        for key, value in list(item.items()):
            if isinstance(value, (dict, list)):
                item[key] = json.dumps(value, sort_keys=True)
        flattened.append(item)
    fields = sorted({key for row in flattened for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(flattened)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output" / "tii_restoration_v1")
    parser.add_argument("--model", default=os.environ.get("OLLAMA_MODEL", "llama3.1:8b"))
    parser.add_argument("--seeds", default="101,202,303")
    parser.add_argument("--methods", default=",".join(METHODS))
    parser.add_argument("--steps", type=int, default=3)
    parser.add_argument("--k-candidates", type=int, default=5)
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    fleet = storage_names(STORAGE_FILE)
    overlay = build_overlay(SOURCE_MASTER)
    main_dss = Path(overlay["compatibility_master"])

    base_commands = ["set controlmode=off"]
    outage_commands = base_commands + [f"Open Line.{FAULT_LINE}"]
    blind_commands = outage_commands + [f"Edit Line.{TIE_LINE} enabled=yes"]
    fleet40_commands = blind_commands + [
        f"Edit Storage.{name} DispMode=EXTERNAL State=CHARGING %Charge=40"
        for name in fleet
    ]
    canonical: dict[str, dict[str, Any]] = {}
    pre_contingency_snapshot: gridguard.SnapshotResult | None = None
    for label, commands in (
        ("pre_contingency", base_commands),
        ("outage", outage_commands),
        ("blind_tie_close", blind_commands),
        ("tie_plus_fleet_40pct", fleet40_commands),
    ):
        metrics, snapshot = state_record(label, main_dss, commands)
        canonical[label] = metrics
        if label == "pre_contingency":
            pre_contingency_snapshot = snapshot
    if pre_contingency_snapshot is None:
        raise RuntimeError("Pre-contingency reference snapshot was not created")
    (output_dir / "canonical_states.json").write_text(
        json.dumps(canonical, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )

    methods = [item.strip() for item in args.methods.split(",") if item.strip()]
    unknown = sorted(set(methods) - set(METHODS))
    if unknown:
        raise SystemExit(f"Unknown methods: {unknown}")
    seeds = [int(item.strip()) for item in args.seeds.split(",") if item.strip()]
    if any(method not in {"no_action", "physics_seed", "random_screen"} for method in methods):
        warmup = warm_ollama_model(args.model)
    else:
        warmup = {"status": "not_required"}
    model_info = ollama_metadata(args.model)
    manifest = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "case": "SMART-DS Greensboro uhs20_1247 parent substation",
        "source_master": str(SOURCE_MASTER),
        "source_master_sha256": sha256(SOURCE_MASTER),
        "redirected_source_tree_sha256": overlay["redirected_source_tree_sha256"],
        "compatibility_master": str(main_dss),
        "compatibility_master_sha256": overlay["compatibility_master_sha256"],
        "gridguard_core_sha256": file_sha256(ROOT / "OPRO_Optimizer.py"),
        "runner_sha256": file_sha256(Path(__file__).resolve()),
        "fault_line": FAULT_LINE,
        "quarantined_fault": True,
        "alternate_tie": TIE_LINE,
        "fleet_id": FLEET_ID,
        "fleet_device_count": len(fleet),
        "fleet_membership_sha256": hashlib.sha256(
            json.dumps(sorted(name.lower() for name in fleet)).encode("utf-8")
        ).hexdigest(),
        "critical_recloser": CRITICAL_RECLOSER,
        "adaptive_restoration_repair": {
            "method": "same-state watch-line secant update",
            "initial_probe_pct_kw": 40.0,
            "target_loading_pct": 99.5,
            "watch_lines": [CRITICAL_RECLOSER],
            "candidate_budget_treatment": "Consumes one ordinary next-iteration candidate slot",
            "hidden_solver_calls": 0,
        },
        "methods": methods,
        "seeds": seeds,
        "budgets": {
            "iterations": args.steps,
            "candidate_slots_per_iteration": args.k_candidates,
            "supervisory_actions_per_candidate": 2,
            "physical_actions_per_candidate": 500,
        },
        "certificate": {
            "mode": "pre-contingency-relative safe improvement",
            "voltage_severity_tolerance_pu": 1e-5,
            "max_line_loading_tolerance_pct": 0.10,
            "thermal_severity_tolerance_pct_sum": 0.50,
            "restoration_tolerance_kw": 0.10,
        },
        "model": model_info,
        "model_warmup_excluded": warmup,
        "scope_note": "Software-in-the-loop static snapshot; not field actuation or absolute feasibility.",
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )

    rows: list[dict[str, Any]] = []
    deterministic = {"no_action", "physics_seed"}
    for seed_index, seed in enumerate(seeds):
        offset = seed_index % max(1, len(methods))
        ordered = methods[offset:] + methods[:offset]
        for method in ordered:
            if method in deterministic and seed_index > 0:
                continue
            print(f"[restoration] method={method} seed={seed}", flush=True)
            row = run_method(
                method, seed, main_dss, output_dir, fleet,
                canonical["pre_contingency"], pre_contingency_snapshot,
                canonical["outage"],
                args.steps, args.k_candidates, args.model,
            )
            rows.append(row)
            with (output_dir / "trials.jsonl").open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(row, allow_nan=False) + "\n")
    write_csv(output_dir / "trials.csv", rows)

    summary_rows = []
    for method in methods:
        items = [row for row in rows if row["method"] == method]
        if not items:
            continue
        restored = [float(row["restored_load_pct"]) for row in items]
        success = [1.0 if row["run_success"] else 0.0 for row in items]
        low, high = bootstrap_ci(success)
        summary_rows.append({
            "method": method,
            "n": len(items),
            "certified_run_rate": statistics.fmean(success),
            "certified_run_rate_ci95_low": low,
            "certified_run_rate_ci95_high": high,
            "restored_load_pct_mean": statistics.fmean(restored),
            "elapsed_seconds_mean": statistics.fmean(float(row["elapsed_seconds"]) for row in items),
            "unsafe_commits": sum(int(row["unsafe_commits"] or 0) for row in items),
        })
    write_csv(output_dir / "summary.csv", summary_rows)
    (output_dir / "summary.json").write_text(json.dumps({
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "trial_count": len(rows),
        "method_groups": summary_rows,
        "canonical_states": canonical,
    }, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "output_dir": str(output_dir),
        "trial_count": len(rows),
        "canonical_states": str(output_dir / "canonical_states.json"),
        "summary": str(output_dir / "summary.json"),
    }, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
