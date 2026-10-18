"""Explicit test doubles for routing/failure boundaries, not experiment evidence."""
import unittest
from unittest.mock import patch
from src.standard_agent_workflow import run_case


class TestStandardWorkflowBoundaries(unittest.TestCase):
    def test_cross_application_route_cannot_invoke_numerical_tool(self):
        class WrongRoute:
            def ask(self, *args):
                return {'choice': 'RESTORATION_MILP', 'reason': 'test-only incompatible route'}
        with patch('src.standard_agent_workflow.numerical_tool') as numerical:
            result = run_case('voltage', supervisor='agentic', llama=WrongRoute())
            numerical.assert_not_called()
        self.assertEqual(result['status'], 'REVIEW')
        self.assertEqual(len(result['trace']), 8)
        self.assertFalse(result['trace'][-1]['response']['dispatch_authorized'])

    def test_tool_failure_preserves_review_without_candidate(self):
        with patch('src.standard_agent_workflow.numerical_tool', side_effect=RuntimeError('test-only unavailable solver')):
            result = run_case('restoration')
        self.assertEqual(result['status'], 'REVIEW')
        self.assertIsNone(result['numerical_evidence'])
        self.assertIn('unavailable solver', result['summary']['error'])
        self.assertEqual(len(result['trace']), 8)

    def test_agentic_mode_cannot_silently_use_fixed_fallback(self):
        with self.assertRaises(ValueError):
            run_case('cyber', supervisor='agentic')

    def test_explanation_cannot_override_failed_engineering_check(self):
        class AlwaysReport:
            def ask(self, role, *args):
                return {'choice': 'VOLTVAR_OPF' if role == 'Planning' else 'REPORT_LIMITS',
                        'reason': 'test-only response'}
        with patch('src.standard_agent_workflow.numerical_tool', return_value=(
                {'test_double': True}, {'violations': {'line_current': 1}}, False, {'fresh_backend_accepted': False})):
            result = run_case('voltage', supervisor='agentic', llama=AlwaysReport())
        self.assertEqual(result['status'], 'REVIEW')
        self.assertEqual(next(s for s in result['trace'] if s['stage'] == 'Verification')['status'], 'REJECT')
        self.assertFalse(result['trace'][-1]['response']['equipment_operated'])


if __name__ == '__main__':
    unittest.main()
