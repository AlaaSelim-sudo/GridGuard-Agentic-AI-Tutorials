"""Read-only, case-specific comparisons from the tutorial's recorded evidence.

These helpers make no model calls, change no controls, and operate no equipment.
They retain unfavorable Llama decisions and separate a provisional numerical
candidate from a final workflow recommendation.  All power-flow consequences
are simulated, including the deliberately ungated proposal comparisons.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'


def _read(name):
    return json.loads((RESULTS / name).read_text(encoding='utf-8'))


def voltage_comparison(fixed, agentic):
    """Compare the raw SAC proposal with two supervisors in one paired case.

The raw proposal is the recorded first SAC attempt, audited in the selected
model. It is a baseline without a corrective gate, not an equipment dispatch.
An agentic REVIEW remains REVIEW even if a numerical candidate passed checks.
"""
    if (fixed['backend'], fixed['case'], fixed['case_definition']) != (
            agentic['backend'], agentic['case'], agentic['case_definition']):
        raise ValueError('The comparison requires the same backend and case definition.')
    attempts = fixed.get('attempts', [])
    if not attempts or attempts[0]['candidate'].get('tool') != 'SAC':
        raise ValueError('The fixed record must retain the common first SAC proposal.')
    first = attempts[0]

    def row(label, candidate, point, failures, status, gate_used, llm_calls):
        control = candidate.get('control', []) if candidate else []
        return {
            'method': label, 'backend': fixed['backend'], 'case': fixed['case'],
            'proposal_tool': candidate.get('tool') if candidate else None,
            'P_fraction': control[0] if len(control) == 2 else None,
            'Q_fraction': control[1] if len(control) == 2 else None,
            'simulated_P_kW': point.get('p_actual_kw'),
            'simulated_Q_kvar': point.get('q_actual_kvar'),
            'maximum_current_pct_of_allowance': point.get('max_allowed_current_pct'),
            'numerical_candidate_passed': bool(point) and not failures and point.get('accepted') is True,
            'candidate_failure_reasons': ', '.join(failures),
            'corrective_gate_used': gate_used,
            'workflow_status': status, 'LLM_calls': llm_calls,
            'equipment_operated': False,
        }

    rows = [row('Raw SAC proposal (audit only)', first['candidate'], first['point'],
                first['failures'], 'UNGATED_PROPOSAL', False, 0)]
    for label, run in [('Conventional adaptive supervisor', fixed),
                       ('Agentic supervisor', agentic)]:
        last = run.get('attempts', [])[-1] if run.get('attempts') else {}
        candidate = run.get('candidate') or last.get('candidate')
        point = last.get('point', {})
        rows.append(row(label, candidate, point, last.get('failures', ['not_evaluated']),
                        run['status'], True, run.get('llm_calls', 0)))
    return rows


def restoration_language_comparison():
    """Return tables and the exact actual Llama reply for the outage subset.

This is a descriptive, post-hoc selection by scene from a previously frozen
confirmation record: five clear requests and two missing/prohibited requests.
It is not a fresh prospective restoration benchmark or an operator time study.
"""
    all_rows = _read('confirmation.json')['rows']
    selected = [x for x in all_rows if x['scene'] == 'outage']
    clear_ids = ['h03', 'h04', 'h06', 'h07', 'h08']
    clarification_ids = ['h10', 'h11']
    expected = set(clear_ids + clarification_ids)
    summary, requests = [], []
    for method, label in [('rule_parser', 'Conventional documented parser'),
                          ('hybrid', 'Parser then Llama when needed')]:
        rows = [x for x in selected if x['method'] == method]
        if len(rows) != 7 or {x['id'] for x in rows} != expected:
            raise ValueError('Restoration confirmation subset differs from the declared seven requests.')
        clear = [x for x in rows if x['id'] in clear_ids]
        clarify = [x for x in rows if x['id'] in clarification_ids]
        summary.append({
            'method': label,
            'clear_requests': len(clear),
            'correct_automatic_completions': sum(bool(x['correct_automatic_completion']) for x in clear),
            'unnecessary_handoffs': sum(bool(x['unnecessary_handoff']) for x in clear),
            'missing_or_prohibited_requests': len(clarify),
            'correct_clarifications': sum(bool(x['correct_semantic_clarification']) for x in clarify),
            'incorrect_READY_interpretations': sum(bool(x['incorrect_ready_interpretation']) for x in rows),
            'actual_LLM_calls': sum(x['llm_calls'] for x in rows),
        })
        for x in rows:
            interpretation = x['interpretation']
            runtime = x.get('runtime') or {}
            metrics = runtime.get('metrics') or {}
            requests.append({
                'request_id': x['id'], 'method': label,
                'request_type': 'clear' if x['id'] in clear_ids else 'missing value' if x['id'] == 'h10' else 'prohibited action',
                'request': x['request'], 'intake_status': interpretation['status'],
                'short_bypass_limit_A': interpretation['short_limit_amps'],
                'allow_long_tie': interpretation['allow_long_tie'],
                'allow_PV': interpretation['allow_pv'],
                'correct_automatic_completion': x['correct_automatic_completion'],
                'correct_clarification': x['correct_semantic_clarification'],
                'downstream_status': runtime.get('status', 'NOT_RUN'),
                'simulated_served_kW': metrics.get('served_kw'),
                'simulated_critical_served_kW': metrics.get('critical_served_kw'),
                'maximum_current_pct_of_allowance': metrics.get('max_line_pct'),
                'interpretation_reason': interpretation['reason'],
                'equipment_operated': False,
            })
    h06 = next(x for x in selected if x['id'] == 'h06' and x['method'] == 'hybrid')
    matched_calls = []
    for call in _read('confirmation_calls.json'):
        messages = call.get('payload', {}).get('messages', [])
        for message in messages:
            if message.get('role') == 'user':
                context = json.loads(message['content'])
                if context.get('operator_request') == h06['request']:
                    matched_calls.append(call)
    if len(matched_calls) != 1:
        raise ValueError('Expected exactly one actual recorded h06 Llama response.')
    raw_reply = matched_calls[0]['raw_response']['message']['content']
    if json.loads(raw_reply) != h06['interpretation']:
        raise ValueError('The raw h06 response and recorded interpretation do not agree.')
    return {
        'summary': summary, 'requests': requests,
        'h06_llama_response': raw_reply,
        'scope_note': (
            'Recorded historical feeder experiment, using the original finite restoration catalog and OpenDSS; '
            'not the continuous SAC voltage experiment. Descriptive post-hoc outage subset of the frozen '
            'confirmation set: seven request cases, of which five are clear (h03, h04, h06, h07, h08) '
            'and two require clarification (h10 missing current value; h11 prohibited fault reclosure). '
            'Both methods share the same downstream numerical tools and verifier. The observed gain '
            'is request completion against this documented parser, not a better restoration optimum '
            'or measured operator-time reduction.'),
    }


def cyber_comparison():
    """Compare a compromised-data baseline and matched trusted-data workflows.

Candidate consequences use known synthetic truth in a four-bus DC model.
The agentic candidate remains provisional when the recorded Llama says REVIEW.
The trusted sensor branch is explicitly supplied, not discovered by the LLM.
"""
    numerical = _read('standard_formulations.json')['cyber']
    naive = next(x for x in numerical['cases'] if x['name'] == 'stealth_Hc')
    rows = []

    def row(label, control, status, trusted, provisional, llm_calls):
        return {
            'method': label, 'protected_measurements_supplied': trusted,
            'candidate_injection_pu': control['flexible_injection_pu'],
            'simulated_actual_flow_1_2_pu': control['actual_toy_model_flows_pu'][1],
            'flow_1_2_limit_pu': control['line_limits_pu'][1],
            'simulated_violation_count': control['actual_violation_count'],
            'workflow_status': status, 'candidate_is_provisional': provisional,
            'LLM_calls': llm_calls, 'equipment_operated': False,
        }

    rows.append(row('Compromised WLS + redispatch', naive['control'],
                    'NUMERICAL_PROPOSAL_ONLY', False, True, 0))
    workflows = _read('standard_agent_workflow.json')['runs']
    for supervisor, label in [('fixed', 'Conventional adaptive + protected data'),
                              ('agentic', 'Agentic + same protected data')]:
        matching = [x for x in workflows if x['case'] == 'cyber' and x['supervisor'] == supervisor]
        if len(matching) != 1:
            raise ValueError('Expected one recorded cyber run per supervisor.')
        run = matching[0]
        calls = set()
        for stage in run['trace']:
            response = stage.get('response', {})
            if 'call_id' in response:
                calls.add(response['call_id'])
            if 'call_id' in response.get('routing', {}):
                calls.add(response['routing']['call_id'])
        rows.append(row(label, run['summary']['control'], run['status'], True,
                        run['status'] != 'MODEL_RECOMMEND', len(calls)))
    return rows


def evidence_report():
    """Build a reproducible report; source hashes refer to the records read."""
    source_names = ['confirmation.json', 'confirmation_calls.json',
                    'standard_formulations.json', 'standard_agent_workflow.json',
                    'workshop_run_opendss.json', 'workshop_run_lindistflow3.json']
    voltage = []
    for backend in ('opendss', 'lindistflow3'):
        saved = _read('workshop_run_' + backend + '.json')
        voltage.extend(voltage_comparison(saved['fixed'], saved['agentic']))
    return {
        'schema': 'case_comparison_evidence_v1',
        'generated_utc': datetime.now(timezone.utc).isoformat(),
        'source_sha256': {'results/' + name: hashlib.sha256((RESULTS / name).read_bytes()).hexdigest()
                          for name in source_names},
        'helper_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'voltage': voltage,
        'restoration_language': restoration_language_comparison(),
        'cyber': cyber_comparison(),
        'interpretation_limits': [
            'Read-only comparison of recorded results; no new Llama calls or numerical solves.',
            'Voltage raw SAC is a provisional proposal audited in the selected model, never an actual unchecked dispatch.',
            'Fixed and agentic voltage supervision use the same proposal, MPC contingency, model, and checks; both repair the recorded OpenDSS current violation.',
            'Restoration language counts are a descriptive post-hoc subset of a previously frozen authored confirmation set, not a new prospective benchmark.',
            'Cyber recovery benefits arise from supplied protected measurements and numerical redispatch; the same tools yield the same physical toy consequences in both supervisors.',
            'The recorded cyber Llama explanation escalates to REVIEW despite passed numerical checks; no additional LLM detection/control advantage is demonstrated.',
            'An equipment_operated=false value applies to every row. No utility deployment, operator-time saving, or generalized reliability claim is measured.',
        ],
    }


if __name__ == '__main__':
    destination = RESULTS / 'case_comparison_evidence.json'
    destination.write_text(json.dumps(evidence_report(), indent=2, allow_nan=False), encoding='utf-8')
    print(destination)
