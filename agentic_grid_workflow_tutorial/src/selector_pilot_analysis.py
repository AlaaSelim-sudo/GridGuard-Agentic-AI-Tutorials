"""Frozen-protocol analysis of the small, actual multi-LLM voltage pilot.

Counterfactuals were collected in simulation. During bandit training this
module reads only the outcome of the selected operation, after selection.
This is controlled simulator replay, not deployment logging or a proof of
causal/off-policy evaluation from observational data. No test rewards update
the selector. All saved existing tutorial studies remain unchanged.
"""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math
import time

import numpy as np

from .response_selector import (LinUCB, canonicalize_responses, context_vector,
                                majority_select, uniform_select)

ROOT = Path(__file__).resolve().parents[1]
OPERATIONS = ("INCREASE_PV_0025", "RELAX_Q_10_PERCENT", "DECREASE_PV_0025", "KEEP_INCUMBENT")
SEEDS = (270927, 270928, 270929, 270930, 270931)


def _read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write(path, value):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, allow_nan=False), encoding="utf-8")


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()


def _verify_collection(output):
    """Check recorded provenance before using results; hashes are not signatures."""
    output = Path(output)
    protocol = _read(output / "protocol.json")
    unsigned = deepcopy(protocol)
    digest = unsigned.pop("protocol_hash")
    if _canonical_hash(unsigned) != digest:
        raise ValueError("Collection protocol self-hash mismatch")
    manifest = _read(output / "collection_manifest.json")
    if manifest["protocol_hash"] != digest:
        raise ValueError("Collection manifest belongs to another protocol")
    for relative, expected in manifest["files"].items():
        target = (output / relative).resolve()
        if not target.is_relative_to(output.resolve()) or _sha(target) != expected:
            raise ValueError("Collection file/hash mismatch: " + relative)
    if "source_hashes" in protocol:
        for relative, expected in protocol["source_hashes"].items():
            if _sha(ROOT / relative) != expected:
                raise ValueError("Original numerical source identity changed: " + relative)
    else:
        if _sha(ROOT / "src/ensemble_voltage_ac.py") != protocol["source_sha256"]:
            raise ValueError("AC collection source changed")
        if _sha(ROOT / "src/ensemble_voltage.py") != protocol["base_source_sha256"]:
            raise ValueError("AC collector's recorded base source changed")
        parent = output.parent
        if _read(parent / "protocol.json")["protocol_hash"] != protocol["parent_protocol_hash"]:
            raise ValueError("AC transfer parent protocol changed")
        for relative, expected in protocol["parent_files"].items():
            if _sha(parent / relative) != expected:
                raise ValueError("AC transfer parent evidence changed: " + relative)
    return {"protocol_hash": digest, "manifest_sha256": _sha(output / "collection_manifest.json"),
            "manifest_files_checked": len(manifest["files"])}


def _validate_evaluation(context, evaluation, backend, expected_control=None):
    candidate = evaluation["candidate"]
    control = candidate["control"]
    if (not isinstance(control, list) or len(control) != 2
            or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in control)):
        raise ValueError("Invalid finite control identity")
    expected = _canonical_hash({"case": context["case"], "candidate": candidate, "backend": backend})
    if evaluation["candidate_hash"] != expected or evaluation["backend"] != backend:
        raise ValueError("Candidate/case/backend identity mismatch")
    if expected_control is not None and control != expected_control:
        raise ValueError("Numerical evidence belongs to a different selected control")
    if type(evaluation["feasible"]) is not bool or bool(evaluation["failures"]) == evaluation["feasible"]:
        raise ValueError("Numerical feasibility and failures disagree")
    if evaluation["feasible"] and (isinstance(evaluation["score"], bool)
            or not isinstance(evaluation["score"], (int, float)) or not math.isfinite(evaluation["score"])):
        raise ValueError("Feasible evaluation needs a finite objective")
    if "evidence" in evaluation:
        evidence = evaluation["evidence"]
        if _canonical_hash(evidence) != evaluation["evidence_hash"]:
            raise ValueError("Numerical evidence hash mismatch")
        if evidence and (evidence.get("control") != control or evidence.get("backend") != backend):
            raise ValueError("Numerical evidence control/backend mismatch")


def freeze_analysis_protocol(output):
    """Call before training/evaluation; no trial-outcome file is opened here."""
    output = Path(output)
    data_protocol = _read(output / "protocol.json")
    sources = {name: _sha(ROOT / "src" / name)
               for name in ("response_selector.py", "selector_pilot_analysis.py")}
    path = output / "selector_analysis_protocol.json"
    if path.exists():
        record = _read(path)
        if record["sources"] != sources or record["dataset_protocol_hash"] != data_protocol["protocol_hash"]:
            raise ValueError("Frozen selector analysis sources or dataset protocol changed")
        return record
    train_ids = [row["id"] for row in data_protocol["scenarios"] if row["split"] == "train"]
    record = {"schema": "selector_analysis_protocol_v1",
        "frozen_utc": datetime.now(timezone.utc).isoformat(),
        "dataset_protocol_hash": data_protocol["protocol_hash"], "sources": sources,
        "operation_ids": list(OPERATIONS), "algorithm": "Linear contextual-action LinUCB",
        "alpha": 0.5, "regularization": 1.0, "primary_seed": SEEDS[0], "training_seeds": list(SEEDS),
        "training_orders": {str(seed): np.random.default_rng(seed).permutation(train_ids).tolist() for seed in SEEDS},
        "training": "One pass per training seed; one revealed chosen outcome/update per eligible training context",
        "validation": "Report frozen-policy validation; no hyperparameter or checkpoint selection",
        "test": "Frozen greedy predicted-reward selector; no exploration bonus and no updates",
        "reward": {"improvement_scale": 0.01, "simulation_trial_penalty": 0.01,
                   "rejection_penalty": 1.0,
                   "feasible": "clip(max(0,J_inc-J_trial)/0.01,0,1)-0.01",
                   "rejected": "-1.0-0.01",
                   "scope": "Planning-model objective and gate only; AC audit is excluded"},
        "fixed_numerical_operation": "INCREASE_PV_0025",
        "uniform_primary_seed": 91127,
        "uniform_sensitivity_seeds": [91127, 91128, 91129, 91130, 91131],
        "majority_tie_rule": "Lexicographically smallest canonical SHA-256 operation ID",
        "voting_terminology": "Most-voted (plurality) operation; a three-way tie has no strict majority",
        "best_of_all": "Extra-budget audit reference over all unique actual response actions",
        "latency": "Accounted serial components, not measured online end-to-end deployment latency",
        "claims": "Small illustrative single-feeder pilot; no promised learned or language-model advantage"}
    _write(path, record)
    return record


def _public_responses(rows):
    # Numeric outcomes, latency and offline audits never enter canonical voting.
    return [{key: row[key] for key in ("model_id", "operation_id", "reason")} for row in rows]


def _load_decisions(output, expected_splits=None):
    """Open only inputs known before a response's numerical trial."""
    output = Path(output)
    contexts, responses = _read(output / "contexts.json"), _read(output / "responses.json")
    identities = [row["id"] for row in contexts]
    if len(set(identities)) != len(identities):
        raise ValueError("Duplicate physical context identity across splits")
    if expected_splits and Counter(row["split"] for row in contexts) != Counter(expected_splits):
        raise ValueError("The expected complete scenario splits are not available")
    by_context = {key: [] for key in identities}
    seen = set()
    for row in responses:
        pair = (row["context_id"], row["model_id"])
        if pair in seen or row["context_id"] not in by_context:
            raise ValueError("Duplicate or unidentified model response")
        seen.add(pair)
        by_context[row["context_id"]].append(row)
    for context in contexts:
        if context["status"] == "READY":
            unsigned = deepcopy(context)
            context_hash = unsigned.pop("context_hash")
            if _canonical_hash(unsigned) != context_hash:
                raise ValueError("Pretrial context self-hash mismatch")
            context_vector(context["pretrial_features"])
            _validate_evaluation(context, context["incumbent"], context["pretrial_features"]["planning_backend"])
            rows = by_context[context["id"]]
            if len(rows) != 3:
                raise ValueError("Wait for all three actual model call records, including failures")
            if any(row.get("context_hash") != context["context_hash"] for row in rows):
                raise ValueError("Response belongs to a different numerical context")
            if set(context["catalog"]) != set(OPERATIONS):
                raise ValueError("The frozen operation catalog changed")
    return contexts, by_context


class SelectedFeedback:
    """Read one selected trial after the caller has made a decision.

    Full-information files exist on disk for comparison, but this interface
    records every feedback access so the training trace can be audited.
    """
    def __init__(self, output):
        self.output, self.access_log = Path(output), []

    def reveal(self, context, operation_id):
        if operation_id not in context["catalog"]:
            raise ValueError("Selected operation is outside the fixed catalog")
        path = self.output / "counterfactuals" / f"{context['id']}_{operation_id}.json"
        record = _read(path)
        trial = record["planning_model_trial"]
        if record["context_id"] != context["id"] or record["operation_id"] != operation_id:
            raise ValueError("Selected feedback identity mismatch")
        if trial["candidate"]["control"] != context["catalog"][operation_id]["parameters"]["control"]:
            raise ValueError("Feedback control does not match the chosen operation")
        _validate_evaluation(context, trial, context["pretrial_features"]["planning_backend"],
                             context["catalog"][operation_id]["parameters"]["control"])
        if trial["backend"] != context["pretrial_features"]["planning_backend"]:
            raise ValueError("Feedback uses a different planning backend")
        if type(trial["feasible"]) is not bool or bool(trial["failures"]) == trial["feasible"]:
            raise ValueError("Feedback feasibility and numerical gate disagree")
        if trial["feasible"] and (isinstance(trial["score"], bool) or not isinstance(trial["score"], (int, float))
                                  or not math.isfinite(trial["score"])):
            raise ValueError("Feasible trial needs a finite numerical score")
        self.access_log.append({"context_id": context["id"], "operation_id": operation_id,
                                "file": str(path.relative_to(self.output)), "sha256": _sha(path)})
        # The online reward interface intentionally omits independent AC audits.
        return deepcopy(trial)


def reward_from_selected_feedback(context, trial, protocol):
    if not trial["feasible"]:
        return -protocol["reward"]["rejection_penalty"] - protocol["reward"]["simulation_trial_penalty"]
    improvement = max(0.0, context["incumbent"]["score"] - trial["score"])
    return min(1.0, improvement / protocol["reward"]["improvement_scale"]) - protocol["reward"]["simulation_trial_penalty"]


def _train(output, contexts, response_rows, protocol):
    by_id = {row["id"]: row for row in contexts}
    histories, models = [], {}
    for seed in protocol["training_seeds"]:
        policy = LinUCB(protocol["operation_ids"], protocol["alpha"], protocol["regularization"])
        oracle = SelectedFeedback(output)
        records = []
        for identifier in protocol["training_orders"][str(seed)]:
            context = by_id[identifier]
            if context["split"] != "train":
                raise ValueError("A non-training context entered the update loop")
            if context["status"] != "READY":
                records.append({"context_id": identifier, "status": "SKIP_REVIEW"})
                continue
            pool = canonicalize_responses(_public_responses(response_rows[identifier]), context["catalog"])
            if not pool["candidates"]:
                records.append({"context_id": identifier, "status": "SKIP_NO_VALID_RESPONSES"})
                continue
            selected = policy.select(context["pretrial_features"], pool["candidates"])
            # No trial outcome is read before the line above.
            trial = oracle.reveal(context, selected.operation_id)
            reward = reward_from_selected_feedback(context, trial, protocol)
            policy.update(selected, reward)
            records.append({"context_id": identifier, "status": "UPDATED", "decision_id": selected.decision_id,
                "candidate_id": selected.candidate_id, "operation_id": selected.operation_id,
                "prediction_before_feedback": selected.predicted_reward,
                "uncertainty_before_feedback": selected.uncertainty, "selected_reward": reward,
                "selected_trial_feasible": trial["feasible"], "selected_trial_score": trial["score"],
                "incumbent_score": context["incumbent"]["score"], "updates_after": policy.updates})
        policy.freeze()
        checkpoint = Path(output) / "selector_models" / f"linucb_seed_{seed}.json"
        policy.save(checkpoint)
        if len(oracle.access_log) != policy.updates:
            raise AssertionError("Training used more feedback than selected updates")
        if any(access["context_id"] != row["context_id"] or access["operation_id"] != row["operation_id"]
               for access, row in zip(oracle.access_log, (row for row in records if row["status"] == "UPDATED"))):
            raise AssertionError("Training feedback was not restricted to selected decisions")
        histories.append({"seed": seed, "updates": policy.updates, "frozen": policy.frozen,
            "checkpoint": str(checkpoint.relative_to(output)), "checkpoint_sha256": _sha(checkpoint),
            "records": records, "selected_feedback_accesses": oracle.access_log})
        models[seed] = policy
    return models, histories


def _chosen(pool, candidate_id):
    return next(row for row in pool["candidates"] if row["candidate_id"] == candidate_id)


def _mean(values):
    values = [value for value in values if value is not None]
    return float(np.mean(values)) if values else None


def _final_lookup(output, contexts):
    rows = _read(Path(output) / "final_rechecks.json")
    if isinstance(rows, dict):
        rows = rows["rows"]
    lookup = {}
    by_id = {row["id"]: row for row in contexts}
    for row in rows:
        key = (row["context_id"], row["operation_id"])
        if key in lookup:
            raise ValueError("Duplicate final recheck identity")
        context = by_id[row["context_id"]]
        full = _read(Path(output) / row["record"])
        final = full["final_recheck"]
        _validate_evaluation(context, final, context["pretrial_features"]["planning_backend"])
        for field in ("feasible", "candidate", "candidate_hash", "evidence_hash", "score", "failures", "seconds"):
            if row[field] != final[field]:
                raise ValueError("Final summary and full evidence disagree")
        if row["final_ac_audit"] != full["final_ac_audit"]:
            raise ValueError("Final AC audit linkage changed")
        if row["final_ac_audit"] is not None:
            audit = row["final_ac_audit"]
            if _sha(Path(output) / audit["record"]) != audit["record_sha256"]:
                raise ValueError("Final AC audit file changed")
            _validate_evaluation(context, audit["result"], "opendss", row["candidate"]["control"])
        lookup[key] = row
    return lookup


def _recheck_parts(record):
    """MV has an exact-control AC audit; AC transfer is already freshly AC checked."""
    return record, record["final_ac_audit"]["result"] if record["final_ac_audit"] is not None else record


def _preparation_seconds(numerical):
    if "planning_and_initial_seconds" in numerical:
        return numerical["planning_and_initial_seconds"], 0.0
    # Transfer reuses an already executed AC plan. Report its recorded original
    # cost separately; do not count it as a new live execution in this replay.
    return sum(row["seconds"] for row in numerical["initial_evaluations"]), numerical["planning_seconds_reused"]


def _selection_row(output, context, responses, pool, method, operation, protocol, rechecks,
                   decision_seconds=0.0, seed=None, evaluated_operations=None, no_llm=False,
                   retain_without_trial=False, selection_failure=None):
    oracle = SelectedFeedback(output)
    trials = [] if retain_without_trial else [(key, oracle.reveal(context, key))
                                              for key in (evaluated_operations or [operation])]
    trial = context["incumbent"] if retain_without_trial else next(row for key, row in trials if key == operation)
    final_record = rechecks[(context["id"], operation)]
    final, ac = _recheck_parts(final_record)
    if not isinstance(final["feasible"], bool) or not isinstance(ac["feasible"], bool):
        raise ValueError("Final feasibility must be an actual gate Boolean")
    expected = trial if trial["feasible"] and trial["score"] < context["incumbent"]["score"] else context["incumbent"]
    if final["candidate"]["control"] != expected["candidate"]["control"]:
        raise ValueError("Final recheck did not retain the minimum feasible tested action")
    numerical = _read(Path(output) / context["numerical_record"])
    preparation, reused_planning = _preparation_seconds(numerical)
    language = 0.0 if no_llm else sum(row["seconds"] for row in responses)
    simulation = sum(row["seconds"] for _, row in trials)
    selected = next((row for row in pool["candidates"] if operation in row["operation_ids"]), None)
    score = final["score"] if final["feasible"] else None
    return {"context_id": context["id"], "split": context["split"],
        "backend": context["pretrial_features"]["planning_backend"], "method": method, "seed": seed,
        "operation_id": operation, "canonical_candidate_id": selected["candidate_id"] if selected else None,
        "pool_unique_operations": len(pool["candidates"]), "valid_responses": pool["valid_responses"],
        "selected_votes": selected["vote_count"] if selected else 0,
        "selection_failure": selection_failure,
        "trial_feasible": trial["feasible"], "trial_score": trial["score"], "trial_failures": trial["failures"],
        "incumbent_score": context["incumbent"]["score"], "final_score": score,
        "objective_improvement": context["incumbent"]["score"] - score if score is not None else None,
        "final_model_feasible": final["feasible"], "final_model_failures": final["failures"],
        "final_ac_feasible": ac["feasible"], "final_ac_failures": ac["failures"],
        "final_control": final["candidate"]["control"],
        "final_candidate_hash": final["candidate_hash"], "final_evidence_hash": final["evidence_hash"],
        "independent_ac_audit_seconds": ac["seconds"] if final_record["final_ac_audit"] is not None else 0.0,
        "ac_audit_kind": "Separate previously collected exact-control AC audit" if final_record["final_ac_audit"] is not None
                         else "Selected-model final check is already OpenDSS; no additional independent AC solve",
        "refinement_trials": len(trials), "response_calls_accounted": 0 if no_llm else len(responses),
        "planning_and_initial_seconds": preparation, "response_pool_serial_seconds": language,
        "recorded_planning_seconds_reused": reused_planning,
        "selected_trial_seconds": simulation, "final_recheck_seconds": final["seconds"],
        "selector_seconds": decision_seconds,
        "accounted_serial_seconds_excluding_ac_audit": preparation + language + simulation + final["seconds"] + decision_seconds,
        "timing_scope": "Sum of observed component times in simulator replay; model calls were collected in model batches",
        "scope": "Final planning-model gate; separate AC audit does not secretly change its decision",
        "budget_label": "Fixed response from the shared three-call pool" if method.startswith("fixed_pool_response:")
                        else "One selected trial, plus a distinct final recheck" if not evaluated_operations
                        else "Full pool evaluation; additional trial budget",
        "operator_acknowledged": False, "dispatch_authorized": False}


def _initial_row(output, context, responses, method, initial, initial_audits):
    audit = initial_audits[(context["id"], initial["candidate"]["operation"])]
    numerical = _read(Path(output) / context["numerical_record"])
    return {"context_id": context["id"], "split": context["split"],
        "backend": context["pretrial_features"]["planning_backend"], "method": method, "seed": None,
        "operation_id": initial["candidate"]["operation"], "final_control": initial["candidate"]["control"],
        "trial_feasible": initial["feasible"], "trial_score": initial["score"], "trial_failures": initial["failures"],
        "incumbent_score": context["incumbent"]["score"], "final_score": initial["score"],
        "objective_improvement": context["incumbent"]["score"] - initial["score"] if initial["feasible"] else None,
        "final_model_feasible": initial["feasible"], "final_model_failures": initial["failures"],
        "final_ac_feasible": audit["feasible"], "final_ac_failures": audit["failures"],
        "refinement_trials": 0, "response_calls_accounted": 0,
        "planning_and_initial_seconds": _preparation_seconds(numerical)[0],
        "recorded_planning_seconds_reused": _preparation_seconds(numerical)[1],
        "response_pool_serial_seconds": 0.0, "selected_trial_seconds": 0.0,
        "final_recheck_seconds": initial["seconds"], "selector_seconds": 0.0,
        "accounted_serial_seconds_excluding_ac_audit": None,
        "timing_scope": "Standalone method timing not reconstructed from shared two-controller preparation",
        "scope": "Initial independent model check; raw controller action, no learned selection",
        "operator_acknowledged": False, "dispatch_authorized": False}


def _summaries(rows):
    results = []
    for method in sorted({row["method"] for row in rows}):
        selected = [row for row in rows if row["method"] == method]
        results.append({"method": method, "contexts": len(selected),
            "final_model_passes": sum(row["final_model_feasible"] for row in selected),
            "final_ac_passes": sum(row["final_ac_feasible"] for row in selected),
            "trial_rejections": sum(not row["trial_feasible"] for row in selected),
            "mean_final_objective_on_model_passes": _mean([row["final_score"] for row in selected]),
            "mean_objective_improvement_on_model_passes": _mean([row["objective_improvement"] for row in selected]),
            "improved_contexts": sum(row["objective_improvement"] is not None and row["objective_improvement"] > 1e-10 for row in selected),
            "mean_refinement_trials": _mean([row["refinement_trials"] for row in selected]),
            "mean_response_calls_accounted": _mean([row["response_calls_accounted"] for row in selected]),
            "mean_accounted_serial_seconds": _mean([row["accounted_serial_seconds_excluding_ac_audit"] for row in selected])})
    return results


def _evaluate(output, contexts, response_rows, policy, protocol, split="test", include_all_baselines=True, seed=None):
    rechecks = _final_lookup(output, contexts)
    audit_path = Path(output) / "initial_model_audits.json"
    initial_audits = ({(row["context_id"], row["initial_method"]): row["opendss"]
                      for row in _read(audit_path)} if audit_path.exists() else
                     {(context["id"], initial["candidate"]["operation"]): initial
                      for context in contexts if context["status"] == "READY"
                      for initial in context["initial_evaluations"]})
    rows, pool_records = [], []
    rng = np.random.default_rng(protocol["uniform_primary_seed"])
    before = policy.state_dict()
    for context in contexts:
        if context["split"] != split or context["status"] != "READY":
            continue
        responses = response_rows[context["id"]]
        pool = canonicalize_responses(_public_responses(responses), context["catalog"])
        pool_records.append({"context_id": context["id"], **pool})
        if not pool["candidates"]:
            rows.append(_selection_row(output, context, responses, pool, "learned_selector", "KEEP_INCUMBENT",
                        protocol, rechecks, seed=seed, retain_without_trial=True,
                        selection_failure="No valid responses; retain independently checked incumbent"))
        else:
            tick = time.perf_counter()
            selection = policy.select(context["pretrial_features"], pool["candidates"])
            elapsed = time.perf_counter() - tick
            rows.append(_selection_row(output, context, responses, pool, "learned_selector", selection.operation_id,
                                       protocol, rechecks, elapsed, seed))
        if not include_all_baselines:
            continue
        choices = {"fixed_numerical": protocol["fixed_numerical_operation"]}
        if pool["candidates"]:
            choices.update({"majority_vote": _chosen(pool, majority_select(pool["candidates"]))["operation_ids"][0],
                            "uniform_response": _chosen(pool, uniform_select(pool["candidates"], rng))["operation_ids"][0]})
        else:
            for method in ("majority_vote", "uniform_response"):
                rows.append(_selection_row(output, context, responses, pool, method, "KEEP_INCUMBENT",
                            protocol, rechecks, retain_without_trial=True,
                            selection_failure="No valid responses; retain independently checked incumbent"))
        for response in responses:
            if response["operation_id"] in context["catalog"]:
                choices["fixed_pool_response:" + response["model_id"]] = response["operation_id"]
            else:
                rows.append(_selection_row(output, context, responses, pool,
                            "fixed_pool_response:" + response["model_id"], "KEEP_INCUMBENT", protocol,
                            rechecks, retain_without_trial=True,
                            selection_failure="Invalid model response; retain independently checked incumbent"))
        for method, operation in choices.items():
            rows.append(_selection_row(output, context, responses, pool, method, operation, protocol,
                                       rechecks, no_llm=method == "fixed_numerical"))
        # Extra-budget reference is evaluated after all actual selectors decide.
        oracle = SelectedFeedback(output)
        candidates = [(row["operation_ids"][0], oracle.reveal(context, row["operation_ids"][0]))
                      for row in pool["candidates"]]
        best = min(candidates, key=lambda item: (min(context["incumbent"]["score"], item[1]["score"])
                   if item[1]["feasible"] else context["incumbent"]["score"], item[0]))[0] if candidates else "KEEP_INCUMBENT"
        rows.append(_selection_row(output, context, responses, pool, "best_of_all_responses_extra_budget", best,
                                   protocol, rechecks, evaluated_operations=[key for key, _ in candidates],
                                   retain_without_trial=not candidates,
                                   selection_failure=None if candidates else "No valid responses; retain incumbent"))
        for initial in context["initial_evaluations"]:
            name = initial["candidate"]["operation"]
            if name in ("INITIAL_MPC", "INITIAL_SAC"):
                rows.append(_initial_row(output, context, responses,
                            "mpc_only" if name == "INITIAL_MPC" else "raw_sac", initial, initial_audits))
    after = policy.state_dict()
    if any(before[field] != after[field] for field in ("A", "b", "updates")):
        raise AssertionError("Held-out evaluation changed learned parameters")
    return {"split": split, "rows": rows, "summaries": _summaries(rows), "pools": pool_records,
            "total_requested_contexts": sum(row["split"] == split for row in contexts),
            "review_contexts": [row["id"] for row in contexts if row["split"] == split and row["status"] != "READY"],
            "test_updates": 0}


def _paired_comparison(rows):
    learned = {row["context_id"]: row for row in rows if row["method"] == "learned_selector"}
    results = []
    for method in ("majority_vote", "uniform_response", "fixed_numerical"):
        differences = []
        for other in (row for row in rows if row["method"] == method):
            candidate = learned.get(other["context_id"])
            if candidate and candidate["final_score"] is not None and other["final_score"] is not None:
                differences.append(candidate["final_score"] - other["final_score"])
        values = np.array(differences)
        if not len(values):
            continue
        rng = np.random.default_rng(31327)
        means = np.mean(rng.choice(values, (2000, len(values)), replace=True), axis=1)
        results.append({"comparator": method, "paired_contexts": len(values),
            "learned_minus_baseline_objective": float(values.mean()), "negative_favors_learned": True,
            "illustrative_bootstrap_95pct_interval": np.quantile(means, [.025, .975]).tolist(),
            "learned_better": int(np.sum(values < -1e-10)), "ties": int(np.sum(abs(values) <= 1e-10)),
            "learned_worse": int(np.sum(values > 1e-10)),
            "scope": "Paired test contexts with both model passes; 12-context teaching sample, one feeder, no multiplicity correction"})
    return results


def run_analysis(output=None, include_ac_transfer=True):
    output = Path(output) if output is not None else ROOT / "results/ensemble_voltage_pilot"
    protocol = freeze_analysis_protocol(output)
    validation_evidence = {"main": _verify_collection(output)}
    contexts, responses = _load_decisions(output, {"train": 24, "validation": 8, "test": 12})
    policies, histories = _train(output, contexts, responses, protocol)
    primary = policies[protocol["primary_seed"]]
    validation = _evaluate(output, contexts, responses, primary, protocol, split="validation",
                           include_all_baselines=False, seed=protocol["primary_seed"])
    test = _evaluate(output, contexts, responses, primary, protocol, seed=protocol["primary_seed"])
    sensitivity = []
    for seed, policy in policies.items():
        result = _evaluate(output, contexts, responses, policy, protocol, include_all_baselines=False, seed=seed)
        sensitivity.append({"seed": seed, "summary": result["summaries"], "rows": result["rows"]})
    analysis = {"schema": "selector_pilot_analysis_v1", "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol": protocol, "training": histories, "validation": validation, "test": test,
        "paired_test_comparison": _paired_comparison(test["rows"]), "training_order_sensitivity": sensitivity,
        "interpretation": ["Actual LLM response pools; outcome collection and policy evaluation are simulator replay",
            "Only selected training feedback updates the bandit; validation and test never update it",
            "Frozen hyperparameters; one small pass of 24 training contexts per seed",
            "The learned policy allocates a trial; independent numerical checks retain the incumbent on bad trials",
            "Model-only acceptance and independent full-feeder AC audit remain distinct",
            "Best-of-all uses more trial budget; no LLM or RL superiority is presumed"],
        "sources": protocol["sources"]}
    if include_ac_transfer:
        transfer = output / "ac_transfer"
        validation_evidence["ac_transfer"] = _verify_collection(transfer)
        ac_contexts, ac_responses = _load_decisions(transfer, {"test": 12})
        if {row["id"] for row in ac_contexts} != {row["id"] for row in contexts if row["split"] == "test"}:
            raise ValueError("AC transfer does not use the same twelve held-out physical contexts")
        original_cases = {row["id"]: row["case"] for row in contexts if row["split"] == "test"}
        if any(row["case"] != original_cases[row["id"]] for row in ac_contexts):
            raise ValueError("AC transfer changed a held-out physical case despite keeping its ID")
        result = _evaluate(transfer, ac_contexts, ac_responses, primary, protocol, seed=protocol["primary_seed"])
        analysis["ac_transfer"] = {**result, "training_backend": "lindistflow3", "evaluation_backend": "opendss",
            "no_retraining_or_tuning": True, "paired_comparison": _paired_comparison(result["rows"])}
    analysis["evidence_validation"] = validation_evidence
    _write(output / "selector_analysis.json", analysis)
    return analysis


if __name__ == "__main__":
    run_analysis()
