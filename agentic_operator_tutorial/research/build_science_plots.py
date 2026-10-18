"""Replot reported scientific-agent data; no invented uncertainty or cross-task ranking."""
from pathlib import Path
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'diagrams/_rigorous_build/pythonpackages'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'axes.labelsize':17,
 'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path','pdf.fonttype':42})
BLUE='#00629B'; CYAN='#00A8C8'; ORANGE='#B65B14'; NAVY='#003B5C'; GRAY='#738590'
records={}
def save(fig,name,caption,assumptions,refs,url,data):
    for ext in ['png','pdf','svg']:
        fig.savefig(ROOT/'images'/(name+'.'+ext),dpi=180,facecolor='white')
    plt.close(fig)
    caption=re.sub(r'\b([A-Za-z][a-z]{1,})(?=\d)',r'\1 ',caption)
    assumptions=re.sub(r'\b([A-Za-z][a-z]{1,})(?=\d)',r'\1 ',assumptions)
    if name=='expanded_science_popper':
        data['nonnull_hypotheses_per_run']=86
        data['constructed_null_cases_per_run']=86
        data['backend']='Claude-Sonnet-3.5'
        data['max_tests_per_hypothesis']=3
        caption+=' Each run uses 86 non-null and 86 constructed-null cases; Claude-Sonnet-3.5, at most three tests per hypothesis. Repeated runs do not create 430 independent hypotheses.'
    records[name]={'file':name+'.png','pdf':name+'.pdf','svg':name+'.svg','title':name,
     'caption':caption,'assumptions':assumptions,'source_refs':refs,'source_url':url,
     'credit':'Original plot of author-reported paper data; full protocol and limitations in the reading guide', 'data':data}
def axis(ax):
    ax.grid(axis='x',color='#D9E3E9',lw=.7); ax.set_axisbelow(True)
    ax.set_xlim(0,105); ax.xaxis.set_major_formatter(mtick.PercentFormatter(100,decimals=0))

fig,ax=plt.subplots(figsize=(10.2,4.6),layout='constrained')
for y,baseline,tools in [(1,56.7,78.3),(0,94.3,99.5)]:
    ax.plot([baseline,tools],[y,y],lw=4,color=CYAN)
    ax.scatter([baseline,tools],[y,y],s=135,color=[GRAY,BLUE],zorder=3)
    ax.text(baseline,y-.19,f'{baseline:.1f}',ha='center',color=GRAY,fontweight='bold')
    ax.text(tools,y+.17,f'{tools:.1f}',ha='center',color=BLUE,fontweight='bold')
ax.set(yticks=[1,0],yticklabels=['DbQA\n60 questions','SeqQA\n70 questions'],ylim=(-.5,1.55),xlabel='Reported task accuracy (%)')
axis(ax)
ax.scatter([],[],color=GRAY,s=100,label='Claude Code without ToolUniverse')
ax.scatter([],[],color=BLUE,s=100,label='Same agent with ToolUniverse')
ax.legend(frameon=False,loc='upper left',bbox_to_anchor=(0,1.04),fontsize=12)
save(fig,'expanded_science_tooluniverse','ToolUniverse v3 supplementary S8, Figure S2, PDF pp.23–24. Matched Claude Code / Claude Opus 4.8 point estimates on 60 DbQA and70 SeqQA questions. Same agent/base model with and without ToolUniverse. Refusals and unparsable answers count as incorrect. Values are reported percentages; do not reconstruct integer successes from them.','Point estimates only for this comparison; no sampling interval supplied. Biomedical tasks, not grid engineering. The overall platform effect does not isolate each module.',['H02'],'https://arxiv.org/pdf/2509.23426v3',{'DbQA':{'n':60,'without':56.7,'with':78.3},'SeqQA':{'n':70,'without':94.3,'with':99.5}})

fig,ax=plt.subplots(figsize=(10.2,4.6),layout='constrained')
labels=['Llama 3.1 70B','GPT-4o','TxAgent 8B']; vals=[52.8,66.3,92.1]
ax.barh([2,1,0],vals,color=[GRAY,CYAN,BLUE],height=.49)
for y,v in zip([2,1,0],vals):ax.text(v+1.3,y,f'{v:.1f}%',va='center',fontweight='bold',color=NAVY)
ax.set(yticks=[2,1,0],yticklabels=labels,xlabel='Open-ended DrugPC accuracy (%)');axis(ax)
save(fig,'expanded_science_txagent','TxAgent v1 Results, PDF p.10, Figure1d. Open-ended DrugPC accuracy; DrugPC has3,168 questions. TxAgent is fine-tuned Llama3.1-8B plus ToolRAG and211 tools; comparison models differ in training and tool access. Methods5.2, PDF p.61: answers generated without choices are mapped back to the original multiple-choice options for scoring.','A system comparison, not a same-model tool ablation or direct free-text semantic grading. Rounded author percentages; no reconstructed success counts or uncertainty. Benchmark answers, not prospective clinical outcomes.',['H06'],'https://arxiv.org/pdf/2503.10970v1',{'n_questions':3168,'metric':'open-ended accuracy percent','models':dict(zip(labels,vals))})

fig,ax=plt.subplots(figsize=(10.2,4.6),layout='constrained')
labels=['Llama 3.1 8B\nmimics tools','GPT-4o\nmimics tools','Actual\nToolUniverse tools'];vals=[68.7,72.7,93.8]
ax.barh([2,1,0],vals,color=[GRAY,CYAN,BLUE],height=.49)
for y,v in zip([2,1,0],vals):ax.text(v+1.2,y,f'{v:.1f}%',va='center',fontweight='bold',color=NAVY)
ax.set(yticks=[2,1,0],yticklabels=labels,xlabel='Multiple-choice DrugPC accuracy (%)');axis(ax)
save(fig,'expanded_science_txagent_ablation','TxAgent v1 Results p.17; Figure3c graphic/caption pp.27–28; Online Methods6.1 pp.61–62. ToolUniverse services are replaced by LLMs prompted to mimic tool behavior. DrugPC is multiple-choice here: actual tools93.8%, GPT-4o mimic72.7%, Llama3.1-8B mimic68.7%.','Different output setting from the92.1% open-ended score; do not combine them. Source reports other settings held unchanged; no uncertainty interval supplied. Demonstrates this benchmark comparison, not correctness of all external tools.',['H06'],'https://arxiv.org/pdf/2503.10970v1',{'n_questions':3168,'metric':'multiple-choice accuracy percent','conditions':dict(zip(labels,vals))})

fig,axs=plt.subplots(1,2,figsize=(10.8,4.7),layout='constrained',sharey=True)
names=['ReAct','POPPER without\nrelevance check','POPPER']; ys=np.array([2,1,0]); colors=[GRAY,ORANGE,BLUE]
for ax,vals,sds,title in [(axs[0],[7.8,13.4,10.3],[6.1,2.1,2.0],'Type-I error (%)'),(axs[1],[38.3,61.0,63.8],[1.7,4.2,6.6],'Power (%)')]:
    for y,v,sd,c in zip(ys,vals,sds,colors):
        ax.errorbar(v,y,xerr=sd,fmt='o',color=c,capsize=5,ms=9,lw=2)
        ax.text(v,y+.21,f'{v:.1f} ± {sd:.1f}',color=c,ha='center',fontsize=20,fontweight='bold')
    ax.set_xlabel(title);ax.grid(axis='x',color='#D9E3E9');ax.set_axisbelow(True)
axs[0].set(yticks=ys,yticklabels=names,xlim=(0,22),ylim=(-.5,2.65))
axs[0].axvline(10,color=NAVY,ls='--',lw=1.3)
axs[0].text(10.6,2.5,'α =10%',fontsize=16,color=NAVY)
axs[1].set_xlim(0,85)
save(fig,'expanded_science_popper','POPPER ICML2025 Table3, PDF p.6: DiscoveryBench comparison, mean ± standard deviation across5 independent runs, nominal alpha0.1. ReAct Type-I error0.078±0.061/power0.383±0.017; no relevance check0.134±0.021/0.610±0.042; POPPER0.103±0.020/0.638±0.066. Values multiplied by100 for percent axes.','Whiskers are standard deviations, not95% confidence intervals. Power is rejection probability on non-null hypotheses; Type-I error is rejection on nulls. The observed POPPER mean slightly exceeds nominalalpha; theoretical control requires its assumptions. Appendix protocol constructs null tests via data permutations.',['H09','H10'],'https://cs.stanford.edu/~jure/pubs/auto-hypothesis-validation-icml25.pdf',{'runs':5,'alpha':.1,'methods':{'ReAct':{'type1':.078,'type1_sd':.061,'power':.383,'power_sd':.017},'POPPER-NoReleCheck':{'type1':.134,'type1_sd':.021,'power':.610,'power_sd':.042},'POPPER':{'type1':.103,'type1_sd':.020,'power':.638,'power_sd':.066}}})

fig,ax=plt.subplots(figsize=(10.2,4.7),layout='constrained')
names=['p-value context error','Ineffective test','Broken logical implication','Implementation error','Relevant data not found'];v=[35.9,28.1,17.2,8.6,7.0]
ax.barh(range(4,-1,-1),v,color=[BLUE,CYAN,ORANGE,GRAY,GRAY],height=.5)
for y,val in zip(range(4,-1,-1),v):ax.text(val+.7,y,f'{val:.1f}%',va='center',fontweight='bold',color=NAVY)
ax.set(yticks=range(4,-1,-1),yticklabels=names,xlim=(0,43),xlabel='Fraction of128 failed experiment logs with this label (%)')
ax.grid(axis='x',color='#D9E3E9');ax.set_axisbelow(True)
save(fig,'expanded_science_popper_failures','POPPER AppendixD, PDF p.15, Figure5: selected failure labels among128 failed experiment logs. Multiple labels may occur per log. Labels generated by o1;30 labeled logs manually checked with93.3% agreement.','Conditional sample of failed logs, not all attempts; percentages are not unconditional system failure probabilities and need not sum to100. Shown five categories, not full taxonomy.',['H10'],'https://cs.stanford.edu/~jure/pubs/auto-hypothesis-validation-icml25.pdf',{'failed_logs':128,'labels_percent':dict(zip(names,v)),'multiple_labels':True})

(ROOT/'images/expanded_science_statistics.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print('Wrote',len(records),'science plots')
