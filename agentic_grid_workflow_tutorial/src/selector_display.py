"""Read-only teaching views for the separate multi-LLM voltage pilot."""
from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'results/ensemble_voltage_pilot'


def read(relative, root=DATA):
    return json.loads((Path(root)/relative).read_text(encoding='utf-8'))


def scenario_table():
    protocol = read('protocol.json')
    rows = []
    for s in protocol['scenarios']:
        c = s['case']
        rows.append({'scenario': s['id'], 'split': s['split'],
                     'load forecast': c['forecast_loads'],
                     'rating fraction': c['rating_fraction'],
                     'previous a,b': c['previous']})
    return pd.DataFrame(rows)


def initial_candidates(context_id='test_01', backend='lindistflow3'):
    root = DATA if backend == 'lindistflow3' else DATA/'ac_transfer'
    context = next(c for c in read('contexts.json', root) if c['id'] == context_id)
    rows = []
    for c in context['initial_evaluations']:
        rows.append({'method': c['candidate']['operation'], 'a': c['candidate']['control'][0],
                     'b': c['candidate']['control'][1], 'model PASS': c['feasible'],
                     'current-step J': c['score'], 'failures': ', '.join(c['failures']) or 'none',
                     'chosen incumbent': c['candidate_hash'] == context['incumbent']['candidate_hash']})
    return pd.DataFrame(rows)


def response_table(context_id='test_01', backend='lindistflow3'):
    root = DATA if backend == 'lindistflow3' else DATA/'ac_transfer'
    return pd.DataFrame([{'model': r['model_id'], 'operation': r['operation_id'],
                         'public reason (verbatim)': r['reason'], 'actual call seconds': r['seconds'],
                         'source': r['source']}
                        for r in read('responses.json', root) if r['context_id'] == context_id])


def canonical_pool(context_id='test_01', backend='lindistflow3'):
    from .response_selector import canonicalize_responses
    root = DATA if backend == 'lindistflow3' else DATA/'ac_transfer'
    context = next(c for c in read('contexts.json', root) if c['id'] == context_id)
    responses = [{k:r[k] for k in ('model_id','operation_id','reason')}
                 for r in read('responses.json', root) if r['context_id'] == context_id]
    return canonicalize_responses(responses, context['catalog'])


def latency_table():
    rows = []
    for backend, root in [('MV LinDistFlow', DATA), ('OpenDSS transfer', DATA/'ac_transfer')]:
        for r in read('responses.json', root):
            rows.append({'backend': backend, 'model': r['model_id'],
                         'split': r['split'], 'seconds': r['seconds'],
                         'case': r['context_id'], 'valid response': r['source']=='actual_local_llm'})
    return pd.DataFrame(rows)


def plot_latency():
    df = latency_table()
    fig, ax = plt.subplots(figsize=(8.8,3.6), constrained_layout=True)
    groups = list(df.groupby(['backend','model'], sort=False))
    labels = [b.replace(' transfer','')+'\n'+m.replace(':','\n') for (b,m),_ in groups]
    ax.boxplot([g['seconds'].to_numpy() for _,g in groups], tick_labels=labels, showmeans=True)
    ax.set_ylabel('Actual local model call (seconds)')
    ax.set_title('Recorded inference latency; calls were batched by model')
    ax.grid(axis='y', alpha=.2)
    ax.tick_params(axis='x', labelsize=8)
    return fig


def model_comparison():
    rows = []
    for row in read('heldout_model_comparison.json'):
        context_id = row['context_id']
        ac = row['opendss_mpc']
        mv = row['lindistflow_incumbent']
        audit = next(a for a in read('initial_model_audits.json')
                     if a['context_id']==context_id and a['initial_method']==mv['candidate']['operation'])
        rows.append({'scenario':context_id, 'MV incumbent a':mv['candidate']['control'][0],
            'MV model PASS':mv['feasible'], 'same action AC PASS':audit['opendss']['feasible'],
            'AC MPC a':ac['candidate']['control'][0] if ac else None,
            'AC MPC PASS':ac['feasible'] if ac else False,
            'AC MPC solve seconds':row['opendss_mpc_seconds']})
    return pd.DataFrame(rows)


def plot_model_comparison():
    df = model_comparison()
    fig, ax = plt.subplots(figsize=(8.8,3.7), constrained_layout=True)
    x = range(len(df))
    ax.plot(x, df['MV incumbent a'], 'o-', color='#006b47', label='MV LinDistFlow incumbent')
    ax.plot(x, df['AC MPC a'], 's-', color='#b26b19', label='Full-feeder OpenDSS MPC')
    ax.set_xticks(list(x), df['scenario'], rotation=35, ha='right', fontsize=8)
    ax.set_ylabel('Common fleet active fraction a')
    ax.set_title('Same test cases; different constraint coverage')
    ax.grid(alpha=.2); ax.legend(loc='best', fontsize=9)
    return fig


def method_label(method):
    labels = {'learned_selector':'Learned selector', 'majority_vote':'Majority vote',
              'uniform_response':'Uniform (primary seed)', 'fixed_numerical':'Fixed numerical',
              'mpc_only':'MPC first action', 'raw_sac':'Raw SAC',
              'best_of_all_responses_extra_budget':'All responses (extra trials)'}
    return labels.get(method, method.replace('fixed_pool_response:','Pool: ').replace('fixed_model:','Pool: '))


def plot_selection_results(analysis):
    wanted = ['mpc_only','fixed_numerical','majority_vote','uniform_response','learned_selector',
              'best_of_all_responses_extra_budget']
    summary = {r['method']:r for r in analysis['test']['summaries']}
    rows = [summary[k] for k in wanted if k in summary]
    fig, axes = plt.subplots(1,2,figsize=(10.2,3.7),constrained_layout=True)
    names = [method_label(r['method']) for r in rows]
    gains = [1000*r['mean_objective_improvement_on_model_passes'] for r in rows]
    axes[0].barh(names,gains,color=['#637970' if r['method']!='learned_selector' else '#006b47' for r in rows])
    axes[0].invert_yaxis(); axes[0].set_xlabel('Mean current-step objective reduction (× 0.001)')
    axes[0].set_title('12 held-out MV contexts')
    pairs = analysis['paired_test_comparison']
    values = [1000*p['learned_minus_baseline_objective'] for p in pairs]
    bounds = [p['illustrative_bootstrap_95pct_interval'] for p in pairs]
    y = list(range(len(pairs)))
    axes[1].errorbar(values,y,xerr=[[v-1000*b[0] for v,b in zip(values,bounds)],
                                  [1000*b[1]-v for v,b in zip(values,bounds)]],
                    fmt='o',color='#006b47',capsize=4)
    axes[1].set_yticks(y,[method_label(p['comparator']) for p in pairs])
    axes[1].invert_yaxis(); axes[1].axvline(0,color='#555',linestyle='--',linewidth=1)
    axes[1].set_xlabel('Learned minus baseline objective (× 0.001)\nNegative favors learned selection')
    axes[1].set_title('Paired means and illustrative 95% intervals')
    for ax in axes: ax.grid(axis='x',alpha=.2); ax.tick_params(labelsize=8)
    return fig


def operator_record(analysis, context_id='test_01', backend='opendss'):
    experiment = analysis['test'] if backend=='lindistflow3' else analysis['ac_transfer']
    row = next(r for r in experiment['rows'] if r['method']=='learned_selector' and r['context_id']==context_id)
    ready = row['final_model_feasible'] and row['final_ac_feasible']
    return {'scenario':context_id,'planning model':backend,
            'selected refinement':row['operation_id'], 'recommended a,b':row['final_control'],
            'model gate PASS':row['final_model_feasible'], 'full-feeder AC PASS':row['final_ac_feasible'],
            'operator status':'READY_FOR_HUMAN_REVIEW' if ready else 'HOLD_FOR_FULL_FEEDER_REVIEW',
            'current-step objective':row['final_score'],
            'candidate identity':row['final_candidate_hash'],
            'evidence identity':row['final_evidence_hash'],
            'unresolved checks':', '.join(row['final_ac_failures']) or 'none within stated checks',
            'human acknowledged':False,'equipment dispatch':False,
            'timing':'Recorded components replayed; no live end-to-end latency claim'}


def fixed_rule_diagnostic():
    """Post-hoc descriptive audit of every predeclared fixed operation.

    This is not a newly tuned comparator or an extra training/evaluation split.
    It tests whether a selected action pattern itself requires LLM generation.
    """
    rows=[]
    for backend,root in [('lindistflow3',DATA),('opendss',DATA/'ac_transfer')]:
        checks=[r for r in read('final_rechecks.json',root) if r['context_id'].startswith('test_')]
        for operation in sorted({r['operation_id'] for r in checks}):
            chosen=[r for r in checks if r['operation_id']==operation]
            scores=[r['score'] for r in chosen if r['feasible']]
            rows.append({'backend':backend,'fixed operation':operation,'contexts':len(chosen),
                'final model passes':sum(r['feasible'] for r in chosen),
                'mean J on passes':sum(scores)/len(scores) if scores else None,
                'LLM calls required':0,'status':'Post-hoc diagnostic; every permitted rule shown'})
    return pd.DataFrame(rows)


def uniform_sensitivity(analysis):
    """Replay the five uniform seeds fixed in the original analysis protocol."""
    import numpy as np
    rows=[]
    for backend,root in [('lindistflow3',DATA),('opendss',DATA/'ac_transfer')]:
        contexts=[c for c in read('contexts.json',root) if c['split']=='test' and c['status']=='READY']
        checks={(r['context_id'],r['operation_id']):r for r in read('final_rechecks.json',root)}
        for seed in analysis['protocol']['uniform_sensitivity_seeds']:
            rng=np.random.default_rng(seed)
            costs=[];rejected=0
            for context in contexts:
                pool=canonical_pool(context['id'],backend)['candidates']
                candidate=pool[int(rng.integers(len(pool)))]
                operation=candidate['operation_ids'][0]
                trial=read(f"counterfactuals/{context['id']}_{operation}.json",root)['planning_model_trial']
                final=checks[(context['id'],operation)]
                rejected+=not trial['feasible']
                if final['feasible']:costs.append(final['score'])
            rows.append({'backend':backend,'uniform seed':seed,'test contexts':len(contexts),
                         'final model passes':len(costs),'rejected trials':rejected,
                         'mean J on passes':sum(costs)/len(costs) if costs else None})
    return pd.DataFrame(rows)


def stage_outputs(analysis, context_id='test_01', backend='opendss'):
    root = DATA if backend=='lindistflow3' else DATA/'ac_transfer'
    context = next(c for c in read('contexts.json',root) if c['id']==context_id)
    experiment = analysis['test'] if backend=='lindistflow3' else analysis['ac_transfer']
    row = next(r for r in experiment['rows'] if r['method']=='learned_selector' and r['context_id']==context_id)
    final = next(r for r in read('final_rechecks.json',root)
                 if r['context_id']==context_id and r['operation_id']==row['operation_id'])
    return pd.DataFrame([
        {'stage':'Awareness','method':'Frozen scenario and scope',
         'returned output':f"Forecast {context['case']['forecast_loads']}; rating fraction {context['case']['rating_fraction']:.4f}"},
        {'stage':'Planning','method':'H=3 MPC + frozen SAC',
         'returned output':'; '.join(f"{r['candidate']['operation']}: {r['candidate']['control']}" for r in context['initial_evaluations'])},
        {'stage':'Simulation','method':f'Fresh {backend} final solve',
         'returned output':str(final['summary'])},
        {'stage':'Verification','method':'Numerical limits and exact candidate binding',
         'returned output':f"Final model PASS={row['final_model_feasible']}; full-feeder AC PASS={row['final_ac_feasible']}"},
        {'stage':'LLM Optimizer','method':'Actual three-model pool + frozen LinUCB',
         'returned output':f"Trial {row['operation_id']}; {row.get('selected_votes',0)} votes; objective gain {row['objective_improvement']:.8f}"}
    ])
