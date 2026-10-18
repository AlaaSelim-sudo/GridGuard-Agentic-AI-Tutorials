"""Read saved tutorial evidence without importing a solver or contacting Ollama.

Durations are individual recorded intervals, not latency distributions. The
report deliberately separates the current voltage protocol, the older small
MILP/DC protocol and the h06 operator-intake protocol.
"""
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]


def _read(root, relative, provenance):
    path = root / relative
    raw = path.read_bytes()
    provenance[relative] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def _language_nodes(value):
    if isinstance(value, dict):
        if 'choice' in value and 'seconds' in value and value.get('call_id'):
            yield value
        else:
            for item in value.values():
                yield from _language_nodes(item)
    elif isinstance(value, list):
        for item in value:
            yield from _language_nodes(item)


def _same_reply(node, call):
    return (node['call_id'] == call.get('call_id') and
            node['choice'] == call['response'].get('choice') and
            node['reason'] == call['response'].get('reason') and
            math.isclose(node['seconds'], call['seconds'], rel_tol=0, abs_tol=1e-9))


def _recorded_number(value, label, integer=False):
    """Require an observed finite nonnegative metric; missing is not zero."""
    if (type(value) not in (int, float) or not math.isfinite(value) or value < 0 or
            (integer and (type(value) is not int))):
        raise ValueError(f'{label} must be a recorded finite nonnegative ' +
                         ('integer' if integer else 'number'))
    return value


def _call_row(call, protocol, case, backend, path, number):
    raw = call['raw_response']
    reply = call['response']
    try:
        actual_reply = json.loads(raw['message']['content'])
    except (KeyError, TypeError, json.JSONDecodeError) as error:
        raise ValueError('Call lacks a valid raw JSON reply') from error
    if actual_reply != reply:
        raise ValueError('Raw model reply disagrees with the parsed journal response')
    client_s = _recorded_number(call.get('seconds'), 'Client call duration')
    durations = {key: _recorded_number(raw.get(key), key) / 1e9
                 for key in ('total_duration', 'load_duration',
                             'prompt_eval_duration', 'eval_duration')}
    counts = {key: _recorded_number(raw.get(key), key, integer=True)
              for key in ('prompt_eval_count', 'prompt_eval_cached_count', 'eval_count')}
    generation_s = durations['eval_duration']
    # Do not infer unseen stages by adding or subtracting server sub-durations.
    return dict(protocol=protocol, case=case, backend=backend,
                role=call.get('role', 'Interpreter'),
                choice=reply.get('choice', reply.get('status')),
                reason=reply.get('reason'), client_s=client_s,
                server_s=durations['total_duration'],
                load_s=durations['load_duration'],
                prompt_s=durations['prompt_eval_duration'],
                generation_s=generation_s,
                prompt_tokens=counts['prompt_eval_count'],
                cached_prompt_tokens=counts['prompt_eval_cached_count'],
                output_tokens=counts['eval_count'],
                generation_tokens_per_s=(counts['eval_count'] / generation_s
                                         if generation_s > 0 else None),
                model=raw.get('model'), utc=call.get('utc'),
                source=path, journal_index=number,
                call_id=call.get('call_id'),
                options=call.get('payload', {}).get('options'))


def load_recorded_evidence(root=ROOT):
    """Match each displayed reply to its journal; fail if the evidence diverges."""
    root = Path(root)
    hashes, calls, workflows, voltage = {}, [], [], {}
    for backend in ('opendss', 'lindistflow3'):
        path = f'results/workshop_run_{backend}.json'
        run = _read(root, path, hashes)
        if run['schema'] != 'continuous_workshop_v1':
            raise ValueError('Unexpected current voltage schema')
        voltage[backend] = run
        nodes = list(_language_nodes(run['agentic']['trace']))
        matches = []
        for candidate in sorted((root / 'results').glob(f'continuous_llama_{backend}_*.json')):
            journal = json.loads(candidate.read_bytes())
            if len(journal) == len(nodes) and all(_same_reply(n, c) for n, c in zip(nodes, journal)):
                matches.append((candidate.relative_to(root).as_posix(), journal))
        if len(matches) != 1:
            raise ValueError(f'Need one matching voltage journal for {backend}; found {len(matches)}')
        journal_path, journal = matches[0]
        _read(root, journal_path, hashes)
        case_calls = [_call_row(c, 'current_voltage', 'voltage', backend, journal_path, i)
                      for i, c in enumerate(journal, 1)]
        calls.extend(case_calls)
        for route in ('fixed', 'agentic'):
            result = run[route]
            duration = _recorded_number(result.get('seconds'), 'Voltage workflow duration')
            declared_calls = _recorded_number(result.get('llm_calls'), 'Voltage LLM call count', integer=True)
            if declared_calls != (len(case_calls) if route == 'agentic' else 0):
                raise ValueError('Declared voltage call count disagrees with the matched journal')
            llm_s = sum(c['client_s'] for c in case_calls) if route == 'agentic' else 0.
            if llm_s > duration + 1e-6:
                raise ValueError('LLM intervals exceed containing workflow interval')
            workflows.append(dict(protocol='current_voltage', case='voltage', backend=backend,
                                  route=route, seconds=duration, status=result['status'],
                                  llm_calls=declared_calls, llm_client_s=llm_s,
                                  other_in_interval_s=duration - llm_s,
                                  source=path,
                                  scope='Supervisor including calls/checks; excludes precomputed MPC/SAC and training'))
    standard = _read(root, 'results/standard_agent_workflow.json', hashes)
    standard_path = standard['metadata']['journal'].rstrip('/') + '/llama_calls.json'
    journal = _read(root, standard_path, hashes)
    standard_runs = [r for r in standard['runs'] if r['case'] in ('restoration', 'cyber')]
    for run in standard_runs:
        case_calls = []
        for node in _language_nodes(run['trace']):
            matched = [(i, c) for i, c in enumerate(journal, 1) if _same_reply(node, c)]
            if len(matched) != 1:
                raise ValueError('Standard workflow reply has no unique exact journal match')
            i, call = matched[0]
            case_calls.append(_call_row(call, 'historical_standard', run['case'],
                                        run['backend'], standard_path, i))
        calls.extend(case_calls)
        llm_s = sum(c['client_s'] for c in case_calls)
        duration = _recorded_number(run.get('seconds'), 'Standard workflow duration')
        if llm_s > duration + 1e-6:
            raise ValueError('Invalid standard interval nesting')
        workflows.append(dict(protocol='historical_standard', case=run['case'], backend=run['backend'],
                              route=run['supervisor'], seconds=duration, status=run['status'],
                              llm_calls=len(case_calls), llm_client_s=llm_s,
                              other_in_interval_s=duration - llm_s,
                              source='results/standard_agent_workflow.json',
                              scope='Whole small-model workflow including numerical method and calls'))
    confirmation = _read(root, 'results/confirmation.json', hashes)
    h06 = [r for r in confirmation['rows'] if r['id'] == 'h06']
    if len(h06) != 2 or {r.get('method') for r in h06} != {'rule_parser', 'hybrid'}:
        raise ValueError('Expected one parser and one hybrid record for h06')
    hybrid = next(r for r in h06 if r['method'] == 'hybrid')
    intake_path = 'results/confirmation_calls.json'
    intake_calls = _read(root, intake_path, hashes)
    matches = []
    for i, call in enumerate(intake_calls, 1):
        for msg in call['payload']['messages']:
            if msg['role'] == 'user':
                context = json.loads(msg['content'])
                if context.get('operator_request') == hybrid['request']:
                    matches.append((i, call))
    if len(matches) != 1:
        raise ValueError('h06 request has no unique journal match')
    i, call = matches[0]
    if hybrid['interpretation'] != call['response']:
        raise ValueError('h06 interpretation does not match recorded reply')
    intake_call = _call_row(call, 'historical_intake', 'h06', 'opendss', intake_path, i)
    calls.append(intake_call)
    for row in h06:
        for key in ('machine_seconds', 'intake_seconds', 'runtime_seconds'):
            _recorded_number(row.get(key), 'h06 ' + key)
        expected_calls = 1 if row['method'] == 'hybrid' else 0
        if _recorded_number(row.get('llm_calls'), 'h06 call count', integer=True) != expected_calls:
            raise ValueError('h06 declared call count disagrees with its method')
        if not math.isclose(row['machine_seconds'], row['intake_seconds'] + row['runtime_seconds'], rel_tol=0, abs_tol=1e-8):
            raise ValueError('h06 machine duration is not intake plus runtime')
    if intake_call['client_s'] > hybrid['intake_seconds'] + 1e-6:
        raise ValueError('h06 Llama interval exceeds its containing intake interval')
    return dict(voltage=voltage, standard_runs=standard_runs, h06=h06,
                calls=calls, workflows=workflows, source_sha256=hashes,
                caveat='Single recorded intervals; no p50/p95, hardware attribution, energy, price or human time measured.')


def stage_rows(run):
    """Keep full stage replies; measured seconds only for recorded Llama calls."""
    rows = []
    for stage in run['trace']:
        nodes = list(_language_nodes(stage['response']))
        rows.append(dict(stage=stage['stage'], method=stage['method'], status=stage['status'],
                         response_source=stage.get('response_source', 'See response provenance'),
                         returned_response=stage['response'],
                         choices='; '.join(n['choice'] for n in nodes),
                         returned_reasons=' | '.join(n['reason'] for n in nodes),
                         measured_llm_call_s=sum(n['seconds'] for n in nodes) if nodes else None))
    return rows


def plot_workflow_latency(evidence):
    """Four paired panels: periods and included work differ across protocols."""
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 2, figsize=(11, 6.8), constrained_layout=True)
    groups = [('voltage', 'opendss', 'Current voltage / OpenDSS'),
              ('voltage', 'lindistflow3', 'Current voltage / MV LinDistFlow'),
              ('restoration', 'milp', 'Historical six-node restoration'),
              ('cyber', 'dc', 'Historical four-bus cyber')]
    for ax, (case, backend, title) in zip(axes.flat, groups):
        rows = [r for r in evidence['workflows'] if r['case'] == case and
                (case != 'voltage' or r['backend'] == backend)]
        for n, row in enumerate(rows):
            ax.barh(n, row['llm_client_s'], color='#006b47', label='Llama client calls' if n == 0 else '')
            ax.barh(n, row['other_in_interval_s'], left=row['llm_client_s'], color='#b1d6c7',
                    label='Other work in interval' if n == 0 else '')
            ax.text(row['seconds'] + .05, n, f"{row['seconds']:.3f} s | {row['status']}", va='center', fontsize=8)
        ax.set_yticks(range(len(rows)), [r['route'] for r in rows]); ax.invert_yaxis()
        ax.set_xlim(0, max(r['seconds'] for r in rows) * 1.8)
        ax.set_title(title, fontsize=11); ax.set_xlabel('Recorded wall-clock seconds'); ax.grid(axis='x', alpha=.2)
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='outside lower center', ncol=2, fontsize=9)
    fig.suptitle('One recorded pair per setting; separate protocols, no latency distribution', fontsize=12)
    return fig


def plot_call_latency(evidence):
    import matplotlib.pyplot as plt
    rows = evidence['calls']
    fig, ax = plt.subplots(figsize=(11, 6), constrained_layout=True)
    labels = [f"{r['case']} / {r['backend'] if r['case'] == 'voltage' else 'teaching model'} / {r['role']}" for r in rows]
    y = list(range(len(rows)))
    ax.barh([v-.18 for v in y], [r['client_s'] for r in rows], height=.34, color='#006b47', label='Client interval')
    ax.barh([v+.18 for v in y], [r['server_s'] for r in rows], height=.34, color='#b26b19', label='Ollama total_duration')
    ax.set_yticks(y, labels, fontsize=8); ax.invert_yaxis(); ax.set_xlabel('Recorded seconds')
    ax.set_title('Client and server are nested measurements, not additive components')
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='outside lower center', ncol=2)
    ax.grid(axis='x', alpha=.2)
    return fig
