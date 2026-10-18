"""Finite-action economic MPC, trained DQN and shared verification benchmark.

The feeder is quasi-static. Previous cap is the controlled state and demand is
exogenous. No inverter dynamics, battery energy, or stability claim is implied.
"""
import json,time,copy
from pathlib import Path
from functools import lru_cache
import numpy as np
from .framework import ROOT,Llama
from .power_tools import simulate,verify_physics

OUT=ROOT/'results/conventional';OUT.mkdir(parents=True,exist_ok=True)
CAPS=np.array([0,10,20,30,40,60,80,100],float)
LOADS=np.array([.3,.5,.7,1.,1.3])
GAMMA=.95;SWITCH_COST=.15;HORIZON=3
PROFILES=[[3,2,1,0,1,2,3,4,3,2,1,3],[1,2,3,4,3,2,1,0,2,3,4,2]]

def table():
 path=OUT/'ac_table.json'
 if path.exists():return json.loads(path.read_text())
 start=time.perf_counter();data=[]
 for demand in LOADS:
  data.append([simulate(load_mult=float(demand),pv_cap=float(cap)) for cap in CAPS])
 path.write_text(json.dumps(data,indent=2))
 (OUT/'table_cost.json').write_text(json.dumps({'ac_solves':len(LOADS)*len(CAPS),'seconds':time.perf_counter()-start}))
 return data

def metrics(T,li,a,derating):
 m=dict(T[int(li)][int(a)])
 # A uniform temporary reduction in allowed line current changes constraints,
 # not the electrical solution. The only other thermal fact needed is maximum.
 m['max_line_pct']/=derating
 m['overloaded_lines']=int(m['max_line_pct']>100+1e-4)
 return m

def feasible(T,li,a,d):return not verify_physics(metrics(T,li,a,d))
def utility(T,li,a,prev):return T[int(li)][int(a)]['pv_kw']/8000-SWITCH_COST*abs(CAPS[a]-CAPS[prev])/100
def obs(seq,t,prev,derating):
 future=[LOADS[seq[min(t+k,len(seq)-1)]]/1.3 for k in range(HORIZON)]
 return np.array(future+[CAPS[prev]/100,derating,(len(seq)-t)/len(seq)],dtype=np.float64)

def mpc(T,seq,t,prev,derating):
 """Solve an H=3 discounted finite-action problem, apply its first action."""
 @lru_cache(None)
 def value(k,p):
  if k>=HORIZON or t+k>=len(seq):return 0.,-1
  values=[]
  for a in range(len(CAPS)):
   if feasible(T,seq[t+k],a,derating):
    values.append((utility(T,seq[t+k],a,p)+GAMMA*value(k+1,a)[0],a))
  return max(values,key=lambda v:v[0]) if values else (-1e6,-1)
 return value(0,int(prev))[1]

class DQN:
 """Two hidden ReLU layers, experience replay, target network and Adam."""
 def __init__(self,seed):
  self.rng=np.random.default_rng(seed);sizes=[6,48,48,8]
  self.p=[]
  for x,y in zip(sizes[:-1],sizes[1:]):self.p.extend([self.rng.normal(0,np.sqrt(2/x),(x,y)),np.zeros(y)])
  self.target=[v.copy() for v in self.p];self.m=[np.zeros_like(v) for v in self.p];self.v=[np.zeros_like(v) for v in self.p];self.step=0
 def forward(self,x,params=None):
  p=self.p if params is None else params
  h1=np.maximum(0,x@p[0]+p[1]);h2=np.maximum(0,h1@p[2]+p[3]);q=h2@p[4]+p[5]
  return q,(x,h1,h2)
 def train_batch(self,x,a,r,nxt,done):
  q,(x,h1,h2)=self.forward(x)
  # Standard DQN Bellman target. Targets are not MPC labels.
  y=r+GAMMA*(1-done)*self.forward(nxt,self.target)[0].max(axis=1)
  error=q[np.arange(len(a)),a]-y
  dq=np.zeros_like(q);dq[np.arange(len(a)),a]=np.clip(error,-1,1)/len(a)
  g4=h2.T@dq;g5=dq.sum(axis=0);dh2=(dq@self.p[4].T)*(h2>0)
  g2=h1.T@dh2;g3=dh2.sum(axis=0);dh1=(dh2@self.p[2].T)*(h1>0)
  grad=[x.T@dh1,dh1.sum(axis=0),g2,g3,g4,g5]
  self.step+=1
  for i,g in enumerate(grad):
   g=np.clip(g,-5,5);self.m[i]=.9*self.m[i]+.1*g;self.v[i]=.999*self.v[i]+.001*g*g
   self.p[i]-=.001*(self.m[i]/(1-.9**self.step))/(np.sqrt(self.v[i]/(1-.999**self.step))+1e-8)
  if self.step%200==0:self.target=[v.copy() for v in self.p]
  return float(np.mean(np.where(abs(error)<1,.5*error**2,abs(error)-.5)))
 def save(self,path):np.savez(path,**{f'p{i}':v for i,v in enumerate(self.p)})
 def load(self,path):
  z=np.load(path);self.p=[z[f'p{i}'] for i in range(6)];self.target=[v.copy() for v in self.p]

def train(T,seed,steps=18000):
 path=OUT/f'dqn_seed_{seed}.npz';net=DQN(seed)
 if path.exists():net.load(path);return net
 start=time.perf_counter();rng=np.random.default_rng(seed+1000);buffer=[];history=[]
 def sequence():
  # Training uses nominal ratings only. Held-out deterministic trajectories
  # are excluded exactly, although they use the same observed demand levels.
  while True:
   seq=rng.integers(0,len(LOADS),size=12).tolist()
   if seq not in PROFILES:return seq
 seq=sequence();t=0;prev=2;reward_sum=0.;violations=0
 for step in range(steps):
  x=obs(seq,t,prev,1.);eps=max(.05,1-step/(steps*.75))
  a=int(rng.integers(8)) if rng.random()<eps else int(net.forward(x[None])[0][0].argmax())
  ok=feasible(T,seq[t],a,1.)
  reward=utility(T,seq[t],a,prev) if ok else -2.
  done=t==len(seq)-1;nxt=obs(seq,min(t+1,len(seq)-1),a,1.)
  buffer.append((x,a,reward,nxt,float(done)))
  if len(buffer)>12000:buffer.pop(0)
  if len(buffer)>=128:
   sample=[buffer[i] for i in rng.integers(len(buffer),size=64)]
   bx,ba,br,bn,bd=map(np.asarray,zip(*sample));loss=net.train_batch(bx,ba.astype(int),br,bn,bd)
  reward_sum+=reward;violations+=not ok;prev=a;t+=1
  if done:seq=sequence();t=0;prev=2
  if (step+1)%600==0:
   history.append({'step':step+1,'mean_reward':reward_sum/600,'unsafe_proposal_fraction':violations/600,'td_huber_loss':loss,'epsilon':eps})
   reward_sum=0.;violations=0
 net.save(path)
 (OUT/f'training_seed_{seed}.json').write_text(json.dumps({'seed':seed,'steps':steps,'seconds':time.perf_counter()-start,'history':history,'architecture':[6,48,48,8],'reward':'PV_kW/8000 - 0.15*abs(cap-previous_cap)/100 if feasible, otherwise -2','rating_training':[1.0],'gamma':GAMMA,'optimizer':'Adam, lr 0.001','replay_capacity':12000,'batch':64,'target_update':200,'evaluation_used_in_training':False},indent=2))
 return net

def episode(T,net,method,case,profile,seed,llama=None):
 seq=PROFILES[profile];prev=2;rows=[];route='MPC_TOOL';calls0=len(llama.calls) if llama else 0
 for t,li in enumerate(seq):
  actual=.8 if case=='rating_change' and 5<=t<9 else 1.
  started=time.perf_counter();x=obs(seq,t,prev,actual);q=net.forward(x[None])[0][0]
  proposal=None;fallback=False;reason=[];event=None
  if method=='stale_mpc':proposal=mpc(T,seq,t,prev,1.)
  elif method in ['updated_mpc','agentic_mpc']:
   proposal=mpc(T,seq,t,prev,actual)
   if method=='agentic_mpc' and t in ([0,5,9] if case=='rating_change' else [0]):
    context={'actions':[{'id':'MPC_TOOL','purpose':'receding-horizon search with current validated constraints'},{'id':'DQN_TOOL','purpose':'fast trained policy; trained only at nominal ratings'}],
      'objective':'Choose a numerical control tool. Safety checker applies independently to either tool.',
      'validated_state':{'load_multiplier':float(LOADS[li]),'rating_fraction':actual},
      'approved_event':f'Current permitted line-current rating is {actual*100:.0f}% of nominal. This is the already validated structured event.'}
    answer=llama.ask('Supervisory Planning Agent',context,seed+profile*100+t)
    critique=llama.ask('Constraint Critic Agent',{'state':context,'proposed_route':answer,'policy':'When rating changed, prefer updated model-based search. Never bypass verifier.'},seed+5000+t,kind='critic')
    route=answer['action_id'];event={'planner':answer,'critic':critique}
   if method=='agentic_mpc':
    if route=='DQN_TOOL':proposal=int(q.argmax())
    elif route!='MPC_TOOL':proposal=-1
  else:proposal=int(q.argmax())
  proposal_safe=proposal>=0 and feasible(T,li,proposal,actual)
  executed=proposal
  if method in ['shielded_dqn','agentic_mpc'] and not proposal_safe:
   fallback=True;reason=['shared_checker_rejection']
   if method=='shielded_dqn':executed=next((int(a) for a in np.argsort(-q) if feasible(T,li,a,actual)),-1)
   else:executed=mpc(T,seq,t,prev,actual)
  elapsed=time.perf_counter()-started
  if executed<0:raise RuntimeError('No feasible action: explicit escalation required')
  m=metrics(T,li,executed,actual);safe=not verify_physics(m)
  rows.append({'t':t,'minute':t*5,'load_mult':float(LOADS[li]),'rating_fraction':actual,'proposed_cap':float(CAPS[proposal]) if proposal>=0 else None,
   'cap':float(CAPS[executed]),'unsafe_proposal':not proposal_safe,'unsafe_applied':not safe,'intervention':fallback,'pv_kw':m['pv_kw'],
   'max_line_pct':m['max_line_pct'],'voltage_violations':m['voltage_violations'],'stage_utility':utility(T,li,executed,prev),
   'decision_seconds':elapsed,'event':event,'reasons':reason})
  prev=executed
 return {'method':method,'case':case,'profile':profile,'seed':seed,'steps':rows,'unsafe_applied_steps':sum(r['unsafe_applied'] for r in rows),
  'unsafe_proposals':sum(r['unsafe_proposal'] for r in rows),'interventions':sum(r['intervention'] for r in rows),
  'pv_kwh':sum(r['pv_kw'] for r in rows)/12,'discounted_utility':sum(GAMMA**i*r['stage_utility'] for i,r in enumerate(rows)),
  'decision_seconds':sum(r['decision_seconds'] for r in rows),'llm_calls':len(llama.calls)-calls0 if llama else 0}

def main():
 T=table();networks={}
 (OUT/'infeasibility_stress.json').write_text(json.dumps({'load_mult':1.3,'rating_fraction':.65,
  'feasible_caps':[float(CAPS[a]) for a in range(8) if feasible(T,4,a,.65)],
  'required_response':'No admissible action in this PV-only catalog. Escalate for additional controls; do not fabricate feasibility.',
  'design_note':'Main transient uses 80% rating so every demand state has a feasible action. The initially probed 65% case is retained here as an infeasibility stress test.'},indent=2))
 for seed in [11,22,33]:
  print('Training DQN',seed,flush=True);networks[seed]=train(T,seed)
 llama=Llama(log_path=OUT/'supervisor_calls.json');runs=[]
 for case in ['nominal','rating_change']:
  for profile in [0,1]:
   for seed,net in networks.items():
    for method in ['stale_mpc','updated_mpc','raw_dqn','shielded_dqn']:
     runs.append(episode(T,net,method,case,profile,seed))
   print('Live supervisory agents',case,profile,flush=True)
   runs.append(episode(T,networks[11],'agentic_mpc',case,profile,11,llama))
   (OUT/'runs.json').write_text(json.dumps(runs,indent=2))
 (OUT/'metadata.json').write_text(json.dumps({'model':llama.metadata,'controller_horizon':HORIZON,'step_minutes':5,'training_seeds':[11,22,33],
  'test_profiles':PROFILES,'training_steps_per_seed':18000,'shared_table_ac_solves':40,'calls':len(llama.calls),
  'scope':'Quasi-static finite-action voltage-control benchmark. Exact shared AC lookup; two held-out load sequences, nominal and changed-rating versions. DRL has 3 seeds; Llama supervisor uses seed11 DQN only. No deployment or statistical claim.',
  'cost':'Controller decision time uses precomputed AC lookup and excludes table construction. Training and table costs are separate. Updated MPC sees current rating; stale MPC intentionally retains nominal rating. All controllers get the same load forecasts.',
  'safety':'Shielded DQN and agentic MPC use the same checker. Deterministic updated MPC is the strong matched-information counterfactual.'},indent=2))
 print('DONE',len(runs),'episodes;',len(llama.calls),'actual supervisory Llama calls',flush=True)
if __name__=='__main__':main()
