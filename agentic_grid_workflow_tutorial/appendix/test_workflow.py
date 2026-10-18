"""Bounded regression tests; test doubles here are NOT experiment evidence.

Run from the tutorial directory: ``python appendix/test_workflow.py``.
No Ollama requests, checkpoint writes, or DQN training runs are performed.
Electrical verification tests use fresh OpenDSS solves on the bundled feeder.
"""
import copy
import itertools
import math
import sys
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src import control_tools as control
from src import workflow
from src.learning import DQN
from src.power_tools import verify_physics


class TestOnlyQPolicy:
    """Deterministic unit-test double, never used as a trained-policy result."""
    def __init__(self, action_index=3):
        self.action_index = action_index

    def forward(self, x):
        values = np.zeros((len(x), 8))
        values[:, self.action_index] = 1.
        return values, None


class TestOnlyLlama:
    """Unit-test message recorder; it does not contact or emulate Llama quality."""
    def __init__(self):
        self.calls = []

    def ask(self, role, context, seed=11):
        response = ({"repair_tool": "MPC", "reason": "Unit-test repair feedback."}
                    if role == "Critic" else
                    {"tool": "MPC", "reason": "Unit-test next planner response."})
        self.calls.append({"role": role, "context": copy.deepcopy(context),
                           "seed": seed, "response": copy.deepcopy(response)})
        return response


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = control.ac_table()
        cls.nominal = control.Case("unit_nominal", forecast=(3, 3, 3))
        cls.derated = replace(cls.nominal, id="unit_derated", rating_fraction=.8)

    def test_mpc_matches_exhaustive_horizon(self):
        case = control.Case("unit_horizon", forecast=(3, 2, 1), previous=2)
        feasible = {li: [a for a in range(8) if not verify_physics(self.table[li][a])]
                    for li in set(case.forecast)}
        best_value = -math.inf
        optimal_first = set()
        for actions in itertools.product(*(feasible[li] for li in case.forecast)):
            value, previous = 0., case.previous
            for k, (li, action) in enumerate(zip(case.forecast, actions)):
                value += control.GAMMA**k * control.utility(self.table, li, action, previous)
                previous = action
            if value > best_value + 1e-10:
                best_value, optimal_first = value, {actions[0]}
            elif abs(value-best_value) < 1e-10:
                optimal_first.add(actions[0])
        answer = control.mpc(self.table, case)
        self.assertEqual(answer["status"], "PROPOSE")
        self.assertAlmostEqual(answer["objective"], best_value, places=10)
        self.assertIn(answer["candidate"]["pv_cap"],
                      {float(control.CAPS[a]) for a in optimal_first})

    def test_current_and_future_infeasibility_propagate(self):
        for forecast in ((4, 0, 0), (0, 4, 0)):
            with self.subTest(forecast=forecast):
                case = control.Case("unit_infeasible", forecast=forecast, rating_fraction=.65)
                result = control.mpc(self.table, case)
                self.assertEqual(result["status"], "ESCALATE")
                self.assertIsNone(result["candidate"])
                self.assertIsNone(result["objective"])
                self.assertEqual(result["plan_caps"], [])

    def test_missing_or_stale_evidence_prevents_llm_and_control_calls(self):
        evidence, _ = workflow.awareness(self.nominal)
        evidence["age_s"] = 120.
        for supplied in ({}, evidence):
            llama = TestOnlyLlama()
            with patch.object(workflow, "mpc", side_effect=AssertionError("No tool should run")), \
                 patch.object(workflow, "drl", side_effect=AssertionError("No tool should run")):
                result = workflow.run_workflow(
                    self.nominal, self.table, TestOnlyQPolicy(), llama=llama, evidence=supplied)
            self.assertEqual(result["status"], "REVIEW")
            self.assertIsNone(result["candidate"])
            self.assertEqual(result["tool_calls"], 0)
            self.assertEqual(result["llm_calls"], 0)
            self.assertEqual(llama.calls, [])

    def test_invalid_candidates_reject_before_simulation(self):
        invalid = [None, {}, control.Candidate("UNKNOWN", 20),
                   control.Candidate("MPC", False), control.Candidate("MPC", float("nan")),
                   control.Candidate("MPC", float("inf")), control.Candidate("MPC", 21),
                   control.Candidate("MPC", 20, shed_fraction=True),
                   control.Candidate("MPC", 20, shed_fraction=-.1),
                   control.Candidate("MPC", 20, tie="external_command")]
        with patch.object(workflow, "simulate_candidate", side_effect=AssertionError("Invalid action simulated")):
            for candidate in invalid:
                with self.subTest(candidate=candidate):
                    result = workflow.verify_candidate(self.nominal, candidate)
                    self.assertFalse(result["accepted"])
                    self.assertEqual(result["fresh_ac_solves"], 0)
                    self.assertTrue(result["reasons"])

    def test_invalid_cases_reject_before_awareness_or_llm(self):
        invalid = [None, {}, replace(self.nominal, forecast=()),
                   replace(self.nominal, forecast=(-1, 2, 3)),
                   replace(self.nominal, forecast=(True, 2, 3)),
                   replace(self.nominal, previous=8),
                   replace(self.nominal, rating_fraction=0),
                   replace(self.nominal, rating_fraction=float("nan")),
                   replace(self.nominal, capacity=-1),
                   replace(self.nominal, task="unknown"),
                   replace(self.nominal, fault="false")]
        for case in invalid:
            with self.subTest(case=case):
                llama = TestOnlyLlama()
                with patch.object(workflow, "awareness", side_effect=AssertionError("Invalid case simulated")):
                    result = workflow.run_workflow(
                        case, self.table, TestOnlyQPolicy(), llama=llama)
                self.assertEqual(result["status"], "REVIEW")
                self.assertIsNone(result["candidate"])
                self.assertEqual(result["fresh_ac_solves"], 0)
                self.assertEqual(result["tool_calls"], 0)
                self.assertEqual(llama.calls, [])
                answer = control.mpc(self.table, case)
                self.assertEqual(answer["status"], "ESCALATE")
                self.assertIsNone(answer["candidate"])
                self.assertEqual(answer["fresh_ac_solves"], 0)

    def test_fresh_gate_rejects_nominal_drl_action_under_derating(self):
        proposal = control.drl(TestOnlyQPolicy(3), self.derated)
        self.assertEqual(proposal["candidate"]["pv_cap"], 30)
        candidate = control.Candidate(**proposal["candidate"])
        with patch.object(workflow, "simulate_candidate", wraps=control.simulate_candidate) as fresh:
            result = workflow.verify_candidate(self.derated, candidate)
        fresh.assert_called_once()
        self.assertEqual(result["fresh_ac_solves"], 1)
        self.assertFalse(result["accepted"])
        self.assertIn("thermal", result["reasons"])
        self.assertGreater(result["metrics"]["max_line_pct"], 100)
        self.assertGreater(result["metrics"]["overloaded_lines"], 0)

    def test_critic_feedback_reaches_next_planner(self):
        llama = TestOnlyLlama()
        result = workflow.run_workflow(
            self.derated, self.table, TestOnlyQPolicy(3), llama=llama,
            initial_tool="DRL", budget=2)
        self.assertEqual(result["status"], "RECOMMEND")
        self.assertEqual(result["candidate"]["tool"], "MPC")
        self.assertEqual(result["tool_calls"], 2)
        self.assertEqual(result["gate_rejections"], 1)
        self.assertEqual([c["role"] for c in llama.calls], ["Critic", "Planner"])
        self.assertEqual(llama.calls[1]["context"]["critic_feedback"], llama.calls[0]["response"])
        self.assertNotIn("DRL", llama.calls[1]["context"]["available_tools"])

    def test_infeasible_workflow_has_no_action_and_no_myopic_fallback(self):
        for forecast in ((4, 0, 0), (0, 4, 0)):
            case = control.Case("unit_escalation", forecast=forecast, rating_fraction=.65)
            with patch.object(workflow, "drl", side_effect=AssertionError("No myopic fallback")):
                result = workflow.run_workflow(
                    case, self.table, TestOnlyQPolicy(), method="fixed", initial_tool="MPC")
            self.assertEqual(result["status"], "ESCALATE")
            self.assertIsNone(result["candidate"])
            self.assertIsNone(result["metrics"])
            self.assertEqual(result["tool_calls"], 1)
            self.assertIn("no_feasible_horizon", result["reasons"])

    def test_supplied_evidence_cannot_replace_internal_trust_anchors(self):
        evidence, _ = workflow.awareness(self.nominal)
        evidence.update(reported_topology="forged", trusted_topology="forged",
                        reported_vmax=1.01, trusted_vmax=1.01)
        llama = TestOnlyLlama()
        result = workflow.run_workflow(
            self.nominal, self.table, TestOnlyQPolicy(), llama=llama, evidence=evidence)
        self.assertEqual(result["status"], "REVIEW")
        self.assertIsNone(result["candidate"])
        self.assertEqual(result["tool_calls"], 0)
        self.assertEqual(result["llm_calls"], 0)

    def test_audit_evidence_is_a_snapshot_not_callers_mutable_dict(self):
        evidence, _ = workflow.awareness(self.nominal)
        result = workflow.run_workflow(
            self.nominal, self.table, TestOnlyQPolicy(), method="fixed", evidence=evidence,
            initial_tool="MPC")
        captured = copy.deepcopy(result["trace"][0]["evidence"])
        evidence["trusted_source"] = False
        evidence["age_s"] = 9999
        self.assertEqual(result["trace"][0]["evidence"], captured)

    def test_dqn_training_step_is_finite_and_target_network_is_separate(self):
        # Tiny synthetic batch checks gradient mechanics only; no training claim.
        network = DQN(11)
        before = [v.copy() for v in network.p]
        targets = [v.copy() for v in network.target]
        x = np.full((4, 6), .5)
        loss = network.train_batch(x, np.array([0, 1, 2, 3]), np.ones(4), x, np.ones(4))
        self.assertTrue(math.isfinite(loss))
        self.assertTrue(any(not np.array_equal(a, b) for a, b in zip(before, network.p)))
        self.assertTrue(all(np.isfinite(v).all() for v in network.p))
        self.assertTrue(all(np.array_equal(a, b) for a, b in zip(targets, network.target)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
