"""Portable tables, plots and public stage responses for the proposal workflow.

Reading saved evidence never invokes an electrical solver or a language model.
Recorded stage time, HTTP-call time and whole-workflow time are kept distinct.
"""
from pathlib import Path
import hashlib
import html
import json
import math

ROOT = Path(__file__).resolve().parents[1]
STAGES = ['Awareness Agent', 'Planning Agent', 'Simulation Agent',
          'Verification Agent', 'LLM Optimizer']
SETTINGS = [('voltage', 'opendss'), ('voltage', 'lindistflow3'),
            ('restoration', 'opendss'), ('restoration', 'lindistflow3'),
            ('cyber_isolated', 'dc'), ('cyber_stealth', 'dc')]
LABELS = {'voltage': 'Voltage support', 'restoration': 'Restoration',
          'cyber_isolated': 'Isolated corruption', 'cyber_stealth': 'Stealth Hc'}


def _hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _replies(run):
    for event in run['trace']:
        response = event['response']
        if isinstance(response, dict) and isinstance(response.get('language_response'), dict):
            yield event, response['language_response']


def _journal_name(run):
    return 'qwen_calls.json' if str(run.get('model', '')).startswith('qwen') else 'llama_calls.json'


def _match_call(suite, run, reply):
    if reply.get('source') == 'deterministic':
        return None
    rows = suite['_display_journals'].get(_journal_name(run), [])
    matched = [row for row in rows if row.get('call_id') == reply.get('call_id')]
    if len(matched) != 1:
        raise ValueError('Recorded stage reply has no unique call-journal entry')
    call = matched[0]
    response = call.get('response', {})
    for key in ('choice', 'ranking', 'reason'):
        if response.get(key) != reply.get(key):
            raise ValueError('Stage response differs from its call journal: ' + key)
    if call.get('source') != reply.get('source') or call.get('seconds') != reply.get('seconds'):
        raise ValueError('Response provenance or duration differs from the call journal')
    return call


def load_suite(path=None, verify_sources=True):
    """Load a complete saved suite, bind its responses to the actual journals."""
    path = ROOT/'results/proposal_complete_workflow.json' if path is None else Path(path)
    if not path.is_absolute():
        path = ROOT/path
    suite = json.loads(path.read_text(encoding='utf-8'))
    if suite.get('schema') != 'proposal_suite_v1' or not isinstance(suite.get('runs'), list):
        raise ValueError('Expected proposal_suite_v1 saved evidence')
    seen = {(run['case'], run['backend'], run['supervisor']) for run in suite['runs']}
    expected = {(case, backend, route) for case, backend in SETTINGS for route in ('fixed', 'agentic')}
    if seen != expected or len(suite['runs']) != len(expected):
        raise ValueError('Incomplete or duplicated matched suite')
    journal_folder = (ROOT/suite['journal_folder']).resolve()
    if not journal_folder.is_relative_to(ROOT.resolve()):
        raise ValueError('Journal path must remain within the tutorial folder')
    suite['_display_journals'] = {}
    for name in ('llama_calls.json', 'qwen_calls.json'):
        file = journal_folder/name
        if file.exists():
            suite['_display_journals'][name] = json.loads(file.read_text(encoding='utf-8'))
    audit = []
    for name, expected_hash in suite.get('source_sha256', {}).items():
        file = ROOT/'src'/name
        actual = _hash(file)
        audit.append({'source': name, 'recorded_sha256': expected_hash,
                      'current_sha256': actual, 'matches': actual == expected_hash})
    if verify_sources and any(not row['matches'] for row in audit):
        raise ValueError('Scientific source differs from this run; inspect source_audit before interpreting it')
    suite['_display_source_audit'] = audit
    all_runs = list(suite['runs'])
    if suite.get('model_portability_example'):
        all_runs.append(suite['model_portability_example'])
    for run in all_runs:
        if run.get('schema') != 'proposal_complete_v1':
            raise ValueError('Unknown individual run schema')
        replies = list(_replies(run))
        actual_calls = 0
        for _, reply in replies:
            if _match_call(suite, run, reply) is not None:
                actual_calls += 1
        if actual_calls != run['llm_calls']:
            raise ValueError('Run call count differs from its stage responses')
        if not math.isfinite(run['seconds']) or run['seconds'] < 0:
            raise ValueError('Invalid whole-workflow duration')
    return suite


def source_audit(suite):
    import pandas as pd
    return pd.DataFrame(suite['_display_source_audit'])


def select_run(suite, case, backend, supervisor='agentic', portability=False):
    if portability:
        row = suite.get('model_portability_example')
        if not row or row['case'] != case or row['backend'] != backend:
            raise ValueError('No matching optional model-portability example')
        return row
    rows = [row for row in suite['runs'] if row['case'] == case and row['backend'] == backend
            and row['supervisor'] == supervisor]
    if len(rows) != 1:
        raise ValueError('Select one recorded case/backend/supervisor combination')
    return rows[0]


def contract_table():
    """A compact visual reading of all five modules, independent of solvers."""
    import pandas as pd
    return pd.DataFrame([
        [STAGES[0], 'Observe', 'Model snapshot, alarms, topology, DER and forecast', 'State contract'],
        [STAGES[1], 'Propose', 'Model-free policy and/or model-based candidate tools', 'Two initial actions'],
        [STAGES[2], 'Simulate', 'Fresh OpenDSS, three-phase LinDistFlow or DC evaluation', 'Physical consequences'],
        [STAGES[3], 'Verify', 'Numerical limits, evidence identity and operating policy', 'Pass or explicit rejection'],
        [STAGES[4], 'Refine + rank', 'Bounded Llama critique, tool selection and feasible ordering', 'New trial and auditable ranking'],
    ], columns=['Proposal module', 'Question/action', 'Specific method', 'Output'])


def _short_response(event):
    row = event['response']
    stage = event['stage']
    if stage == STAGES[0]:
        aware = row.get('awareness', {})
        return 'Alarms: ' + (', '.join(aware.get('alarms', [])) or 'none in modeled checks') + '; ' + row.get('scope', '')
    if stage == STAGES[1]:
        return ', '.join(c.get('tool', '?') for c in row.get('candidates', []))
    if stage == STAGES[2]:
        metrics = row.get('metrics', {})
        keys = ('vmin', 'vmax', 'max_allowed_current_pct', 'allowed_current_utilization_pct',
                'served_kw', 'critical_served_kw', 'u_pu')
        values = [f'{key}={metrics[key]:.6g}' for key in keys if isinstance(metrics.get(key), (int, float))]
        return row.get('candidate_id', '') + ': ' + ('; '.join(values) or json.dumps(metrics, ensure_ascii=False))
    if stage == STAGES[3]:
        return row.get('candidate_id', '') + ': ' + (', '.join(row.get('failures', [])) or
              ('PASS; cost=' + format(row['score'], '.8g') if row.get('score') is not None else 'no cost'))
    reply = row.get('language_response', {})
    return str(reply.get('choice', reply.get('ranking', row.get('reason', row.get('error', '')))))


def stage_table(run):
    """Every stage event, including deterministic simulation and verification."""
    import pandas as pd
    rows = []
    for event in run['trace']:
        reply = event['response'].get('language_response', {})
        rows.append({'event': event['event'], 'stage': event['stage'], 'status': event['status'],
            'method': event['method'], 'returned_output': _short_response(event),
            'stage_seconds': event['seconds'],
            'response_source': reply.get('source', 'deterministic_numerical'),
            'model_call_seconds': reply.get('seconds', 0.) if reply.get('source') != 'deterministic' else 0.})
    return pd.DataFrame(rows)


def language_table(suite, run):
    """Exact public reason strings; no private reasoning trace is requested."""
    import pandas as pd
    rows = []
    for event, reply in _replies(run):
        call = _match_call(suite, run, reply)
        raw = call.get('raw_response', {}) if call else {}
        rows.append({'event': event['event'], 'role': event['stage'],
            'phase': event['response'].get('phase', 'planning'),
            'choice_or_ranking': reply.get('choice', reply.get('ranking')),
            'public_reason_exact': reply['reason'], 'source': reply['source'],
            'call_id': reply.get('call_id'), 'client_seconds': reply.get('seconds', 0.),
            'prompt_tokens': raw.get('prompt_eval_count'), 'generated_tokens': raw.get('eval_count'),
            'model': run.get('model')})
    return pd.DataFrame(rows)


def candidate_table(run):
    import pandas as pd
    return pd.DataFrame([{'id': row['id'], 'phase': row['phase'],
        'operation': row['candidate'].get('operation', row['candidate'].get('tool')),
        'command': json.dumps({key: value for key, value in row['candidate'].items()
                               if key not in ('operation', 'tool')}, ensure_ascii=False),
        'accepted_in_scope': not row['failures'], 'failures': ', '.join(row['failures']),
        'cost_lower_is_better': row['score']} for row in run['evaluations']])


def call_table(suite, include_portability=False):
    import pandas as pd
    rows = []
    runs = list(suite['runs'])
    if include_portability and suite.get('model_portability_example'):
        runs.append(suite['model_portability_example'])
    for run in runs:
        for event, reply in _replies(run):
            call = _match_call(suite, run, reply)
            if call is None:
                continue
            raw = call.get('raw_response', {})
            seconds = lambda field: raw[field]/1e9 if isinstance(raw.get(field), (int, float)) else None
            generation_seconds = seconds('eval_duration')
            rows.append({'case': run['case'], 'backend': run['backend'], 'model': run['model'],
                'event': event['event'], 'role': call['role'], 'call_id': call['call_id'],
                'source': call['source'], 'client_seconds': call['seconds'],
                'server_total_seconds': seconds('total_duration'),
                'server_load_seconds': seconds('load_duration'),
                'prompt_eval_seconds': seconds('prompt_eval_duration'),
                'generation_seconds': generation_seconds,
                'prompt_tokens': raw.get('prompt_eval_count'),
                'cached_prompt_tokens': raw.get('prompt_eval_cached_count'),
                'generated_tokens': raw.get('eval_count'),
                'generation_tokens_per_second': raw['eval_count']/generation_seconds
                    if generation_seconds and isinstance(raw.get('eval_count'), (int, float)) else None})
    return pd.DataFrame(rows)


def _llm_seconds(run):
    return sum(reply.get('seconds', 0.) for _, reply in _replies(run)
               if reply.get('source') != 'deterministic')


def comparison_table(suite):
    import pandas as pd
    rows = []
    for case, backend in SETTINGS:
        fixed = select_run(suite, case, backend, 'fixed')
        agent = select_run(suite, case, backend)
        score = lambda run: run['selected']['score'] if run.get('selected') else None
        fs, ags = score(fixed), score(agent)
        rows.append({'case': case, 'backend': backend, 'fixed_status': fixed['status'],
            'agent_status': agent['status'], 'fixed_cost': fs, 'agent_cost': ags,
            'agent_minus_fixed_cost': ags-fs if fs is not None and ags is not None else None,
            'same_cost_within_1e-8': abs(ags-fs) <= 1e-8 if fs is not None and ags is not None else False,
            'fixed_seconds': fixed['seconds'], 'agent_seconds': agent['seconds'],
            'agent_LLM_seconds': _llm_seconds(agent), 'agent_LLM_calls': agent['llm_calls'],
            'fixed_refinements_used': fixed['counts']['refinement'],
            'agent_refinements_used': agent['counts']['refinement'],
            'same_max_refinement_budget': fixed['refinement_budget'] == agent['refinement_budget'],
            'all_five_agent_stages_executed': all(agent['core_stage_coverage'].get(stage, False) for stage in STAGES)})
    return pd.DataFrame(rows)


def interpretation(suite):
    """Generate the outcome statement from the loaded observations, not a template claim."""
    table = comparison_table(suite)
    comparable = table.dropna(subset=['agent_minus_fixed_cost'])
    ties = int((comparable['agent_minus_fixed_cost'].abs() <= 1e-8).sum())
    worse = comparable[comparable['agent_minus_fixed_cost'] > 1e-8]
    better = comparable[comparable['agent_minus_fixed_cost'] < -1e-8]
    covered = int(table['all_five_agent_stages_executed'].sum())
    text = (f"**Recorded result:** all five modules executed in {covered}/{len(table)} agentic settings. "
            f"Among {len(comparable)} settings with a selected action on both routes, numerical cost "
            f"ties in {ties}, is lower for the agent in {len(better)}, and is higher for the agent in {len(worse)}. ")
    for _, row in worse.iterrows():
        text += (f"In {row['case']} / {row['backend']}, agent cost {row['agent_cost']:.8g} "
                 f"exceeds fixed cost {row['fixed_cost']:.8g}; inspect its chosen refinements. ")
    slower = int((table['agent_seconds'] > table['fixed_seconds']).sum())
    return text + (f"Agentic wall time is greater in {slower}/{len(table)} settings in this single recorded suite. "
                   "Complete stage execution and feasibility are distinct from better numerical performance.")


def stage_coverage_table(suite):
    import pandas as pd
    return pd.DataFrame([{'case / model': run['case'] + ' / ' + run['backend'],
        'supervisor': run['supervisor'],
        **{stage: '✓' if run['core_stage_coverage'].get(stage, False) else '—' for stage in STAGES}}
        for run in suite['runs']])


def pair_summary_table(suite, case, backend):
    import pandas as pd
    rows = []
    for route in ('fixed', 'agentic'):
        run = select_run(suite, case, backend, route)
        selected = run.get('selected')
        rows.append({'supervisor': route, 'status': run['status'],
            'selected_cost': selected['score'] if selected else None,
            'workflow_seconds': run['seconds'], 'LLM_seconds': _llm_seconds(run),
            'LLM_calls': run['llm_calls'], 'refinements_used': run['counts']['refinement'],
            'final_fresh_recheck': run['counts']['final_recheck']})
    return pd.DataFrame(rows)


def plot_comparison(suite):
    """Two matched bars per setting; historical wall time, not replay-cell time."""
    import numpy as np
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), constrained_layout=True)
    x = np.arange(len(SETTINGS))
    labels = [LABELS[case] + '\n' + backend for case, backend in SETTINGS]
    colors = {'fixed': '#88ada5', 'agentic': '#0d6658'}
    for route, offset in [('fixed', -.2), ('agentic', .2)]:
        runs = [select_run(suite, case, backend, route) for case, backend in SETTINGS]
        axes[0].bar(x+offset, [r['seconds'] for r in runs], .37, color=colors[route],
                    label='Conventional fixed' if route == 'fixed' else 'Llama supervised')
        axes[1].bar(x+offset, [r['counts']['refinement'] for r in runs], .37,
                    color=colors[route])
    axes[0].set(ylabel='Recorded workflow wall time (s)', title='Matched tools; measured duration')
    axes[0].legend(fontsize=8)
    axes[1].axhline(2, color='#ad763d', linestyle='--', linewidth=1, label='Shared maximum: 2')
    axes[1].set(ylabel='Additional candidates evaluated', ylim=(0, 2.6),
                title='Used refinement budget can differ')
    axes[1].legend(fontsize=8)
    for ax in axes:
        ax.set_xticks(x, labels, rotation=25, ha='right', fontsize=8)
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(axis='y', alpha=.2)
    fig.suptitle('One authored local run per route; no statistical or real-time guarantee', fontsize=11)
    return fig


def plot_progress(suite):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), constrained_layout=True)
    for ax, (case, backend) in zip(axes.flat, SETTINGS):
        for route, color, marker in [('fixed', '#b77934', 'o'), ('agentic', '#0d6658', 's')]:
            run = select_run(suite, case, backend, route)
            points = [p for p in run['progress'] if p.get('best_cost') is not None]
            ax.plot([p['evaluated'] for p in points], [p['best_cost'] for p in points],
                    marker=marker, color=color, label=route, linewidth=1.8, alpha=.85)
        ax.set(title=LABELS[case]+' / '+backend, xlabel='Candidate evaluation number',
               ylabel='Best feasible cost (lower is better)', xticks=range(1, 6))
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(alpha=.2)
        ax.legend(fontsize=8)
    fig.suptitle('Refinement retains the best verified action; costs have case-specific units', fontsize=12)
    return fig


def show_case(suite, case, backend, portability=False):
    """Notebook display with full public reasons and every numerical event."""
    from IPython.display import display, Markdown, HTML
    run = select_run(suite, case, backend, portability=portability)
    display(Markdown(f"### Recorded {LABELS[case]} — {backend}\n\n"
        f"**{run['status']}** · model `{run.get('model')}` · "
        f"{run['llm_calls']} model calls · workflow **{run['seconds']:.3f} s**.\n\n"
        f"Scope: {run['scope']}\n\nObjective: {run['objective']}"))
    if not portability:
        display(pair_summary_table(suite, case, backend))
    display(candidate_table(run))
    stages = stage_table(run)
    display(stages[['event', 'stage', 'status', 'returned_output', 'stage_seconds', 'response_source']])
    for row in language_table(suite, run).to_dict('records'):
        reason = html.escape(row['public_reason_exact'])
        selection = html.escape(str(row['choice_or_ranking']))
        label = html.escape(row['role']+' / '+row['phase'])
        display(HTML('<div style="border-left:4px solid #0d6658;padding:8px 14px;margin:10px 0">'
            f'<b>{label}</b> · returned <code>{selection}</code> · '
            f"{row['client_seconds']:.3f} s client time · call {row['call_id']}"
            f'<blockquote style="margin:8px 0">{reason}</blockquote></div>'))
    return run


def show_operator(run):
    """Review card only. Displaying it does not record a human acknowledgment."""
    from IPython.display import display, Markdown
    selected = run.get('selected')
    action = selected['candidate'] if selected else None
    payload = {'recommendation_id': run['recommendation_id'], 'status': run['status'],
        'selected_action': action, 'selected_metrics': selected['summary'] if selected else None,
        'scope': run['scope'], 'operator': run['operator']}
    display(Markdown('### Operator review and readback\n\n'
        'The operator reviews the proposed action, limits, rejected alternatives and remaining authority. '
        '**Acknowledgment remains pending; no equipment command is issued.**\n\n'
        '```json\n'+json.dumps(payload, indent=2, ensure_ascii=False)+'\n```'))
    return payload


def public_stage_outputs(run):
    """All actual recorded stage outputs, suitable for independent inspection."""
    return [{'event': event['event'], 'stage': event['stage'], 'method': event['method'],
             'status': event['status'], 'seconds': event['seconds'],
             'response': event['response']} for event in run['trace']]


def show_stage_outputs(run):
    """Expandable full stage records; compact reports do not replace evidence."""
    from IPython.display import display, HTML
    for event in public_stage_outputs(run):
        heading = html.escape(f"{event['event']:02d} · {event['stage']} · {event['status']} · {event['seconds']:.4f} s")
        payload = html.escape(json.dumps(event, indent=2, ensure_ascii=False))
        display(HTML(f'<details style="margin:8px 0"><summary>{heading}</summary>'
            f'<pre style="white-space:pre-wrap;overflow-wrap:anywhere">{payload}</pre></details>'))
