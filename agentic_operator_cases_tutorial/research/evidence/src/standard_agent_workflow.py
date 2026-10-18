"""Visible standard-method stage demo, separate from the frozen 32-run study.

Both supervisors invoke the identical numerical methods. Llama routes the
structured task and explains its result; no numerical advantage is presumed.
"""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
TOOLS = {'voltage': 'VOLTVAR_OPF', 'restoration': 'RESTORATION_MILP', 'cyber': 'WLS_TRUSTED_REDISPATCH'}
SCOPES = {'voltage': 'Selected Greensboro electrical model with shared continuous P/Q controls',
          'restoration': 'Six-node synthetic graph, active-power transport capacities, no voltage model',
          'cyber': 'Four-bus DC measurement/control example with explicitly assumed trusted sensors'}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, allow_nan=False).encode()).hexdigest()


class MethodLlama:
    def __init__(self, journal, model='llama3.1:8b'):
        import requests
        self.requests, self.journal, self.model = requests, Path(journal), model
        self.calls = []

    def ask(self, role, context, choices):
        schema = {'type': 'object', 'properties': {'choice': {'type': 'string', 'enum': choices},
                  'reason': {'type': 'string'}}, 'required': ['choice', 'reason'], 'additionalProperties': False}
        system = ('You are a bounded agent in an educational numerical workflow. Select a permitted choice '
                  'and explain it briefly from the supplied evidence. VOLTVAR_OPF optimizes continuous '
                  'inverter P/Q. RESTORATION_MILP selects load pickup and an energized tree. '
                  'WLS_TRUSTED_REDISPATCH estimates states and uses explicitly trusted measurements for '
                  'a small DC redispatch example. These tools have different scopes. You cannot change '
                  'constraints, invent trust, claim field safety or acknowledge for a person. Numerical '
                  'routines compute all setpoints. Return JSON only.')
        record = {'role': role, 'context': context, 'schema': schema, 'system': system,
                  'model': self.model, 'utc': datetime.now(timezone.utc).isoformat()}
        started = time.perf_counter()
        try:
            reply = self.requests.post('http://localhost:11434/api/chat', json={
                'model': self.model, 'messages': [{'role': 'system', 'content': system},
                                                {'role': 'user', 'content': json.dumps(context)}],
                'format': schema, 'stream': False, 'keep_alive': '30m',
                'options': {'temperature': 0, 'seed': 11, 'num_ctx': 8192, 'num_predict': 200}}, timeout=120)
            reply.raise_for_status()
            raw = reply.json()
            record['raw_response'] = raw
            parsed = json.loads(raw['message']['content'])
            if set(parsed) != {'choice', 'reason'} or parsed['choice'] not in choices or not isinstance(parsed['reason'], str):
                raise ValueError('Response schema mismatch')
            record['response'] = parsed
            provenance = 'actual_local_llama'
        except Exception as error:
            record['error'] = f'{type(error).__name__}: {error}'
            record['response'] = {'choice': 'REVIEW', 'reason': 'Local model or schema failure; inspect journal.'}
            provenance = 'local_failure_fallback'
        record['seconds'] = time.perf_counter() - started
        record['call_id'] = len(self.calls) + 1
        self.calls.append(record)
        self.journal.write_text(json.dumps(self.calls, indent=2, allow_nan=False), encoding='utf-8')
        return {**record['response'], 'call_id': record['call_id'], 'seconds': record['seconds'],
                'provenance': provenance, 'error': record.get('error')}


def numerical_tool(case, backend):
    from .standard_formulations import run_voltvar, solve_restoration_milp, run_wls_demo
    if case == 'voltage':
        result = run_voltvar(backend)
        point = result['optimized']
        summary = {k: point[k] for k in ('control', 'p_actual_kw', 'q_actual_kvar', 'objective', 'violations', 'accepted')}
        summary['scope'] = result['scope']
        accepted = bool(result['validation']['fresh_backend_accepted'])
        checks = result['validation']
    elif case == 'restoration':
        result = solve_restoration_milp(100.)
        summary = {k: result['milp'][k] for k in ('objective', 'served_kw', 'critical_served_kw', 'pickup', 'closed_edges', 'mip_gap')}
        summary['scope'] = SCOPES[case]
        accepted = bool(result['milp']['success'] and result['agreement'])
        checks = {'solver_success': result['milp']['success'], 'independent_enumeration_agreement': result['agreement'],
                  'scope': 'Discrete pickup and graph-flow constraints only; no AC voltage or protection check'}
    else:
        result = run_wls_demo()
        recovery = result['trusted_recovery']
        control = recovery['control']
        summary = {'trusted_state_estimate': recovery['estimate'], 'rank': recovery['rank'],
                   'residual_degrees_of_freedom': recovery['chi_square']['degrees_of_freedom'], 'control': control,
                   'scope': SCOPES[case]}
        accepted = bool(recovery['rank'] == 3 and control['status'] == 'PROPOSE' and control['actual_violation_count'] == 0)
        checks = {'trusted_observability_rank': recovery['rank'], 'trusted_channels_assumed': True,
                  'actual_toy_model_violation_count': control.get('actual_violation_count'),
                  'scope': 'DC toy-model validation, not the full distribution feeder or authenticated communications'}
    return result, summary, accepted, checks


def run_case(case, backend='lindistflow3', supervisor='fixed', llama=None):
    if case not in TOOLS or backend not in ('opendss', 'lindistflow3') or supervisor not in ('fixed', 'agentic'):
        raise ValueError('Unsupported task, model or supervisor')
    if supervisor == 'agentic' and llama is None:
        raise ValueError('Agentic mode requires an actual model client; use fixed for numerical-only execution')
    started = time.perf_counter()
    trace = []
    def stage(name, method, status, response):
        trace.append({'stage': name, 'method': method, 'status': status, 'response': response})
    specification = {'use_case': case, 'authorized_tool': TOOLS[case], 'scope': SCOPES[case],
                     'backend': backend if case == 'voltage' else 'separate_reduced_teaching_model',
                     'approved_inputs': 'Supplied transparent simulation fixtures; no live utility measurements'}
    stage('Awareness', 'Declared scenario/schema and model-coverage checks', 'PASS', specification)
    routing = ({'choice': TOOLS[case], 'reason': 'Fixed mapping from structured use case to its numerical tool',
                'provenance': 'deterministic'} if supervisor == 'fixed' else
               llama.ask('Planning', specification, [*TOOLS.values(), 'REVIEW']))
    if routing['choice'] != TOOLS[case]:
        stage('Planning', 'Tool-family selection with application scope gate', 'REVIEW', routing)
        for name in ('Execution proposal', 'Simulation', 'Verification', 'Recovery', 'Explanation'):
            stage(name, 'Fail-closed routing gate', 'NOT_RUN', {'reason': 'No permitted numerical plan was selected'})
        summary, accepted, numerical = {'reason': 'Routing requires review'}, False, None
    else:
        try:
            numerical, summary, accepted, checks = numerical_tool(case, backend)
            stage('Planning', TOOLS[case] + ' with fixed parameters', 'SOLVED',
                  {'routing': routing, 'numerical_plan': summary})
            stage('Execution proposal', 'Extract the numerical solution; no physical actuation', 'PROPOSED', summary)
            stage('Simulation', 'Fresh selected electrical solve' if case == 'voltage' else
                  'Independent graph enumeration' if case == 'restoration' else 'DC response model using known synthetic truth',
                  'EVALUATED', checks)
            stage('Verification', 'Declared numerical success and modeled-constraint checks',
                  'PASS' if accepted else 'REJECT', checks)
            stage('Recovery', 'One numerical attempt; unsuccessful verification requires review',
                  'NOT_NEEDED' if accepted else 'REVIEW', {'additional_attempts': 0})
            report = ({'choice': 'REPORT_LIMITS', 'reason': 'Return numerical evidence and the declared model scope',
                       'provenance': 'deterministic'} if supervisor == 'fixed' else
                      llama.ask('Explanation', {'use_case': case, 'numerical_summary': summary,
                                'passed_modeled_checks': accepted}, ['REPORT_LIMITS', 'REVIEW']))
            stage('Explanation', 'Numerical metric card and separately labeled explanation',
                  'REVIEW' if report['choice'] == 'REVIEW' else 'RECORDED', report)
            if report['choice'] == 'REVIEW':
                accepted = False
        except Exception as error:
            summary, accepted, numerical = {'error': f'{type(error).__name__}: {error}'}, False, None
            # Preserve the routing response if a numerical tool fails.
            if len(trace) == 1:
                stage('Planning', TOOLS[case], 'FAILED', {'routing': routing, **summary})
            for name in ('Execution proposal', 'Simulation', 'Verification', 'Recovery', 'Explanation'):
                if not any(row['stage'] == name for row in trace):
                    stage(name, 'Stop on numerical failure', 'REVIEW', summary)
    stage('Operator acknowledgment', 'Human review of immutable result identity', 'PENDING',
          {'acknowledged': False, 'dispatch_authorized': False, 'equipment_operated': False})
    row = {'case': case, 'backend': specification['backend'], 'supervisor': supervisor,
           'status': 'MODEL_RECOMMEND' if accepted else 'REVIEW', 'summary': summary, 'trace': trace,
           'numerical_evidence': numerical, 'seconds': time.perf_counter()-started}
    row['review_id'] = fingerprint({'specification': specification, 'summary': summary, 'trace': trace})
    return row


def run_demo():
    folder = ROOT/'results'/('standard_stage_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8])
    folder.mkdir(parents=True)
    llama = MethodLlama(folder/'llama_calls.json')
    cases = [('voltage', 'opendss'), ('voltage', 'lindistflow3'), ('restoration', 'lindistflow3'), ('cyber', 'lindistflow3')]
    data = {'metadata': {'created_utc': datetime.now(timezone.utc).isoformat(),
                         'journal': folder.relative_to(ROOT).as_posix(),
                         'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                         'numerical_source_sha256': hashlib.sha256((ROOT/'src/standard_formulations.py').read_bytes()).hexdigest(),
                         'protocol': 'Four structured specifications, fixed then agentic; identical numerical parameters. One numerical attempt. No causal advantage or timing-distribution claim.'}, 'runs': []}
    for case, backend in cases:
        for supervisor in ('fixed', 'agentic'):
            print(case, backend, supervisor, flush=True)
            row = run_case(case, backend, supervisor, llama if supervisor == 'agentic' else None)
            data['runs'].append(row)
            (folder/'workflow.json').write_text(json.dumps(data, indent=2, allow_nan=False), encoding='utf-8')
    data['metadata']['actual_llama_calls'] = len(llama.calls)
    data['metadata']['llama_failures'] = sum(bool(call.get('error')) for call in llama.calls)
    (folder/'workflow.json').write_text(json.dumps(data, indent=2, allow_nan=False), encoding='utf-8')
    (ROOT/'results/standard_agent_workflow.json').write_text(json.dumps(data, indent=2, allow_nan=False), encoding='utf-8')
    return data


if __name__ == '__main__':
    argparse.ArgumentParser(description=__doc__).parse_args()
    run_demo()
