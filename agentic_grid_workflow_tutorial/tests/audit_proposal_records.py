"""Independently validate completed five-stage records without re-running physics."""
from pathlib import Path
import json
import hashlib
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.proposal_workflow import canonical_hash

suite=json.loads((ROOT/'results/proposal_complete_workflow.json').read_text())
pilot=json.loads((ROOT/'results/proposal_contract_pilot.json').read_text())
assert len(suite['runs'])==12 and len(pilot['runs'])==12
assert all(hashlib.sha256((ROOT/'src'/n).read_bytes()).hexdigest()==h for n,h in suite['source_sha256'].items())
all_runs=suite['runs']+[suite['model_portability_example']]
rows=[]
for run in all_runs:
    assert canonical_hash(run['contract'])==run['contract_id']
    assert run['counts']=={'initial':2,'refinement':2,'final_recheck':1}
    assert all(run['core_stage_coverage'].values())
    assert run['operator']['acknowledged'] is False
    assert run['operator']['dispatch_authorized'] is False
    search=[]
    for row in run['evaluations']:
        assert row['candidate_hash']==canonical_hash({'contract_id':run['contract_id'],'candidate':row['candidate']})
        assert row['evidence_hash']==canonical_hash(row['evidence'])
        assert row['failures'] or (type(row['score']) in (int,float) and math.isfinite(row['score']))
        if not row['failures'] and row['phase']!='final_independent_recheck':search.append(row)
    expected=sorted(search,key=lambda r:(r['score'],r['id']))
    assert [r['id'] for r in run['ranked_actions']]==[r['id'] for r in expected]
    final=run['evaluations'][-1]
    assert final['phase']=='final_independent_recheck' and not final['failures']
    assert final['candidate']==expected[0]['candidate']
    assert final['candidate_hash']==run['selected']['candidate_hash']
    assert final['evidence_hash']==run['selected']['evidence_hash']
    assert run['status']=='MODEL_RECOMMEND'
    vals=[p['best_cost'] for p in run['progress'] if p['best_cost'] is not None]
    assert all(b<=a+1e-12 for a,b in zip(vals,vals[1:]))
    ranking=next(t['response'] for t in run['trace'] if t['stage']=='LLM Optimizer' and t['response'].get('phase')=='ranking')
    replies=[t['response']['language_response'] for t in run['trace'] if 'language_response' in t.get('response',{})]
    journal_name='qwen_calls.json' if run.get('model','')=='qwen2.5:7b-instruct' else 'llama_calls.json'
    journal=json.loads((ROOT/suite['journal_folder']/journal_name).read_text())
    actual_replies=[r for r in replies if r['source']=='actual_local_llm']
    assert len(actual_replies)==run['llm_calls']
    for response in actual_replies:
        call=next(c for c in journal if c['call_id']==response['call_id'])
        assert call['source']=='actual_local_llm' and not call.get('error')
        assert all(response[k]==v for k,v in call['response'].items())
        assert response['seconds']==call['seconds']
        prompt=call['payload']['messages'][-1]['content']
        for forbidden in ('offline_truth_audit','actual_toy_flows_pu','actual_toy_model_flows_pu','true_state'):
            assert forbidden not in prompt, (run['case'],forbidden)
    rows.append({'case':run['case'],'backend':run['backend'],'route':run['supervisor'],
        'model':run.get('model'),'cost':run['selected']['score'],'seconds':run['seconds'],
        'ranking_agrees':ranking['language_order_agrees_with_cost'],'calls':run['llm_calls']})
summary={'schema':'independent_record_audit_v1','protocol':suite['protocol_version'],
    'source_hashes_match':True,'all_13_runs_bound_and_finally_rechecked':True,
    'all_actual_call_replies_match_journals':True,'oracle_absent_from_actual_llm_contexts':True,
    'pilot_retained':True,'rows':rows}
(Path(__file__).with_name('recorded_suite_audit.json')).write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
