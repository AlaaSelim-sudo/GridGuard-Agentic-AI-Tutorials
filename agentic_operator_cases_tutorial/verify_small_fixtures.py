"""Recheck the two small numerical fixtures, without changing archived evidence."""
from pathlib import Path
import importlib.util,json,math
import numpy as np
ROOT=Path(__file__).resolve().parent
source=ROOT/'research/evidence/src/standard_formulations.py'
spec=importlib.util.spec_from_file_location('checked_standard_formulations',source)
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
rows=[]
for capacity,expected_weighted,expected_plain in [(40,(130,90),(140,30)),(60,(180,90),(190,30)),(80,(200,90),(200,90)),(100,(200,90),(200,90)),(120,(250,90),(250,90))]:
    graph=model.restoration_graph(capacity);checked=model.solve_restoration_milp(capacity);result=checked['milp']
    assert checked['agreement']
    assert (result['served_kw'],result['critical_served_kw'])==expected_weighted,(capacity,result)
    graph['priority']=[0,1,1,1,1,1]
    plain=model._enumerate_restoration(graph)['solution']['pickup']
    total=sum(a*b for a,b in zip(graph['demand_kw'],plain))
    critical=sum(graph['demand_kw'][i]*plain[i] for i in [2,5])
    assert (total,critical)==expected_plain,(capacity,total,critical)
    rows.append({'tie_capacity_kw':capacity,'weighted_total_kw':result['served_kw'],'weighted_critical_kw':result['critical_served_kw'],
                 'unweighted_total_kw':total,'unweighted_critical_kw':critical})
cyber=model.run_wls_demo()
assert math.isclose(cyber['cases'][0]['chi_square']['statistic'],3.9202216910306,abs_tol=1e-8)
assert math.isclose(cyber['cases'][2]['chi_square']['statistic'],cyber['cases'][0]['chi_square']['statistic'],abs_tol=1e-8)
assert math.isclose(cyber['cases'][0]['chi_square']['threshold'],15.08627246938899,abs_tol=1e-8)
assert cyber['trusted_recovery']['chi_square']['degrees_of_freedom']==0
control=cyber['trusted_recovery']['control']
assert math.isclose(control['flexible_injection_pu'],.12169366726390399,abs_tol=1e-8)
assert math.isclose(control['actual_toy_model_flows_pu'][1],.17046076156,abs_tol=1e-8)
assert control['actual_violation_count']==0
report={'status':'passed','purpose':'Consistency check of the existing synthetic fixtures; not a new aggregate agent-performance study.',
        'restoration':rows,'cyber':{'nominal_J':cyber['cases'][0]['chi_square']['statistic'],'stealth_J':cyber['cases'][2]['chi_square']['statistic'],
            'threshold':cyber['cases'][0]['chi_square']['threshold'],'recovery_u_pu':control['flexible_injection_pu'],
            'offline_actual_flow12_pu':control['actual_toy_model_flows_pu'][1]}}
(ROOT/'research/numerical_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
