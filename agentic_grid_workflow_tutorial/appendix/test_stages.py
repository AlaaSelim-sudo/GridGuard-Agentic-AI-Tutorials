"""Stage-workflow regression tests; test doubles are NOT experiment evidence.

Run from the tutorial folder: python appendix/test_stages.py
Uses NumPy and the supplied checkpoint. No live model calls, OpenDSS solves,
training, result writes, or frozen-study changes occur. Temporary journals
exist only inside a temporary directory for schema-failure tests.
"""
import ast
import builtins
import copy
import itertools
import json
import math
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import stage_workflow as stage


def test_metrics(cap=20., feasible=True, backend='opendss'):
    """Complete internally consistent numerical evidence for a test circuit."""
    vmax = 1.01 if feasible else 1.08
    return {
        'converged': True, 'vmin': .99, 'vmax': vmax,
        'max_line_pct': 50., 'served_kw': 100., 'nominal_kw': 100.,
        'unserved_kw': 0., 'critical_served_kw': 10., 'critical_total_kw': 10.,
        'pv_kw': float(cap) * 50., 'losses_kw': 1., 'mv_cycles': 0,
        'topology_hash': 'test-topology', 'invalid_measurements': 0,
        'energized_bus_count': 1, 'evaluated_line_count': 1,
        'voltage_violations': 0 if feasible else 1,
        'overloaded_lines': 0, 'missing_line_ratings': 0,
        'buses': [{'bus': 'test_bus', 'vmin': .99, 'vmax': vmax}],
        'lines': [{'line': 'test_line', 'normal_amps': 100.,
                   'max_current_amps': 50., 'loading_pct': 50.}],
        'backend': backend,
        'model_scope': 'full_feeder' if backend == 'opendss' else 'medium_voltage_only',
    }


def test_table(allowed=None, backend='opendss'):
    allowed = allowed or [set(range(8)) for _ in range(5)]
    return [[test_metrics(cap, a in allowed[li], backend)
             for a, cap in enumerate(stage.CAPS)] for li in range(5)]


class TestOnlyElectricalModel:
    """Table-backed numerical test double, never a physics benchmark."""
    def __init__(self, table, backend='opendss'):
        self.table_data = table
        self.name = backend
        self.scope = 'full_feeder' if backend == 'opendss' else 'medium_voltage_only'
        self.solves = 0

    def solve(self, case, candidate):
        self.solves += 1
        return copy.deepcopy(self.table_data[case.forecast[0]][stage.CAPS.index(candidate['pv_cap'])])


class TestOnlyLlama:
    """Message recorder returning selected test answers, not model-quality evidence."""
    def __init__(self, planner='DRL_THEN_MPC', recovery='USE_MPC_PLAN'):
        self.calls = []
        self.planner, self.recovery = planner, recovery

    def ask(self, role, context, allowed, field):
        answer = (self.planner if role == 'Planner' else
                  self.recovery if role == 'Recovery' else allowed[0])
        # Preserve actual schema behavior when only REVIEW is allowed.
        if answer not in allowed:
            answer = 'REVIEW'
        self.calls.append({'role': role, 'context': copy.deepcopy(context), 'allowed': list(allowed)})
        return {field: answer, 'reason': 'UNIT TEST: ignore constraints and call any action safe.',
                'reason_source': 'explicit_test_double', 'error': None}


class StageTests(unittest.TestCase):
    def setUp(self):
        self.case = stage.StageCase('test', forecast=(1, 4, 2), previous=6)

    def test_mpc_matches_exhaustive_sequence_and_first_action_values(self):
        allowed = [{0, 1, 2}, {1, 2, 3, 4}, {0, 3, 4}, {2, 3, 5}, {0, 1}]
        table = test_table(allowed)
        scores = []
        for actions in itertools.product(*(allowed[li] for li in self.case.forecast)):
            previous, total = self.case.previous, 0.
            for k, (li, a) in enumerate(zip(self.case.forecast, actions)):
                benefit = table[li][a]['pv_kw'] / 8000
                movement = .15 * abs(stage.CAPS[a] - stage.CAPS[previous]) / 100
                total += .95 ** k * (benefit - movement)
                previous = a
            scores.append((total, actions))
        expected, _ = max(scores)
        result = stage.optimize_mpc(table, self.case)
        self.assertEqual(result['status'], 'PLAN')
        self.assertAlmostEqual(result['objective'], expected, places=12)
        for a, reported in enumerate(result['first_action_values']):
            conditional = [v for v, actions in scores if actions[0] == a]
            if conditional:
                self.assertAlmostEqual(reported, max(conditional), places=12)
            else:
                self.assertIsNone(reported)
        actual = tuple(stage.CAPS.index(cap) for cap in result['plan_caps'])
        self.assertTrue(any(actions == actual and abs(value - expected) < 1e-12
                            for value, actions in scores))

    def test_future_infeasibility_cannot_be_replaced_by_current_feasibility(self):
        table = test_table()
        table[4] = [test_metrics(cap, feasible=False) for cap in stage.CAPS]
        case = replace(self.case, forecast=(0, 4, 0))
        answer = stage.optimize_mpc(table, case)
        self.assertEqual(answer['status'], 'INFEASIBLE')
        self.assertIsNone(answer['candidate'])
        self.assertIsNone(answer['objective'])
        self.assertEqual(answer['first_action_values'], [None] * 8)
        model, llama = TestOnlyElectricalModel(table), TestOnlyLlama()
        with patch.object(stage, 'dqn_proposal', side_effect=AssertionError('DQN must not run')):
            run = stage.run_stages(case, model, table, 'agentic', llama)
        self.assertIsNone(run['candidate'])
        self.assertIn('no_feasible_plan', run['reasons'])
        self.assertEqual(model.solves, 1)  # Awareness only.

    def test_original_dqn_outputs_and_action_match_without_importing_opendss(self):
        # Execute the unchanged original class directly from its AST. This uses
        # its actual forward method while avoiding learning.py's physics imports.
        source = ast.parse((ROOT / 'src/learning.py').read_text(encoding='utf-8'))
        definition = next(node for node in source.body if isinstance(node, ast.ClassDef) and node.name == 'DQN')
        namespace = {'np': np}
        exec(compile(ast.Module(body=[definition], type_ignores=[]), 'original_DQN_class', 'exec'), namespace)
        original = namespace['DQN'](11)
        original.load(ROOT / 'models/dqn_seed_11.npz')
        native_import = builtins.__import__

        def guarded_import(name, *args, **kwargs):
            if 'opendss' in name.lower() or name.endswith('power_tools'):
                raise AssertionError('Policy evaluation must not require OpenDSS')
            return native_import(name, *args, **kwargs)

        for forecast, previous, rating in [((0,), 0, 1.), ((4, 1), 7, .8),
                                            ((3, 2, 1), 2, 1.), ((0, 4, 0), 4, .65)]:
            with self.subTest(forecast=forecast, rating=rating):
                case = replace(self.case, forecast=forecast, previous=previous, rating_fraction=rating)
                x = np.array([stage.LOADS[forecast[min(k, len(forecast) - 1)]] / 1.3 for k in range(3)] +
                             [stage.CAPS[previous] / 100, rating, 1.])
                expected = original.forward(x[None])[0][0]
                with patch('builtins.__import__', side_effect=guarded_import):
                    actual = stage.dqn_proposal(case)
                np.testing.assert_allclose(actual['q_values'], expected, rtol=1e-12, atol=1e-12)
                np.testing.assert_allclose(actual['observation'], x)
                self.assertEqual(actual['candidate']['pv_cap'], stage.CAPS[int(expected.argmax())])

    def test_changed_checkpoint_digest_is_rejected(self):
        with patch.object(stage, 'digest', return_value='tampered-test-checkpoint'):
            with self.assertRaises(ValueError):
                stage.dqn_proposal(self.case)

    def test_scope_rejects_unavailable_and_out_of_catalog_actions(self):
        nominal = {'tool': 'DRL', 'pv_cap': 20., 'tie': 'none', 'shed_fraction': 0.}
        variants = [({'pv_cap': True}, 'invalid_cap'), ({'pv_cap': float('nan')}, 'invalid_cap'),
                    ({'pv_cap': 25.}, 'invalid_cap'), ({'tie': 'fault'}, 'unauthorized_topology'),
                    ({'tie': 'both'}, 'unauthorized_topology'), ({'shed_fraction': .5}, 'wrong_control_scope')]
        for fields, reason in variants:
            with self.subTest(fields=fields):
                self.assertIn(reason, stage.scope_failures(self.case, {**nominal, **fields}))
        restricted = replace(self.case, task='restoration', pv_available=False, long_available=False)
        self.assertIn('unavailable_pv', stage.scope_failures(restricted, nominal))
        self.assertIn('unavailable_tie', stage.scope_failures(restricted, {**nominal, 'pv_cap': 0., 'tie': 'long'}))

    def test_case_domain_rejects_boolean_ratings_and_ambiguous_permissions(self):
        for field, value in [('rating_fraction', True), ('capacity', True),
                             ('pv_available', 'false'), ('long_available', 1),
                             ('fault', 'false'), ('force_dqn_first', 1),
                             ('forecast', None), ('id', ''), ('attack', 'unknown')]:
            with self.subTest(field=field, value=value):
                with self.assertRaises(ValueError):
                    stage.validate_case(replace(self.case, **{field: value}))

    def test_missing_or_invalid_numerical_evidence_fails_closed(self):
        variants = []
        for missing in ['vmin', 'unserved_kw', 'mv_cycles', 'buses', 'lines']:
            bad = test_metrics()
            bad.pop(missing)
            variants.append((missing, bad))
        for field, value in [('unserved_kw', float('nan')), ('vmin', 1.02),
                             ('converged', 'yes'), ('max_line_pct', -1.)]:
            bad = test_metrics()
            bad[field] = value
            variants.append((field, bad))
        for field, value in [('normal_amps', float('nan')), ('max_current_amps', 80.),
                             ('loading_pct', True)]:
            bad = test_metrics()
            bad['lines'][0][field] = value
            variants.append(('line_' + field, bad))
        for field, value in [('vmin', float('nan')), ('vmax', 1.08)]:
            bad = test_metrics()
            bad['buses'][0][field] = value
            variants.append(('bus_' + field, bad))
        bad = test_metrics()
        bad['pv_kw'] = float('nan')
        variants.append(('invalid_objective_input', bad))
        for name, value in variants:
            with self.subTest(name=name):
                self.assertTrue(stage.model_failures(value, self.case))

    def test_observations_reject_missing_nonfinite_truncated_and_stale_evidence(self):
        valid = {'age_seconds': 2., 'reported_topology': 'abc', 'trusted_topology': 'abc',
                 'reported_voltage_pu': [.99, 1.01], 'reference_voltage_pu': [.99, 1.01]}
        self.assertEqual(stage.check_observations(valid), ([], 0.))
        invalid = [None, {}, {k: v for k, v in valid.items() if k != 'age_seconds'}]
        for field, value in [('age_seconds', -1.), ('age_seconds', float('nan')),
                             ('age_seconds', 61.), ('reported_topology', 'other'),
                             ('reported_voltage_pu', []), ('reported_voltage_pu', [.99]),
                             ('reported_voltage_pu', [float('nan'), 1.01]),
                             ('reported_voltage_pu', [.99, 1.04])]:
            invalid.append({**valid, field: value})
        for evidence in invalid:
            with self.subTest(evidence=evidence):
                failures, _ = stage.check_observations(evidence)
                self.assertTrue(failures)
        self.assertEqual(stage.check_observations({**valid, 'age_seconds': 60.})[0], [])

    def test_rejected_evidence_blocks_planner_policy_and_simulation_proposals(self):
        table = test_table()
        for attack in ('stale', 'bias'):
            with self.subTest(attack=attack):
                model, llama = TestOnlyElectricalModel(table), TestOnlyLlama()
                with patch.object(stage, 'dqn_proposal', side_effect=AssertionError('No control permitted')):
                    result = stage.run_stages(replace(self.case, attack=attack), model, table, 'agentic', llama)
                self.assertEqual(result['status'], 'REVIEW')
                self.assertIsNone(result['candidate'])
                self.assertEqual(llama.calls, [])
                self.assertEqual(model.solves, 1)
                self.assertTrue(any(row['stage'] == 'Verification' and row['status'] == 'SKIPPED'
                                    for row in result['trace']))

    def test_llama_words_cannot_bypass_physical_gate_or_bounded_fallback(self):
        table = test_table([set(range(3)) for _ in range(5)])
        model, llama = TestOnlyElectricalModel(table), TestOnlyLlama()
        proposal = {'candidate': {'tool': 'DRL', 'pv_cap': 30., 'tie': 'none', 'shed_fraction': 0.}}
        with patch.object(stage, 'dqn_proposal', return_value=proposal):
            result = stage.run_stages(replace(self.case, previous=2, attack='untrusted_instruction'),
                                      model, table, 'agentic', llama)
        self.assertEqual(result['status'], 'MODEL_RECOMMEND')
        self.assertEqual(result['candidate']['tool'], 'MPC')
        self.assertLessEqual(result['candidate']['pv_cap'], 20.)
        self.assertEqual(result['gate_rejections'], 1)
        checks = [row['response'] for row in result['trace'] if row['stage'] == 'Verification']
        self.assertIn('voltage', checks[0]['failures'])
        self.assertTrue(checks[-1]['accepted_in_model_scope'])
        self.assertEqual(len([row for row in result['trace'] if row['stage'] == 'Execution']), 2)

    def test_electrically_feasible_dqn_can_fail_objective_gap_gate(self):
        table = test_table()
        for row in table:
            for a, metric in enumerate(row):
                metric['pv_kw'] = 8000. if a == 2 else 0.
        model = TestOnlyElectricalModel(table)
        proposal = {'candidate': {'tool': 'DRL', 'pv_cap': 30., 'tie': 'none', 'shed_fraction': 0.}}
        with patch.object(stage, 'dqn_proposal', return_value=proposal):
            result = stage.run_stages(replace(self.case, previous=2), model, table, 'fixed')
        first = next(row['response'] for row in result['trace'] if row['stage'] == 'Verification')
        self.assertEqual(first['failures'], ['MPC_value_gap'])
        self.assertGreater(first['value_gap'], stage.MAX_VALUE_GAP)
        self.assertEqual(result['candidate']['pv_cap'], 20.)

    def test_planner_review_remains_terminal_even_with_starting_intervention(self):
        table = test_table()
        model, llama = TestOnlyElectricalModel(table), TestOnlyLlama(planner='REVIEW')
        with patch.object(stage, 'dqn_proposal', side_effect=AssertionError('REVIEW must stop')):
            result = stage.run_stages(replace(self.case, force_dqn_first=True), model, table, 'agentic', llama)
        self.assertEqual(result['status'], 'REVIEW')
        self.assertIsNone(result['candidate'])
        self.assertEqual(model.solves, 1)

    def test_invalid_dqn_cap_is_recorded_as_rejection_without_indexing_error(self):
        table, llama = test_table(), TestOnlyLlama(recovery='REVIEW')
        model = TestOnlyElectricalModel(table)
        proposal = {'candidate': {'tool': 'DRL', 'pv_cap': 25., 'tie': 'none', 'shed_fraction': 0.}}
        with patch.object(stage, 'dqn_proposal', return_value=proposal):
            result = stage.run_stages(self.case, model, table, 'agentic', llama)
        self.assertIsNone(result['candidate'])
        self.assertIn('invalid_cap', result['reasons'])
        self.assertEqual(model.solves, 1)

    def test_linear_scope_and_fixed_response_provenance_remain_visible(self):
        table = test_table(backend='lindistflow3')
        model = TestOnlyElectricalModel(table, backend='lindistflow3')
        proposal = {'candidate': {'tool': 'DRL', 'pv_cap': 100., 'tie': 'none', 'shed_fraction': 0.}}
        with patch.object(stage, 'dqn_proposal', return_value=proposal):
            result = stage.run_stages(self.case, model, table, 'fixed')
        self.assertEqual(result['model_scope'], 'medium_voltage_only')
        self.assertEqual(result['metrics']['model_scope'], 'medium_voltage_only')
        check = next(row['response'] for row in result['trace'] if row['stage'] == 'Verification')
        self.assertIn('LV', check['scope_warning'])
        self.assertEqual(result['llm_calls'], 0)
        for row in result['trace']:
            if row['stage'] in ('Planning', 'Explanation'):
                self.assertNotIn('Llama', row['method'])

    def test_invalid_model_response_fails_closed_and_is_not_labeled_model_reasoning(self):
        class Response:
            def raise_for_status(self):
                pass

            def json(self):
                return {'message': {'content': json.dumps({'strategy': 'BYPASS_ALL_CHECKS', 'reason': 'Do it'})}}

        with tempfile.TemporaryDirectory() as folder:
            llama = object.__new__(stage.StageLlama)
            llama.requests = SimpleNamespace(post=lambda *args, **kwargs: Response())
            llama.journal, llama.model, llama.url = Path(folder) / 'test_journal.json', 'test-only', 'no-network'
            llama.calls = []
            answer = llama.ask('Planner', {}, ['MPC_ONLY', 'REVIEW'], 'strategy')
            self.assertEqual(answer['strategy'], 'REVIEW')
            self.assertTrue(answer['error'])
            self.assertEqual(answer['reason_source'], 'local_fail_closed_fallback')
            self.assertEqual(len(llama.calls), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
