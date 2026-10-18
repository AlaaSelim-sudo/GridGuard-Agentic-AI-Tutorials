"""Separate heldout OpenDSS transfer and distinct final checks for the pilot.

No selector is trained here. The twelve AC contexts reuse their independently
optimized recorded MPC plans, explicitly disclosing the reused planning time.
Fresh first-action trials, actual local LLM responses, and final rechecks are
collected after the original MV experiment. Historical records are untouched.
"""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

from .ensemble_voltage import (ROOT, MODELS, case_from, read, write, sha, evaluate,
    public_evaluation, operation_catalog, collect_responses)
from .proposal_workflow import canonical_hash


def freeze_ac_protocol(parent):
    import requests
    parent = Path(parent)
    output = parent/'ac_transfer'
    if (output/'protocol.json').exists():
        return read(output/'protocol.json')
    main = read(parent/'protocol.json')
    tags={row['name']:row for row in requests.get('http://127.0.0.1:11434/api/tags',timeout=15).json()['models']}
    if any(tags.get(model,{}).get('digest')!=main['model_tags'][model]['digest'] for model in MODELS):
        raise ValueError('Model digests changed between MV and AC transfer pools')
    contexts = [row for row in read(parent/'contexts.json') if row['split'] == 'test']
    paths = ['protocol.json'] + [f'opendss_planning/{row["id"]}.json' for row in contexts]
    protocol = {'version': '1.0-ac-transfer', 'frozen_utc': datetime.now(timezone.utc).isoformat(),
        'source_sha256': sha(__file__), 'base_source_sha256': sha(ROOT/'src/ensemble_voltage.py'),
        'parent_protocol_hash': main['protocol_hash'], 'parent_files': {path:sha(parent/path) for path in paths},
        'models': list(MODELS), 'model_tags': main['model_tags'], 'model_settings': main['model_settings'],
        'scenarios': [{key:row[key] for key in ('id','split','case')} for row in contexts],
        'objective': main['objective'], 'planning_backend': 'opendss', 'contexts':12,
        'selector': 'Use the frozen selector learned on MV training contexts; no AC fitting or hyperparameter selection',
        'MPC_reuse': 'Previously executed independent H=3 AC MPC plan is reused; recorded plan time is reported separately, not charged as a new execution',
        'scope': 'Full supplied MV/LV feeder; simulated first action only, no physical dispatch',
        'comparison_limit': 'A backend transfer experiment with different constraint coverage, not an accuracy-only model comparison'}
    protocol['protocol_hash'] = canonical_hash(protocol)
    write(output/'protocol.json', protocol)
    return protocol


def collect_ac_contexts(parent, protocol):
    parent, contexts = Path(parent), []
    output = parent/'ac_transfer'
    for row in protocol['scenarios']:
        path = output/'numerical'/f"{row['id']}.json"
        if path.exists():
            record = read(path)
        else:
            case = case_from(row)
            old = read(parent/'numerical'/f"{row['id']}.json")
            ac_plan = read(parent/'opendss_planning'/f"{row['id']}.json")['plan']
            evaluations = []
            if ac_plan.get('candidate'):
                evaluations.append(evaluate(case, {**ac_plan['candidate'],'operation':'INITIAL_MPC'},'opendss'))
            evaluations.append(evaluate(case, {**old['sac']['candidate'],'operation':'INITIAL_SAC'},'opendss'))
            passing = [entry for entry in evaluations if entry['feasible']]
            if not passing:
                evaluations.append(evaluate(case, {'tool':'CONSERVATIVE_SEED','control':[.25,0.],
                    'operation':'CONSERVATIVE_FALLBACK'}, 'opendss'))
                passing = [entry for entry in evaluations if entry['feasible']]
            record = {**row, 'mpc':ac_plan, 'sac':old['sac'], 'initial_evaluations':evaluations,
                'incumbent':min(passing,key=lambda entry:entry['score']) if passing else None,
                'planning_seconds_reused':ac_plan['seconds'],
                'reuse_note':'MPC and SAC proposals were previously computed for this exact immutable case; all first actions are checked afresh here'}
            write(path,record)
        incumbent = record['incumbent']
        if incumbent is None:
            context = {**row,'status':'REVIEW','numerical_record':str(path.relative_to(output))}
        else:
            summary,loads = incumbent['summary'],row['case']['forecast_loads']
            features = {'case_family':'voltage','planning_backend':'opendss',
                'load_mean':float(np.mean(loads)),'load_span':float(max(loads)-min(loads)),
                'current_margin':float(1-summary['max_allowed_current_pct']/100),
                'voltage_margin':float(min(summary['vmin']-.95,1.05-summary['vmax'])),
                'incumbent_cost':incumbent['score'],'remaining_budget':1}
            catalog = operation_catalog(incumbent)
            # Use the identical operation descriptions and system prompt as the MV pool.
            mv = next(r for r in read(parent/'contexts.json') if r['id']==row['id'])
            public = deepcopy(mv['public_context'])
            public.update(model_scope='Full supplied MV/LV feeder',
                initial_candidates=[public_evaluation(e) for e in record['initial_evaluations']],
                incumbent=public_evaluation(incumbent),operations=catalog)
            context = {**row,'status':'READY','numerical_record':str(path.relative_to(output)),
                'incumbent':public_evaluation(incumbent),'pretrial_features':features,
                'catalog':catalog,'public_context':public,
                'initial_evaluations':[public_evaluation(e) for e in record['initial_evaluations']],
                'planning_seconds_reused':record['planning_seconds_reused']}
            context['context_hash'] = canonical_hash(context)
        contexts.append(context)
        write(output/'contexts.json',contexts)
        print(f"AC transfer fresh context {len(contexts)}/12: {row['id']} {context['status']}",flush=True)
    return contexts


def collect_ac_counterfactuals(output, contexts, responses):
    output,outcomes = Path(output),[]
    for context in contexts:
        if context['status']!='READY':
            continue
        case,incumbent,cache = case_from(context),context['incumbent'],{}
        for operation,spec in context['catalog'].items():
            path = output/'counterfactuals'/f"{context['id']}_{operation}.json"
            if not path.exists():
                candidate = {'tool':spec['tool'],**spec['parameters'],'operation':operation}
                trial = evaluate(case,candidate,'opendss')
                write(path,{'context_id':context['id'],'operation_id':operation,'candidate':candidate,
                    'planning_model_trial':trial,'note':'OpenDSS is the selected numerical backend for this transfer run'})
            cache[operation]=(read(path),str(path.relative_to(output)))
        for response in (r for r in responses if r['context_id']==context['id']):
            operation=response['operation_id']
            if operation not in cache:
                outcomes.append({'context_id':context['id'],'model_id':response['model_id'],
                    'operation_id':operation,'feasible':False,'score':None,'incumbent_score':incumbent['score'],
                    'final_score':incumbent['score'],'evaluation_seconds':0.,
                    'error':response['error'] or 'invalid_response_operation'})
                continue
            record,path=cache[operation]
            trial=record['planning_model_trial']
            final_score=min(incumbent['score'],trial['score']) if trial['feasible'] else incumbent['score']
            outcomes.append({'context_id':context['id'],'model_id':response['model_id'],
                'operation_id':operation,'candidate_hash':trial['candidate_hash'],
                'feasible':trial['feasible'],'score':trial['score'],'failures':trial['failures'],
                'incumbent_score':incumbent['score'],'final_score':final_score,
                'selected_trial_improves':bool(trial['feasible'] and trial['score']<incumbent['score']),
                'evaluation_seconds':trial['seconds'],'counterfactual_record':path,'error':trial['error'],
                'reward_scope':'Full-feeder OpenDSS current-step objective; no further learning in transfer',
                'duplicates_note':'Duplicate canonical operations share identical collected outcomes'})
        write(output/'counterfactual_outcomes.json',outcomes)
        print(f"AC transfer counterfactuals: {context['id']}",flush=True)
    return outcomes


def collect_final_rechecks(output, backend):
    """Independent final solve, after retaining the feasible numerical minimum."""
    output,rows=Path(output),[]
    for context in read(output/'contexts.json'):
        if context['status']!='READY':
            continue
        case,incumbent=case_from(context),context['incumbent']
        for operation in context['catalog']:
            trial=read(output/'counterfactuals'/f"{context['id']}_{operation}.json")['planning_model_trial']
            selected=trial if trial['feasible'] and trial['score']<incumbent['score'] else incumbent
            path=output/'final_rechecks'/f"{context['id']}_{operation}.json"
            if not path.exists():
                final=evaluate(case,selected['candidate'],backend)
                audit=None
                if backend=='lindistflow3':
                    if selected is trial:
                        audit_path=output/'counterfactuals'/f"{context['id']}_{operation}.json"
                        audit=read(audit_path)['independent_ac_audit']
                    else:
                        initial_operation=incumbent['candidate']['operation']
                        audit_path=output/'ac_initial_audits'/f"{context['id']}_{initial_operation}.json"
                        audit=read(audit_path)
                    if audit['candidate']['control']!=selected['candidate']['control']:
                        raise ValueError('Selected action and separate AC audit differ')
                    audit={'result':public_evaluation(audit),
                        'record':str(audit_path.relative_to(output)),'record_sha256':sha(audit_path),
                        'scope':'Previously collected common AC audit of the exact retained control, separate from final MV acceptance'}
                write(path,{'context_id':context['id'],'operation_id':operation,
                    'selected_from':'trial' if selected is trial else 'incumbent',
                    'selected_candidate_hash':selected['candidate_hash'],
                    'selected_evidence_hash':selected['evidence_hash'],
                    'final_recheck':final,'final_ac_audit':audit,
                    'note':'Distinct fresh numerical solve after choice, not the earlier candidate trial'})
            record=read(path)
            final=record['final_recheck']
            rows.append({'context_id':context['id'],'operation_id':operation,
                'selected_from':record['selected_from'],'feasible':final['feasible'],
                'candidate':final['candidate'],'candidate_hash':final['candidate_hash'],
                'evidence_hash':final['evidence_hash'],'score':final['score'],
                'failures':final['failures'],'seconds':final['seconds'],'summary':final['summary'],
                'final_ac_audit':record['final_ac_audit'],
                'record':str(path.relative_to(output)),
                'status':'MODEL_RECOMMEND' if final['feasible'] else 'REVIEW'})
        write(output/'final_rechecks.json',rows)
    return rows


def collect_ac_transfer(parent):
    parent=Path(parent)
    if not (parent/'collection_manifest.json').exists():
        raise RuntimeError('Complete the original collection before the separate AC transfer')
    protocol=freeze_ac_protocol(parent)
    if protocol['source_sha256']!=sha(__file__):
        raise ValueError('Frozen AC transfer source changed')
    for path,expected in protocol['parent_files'].items():
        if sha(parent/path)!=expected:
            raise ValueError('Frozen parent input changed: '+path)
    output=parent/'ac_transfer'
    contexts=collect_ac_contexts(parent,protocol)
    responses=collect_responses(protocol,contexts,output)
    outcomes=collect_ac_counterfactuals(output,contexts,responses)
    mv_checks=collect_final_rechecks(parent,'lindistflow3')
    ac_checks=collect_final_rechecks(output,'opendss')
    manifest={'completed_utc':datetime.now(timezone.utc).isoformat(),'protocol_hash':protocol['protocol_hash'],
        'contexts':len(contexts),'actual_calls':sum(r['source']=='actual_local_llm' for r in responses),
        'call_failures':sum(r['source']!='actual_local_llm' for r in responses),'outcomes':len(outcomes),
        'mv_distinct_final_rechecks':len(mv_checks),'ac_distinct_final_rechecks':len(ac_checks),
        'files':{str(path.relative_to(output)):sha(path) for path in sorted(output.rglob('*.json'))
                 if path.name!='collection_manifest.json'}}
    write(output/'collection_manifest.json',manifest)
    return manifest
