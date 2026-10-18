"""Scientific plots reconstructed from the saved experimental records."""
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Patch
from .framework import ROOT,SCENARIOS,dispatch,Action

TEAL='#007F83';ORANGE='#C86B35';INK='#18384B'
LABELS={'random':'Random','rule_search':'Rule search','single_llm':'Single Llama','no_critic':'No critic','multi_agent':'Multi-agent'}
def load(name):return json.loads((ROOT/'results'/name).read_text())
def save(fig,name):
 fig.tight_layout();(ROOT/'figures').mkdir(exist_ok=True)
 for ext in ['png','svg']:fig.savefig(ROOT/'figures'/f'{name}.{ext}',dpi=170,bbox_inches='tight')
 return fig

def all_plots():
 plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':INK,'axes.titleweight':'bold','figure.facecolor':'white'})
 ref=load('reference.json');runs=load('benchmark.json');attacks=load('attacks.json');figs={}
 before=dispatch(SCENARIOS[0],Action('baseline',100),True)
 best=dispatch(SCENARIOS[0],Action('ref',ref['V1']['best']['metrics']['pv_cap']),True)
 coords={}
 for line in (ROOT/'data/greensboro_udt8894/Buscoords.dss').read_text().splitlines():
  p=line.replace(',',' ').split()
  if len(p)==3:coords[p[0].lower()]=tuple(map(float,p[1:]))
 fig,ax=plt.subplots(figsize=(10,6))
 segments=[[coords[a],coords[b]] for _,a,b in before['line_endpoints'] if a in coords and b in coords]
 ax.add_collection(LineCollection(segments,colors='#A8B8BE',linewidths=.65))
 pts=[(coords[r['bus']],r['vmax']) for r in before['buses'] if r['bus'] in coords]
 dots=ax.scatter([p[0][0] for p in pts],[p[0][1] for p in pts],c=[p[1] for p in pts],s=9,cmap='viridis',vmin=.99,vmax=1.11)
 ax.autoscale();ax.set_aspect(1/np.cos(np.deg2rad(36.1)));fig.colorbar(dots,ax=ax,label='Maximum phase voltage (pu)')
 ax.set(xlabel='Longitude',ylabel='Latitude',title='One synthetic Greensboro feeder: udt8894')
 figs['01_feeder_map']=save(fig,'01_feeder_map')
 fig,axs=plt.subplots(1,2,figsize=(12,4.5))
 for m,label,c in [(before,'No action',ORANGE),(best,'Catalog reference',TEAL)]:
  v=np.sort([r['vmax'] for r in m['buses']]);axs[0].plot(np.linspace(0,100,len(v)),v,label=label,color=c)
  l=sorted([r['loading_pct'] for r in m['lines'] if r['loading_pct'] is not None],reverse=True)[:25]
  axs[1].plot(range(1,len(l)+1),l,label=label,color=c)
 axs[0].axhline(1.05,color='gray',ls='--');axs[1].axhline(100,color='gray',ls='--')
 axs[0].set(xlabel='Bus percentile (%)',ylabel='Maximum phase voltage (pu)',title='Voltage distribution')
 axs[1].set(xlabel='Line rank by loading',ylabel='Normal rating (%)',title='25 most loaded lines')
 for ax in axs:ax.legend()
 figs['02_voltage_before_after']=save(fig,'02_voltage_before_after')
 fig,axs=plt.subplots(1,2,figsize=(12,4.5))
 for sid,ax in zip(['V1','V2'],axs):
  rows=ref[sid]['candidates'];x=[r['metrics']['pv_cap'] for r in rows];y=[r['metrics']['pv_kw']/1000 for r in rows]
  ax.plot(x,y,color='#B3BFC5')
  for passed,color,label in [(True,TEAL,'Verified'),(False,ORANGE,'Rejected')]:
   ix=[i for i,r in enumerate(rows) if r['verified']==passed];ax.scatter(np.array(x)[ix],np.array(y)[ix],color=color,label=label,s=70,zorder=3)
  ax.set(xlabel='PV cap (% of Pmpp)',ylabel='Actual snapshot PV (MW)',title=sid+' finite action space');ax.legend()
 figs['03_voltage_tradeoff']=save(fig,'03_voltage_tradeoff')
 fig,axs=plt.subplots(1,2,figsize=(12,4.5))
 for sid,ax in zip(['R1','R2'],axs):
  rr=[r for r in ref[sid]['candidates'] if r['metrics'] and r['action_id'] in ['hold','short_all','long_all','short_shed_50','short_shed_65','short_shed_75','short_shed_90']]
  x=np.arange(len(rr));m=[r['metrics'] for r in rr]
  ax.bar(x,[q['served_kw']/1000 for q in m],color=[TEAL if r['verified'] else ORANGE for r in rr])
  ax.scatter(x,[q['critical_served_kw']/1000 for q in m],marker='D',color=INK,label='Critical service')
  ax.set_xticks(x,[r['action_id'].replace('short_','') for r in rr],rotation=35,ha='right');ax.set(ylabel='Nominal load (MW)',title=sid+' restoration')
  handles,labels=ax.get_legend_handles_labels();ax.legend(handles+[Patch(color=TEAL,label='Verified'),Patch(color=ORANGE,label='Rejected')],labels+['Verified','Rejected'],fontsize=9)
 figs['04_restoration_service']=save(fig,'04_restoration_service')
 fig,ax=plt.subplots(figsize=(9,4.5));rr=[r for r in ref['R2']['candidates'] if r['metrics'] and r['action_id'].startswith('short')]
 ax.plot([100*r['metrics']['shed_fraction'] for r in rr],[r['metrics']['tie_loading_pct'] for r in rr],'-o',color=TEAL)
 ax.axhline(100,ls='--',color=ORANGE,label='100 A normal rating')
 ax.set(xlabel='Noncritical load objects disconnected (%)',ylabel='Short-tie loading (% of rating)',title='R2: shedding quantity is not the same as shed power');ax.legend()
 figs['05_restoration_capacity']=save(fig,'05_restoration_capacity')
 methods=list(LABELS);fig,axs=plt.subplots(1,2,figsize=(12,5))
 df=pd.DataFrame(runs)
 success=df.groupby('method').success.mean().reindex(methods)*100
 axs[0].bar(range(5),success,color=TEAL);axs[0].set_ylim(0,112);axs[0].set(ylabel='Runs with a verified solution (%)',title='Eight runs per method')
 latency=df.groupby('method').elapsed_s.mean().reindex(methods)
 axs[1].bar(range(5),latency,color=ORANGE);axs[1].set(ylabel='Mean end-to-end seconds',title='Critic calls have a measurable cost')
 for ax in axs:ax.set_xticks(range(5),[LABELS[m] for m in methods],rotation=25,ha='right')
 figs['06_success_and_cost']=save(fig,'06_success_and_cost')
 fig,axs=plt.subplots(2,2,figsize=(12,8))
 for sid,ax in zip(['V1','V2','R1','R2'],axs.flat):
  for method in ['single_llm','no_critic','multi_agent']:
   rows=[r for r in runs if r['scenario']==sid and r['method']==method and r['seed']==101]
   row=rows[0];best_score=0;yy=[]
   for r in row['history']:
    if r['verified']:best_score=max(best_score,r['score'])
    yy.append(best_score/ref[sid]['best']['score']*100)
   ax.plot(range(1,5),yy,'-o',label=LABELS[method])
  ax.set(ylim=(-3,105),xticks=range(1,5),xlabel='Candidate slot',ylabel='Catalog-reference objective (%)',title=sid+' / seed 101');ax.legend(fontsize=9)
 figs['07_search_trajectory']=save(fig,'07_search_trajectory')
 fig,ax=plt.subplots(figsize=(11,6));names=[r['case'] for r in attacks];vals=[int(r['verified']) for r in attacks]
 ax.barh(range(len(names)),[1]*len(names),color=[TEAL if v else ORANGE for v in vals])
 ax.set_yticks(range(len(names)),names);ax.set_xticks([]);ax.invert_yaxis();ax.set_title('Final recommendation gate across cyber test fixtures')
 for i,r in enumerate(attacks):ax.text(.02,i,('PASS' if r['verified'] else 'REJECT: '+', '.join(r['failure_reasons'])),va='center',color='white',fontsize=10)
 figs['08_attack_outcomes']=save(fig,'08_attack_outcomes')
 fig,ax=plt.subplots(figsize=(10,4.5))
 vv=df.pivot_table(index='scenario',columns='method',values='success',aggfunc='mean').reindex(index=['V1','V2','R1','R2'],columns=methods)
 im=ax.imshow(vv.values,vmin=0,vmax=1,cmap='YlGnBu',aspect='auto');ax.set_xticks(range(5),[LABELS[m] for m in methods]);ax.set_yticks(range(4),vv.index)
 for i in range(4):
  for j in range(5):ax.text(j,i,f'{int(round(vv.iloc[i,j]*2))}/2',ha='center',va='center',color='white' if vv.iloc[i,j]>.5 else INK)
 fig.colorbar(im,ax=ax,label='Success fraction');ax.set_title('Two seeds per scenario: descriptive results')
 figs['09_scenario_comparison']=save(fig,'09_scenario_comparison')
 return figs

if __name__=='__main__':
 all_plots();plt.close('all')
