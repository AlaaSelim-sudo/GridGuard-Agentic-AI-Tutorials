"""Replay recorded Llama tool choices without importing or contacting a model.

The returned reasons are exact public JSON fields, not hidden reasoning. All
electrical results below are read from the dated archives, never recalculated.
The archived fixed P3 and cyber comparators produced identical numerical
results; their language calls demonstrate coordination, not a control benefit.
"""
from pathlib import Path
import hashlib
import html
import json
import math


ROOT = Path(__file__).resolve().parents[1]
VOLTAGE_RUN = 'results/workshop_run_opendss.json'
VOLTAGE_CALLS = 'results/continuous_llama_opendss_20260927T161223523552Z.json'
RESTORATION_RUN = 'results/proposal_complete_workflow.json'
RESTORATION_CALLS = 'results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json'
CYBER_RUN = 'results/standard_agent_workflow.json'
CYBER_CALLS = 'results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json'
GITHUB = 'https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/'


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _read(root, relative, hashes):
    raw = (root / relative).read_bytes()
    hashes[relative] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def _walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


def _one(items, description):
    items = list(items)
    _require(len(items) == 1, 'Expected one ' + description)
    return items[0]


def _verified_call(journal, call_id, trace, source):
    call = _one((c for c in journal if c.get('call_id') == call_id), 'journal call ' + str(call_id))
    try:
        public = json.loads(call['raw_response']['message']['content'])
    except (KeyError, TypeError, json.JSONDecodeError) as error:
        raise ValueError('Recorded call lacks a raw public JSON reply: ' + source) from error
    _require(public == call['response'], 'Raw and parsed replies disagree: ' + source)
    matches = [node for node in _walk(trace)
               if node.get('call_id') == call_id
               and all(node.get(key) == value for key, value in public.items())]
    match = _one(matches, 'matching trace reply for call ' + str(call_id))
    _require(math.isclose(match['seconds'], call['seconds'], rel_tol=0, abs_tol=1e-9),
             'Journal and trace durations disagree: ' + source)
    return call


def _context(call):
    if 'payload' in call:
        message = _one((m for m in call['payload']['messages'] if m['role'] == 'user'),
                       'recorded user message')
        return json.loads(message['content'])
    return call['context']


def _allowed(call):
    schema = call.get('schema', call.get('payload', {}).get('format', {}))
    properties = schema.get('properties', {})
    if 'choice' in properties:
        return list(properties['choice']['enum'])
    return list(properties['ranking']['items']['enum'])


def _step(call, title, facts, tool_result, result_data, next_step, journal, record):
    public = call['response']
    return {
        'title': title,
        'call_id': call['call_id'],
        'role': call['role'],
        'model': call.get('model', call.get('payload', {}).get('model')),
        'recorded_utc': call.get('utc'),
        'recorded_client_seconds': call['seconds'],
        'input_facts': facts,
        'allowed_choices': _allowed(call),
        'choice': public.get('choice', public.get('ranking')),
        'exact_public_reason': public['reason'],
        'tool_result': tool_result,
        'tool_result_data': result_data,
        'next_step': next_step,
        'source_paths': [journal, record],
        'verification': {'raw_json_equals_parsed_reply': True,
                         'reply_and_duration_match_trace': True},
    }


def _evaluation_summary(record):
    # Preserve exact returned fields and evidence identities without repeating
    # hundreds of bus/line records; the complete evidence stays in the source.
    return {key: record[key] for key in ('id', 'phase', 'candidate', 'candidate_hash',
            'evidence_hash', 'summary', 'failures', 'score')}


def _base(scenario, title, scope, distinction, trace_checkpoint, sources, hashes):
    return {
        'schema': 'recorded_llama_teaching_episode_v1',
        'scenario': scenario,
        'title': title,
        'mode': 'RECORDED REPLAY — no new LLM call or electrical solve',
        'scope': scope,
        'study_boundary': distinction,
        'notebook_alignment': trace_checkpoint,
        'reason_limit': 'Exact public returned explanations; no hidden reasoning is exposed or inferred.',
        'hash_limit': 'SHA-256 identifies the local source bytes; it does not authenticate measurements.',
        'source_sha256': {source: hashes[source] for source in sources},
        'steps': [],
    }


def load_episodes(root=ROOT):
    """Return three JSON-serializable recorded episodes with verified replies.

    Every reply is matched to raw model JSON and the corresponding result
    trace. Results retain their separate model scopes and authority boundaries.
    This function only reads six files and uses the Python standard library.
    """
    root = Path(root)
    hashes = {}
    voltage_run = _read(root, VOLTAGE_RUN, hashes)
    voltage_journal = _read(root, VOLTAGE_CALLS, hashes)
    restoration_suite = _read(root, RESTORATION_RUN, hashes)
    restoration_journal = _read(root, RESTORATION_CALLS, hashes)
    cyber_suite = _read(root, CYBER_RUN, hashes)
    cyber_journal = _read(root, CYBER_CALLS, hashes)

    run = voltage_run['agentic']
    _require(run['case'] == 'P3_current_reserve' and run['backend'] == 'opendss',
             'Expected the archived P3 OpenDSS study')
    calls = {i: _verified_call(voltage_journal, i, run['trace'], VOLTAGE_CALLS) for i in (1, 2, 3)}
    _require([calls[i]['response']['choice'] for i in (1, 2, 3)] ==
             ['VERIFY_SAC_FIRST', 'USE_MPC_PLAN', 'REVIEW_EVIDENCE'], 'Unexpected P3 route')
    first, second = run['attempts']
    p0, p1 = first['point'], second['point']
    operator = run['trace'][-1]
    _require(first['failures'] == ['thermal'] and not p0['accepted'] and p1['accepted']
             and not second['failures'], 'Unexpected archived P3 engineering checks')
    _require(operator['stage'] == 'Operator acknowledgment' and operator['status'] == 'PENDING'
             and not operator['response']['acknowledged'] and not run['equipment_operated'],
             'The archived P3 operator step must remain pending')
    voltage = _base('voltage', 'Voltage: reject the failed proposal, then check the fallback',
        'P3_current_reserve; supplied full MV/LV OpenDSS feeder; 27 September 2026.',
        'Separate from Classroom L2 and L3 test_01. No live SCADA, protection or transient study.',
        'Agent_Trace_and_Latency: T2 stages and operator card; T3 exact public replies.',
        [VOLTAGE_RUN, VOLTAGE_CALLS], hashes)
    ctx1, ctx2 = _context(calls[1]), _context(calls[2])
    contract = ctx1['contract']
    voltage['steps'] = [
        _step(calls[1], 'Request a fresh check of the SAC proposal', [
            'Forecast load multipliers: ' + str(contract['case']['forecast_loads']) + '.',
            f"Current allowance: {contract['allowed_current_percent_of_nominal']:g}% of nominal; voltage limits: {contract['voltage_limits_pu']} p.u.",
            'The saved SAC action is a proposal, not a checked command.',
        ], [
            f"OpenDSS: {p0['max_allowed_current_pct']:.6f}% of the allowed current; {p0['violations']['line_current']} current violations.",
            'Deterministic check: REJECT; failure = thermal.',
        ], first, 'The recorded route rejects SAC and asks Recovery for the next allowed step.',
            VOLTAGE_CALLS, VOLTAGE_RUN),
        _step(calls[2], 'Request a fresh check of the existing MPC fallback', [
            'The supplied failed checks are: ' + ', '.join(ctx2['failed_checks']) + '.',
            'An MPC plan already exists; its recovery-eligibility failure list is empty.',
            f"At most {contract['maximum_candidates']} candidate checks are permitted.",
        ], [
            f"OpenDSS: {p1['max_allowed_current_pct']:.6f}% of allowed current; no recorded violations.",
            f"Proposed P = {p1['p_actual_kw']:.3f} kW; Q = {p1['q_actual_kvar']:+.3f} kvar.",
        ], second, 'Keep the numerically passed candidate and ask how to focus the operator explanation.',
            VOLTAGE_CALLS, VOLTAGE_RUN),
        _step(calls[3], 'Explain the evidence without acknowledging for the operator', [
            f"The full-feeder first-action check passed; voltage is {p1['vmin']:.6f}–{p1['vmax']:.6f} p.u.",
            'Protection, transients and implementation authority remain outside this model.',
        ], [
            'Numerical status: ' + run['status'] + '; recorded human acknowledgment: ' + operator['status'] + '.',
            'Acknowledged = False; dispatch authorized = False; equipment operated = False.',
        ], {'metrics': p1, 'operator': operator['response']},
            'A person must review this exact packet through a separate authorized process. No human decision is recorded.',
            VOLTAGE_CALLS, VOLTAGE_RUN),
    ]
    same_voltage = voltage_run['fixed']['candidate'] == run['candidate'] and voltage_run['fixed']['metrics'] == run['metrics']
    _require(same_voltage, 'Expected identical fixed and language-supervised P3 numerical results')
    voltage['baseline_note'] = ('The fixed supervisor used the same SAC→MPC checks and returned the same numerical result. '
        'The replay shows bounded routing, not evidence of a better controller or reduced operator workload.')
    voltage['operator_state'] = operator['response']

    run = _one((r for r in restoration_suite['runs'] if r['case'] == 'restoration'
                and r['backend'] == 'lindistflow3' and r['supervisor'] == 'agentic'), 'feeder restoration run')
    calls = {i: _verified_call(restoration_journal, i, run['trace'], RESTORATION_CALLS) for i in (14, 15, 16)}
    _require(calls[14]['response']['choice'] == 'SHED_075' and calls[15]['response']['choice'] == 'SHED_065',
             'Unexpected feeder restoration refinements')
    evaluations = {e['id']: e for e in run['evaluations']}
    e2, e3, e4, e5 = (evaluations[key] for key in ('E02', 'E03', 'E04', 'E05'))
    ranking = _one((event['response'] for event in run['trace']
                    if event.get('response', {}).get('phase') == 'ranking'), 'restoration ranking guard')
    _require(not e3['failures'] and e4['failures'] == ['thermal'] and not e5['failures']
             and ranking['numerical_order'] == ['E03', 'E02']
             and ranking['language_order_agrees_with_cost'] is False
             and run['selected']['id'] == 'E05', 'Unexpected restoration guard or final recheck')
    restoration = _base('restoration', 'Restoration: test a smaller disconnection, then catch a ranking error',
        'MV feeder bypass catalog with fixed critical-load priorities; 27 September 2026.',
        'This is Classroom L10’s feeder catalog, not L6’s six-node restoration MILP. No physical switching sequence is verified.',
        'Classroom L10 full five-stage records. This study is not loaded by Agent_Trace T4, which uses a separate six-node MILP archive.',
        [RESTORATION_RUN, RESTORATION_CALLS], hashes)
    restoration['steps'] = [
        _step(calls[14], 'Choose a permitted new trial from the checked evidence', [
            'E01 failed its thermal check; E02 passed.',
            f"E02 serves {e2['summary']['served_kw']:.3f} kW with {e2['summary']['tie_loading_pct']:.6f}% tie loading.",
            'The first refinement is required by the recorded protocol; the model chooses between offered fractions.',
        ], [
            f"SHED_075 produces E03: {e3['summary']['served_kw']:.3f} kW served and {e3['summary']['critical_served_kw']:.3f} critical kW.",
            f"E03 passes at {e3['summary']['tie_loading_pct']:.6f}% tie loading; cost = {e3['score']:.6f} (smaller is better).",
        ], {'before': _evaluation_summary(e2), 'trial': _evaluation_summary(e3)}, 'Use E03 as the checked incumbent; one further trial remains.',
            RESTORATION_CALLS, RESTORATION_RUN),
        _step(calls[15], 'Try the remaining fraction without weakening the limit', [
            'E03 is the lowest-cost passed candidate; one refinement evaluation remains.',
            'SHED_065 means disconnecting 65% of ordered noncritical load objects, not 65% of kW.',
        ], [
            f"E04 reaches {e4['summary']['tie_loading_pct']:.6f}% tie loading: REJECT, thermal failure.",
            'The rejected trial has no eligible score; its larger served load cannot make it acceptable.',
        ], _evaluation_summary(e4), 'Discard the failed trial and rank only the already verified feasible candidates.',
            RESTORATION_CALLS, RESTORATION_RUN),
        _step(calls[16], 'Keep the numerical ranking guard when the explanation is wrong', [
            f"E02 cost = {e2['score']:.6f}; E03 cost = {e3['score']:.6f}; smaller is better.",
            'Only the passed candidates E03 and E02 are offered for ranking.',
        ], [
            'Returned language order: E02 → E03. Correct numerical order: E03 → E02.',
            f"The guard retains E03 and rechecks it as E05: {e5['summary']['served_kw']:.3f} kW served; no recorded failures.",
        ], {'ranking_guard': ranking, 'final_recheck': _evaluation_summary(e5)},
            'Return the checked proposal for human review; acknowledgment and dispatch remain False.',
            RESTORATION_CALLS, RESTORATION_RUN),
    ]
    fixed = _one((r for r in restoration_suite['runs'] if r['case'] == 'restoration'
                  and r['backend'] == 'lindistflow3' and r['supervisor'] == 'fixed'), 'fixed feeder restoration run')
    same_restoration = fixed['selected']['candidate'] == run['selected']['candidate'] and fixed['selected']['score'] == run['selected']['score']
    restoration['baseline_note'] = ('The paired fixed workflow returns the same final action and cost. '
        'This replay does not establish language-model superiority.' if same_restoration else
        'The fixed comparator is a separate recorded route; inspect the archive before claiming any performance advantage.')
    restoration['operator_state'] = run['operator']

    run = _one((r for r in cyber_suite['runs'] if r['case'] == 'cyber'
                and r['supervisor'] == 'agentic'), 'standard four-bus cyber run')
    calls = {i: _verified_call(cyber_journal, i, run['trace'], CYBER_CALLS) for i in (7, 8)}
    _require(calls[7]['response']['choice'] == 'WLS_TRUSTED_REDISPATCH'
             and calls[8]['response']['choice'] == 'REVIEW', 'Unexpected standard cyber route')
    summary = run['summary']
    control = summary['control']
    verification = _one((event for event in run['trace'] if event['stage'] == 'Verification'), 'cyber numerical check')
    operator = run['trace'][-1]
    _require(verification['status'] == 'PASS' and run['status'] == 'REVIEW'
             and operator['stage'] == 'Operator acknowledgment' and operator['status'] == 'PENDING',
             'Unexpected cyber verification or review state')
    cyber = _base('cyber', 'Cyber: route to the trusted-data tool, then retain human review',
        'Four-bus DC fixture; three explicitly assumed trusted angle channels; 21 September 2026.',
        'Separate from L10’s proposal-complete cyber route. Trust is supplied as an assumption, not created or authenticated by Llama.',
        'Agent_Trace_and_Latency: T6 exact standard cyber replies and numerical result.',
        [CYBER_RUN, CYBER_CALLS], hashes)
    cyber['steps'] = [
        _step(calls[7], 'Select the authorized tool without inventing measurement trust', [
            'The structured task already authorizes WLS_TRUSTED_REDISPATCH.',
            'Trusted sensors are explicitly assumed; no live utility measurements are supplied.',
            f"Three angles, rank {summary['rank']}; residual degrees of freedom = {summary['residual_degrees_of_freedom']}.",
        ], [
            f"The numerical tool proposes u = {control['flexible_injection_pu']:.9f} p.u.; predicted flow12 = {control['predicted_flows_pu'][1]:.6f} p.u.",
            f"Offline synthetic-truth flow12 = {control['actual_toy_model_flows_pu'][1]:.6f} p.u.; rating = {control['line_limits_pu'][1]:.6f} p.u.",
        ], summary, 'The numerical check passes within this fixture; request a separately labeled explanation.',
            CYBER_CALLS, CYBER_RUN),
        _step(calls[8], 'Respect the returned REVIEW decision despite passing checks', [
            'The model receives the actual numerical summary and passed_modeled_checks = True.',
            'No communication authentication, AC feeder or operating-permission check is included.',
        ], [
            'Numerical verification: PASS. Language choice: REVIEW. Overall result: REVIEW.',
            'Human acknowledgment: PENDING; dispatch authorized = False; equipment operated = False.',
        ], {'verification': verification, 'status': run['status'], 'operator': operator['response']},
            'Keep the recommendation under review. A person must resolve the trust premise and remaining engineering scope.',
            CYBER_CALLS, CYBER_RUN),
    ]
    fixed = _one((r for r in cyber_suite['runs'] if r['case'] == 'cyber'
                  and r['supervisor'] == 'fixed'), 'fixed standard cyber run')
    _require(fixed['summary'] == summary, 'Expected identical fixed and language-supervised cyber numerical results')
    cyber['baseline_note'] = ('The fixed comparator returns the same numerical estimate and correction without Llama. '
        'Llama selects an allowed tool and a report disposition; it does not authenticate sensors or improve this solver.')
    cyber['operator_state'] = operator['response']
    return {'voltage': voltage, 'restoration': restoration, 'cyber': cyber}


def extract_episode_data(root=ROOT):
    """Named export for presentation builders that need the structured records."""
    return load_episodes(root)


def render_episode_html(episode):
    """Return compact HTML; the notebook caller owns IPython display."""
    esc = lambda value: html.escape(str(value), quote=True)
    def bullets(items):
        return '<ul>' + ''.join('<li>' + esc(item) + '</li>' for item in items) + '</ul>'
    scenario = esc(episode['scenario'])
    out = ['<div class="llama-walkthrough" id="llama-replay-' + scenario + '" data-scenario="' + scenario + '"><style>']
    out.append('''
.llama-walkthrough{font:16px/1.5 Arial,sans-serif;color:#17384b;max-width:1120px;margin:16px 0}
.llama-walkthrough h2,.llama-walkthrough h3{color:#00629b;margin:8px 0}
.llama-walkthrough .lw-mode{font-weight:bold;color:#003b5c;background:#e8f3f7;padding:12px;border-left:5px solid #00a6b2}
.llama-walkthrough .lw-step{border:1px solid #bdced8;border-left:5px solid #00a6b2;border-radius:5px;padding:16px;margin:18px 0}
.llama-walkthrough .lw-row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.llama-walkthrough .lw-panel{background:#f4f8fa;padding:10px 14px;border-radius:4px;margin:5px 0}
.llama-walkthrough .lw-reason{background:#fff7e8;border-left:4px solid #a66610;padding:12px 15px;margin:12px 0}
.llama-walkthrough .lw-label{font-weight:bold;color:#003b5c}
.llama-walkthrough .lw-source{font-size:13px;color:#526470;overflow-wrap:anywhere}
.llama-walkthrough ul{margin:6px 0;padding-left:20px}.llama-walkthrough li{margin:5px 0}
.llama-walkthrough code{white-space:normal;overflow-wrap:anywhere}
@media(max-width:720px){.llama-walkthrough .lw-row{grid-template-columns:1fr}}
</style>''')
    out += ['<h2>' + esc(episode['title']) + '</h2>',
            '<p class="lw-mode">' + esc(episode['mode']) + '</p>',
            '<p>' + esc(episode['scope']) + '<br>' + esc(episode['study_boundary']) + '</p>',
            '<p>' + esc(episode['reason_limit']) + '</p>']
    for step_number, step in enumerate(episode['steps'], 1):
        choice = step['choice'] if isinstance(step['choice'], str) else ' → '.join(step['choice'])
        out += ['<section class="lw-step" id="llama-replay-' + scenario + '-call-' + esc(step['call_id']) + '" data-step="' + str(step_number) + '" data-call-id="' + esc(step['call_id']) + '"><h3>Call ' + esc(step['call_id']) + ' · ' + esc(step['title']) + '</h3>',
                '<div class="lw-row"><div class="lw-panel lw-input"><span class="lw-label">1. Input facts</span>' + bullets(step['input_facts']) + '</div>',
                '<div class="lw-panel lw-choice"><span class="lw-label">2. Allowed choice</span><p>' + esc(', '.join(step['allowed_choices'])) + '</p><p><b>Returned:</b> <code>' + esc(choice) + '</code></p></div></div>',
                '<div class="lw-reason"><span class="lw-label">3. Exact recorded public reason</span><p>“' + esc(step['exact_public_reason']) + '”</p></div>',
                '<div class="lw-row"><div class="lw-panel lw-result"><span class="lw-label">4. Actual tool result</span>' + bullets(step['tool_result']) + '</div>',
                '<div class="lw-panel lw-next"><span class="lw-label">5. Next step</span><p>' + esc(step['next_step']) + '</p></div></div>',
                '<p class="lw-source">' + esc(step['model']) + ' · ' + esc(step['role']) + ' · recorded client interval ' + f"{step['recorded_client_seconds']:.6f}" + ' s. Raw JSON, parsed reply and trace match.</p></section>']
    out += ['<p><b>Compare with automation:</b> ' + esc(episode['baseline_note']) + '</p>',
            '<p><b>Find the same archive:</b> ' + esc(episode['notebook_alignment']) + '</p>',
            '<details class="lw-source"><summary>Recorded sources and SHA-256 fingerprints</summary>']
    for path, digest in episode['source_sha256'].items():
        out.append('<p><a target="_blank" rel="noopener noreferrer" href="' + esc(GITHUB + path) + '">' + esc(path) + '</a><br><code>' + esc(digest) + '</code></p>')
    out += ['<p>' + esc(episode['hash_limit']) + '</p></details></div>']
    return ''.join(out)
