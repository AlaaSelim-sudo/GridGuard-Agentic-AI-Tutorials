"""Small DQN trained on rewards, not on MPC labels. Training is optional."""
import json, time
import numpy as np
from dataclasses import replace
from .power_tools import ROOT, verify_physics
from .control_tools import CAPS, LOADS, GAMMA, Case, observation, utility, provenance, digest

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

TRAINING = {'seed': 11, 'steps': 18000, 'architecture': [6,48,48,8],
 'reward': 'PV_kW/8000 - 0.15*abs(cap-previous_cap)/100 if feasible, otherwise -2',
 'rating_training': [1.0], 'gamma': GAMMA, 'optimizer': 'Adam, lr 0.001',
 'replay_capacity': 12000, 'batch': 64, 'target_update': 200,
 'observation': ['forecast_load_0/1.3','forecast_load_1/1.3','forecast_load_2/1.3',
                 'previous_cap/100','rating_fraction','remaining_episode_fraction'],
 'held_out_sequences': [[3,2,1,0,1,2,3,4,3,2,1,3], [1,2,3,4,3,2,1,0,2,3,4,2]]}

def train(T):
 """Reproducible CPU training; save weights and their full input manifest."""
 seed=TRAINING['seed'];steps=TRAINING['steps'];net=DQN(seed)
 started=time.perf_counter();rng=np.random.default_rng(seed+1000);buffer=[];history=[]
 valid=[[not verify_physics(T[li][a]) for a in range(8)] for li in range(5)]
 def sequence():
  while True:
   seq=rng.integers(0,len(LOADS),size=12).tolist()
   if seq not in TRAINING['held_out_sequences']:return seq
 def obs(seq,t,prev):
  horizon=tuple(seq[min(t+k,len(seq)-1)] for k in range(3))
  return observation(Case('training',forecast=horizon,previous=prev),(len(seq)-t)/len(seq))
 seq=sequence();t=0;prev=2;reward_sum=0.;violations=0
 for step in range(steps):
  x=obs(seq,t,prev);eps=max(.05,1-step/(steps*.75))
  a=int(rng.integers(8)) if rng.random()<eps else int(net.forward(x[None])[0][0].argmax())
  ok=valid[seq[t]][a];reward=utility(T,seq[t],a,prev) if ok else -2.
  done=t==len(seq)-1;nxt=obs(seq,min(t+1,len(seq)-1),a)
  buffer.append((x,a,reward,nxt,float(done)))
  if len(buffer)>12000:buffer.pop(0)
  if len(buffer)>=128:
   sample=[buffer[i] for i in rng.integers(len(buffer),size=64)]
   bx,ba,br,bn,bd=map(np.asarray,zip(*sample));loss=net.train_batch(bx,ba.astype(int),br,bn,bd)
  reward_sum+=reward;violations+=not ok;prev=a;t+=1
  if done:seq=sequence();t=0;prev=2
  if (step+1)%600==0:
   history.append({'step':step+1,'mean_reward':reward_sum/600,
    'unsafe_proposal_fraction':violations/600,'td_huber_loss':loss,'epsilon':eps})
   reward_sum=0.;violations=0
 path=ROOT/'models/dqn_seed_11.npz';net.save(path)
 record=dict(TRAINING,seconds=time.perf_counter()-started,history=history,
             scope='Same five demand levels in training and testing; two exact trajectories excluded. No broad generalization claim.')
 (ROOT/'models/training_seed_11.json').write_text(json.dumps(record,indent=2))
 manifest={'inputs':provenance(),'training':TRAINING,'training_code':digest(__file__),
           'weights_sha256':digest(path),'record_sha256':digest(ROOT/'models/training_seed_11.json')}
 (ROOT/'models/manifest.json').write_text(json.dumps(manifest,indent=2))
 return net

def load_policy():
 manifest=json.loads((ROOT/'models/manifest.json').read_text())
 expected={'inputs':provenance(),'training':TRAINING,'training_code':digest(__file__),
           'weights_sha256':digest(ROOT/'models/dqn_seed_11.npz'),
           'record_sha256':digest(ROOT/'models/training_seed_11.json')}
 if manifest!=expected:
  raise ValueError('Policy provenance mismatch. Rebuild the AC table and explicitly retrain: python -m src.run_labs --train')
 net=DQN(11);net.load(ROOT/'models/dqn_seed_11.npz');return net
