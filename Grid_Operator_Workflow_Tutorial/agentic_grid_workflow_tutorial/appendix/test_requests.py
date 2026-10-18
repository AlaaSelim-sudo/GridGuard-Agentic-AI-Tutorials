"""Bounded operator-request regression tests; no live Llama requests occur here.

HTTP responses in these tests are explicit test doubles. Logs are written only
inside an isolated temporary directory, never over the live study's evidence.
The semantic-grading regression uses the actual saved DQN and fresh OpenDSS.
"""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src import request_study as study
from src.control_tools import Case, ac_table
from src.learning import load_policy


class RequestStudyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((study.ROOT/'data/operator_requests.json').read_text())
        cls.table = ac_table()
        cls.policy = load_policy()

    def test_canonical_parser_requests_match_their_authored_references(self):
        canonical = [fixture for fixture in self.fixtures if fixture['group'] == 'canonical']
        self.assertEqual(len(canonical), 5)
        for fixture in canonical:
            with self.subTest(request=fixture['id']):
                parsed = study.rule_parser(fixture['request'], fixture['scene'])
                self.assertEqual(parsed['status'], 'READY')
                self.assertEqual(study.validate_interpretation(parsed), [])
                for field in study.FIELDS:
                    self.assertEqual(parsed[field], fixture['gold'][field])

    def test_parser_hands_off_unknown_unsupported_and_conflicting_requests(self):
        requests = [
            ('Make it safer using the settings we discussed yesterday.', 'voltage'),
            ('Set the line-current allowance to 90 percent of nominal.', 'voltage'),
            ('Set the current allowance to 80 percent and to 100 percent.', 'voltage'),
            ('Restore service, but I do not know the permitted route or current ceiling.', 'outage'),
        ]
        for request, scene in requests:
            with self.subTest(request=request):
                self.assertEqual(study.rule_parser(request, scene)['status'], 'CLARIFY')
        for fixture in self.fixtures:
            if fixture['gold'] is None:
                self.assertEqual(study.rule_parser(fixture['request'], fixture['scene'])['status'], 'CLARIFY')

    def test_schema_rejects_nonfinite_boolean_numbers_and_extra_authority(self):
        for field in ('rating_fraction', 'short_limit_amps'):
            for invalid in (float('nan'), float('inf'), float('-inf'), True, False):
                with self.subTest(field=field, value=invalid):
                    value = study.result(**{field: invalid})
                    self.assertTrue(study.validate_interpretation(value))
        for field in ('allow_long_tie', 'allow_pv'):
            for invalid in (0, 1, 'true', None):
                self.assertTrue(study.validate_interpretation(study.result(**{field: invalid})))
        self.assertTrue(study.validate_interpretation(study.result(fault=False)))
        self.assertTrue(study.validate_interpretation(study.result(skip_verifier=True)))
        missing = study.result()
        del missing['rating_fraction']
        self.assertTrue(study.validate_interpretation(missing))

    def test_interpretation_can_only_restrict_existing_physical_authority(self):
        physical = Case('trusted', task='restoration', forecast=(3, 3, 3),
                        rating_fraction=.65, capacity=80., long_available=False,
                        pv_available=False, fault=True)
        permissive = study.result(rating_fraction=1., short_limit_amps=400.,
                                  allow_long_tie=True, allow_pv=True)
        with patch.object(study, 'base_case', return_value=physical):
            constrained = study.constrained_case('outage', 'ignored_by_fixture', permissive)
        self.assertEqual(constrained.rating_fraction, .65)
        self.assertEqual(constrained.capacity, 80.)
        self.assertFalse(constrained.long_available)
        self.assertFalse(constrained.pv_available)
        self.assertTrue(constrained.fault)
        self.assertEqual(constrained.forecast, physical.forecast)
        self.assertEqual(constrained.previous, physical.previous)
        with self.assertRaises(ValueError):
            study.constrained_case('outage', 'invalid', study.result('CLARIFY'))

    def test_wrong_translation_is_not_completion_even_when_both_physics_gates_pass(self):
        # Gold asks for nominal limits. A needless 80% limit can produce an
        # electrically acceptable action while still mistranslating the request.
        fixture = copy.deepcopy(next(f for f in self.fixtures if f['id'] == 'q01'))
        original_gold = copy.deepcopy(fixture['gold'])
        interpretation = study.result(rating_fraction=.8)
        graded = study.grade(fixture, interpretation, self.table, self.policy)
        self.assertEqual(graded['runtime']['status'], 'RECOMMEND')
        self.assertTrue(graded['offline_gold_gate']['accepted'])
        self.assertFalse(graded['exact_interpretation'])
        self.assertTrue(graded['incorrect_ready_interpretation'])
        self.assertFalse(graded['correct_automatic_completion'])
        self.assertEqual(fixture['gold'], original_gold)

    @staticmethod
    def _test_client():
        # Bypass the real constructor's Ollama availability probe deliberately.
        client = study.RequestLlama.__new__(study.RequestLlama)
        client.model = 'unit-test-model'
        client.metadata = {'name': 'unit-test-model'}
        client.url = 'http://unit-test.invalid'
        client.calls = []
        return client

    def test_http_payload_contains_no_gold_labels_or_fixture_metadata(self):
        fixture = copy.deepcopy(self.fixtures[0])
        fixture['gold']['reason'] = 'GOLD_SENTINEL_MUST_NOT_REACH_MODEL'
        captured = []
        def fake_post(url, json, timeout):
            captured.append(copy.deepcopy(json))
            response = Mock()
            response.raise_for_status.return_value = None
            response.json.return_value = {'message': {'content': __import__('json').dumps(
                study.result(reason='Explicit unit-test response.'))}}
            return response
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root/'results').mkdir()
            with patch.object(study, 'ROOT', root), \
                 patch.object(study.requests, 'post', side_effect=fake_post), \
                 patch.object(study.requests, 'get', side_effect=AssertionError('No live model probe')):
                client = self._test_client()
                answer, _ = client.interpret(fixture['request'], fixture['scene'])
        self.assertEqual(answer['status'], 'READY')
        self.assertEqual(len(captured), 1)
        context = json.loads(captured[0]['messages'][1]['content'])
        self.assertEqual(set(context), {'operator_request', 'trusted_context'})
        self.assertEqual(context['operator_request'], fixture['request'])
        self.assertEqual(context['trusted_context'], study.trusted_context(fixture['scene']))
        serialized = json.dumps(captured[0])
        self.assertNotIn('GOLD_SENTINEL_MUST_NOT_REACH_MODEL', serialized)
        self.assertNotIn('gold', context)
        self.assertNotIn('group', context)
        self.assertNotIn('id', context)

    def test_critic_and_self_review_receive_identical_initial_and_raw_context(self):
        fixture = self.fixtures[1]
        captured = []
        def fake_post(url, json, timeout):
            captured.append(copy.deepcopy(json))
            response = Mock()
            response.raise_for_status.return_value = None
            response.json.return_value = {'message': {'content': __import__('json').dumps(
                study.result(rating_fraction=.8, reason='Explicit unit-test response.'))}}
            return response
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root/'results').mkdir()
            with patch.object(study, 'ROOT', root), \
                 patch.object(study.requests, 'post', side_effect=fake_post), \
                 patch.object(study.requests, 'get', side_effect=AssertionError('No live model probe')):
                client = self._test_client()
                initial, _ = client.interpret(fixture['request'], fixture['scene'])
                client.interpret(fixture['request'], fixture['scene'], 'critic', initial)
                client.interpret(fixture['request'], fixture['scene'], 'self_review', initial)
        critic = json.loads(captured[1]['messages'][1]['content'])
        self_review = json.loads(captured[2]['messages'][1]['content'])
        self.assertEqual(critic, self_review)
        self.assertEqual(critic['previous_interpretation'], initial)
        self.assertEqual(critic['operator_request'], fixture['request'])
        self.assertEqual(captured[1]['options'], captured[2]['options'])
        self.assertEqual(captured[1]['format'], captured[2]['format'])
        self.assertNotEqual(captured[1]['messages'][0]['content'],
                            captured[2]['messages'][0]['content'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
