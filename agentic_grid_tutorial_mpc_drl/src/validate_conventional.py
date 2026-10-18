"""Independent finite-horizon enumeration and saved-study consistency checks."""
import itertools,json
import numpy as np
from .conventional import *
def main():
 T=table()
 for derating in [1.,.8]:
  for previous in [0,3,7]:
   seq=PROFILES[0];choices=[]
   for plan in itertools.product(range(8),repeat=3):
    if not all(feasible(T,seq[k],a,derating) for k,a in enumerate(plan)):continue
    value=0.;p=previous
    for k,a in enumerate(plan):value+=GAMMA**k*utility(T,seq[k],a,p);p=a
    choices.append((value,plan[0]))
   optimum=max(v for v,a in choices)
   first=mpc(T,seq,0,previous,derating)
   assert any(abs(v-optimum)<1e-10 and a==first for v,a in choices)
 for seed in [11,22,33]:
  initial=DQN(seed);trained=DQN(seed);trained.load(OUT/f'dqn_seed_{seed}.npz')
  assert any(not np.allclose(x,y) for x,y in zip(initial.p,trained.p))
  assert all(np.isfinite(v).all() for v in trained.p)
 runs=json.loads((OUT/'runs.json').read_text());assert len(runs)==52
 for r in runs:
  assert len(r['steps'])==12
  if r['method'] in ['updated_mpc','shielded_dqn','agentic_mpc']:
   assert r['unsafe_applied_steps']==0
  assert abs(r['pv_kwh']-sum(s['pv_kw'] for s in r['steps'])/12)<1e-8
 # Fresh OpenDSS checks establish cache agreement for selected demand/cap pairs.
 for i,a in [(0,2),(2,3),(4,2)]:
  fresh=simulate(load_mult=float(LOADS[i]),pv_cap=float(CAPS[a]))
  assert abs(fresh['max_line_pct']-T[i][a]['max_line_pct'])<1e-7
  assert abs(fresh['pv_kw']-T[i][a]['pv_kw'])<1e-7
 assert not any(feasible(T,4,a,.65) for a in range(8))
 print('Passed: MPC vs exhaustive sequences, trained finite weights, 52 episode records, protected outcomes, energy accounting, fresh AC/cache agreement and infeasibility stress.')
if __name__=='__main__':main()
