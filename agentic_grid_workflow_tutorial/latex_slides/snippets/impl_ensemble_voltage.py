"""Frozen, small multi-LLM voltage response-selection teaching experiment.

MPC and a saved SAC actor propose initial actions. Numerical models, not a
language model or RL policy, check electrical constraints. The response pool
and counterfactual simulator outcomes are separate files: a selector must not
inspect outcomes before choosing. This is simulator replay, not deployment
bandit feedback, and is independent of the archived five-stage study.
"""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
import numpy as np

from .continuous_control import ContinuousCase, ContinuousPlant, compact, optimize_mpc, sac_proposal, stage_cost, verify_control
from .continuous_workflow import plan_failures
from .proposal_workflow import ProposalLlama, canonical_hash

ROOT = Path(__file__).resolve().parents[1]
MODELS = ('llama3.1:8b', 'llama3.2:3b', 'qwen2.5:7b-instruct')
OPERATIONS = ('INCREASE_PV_0025', 'RELAX_Q_10_PERCENT', 'DECREASE_PV_0025', 'KEEP_INCUMBENT')


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False), encoding='utf-8')


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def freeze_protocol(output):
    """Freeze scenario values and source identities before collecting outcomes."""
    import requests
    output = Path(output)
    if (output/'protocol.json').exists():
        return read(output/'protocol.json')
    rng = np.random.default_rng(270926)
    scenarios = []
    for split, size in (('train', 24), ('validation', 8), ('test', 12)):
        for index in range(size):
            case = ContinuousCase(f'{split}_{index+1:02d}', tuple(float(x) for x in rng.uniform(.9, 1.1, 3)),
                                  float(rng.uniform(.78, .88)), (float(rng.uniform(.2, .3)), 0.))
            scenarios.append({'id': case.id, 'split': split, 'case': asdict(case)})
    tags = requests.get('http://127.0.0.1:11434/api/tags', timeout=15).json()['models']
    available = {row['name']: row for row in tags}
    if any(model not in available for model in MODELS):
        raise RuntimeError('Every specified local model must be available before freezing')
    sources = ['src/ensemble_voltage.py', 'src/continuous_control.py', 'src/continuous_workflow.py',
               'src/proposal_workflow.py', 'src/standard_formulations.py', 'src/lindistflow3.py',
               'models/continuous_sac/actor_numpy.npz', 'models/continuous_sac/training.json',
               'data/lindistflow3_network.json']
    protocol = {'version': '1.0', 'frozen_utc': datetime.now(timezone.utc).isoformat(),
        'seed': 270926, 'scenario_splits': {'train': 24, 'validation': 8, 'test': 12},
        'scenarios': scenarios, 'models': list(MODELS),
        'model_tags': {model: available[model] for model in MODELS},
        'model_settings': {'temperature': 0, 'seed': 29, 'num_ctx': 8192, 'num_predict': 260},
        'source_hashes': {path: sha(ROOT/path) for path in sources},
        'planning_backend': 'lindistflow3', 'independent_audit_backend': 'opendss',
        'test_comparison': 'Fresh OpenDSS-based H=3 MPC, separately optimized on the same twelve test contexts',
        'initial_candidates': ['H=3 local sensitivity MPC', 'saved reward-trained continuous SAC'],
        'conservative_fallback': 'Test [0.25,0] only if neither initial first action passes; otherwise no fallback',
        'response_operations': list(OPERATIONS),
        'budget': 'One selected response action is simulated; final feasible minimum includes the verified incumbent',
        'objective': 'Current-step J=(1-a)^2+0.05*b^2+10*mean((V-1.01)^2)+0.05*||u-u_previous||^2',
        'separation': 'LLMs see only initial checked evidence and pretrial context; all response trial outcomes live in a separate counterfactual table',
        'data_kind': 'Full-information simulator counterfactuals for deterministic replay, not logged deployment bandit data',
        'limitations': ['Small single-seed teaching pilot on one supplied feeder',
            'The saved SAC was trained on a response surface at nominal current allowance; these derated contexts are a transfer test',
            'LinDistFlow includes MV phases and ideal LV aggregation; OpenDSS includes supplied MV/LV feeder',
            'OpenDSS audit does not secretly change the LinDistFlow acceptance rule',
            'The horizon MPC is a local sensitivity method, not a certified global optimum',
            'No physical dispatch, no automatic operator acknowledgment, no claim of RL superiority']}
    protocol['protocol_hash'] = canonical_hash(protocol)
    write(output/'protocol.json', protocol)
    return protocol


def case_from(row):
    c = row['case']
    return ContinuousCase(c['id'], tuple(c['forecast_loads']), c['rating_fraction'], tuple(c['previous']))


def evaluate(case, candidate, backend):
    """Fresh solve and independent reconstruction of modeled constraints."""
    started = time.perf_counter()
    identity = canonical_hash({'case': asdict(case), 'candidate': candidate, 'backend': backend})
    try:
        point = ContinuousPlant(backend).solve(candidate['control'], case.forecast_loads[0], case.rating_fraction)
        failures = verify_control(point, case)
        if point['control'] != candidate['control']:
            failures.append('candidate_evidence_mismatch')
        raw_cost = stage_cost(candidate['control'], point['voltages_pu'], case.previous)
        summary = compact(point)
        error = None
    except Exception as exc:
        point, failures, raw_cost, summary = {}, ['model_or_candidate_failure'], None, {}
        error = f'{type(exc).__name__}: {exc}'
    if identity != canonical_hash({'case': asdict(case), 'candidate': candidate, 'backend': backend}):
        failures.append('candidate_mutation')
    return {'candidate': deepcopy(candidate), 'backend': backend, 'candidate_hash': identity,
            'evidence_hash': canonical_hash(point), 'evidence': point, 'summary': summary,
            'failures': sorted(set(failures)), 'feasible': not failures,
            'score': raw_cost if not failures else None, 'raw_objective_even_if_rejected': raw_cost,
            'seconds': time.perf_counter()-started, 'error': error}


def public_evaluation(row):
    return {key: deepcopy(row[key]) for key in ('candidate', 'backend', 'candidate_hash', 'evidence_hash',
            'summary', 'failures', 'feasible', 'score', 'seconds', 'error')}


def operation_catalog(incumbent):
    a, b = incumbent['candidate']['control']
    controls = {'INCREASE_PV_0025': [min(1., a+.0025), b],
                'RELAX_Q_10_PERCENT': [a, .9*b],
                'DECREASE_PV_0025': [max(0., a-.0025), b], 'KEEP_INCUMBENT': [a, b]}
    return {key: {'tool': 'BOUNDED_LOCAL_SEARCH', 'parameters': {'control': [float(v) for v in value]}}
            for key, value in controls.items()}


def collect_numerics(protocol, output):
    output = Path(output)
    contexts = []
    for row in protocol['scenarios']:
        path = output/'numerical'/f"{row['id']}.json"
        if path.exists():
            record = read(path)
        else:
            started = time.perf_counter()
            case = case_from(row)
            mpc = optimize_mpc(case, 'lindistflow3')
            sac = sac_proposal(case)
            evaluations = []
            if mpc.get('candidate') is not None:
                evaluation = evaluate(case, {**mpc['candidate'], 'operation': 'INITIAL_MPC'}, 'lindistflow3')
                evaluation['planning_failures'] = plan_failures(mpc, case, 'lindistflow3')
                evaluations.append(evaluation)
            evaluations.append(evaluate(case, {**sac['candidate'], 'operation': 'INITIAL_SAC'}, 'lindistflow3'))
            feasible = [entry for entry in evaluations if entry['feasible']]
            if not feasible:
                evaluations.append(evaluate(case, {'tool': 'CONSERVATIVE_SEED', 'control': [.25, 0.],
                    'operation': 'CONSERVATIVE_FALLBACK'}, 'lindistflow3'))
                feasible = [entry for entry in evaluations if entry['feasible']]
            incumbent = min(feasible, key=lambda entry: entry['score']) if feasible else None
            record = {'id': row['id'], 'split': row['split'], 'case': asdict(case), 'mpc': mpc, 'sac': sac,
                      'initial_evaluations': evaluations, 'incumbent': incumbent,
                      'planning_and_initial_seconds': time.perf_counter()-started}
            write(path, record)
        incumbent = record['incumbent']
        if incumbent is None:
            context = {**row, 'status': 'REVIEW', 'numerical_record': str(path.relative_to(output)),
                       'reason': 'No verified numerical incumbent; no LLM trial is eligible'}
        else:
            summary = incumbent['summary']
            loads = record['case']['forecast_loads']
            feature = {'case_family': 'voltage', 'planning_backend': 'lindistflow3',
                       'load_mean': float(np.mean(loads)), 'load_span': float(max(loads)-min(loads)),
                       'current_margin': float(1-summary['max_allowed_current_pct']/100),
                       'voltage_margin': float(min(summary['vmin']-.95, 1.05-summary['vmax'])),
                       'incumbent_cost': incumbent['score'], 'remaining_budget': 1}
            catalog = operation_catalog(incumbent)
            public = {'case_id': row['id'], 'model_scope': 'MV phases only; ideal LV aggregation',
                'case': record['case'], 'objective': protocol['objective'],
                'initial_candidates': [public_evaluation(e) for e in record['initial_evaluations']],
                'incumbent': public_evaluation(incumbent), 'remaining_candidate_evaluations': 1,
                'operations': catalog,
                'operation_meanings': {'INCREASE_PV_0025': 'Increase active participation a by 0.0025 to reduce curtailment; a fresh check may reject it',
                    'RELAX_Q_10_PERCENT': 'Reduce reactive effort magnitude by ten percent; recheck voltages and currents',
                    'DECREASE_PV_0025': 'Reduce active participation by 0.0025 to add possible headroom at curtailment cost',
                    'KEEP_INCUMBENT': 'Retain the already checked numerical incumbent; final fresh check still required'},
                'instruction': 'Choose one permitted operation and give a brief evidence-based public reason. Do not invent future trial outcomes.'}
            context = {**row, 'status': 'READY', 'numerical_record': str(path.relative_to(output)),
                       'incumbent': public_evaluation(incumbent), 'pretrial_features': feature,
                       'catalog': catalog, 'public_context': public,
                       'initial_evaluations': [public_evaluation(e) for e in record['initial_evaluations']]}
            context['context_hash'] = canonical_hash(context)
        contexts.append(context)
        write(output/'contexts.json', contexts)
        print(f"Numerical context {len(contexts)}/44: {row['id']} {context['status']}", flush=True)
    return contexts


def collect_responses(protocol, contexts, output):
    """Batch by model for realistic local model residency; retain failed calls."""
    output = Path(output)
    rows = read(output/'responses.json') if (output/'responses.json').exists() else []
    completed = {(r['context_id'], r['model_id']) for r in rows}
    for model in protocol['models']:
        for context in contexts:
            if context['status'] != 'READY' or (context['id'], model) in completed:
                continue
            safe_model = model.replace(':', '_').replace('.', '_')
            journal = output/'llm_calls'/safe_model/f"{context['id']}.json"
            if journal.exists():
                call = read(journal)[-1]
                reply = {**call['response'], 'call_id': call['call_id'], 'seconds': call['seconds'],
                         'source': call['source'], 'error': call.get('error')}
            else:
                reply = ProposalLlama(journal, model).ask('Optimization Agent', context['public_context'], list(context['catalog']))
            rows.append({'context_id': context['id'], 'context_hash': context['context_hash'],
                'split': context['split'], 'model_id': model, 'operation_id': reply['choice'],
                'reason': reply['reason'], 'seconds': reply['seconds'], 'source': reply['source'],
                'error': reply.get('error'), 'journal': str(journal.relative_to(output)),
                'model_digest': protocol['model_tags'][model]['digest']})
            write(output/'responses.json', rows)
            print(f"Actual response {len(rows)}/132: {context['id']} {model} {reply['choice']} {reply['seconds']:.2f}s", flush=True)
    return rows


def collect_counterfactual_audit(protocol, contexts, responses, output):
    """Counterfactual outcomes are audit-only, inaccessible to decision context."""
    output = Path(output)
    outcomes, audits, comparisons = [], [], []
    for context in contexts:
        if context['status'] != 'READY':
            continue
        case = case_from(context)
        incumbent = context['incumbent']
        cache = {}
        for operation, spec in context['catalog'].items():
            candidate = {'tool': spec['tool'], **spec['parameters'], 'operation': operation}
            path = output/'counterfactuals'/f"{context['id']}_{operation}.json"
            if path.exists():
                record = read(path)
            else:
                trial = evaluate(case, candidate, 'lindistflow3')
                # Every canonical operation gets the same separately reported AC audit.
                ac = evaluate(case, candidate, 'opendss')
                record = {'context_id': context['id'], 'operation_id': operation,
                    'candidate': candidate, 'planning_model_trial': trial,
                    'independent_ac_audit': ac,
                    'note': 'AC audit is held outside LinDistFlow acceptance and selector reward'}
                write(path, record)
            cache[operation] = (record, str(path.relative_to(output)))
        # Audit both initial methods too, including rejected SAC; do not hide failures.
        for initial in context['initial_evaluations']:
            operation = initial['candidate']['operation']
            path = output/'ac_initial_audits'/f"{context['id']}_{operation}.json"
            if not path.exists():
                write(path, evaluate(case, initial['candidate'], 'opendss'))
            ac = read(path)
            audits.append({'context_id': context['id'], 'split': context['split'],
                'initial_method': operation, 'lindistflow': initial,
                'opendss': public_evaluation(ac), 'record': str(path.relative_to(output))})
        for response in (r for r in responses if r['context_id'] == context['id']):
            operation = response['operation_id']
            if operation not in cache:
                outcomes.append({'context_id': context['id'], 'model_id': response['model_id'],
                    'operation_id': operation, 'feasible': False, 'score': None,
                    'incumbent_score': incumbent['score'], 'final_score': incumbent['score'],
                    'evaluation_seconds': 0., 'error': response['error'] or 'invalid_response_operation',
                    'reward_scope': 'LinDistFlow current-step objective, no AC information'})
                continue
            record, record_path = cache[operation]
            trial, ac = record['planning_model_trial'], record['independent_ac_audit']
            final_score = min(incumbent['score'], trial['score']) if trial['feasible'] else incumbent['score']
            outcomes.append({'context_id': context['id'], 'model_id': response['model_id'],
                'operation_id': operation, 'candidate_hash': trial['candidate_hash'],
                'feasible': trial['feasible'], 'score': trial['score'], 'failures': trial['failures'],
                'incumbent_score': incumbent['score'], 'final_score': final_score,
                'selected_trial_improves': bool(trial['feasible'] and trial['score'] < incumbent['score']),
                'evaluation_seconds': trial['seconds'], 'ac_audit': public_evaluation(ac),
                'counterfactual_record': record_path, 'error': trial['error'],
                'reward_scope': 'LinDistFlow current-step objective, no AC information',
                'duplicates_note': 'Identical canonical operations share one collected numerical outcome; deployment may evaluate only the selected one'})
        if context['split'] == 'test':
            path = output/'opendss_planning'/f"{context['id']}.json"
            if not path.exists():
                plan = optimize_mpc(case, 'opendss')
                fresh = evaluate(case, {**plan['candidate'], 'operation': 'INITIAL_MPC'}, 'opendss') if plan.get('candidate') else None
                write(path, {'context_id': context['id'], 'plan': plan, 'fresh_first_action': fresh})
            record = read(path)
            fresh = record['fresh_first_action']
            comparisons.append({'context_id': context['id'], 'record': str(path.relative_to(output)),
                'opendss_mpc': public_evaluation(fresh) if fresh else None,
                'opendss_mpc_seconds': record['plan']['seconds'],
                'lindistflow_incumbent': incumbent,
                'scope_note': 'Same context but different constraint coverage: full MV/LV OpenDSS versus MV-only LinDistFlow'})
        write(output/'counterfactual_outcomes.json', outcomes)
        write(output/'initial_model_audits.json', audits)
        write(output/'heldout_model_comparison.json', comparisons)
        print(f"Counterfactual and separate AC audit: {context['id']}", flush=True)
    return outcomes


def collect_pilot(output):
    output = Path(output)
    protocol = freeze_protocol(output)
    for path, expected in protocol['source_hashes'].items():
        if sha(ROOT/path) != expected:
            raise ValueError('Frozen source changed: '+path)
    contexts = collect_numerics(protocol, output)
    responses = collect_responses(protocol, contexts, output)
    outcomes = collect_counterfactual_audit(protocol, contexts, responses, output)
    manifest = {'protocol_hash': protocol['protocol_hash'], 'completed_utc': datetime.now(timezone.utc).isoformat(),
        'contexts': len(contexts), 'actual_calls': sum(r['source']=='actual_local_llm' for r in responses),
        'call_failures': sum(r['source']!='actual_local_llm' for r in responses), 'outcomes': len(outcomes),
        'files': {str(path.relative_to(output)): sha(path) for path in sorted(output.rglob('*.json'))
                  if path.name != 'collection_manifest.json'}}
    write(output/'collection_manifest.json', manifest)
    return manifest
