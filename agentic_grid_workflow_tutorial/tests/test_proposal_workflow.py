"""Independent orchestration checks; synthetic doubles, not electrical/LLM results."""
import importlib.util
from copy import deepcopy
import json
import math
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src import proposal_workflow as engine


class Adapter:
    scope = 'test scope'
    objective = 'minimize cost'
    def __init__(self, mode='normal'):
        self.mode, self.calls, self.setup = mode, 0, {}
    def awareness(self):
        return {'fixed_limit': 1.0}
    def plan(self):
        return [{'cost': 10., 'x': .8}, {'cost': 5., 'x': .6}]
    def simulate(self, candidate):
        self.calls += 1
        return {'predicted': candidate['x'], 'solve': self.calls}
    def summary(self, candidate, evidence):
        return {'value': evidence['predicted'],
                'offline_truth_audit': {'truth_secret': 123.456}}
    def verify(self, candidate, evidence):
        if self.mode == 'reject_all':
            return ['fixture_rejected']
        if self.mode == 'final_reject' and self.calls == 5:
            return ['fixture_final_failure']
        if self.mode == 'mutate_candidate':
            candidate['x'] += .01
        if self.mode == 'mutate_evidence':
            evidence['predicted'] += .01
        return []
    def score(self, candidate, evidence):
        if self.mode == 'nan_score':
            return math.nan
        if self.mode == 'bool_score':
            return True
        if self.mode == 'score_mutation':
            evidence['predicted'] += .01
        return candidate['cost']
    def operations(self, evaluations):
        return {'O1': 'Improve', 'O2': 'Trial'}
    def fixed_choice(self, evaluations, offered):
        return next(iter(offered))
    def propose(self, operation, evaluations):
        return {'cost': 2. if operation == 'O1' else 4., 'x': .4}


class Client:
    model = 'TEST_DOUBLE'
    def __init__(self, mode='normal'):
        self.calls, self.mode = [], mode
    def ask(self, role, context, choices, ranking=False):
        self.calls.append({'role': role, 'context': deepcopy(context)})
        if self.mode == 'mutate_contract' and role == 'Planning Agent':
            context['contract']['awareness']['fixed_limit'] = 999.
        if ranking:
            value = choices[::-1] if self.mode == 'reverse' else choices
            if self.mode == 'duplicate':
                value = [choices[0]] * len(choices)
            if self.mode == 'unknown':
                value = ['UNKNOWN'] + choices[1:]
            return {'ranking': value, 'reason': 'TEST_DOUBLE', 'source': 'test_double'}
        return {'choice': choices[0], 'reason': 'TEST_DOUBLE', 'source': 'test_double'}


def run(mode='normal', client=None):
    adapter = Adapter(mode)
    original = sys.modules.get('src.proposal_case_tools')
    sys.modules['src.proposal_case_tools'] = types.SimpleNamespace(make_adapter=lambda *args: adapter)
    try:
        result = engine.run_proposal_case('fixture', 'fixture',
            supervisor='agentic' if client else 'fixed', client=client)
    finally:
        if original is None:
            sys.modules.pop('src.proposal_case_tools')
        else:
            sys.modules['src.proposal_case_tools'] = original
    return result


def inspect(result):
    selected = result['selected']
    candidate_binding = all(engine.canonical_hash({'contract_id': result['contract_id'],
        'candidate': row['candidate']}) == row['candidate_hash'] for row in result['evaluations'])
    evidence_binding = all(engine.canonical_hash(row['evidence']) == row['evidence_hash']
        for row in result['evaluations'])
    return {'status': result['status'], 'selected_cost': selected['score'] if selected else None,
        'candidate_binding': candidate_binding, 'evidence_binding': evidence_binding,
        'counts': result['counts'], 'calls': result['llm_calls']}


findings = {}
for mode in ('normal', 'reject_all', 'final_reject', 'nan_score', 'bool_score', 'mutate_candidate',
             'mutate_evidence', 'score_mutation'):
    findings[mode] = inspect(run(mode))
for mode in ('normal', 'reverse', 'duplicate', 'unknown', 'mutate_contract'):
    client = Client(mode)
    findings['llm_' + mode] = inspect(run(client=client))
    findings['llm_' + mode]['offline_truth_in_context'] = any(
        'offline_truth_audit' in json.dumps(call['context']) or
        'truth_secret' in json.dumps(call['context']) for call in client.calls)

for name, result in findings.items():
    should_recommend = name in ('normal', 'llm_normal', 'llm_reverse')
    assert result['status'] == ('MODEL_RECOMMEND' if should_recommend else 'REVIEW'), (name, result)
    assert result['counts']['initial'] <= 2 and result['counts']['refinement'] <= 2
    assert result['counts']['final_recheck'] <= 1
    assert not result.get('offline_truth_in_context'), name
    if should_recommend:
        assert result['selected_cost'] == 2.
        assert result['candidate_binding'] and result['evidence_binding']
target = Path(__file__).with_name('audit_engine_results.json')
target.write_text(json.dumps(findings, indent=2), encoding='utf8')
print(json.dumps(findings, indent=2))
