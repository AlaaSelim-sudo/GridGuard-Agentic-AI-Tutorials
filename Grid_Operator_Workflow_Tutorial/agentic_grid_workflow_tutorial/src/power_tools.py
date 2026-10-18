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

def element_state(kind,name):
 """Identity and switching state, retaining terminal phases and parallel assets."""
 terminals=int(dss.CktElement.NumTerminals())
 conductors=int(dss.CktElement.NumConductors())
 return {'kind':kind,'name':name.lower(),'enabled':bool(dss.CktElement.Enabled()),
         'buses':[b.lower() for b in dss.CktElement.BusNames()],
         'phases':int(dss.CktElement.NumPhases()),
         'open_conductors':[[bool(dss.CktElement.IsOpen(t,c))
                             for c in range(1,conductors+1)]
                            for t in range(1,terminals+1)],
         'normal_amps':float(dss.CktElement.NormalAmps())}

def terminal_connected(state,terminal):
 # Reachability remains a bus-level approximation, not a phase-level proof.
 return any(not opened for opened in state['open_conductors'][terminal][:state['phases']])

def graph_data():
 edges=[];mv=[];line_catalog=[];states=[]
 for name in dss.Lines.AllNames():
  dss.Lines.Name(name)
  state=element_state('line',name);states.append(state)
  if not state['enabled'] or not all(terminal_connected(state,t) for t in [0,1]):continue
  a,b=map(base,dss.CktElement.BusNames()[:2]);edges.append((a,b))
  dss.Circuit.SetActiveBus(a);ka=dss.Bus.kVBase()
  dss.Circuit.SetActiveBus(b);kb=dss.Bus.kVBase()
  if min(ka,kb)>1:mv.append((a,b))
  line_catalog.append((name,a,b))
 for name in dss.Transformers.AllNames():
  dss.Transformers.Name(name)
  state=element_state('transformer',name);states.append(state)
  if not state['enabled']:continue
  buses=list(dict.fromkeys(base(b) for t,b in enumerate(state['buses'])
                          if terminal_connected(state,t)))
  if buses:edges.extend((buses[0],b) for b in buses[1:])
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
 # A set of bus pairs would identify short, long and parallel ties as identical.
 # Include disabled assets and conductor states as well as active edge identity.
 topology=hashlib.sha256(json.dumps(sorted(states,key=lambda s:(s['kind'],s['name'])),
                                    sort_keys=True,separators=(',',':')).encode()).hexdigest()
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
  current=float(amps.max()) if len(amps) else float('nan')
  lines.append({'line':name,'normal_amps':rating,'max_current_amps':current,
                'loading_pct':100*current/rating if math.isfinite(rating) and rating>0 else None})
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
    'energized_bus_count':len(buses),'evaluated_line_count':len(lines),
    'invalid_measurements':sum(not all(math.isfinite(r[k]) for k in ['vmin','vmax']) for r in buses)
       +sum(not math.isfinite(r['max_current_amps']) for r in lines),
    'served_kw':served,'unserved_kw':nominal-served,'nominal_kw':nominal,
    'critical_served_kw':crit_served,'critical_total_kw':crit_total,'pv_kw':sum(pvs),
    'losses_kw':float(dss.Circuit.Losses()[0])/1000,
    'tie_loading_pct':next((r['loading_pct'] for r in lines if r['line']==f'tutorial_{tie}'),None),
    'load_mult':load_mult,'pv_cap':pv_cap,'tie':tie,'shed_fraction':shed_fraction,
    'physical_load_disconnects':len(shed),'elapsed_s':time.perf_counter()-started}
 if details:m.update(buses=buses,lines=lines,line_endpoints=catalog)
 return m

def verify_physics(m,allow_unserved=False,rating_fraction=1.0):
 """Fail-closed nominal-model checks; an empty list is a modelled acceptance.

 A temporary rating fraction changes permitted currents, not the AC solution.
 Per-line evidence is required to assess derating; the input is never mutated.
 This is not a protection, transformer-thermal or robust safety certificate.
 """
 def finite(v):
  return isinstance(v,(int,float,np.integer,np.floating)) and not isinstance(v,(bool,np.bool_)) and math.isfinite(float(v))
 def count(v):return finite(v) and v>=0 and float(v).is_integer()
 if not isinstance(m,dict) or not m:return ['missing_evidence']
 required=['converged','vmin','vmax','voltage_violations','overloaded_lines',
           'max_line_pct','missing_line_ratings','mv_cycles','topology_hash',
           'served_kw','unserved_kw','nominal_kw','critical_served_kw','critical_total_kw']
 if any(k not in m for k in required):return ['missing_evidence']
 if not finite(rating_fraction) or not 0<rating_fraction<=1:return ['invalid_rating_fraction']
 numbers=['vmin','vmax','max_line_pct','served_kw','unserved_kw','nominal_kw',
          'critical_served_kw','critical_total_kw']
 counters=['voltage_violations','overloaded_lines','missing_line_ratings','mv_cycles']
 counters += [k for k in ['energized_bus_count','evaluated_line_count','invalid_measurements'] if k in m]
 optional=[k for k in ['pv_kw','losses_kw','voltage_severity','load_mult','pv_cap','shed_fraction'] if k in m]
 if any(not finite(m[k]) for k in numbers+optional) or any(not count(m[k]) for k in counters):
  return ['invalid_numerical_evidence']
 if not isinstance(m['converged'],(bool,np.bool_)) or not isinstance(m['topology_hash'],str) or not m['topology_hash']:
  return ['invalid_evidence_schema']
 if (any(m[k]<0 for k in numbers) or m['vmin']>m['vmax']
     or m['served_kw']>m['nominal_kw']+.1
     or abs(m['served_kw']+m['unserved_kw']-m['nominal_kw'])>.1
     or m['critical_served_kw']>m['critical_total_kw']+.1
     or m['critical_served_kw']>m['served_kw']+.1
     or m['critical_total_kw']>m['nominal_kw']+.1
     or ('load_mult' in m and m['load_mult']<=0)
     or ('pv_cap' in m and not 0<=m['pv_cap']<=100)
     or ('shed_fraction' in m and not 0<=m['shed_fraction']<=1)):
  return ['invalid_evidence_domain']
 reasons=[]
 if not m['converged']:reasons.append('power_flow')
 if m.get('invalid_measurements',0):reasons.append('invalid_numerical_evidence')
 if m.get('energized_bus_count',1)==0 or m.get('evaluated_line_count',1)==0 or m['vmin']<=0:
  reasons.append('empty_measurement_evidence')
 if m['voltage_violations'] or m['vmin']<.95-1e-6 or m['vmax']>1.05+1e-6:reasons.append('voltage')
 if m['overloaded_lines'] or m['max_line_pct']>100+1e-4:reasons.append('thermal')
 if m['missing_line_ratings']:reasons.append('missing_rating')
 if m['mv_cycles']:reasons.append('mv_radiality')
 if not allow_unserved and m['unserved_kw']>.1:reasons.append('load_service')
 if 'buses' in m:
  buses=m['buses']
  if not isinstance(buses,list) or not buses:reasons.append('empty_measurement_evidence')
  elif any(not isinstance(r,dict) or not all(finite(r.get(k)) for k in ['vmin','vmax']) for r in buses):
   reasons.append('invalid_numerical_evidence')
  elif any(r['vmin']<=0 or r['vmin']>r['vmax'] for r in buses):reasons.append('invalid_evidence_domain')
  else:
   violations=sum(r['vmin']<.95-1e-6 or r['vmax']>1.05+1e-6 for r in buses)
   if violations:reasons.append('voltage')
   if (violations!=m['voltage_violations']
       or abs(min(r['vmin'] for r in buses)-m['vmin'])>1e-8
       or abs(max(r['vmax'] for r in buses)-m['vmax'])>1e-8
       or ('energized_bus_count' in m and len(buses)!=m['energized_bus_count'])):
    reasons.append('inconsistent_measurement_evidence')
 lines=m.get('lines')
 if lines is None:
  if rating_fraction!=1:reasons.append('missing_line_evidence')
 elif not isinstance(lines,list) or not lines:reasons.append('empty_measurement_evidence')
 else:
  loadings=[]
  for row in lines:
   if not isinstance(row,dict) or not finite(row.get('normal_amps')) or row['normal_amps']<=0:
    reasons.append('missing_rating');continue
   if not finite(row.get('max_current_amps')) or not finite(row.get('loading_pct')):
    reasons.append('invalid_numerical_evidence');continue
   if row['max_current_amps']<0 or row['loading_pct']<0:
    reasons.append('invalid_evidence_domain');continue
   loading=100*row['max_current_amps']/row['normal_amps']
   if abs(loading-row['loading_pct'])>1e-8:reasons.append('inconsistent_measurement_evidence')
   loadings.append(loading)
  if any(v/rating_fraction>100+1e-4 for v in loadings):reasons.append('thermal')
  if len(loadings)==len(lines) and (sum(v>100+1e-4 for v in loadings)!=m['overloaded_lines']
      or abs(max(loadings)-m['max_line_pct'])>1e-8
      or ('evaluated_line_count' in m and len(lines)!=m['evaluated_line_count'])):
   reasons.append('inconsistent_measurement_evidence')
 return list(dict.fromkeys(reasons))
