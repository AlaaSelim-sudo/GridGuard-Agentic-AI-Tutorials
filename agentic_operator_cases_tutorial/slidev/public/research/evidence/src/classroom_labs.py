"""Small, fresh classroom experiments; historical studies remain read-only.

Numerical evidence, an archived model reply, and a new live reply are distinct
types of evidence. Hashes demonstrate binding, not authentication/security.
"""
from copy import deepcopy
from dataclasses import asdict, replace
from pathlib import Path
import hashlib
import json
import time
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'results/ensemble_voltage_pilot'


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def bind_evidence(request, candidate, result):
    return {'request_hash': digest(request), 'candidate_hash': digest(candidate),
            'result_hash': digest(result), 'result': deepcopy(result)}


def bound_to(request, candidate, evidence):
    return (evidence.get('request_hash') == digest(request)
            and evidence.get('candidate_hash') == digest(candidate)
            and evidence.get('result_hash') == digest(evidence.get('result')))


def validate_request(request):
    """A typed local contract, deliberately separate from natural-language text."""
    required = {'task', 'backend', 'load_scale', 'rating_fraction', 'revision'}
    if set(request) != required or request['task'] != 'voltage':
        raise ValueError('Exactly the declared voltage request fields are required')
    if request['backend'] not in ('lindistflow3', 'opendss'):
        raise ValueError('Backend is outside the tool allowlist')
    for key, low, high in [('load_scale', .5, 1.5), ('rating_fraction', .01, 1.)]:
        value = request[key]
        if type(value) not in (int, float) or not np.isfinite(value) or not low <= value <= high:
            raise ValueError(f'{key} is outside its finite numeric domain')
    if type(request['revision']) is not int or request['revision'] < 1:
        raise ValueError('revision must be a positive integer')
    return deepcopy(request)


def saved_pool(case_id='test_01'):
    """Actual recorded responses bound to their ORIGINAL numerical context."""
    from .response_selector import canonicalize_responses, majority_select, LinUCB
    context = next(r for r in read(ARCHIVE / 'contexts.json') if r['id'] == case_id)
    responses = [r for r in read(ARCHIVE / 'responses.json') if r['context_id'] == case_id]
    votes = [{k: r[k] for k in ('model_id', 'operation_id', 'reason')} for r in responses]
    pool = canonicalize_responses(votes, context['catalog'])
    selector = LinUCB.load(ARCHIVE / 'selector_models/linucb_seed_270927.json')
    selected = selector.select(context['pretrial_features'], pool['candidates'])
    return {'context': context, 'responses': responses, 'pool': pool,
            'vote_id': majority_select(pool['candidates']), 'selection': selected,
            'frozen': selector.frozen, 'training_updates': selector.updates}


def voltage_lab(load_scale=1., rating_fraction=None, backend='lindistflow3'):
    """Fresh MPC planning, saved-actor inference, and fresh first-action checks."""
    from .ensemble_voltage import case_from, evaluate
    from .continuous_control import optimize_mpc, sac_proposal
    original = saved_pool()['context']
    base = case_from(original)
    case = replace(base, id='classroom_fresh',
                   forecast_loads=tuple(float(v * load_scale) for v in base.forecast_loads),
                   rating_fraction=base.rating_fraction if rating_fraction is None else float(rating_fraction))
    start = time.perf_counter()
    mpc, sac = optimize_mpc(case, backend), sac_proposal(case)
    records = []
    for name, proposal in [('MPC', mpc), ('saved SAC actor', sac)]:
        if proposal.get('candidate') is not None:
            record = evaluate(case, proposal['candidate'], backend)
            records.append({'method': name, **record})
    rows = [{'method': r['method'], 'feasible': r['feasible'],
             'current_step_J': r['score'], 'a': r['candidate']['control'][0],
             'b': r['candidate']['control'][1], 'vmin': r['summary'].get('vmin'),
             'vmax': r['summary'].get('vmax'),
             'max_allowed_current_pct': r['summary'].get('max_allowed_current_pct'),
             'failures': ', '.join(r['failures']) or 'none'} for r in records]
    return {'case': case, 'backend': backend, 'mpc': mpc, 'sac': sac,
            'evaluations': records, 'table': pd.DataFrame(rows),
            'seconds': time.perf_counter() - start,
            'mode': 'FRESH numerical solves; saved SAC weights; no LLM call'}


def trial_saved_selection(pool, backend='lindistflow3'):
    """New solve of the selected archived operation on its original context.

    This is a reproducibility exercise, not a new live LLM experiment.
    """
    from .ensemble_voltage import case_from, evaluate
    case = case_from(pool['context'])
    choices = {'majority vote': pool['vote_id'], 'frozen LinUCB': pool['selection'].candidate_id}
    rows, evaluations = [], {}
    for method, identifier in choices.items():
        item = next(c for c in pool['pool']['candidates'] if c['candidate_id'] == identifier)
        candidate = {'tool': item['operation']['tool'], **item['operation']['parameters']}
        checked = evaluate(case, candidate, backend)
        evaluations[method] = checked
        rows.append({'selector': method, 'operation': ', '.join(item['operation_ids']),
                     'new_check_passes': checked['feasible'], 'current_step_J': checked['score'],
                     'verification_s': checked['seconds'], 'failures': ', '.join(checked['failures']) or 'none'})
    return {'case': case, 'table': pd.DataFrame(rows), 'evaluations': evaluations}


def backend_audit(pool, run_opendss=False):
    """Compare the same physical command, then separately replan in OpenDSS."""
    from .ensemble_voltage import case_from, evaluate
    from .continuous_control import optimize_mpc
    case = case_from(pool['context'])
    candidate = pool['context']['incumbent']['candidate']
    rows, records = [], []
    for backend in (['lindistflow3', 'opendss'] if run_opendss else ['lindistflow3']):
        checked = evaluate(case, candidate, backend)
        records.append(checked)
        rows.append({'model': backend, 'command': 'same archived MV-MPC first action',
                     'fresh': True, 'passes': checked['feasible'],
                     'vmin': checked['summary'].get('vmin'), 'vmax': checked['summary'].get('vmax'),
                     'current_pct': checked['summary'].get('max_allowed_current_pct'),
                     'failures': ', '.join(checked['failures']) or 'none'})
    if run_opendss:
        plan = optimize_mpc(case, 'opendss')
        if plan['candidate'] is not None:
            checked = evaluate(case, plan['candidate'], 'opendss')
            records.append(checked)
            rows.append({'model': 'opendss', 'command': 'new full-model MPC first action',
                         'fresh': True, 'passes': checked['feasible'],
                         'vmin': checked['summary'].get('vmin'), 'vmax': checked['summary'].get('vmax'),
                         'current_pct': checked['summary'].get('max_allowed_current_pct'),
                         'failures': ', '.join(checked['failures']) or 'none'})
    else:
        return {'table': pd.DataFrame(rows), 'records': records,
                'optional_mode': 'OpenDSS disabled: full-model claims require enabling it or inspecting the separate recorded study',
                'recorded_comparison_path': 'results/ensemble_voltage_pilot/heldout_model_comparison.json'}
    return {'table': pd.DataFrame(rows), 'records': records, 'optional_mode': 'Fresh sequential OpenDSS audit and replanning'}


def restoration_sweep(capacities=(40., 60., 80., 100., 120.)):
    """Identical feasible graph: weighted MILP vs unweighted maximum-kW policy.

    Both are conventional optimizers. An agent's contribution is preserving
    the declared service priorities and rechecking changed constraints.
    """
    from .standard_formulations import solve_restoration_milp, _enumerate_restoration
    rows, records = [], []
    for capacity in capacities:
        solved = solve_restoration_milp(float(capacity))
        graph = deepcopy(solved['graph'])
        unweighted = deepcopy(graph)
        unweighted['priority'] = [0.] + [1.] * (len(graph['nodes']) - 1)
        baseline = _enumerate_restoration(unweighted)['solution']
        records.append({'capacity_kw': capacity, 'weighted': solved, 'unweighted': baseline})
        for name, pickup in [('priority-weighted MILP', solved['milp']['pickup']),
                             ('unweighted max-kW baseline', baseline['pickup'])]:
            demand, weight, x = np.array(graph['demand_kw']), np.array(graph['priority']), np.array(pickup)
            rows.append({'tie_capacity_kw': float(capacity), 'method': name,
                         'served_kw': float(demand @ x),
                         'critical_kw': float(demand[weight == 10] @ x[weight == 10]),
                         'weighted_service': float((demand * weight) @ x),
                         'pickup': pickup,
                         'MILP_matches_exhaustive_check': solved['agreement']})
    return {'table': pd.DataFrame(rows), 'records': records}


def cyber_sweep(scales=(0., .25, .5, 1., 1.5)):
    """Fresh WLS under isolated measurement errors and a=Hc negative control."""
    from .standard_formulations import run_wls_demo, weighted_least_squares
    demo = run_wls_demo()
    m = demo['measurement_model']
    H, sigma, truth = np.array(m['H']), np.array(m['sigma']), np.array(m['true_state'])
    clean = np.array(demo['cases'][0]['measurements'])
    direction = np.array(m['stealth_shift'])
    rows = []
    for scale in scales:
        for name in ('isolated bias', 'stealth Hc'):
            z = clean.copy()
            if name == 'isolated bias':
                z[1] += float(scale) * .08
            else:
                z += H @ (float(scale) * direction)
            fit = weighted_least_squares(H, z, sigma)
            chi = fit['chi_square']
            rows.append({'attack': name, 'scale': float(scale), 'J': chi['statistic'],
                         'threshold': chi['threshold'], 'alarm': chi['alarm'],
                         'state_error_rad': float(np.linalg.norm(np.array(fit['estimate']) - truth))})
    return {'table': pd.DataFrame(rows), 'demo': demo}


def trusted_response(cyber, protected_available):
    if not protected_available:
        return {'status': 'HOLD', 'reason': 'No independent trusted state for a stealth-capable threat',
                'protected_measurements': False, 'dispatch': False}
    recovery = cyber['demo']['trusted_recovery']
    return {**deepcopy(recovery['control']), 'protected_measurements': True,
            'assumption': 'Three separately trusted angle channels; authentication is assumed, not implemented',
            'dispatch': False}


def archived_stage_replies(case='restoration', backend='lindistflow3'):
    """Return exact prior-run public explanations; no invented stage dialogue."""
    suite = read(ROOT / 'results/proposal_complete_workflow.json')
    run = next(r for r in suite['runs'] if r['case'] == case and r['backend'] == backend and r['supervisor'] == 'agentic')
    return run


def archived_stage_table(run):
    """All actual trace events, with selected exact fields and no invented dialogue."""
    stages = ('Awareness Agent', 'Planning Agent', 'Simulation Agent',
              'Verification Agent', 'LLM Optimizer')
    metric_keys = ('vmin', 'vmax', 'max_allowed_current_pct', 'allowed_current_utilization_pct',
                   'tie_loading_pct', 'served_kw', 'critical_served_kw', 'chi_square',
                   'estimate', 'predicted_max_flow_pu', 'protected_measurements_available',
                   'trust', 'control', 'flexible_injection_pu', 'u_pu', 'measurement_basis',
                   'predicted_flows_pu', 'line_limits_pu', 'planning_margin_pu', 'offline_truth_audit')
    rows = []
    for event in run['trace']:
        response = event.get('response', {})
        fields = {k: response[k] for k in ('candidate_id', 'phase', 'failures', 'score',
                  'rank_eligible', 'scope', 'numerical_order', 'language_order_agrees_with_cost')
                  if k in response}
        if 'awareness' in response:
            awareness = response['awareness']
            fields.update({k: awareness[k] for k in ('alarms', 'trust', 'threat_model',
                          'residual_test', 'state_estimate_unprotected_rad', 'protected_state_estimate_rad')
                          if k in awareness})
            measurements = awareness.get('measurements', {})
            if isinstance(measurements, dict):
                fields['measurements'] = {k: measurements[k] for k in metric_keys if k in measurements}
        if 'candidates' in response:
            fields['candidates'] = response['candidates']
        if 'metrics' in response:
            metrics = response['metrics']
            fields['metrics'] = {k: metrics[k] for k in metric_keys if k in metrics}
        if 'language_response' in response:
            reply = response['language_response']
            fields['language_decision'] = {k: reply[k] for k in ('choice', 'ranking', 'source', 'error') if k in reply}
        # An unfamiliar role is retained separately, never relabeled as one of the five.
        if event['stage'] not in stages:
            fields = response
        rows.append({'event': event['event'], 'stage': event['stage'],
                     'role_group': 'proposal stage' if event['stage'] in stages else 'additional role',
                     'actual_method': event['method'], 'actual_status': event['status'],
                     'selected_actual_returned_fields': json.dumps(fields, ensure_ascii=False),
                     'recorded_event_s': event['seconds']})
    return pd.DataFrame(rows)


def operator_packet(request, candidate, evidence, engineering_pass, scope, required_scope):
    integrity = bound_to(request, candidate, evidence)
    ready = integrity and engineering_pass and scope == required_scope
    return {'recommendation_id': digest({'request': request, 'candidate': candidate, 'evidence': evidence})[:16],
            'state': 'READY_FOR_READBACK' if ready else 'HOLD',
            'evidence_matches': integrity, 'engineering_pass': bool(engineering_pass),
            'scope_matches': scope == required_scope, 'scope': scope,
            'acknowledged': False, 'equipment_dispatch': False}


def acknowledge(packet, readback_id, operator_name):
    result = deepcopy(packet)
    if packet['state'] != 'READY_FOR_READBACK' or readback_id != packet['recommendation_id'] or not operator_name.strip():
        result['acknowledgment_result'] = 'REJECTED'
        return result
    result.update(acknowledged=True, operator=operator_name.strip(),
                  acknowledgment_result='SIMULATION_READBACK_RECORDED')
    return result
