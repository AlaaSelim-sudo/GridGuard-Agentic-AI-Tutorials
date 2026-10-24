"""Revise the 80-slide baseline: show a real agentic loop before notebook setup."""
from pathlib import Path
import copy,json,subprocess
ROOT=Path(__file__).resolve().parents[2]
BASELINE='f65c30e86afc593cb0637bb233952e3991a9ba4d'
def original(module):
 data=subprocess.check_output(['git','show',BASELINE+':agentic_operator_cases_tutorial/content/'+module+'.json'],cwd=ROOT)
 return json.loads(data.decode('utf-8-sig'))
def dump(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
o,v,r,c,end=[original(m) for m in ['opening','voltage','restoration','cyber','closing']]

def diagram(s,title,id,points,minutes,caption,note,refs):
 s=copy.deepcopy(s)
 for key in ['notebook_cell','image_source_path','image_source_url','image_credit','image_asset_type','image_transformation']:
  s.pop(key,None)
 s.update(title=title,kind='diagram',diagram=id,points=points,minutes=minutes,caption=caption,note=note,refs=refs,
          visual_height_px=350,visual_height_cm=3.9)
 s.pop('source_label',None)
 return s

# The first five slides teach the concept in five minutes, using a real trace.
cover=copy.deepcopy(o[0]);cover['note']+=' The first five slides take five minutes and make the agentic loop explicit before setup. The opening as a whole takes 12 minutes. Case-level replay slides preview saved examples; learners run L10B later in the guided notebook order.'
goal=diagram(o[1],'What is agentic AI?','agent_goal_loop',
 ['An LLM agent works toward a goal by choosing tools, reading their results and choosing what to do next.'],1,
 'A bounded agentic loop. In this workshop, Llama choices are recorded; Python calculations can run now.',
 'Use the architectural definition in Anthropic, Building effective agents: an agent lets the LLM direct its process and tool use. Agentic AI is a broad term; here it means a system organized around this bounded loop. An AI agent is the component that chooses and follows steps. A tool is a permitted software function that returns a result. Point to the goal, model choice, executable tool, returned evidence and feedback arrow. The application stores case facts and prior results as the context supplied at the next model request. If a required check is missing, the outcome remains HOLD. Stop or return a proposal only under the fixed workflow rules. Do not imply that feedback alone establishes agency: conventional programs can also branch and loop. Our default notebook calculates engineering results now but replays the actual old Llama choices. No live model service is needed.',
 ['DEF03','LR0'])
contrast=diagram(o[2],'From a text answer to a tool loop','agent_text_tool',
 ['The key change: the model chooses a permitted next step using the result returned by a tool.'],1,
 'Two interaction patterns. Tools and feedback can also be used in ordinary software.',
 'Trace the first row once, then follow the lower feedback arrow. In the text-only interaction the immediate product is a reply. In the illustrated agentic interaction the model can request a calculation, read its returned facts and select another allowed action. A chatbot may itself contain such an agent; the interface name does not determine the architecture. A fixed program can branch, retry and optimize too. The narrow feature in the recorded examples is that Llama selects among an explicitly permitted set of next actions. The wrappers validate its JSON and then call functions; they do not execute arbitrary generated code. This is bounded model choice, not unrestricted control or a claim of superior numerical results.',
 ['DEF03','LR0'])
trace=diagram(o[3],'A real agent changes its next step','agent_recorded_trace',
 ['The failed tool result leads to a fallback check. Passing the checks still leaves human review.'],1.5,
 'Recorded P3 example, separate from L2. 111.966607% and 99.604410% are rounded here.',
 'This is an actual saved Llama 3.1:8b voltage episode, not a fabricated interactive exchange. Call 1 selects VERIFY_SAC_FIRST; the numerical check returns 111.966607 percent of allowed current and two current violations. Call 2 selects USE_MPC_PLAN; its numerical check returns 99.604410 percent of allowed current and no recorded violations. The SAC and MPC tools already exist; Llama does not invent or solve the power flow. The arrows show tool-request, result, next-request, result. Call 3 selects REVIEW_EVIDENCE. Human acknowledgment remains PENDING and equipment_dispatch is False. This separate P3 MV/LV OpenDSS archive differs from the fresh L2 exercise and from L3 test_01. Later voltage slides display the exact public returned reasons; learners can replay the source in L10B after completing the three cases. The fixed comparator reaches the same numerical outcome, so the trace illustrates coordination rather than a proven performance improvement.',
 ['LRV','LR0'])
roles=diagram(o[16],'Llama chooses; tools calculate; people decide','agent_roles_simple',
 ['The agent coordinates a study. Numerical tools supply the checks. The operator reviews the proposal.'],1,
 'Default class route: new numerical results plus saved Llama replies. No equipment commands.',
 'Use the three symbols to assign responsibilities: the speech box is Llama making a permitted choice and returning a public reason; the function is Python and OpenDSS calculating physical results and enforcing workflow limits; the person is the operator reviewing evidence and retaining operating authority. The Llama wrappers use constrained JSON interpreted by the application, rather than native tool_calls. Language explanations are not proof of physical correctness. In our replay the model may say REVIEW but the human acknowledgment is still PENDING. For each exercise work in pairs: one person runs while the other checks, then swap. Save the input, result, check and next decision.',
 ['DEF03','LR0','OLL1'])
setup=[copy.deepcopy(o[i]) for i in [11,12,13,14,15]]
for s,t in zip(setup,[1,1.5,1.5,1,2]):s['minutes']=t
opening=[cover,goal,contrast,trace,roles]+setup
assert len(opening)==10 and sum(s['minutes'] for s in opening)==12

# Teach terms where the audience uses them, rather than as an opening glossary.
controllers=diagram(o[8],'MPC plans; SAC proposes','agent_mpc_sac',
 ['Both tools propose control settings. The same numerical check tests their voltage and current limits.'],1.5,
 'MPC: model predictive control. SAC: Soft Actor–Critic. These are control tools inside the larger workflow.',
 'MPC uses a model and a short forecast to optimize a plan; this lab applies its first action. SAC is a saved policy learned through reinforcement learning; it produces a new control proposal using old weights, without training again. Neither is the coordinating LLM. The outer agent can choose which permitted study to request. L2 calls both tools directly and displays their checks; this cell alone is not a live LLM agent. Later recorded P3 figures illustrate Llama coordinating the existing tools. Define per unit when the control-limit slide introduces the voltage scale: 1.0 p.u. is the stated base value. Explain MILP and WLS only in their respective cases.',
 ['H02','VMPC','VSAC','LRV'])
python_tool=diagram(o[10],'A tool is a Python function in this lab','agent_python_tool',
 ['A tool takes defined inputs and returns evidence. The notebook lets you see both.'],1.5,
 'L2 calls lab.voltage_lab(LOAD_SCALE, RATING_FRACTION) directly. Recorded agent coordination is separate.',
 'Find the actual function call on the next slide. The first two cell lines set the load scale and current allowance; the helper returns numerical proposals, checks and a table for plotting. A tool can be an optimizer, simulator, estimator, lookup or evidence checker. It is not the LLM itself. The student initiates this direct function call with the play button. In the separate recorded workflow Llama selects a named action, the Python application validates that action and its inputs, then invokes a permitted numerical function. Do not claim that the L2 helper uses a live agent gateway. Saving a notebook is separate from keeping a runtime: after a reset, rerun setup and earlier cells.',
 ['H02','LR0'])
rule=copy.deepcopy(o[5])
modes=copy.deepcopy(o[9]);modes['title']='What runs now and what was recorded';modes['points']=[
 'The current cell calculates new results. The saved Llama reply keeps its original inputs.',
 'Changing your lab input does not rewrite the recorded agent study.']
modes['note']+=' This slide comes just before L3 so the distinction is applied immediately.'
replays={m:[] for m in ['voltage','restoration','cyber']}
for s in end:
 if not s.get('replay_scenario'):continue
 s=copy.deepcopy(s);m=s['replay_scenario']
 s['hands_on']=False;s['replay_preview']=True;s['visual_height_cm']=4.4
 s['eyebrow']='Recorded agent example · '+{'voltage':'separate P3 study','restoration':'separate feeder study','cyber':'separate recovery study'}[m]
 s['caption']='Saved '+m+' example; separate from this case’s fresh calculation. Replay it in L10B later.'
 s['note']+=' This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.'
 replays[m].append(s)
v[3]['minutes']+=1;r[3]['minutes']+=1;c[3]['minutes']+=1
voltage=v[:1]+[controllers]+v[1:2]+[python_tool]+v[2:5]+[rule]+v[5:8]+[modes]+v[8:-1]+replays['voltage']+v[-1:]
restoration=r[:-1]+replays['restoration']+r[-1:]
cyber=c[:-1]+replays['cyber']+c[-1:]
voltage[-1]['note']+=' The three P3 previews are an additional separate archive. Contrast their saved Llama decisions with your current direct function calls.'
for m,case in [('restoration',restoration),('cyber',cyber)]:
 case[-1]['note']+=' Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.'
# Consolidate replay execution and reliability lessons after the three hands-on cases.
walk=copy.deepcopy(end[1]);walk['minutes']+=1
walk['note']=walk['note'].replace('The following slides show selected fields from the same replay.','Earlier case slides previewed selected fields from these replays. Now inspect the full episodes in the same notebook.')
walk['points']=['Now replay the three saved episodes: set SCENARIO to voltage, restoration and cyber, rerunning each time.']
closing=[end[0],walk,copy.deepcopy(o[4]),copy.deepcopy(o[6]),copy.deepcopy(o[7])]+end[10:]
modules=dict(opening=opening,voltage=voltage,restoration=restoration,cyber=cyber,closing=closing)
allslides=[s for rows in modules.values() for s in rows]
assert len(allslides)==80 and sum(s['minutes'] for s in allslides)==180
exercises=[i for i,s in enumerate(allslides,1) if s['kind']=='exercise']
assert len(exercises)==3 and all(s['minutes']==4 for s in allslides if s['kind']=='exercise')
for module,slides in modules.items():dump(ROOT/'content'/(module+'.json'),slides)
manifest=dict(edition='concrete-agentic-opening',main_slides=80,minutes=180,
 first_five_slides_minutes=5,opening_slides=10,opening_minutes=12,
 exercise_slides=exercises,module_schedule=[dict(module=m,slides=len(rows),minutes=sum(s['minutes'] for s in rows)) for m,rows in modules.items()],
 stanford_original_excerpt_pages=[19,40],stanford_review_question_source_pages=[52,53],
 intro_diagrams=[s['diagram'] for s in opening if s.get('diagram')],
 recorded_llama_preview_slides=[i for i,s in enumerate(allslides,1) if s.get('replay_preview')],
 recorded_llama_execution_slide=next(i for i,s in enumerate(allslides,1) if s.get('notebook_cell',{}).get('id')=='classroom-llama-walkthrough'),
 proposed_pilot_slides=[i for i,s in enumerate(allslides,1) if str(s.get('diagram','')).startswith('ops_')],
 revision_detail='research/agentic_opening/revision_map.json')
dump(ROOT/'content/expansion_manifest.json',manifest)
dump(ROOT/'research/agentic_opening/revision_map.json',dict(
 baseline_commit=BASELINE,request='Make agentic AI explicit, use visual aids and be concise at the beginning.',
 changes=['Ten-slide, twelve-minute opening; first five slides teach the loop in five minutes.',
          'Goal, context, permitted model choice, numerical tool and result feedback drawn explicitly.',
          'A real P3 voltage failure leads to a fallback check; human acknowledgment stays pending.',
          'Eight unchanged recorded reply figures moved beside their matching cases as labeled previews.',
          'Controller definitions and tool-function concept placed beside the actual L2 code.',
          'Stanford source figures and accountability questions retained after hands-on cases.'],
 preserved=['80 slides, 180 minutes, three four-minute exercises and 13 exact code excerpts.',
            'One canonical notebook and its sequential L0–L12 route, including L10B after L10.',
            'Foundations tutorial, all original source credits, recorded reasons and numerical figures.'],
 schedule=manifest['module_schedule'],exercise_slides=exercises))
print(json.dumps(manifest,indent=2))
