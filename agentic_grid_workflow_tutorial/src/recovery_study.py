"""Known-failure recovery study with a competent deterministic counterfactual.

The controller tools and OpenDSS gate are real. Two software-availability faults
are deliberately injected by the adapter; they are not observed service outages.
This study measures the benefit of a repair loop, not uniquely of an LLM.
Run: ``python -m src.recovery_study`` after the saved DQN has been trained.
"""
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
import copy
import hashlib
import json
import time

from .control_tools import ROOT, Case, Candidate, ac_table, mpc, drl, digest, provenance
from .learning import load_policy
from .workflow import Llama, awareness, evidence_failures, verify_candidate


@dataclass(frozen=True)
class RecoveryCase:
    id: str
    description: str
    case: Case
    initial_tool: str
    unavailable_tool: str = ""
    injected_delay_seconds: float = .02


CASES = (
    RecoveryCase("F1", "Injected MPC service-unavailable response; nominal DQN remains usable.",
                 Case("recovery_F1", forecast=(3, 3, 3)), "MPC", "MPC"),
    RecoveryCase("F2", "Injected DQN checkpoint-access failure; MPC remains usable.",
                 Case("recovery_F2", forecast=(3, 3, 3)), "DRL", "DRL"),
    RecoveryCase("F3", "Actual nominal-trained DQN proposal fails the 80% current-rating check.",
                 Case("recovery_F3", forecast=(3, 3, 3), rating_fraction=.8), "DRL"),
)
METHODS = ("single_pass", "adaptive_rules", "agent_loop")
TOOL_BUDGET = 2


def call_tool(study_case, tool, table, policy):
    """Failure injection is isolated here, with explicit provenance in the result."""
    started = time.perf_counter()
    if tool == study_case.unavailable_tool:
        time.sleep(study_case.injected_delay_seconds)
        return {
            "status": "TOOL_UNAVAILABLE", "candidate": None,
            "reason": "injected_mpc_service_unavailable" if tool == "MPC"
                      else "injected_dqn_checkpoint_access_failure",
            "injected_failure": True,
            "injected_delay_seconds": study_case.injected_delay_seconds,
            "seconds": time.perf_counter()-started, "fresh_ac_solves": 0,
        }
    if tool == "MPC":
        answer = mpc(table, study_case.case)
    elif tool == "DRL":
        answer = drl(policy, study_case.case)
    else:
        return {"status": "TOOL_ERROR", "candidate": None, "reason": "unknown_tool",
                "injected_failure": False, "seconds": time.perf_counter()-started,
                "fresh_ac_solves": 0}
    return dict(answer, injected_failure=False)


def next_rule_tool(available_tools):
    """Competent finite-state recovery: remove failed tools and use an alternative."""
    return next((tool for tool in ("MPC", "DRL") if tool in available_tools), "REVIEW")


def run_recovery(study_case, table, policy, method, llama=None):
    if method not in METHODS:
        raise ValueError(f"Unknown recovery method: {method}")
    if method == "agent_loop" and llama is None:
        raise ValueError("agent_loop requires a live Llama instance; tests supply explicit doubles.")
    started = time.perf_counter()
    calls_before = len(llama.calls) if llama is not None else 0
    evidence, state = awareness(study_case.case)
    failures = evidence_failures(evidence)
    trace = [{"role": "Awareness", "event": "evidence_validation",
              "state": copy.deepcopy(state), "evidence": copy.deepcopy(evidence),
              "failures": failures}]
    result = {
        "case": study_case.id, "method": method, "status": "ESCALATE",
        "initial_tool": study_case.initial_tool, "initial_tool_forced_equally": True,
        "tool_budget": TOOL_BUDGET, "tool_calls": 0, "fresh_ac_solves": 1,
        "gate_rejections": 0, "unavailable_responses": 0,
        "candidate": None, "metrics": None, "reasons": list(failures),
        "trace": trace, "injection": {
            "tool": study_case.unavailable_tool or None,
            "delay_seconds": study_case.injected_delay_seconds if study_case.unavailable_tool else 0.,
            "description": study_case.description,
        },
    }
    used = []
    selected = study_case.initial_tool
    if failures:
        result["status"] = "REVIEW"
    for attempt in range(TOOL_BUDGET if not failures else 0):
        if selected == "REVIEW" or selected in used or selected not in ("MPC", "DRL"):
            result["reasons"] = ["planner_review" if selected == "REVIEW" else "unavailable_tool"]
            break
        used.append(selected)
        result["tool_calls"] += 1
        trace.append({"role": "Planner", "event": "selected_tool", "tool": selected,
                      "forced_initial_tool": attempt == 0})
        proposal = call_tool(study_case, selected, table, policy)
        result["fresh_ac_solves"] += proposal["fresh_ac_solves"]
        trace.append({"role": "Tool", "event": "result", "tool": selected,
                      "result": copy.deepcopy(proposal)})
        if proposal["status"] == "TOOL_UNAVAILABLE":
            result["unavailable_responses"] += 1
            result["reasons"] = [proposal["reason"]]
            failed_check = {"kind": "tool_availability", "tool": selected,
                            "reasons": list(result["reasons"]), "injected_failure": True}
        elif proposal["candidate"] is None:
            # A proven infeasible horizon does not authorize a myopic fallback.
            result["reasons"] = [proposal["reason"]]
            break
        else:
            candidate = Candidate(**proposal["candidate"])
            gate = verify_candidate(study_case.case, candidate)
            result["fresh_ac_solves"] += gate["fresh_ac_solves"]
            trace.append({"role": "Verification", "event": "fresh_AC_check", **copy.deepcopy(gate)})
            if gate["accepted"]:
                result.update(status="RECOMMEND", candidate=asdict(candidate),
                              metrics=gate["metrics"], reasons=[])
                break
            result["gate_rejections"] += 1
            result["reasons"] = list(gate["reasons"])
            failed_check = dict(gate, kind="electrical_verification", tool=selected)
        if method == "single_pass" or attempt+1 >= TOOL_BUDGET:
            break
        available = [tool for tool in ("MPC", "DRL") if tool not in used]+["REVIEW"]
        context = {
            "case": asdict(study_case.case), "validated_state": state,
            "operator_request": "Obtain a verified PV cap, or stop if no tool can support one.",
            "available_tools": available,
            "tool_health": {tool: "failed_in_this_attempt" if tool in used else "not_failed"
                            for tool in ("MPC", "DRL")},
            "latest_failed_check": failed_check,
            "history": [copy.deepcopy(row) for row in trace if row["role"] in ("Tool", "Verification")],
            "remaining_tool_calls": TOOL_BUDGET-attempt-1,
        }
        if method == "adaptive_rules":
            selected = next_rule_tool(available)
            trace.append({"role": "Deterministic supervisor", "event": "repair_selection",
                          "tool": selected, "reason": "Exclude failed tool; use the available alternative."})
        else:
            critique = llama.ask("Critic", context, seed=101+attempt)
            trace.append({"role": "Critic", "event": "repair_feedback", **copy.deepcopy(critique)})
            planner_context = dict(context, critic_feedback=copy.deepcopy(critique))
            decision = llama.ask("Planner", planner_context, seed=11+attempt)
            trace.append({"role": "Planner", "event": "repair_selection", **copy.deepcopy(decision)})
            selected = decision["tool"]
            if selected not in available:
                result["reasons"] = ["unavailable_tool"]
                break
    new_calls = llama.calls[calls_before:] if llama is not None else []
    result.update(
        verified_completion=result["status"] == "RECOMMEND",
        llm_calls=len(new_calls), llm_seconds=sum(row.get("seconds", 0.) for row in new_calls),
        seconds=time.perf_counter()-started,
        injected_delay_seconds=sum(row["result"].get("injected_delay_seconds", 0.)
                                   for row in trace if row["role"] == "Tool"),
    )
    return result


def protocol_record():
    return {
        "study": "Known-failure recovery; a teaching ablation with a competent deterministic supervisor",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "cases": [asdict(case) for case in CASES], "methods": list(METHODS),
        "tool_budget": TOOL_BUDGET,
        "single_pass": "Same forced first tool and gate; stops after its first failure. This is a repair-loop ablation, not the strongest conventional practice.",
        "adaptive_rules": "Structured finite-state recovery excludes failed tools and chooses the available alternative; no hidden expected answer.",
        "agent_loop": "Actual local Llama critic followed by planner; planner receives critic feedback and the same failed-tool observations.",
        "availability_faults": "Injected adapter responses with a real 20 ms delay. No process was stopped and no checkpoint was deleted.",
        "electrical_case": "Uses the saved trained DQN and fresh OpenDSS verification at 80% permitted line ratings; no policy action is fabricated.",
        "cost": "End-to-end run latency includes one awareness AC solve, numerical tools, fresh gate solves, injected delay and any Llama calls. Excludes AC-table build and DQN training, shared by all methods.",
        "claim_boundary": "Demonstrates recovery versus a single pass. Matching a competent finite-state supervisor does not establish a unique LLM advantage. Three authored cases, one live run per condition; no statistical or field-performance claim.",
        "sources": provenance(),
        "study_code_sha256": digest(__file__),
        "workflow_code_sha256": digest(ROOT/'src/workflow.py'),
        "policy_weights_sha256": digest(ROOT/'models/dqn_seed_11.npz'),
    }


def main():
    table = ac_table()
    policy = load_policy()
    protocol_path = ROOT/'results/recovery_protocol.json'
    protocol = protocol_record()
    # Freeze the full protocol before constructing or calling the model client.
    protocol_path.write_text(json.dumps(protocol, indent=2), encoding='utf-8')
    frozen_hash = digest(protocol_path)
    llama = Llama(log_path=ROOT/'results/recovery_calls.json')
    rows = []
    for case in CASES:
        for method in METHODS:
            print(f"Recovery {case.id}: {method}", flush=True)
            rows.append(run_recovery(case, table, policy, method, llama if method == "agent_loop" else None))
            (ROOT/'results/recovery.json').write_text(json.dumps({
                "protocol_sha256": frozen_hash, "model": llama.metadata,
                "complete": False, "runs": rows}, indent=2), encoding='utf-8')
    if digest(protocol_path) != frozen_hash:
        raise RuntimeError("The frozen protocol changed during the study.")
    summary = {}
    for method in METHODS:
        selected = [row for row in rows if row["method"] == method]
        summary[method] = {
            "runs": len(selected), "verified_completions": sum(row["verified_completion"] for row in selected),
            "no_action_outcomes": sum(row["candidate"] is None for row in selected),
            "tool_calls": sum(row["tool_calls"] for row in selected),
            "llm_calls": sum(row["llm_calls"] for row in selected),
            "total_seconds": sum(row["seconds"] for row in selected),
            "fresh_ac_solves": sum(row["fresh_ac_solves"] for row in selected),
        }
    result = {"protocol_sha256": frozen_hash, "model": llama.metadata,
              "complete": True, "runs": rows, "summary": summary,
              "interpretation": "Repair is compared with a competent deterministic supervisor. Llama superiority is not assumed; compare the recorded completion and cost outcomes."}
    (ROOT/'results/recovery.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
