"""Descriptive paired scoring and figures; not an inference-time decision tool."""
import json
from pathlib import Path
import numpy as np
from .control_tools import ROOT

METHODS=['rule_parser','llama_once','llama_critic','llama_self_review','structured_reference']
LABELS={'rule_parser':'Conventional parser','llama_once':'Llama: one pass',
        'llama_critic':'Llama + critic','llama_self_review':'Llama + self-review',
        'structured_reference':'Correct structured inputs'}

def report():
    study=json.loads((ROOT/'results/request_study.json').read_text())
    calls=json.loads((ROOT/'results/request_calls.json').read_text())
    fixtures=json.loads((ROOT/'data/operator_requests.json').read_text())
    expected_ids={f['id'] for f in fixtures}
    if {r['id'] for r in study['rows']}!=expected_ids or len(calls)!=3*len(fixtures):
        raise RuntimeError('The request study is incomplete; do not report interim denominators as final results.')
    call_errors={}
    for i,f in enumerate(fixtures):
        call_errors[f['id']]={'llama_once':bool(calls[3*i].get('error')),
                             'llama_critic':bool(calls[3*i+1].get('error')),
                             'llama_self_review':bool(calls[3*i+2].get('error'))}
    summary=[]
    for method in METHODS:
        rows=[r for r in study['rows'] if r['method']==method]
        valid=[r for r in rows if r['group']!='clarification']
        unclear=[r for r in rows if r['group']=='clarification']
        clean_clarification=sum(r['correct_clarification'] and not call_errors[r['id']].get(method,False) for r in unclear)
        summary.append({'method':method,'label':LABELS[method],'clear_requests':len(valid),
            'correct_automatic_completions':sum(r['correct_automatic_completion'] for r in valid),
            'exact_interpretations':sum(r['exact_interpretation'] for r in valid),
            'incorrect_ready_interpretations':sum(r['incorrect_ready_interpretation'] for r in rows),
            'unnecessary_handoffs':sum(r['unnecessary_handoff'] for r in valid),
            'clarification_cases':len(unclear),'correct_semantic_clarifications':clean_clarification,
            'final_response_service_or_schema_errors':sum(call_errors[r['id']].get(method,False) for r in rows),
            'canonical_completions':sum(r['correct_automatic_completion'] for r in valid if r['group']=='canonical'),
            'paraphrase_completions':sum(r['correct_automatic_completion'] for r in valid if r['group']=='paraphrase'),
            'median_machine_seconds':float(np.median([r['machine_seconds'] for r in rows])),
            'machine_seconds_total':sum(r['machine_seconds'] for r in rows),
            'outside_gold_limits':sum(r['offline_gold_gate'] is not None and not r['offline_gold_gate']['accepted'] for r in rows)})
    by_key={(r['id'],r['method']):r for r in study['rows']}
    def semantically_correct(r):
        if call_errors[r['id']].get(r['method'],False):return False
        return r['correct_clarification'] if r['group']=='clarification' else r['exact_interpretation']
    paired=[]
    for method in ['llama_critic','llama_self_review']:
        corrections=[];regressions=[]
        for f in fixtures:
            before=semantically_correct(by_key[f['id'],'llama_once'])
            after=semantically_correct(by_key[f['id'],method])
            if after and not before:corrections.append(f['id'])
            if before and not after:regressions.append(f['id'])
        paired.append({'method':method,'corrections':corrections,'regressions':regressions})
    recovery=json.loads((ROOT/'results/recovery.json').read_text())
    result={'summary':summary,'paired_reviews':paired,
            'total_actual_request_llm_calls':len(calls),'unique_model_service_schema_errors':sum(bool(c.get('error')) for c in calls),
            'recovery_summary':recovery['summary'],
            'scoring_note':'Correct completion requires exact requested restrictions and fresh verification under the offline gold constraints. Model errors are handoffs, not successful semantic clarification. Structured-input reference excludes unmeasured human translation time.',
            'timing_note':'Descriptive timings from one local session; fixed evaluation order and model caching. Initial Llama output is shared across the paired critic/self-review comparisons.'}
    confirmation=json.loads((ROOT/'results/confirmation.json').read_text())
    if not confirmation['metadata']['complete']:raise RuntimeError('Confirmation study incomplete')
    result['confirmation']=[]
    for method in ['rule_parser','hybrid']:
        rows=[r for r in confirmation['rows'] if r['method']==method]
        result['confirmation'].append({'method':method,'clear_requests':8,
            'correct_automatic_completions':sum(r['correct_automatic_completion'] for r in rows),
            'incorrect_ready_interpretations':sum(r['incorrect_ready_interpretation'] for r in rows),
            'clear_request_errors':sum(r['incorrect_ready_interpretation'] for r in rows if r['group']!='clarification'),
            'outside_gold_requested_limits':sum(r['offline_gold_gate'] is not None and not r['offline_gold_gate']['accepted'] for r in rows),
            'unnecessary_handoffs':sum(r['unnecessary_handoff'] for r in rows),
            'clarification_cases':4,'correct_semantic_clarifications':sum(r['correct_semantic_clarification'] for r in rows),
            'model_calls':sum(r['llm_calls'] for r in rows),
            'median_machine_seconds':float(np.median([r['machine_seconds'] for r in rows]))})
    # This policy was selected after seeing the pilot. Keep that fact explicit.
    selected=[]
    for f in fixtures:
        parser=by_key[f['id'],'rule_parser']
        selected.append(parser if parser['interpretation']['status']=='READY' else by_key[f['id'],'llama_once'])
    result['exploratory_hybrid_pilot']={'label':'Post-hoc exploratory policy, not a prespecified pilot arm',
        'correct_automatic_completions':sum(r['correct_automatic_completion'] for r in selected),
        'incorrect_ready_interpretations':sum(r['incorrect_ready_interpretation'] for r in selected)}
    (ROOT/'results/advantage_summary.json').write_text(json.dumps(result,indent=2))
    return result

def plots():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from .plots import finish,TEAL,INK,ORANGE,RED
    summary=report()
    rows=summary['summary'][:4]
    labels=['Rule parser','Llama\none pass','Llama +\ncritic','Llama +\nself-review']
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(12,4.6))
    for ax,key,title,n in [(axes[0],'canonical_completions','Standard wording',5),(axes[1],'paraphrase_completions','Varied wording',15)]:
        counts=[r[key] for r in rows]
        ax.bar(np.arange(4),counts,color=[INK,TEAL,TEAL,TEAL])
        ax.axhline(n,color=ORANGE,ls='--',label=f'Correct structured input: {n}/{n}')
        ax.set_xticks(range(4),labels);ax.set_ylim(0,n+2);ax.set_yticks(range(0,n+1,1 if n==5 else 3))
        ax.set(ylabel='Correct automatic recommendations',title=title)
        for i,c in enumerate(counts):ax.text(i,c+.15,f'{c}/{n}',ha='center',fontweight='bold')
        ax.legend(fontsize=9,loc='lower right')
    fig.suptitle('Same control tools and OpenDSS gate; only request interpretation changes',fontsize=13)
    fig.tight_layout();finish(fig,'language_advantage')
    fig,axes=plt.subplots(1,2,figsize=(12,4.4))
    x=np.arange(4)
    axes[0].bar(x,[r['unnecessary_handoffs'] for r in rows],color=ORANGE,label='Handoff on clear requests')
    axes[0].bar(x,[r['incorrect_ready_interpretations'] for r in rows],bottom=[r['unnecessary_handoffs'] for r in rows],color=RED,label='Wrong automatic interpretation')
    axes[0].set(ylabel='Requests',title='Automation has to remain semantically correct',ylim=(0,21))
    axes[0].legend(fontsize=9)
    axes[1].bar(x,[r['median_machine_seconds'] for r in rows],color=[INK,TEAL,TEAL,TEAL])
    axes[1].set(ylabel='Median machine time (seconds)',title='More model calls cost time')
    for ax in axes:ax.set_xticks(x,labels)
    fig.text(.10,.005,'Clear-request handoffs use denominator 20; wrong interpretations use all 24. Human handling time was not measured.',fontsize=9)
    fig.tight_layout(rect=[0,.04,1,1]);finish(fig,'language_cost')
    rec=recovery_rows=json.loads((ROOT/'results/recovery.json').read_text())['runs']
    methods=['single_pass','adaptive_rules','agent_loop'];labels=['Single pass','Adaptive rules','Agent feedback loop']
    successes=[sum(r['verified_completion'] for r in rec if r['method']==m) for m in methods]
    fig,axes=plt.subplots(1,2,figsize=(11,4.1))
    axes[0].bar(range(3),successes,color=[ORANGE,INK,TEAL]);axes[0].set(ylim=(0,3.6),yticks=range(4),ylabel='Verified completions / 3',title='A feedback loop recovers from failure')
    for i,n in enumerate(successes):axes[0].text(i,n+.1,f'{n}/3',ha='center',fontweight='bold')
    axes[1].bar(range(3),[sum(r['seconds'] for r in rec if r['method']==m) for m in methods],color=[ORANGE,INK,TEAL]);axes[1].set(ylabel='Total machine time (seconds)',title='Known failures also admit simple rules')
    for ax in axes:ax.set_xticks(range(3),labels)
    fig.tight_layout();finish(fig,'recovery_advantage')
    confirm=summary['confirmation'];fig,axes=plt.subplots(1,2,figsize=(11,4.2))
    axes[0].bar([0,1],[r['correct_automatic_completions'] for r in confirm],color=[INK,TEAL])
    axes[0].set(ylim=(0,9),yticks=range(0,9,2),ylabel='Correct automatic recommendations / 8',title='New clear requests: additional coverage')
    axes[0].axhline(8,color=ORANGE,ls='--')
    for i,r in enumerate(confirm):axes[0].text(i,r['correct_automatic_completions']+.1,f"{r['correct_automatic_completions']}/8",ha='center',fontweight='bold')
    axes[1].bar([0,1],[r['correct_semantic_clarifications'] for r in confirm],color=[INK,TEAL])
    axes[1].set(ylim=(0,4.6),yticks=range(5),ylabel='Correct clarifications / 4',title='Ambiguous/unsupported requests: remaining risk')
    for i,r in enumerate(confirm):axes[1].text(i,r['correct_semantic_clarifications']+.08,f"{r['correct_semantic_clarifications']}/4",ha='center',fontweight='bold')
    for ax in axes:ax.set_xticks([0,1],['Conventional parser','Parser + selective Llama'])
    fig.text(.10,.005,'Both methods also misinterpreted one clear request. The hybrid added one wrong READY on an unsupported request.',fontsize=9)
    fig.tight_layout(rect=[0,.04,1,1]);finish(fig,'hybrid_confirmation')
    return summary

if __name__=='__main__':
    print(json.dumps(plots(),indent=2))
