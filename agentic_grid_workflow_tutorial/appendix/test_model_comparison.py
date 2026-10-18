"""Audit-scope and electrical-identity regressions; no Llama inference.

Most cases use handcrafted electrical evidence. One integration test checks the
actual 100%-PV candidate, separating common MV agreement from LV constraints.
Temporary report output cannot overwrite the recorded study.
"""
import copy
from dataclasses import asdict
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src import model_comparison as comparison
from src.stage_workflow import StageCase


def evidence():
    return {
        'buses': [
            {'bus': 'mv_a', 'vmin': 1., 'vmax': 1.03},
            {'bus': 'mv_b', 'vmin': .94, 'vmax': 1.},
            {'bus': 'lv_a', 'vmin': 1., 'vmax': 1.06},
            {'bus': 'lv_b', 'vmin': 1., 'vmax': 1.02},
        ],
        'lines': [
            {'line': 'mv_line', 'normal_amps': 100., 'max_current_amps': 90., 'loading_pct': 90.},
            {'line': 'lv_line', 'normal_amps': 20., 'max_current_amps': 18., 'loading_pct': 90.},
            {'line': 'island_line', 'normal_amps': 10., 'max_current_amps': 20., 'loading_pct': 200.},
        ],
    }


BASES = {'mv_a': 7.2, 'mv_b': 7.2, 'lv_a': .12, 'lv_b': .12,
         'island_a': .12, 'island_b': .12}
ENDPOINTS = [('mv_line', 'mv_a', 'mv_b'), ('lv_line', 'lv_a', 'lv_b'),
             ('island_line', 'island_a', 'island_b')]


class ComparisonTests(unittest.TestCase):
    def test_scope_uses_bus_voltage_base_and_actual_allowed_current(self):
        classified = comparison.classify_failure_scope(evidence(), .8, BASES, ENDPOINTS, ['voltage', 'thermal'])
        self.assertEqual(classified['voltage_current_failure_scope'], 'MV_AND_LV')
        self.assertEqual(classified['counts']['mv_voltage_buses'], 1)
        self.assertEqual(classified['counts']['lv_voltage_buses'], 1)
        self.assertEqual(classified['counts']['mv_overloaded_lines'], 1)
        self.assertEqual(classified['counts']['lv_overloaded_lines'], 1)
        self.assertEqual(classified['skipped_unenergized_lines'], 1)
        self.assertEqual(classified['other_failure_reasons'], [])

    def test_unknown_or_invalid_scope_is_not_silently_called_lv(self):
        bases = dict(BASES)
        del bases['lv_a']
        classified = comparison.classify_failure_scope(evidence(), 1., bases, ENDPOINTS, ['power_flow'])
        self.assertEqual(classified['counts']['unknown_voltage_buses'], 1)
        self.assertIn('UNCLASSIFIED_EVIDENCE', classified['voltage_current_failure_scope'])
        self.assertEqual(classified['other_failure_reasons'], ['power_flow'])
        damaged = evidence()
        damaged['lines'][0]['max_current_amps'] = float('nan')
        classified = comparison.classify_failure_scope(damaged, 1., BASES, ENDPOINTS)
        self.assertIn('line:mv_line', classified['invalid_rows'])
        with self.assertRaises(ValueError):
            comparison.classify_failure_scope(evidence(), 0., BASES, ENDPOINTS)

    @staticmethod
    def paired_evidence():
        prediction = {
            'node_phase_voltages': [{'bus': 'BUS_A', 'phase': 2, 'v_pu': 1.02},
                                    {'bus': 'bus_a', 'phase': 1, 'v_pu': 1.01}],
            'lines': [{'line': 'LINE_A', 'max_current_amps': 14.}],
        }
        audit = {
            'node_phase_voltages': [{'bus': 'bus_a', 'phase': 1, 'v_pu': 1.},
                                    {'bus': 'bus_a', 'phase': 2, 'v_pu': 1.04}],
            'lines': [{'line': 'line_a', 'max_current_amps': 10.},
                      {'line': 'lv_only', 'max_current_amps': 100.}],
        }
        return prediction, audit

    def test_pairing_uses_bus_phase_identity_not_row_order(self):
        prediction, audit = self.paired_evidence()
        error, phases, lines = comparison.common_mv_errors(prediction, audit)
        self.assertEqual(error['common_mv_phase_count'], 2)
        self.assertAlmostEqual(error['voltage_mae_pu'], .015)
        self.assertAlmostEqual(error['voltage_max_abs_error_pu'], .02)
        self.assertEqual(error['current_mae_amps'], 4.)
        self.assertEqual(error['common_mv_line_count'], 1)
        self.assertTrue(error['alignment_complete_for_prediction'])
        self.assertEqual(phases[0]['phase'], 2)
        self.assertAlmostEqual(phases[0]['ac_v_pu'], 1.04)
        self.assertEqual(lines[0]['ac_current_amps'], 10.)

    def test_unmatched_duplicate_or_nonfinite_comparison_data_are_visible(self):
        prediction, audit = self.paired_evidence()
        audit['node_phase_voltages'].pop()
        error, _, _ = comparison.common_mv_errors(prediction, audit)
        self.assertEqual(error['unmatched_predicted_mv_phase_count'], 1)
        self.assertEqual(error['unmatched_predicted_mv_phases'], ['bus_a.2'])
        self.assertFalse(error['alignment_complete_for_prediction'])
        prediction, audit = self.paired_evidence()
        audit['node_phase_voltages'].append(dict(audit['node_phase_voltages'][0]))
        with self.assertRaises(ValueError):
            comparison.common_mv_errors(prediction, audit)
        prediction, audit = self.paired_evidence()
        prediction['lines'][0]['max_current_amps'] = float('nan')
        with self.assertRaises(ValueError):
            comparison.common_mv_errors(prediction, audit)

    def test_reference_review_preserves_candidate_and_binds_failure_scope(self):
        prediction, audit = self.paired_evidence()
        candidate = {'tool': 'MPC', 'pv_cap': 100., 'tie': 'none', 'shed_fraction': 0.}
        metrics = {'served_kw': 100., 'vmin': 1., 'vmax': 1.02, 'allowed_current_utilization_pct': 50.}
        row = {'case': 'unit', 'backend': 'lindistflow3', 'method': 'fixed',
               'status': 'RECOMMEND', 'candidate': candidate, 'prediction': prediction,
               'recommendation_id': 'fixed-unit-id', 'trace': [{'inputs': {}}],
               'metrics': metrics, 'model_solves': 1, 'llm_calls': 0, 'seconds': .01}
        audit.update(accepted=False, failures=['thermal'], metrics=dict(metrics), seconds=.01,
                     failure_scope={'voltage_current_failure_scope': 'LV_ONLY', 'counts': {'lv_overloaded_lines': 1}})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'results').mkdir()
            with patch.object(comparison, 'ROOT', root), patch.object(comparison, 'audit_candidate', return_value=audit):
                first, _ = comparison.build_comparison({'runs': [copy.deepcopy(row)]})
                changed = copy.deepcopy(audit)
                changed['failure_scope']['voltage_current_failure_scope'] = 'MV_ONLY'
                with patch.object(comparison, 'audit_candidate', return_value=changed):
                    second, _ = comparison.build_comparison({'runs': [copy.deepcopy(row)]})
        self.assertEqual(first['runs'][0]['candidate'], candidate)
        self.assertEqual(first['runs'][0]['final_review_status'], 'MODEL_DISAGREEMENT_REVIEW')
        self.assertNotEqual(first['runs'][0]['review_id'], second['runs'][0]['review_id'])
        self.assertEqual(first['runs'][0]['trace'][-1]['inputs']['review_id'], first['runs'][0]['review_id'])

    @unittest.skipUnless(importlib.util.find_spec('opendssdirect'), 'Optional actual AC scope audit')
    def test_actual_pv100_ac_failures_are_lv_coverage_gaps(self):
        row = {'case_definition': asdict(StageCase('unit_pv100')),
               'candidate': {'tool': 'MPC', 'pv_cap': 100., 'tie': 'none', 'shed_fraction': 0.}}
        audit = comparison.audit_candidate(row)
        self.assertFalse(audit['accepted'])
        classified = audit['failure_scope']
        self.assertEqual(classified['voltage_current_failure_scope'], 'LV_ONLY')
        self.assertEqual(classified['counts']['mv_voltage_buses'], 0)
        self.assertEqual(classified['counts']['mv_overloaded_lines'], 0)
        self.assertGreater(classified['counts']['lv_voltage_buses'], 0)
        self.assertGreater(classified['counts']['lv_overloaded_lines'], 0)
        self.assertEqual(classified['invalid_rows'], [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
