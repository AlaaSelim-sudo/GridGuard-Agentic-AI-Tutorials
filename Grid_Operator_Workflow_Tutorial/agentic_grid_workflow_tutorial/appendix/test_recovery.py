"""Recovery regression tests. All doubles are confined to this test file.

No Llama requests or checkpoint writes occur here. The published recovery study
uses the actual saved trained DQN and live local Llama through recovery_study.main.
"""
import copy
from dataclasses import replace
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src import recovery_study as study
from src.control_tools import Case, ac_table


class TestOnlyPolicy:
    """A fixed 30% proposal for boundary tests, not a trained policy."""
    def forward(self, x):
        values = np.zeros((len(x), 8))
        values[:, 3] = 1.
        return values, None


class TestOnlyLlama:
    def __init__(self):
        self.calls = []

    def ask(self, role, context, seed=11):
        available = context['available_tools']
        selected = next((tool for tool in available if tool != 'REVIEW'), 'REVIEW')
        field = 'repair_tool' if role == 'Critic' else 'tool'
        response = {field: selected, 'reason': 'Unit-test scripted response.'}
        self.calls.append({'role': role, 'context': copy.deepcopy(context),
                           'response': copy.deepcopy(response), 'seconds': 0.})
        return response


class RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.table = ac_table()
        cls.policy = TestOnlyPolicy()

    def test_injected_unavailability_is_structured_and_does_not_call_controller(self):
        case = replace(study.CASES[0], injected_delay_seconds=0.)
        with patch.object(study, 'mpc', side_effect=AssertionError('Unavailable service called')):
            result = study.call_tool(case, 'MPC', self.table, self.policy)
        self.assertEqual(result['status'], 'TOOL_UNAVAILABLE')
        self.assertIsNone(result['candidate'])
        self.assertTrue(result['injected_failure'])
        self.assertEqual(result['fresh_ac_solves'], 0)
        self.assertIn('injected', result['reason'])

    def test_single_pass_stops_safely_and_adaptive_rules_recover(self):
        for case in study.CASES:
            with self.subTest(case=case.id):
                single = study.run_recovery(case, self.table, self.policy, 'single_pass')
                repaired = study.run_recovery(case, self.table, self.policy, 'adaptive_rules')
                self.assertEqual(single['tool_calls'], 1)
                self.assertIsNone(single['candidate'])
                self.assertFalse(single['verified_completion'])
                self.assertEqual(repaired['tool_calls'], 2)
                self.assertEqual(repaired['status'], 'RECOMMEND')
                self.assertTrue(repaired['verified_completion'])
                self.assertEqual(repaired['llm_calls'], 0)
                self.assertLessEqual(repaired['metrics']['max_line_pct'], 100+1e-4)

    def test_agent_repair_passes_critic_feedback_to_planner(self):
        for case in study.CASES:
            with self.subTest(case=case.id):
                llama = TestOnlyLlama()
                result = study.run_recovery(case, self.table, self.policy, 'agent_loop', llama)
                self.assertTrue(result['verified_completion'])
                self.assertEqual(result['tool_calls'], 2)
                self.assertEqual(result['llm_calls'], 2)
                self.assertEqual([row['role'] for row in llama.calls], ['Critic', 'Planner'])
                self.assertEqual(llama.calls[1]['context']['critic_feedback'],
                                 llama.calls[0]['response'])
                self.assertNotIn(case.initial_tool, llama.calls[1]['context']['available_tools'])

    def test_electrical_rejection_is_real_not_an_injected_tool_outage(self):
        result = study.run_recovery(study.CASES[2], self.table, self.policy, 'adaptive_rules')
        self.assertEqual(result['unavailable_responses'], 0)
        self.assertEqual(result['gate_rejections'], 1)
        self.assertEqual(result['injected_delay_seconds'], 0)
        gates = [row for row in result['trace'] if row['role'] == 'Verification']
        self.assertEqual(len(gates), 2)
        self.assertFalse(gates[0]['accepted'])
        self.assertIn('thermal', gates[0]['reasons'])
        self.assertGreater(gates[0]['metrics']['max_line_pct'], 100)
        self.assertTrue(gates[1]['accepted'])
        self.assertEqual(result['candidate']['pv_cap'], 20)

    def test_infeasible_mpc_horizon_never_falls_back_to_myopic_drl(self):
        case = study.RecoveryCase('unit_infeasible', 'Unit-test fixture.',
                                 Case('unit', forecast=(0, 4, 0), rating_fraction=.65), 'MPC')
        llama = TestOnlyLlama()
        with patch.object(study, 'drl', side_effect=AssertionError('Improper myopic fallback')):
            result = study.run_recovery(case, self.table, self.policy, 'agent_loop', llama)
        self.assertEqual(result['status'], 'ESCALATE')
        self.assertIsNone(result['candidate'])
        self.assertEqual(result['tool_calls'], 1)
        self.assertEqual(result['llm_calls'], 0)
        self.assertIn('no_feasible_horizon', result['reasons'])

    def test_agent_mode_requires_explicit_model(self):
        with self.assertRaises(ValueError):
            study.run_recovery(study.CASES[0], self.table, self.policy, 'agent_loop')


if __name__ == '__main__':
    unittest.main(verbosity=2)
