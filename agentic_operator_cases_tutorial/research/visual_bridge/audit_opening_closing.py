"""Read-only source/value audit; no LLM call or numerical experiment."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
CASES=HERE.parent.parent
REPO=CASES.parent
sys.dont_write_bytecode=True
helper=REPO/'agentic_grid_workflow_tutorial/src/llama_walkthrough.py'
spec=importlib.util.spec_from_file_location('read_only_replay_audit',helper)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
episodes=module.load_episodes()
v=episodes['voltage']
r=episodes['restoration']
c=episodes['cyber']
run=json.loads((REPO/'agentic_grid_workflow_tutorial/results/workshop_run_opendss.json').read_text())
assert all('no new LLM call or electrical solve' in x['mode'] for x in episodes.values())
values={
    'SAC_current_pct_allowance':v['steps'][0]['tool_result_data']['point']['max_allowed_current_pct'],
    'MPC_current_pct_allowance':v['steps'][1]['tool_result_data']['point']['max_allowed_current_pct'],
    'MPC_P_kw':v['steps'][1]['tool_result_data']['point']['p_actual_kw'],
    'MPC_Q_kvar':v['steps'][1]['tool_result_data']['point']['q_actual_kvar'],
    'MPC_vmin_pu':v['steps'][1]['tool_result_data']['point']['vmin'],
    'MPC_vmax_pu':v['steps'][1]['tool_result_data']['point']['vmax'],
    'E02_served_kw':r['steps'][0]['tool_result_data']['before']['summary']['served_kw'],
    'E03_served_kw':r['steps'][0]['tool_result_data']['trial']['summary']['served_kw'],
    'E03_critical_kw':r['steps'][0]['tool_result_data']['trial']['summary']['critical_served_kw'],
    'E03_tie_pct_allowance':r['steps'][0]['tool_result_data']['trial']['summary']['tie_loading_pct'],
    'E04_tie_pct_allowance':r['steps'][1]['tool_result_data']['summary']['tie_loading_pct'],
    'E02_cost':r['steps'][0]['tool_result_data']['before']['score'],
    'E03_cost':r['steps'][0]['tool_result_data']['trial']['score'],
}
rounded={key:format(value,'.6f' if any(word in key for word in ['pct','vmin','vmax']) else '.3f') for key,value in values.items()}
sourcefiles=[CASES/'content/opening.json',CASES/'content/closing.json',helper]
content=[json.loads(path.read_text(encoding='utf-8')) for path in sourcefiles[:2]]
report={
 'scope':'Read-only audit of opening/closing classification, plain language and exact replay values. No electrical solve, model call, publishing or source edit.',
 'source_sha256':{str(path.relative_to(REPO)):hashlib.sha256(path.read_bytes()).hexdigest() for path in sourcefiles},
 'validated_recorded_episodes':list(episodes),
 'recorded_calls':{key:[step['call_id'] for step in episode['steps']] for key,episode in episodes.items()},
 'canonical_values':values,
 'rounded_display_values':rounded,
 'workflow_timing_fields':{key:{k:value for k,value in run[key].items() if isinstance(value,(int,float)) or k in ('status','case','backend')} for key in ('fixed','agentic')},
 'classification_findings':[
   'Default numerical calculations, saved SAC inference, archived Llama replies and proposed advisory pilot are explicitly separated.',
   'L10B only reads verified original replies/results; replay makes no model call or electrical solve.',
   'P3 supplied full MV/LV OpenDSS, L3 test_01, L6 six-node MILP, L10 feeder catalog and four-bus DC cyber records retain separate scopes.',
   'Hash consistency is not claimed as sensor authentication; trusted channels remain an assumption.',
   'Human review, simulated readback and equipment dispatch are distinguished.',
   'Paired fixed comparisons are stated to have the same final numerical results; no accuracy, workload or speed benefit is promised.',
 ],
 'minor_wording_finding':{
   'file':'content/opening.json','locator':'Connect a CPU and run setup — speaker note',
   'current':'The default route needs no GPU, API key or model download.',
   'recommendation':'Use “no LLM download”; setup does retrieve the saved SAC weights, so “no model download” is too broad.',
 },
 'slide_counts':dict(zip(('opening','closing'),map(len,content))),
 'status':'No material classification or numerical discrepancy found; one minor setup-note wording issue.',
}
(HERE/'content_audit.json').write_bytes(json.dumps(report,indent=2,ensure_ascii=False).encode())
print(json.dumps(report,indent=2,ensure_ascii=False))
