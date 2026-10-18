"""Independent, reset-per-candidate OpenDSS tools for the three-hour tutorial."""
from pathlib import Path
import re,json,hashlib,time,math
from collections import defaultdict,deque
import numpy as np
import opendssdirect as dss

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/greensboro_udt8894'
SOURCE='udt8894-uhs20_1247x'
FAULT='l(r:udt8894-uhs20_1247)'
TAIL='udt8894-uhs20_1247x_b1_1'

def prepare():
 """Copy and patch deprecated syntax, preserving an original-source manifest."""
 dest=ROOT/'generated';dest.mkdir(exist_ok=True)
 manifest={}
 for p in DATA.glob('*.dss'):
  text=p.read_text(encoding='utf-8-sig')
  manifest[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
  text=re.sub(r'\bkvarlimit\b','kvarMax',text,flags=re.I)
  text=re.sub(r'\bVV_RefReactivePower\b','RefReactivePower',text,flags=re.I)
  if p.name.lower()=='master.dss':
   text='\n'.join('! teaching overlay: '+ln if ln.strip().lower()=='solve' or ln.strip().lower().startswith('plot ') else ln for ln in text.splitlines())
  (dest/p.name).write_text(text,encoding='utf-8')
 (ROOT/'results/source_manifest.json').write_text(json.dumps({'source':'OEDI SMART-DS 2981, uhs20_1247/udt8894','sha256':manifest,'changes':['deprecated PV property spelling','disable auto solve and plot']},indent=2))
 return dest/'Master.dss'

def base(bus):return bus.lower().split('.')[0]

def graph_data():
 edges=[];mv=[];line_catalog=[]
 for name in dss.Lines.AllNames():
  dss.Lines.Name(name)
  if not dss.CktElement.Enabled() or dss.CktElement.IsOpen(1,0):continue
  a,b=map(base,dss.CktElement.BusNames()[:2]);edges.append((a,b))
  dss.Circuit.SetActiveBus(a);ka=dss.Bus.kVBase()
  dss.Circuit.SetActiveBus(b);kb=dss.Bus.kVBase()
  if min(ka,kb)>1:mv.append((a,b))
  line_catalog.append((name,a,b))
 for name in dss.Transformers.AllNames():
  dss.Transformers.Name(name)
  if not dss.CktElement.Enabled():continue
  buses=list(dict.fromkeys(map(base,dss.CktElement.BusNames())))
  edges.extend((buses[0],b) for b in buses[1:])
 adj=defaultdict(set)
 for a,b in edges:adj[a].add(b);adj[b].add(a)
 seen={SOURCE};q=deque([SOURCE])
 while q:
  for b in adj[q.popleft()]-seen:seen.add(b);q.append(b)
 # Cycle rank of the reachable MV multigraph; parallel closed ties form a loop.
 medges=[tuple(sorted((a,b))) for a,b in mv if a in seen and b in seen and a!=b]
 nodes=set(x for e in medges for x in e)
 parent={n:n for n in nodes}
 def find(n):
  while parent[n]!=n:parent[n]=parent[parent[n]];n=parent[n]
  return n
 loops=0
 for a,b in medges:
  ra,rb=find(a),find(b)
  if ra==rb:loops+=1
  else:parent[ra]=rb
 topology=hashlib.sha256(json.dumps(sorted(set(tuple(sorted(e)) for e in edges))).encode()).hexdigest()[:16]
 return seen,loops,topology,line_catalog

def reset(load_mult=1,pv_cap=100,fault=False,tie='none',capacity=400,shed_fraction=0):
 master=ROOT/'generated/Master.dss'
 if not master.exists():prepare()
 dss.Basic.ClearAll();dss.Text.Command(f'compile [{master.as_posix()}]')
 dss.Text.Command('set controlmode=off');dss.Text.Command('set maxiterations=100')
 dss.Text.Command(f'set loadmult={load_mult}')
 dss.Text.Command(f'batchedit PVSystem..* %Pmpp={pv_cap}')
 dss.Text.Command('batchedit Storage..* State=IDLING DispMode=EXTERNAL')
 # Two openly synthetic restoration alternatives. A short and a long bypass.
 for name,length,amps in [('short',.25,capacity),('long',2.0,400)]:
  dss.Text.Command(f'New Line.tutorial_{name} phases=3 bus1={SOURCE}.1.2.3 bus2={TAIL}.1.2.3 r1=0.2 x1=0.3 r0=0.5 x0=0.6 units=km length={length} normamps={amps} emergamps={amps} enabled=no')
 if fault:dss.Text.Command(f'Edit Line.{FAULT} enabled=no')
 if tie in ['short','long','both']:
  names=['short','long'] if tie=='both' else [tie]
  for name in names:dss.Text.Command(f'Edit Line.tutorial_{name} enabled=yes')
 if tie=='fault':dss.Text.Command(f'Edit Line.{FAULT} enabled=yes')
 loads=[]
 for name in dss.Loads.AllNames():
  dss.Loads.Name(name);loads.append((name,dss.Loads.kW(),base(dss.CktElement.BusNames()[0])))
 # Artificial critical-priority set is explicitly reproducible, not a hospital map.
 critical={n for n,_,_ in sorted(loads)[::10]}
 noncritical=[n for n,_,_ in sorted(loads) if n not in critical]
 shed=set(noncritical[:round(len(noncritical)*shed_fraction)])
 for name in shed:dss.Text.Command(f'Edit Load.{name} enabled=no')
 reachable,cycles,topology,catalog=graph_data()
 # Grid-following devices cannot energize an island in this model.
 for cls,api in [('PVSystem',dss.PVsystems),('Storage',dss.Storages)]:
  for name in api.AllNames():
   api.Name(name)
   if base(dss.CktElement.BusNames()[0]) not in reachable:dss.Text.Command(f'Edit {cls}.{name} enabled=no')
 dss.Solution.Solve()
 return loads,critical,shed,reachable,cycles,topology,catalog

def simulate(load_mult=1,pv_cap=100,fault=False,tie='none',capacity=400,shed_fraction=0,details=False):
 started=time.perf_counter()
 loads,critical,shed,reachable,cycles,topology,catalog=reset(load_mult,pv_cap,fault,tie,capacity,shed_fraction)
 buses=[]
 for name in dss.Circuit.AllBusNames():
  dss.Circuit.SetActiveBus(name);v=np.asarray(dss.Bus.puVmagAngle()[::2],float)
  if len(v) and name.lower() in reachable:
   buses.append({'bus':name,'vmin':float(v.min()),'vmax':float(v.max())})
 lines=[]
 for name in dss.Lines.AllNames():
  dss.Lines.Name(name)
  if not dss.CktElement.Enabled():continue
  rating=float(dss.CktElement.NormalAmps());amps=np.asarray(dss.CktElement.CurrentsMagAng()[::2],float)
  lines.append({'line':name,'loading_pct':100*float(amps.max())/rating if rating>0 else None})
 missing=sum(r['loading_pct'] is None for r in lines)
 pvs=[]
 for name in dss.PVsystems.AllNames():
  dss.PVsystems.Name(name)
  if not dss.CktElement.Enabled():continue
  pvs.append(float(dss.PVsystems.kW()))
 nominal=sum(kw*load_mult for _,kw,_ in loads)
 served=sum(kw*load_mult for n,kw,b in loads if b in reachable and n not in shed)
 crit_total=sum(kw*load_mult for n,kw,_ in loads if n in critical)
 crit_served=sum(kw*load_mult for n,kw,b in loads if n in critical and b in reachable and n not in shed)
 voltage_viol=sum(r['vmin']<.95-1e-6 or r['vmax']>1.05+1e-6 for r in buses)
 m={'converged':bool(dss.Solution.Converged()),'voltage_violations':int(voltage_viol),
    'vmin':min((r['vmin'] for r in buses),default=0),'vmax':max((r['vmax'] for r in buses),default=0),
    'voltage_severity':sum(max(0,.95-r['vmin'])+max(0,r['vmax']-1.05) for r in buses),
    'overloaded_lines':sum(r['loading_pct']>100+1e-4 for r in lines if r['loading_pct'] is not None),
    'max_line_pct':max((r['loading_pct'] for r in lines if r['loading_pct'] is not None),default=0),
    'missing_line_ratings':missing,'mv_cycles':cycles,'topology_hash':topology,
    'served_kw':served,'unserved_kw':nominal-served,'nominal_kw':nominal,
    'critical_served_kw':crit_served,'critical_total_kw':crit_total,'pv_kw':sum(pvs),
    'losses_kw':float(dss.Circuit.Losses()[0])/1000,
    'tie_loading_pct':next((r['loading_pct'] for r in lines if r['line']==f'tutorial_{tie}'),None),
    'load_mult':load_mult,'pv_cap':pv_cap,'tie':tie,'shed_fraction':shed_fraction,
    'physical_load_disconnects':len(shed),'elapsed_s':time.perf_counter()-started}
 if details:m.update(buses=buses,lines=lines,line_endpoints=catalog)
 return m

def verify_physics(m,allow_unserved=False):
 reasons=[]
 if not m['converged']:reasons.append('power_flow')
 if m['voltage_violations']:reasons.append('voltage')
 if m['overloaded_lines']:reasons.append('thermal')
 if m['missing_line_ratings']:reasons.append('missing_rating')
 if m['mv_cycles']:reasons.append('mv_radiality')
 if not allow_unserved and m['unserved_kw']>.1:reasons.append('load_service')
 return reasons
