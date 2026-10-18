"""Targeted regression checks for the OpenDSS evidence and verification boundary.

Run from the tutorial directory: ``python appendix/test_physics.py``.
These test the declared nominal model, not operational grid safety.
"""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src import power_tools as physics


class PhysicsEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nominal = physics.simulate(pv_cap=30, details=True)
        cls.restoration = {
            tie: physics.simulate(fault=True, tie=tie, pv_cap=20, details=True)
            for tie in ("short", "long", "both")
        }

    def test_genuine_snapshot_passes(self):
        self.assertTrue(self.nominal["converged"])
        self.assertGreater(self.nominal["energized_bus_count"], 0)
        self.assertEqual(physics.verify_physics(self.nominal), [])
        self.assertEqual(
            len(self.nominal["lines"]), self.nominal["evaluated_line_count"]
        )
        summary = {k: v for k, v in self.nominal.items()
                   if k not in ("buses", "lines", "line_endpoints")}
        self.assertEqual(physics.verify_physics(summary), [])

    def test_missing_empty_nonfinite_and_invalid_evidence_rejected(self):
        for evidence in (None, {}, []):
            with self.subTest(evidence=evidence):
                self.assertIn("missing_evidence", physics.verify_physics(evidence))
        missing = dict(self.nominal)
        del missing["vmax"]
        self.assertIn("missing_evidence", physics.verify_physics(missing))
        for field in ("vmin", "vmax", "max_line_pct", "unserved_kw"):
            for value in (float("nan"), float("inf"), float("-inf")):
                with self.subTest(field=field, value=value):
                    bad = dict(self.nominal, **{field: value})
                    self.assertIn("invalid_numerical_evidence", physics.verify_physics(bad))
        self.assertIn("invalid_numerical_evidence", physics.verify_physics(
            dict(self.nominal, overloaded_lines=-1)))
        self.assertIn("invalid_evidence_domain", physics.verify_physics(
            dict(self.nominal, unserved_kw=-1)))
        self.assertIn("invalid_evidence_domain", physics.verify_physics(
            dict(self.nominal, served_kw=self.nominal["nominal_kw"] + 1)))
        for field in ("buses", "lines"):
            self.assertIn("empty_measurement_evidence", physics.verify_physics(
                dict(self.nominal, **{field: []})))
        self.assertIn("empty_measurement_evidence", physics.verify_physics(
            dict(self.nominal, energized_bus_count=0)))

    def test_detailed_evidence_is_cross_checked(self):
        bad = copy.deepcopy(self.nominal)
        bad["buses"][0]["vmax"] = float("nan")
        self.assertIn("invalid_numerical_evidence", physics.verify_physics(bad))
        bad = copy.deepcopy(self.nominal)
        bad["lines"][0]["max_current_amps"] = float("nan")
        self.assertIn("invalid_numerical_evidence", physics.verify_physics(bad))
        bad = dict(self.nominal, max_line_pct=0)
        self.assertIn("inconsistent_measurement_evidence", physics.verify_physics(bad))
        bad = dict(self.nominal, vmax=1.06)
        self.assertIn("voltage", physics.verify_physics(bad))

    def test_derating_uses_per_line_evidence_without_mutation(self):
        before = copy.deepcopy(self.nominal)
        violations = sum(row["loading_pct"] / .8 > 100 + 1e-4
                         for row in self.nominal["lines"])
        self.assertGreater(violations, 0)
        self.assertIn("thermal", physics.verify_physics(self.nominal, rating_fraction=.8))
        self.assertEqual(self.nominal, before)
        summary = {k: v for k, v in self.nominal.items() if k != "lines"}
        self.assertIn("missing_line_evidence", physics.verify_physics(summary, rating_fraction=.8))
        for fraction in (0, -.1, 1.1, float("nan"), True):
            self.assertIn("invalid_rating_fraction", physics.verify_physics(
                self.nominal, rating_fraction=fraction))

    def test_parallel_assets_have_distinct_identity_and_correct_cycles(self):
        states = self.restoration
        self.assertEqual(len({m["topology_hash"] for m in states.values()}), 3)
        for tie in ("short", "long"):
            self.assertEqual(states[tie]["mv_cycles"], 0)
            self.assertEqual(physics.verify_physics(states[tie]), [])
        self.assertEqual(states["both"]["mv_cycles"], 1)
        self.assertIn("mv_radiality", physics.verify_physics(states["both"]))

    def test_hash_retains_terminal_switch_state(self):
        closed = physics.simulate(fault=True, tie="short", pv_cap=20)
        physics.dss.Circuit.SetActiveElement("Line.tutorial_short")
        physics.dss.CktElement.Open(2, 0)
        reachable, _, opened_hash, _ = physics.graph_data()
        self.assertNotEqual(closed["topology_hash"], opened_hash)
        self.assertNotIn(physics.TAIL, reachable)


if __name__ == "__main__":
    unittest.main(verbosity=2)
