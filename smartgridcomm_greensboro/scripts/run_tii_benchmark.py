"""Run resumable, matched-budget GridGuard experiments for a TII study.

The default ``smoke`` profile is intentionally small.  ``poster`` runs three
representative Greensboro leaf feeders and three LLM seeds.  ``tii`` expands to
six feeders, three operating points, and ten seeds.  Every method receives the
same iteration, candidate, and per-candidate action caps; the ledger records the
actual number of simulations when malformed candidates are rejected early.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import platform
import random
import re
import statistics
import sys
import time
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np
import requests


ROOT = Path(__file__).resolve().parents[1]
SMARTDS_ROOT = ROOT / "SMARTDS_GSO_solar_extreme_batt_high_peak_opendss"
VENDORED_DEPS = ROOT / "tmp" / "gridguard_deps"
DEFAULT_OUTPUT = ROOT / "output" / "tii_experiments"
PROTOCOL_VERSION = "gridguard-tii-v2-2026-09-09"
sys.path.insert(0, str(VENDORED_DEPS))
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
os.environ.setdefault("GRIDGUARD_HEADLESS", "1")

import OPRO_Optimizer as gridguard  # noqa: E402
from build_smartds_feeder_compat import build_overlay  # noqa: E402


CASE_LIBRARY = {
    "tiny": "uhs19_1247/uhs19_1247--udt15839",
    "small": "uhs9_1247/uhs9_1247--udt13714",
    "medium": "uhs19_1247/uhs19_1247--udt19872",
    "undervoltage": "uhs4_1247/uhs4_1247--p1umv8",
    "mixed": "uhs9_1247/uhs9_1247--udt2508",
    "large_leaf": "uhs1_1247/uhs1_1247--udt20176",
}

METHODS = (
    "no_action",
    "random_screen",
    "llm_no_memory",
    "opro_no_critic",
    "gridguard_llm",
    "physics_seed",
    "gridguard_hybrid",
)


@dataclass(frozen=True)
class TrialSpec:
    case_name: str
    case_relative: str
    method: str
    seed: int
    load_mult: float
    steps: int
    k_candidates: int
    max_actions: int
    llm_samples: int
    model: str

    def key(self) -> str:
        payload = json.dumps({
            "protocol_version": PROTOCOL_VERSION,
            "gridguard_core_sha256": sha256_file(ROOT / "OPRO_Optimizer.py"),
            "benchmark_runner_sha256": sha256_file(Path(__file__).resolve()),
            "compatibility_builder_sha256": sha256_file(
                ROOT / "scripts" / "build_smartds_feeder_compat.py"
            ),
            "trial": asdict(self),
        }, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:20]


class NoopLLM:
    model = "deterministic-no-llm"
    seed = None
    candidate_source = "NONE"
    actor_type = "deterministic"

    def chat(self, **_kwargs: Any) -> str:
        return '{"candidates": []}'


class RandomPolicyLLM:
    """Seeded admissible random-search baseline using the prompt's exact examples."""

    model = "seeded-random-policy"
    candidate_source = "RANDOM"
    actor_type = "seeded_random"

    def __init__(self, seed: int, k_candidates: int, max_actions: int):
        self.seed = int(seed)
        self.rng = random.Random(seed)
        self.k_candidates = int(k_candidates)
        self.max_actions = int(max_actions)
        self.call_index = 0

    def _sample_action(
        self, allowed: list[str], pools: dict[str, Any], menu: dict[str, Any]
    ) -> dict[str, Any] | None:
        families = [
            family for family in allowed
            if family in {"der_setpoint", "storage_setpoint", "tap_step", "cap_state", "switch_line"}
        ]
        self.rng.shuffle(families)
        for family in families:
            if family == "der_setpoint" and pools.get("pvsystems"):
                return {
                    "type": family,
                    "device": f"PVSystem.{self.rng.choice(pools['pvsystems'])}",
                    "pct_pmpp": self.rng.choice(menu.get("pv_pct_pmpp") or [0, 20, 40, 60, 75, 90]),
                }
            if family == "storage_setpoint" and pools.get("storages"):
                state = self.rng.choice(["CHARGING", "DISCHARGING", "IDLING"])
                item: dict[str, Any] = {
                    "type": family, "storage": self.rng.choice(pools["storages"]), "state": state,
                }
                if state != "IDLING":
                    item["pct_kw"] = self.rng.choice(
                        menu.get("storage_pct_kw") or [20, 40, 60, 80, 100]
                    )
                return item
            if family == "tap_step" and pools.get("regcontrols"):
                return {
                    "type": family,
                    "regcontrol": self.rng.choice(pools["regcontrols"]),
                    "step": self.rng.choice(menu.get("tap_step") or [-4, -2, -1, 1, 2, 4]),
                }
            if family == "cap_state" and pools.get("capacitors"):
                return {
                    "type": family,
                    "cap": self.rng.choice(pools["capacitors"]),
                    "state": self.rng.choice(["(0)", "(1)"]),
                }
            if family == "switch_line" and pools.get("open_switches"):
                return {
                    "type": family, "line": self.rng.choice(pools["open_switches"]), "op": "close",
                }
        return None

    def chat(
        self,
        system: str,
        user_text: str,
        temperature: float,
        num_predict: int,
        timeout_s: int = 240,
        response_format: Any = None,
    ) -> str:
        del temperature, num_predict, timeout_s, response_format
        self.call_index += 1
        if "Constraint Critic Agent" in system:
            return json.dumps({
                "diagnosis": "Random baseline has no critic.",
                "avoid": [],
                "next_focus": [],
                "repair_instruction": "Continue seeded random search.",
            })
        match = re.search(r"<JSON>(.*?)</JSON>", user_text, flags=re.S)
        context = json.loads(match.group(1)) if match else {}
        schema = context.get("ACTION_SCHEMA") or {}
        allowed = list(schema.get("allowed_types") or [])
        pools = context.get("EXACT_TARGET_POOLS") or {}
        menu = context.get("SETPOINT_MENU") or {}
        if not allowed:
            return '{"candidates": []}'
        candidates = []
        for index in range(self.k_candidates):
            requested_bundle = self.rng.randint(1, max(1, self.max_actions))
            actions: list[dict[str, Any]] = []
            targets: set[str] = set()
            for _ in range(requested_bundle * 3):
                action = self._sample_action(allowed, pools, menu)
                if action is None:
                    break
                target = json.dumps(action, sort_keys=True).split(",", 1)[0] + str(
                    action.get("device") or action.get("storage") or action.get("regcontrol")
                    or action.get("cap") or action.get("line") or ""
                )
                if target in targets:
                    continue
                targets.add(target)
                actions.append(action)
                if len(actions) >= requested_bundle:
                    break
            if not actions:
                continue
            candidates.append({
                "name": f"random_{self.call_index}_{index}",
                "actions": actions,
                "reasoning": "Seeded random search over the same grounded action pool.",
            })
        return json.dumps({"candidates": candidates})


def parse_int_list(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def parse_float_list(value: str) -> list[float]:
    return [float(item.strip()) for item in value.split(",") if item.strip()]


def parse_str_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run matched-budget, resumable GridGuard TII experiments.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--profile", choices=("smoke", "poster", "tii"), default="smoke")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--model", default=os.environ.get("OLLAMA_MODEL", "llama3.1:8b"))
    parser.add_argument("--cases", default=None, help="Comma-separated CASE_LIBRARY names or paths")
    parser.add_argument("--methods", default=None, help="Comma-separated method names")
    parser.add_argument("--seeds", default=None, help="Comma-separated integer seeds")
    parser.add_argument("--load-mults", default=None, help="Comma-separated load multipliers")
    parser.add_argument("--steps", type=int, default=None)
    parser.add_argument("--k-candidates", type=int, default=None)
    parser.add_argument("--max-actions", type=int, default=None)
    parser.add_argument("--llm-samples", type=int, default=1)
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--limit", type=int, default=None, help="Stop after this many pending trials")
    return parser


def profile_defaults(profile: str) -> dict[str, Any]:
    if profile == "smoke":
        return {
            "cases": ["small"],
            "methods": ["random_screen", "llm_no_memory", "opro_no_critic", "gridguard_llm", "physics_seed", "gridguard_hybrid"],
            "seeds": [101],
            "load_mults": [1.0],
            "steps": 2,
            "k_candidates": 2,
            "max_actions": 4,
        }
    if profile == "poster":
        return {
            "cases": ["tiny", "small", "medium"],
            "methods": list(METHODS),
            "seeds": [101, 202, 303],
            "load_mults": [1.0],
            "steps": 3,
            "k_candidates": 2,
            "max_actions": 4,
        }
    return {
        "cases": list(CASE_LIBRARY),
        "methods": list(METHODS),
        "seeds": [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],
        "load_mults": [0.9, 1.0, 1.1],
        "steps": 5,
        "k_candidates": 3,
        "max_actions": 8,
    }


def resolve_case(value: str) -> tuple[str, str]:
    if value in CASE_LIBRARY:
        return value, CASE_LIBRARY[value]
    relative = value.replace("\\", "/").strip("/")
    path = SMARTDS_ROOT / Path(relative)
    if not (path / "Master.dss").is_file():
        raise FileNotFoundError(f"Unknown case '{value}' and no Master.dss at {path}")
    return path.name, relative


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def protocol_id() -> str:
    payload = {
        "version": PROTOCOL_VERSION,
        "gridguard_core_sha256": sha256_file(ROOT / "OPRO_Optimizer.py"),
        "benchmark_runner_sha256": sha256_file(Path(__file__).resolve()),
        "compatibility_builder_sha256": sha256_file(
            ROOT / "scripts" / "build_smartds_feeder_compat.py"
        ),
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:20]


def ollama_metadata(model: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {"requested_model": model}
    try:
        response = requests.get(
            os.environ.get("OLLAMA_URL", "http://localhost:11434").rstrip("/") + "/api/tags",
            timeout=5,
        )
        response.raise_for_status()
        models = response.json().get("models", [])
        chosen = next(
            (item for item in models if item.get("name") == model or item.get("model") == model),
            None,
        )
        if chosen:
            metadata.update({
                "resolved_name": chosen.get("name"),
                "digest": chosen.get("digest"),
                "size_bytes": chosen.get("size"),
                "details": chosen.get("details"),
            })
    except Exception as exc:
        metadata["query_error"] = f"{type(exc).__name__}: {exc}"
    return metadata


def warm_ollama_model(model: str) -> dict[str, Any]:
    """Load the model once so the first measured method does not pay cold-start cost."""
    started = time.perf_counter()
    try:
        response = requests.post(
            os.environ.get("OLLAMA_URL", "http://localhost:11434").rstrip("/") + "/api/chat",
            json={
                "model": model,
                "messages": [{"role": "user", "content": "Return the word ready."}],
                "stream": False,
                "keep_alive": "30m",
                "options": {"temperature": 0, "num_predict": 2, "seed": 1701},
            },
            timeout=240,
        )
        response.raise_for_status()
        data = response.json()
        return {
            "status": "ok",
            "elapsed_seconds": time.perf_counter() - started,
            "load_duration_ms": float(data.get("load_duration") or 0.0) / 1_000_000.0,
        }
    except Exception as exc:
        return {
            "status": "error",
            "elapsed_seconds": time.perf_counter() - started,
            "error": f"{type(exc).__name__}: {exc}",
        }


def method_config(method: str) -> dict[str, bool]:
    if method == "no_action":
        return dict(llm=False, physics=False, portfolio=False, memory=False, feedback=False, critic=False)
    if method == "random_screen":
        return dict(llm=True, physics=False, portfolio=False, memory=False, feedback=False, critic=False)
    if method == "llm_no_memory":
        return dict(llm=True, physics=False, portfolio=False, memory=False, feedback=False, critic=False)
    if method == "opro_no_critic":
        return dict(llm=True, physics=False, portfolio=False, memory=True, feedback=True, critic=False)
    if method == "gridguard_llm":
        return dict(llm=True, physics=False, portfolio=False, memory=True, feedback=True, critic=True)
    if method == "physics_seed":
        return dict(llm=False, physics=True, portfolio=True, memory=True, feedback=True, critic=False)
    if method == "gridguard_hybrid":
        return dict(llm=True, physics=True, portfolio=True, memory=True, feedback=True, critic=True)
    raise ValueError(f"Unsupported method: {method}")


def make_llm(spec: TrialSpec) -> Any:
    if spec.method in {"no_action", "physics_seed"}:
        return NoopLLM()
    if spec.method == "random_screen":
        return RandomPolicyLLM(spec.seed, spec.k_candidates, spec.max_actions)
    os.environ["OLLAMA_MODEL"] = spec.model
    return gridguard.LLMClient(seed=spec.seed)


def finite(value: Any) -> Any:
    if value is None or isinstance(value, (str, bool, int)):
        return value
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value)
    return number if math.isfinite(number) else None


def percent_relief(before: Any, after: Any) -> float | None:
    if before is None or after is None:
        return None
    base = float(before)
    candidate = float(after)
    if not math.isfinite(base) or not math.isfinite(candidate):
        return None
    if abs(base) <= 1e-12:
        return None
    return 100.0 * (base - candidate) / base


def trial_row(
    spec: TrialSpec,
    record: dict[str, Any],
    elapsed_s: float,
    overlay: dict[str, Any],
    raw_path: Path,
) -> dict[str, Any]:
    baseline = record.get("baseline") or {}
    final = record.get("final") or {}
    research = record.get("research_metrics") or {}
    ledger = record.get("candidate_evaluation_ledger") or []
    best_first = min(
        (float(item["obj"]) for item in ledger if item.get("obj") is not None and float(item["obj"]) < 1e29),
        default=None,
    )
    accepted = list((record.get("history") or [])[1:])
    return {
        "trial_key": spec.key(),
        "protocol_id": protocol_id(),
        "status": "complete",
        **asdict(spec),
        "elapsed_seconds": elapsed_s,
        "raw_record": str(raw_path),
        "source_master_sha256": overlay["source_master_sha256"],
        "compatibility_master_sha256": overlay["compatibility_master_sha256"],
        "compatibility_replacements": overlay["replacement_count"],
        "baseline": {key: finite(value) for key, value in baseline.items()},
        "final": {key: finite(value) for key, value in final.items()},
        "voltage_severity_relief_pct": percent_relief(baseline.get("v_severity"), final.get("v_severity")),
        "violating_bus_relief_pct": percent_relief(baseline.get("viol_buses"), final.get("viol_buses")),
        "overloaded_line_relief_pct": percent_relief(baseline.get("over_lines"), final.get("over_lines")),
        "thermal_severity_relief_pct": percent_relief(
            baseline.get("thermal_severity_pct_sum"), final.get("thermal_severity_pct_sum")
        ),
        "max_line_loading_relief_pct": percent_relief(
            baseline.get("max_line_pct"), final.get("max_line_pct")
        ),
        "loss_relief_pct": percent_relief(baseline.get("losses_kw"), final.get("losses_kw")),
        "served_load_gain_kw": float(final.get("served_load_kw", 0.0)) - float(baseline.get("served_load_kw", 0.0)),
        "objective_relief_pct": percent_relief(gridguard.objective(baseline), gridguard.objective(final)),
        "candidate_bundles": research.get("candidate_bundles_proposed", 0),
        "candidate_slots_allocated": research.get("candidate_slots_allocated", 0),
        "llm_candidate_objects_returned": research.get("llm_candidate_objects_returned", 0),
        "llm_parse_valid_candidates": research.get("llm_parse_valid_candidates", 0),
        "historical_duplicates_filtered": research.get("historical_duplicates_filtered", 0),
        "simulated_candidates": research.get("candidate_bundles_simulated", 0),
        "certified_candidates": sum(bool(item.get("certified")) for item in ledger),
        "certified_candidate_rate": research.get("certified_candidate_rate"),
        "certified_per_allocated_slot": research.get("certified_per_allocated_slot"),
        "simulated_per_allocated_slot": research.get("simulated_per_allocated_slot"),
        "accepted_iterations": len(accepted),
        "iterations_executed": research.get("iterations_executed"),
        "iterations_to_first_certified": research.get("iterations_to_first_certified_action"),
        "unsafe_commit_count": research.get("unsafe_commit_count", 0),
        "invalid_action_rejection_rate": research.get("invalid_action_rejection_rate"),
        "pre_simulation_rejection_rate": research.get("pre_simulation_rejection_rate"),
        "exact_readback_rate": research.get("post_solve_readback_rate"),
        "absolute_feasible": research.get("absolute_feasible_final_state"),
        "operating_goal_satisfied": research.get("operating_goal_satisfied"),
        "candidate_source_counts": research.get("candidate_source_counts", {}),
        "certified_source_counts": research.get("certified_source_counts", {}),
        "rejection_taxonomy": research.get("rejection_taxonomy", {}),
        "stage_latency_ms": research.get("stage_latency_ms", {}),
        "llm_call_count": research.get("llm_call_count", 0),
        "llm_calls_by_stream": research.get("llm_calls_by_stream", {}),
        "llm_prompt_tokens": research.get("llm_prompt_tokens", 0),
        "llm_output_tokens": research.get("llm_output_tokens", 0),
        "llm_total_duration_ms": research.get("llm_total_duration_ms", 0),
        "llm_load_duration_ms": research.get("llm_load_duration_ms", 0),
        "cumulative_accepted_device_actions": research.get(
            "cumulative_accepted_device_actions", 0
        ),
        "cumulative_accepted_control_effort": research.get(
            "cumulative_accepted_control_effort", 0
        ),
        "pv_curtailment_command_fraction_sum": research.get(
            "pv_curtailment_command_fraction_sum", 0
        ),
        "storage_dispatch_command_fraction_sum": research.get(
            "storage_dispatch_command_fraction_sum", 0
        ),
        "candidate_simulation_latency_ms": research.get(
            "candidate_simulation_latency_ms", []
        ),
        "candidate_evaluation_latency_ms": research.get(
            "candidate_evaluation_latency_ms", []
        ),
        "best_evaluated_objective": best_first,
    }


def append_jsonl(path: Path, item: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(item, allow_nan=False) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def flatten_trial(row: dict[str, Any]) -> dict[str, Any]:
    flat = {key: value for key, value in row.items() if not isinstance(value, dict)}
    for prefix in ("baseline", "final", "stage_latency_ms"):
        for key, value in (row.get(prefix) or {}).items():
            flat[f"{prefix}_{key}"] = value
    flat["candidate_source_counts"] = json.dumps(row.get("candidate_source_counts") or {}, sort_keys=True)
    flat["certified_source_counts"] = json.dumps(row.get("certified_source_counts") or {}, sort_keys=True)
    flat["llm_calls_by_stream"] = json.dumps(row.get("llm_calls_by_stream") or {}, sort_keys=True)
    flat["rejection_taxonomy"] = json.dumps(row.get("rejection_taxonomy") or {}, sort_keys=True)
    return flat


def bootstrap_ci(values: list[float], seed: int = 1701) -> tuple[float | None, float | None]:
    if not values:
        return None, None
    if len(values) == 1:
        return values[0], values[0]
    rng = np.random.default_rng(seed)
    data = np.asarray(values, dtype=float)
    means = np.mean(rng.choice(data, size=(4000, len(data)), replace=True), axis=1)
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def aggregate(trials_path: Path, output_dir: Path, active_protocol_id: str) -> dict[str, Any]:
    rows = [
        row for row in read_jsonl(trials_path)
        if row.get("status") == "complete" and row.get("protocol_id") == active_protocol_id
    ]
    flat_rows = [flatten_trial(row) for row in rows]
    trials_csv = output_dir / "trials.csv"
    if flat_rows:
        fields = sorted({key for row in flat_rows for key in row})
        with trials_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(flat_rows)

    grouped: dict[tuple[str, str, float], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(row["method"], row["case_name"], float(row["load_mult"]))].append(row)
    metrics = (
        "voltage_severity_relief_pct",
        "violating_bus_relief_pct",
        "overloaded_line_relief_pct",
        "thermal_severity_relief_pct",
        "max_line_loading_relief_pct",
        "loss_relief_pct",
        "objective_relief_pct",
        "elapsed_seconds",
        "certified_candidate_rate",
        "certified_per_allocated_slot",
        "simulated_per_allocated_slot",
        "invalid_action_rejection_rate",
        "pre_simulation_rejection_rate",
        "accepted_iterations",
        "cumulative_accepted_device_actions",
        "cumulative_accepted_control_effort",
        "llm_call_count",
        "llm_prompt_tokens",
        "llm_output_tokens",
        "llm_total_duration_ms",
        "llm_load_duration_ms",
    )
    summary_rows: list[dict[str, Any]] = []
    for (method, case_name, load_mult), items in sorted(grouped.items()):
        summary: dict[str, Any] = {
            "method": method,
            "case_name": case_name,
            "load_mult": load_mult,
            "n": len(items),
            "unsafe_commits": sum(int(item.get("unsafe_commit_count") or 0) for item in items),
            "absolute_feasible_runs": sum(bool(item.get("absolute_feasible")) for item in items),
            "runs_with_certified_action": sum(int(item.get("accepted_iterations") or 0) > 0 for item in items),
        }
        for metric in metrics:
            values = [float(item[metric]) for item in items if item.get(metric) is not None]
            if not values:
                continue
            low, high = bootstrap_ci(values)
            summary[f"{metric}_mean"] = statistics.fmean(values)
            summary[f"{metric}_median"] = statistics.median(values)
            summary[f"{metric}_min"] = min(values)
            summary[f"{metric}_max"] = max(values)
            summary[f"{metric}_ci95_low"] = low
            summary[f"{metric}_ci95_high"] = high
        summary_rows.append(summary)

    # Method-level uncertainty is computed across scenario means so the many
    # LLM seeds within one circuit/loading point are not mistaken for
    # independent utility systems.
    by_method: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_method[str(row["method"])].append(row)
    method_rows: list[dict[str, Any]] = []
    for method, items in sorted(by_method.items()):
        scenario_groups: dict[tuple[str, float], list[dict[str, Any]]] = defaultdict(list)
        for item in items:
            scenario_groups[(str(item["case_name"]), float(item["load_mult"]))].append(item)
        method_row: dict[str, Any] = {
            "method": method,
            "trial_n": len(items),
            "scenario_n": len(scenario_groups),
            "unsafe_commits": sum(int(item.get("unsafe_commit_count") or 0) for item in items),
            "runs_with_certified_action": sum(
                int(item.get("accepted_iterations") or 0) > 0 for item in items
            ),
        }
        for metric in metrics:
            scenario_means = []
            for scenario_items in scenario_groups.values():
                values = [
                    float(item[metric]) for item in scenario_items
                    if item.get(metric) is not None
                ]
                if values:
                    scenario_means.append(statistics.fmean(values))
            if not scenario_means:
                continue
            low, high = bootstrap_ci(scenario_means)
            method_row[f"{metric}_scenario_mean"] = statistics.fmean(scenario_means)
            method_row[f"{metric}_scenario_median"] = statistics.median(scenario_means)
            method_row[f"{metric}_scenario_ci95_low"] = low
            method_row[f"{metric}_scenario_ci95_high"] = high
        method_rows.append(method_row)

    summary_csv = output_dir / "summary.csv"
    if summary_rows:
        fields = sorted({key for row in summary_rows for key in row})
        with summary_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(summary_rows)
    method_summary_csv = output_dir / "summary_by_method.csv"
    if method_rows:
        fields = sorted({key for row in method_rows for key in row})
        with method_summary_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(method_rows)
    payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_id": active_protocol_id,
        "trial_count": len(rows),
        "method_case_scenario_groups": summary_rows,
        "method_groups": method_rows,
        "bootstrap": "4000 resamples of trial means; deterministic seed 1701",
        "uncertainty_note": (
            "Per-scenario intervals resample LLM/random seeds. Method-level intervals resample "
            "case-by-load scenario means, preventing repeated seeds from being counted as independent grids."
        ),
        "scope_note": (
            "Leaf feeders are independently compiled components of the supplied Greensboro export. "
            "These are repeated software-in-the-loop trials, not independent utility field systems."
        ),
    }
    (output_dir / "summary.json").write_text(
        json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    return payload


def candidate_rows(spec: TrialSpec, record: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for index, item in enumerate(record.get("candidate_evaluation_ledger") or []):
        yield {
            "trial_key": spec.key(),
            "case_name": spec.case_name,
            "method": spec.method,
            "seed": spec.seed,
            "load_mult": spec.load_mult,
            "ledger_index": index,
            **item,
        }


def run_trial(spec: TrialSpec, output_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    case_dir = (SMARTDS_ROOT / Path(spec.case_relative)).resolve()
    source_master = case_dir / "Master.dss"
    overlay = build_overlay(source_master)
    main_dss = Path(overlay["compatibility_master"])
    raw_dir = output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    gridguard.RUN_DIR = raw_dir

    policy = method_config(spec.method)
    config = gridguard.GridGuardConfig(
        steps=spec.steps,
        k_candidates=spec.k_candidates,
        max_actions=spec.max_actions,
        llm_samples=spec.llm_samples,
        explore_temp=0.60,
        guardrail_start_stuck=0,
        max_stuck=spec.steps,
        allow_switch=False,
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
            "This is a matched-budget benchmark. Propose only existing-device controls, "
            "use exact catalog names, and use measured voltage/thermal evidence."
        ),
        enable_llm_candidates=policy["llm"],
        enable_physics_fallback=policy["physics"],
        enable_portfolio_seeds=policy["portfolio"],
        enable_scored_memory=policy["memory"],
        enable_verifier_feedback=policy["feedback"],
        enable_critic=policy["critic"],
        allow_recovered_solve=False,
        certificate_mode="relative_safe_improvement",
        max_physical_actions=spec.max_actions,
    )
    llm = make_llm(spec)
    label = re.sub(
        r"[^A-Za-z0-9_.-]+",
        "_",
        f"TII-{spec.case_name}-{spec.method}-s{spec.seed}-lm{spec.load_mult:g}",
    )
    base_commands = [
        f"set loadmult={spec.load_mult:.6f}",
        "set controlmode=off",
    ]
    engine = gridguard.GridGuardEngine(
        llm=llm,
        translator=gridguard.ActionTranslator(),
        config=config,
        progress=lambda message: print(f"[{spec.key()}] {message}", flush=True),
        step_done=lambda _record: None,
    )
    started = time.perf_counter()
    final_state = engine.run({
        "case": {"label": label, "folder": str(case_dir), "main_dss": str(main_dss)},
        "base_cmds": base_commands,
        "vmin": gridguard.V_MIN_PU_DEFAULT,
        "vmax": gridguard.V_MAX_PU_DEFAULT,
    })
    elapsed_s = time.perf_counter() - started
    raw_path = Path(final_state["run_path"])
    record = json.loads(raw_path.read_text(encoding="utf-8"))
    record["benchmark_trial"] = {
        **asdict(spec),
        "trial_key": spec.key(),
        "elapsed_seconds": elapsed_s,
        "base_commands": base_commands,
        "overlay_manifest": overlay["manifest"],
        "code_sha256": sha256_file(ROOT / "OPRO_Optimizer.py"),
    }
    enriched_path = raw_dir / f"{spec.key()}_{label}.json"
    enriched_path.write_text(json.dumps(record, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    row = trial_row(spec, record, elapsed_s, overlay, enriched_path)
    return row, record


def build_specs(args: argparse.Namespace) -> list[TrialSpec]:
    defaults = profile_defaults(args.profile)
    cases = parse_str_list(args.cases) if args.cases else defaults["cases"]
    methods = parse_str_list(args.methods) if args.methods else defaults["methods"]
    seeds = parse_int_list(args.seeds) if args.seeds else defaults["seeds"]
    load_mults = parse_float_list(args.load_mults) if args.load_mults else defaults["load_mults"]
    unknown_methods = sorted(set(methods) - set(METHODS))
    if unknown_methods:
        raise SystemExit(f"Unknown methods: {', '.join(unknown_methods)}")
    resolved_cases = [resolve_case(value) for value in cases]
    steps = args.steps or defaults["steps"]
    k_candidates = args.k_candidates or defaults["k_candidates"]
    max_actions = args.max_actions or defaults["max_actions"]
    if min(steps, k_candidates, max_actions, args.llm_samples) < 1:
        raise SystemExit("All budget values must be positive")
    specs: list[TrialSpec] = []
    deterministic_methods = {"no_action", "physics_seed"}
    for case_name, relative in resolved_cases:
        for load_mult in load_mults:
            for seed_index, seed in enumerate(seeds):
                # Rotate method order by seed to counterbalance any residual
                # thermal/cache drift after the explicit model warm-up.
                offset = seed_index % max(1, len(methods))
                ordered_methods = methods[offset:] + methods[:offset]
                for method in ordered_methods:
                    if method in deterministic_methods and seed_index > 0:
                        continue
                    specs.append(TrialSpec(
                        case_name=case_name,
                        case_relative=relative,
                        method=method,
                        seed=seed,
                        load_mult=load_mult,
                        steps=steps,
                        k_candidates=k_candidates,
                        max_actions=max_actions,
                        llm_samples=args.llm_samples,
                        model=args.model,
                    ))
    return specs


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    trials_path = output_dir / "trials.jsonl"
    candidates_path = output_dir / "candidates.jsonl"
    manifest_path = output_dir / "manifest.json"
    active_protocol_id = protocol_id()
    prior_manifest: dict[str, Any] = {}
    if args.no_resume and trials_path.is_file() and trials_path.stat().st_size > 0:
        raise SystemExit(
            "--no-resume would append duplicate trials. Use a fresh --output-dir instead."
        )
    if manifest_path.is_file() and trials_path.is_file() and trials_path.stat().st_size > 0:
        prior_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if prior_manifest.get("protocol_id") != active_protocol_id:
            raise SystemExit(
                "Output directory contains a different code/protocol fingerprint; "
                "use a fresh --output-dir to avoid mixing evidence."
            )
    specs = build_specs(args)
    completed = {
        row.get("trial_key") for row in read_jsonl(trials_path)
        if row.get("status") == "complete" and row.get("protocol_id") == active_protocol_id
    } if not args.no_resume else set()
    pending = [spec for spec in specs if spec.key() not in completed]
    if args.limit is not None:
        pending = pending[:max(0, args.limit)]

    model_metadata = ollama_metadata(args.model)
    if prior_manifest:
        prior_digest = (prior_manifest.get("ollama") or {}).get("digest")
        current_digest = model_metadata.get("digest")
        if prior_digest and current_digest and prior_digest != current_digest:
            raise SystemExit(
                "The resolved Ollama model digest changed; use a fresh --output-dir "
                "to keep model versions separate."
            )
    llm_methods = {"random_screen", "llm_no_memory", "opro_no_critic", "gridguard_llm", "gridguard_hybrid"}
    should_warm = any(spec.method in llm_methods - {"random_screen"} for spec in pending)
    warmup = warm_ollama_model(args.model) if should_warm else {"status": "not_required"}
    manifest = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_version": PROTOCOL_VERSION,
        "protocol_id": active_protocol_id,
        "profile": args.profile,
        "requested_trials": len(specs),
        "pending_trials_this_invocation": len(pending),
        "methods": sorted({spec.method for spec in specs}),
        "cases": sorted({spec.case_name: spec.case_relative for spec in specs}.items()),
        "seeds": sorted({spec.seed for spec in specs}),
        "load_multipliers": sorted({spec.load_mult for spec in specs}),
        "budget": sorted({(spec.steps, spec.k_candidates, spec.max_actions) for spec in specs}),
        "certificate_mode": "relative_safe_improvement",
        "solver_policy": ["set controlmode=off", "automatic recovery forbidden"],
        "python": platform.python_version(),
        "python_executable": sys.executable,
        "opendssdirect": getattr(gridguard.dss, "__version__", "unknown"),
        "code_sha256": sha256_file(ROOT / "OPRO_Optimizer.py"),
        "benchmark_runner_sha256": sha256_file(Path(__file__).resolve()),
        "compatibility_builder_sha256": sha256_file(
            ROOT / "scripts" / "build_smartds_feeder_compat.py"
        ),
        "ollama": model_metadata,
        "model_warmup_excluded_from_trial_latency": warmup,
        "method_order": "rotated by seed index after one excluded model warm-up",
        "deterministic_seed_handling": (
            "no_action and physics_seed run once per case-load scenario; repeated LLM/random seeds "
            "are not counted as independent deterministic replicates"
        ),
        "scientific_scope": [
            "Same-source Greensboro leaf feeders are multiple circuits, not independent utilities.",
            "Candidate certification is relative safe improvement unless absolute_feasible is separately true.",
            "No field actuation or hardware-in-the-loop validation is performed.",
        ],
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"manifest": str(manifest_path), "pending": len(pending)}, indent=2), flush=True)

    for index, spec in enumerate(pending, start=1):
        print(
            f"[trial {index}/{len(pending)}] {spec.case_name} {spec.method} "
            f"seed={spec.seed} loadmult={spec.load_mult}",
            flush=True,
        )
        try:
            row, record = run_trial(spec, output_dir)
            append_jsonl(trials_path, row)
            for candidate in candidate_rows(spec, record):
                append_jsonl(candidates_path, candidate)
            print(json.dumps({
                "trial_key": spec.key(),
                "method": spec.method,
                "accepted_iterations": row["accepted_iterations"],
                "voltage_severity_relief_pct": row["voltage_severity_relief_pct"],
                "overloaded_line_relief_pct": row["overloaded_line_relief_pct"],
                "elapsed_seconds": row["elapsed_seconds"],
            }), flush=True)
        except Exception as exc:
            error_row = {
                "trial_key": spec.key(),
                "protocol_id": active_protocol_id,
                "status": "error",
                **asdict(spec),
                "error": f"{type(exc).__name__}: {exc}",
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            }
            append_jsonl(trials_path, error_row)
            print(json.dumps(error_row), flush=True)

    summary = aggregate(trials_path, output_dir, active_protocol_id)
    print(json.dumps({
        "trials_jsonl": str(trials_path),
        "candidates_jsonl": str(candidates_path),
        "summary_csv": str(output_dir / "summary.csv"),
        "summary_by_method_csv": str(output_dir / "summary_by_method.csv"),
        "completed_trials": summary["trial_count"],
    }, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
