"""Mechanism and leakage-guard tests; these are not grid performance evidence."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np

from src.response_selector import (LinUCB, canonicalize_responses, context_vector,
                                   majority_select, uniform_select, _hash)


def context(margin=0.2):
    return {"case_family": "voltage", "planning_backend": "lindistflow3",
            "load_mean": 1.0, "load_span": 0.1, "current_margin": margin,
            "voltage_margin": 0.01, "incumbent_cost": 0.4, "remaining_budget": 1}


def pool():
    return canonicalize_responses([
        {"model_id": "model_a", "operation_id": "A", "reason": "Synthetic option A."},
        {"model_id": "model_b", "operation_id": "B", "reason": "Synthetic option B."},
    ], {"A": {"tool": "BOUNDED_SEARCH", "parameters": {"delta": 0.01}},
        "B": {"tool": "BOUNDED_SEARCH", "parameters": {"delta": -0.01}}})["candidates"]


class CanonicalVotes(unittest.TestCase):
    def test_aliases_numeric_identity_and_votes(self):
        result = canonicalize_responses([
            {"model_id": "a", "operation_id": "FIRST", "reason": "First."},
            {"model_id": "b", "operation_id": "ALIAS", "reason": "Same action."},
            {"model_id": "c", "operation_id": "OTHER", "reason": "Different action."},
        ], {"FIRST": {"tool": "control", "parameters": {"u": [1, 0]}},
            "ALIAS": {"tool": "control", "parameters": {"u": [1.0, -0.0]}},
            "OTHER": {"tool": "control", "parameters": {"u": [0.5, 0.0]}}})
        self.assertEqual(result["valid_responses"], 3)
        self.assertEqual(len(result["candidates"]), 2)
        chosen = next(row for row in result["candidates"] if row["vote_count"] == 2)
        self.assertEqual(chosen["operation_ids"], ["ALIAS", "FIRST"])
        self.assertAlmostEqual(chosen["vote_share"], 2 / 3)
        self.assertEqual(majority_select(result["candidates"]), chosen["candidate_id"])

    def test_duplicate_voter_is_not_counted_regardless_of_order(self):
        responses = [
            {"model_id": "a", "operation_id": "A", "reason": "First duplicate."},
            {"model_id": "a", "operation_id": "B", "reason": "Second duplicate."},
            {"model_id": "b", "operation_id": "B", "reason": "One valid vote."},
        ]
        catalog = {"A": {"tool": "x", "parameters": {"v": 1}},
                   "B": {"tool": "x", "parameters": {"v": 2}}}
        for votes in (responses, list(reversed(responses))):
            result = canonicalize_responses(votes, catalog)
            self.assertEqual(result["valid_responses"], 1)
            self.assertEqual(len(result["rejected"]), 2)
            self.assertEqual(result["candidates"][0]["operation_ids"], ["B"])

    def test_unknown_and_malformed_responses_retained_as_rejections(self):
        result = canonicalize_responses([
            {"model_id": "x", "operation_id": "NOT_PERMITTED", "reason": "Invalid."},
            {"model_id": "y", "operation_id": "A", "reason": "Outcome leakage.", "pass": True},
            None,
        ], {"A": {"tool": "bounded", "parameters": {}}})
        self.assertEqual(result["valid_responses"], 0)
        self.assertEqual(len(result["rejected"]), 3)
        with self.assertRaises(ValueError):
            majority_select(result["candidates"])

    def test_nonfinite_catalog_and_changed_candidate_rejected(self):
        with self.assertRaises(ValueError):
            canonicalize_responses([], {"A": {"tool": "x", "parameters": {"u": float("nan")}}})
        with self.assertRaises(ValueError):
            canonicalize_responses([], {"A": {"tool": "x", "parameters": {1: "ambiguous"}}})
        rows = pool()
        rows[0]["operation"]["parameters"]["delta"] = 0.9
        with self.assertRaises(ValueError):
            majority_select(rows)

    def test_ties_and_uniform_are_reproducible_over_unique_operations(self):
        rows = pool()
        self.assertEqual(majority_select(rows), majority_select(list(reversed(rows))))
        a, b = np.random.default_rng(27), np.random.default_rng(27)
        first = [uniform_select(rows, a) for _ in range(30)]
        second = [uniform_select(list(reversed(rows)), b) for _ in range(30)]
        self.assertEqual(first, second)
        self.assertEqual(set(first), {row["candidate_id"] for row in rows})


class PretrialSchema(unittest.TestCase):
    def test_future_outcomes_and_missing_values_rejected(self):
        for key in ("candidate_cost", "pass", "reward", "offline_truth", "score"):
            bad = {**context(), key: 0}
            with self.subTest(key=key), self.assertRaises(ValueError):
                context_vector(bad)
        bad = context()
        del bad["current_margin"]
        with self.assertRaises(ValueError):
            context_vector(bad)

    def test_nonfinite_boolean_and_invalid_budget_rejected(self):
        for value in (float("nan"), float("inf"), True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                context_vector({**context(), "incumbent_cost": value})
        for value in (0, True, 1.5, 101):
            with self.subTest(value=value), self.assertRaises(ValueError):
                context_vector({**context(), "remaining_budget": value})


class BanditMechanics(unittest.TestCase):
    def test_only_pending_selected_feedback_can_update_once(self):
        model = LinUCB(["A", "B"])
        decision = model.select(context(), pool())
        with self.assertRaises(RuntimeError):
            model.select(context(), pool())
        with self.assertRaises(ValueError):
            model.update(deepcopy(decision), 1.0)
        for value in (True, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                model.update(decision, value)
        model.update(decision, 1.0)
        self.assertEqual(model.updates, 1)
        with self.assertRaises(ValueError):
            model.update(decision, 1.0)

    def test_no_unfinished_checkpoint_or_freeze(self):
        model = LinUCB(["A", "B"])
        decision = model.select(context(), pool())
        with self.assertRaises(RuntimeError):
            model.state_dict()
        with self.assertRaises(RuntimeError):
            model.freeze()
        model.update(decision, 0.0)
        model.freeze()
        with self.assertRaises(RuntimeError):
            model.update(decision, 0.0)

    def test_unknown_operation_and_modified_votes_fail_closed(self):
        with self.assertRaises(ValueError):
            LinUCB(["A"]).select(context(), pool())
        rows = pool()
        rows[0]["vote_count"] = 3
        with self.assertRaises(ValueError):
            LinUCB(["A", "B"]).select(context(), rows)

    def test_actual_context_dependent_reward_learning_synthetic_only(self):
        # A mathematical two-arm mechanism test, NOT a grid or LLM benchmark.
        model = LinUCB(["A", "B"], alpha=0.7)
        candidates = pool()
        for episode in range(160):
            sign = 1 if episode % 2 == 0 else -1
            decision = model.select(context(margin=sign), candidates)
            desired = "A" if sign > 0 else "B"
            reward = 1.0 if decision.operation_id == desired else -1.0
            model.update(decision, reward)
        model.freeze()
        self.assertEqual(model.select(context(1), candidates).operation_id, "A")
        self.assertEqual(model.select(context(-1), candidates).operation_id, "B")
        self.assertEqual(model.updates, 160)

    def test_frozen_test_selection_does_not_change_learned_parameters(self):
        model = LinUCB(["A", "B"])
        decision = model.select(context(), pool())
        model.update(decision, 0.5)
        model.freeze()
        before = model.state_dict()
        selected = model.select(context(-0.3), pool())
        self.assertFalse(selected.exploring)
        after = model.state_dict()
        for field in ("A", "b", "updates"):
            self.assertEqual(before[field], after[field])
        with self.assertRaises(RuntimeError):
            model.update(selected, 1.0)

    def test_checkpoint_roundtrip_integrity_and_covariance_validation(self):
        model = LinUCB(["A", "B"])
        decision = model.select(context(), pool())
        model.update(decision, 0.7)
        model.freeze()
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "checkpoint.json"
            model.save(path)
            restored = LinUCB.load(path)
            self.assertTrue(restored.frozen)
            expected = model.select(context(), pool())
            observed = restored.select(context(), pool())
            self.assertEqual(expected.candidate_id, observed.candidate_id)
            self.assertAlmostEqual(expected.predicted_reward, observed.predicted_reward)
            record = json.loads(path.read_text())
            record["b"][0] += 1
            path.write_text(json.dumps(record))
            with self.assertRaises(ValueError):
                LinUCB.load(path)
            # Integrity is not an authenticity claim: even a rehashed malformed
            # checkpoint must fail matrix validation.
            record = model.state_dict()
            record["A"][0][0] = -1.0
            record.pop("sha256")
            record["sha256"] = _hash(record)
            path.write_text(json.dumps(record))
            with self.assertRaises(ValueError):
                LinUCB.load(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
