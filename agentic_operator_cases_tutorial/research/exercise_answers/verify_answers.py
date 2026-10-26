"""Recalculate the three exercise answers with the canonical classroom tools."""
from pathlib import Path
import hashlib,json,sys

REPO=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(REPO/'agentic_grid_workflow_tutorial'))
from src import classroom_labs as lab

v=lab.voltage_lab(1.,.75)['table']
r=lab.restoration_sweep((40.,60.,80.,100.,120.,180.))['table'].drop(columns='pickup')
c=lab.cyber_sweep((0.,.10))['table']
assert v.feasible.all()
assert abs(v.iloc[0].max_allowed_current_pct-78.5278947554)<1e-5
assert abs(v.iloc[1].max_allowed_current_pct-54.8541579372)<1e-5
assert abs(v.iloc[0].current_step_J-.0311038194)<1e-7
assert abs(v.iloc[1].current_step_J-.4324637539)<1e-7
at40=r[r.tie_capacity_kw==40.];at180=r[r.tie_capacity_kw==180.]
assert list(at40.served_kw)==[130.,140.] and list(at40.critical_kw)==[90.,30.]
assert list(at180.served_kw)==[250.,250.] and list(at180.critical_kw)==[90.,90.]
matching=[capacity for capacity,g in r.groupby('tie_capacity_kw') if g.served_kw.nunique()==1 and g.critical_kw.nunique()==1]
assert min(matching)==80.
small=c[c.scale==.10]
assert not small.alarm.any()
assert abs(small.iloc[0].J-10.1432371619)<1e-7
assert abs(small.iloc[1].J-3.920221691)<1e-7
assert abs(small.iloc[0].state_error_rad-.0008057145)<1e-9
assert abs(small.iloc[1].state_error_rad-.0025529499)<1e-9
paths=['Classroom_Labs.ipynb','src/classroom_labs.py','src/continuous_control.py','src/standard_formulations.py']
report=dict(scope='Fresh numerical classroom fixtures; no LLM call or equipment operation',
 voltage=json.loads(v.to_json(orient='records')),restoration=json.loads(r.to_json(orient='records')),
 cyber=json.loads(c.to_json(orient='records')),first_matching_tested_capacity_kw=min(matching),
 source_sha256={p:hashlib.sha256((REPO/'agentic_grid_workflow_tutorial'/p).read_bytes()).hexdigest() for p in paths})
if '--write' in sys.argv:
    (Path(__file__).parent/'reference_results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(voltage_passes=True,restoration_first_matching_capacity_kw=80,cyber_both_alarms=False,verified=True)))
