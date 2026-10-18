"""Focused standard-formulation checks. Run: python appendix/test_standard_formulations.py

Actual SciPy/MV-model numerical checks plus one explicitly mocked solver-failure
check. No LLM calls, training, frozen-study edits, or result-file writes.
"""
from pathlib import Path
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import standard_formulations as standard


class WLSChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.demo = standard.run_wls_demo()

    def test_observability_is_required(self):
        with self.assertRaisesRegex(ValueError, 'rank deficient'):
            standard.weighted_least_squares([[1, 1], [2, 2]], [1, 2], [.1, .1])

    def test_invalid_noise_and_significance_rejected(self):
        for sigma in ([0., .1], [float('nan'), .1]):
            with self.subTest(sigma=sigma), self.assertRaises(ValueError):
                standard.weighted_least_squares([[1.], [2.]], [1., 2.], sigma)
        for alpha in (0., 1., -.1, float('nan')):
            with self.subTest(alpha=alpha), self.assertRaises(ValueError):
                standard.weighted_least_squares([[1.], [2.]], [1., 2.], [.1, .1], alpha)

    def test_exactly_determined_recovery_has_no_residual_detector(self):
        row = self.demo['trusted_recovery']
        self.assertEqual(row['chi_square']['degrees_of_freedom'], 0)
        self.assertIsNone(row['chi_square']['threshold'])
        self.assertIsNone(row['chi_square']['alarm'])
        self.assertEqual(row['normalized_residuals'], [None, None, None])

    def test_attack_preserves_residual_but_shifts_state(self):
        clean, _, stealth = self.demo['cases']
        np.testing.assert_allclose(clean['residual'], stealth['residual'], atol=1e-12)
        np.testing.assert_allclose(np.array(stealth['estimate']) - clean['estimate'],
                                   self.demo['measurement_model']['stealth_shift'], atol=1e-12)
        self.assertFalse(stealth['chi_square']['alarm'])
        self.assertEqual(stealth['control']['actual_violation_count'], 1)

    def test_isolated_corruption_detected_and_untrusted_control_held(self):
        clean, isolated, _ = self.demo['cases']
        self.assertEqual(clean['chi_square']['degrees_of_freedom'], 5)
        self.assertTrue(isolated['chi_square']['alarm'])
        self.assertEqual(isolated['largest_normalized_residual'], 1)
        self.assertEqual(isolated['control']['status'], 'HOLD')
        self.assertEqual(self.demo['isolated_removal']['removed_index'], 1)
        self.assertFalse(self.demo['isolated_removal']['chi_square']['alarm'])

    def test_trusted_control_is_constrained_and_resolves_toy_overload(self):
        control = self.demo['trusted_recovery']['control']
        self.assertEqual(control['status'], 'PROPOSE')
        self.assertGreater(control['flexible_injection_pu'], 0)
        self.assertLessEqual(control['flexible_injection_pu'], .5)
        self.assertEqual(control['actual_violation_count'], 0)
        self.assertTrue(np.all(np.abs(control['predicted_flows_pu']) <=
                               np.array(control['line_limits_pu']) - control['planning_margin_pu'] + 1e-8))

    def test_success_flag_cannot_bypass_control_constraints(self):
        # Only this check uses a solver test double; it is not experiment data.
        bad = SimpleNamespace(success=True, x=np.array([2.]), fun=0.)
        with patch.object(standard, 'minimize', return_value=bad):
            control = standard._redispatch([0., 0., 0.], [0., 0., 0.],
                                           np.ones((4, 3)), np.eye(3))
        self.assertEqual(control['status'], 'HOLD')


class RestorationChecks(unittest.TestCase):
    def check_network(self, row):
        graph, solution = row['graph'], row['milp']
        self.assertTrue(solution['success'])
        self.assertTrue(row['agreement'])
        chosen = set(solution['closed_edges'])
        adjacency = {node: [] for node in graph['nodes']}
        balance = np.zeros(len(graph['nodes']))
        for edge in graph['edges']:
            flow = solution['branch_flows_kw'][edge['name']]
            self.assertLessEqual(abs(flow), edge['capacity_kw'] + 1e-7)
            if edge['name'] in chosen:
                self.assertTrue(edge['available'])
                adjacency[edge['u']].append(edge['v'])
                adjacency[edge['v']].append(edge['u'])
            else:
                self.assertAlmostEqual(flow, 0.)
            balance[edge['u']] -= flow
            balance[edge['v']] += flow
        reachable, todo = {0}, [0]
        for node in todo:
            for other in adjacency[node]:
                if other not in reachable:
                    reachable.add(other); todo.append(other)
        energized = {i for i, value in enumerate(solution['energized']) if value}
        self.assertEqual(reachable, energized)
        self.assertEqual(len(chosen), len(energized) - 1)
        for node in graph['nodes'][1:]:
            self.assertAlmostEqual(balance[node], graph['demand_kw'][node] * solution['pickup'][node])

    def test_milp_matches_enumeration_and_physical_transport(self):
        for capacity, served in [(220., 250.), (100., 200.)]:
            with self.subTest(capacity=capacity):
                row = standard.solve_restoration_milp(capacity)
                self.check_network(row)
                self.assertAlmostEqual(row['milp']['served_kw'], served)
                self.assertAlmostEqual(row['milp']['critical_served_kw'], 90.)

    def test_zero_capacity_still_handles_network_and_matches_enumeration(self):
        self.check_network(standard.solve_restoration_milp(0.))

    def test_invalid_capacity_rejected(self):
        for capacity in (-1., float('nan'), float('inf')):
            with self.subTest(capacity=capacity), self.assertRaises(ValueError):
                standard.solve_restoration_milp(capacity)


class VoltageChecks(unittest.TestCase):
    def test_capability_polygon_is_inscribed(self):
        matrix, rhs = standard.capability_polygon()
        # Adjacent-facet intersections expose an erroneously circumscribed polygon.
        for index in range(len(matrix)):
            pair = [index, (index + 1) % len(matrix)]
            vertex = np.linalg.solve(matrix[pair], rhs[pair])
            self.assertLessEqual(float(vertex @ vertex), 1 + 1e-12)
            self.assertTrue(np.all(matrix @ vertex <= rhs + 1e-12))

    def test_linear_adapter_preserves_phase_scope_and_dispatch(self):
        model = standard.PQBackend('lindistflow3')
        zero_q = model.solve([.25, 0.])
        support = model.solve([.25, .05])
        self.assertEqual(zero_q['voltage_ids'], support['voltage_ids'])
        self.assertEqual(len(zero_q['voltage_ids']), 599)
        self.assertEqual(len(set(zero_q['voltage_ids'])), 599)
        self.assertAlmostEqual(support['p_actual_kw'], .25 * model.s_total, places=6)
        self.assertAlmostEqual(support['q_actual_kvar'], .05 * model.s_total, places=6)
        self.assertGreater(np.mean(support['voltages_pu']), np.mean(zero_q['voltages_pu']))
        self.assertTrue(zero_q['accepted'])

    def test_out_of_domain_or_incapable_dispatch_is_rejected(self):
        model = standard.PQBackend('lindistflow3')
        with self.assertRaises(ValueError): model.solve([.5, .9])
        with self.assertRaises(ValueError): model.solve([float('nan'), 0.])
        incapable = model.solve([1., .2])
        self.assertFalse(incapable['accepted'])
        self.assertEqual(incapable['violations']['inverter_capability'], 1)

    def test_optimized_linear_point_has_fresh_feasible_evidence(self):
        row = standard.run_voltvar('lindistflow3')
        self.assertTrue(row['validation']['fresh_backend_accepted'])
        independent = standard.PQBackend('lindistflow3').solve(row['optimized']['control'])
        self.assertTrue(independent['accepted'])
        np.testing.assert_allclose(independent['voltages_pu'], row['optimized']['voltages_pu'], atol=1e-12)
        for step in row['solver_trace']:
            if step['disposition'] == 'accepted_fresh_backend_solve':
                self.assertLessEqual(step['objective_after'], step['objective_before'] + 1e-9)


if __name__ == '__main__':
    unittest.main(verbosity=2)
