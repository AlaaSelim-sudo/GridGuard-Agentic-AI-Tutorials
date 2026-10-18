import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .conventional import OUT,ROOT
LABELS={'stale_mpc':'MPC, stale limit','updated_mpc':'MPC, updated limit','raw_dqn':'DQN','shielded_dqn':'DQN + checker','agentic_mpc':'Agents + MPC'}
def main():
 data=json.loads((OUT/'runs.json').read_text());flat=pd.DataFrame([{k:v for k,v in r.items() if k!='steps'} for r in data])
 summary=flat.groupby(['case','method']).agg(episodes=('seed','size'),unsafe_steps=('unsafe_applied_steps','mean'),
  unsafe_proposals=('unsafe_proposals','mean'),interventions=('interventions','mean'),pv_kwh=('pv_kwh','mean'),
  utility=('discounted_utility','mean'),seconds=('decision_seconds','mean')).reset_index()
 (OUT/'summary.json').write_text(summary.to_json(orient='records',indent=2))
 plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
 def save(fig,name):
  fig.tight_layout()
  for ext in ['png','svg']:fig.savefig(ROOT/'figures'/f'{name}.{ext}',dpi=160,bbox_inches='tight')
 fig,axs=plt.subplots(1,2,figsize=(12,4.5))
 for seed in [11,22,33]:
  h=json.loads((OUT/f'training_seed_{seed}.json').read_text())['history']
  axs[0].plot([r['step'] for r in h],[r['mean_reward'] for r in h],label=f'Seed {seed}')
  axs[1].plot([r['step'] for r in h],[100*r['unsafe_proposal_fraction'] for r in h],label=f'Seed {seed}')
 axs[0].set(xlabel='Training transitions',ylabel='Mean training reward / 600 steps',title='DQN training includes exploratory failures')
 axs[1].set(xlabel='Training transitions',ylabel='Unsafe exploration (%)',title='Reward penalties do not certify safety')
 for ax in axs:ax.legend()
 save(fig,'10_dqn_training')
 fig,axs=plt.subplots(1,2,figsize=(13,4.8));methods=list(LABELS)
 for case,ax in zip(['nominal','rating_change'],axs):
  d=summary[summary['case']==case].set_index('method').reindex(methods)
  ax.bar(range(5),d.unsafe_steps,color=['#AC6037','#007F83','#AC6037','#3F92A2','#18384B'])
  ax.set_xticks(range(5),[LABELS[m] for m in methods],rotation=25,ha='right')
  ax.set(ylabel='Mean unsafe simulated steps / 12',title=case.replace('_',' ').title(),ylim=(0,12))
 save(fig,'11_controller_safety')
 fig,axs=plt.subplots(2,1,figsize=(11,7),sharex=True)
 for method in methods:
  r=next(r for r in data if r['case']=='rating_change' and r['profile']==0 and r['seed']==11 and r['method']==method)
  axs[0].step([s['minute'] for s in r['steps']],[s['cap'] for s in r['steps']],where='post',label=LABELS[method])
  axs[1].plot([s['minute'] for s in r['steps']],[s['max_line_pct'] for s in r['steps']],'-o',ms=3,label=LABELS[method])
 axs[0].set(ylabel='Fleet PV cap (%)',title='Constraint change at minute 25, normal rating restored at minute 45')
 axs[0].legend(ncol=3,fontsize=9);axs[1].axhline(100,color='black',ls='--');axs[1].set(xlabel='Minute',ylabel='Maximum allowed line current (%)')
 for ax in axs:ax.axvspan(25,45,color='#F5D5BC',alpha=.3)
 save(fig,'12_controller_trajectory')
 fig,axs=plt.subplots(1,2,figsize=(13,4.8))
 d=summary[summary['case']=='rating_change'].set_index('method').reindex(methods)
 axs[0].bar(range(5),d.pv_kwh,color='#007F83');axs[0].set(ylabel='PV energy over one hour (kWh)',title='Energy must be interpreted with violations')
 axs[1].bar(range(5),d.seconds*1000,color='#AC6037');axs[1].set_yscale('log');axs[1].set(ylabel='Total episode decision time (ms, log scale)',title='Online timing uses a shared cached AC table')
 for ax in axs:ax.set_xticks(range(5),[LABELS[m] for m in methods],rotation=25,ha='right')
 save(fig,'13_controller_cost')
 print(summary.to_string(index=False));plt.close('all')
if __name__=='__main__':main()
