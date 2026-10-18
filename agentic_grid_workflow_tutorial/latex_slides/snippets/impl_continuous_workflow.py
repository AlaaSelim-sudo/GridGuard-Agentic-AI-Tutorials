"""Continuous SAC/MPC teaching workflow and human review contract.

Numerical tools return actions. The language model selects only permitted next
steps. All physical evaluations are simulations; this module has no dispatch API.
"""
from dataclasses import asdict
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TOOL_INTERFACE_VERSION = '1.1'
CHOICE_DEFINITIONS = {
    'VERIFY_SAC_FIRST': 'Launch a fresh numerical simulation and deterministic verification of the supplied SAC proposal. This requests a check; it neither approves the action nor operates equipment.',
    'USE_MPC_PLAN': 'Launch a fresh numerical simulation and deterministic verification of the eligible MPC plan first action. This requests a check; it does not apply an unchecked action or operate equipment.',
    'REVIEW': 'Escalate for human review and stop this numerical candidate route without executing a candidate check or operating equipment.',
    'REVIEW_ACTION': 'Focus the operator explanation on the returned action. This does not change the deterministic result or acknowledge for the operator.',
    'REVIEW_EVIDENCE': 'Focus the operator explanation on the returned numerical evidence. This does not change the deterministic result or acknowledge for the operator.',
    'REVIEW_MODEL_LIMITS': 'Focus the operator explanation on model coverage and limitations. This does not change the deterministic result or acknowledge for the operator.',
}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, allow_nan=False).encode()).hexdigest()


def workflow_roles():
    return [
        {'stage': 'Awareness', 'method': 'Structured request, finite-input and provenance checks', 'response': 'Accepted task and model scope'},
        {'stage': 'Planning', 'method': 'Continuous H=3 MPC + bounded Llama or fixed routing', 'response': 'Contingency plan and chosen next step'},
        {'stage': 'Execution', 'method': 'Continuous SAC actor / first MPC control', 'response': 'Proposed active/reactive participation factors'},
        {'stage': 'Simulation', 'method': 'Fresh OpenDSS or three-phase LinDistFlow solve', 'response': 'Voltage, current and dispatch evidence'},
        {'stage': 'Verification', 'method': 'Deterministic action and modeled physical constraints', 'response': 'Pass or explicit failed checks'},
        {'stage': 'Recovery', 'method': 'At most one MPC fallback; Llama or fixed choice', 'response': 'Rechecked replacement or REVIEW'},
        {'stage': 'Explanation', 'method': 'Immutable metric card + bounded explanation focus', 'response': 'Action, evidence, limitations and provenance'},
        {'stage': 'Operator acknowledgment', 'method': 'Human readback of the specific record', 'response': 'Local review only; no equipment command'},
    ]


def request_contract(backend='lindistflow3', case=None):
    from .continuous_control import cases, validate_case
    case = case or cases()[-1]
    validate_case(case)
    if backend not in ('lindistflow3', 'opendss'):
        raise ValueError('Unknown model backend')
    return {'case': asdict(case), 'backend': backend, 'tool_interface_version': TOOL_INTERFACE_VERSION,
            'objective': 'Retain PV with voltage regulation, reactive-effort and control-movement costs',
            'control': 'Shared p_g=a*S_g, q_g=b*S_g; real-valued a,b',
            'voltage_limits_pu': [.95, 1.05],
            'allowed_current_percent_of_nominal': 100 * case.rating_fraction,
            'maximum_candidates': 2,
            'data_source': 'Synthetic scenario and model-generated evidence; no live SCADA',
            'authority': 'Advisory simulation only; human review cannot override failed checks'}


def review_requirements(contract):
    return {'requested_current_allowance_percent': contract['allowed_current_percent_of_nominal'],
            'action_to_read_back': 'Actual proposed P/Q and participation factors',
            'scope_to_confirm': contract['backend'],
            'remaining_questions': ['Model coverage', 'Measurement trust', 'Protection and implementation authority'],
            'state': 'PENDING', 'dispatch_authorized': False}


class ContinuousLlama:
    """Actual local Ollama calls, schema checked and journaled verbatim."""
    def __init__(self, journal, model='llama3.1:8b'):
        self.journal, self.model, self.calls = Path(journal), model, []
        self.journal.parent.mkdir(parents=True, exist_ok=True)

    def ask(self, role, context, choices):
        schema = {'type': 'object', 'properties': {
            'choice': {'type': 'string', 'enum': choices}, 'reason': {'type': 'string'}},
            'required': ['choice', 'reason'], 'additionalProperties': False}
        system = (f'You are the named {role} role in a distribution-grid teaching simulator. '
                  'SAC proposes continuous active/reactive controls; continuous MPC produces a model-based horizon plan. '
                  'Numerical tools compute all controls. A separate deterministic checker evaluates fresh selected-model evidence. '
                  'The context defines the allowed actions and their effects. Requesting a numerical check is distinct from approving its result. '
                  'You may choose only the allowed next step. You cannot alter constraints, invent evidence, authenticate sensors, '
                  'approve a failed point, or acknowledge for the operator. MV-only LinDistFlow omits LV constraints. '
                  'A common initial SAC proposal is declared for this paired comparison. A passing first-action check is '
                  'not a stability or future-horizon guarantee. Return a short JSON choice and evidence-based reason.')
        payload = {'model': self.model, 'messages': [{'role': 'system', 'content': system},
                   {'role': 'user', 'content': json.dumps(context, allow_nan=False)}],
                   'format': schema, 'stream': False, 'keep_alive': '30m',
                   'options': {'temperature': 0, 'seed': 23, 'num_ctx': 8192, 'num_predict': 180}}
        entry = {'role': role, 'utc': datetime.now(timezone.utc).isoformat(),
                 'context': context, 'payload': payload}
        started = time.perf_counter()
        try:
            request = urllib.request.Request('http://127.0.0.1:11434/api/chat',
                data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(request, timeout=120) as response:
                raw = json.load(response)
            entry['raw_response'] = raw
            parsed = json.loads(raw['message']['content'])
            if (set(parsed) != {'choice', 'reason'} or parsed['choice'] not in choices
                    or not isinstance(parsed['reason'], str) or not parsed['reason'].strip()):
                raise ValueError('Invalid language response schema')
            entry['response'] = parsed
        except Exception as error:
            entry['error'] = f'{type(error).__name__}: {error}'
            entry['response'] = {'choice': 'REVIEW', 'reason': 'Local service or schema failure; inspect the journal.'}
        entry['seconds'] = time.perf_counter() - started
        entry['call_id'] = len(self.calls) + 1
        self.calls.append(entry)
        self.journal.write_text(json.dumps(self.calls, indent=2, allow_nan=False), encoding='utf-8')
        return {**entry['response'], 'call_id': entry['call_id'], 'seconds': entry['seconds'],
                'source': 'local_failure_fallback' if entry.get('error') else 'actual_local_llama',
                'error': entry.get('error')}


def point_summary(point):
    keys = ('control', 'p_actual_kw', 'q_actual_kvar', 'vmin', 'vmax',
            'max_line_utilization_pct', 'max_allowed_current_pct', 'accepted', 'violations', 'scope', 'converged',
            'backend', 'load_mult', 'rating_fraction', 'fresh_model_solve')
    return deepcopy({key: point[key] for key in keys if key in point})


def candidate_failures(candidate, expected_tool):
    from .continuous_control import _control
    if not isinstance(candidate, dict) or candidate.get('tool') != expected_tool:
        return ['invalid_candidate_tool']
    try:
        _control(candidate['control'])
    except (KeyError, TypeError, ValueError, OverflowError):
        return ['invalid_candidate_control']
    return []


def plan_failures(plan, case, backend):
    """Check supplied plan identity and horizon evidence before offering recovery.

    Compact planning evidence is not a new power-flow check. The selected first
    action is always solved afresh, regardless of this plan-level screening.
    """
    failures = []
    if not isinstance(plan, dict):
        return ['missing_mpc_plan']
    if plan.get('status') != 'PLAN' or plan.get('horizon_feasible') is not True:
        failures.append('unverified_mpc_horizon')
    if plan.get('backend') != backend:
        failures.append('mpc_backend_mismatch')
    failures += candidate_failures(plan.get('candidate'), 'CONTINUOUS_MPC')
    try:
        sequence, checks = plan['control_sequence'], plan['fresh_checks']
        if len(sequence) != len(case.forecast_loads) or len(checks) != len(sequence):
            raise ValueError('Horizon length mismatch')
        if sequence[0] != plan['candidate']['control']:
            raise ValueError('First action mismatch')
        for control, point, load in zip(sequence, checks, case.forecast_loads):
            if candidate_failures({'tool': 'CONTINUOUS_MPC', 'control': control}, 'CONTINUOUS_MPC'):
                raise ValueError('Invalid sequence')
            if (point['control'] != control or point['backend'] != backend or
                    point['accepted'] is not True or any(point['violations'].values()) or
                    abs(point['load_mult']-load) > 1e-12 or
                    abs(point['rating_fraction']-case.rating_fraction) > 1e-12):
                raise ValueError('Horizon evidence mismatch')
            values = [point[k] for k in ('vmin', 'vmax', 'max_allowed_current_pct', 'load_mult', 'rating_fraction')]
            if (any(type(v) not in (float, int) or not math.isfinite(v) for v in values) or
                    point['vmin'] < .95-1e-7 or point['vmax'] > 1.05+1e-7 or
                    not 0 <= point['max_allowed_current_pct'] <= 100+1e-5):
                raise ValueError('Horizon constraints fail')
    except (KeyError, TypeError, ValueError, IndexError, AttributeError):
        failures.append('invalid_mpc_horizon_evidence')
    return sorted(set(failures))


def recommendation_payload(row):
    return {key: row[key] for key in ('case_definition', 'backend', 'method', 'status',
                                      'candidate', 'metrics', 'contract', 'reasons', 'model_scope')}


def run_continuous_workflow(case, backend='lindistflow3', method='fixed', llama=None,
                            proposal=None, plan=None):
    from .continuous_control import ContinuousPlant, sac_proposal, optimize_mpc, verify_control
    if method not in ('fixed', 'agentic') or (method == 'agentic' and llama is None):
        raise ValueError('Agentic mode requires a local-model client')
    started = time.perf_counter()
    start_calls = len(llama.calls) if llama else 0
    contract = request_contract(backend, case)
    trace = []
    def stage(role, technique, response, status='COMPLETE', source='deterministic_method'):
        trace.append({'stage': role, 'method': technique, 'status': status,
                      'response_source': source, 'response': response})
    def choose(role, context, choices, fixed_choice):
        context = {**deepcopy(context), 'named_role': role, 'tool_interface_version': TOOL_INTERFACE_VERSION,
                   'allowed_actions': {choice: CHOICE_DEFINITIONS[choice] for choice in choices}}
        return llama.ask(role, context, choices) if method == 'agentic' else {
            'choice': fixed_choice, 'reason': 'Declared fixed adaptive policy', 'source': 'fixed_rule'}
    stage('Awareness', 'Validate structured task and provenance', contract, 'PASS')
    proposal = deepcopy(sac_proposal(case) if proposal is None else proposal)
    plan = deepcopy(optimize_mpc(case, backend) if plan is None else plan)
    if not isinstance(proposal, dict):
        proposal = {}
    if not isinstance(plan, dict):
        plan = {}
    invalid_plan = plan_failures(plan, case, backend)
    plan_card = {key: plan.get(key) for key in ('status', 'candidate', 'control_sequence', 'objective')}
    plan_card['recovery_eligibility_failures'] = invalid_plan
    decision = choose('Planner', {'contract': contract, 'numerical_mpc_plan': plan_card,
                      'sac_proposal': proposal,
                      'current_stage': 'A numerical SAC proposal is available; its fresh first-action check has not yet been requested.',
                      'protocol': 'Both supervisors start with the same saved SAC proposal; one MPC fallback at most.'},
                      ['VERIFY_SAC_FIRST', 'REVIEW'], 'VERIFY_SAC_FIRST')
    stage('Planning', 'Continuous MPC contingency plan + bounded strategy selection',
          {'numerical_plan': plan_card, 'language_response': decision,
           'plan_horizon_checks': [point_summary(p) for p in plan.get('fresh_checks', [])]},
          'PLAN' if decision['choice'] == 'VERIFY_SAC_FIRST' else 'REVIEW', decision['source'])
    accepted_candidate, accepted_point = None, None
    rejections, reasons, attempts, evaluations = 0, [], [], 0
    plant = ContinuousPlant(backend)
    if decision['choice'] == 'VERIFY_SAC_FIRST':
        candidate = proposal.get('candidate')
        for attempt in range(2):
            expected_tool = 'SAC' if attempt == 0 else 'CONTINUOUS_MPC'
            stage('Execution', 'Saved continuous SAC actor' if expected_tool == 'SAC' else 'First continuous MPC control',
                  {'candidate': candidate, 'attempt': attempt + 1, 'physical_dispatch': False}, 'PROPOSE')
            failures = candidate_failures(candidate, expected_tool)
            if attempt == 0 and proposal.get('status') != 'PROPOSE':
                failures.append('invalid_sac_proposal_status')
            try:
                if failures:
                    point = {'accepted': False, 'error': 'Candidate contract rejected before model evaluation'}
                else:
                    evaluations += 1
                    point = plant.solve(candidate['control'], load_mult=case.forecast_loads[0], rating_fraction=case.rating_fraction)
                    failures = verify_control(point, case)
                    if point.get('backend') != backend or any(abs(a-b)>1e-12 for a,b in zip(point['control'], candidate['control'])):
                        failures.append('candidate_evidence_mismatch')
            except Exception as error:
                point = {'accepted': False, 'error': f'{type(error).__name__}: {error}'}
                failures = ['model_or_action_failure']
            stage('Simulation', 'Fresh ' + backend + ' evaluation of the exact proposed P/Q',
                  point_summary(point) | ({'error': point['error']} if 'error' in point else {}), 'EVALUATED')
            stage('Verification', 'Declared voltage/current, action, inverter and dispatch checks',
                  {'failures': failures, 'accepted_in_model_scope': not failures,
                   'current_allowance_percent': 100 * case.rating_fraction,
                   'horizon_claim': 'This gate checks the first action. MPC has separately reported planned-horizon checks.'},
                  'REJECT' if failures else 'PASS')
            attempts.append({'candidate': candidate, 'point': point_summary(point), 'failures': failures})
            if not failures:
                accepted_candidate, accepted_point = candidate, point
                reasons = []
                break
            rejections += 1
            reasons = list(failures)
            if attempt == 0 and not invalid_plan:
                recovery = choose('Recovery', {'failed_candidate': candidate, 'failed_checks': failures,
                                   'replacement_plan': plan_card, 'contract': contract},
                                   ['USE_MPC_PLAN', 'REVIEW'], 'USE_MPC_PLAN')
                stage('Recovery', 'One allowed SAC-to-MPC fallback', recovery,
                      'REPAIR' if recovery['choice'] == 'USE_MPC_PLAN' else 'REVIEW', recovery['source'])
                if recovery['choice'] == 'USE_MPC_PLAN':
                    candidate = plan['candidate']
                    continue
            elif attempt == 0 and invalid_plan:
                stage('Recovery', 'Validate MPC fallback eligibility',
                      {'failures': invalid_plan, 'reason': 'No eligible horizon plan; request further review'}, 'REVIEW')
                reasons += invalid_plan
            break
    else:
        reasons = ['planner_review']
    for role in ('Execution', 'Simulation', 'Verification', 'Recovery'):
        if not any(t['stage'] == role for t in trace):
            stage(role, next(r['method'] for r in workflow_roles() if r['stage'] == role),
                  {'reason': 'No retry needed' if accepted_candidate else 'No accepted candidate'}, 'SKIPPED')
    row = {'case': case.id, 'case_definition': asdict(case), 'backend': backend, 'method': method,
           'status': 'MODEL_RECOMMEND' if accepted_candidate else 'REVIEW',
           'candidate': accepted_candidate, 'metrics': point_summary(accepted_point) if accepted_point else None,
           'attempts': attempts, 'reasons': reasons, 'gate_rejections': rejections,
           'model_scope': 'MV-only phase network; internal LV constraints omitted' if backend == 'lindistflow3'
                          else 'Supplied full unbalanced AC feeder; protection/transients outside this model',
           'contract': contract, 'trace': trace, 'equipment_operated': False}
    card = deepcopy({key: row[key] for key in ('status', 'candidate', 'metrics', 'reasons', 'model_scope', 'equipment_operated')})
    explanation = choose('Explanation', card, ['REVIEW_ACTION', 'REVIEW_EVIDENCE', 'REVIEW_MODEL_LIMITS'], 'REVIEW_MODEL_LIMITS')
    if explanation.get('error'):
        row['status'] = 'REVIEW'
        row['reasons'].append('language_service_failure')
        row['candidate'], row['metrics'] = None, None
        card = deepcopy({key: row[key] for key in card})
    stage('Explanation', 'Deterministic evidence card + language focus',
          {'operator_card': card, 'language_response': explanation}, 'RECORDED', explanation['source'])
    row['recommendation_id'] = fingerprint(recommendation_payload(row))
    stage('Operator acknowledgment', 'Human readback bound to this record identity',
          {'recommendation_id': row['recommendation_id'], **review_requirements(contract),
           'acknowledged': False, 'equipment_operated': False}, 'PENDING')
    row.update(seconds=time.perf_counter() - started, llm_calls=(len(llama.calls) - start_calls) if llama else 0,
               fresh_candidate_evaluations=evaluations)
    return row
