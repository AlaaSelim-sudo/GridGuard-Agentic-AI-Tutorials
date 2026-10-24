"""Put Stanford concepts and their Colab connections before notebook setup."""
from pathlib import Path
import copy,json,subprocess
ROOT=Path(__file__).resolve().parents[2]
BASE='f1473be5d85f3da8a7b1eab87c189eda086610a0'
URL='https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf'
COLAB='https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb'
def original(module):return json.loads(subprocess.check_output(['git','show',BASE+':agentic_operator_cases_tutorial/content/'+module+'.json'],cwd=ROOT).decode('utf-8-sig'))
def dump(p,v):(ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def take(slides,title):return copy.deepcopy(next(s for s in slides if s['title']==title))
def bridge(title,id,label,page,point,caption,note,refs):
 return dict(title=title,kind='diagram',diagram=id,minutes=1.5,points=[point],caption=caption,note=note,refs=refs,
  source_label=f'Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.{page}; Classroom Labs {label}.',
  notebook_url=COLAB,lab_label=label,hands_on=False,eyebrow='Stanford idea / Colab preview: '+label,
  visual_height_px=340,visual_height_cm=3.8,teaching_bridge=True)
o,v,r,c,end=[original(m) for m in ['opening','voltage','restoration','cyber','closing']]
wiki=take(end,'Stanford example: check before you write');wiki['minutes']=1.25
wiki['note']+=' This source figure is now in the opening. Spend about one minute on the check-before-writing idea. The next slide maps it to L2; do not run a cell yet.'
genie=take(end,'Stanford example: tools need clear rules');genie['minutes']=1.25
language=take(c,'Stanford: language and decision checks');language['minutes']=1.25
language['note']=language['note'].replace('Keep the previously calculated HOLD/PROPOSE outcomes tied to their stated numerical model and trusted-data assumption.', 'Preview the HOLD/PROPOSE distinction now; participants will calculate the L9 outcomes later with their stated model and trusted-data assumption.')
questions=take(end,'Ask four questions about a study result');questions['minutes']=1.25
questions['note']+=' This closes the twelve-minute opening concept block. Point out that all three labs will use these questions; participants do not need to memorize a framework or run ahead.'
voltage_bridge=bridge('Voltage: a proposal needs a numerical check','stanford_colab_voltage','L2',19,
 'L2 lets you test the numerical check. The saved L10B episode shows Llama choosing the next tool.',
 'Our grid adaptation of WikiChat’s checking habit. L2 calls Python directly; L10B replays saved Llama choices.',
 'Connect the preceding original WikiChat figure to a grid claim. A text answer might say that a proposed plan fits the limits; a numerical tool must calculate the supporting result. The reference bar is the default L2 MPC result: maximum allowed-current utilization 73.619901%, rounded to 73.62%, at LOAD_SCALE=1.0 and RATING_FRACTION=0.80. It passes this current allowance; modeled voltage and required model coverage must also be checked. The default medium-voltage calculation is not proof for the full MV/LV system. This visual previews the lab; do not run L2 before setup, L0 and L1. L2 calls numerical functions directly. The separate P3 L10B archive later shows Llama requesting a check, reading a failed result and selecting a fallback. Our application is an analogy to evidence checking, not a claim that the notebook runs WikiChat.',
 ['ST01','ST02','H02','LR0'])
restoration_bridge=bridge('Restoration: the service goal shapes the plan','stanford_colab_restoration','L6',40,
 'An agent must keep the stated service goal. L6 lets you see how that goal changes the plan.',
 'Our grid adaptation of explicit task rules. L6 uses the same 40 kW varied tie and 100 kW fixed tie for both goals.',
 'The preceding Genie excerpt motivates writing down the task and its rules before calling a function. In L6 the goal is part of the optimization problem: priority weighting serves 130 total kW, including 90 critical kW; maximizing total service gives 140 total kW, including 30 critical kW. The 40 kW limit belongs to one varied tie, while another tie stays fixed at 100 kW. Totals also include the 40 kW load at node 1 upstream of those ties. A 40 kW varied-tie limit is not a cap on total system service. Each stacked bar uses the same scale. Critical service is cyan; other service is blue. Ask which goal better matches an illustrative request to prioritize a hospital. The numerical model uses abstract critical loads, not an actual hospital dataset. Later learners run both goals and change the tie capacity. L6 is a direct Python calculation, not a live LLM agent. An agent coordinating such a study must preserve the requested goal and explain the returned tradeoff. The separate L10B feeder-catalog archive supplies actual saved Llama choices; it differs from this six-node L6 model. Our notebook does not implement Genie Worksheets.',
 ['ST01','ST03','H06','LR0'])
cyber_bridge=bridge('Cyber: a clear answer still needs evidence','stanford_colab_cyber','L8–L9',53,
 'L8 tests whether readings can look consistent but be wrong. L9 adds a trust assumption and recovery checks.',
 'Our grid adaptation of separating language from checks. The fixed L9 example returns HOLD or PROPOSE under stated assumptions.',
 'Relate the original Stanford clinical example to this lab without importing a formal guarantee. L8 fits readings to a four-bus DC model using WLS, weighted least squares. Its small residual is a measure of fit, not proof of sensor truth; the known simulation truth is used only for teaching error comparisons. L9 is a separate fixed recovery fixture. Without trusted replacement data it returns HOLD. With three additional readings assumed trusted and a successful modeled recovery check, it returns PROPOSE. The yes branch depicts this fixed example with passing numerical checks; a real study also needs every required check to pass. The calculation does not authenticate the extra readings. Later learners run L8, vary the attack scale, then reset before the independent L9 example. Python performs these calculations now. A coordinating agent should request evidence and retain HOLD when a required premise is missing; saved L10B replies show a separate recorded cyber case. Our code uses numerical checks, not the Stanford SMT/MaxSAT runtime.',
 ['ST01','H08','H09','LR0'])
# Keep the concept block to twelve minutes, followed by seven minutes of setup.
o[0]['note']='Open the one required Classroom Labs notebook. This hands-on workshop uses 80 slides and 180 teaching minutes, with breaks outside that total. Start with a twelve-minute Stanford concept block: show each original source figure, then its simple grid adaptation. The next seven minutes prepare Colab and run L0–L1. Learners calculate fresh numerical results and inspect separately labeled saved Llama replies. No default cell calls an LLM or operates equipment. Keep the notebook in order and run L10B only after L10. Work in pairs and use the six-page participant guide. Presenter affiliations were supplied by the presenters. The IEEE ComSoc theme is an independent educational adaptation.'
o[2]['caption']='Original Stanford lecture excerpt, p.2. Next, connect tool use to evidence, task rules and decision checks.'
o[2]['note']=o[2]['note'].replace('The next slide supplies a real recorded grid example.', 'The following source-and-lab pairs show why tool results, explicit goals and checked evidence matter in each case.')
opening=[o[0],o[1],o[2],wiki,voltage_bridge,genie,restoration_bridge,language,cyber_bridge,questions]+o[5:]
assert len(opening)==15 and sum(s['minutes'] for s in opening[:10])==12 and sum(s['minutes'] for s in opening)==19
# Reuse the former case checkpoint slots for the three opening application visuals.
trace=o[3];trace['eyebrow']='Recorded P3 example / separate from the L2 calculation'
trace['note']+=' This recorded example now follows the MPC/SAC definition slide in the voltage case, after Colab setup. It remains a preview; run the complete episode in L10B later.'
voltage=v[:2]+[trace]+v[2:-1]
restoration=r[:-1]
cyber=[s for s in c[:-1] if s['title']!='Stanford: language and decision checks']
for module in [voltage,restoration,cyber]:
 checkpoint={'voltage':v[-1],'restoration':r[-1],'cyber':c[-1]}[('voltage' if module is voltage else 'restoration' if module is restoration else 'cyber')]
 module[-1]['note']+=' End-of-case partner check: '+ ' '.join(checkpoint['points'])+' '+checkpoint['note']
# Put role reminders beside the proposed control-room pilot, after the readback.
closing=[s for s in end if s['title'] not in [wiki['title'],genie['title'],questions['title']]]
roles=o[4];roles['note']+=' This role reminder now introduces the closing advisory-pilot discussion, after the L12 readback.'
insert=next(i for i,s in enumerate(closing) if s.get('diagram')=='ops_request_snapshot');closing.insert(insert,roles)
# Time released by concise source explanations goes to experiment discussion and replay inspection.
for module,title in [(voltage,'Change one number and explain the difference'),(restoration,'Debrief: the tradeoff disappears here'),(cyber,'Debrief: no alarm does not prove truth')]:
 next(s for s in module if s['title']==title)['minutes']+=1
walk=next(s for s in closing if s.get('notebook_cell',{}).get('id')=='classroom-llama-walkthrough');walk['minutes']+=3
walk['note']+=' Allow about two minutes per scenario: one partner identifies the model choice, the other finds its tool result and the unresolved operator decision. These additional minutes replace removed checkpoint slides and the longer source explanations.'
modules=dict(opening=opening,voltage=voltage,restoration=restoration,cyber=cyber,closing=closing)
slides=[s for rows in modules.values() for s in rows]
assert len(slides)==80 and sum(s['minutes'] for s in slides)==180
assert len([s for s in slides if s['kind']=='exercise'])==3 and all(s['minutes']==4 for s in slides if s['kind']=='exercise')
for m,rows in modules.items():dump('content/'+m+'.json',rows)
manifest=dict(edition='stanford-first-colab-connections',main_slides=80,minutes=180,
 opening_slides=15,opening_minutes=19,stanford_concept_slides=10,stanford_concept_minutes=12,colab_setup_minutes=7,
 exercise_slides=[i for i,s in enumerate(slides,1) if s['kind']=='exercise'],
 module_schedule=[dict(module=m,slides=len(rows),minutes=sum(s['minutes'] for s in rows)) for m,rows in modules.items()],
 stanford_original_excerpt_pages=[2,19,40,53],stanford_original_excerpt_slides=[3,4,6,8],stanford_accountability_slide=10,
 stanford_colab_connection_slides=[5,7,9],intro_diagrams=[s['diagram'] for s in opening if s.get('diagram')],
 recorded_llama_preview_slides=[i for i,s in enumerate(slides,1) if s.get('replay_preview')],
 recorded_llama_execution_slide=next(i for i,s in enumerate(slides,1) if s.get('notebook_cell',{}).get('id')=='classroom-llama-walkthrough'),
 proposed_pilot_slides=[i for i,s in enumerate(slides,1) if str(s.get('diagram','')).startswith('ops_')],
 revision_detail='research/stanford_colab_bridge/revision_map.json')
dump('content/expansion_manifest.json',manifest)
dump('research/stanford_colab_bridge/revision_map.json',dict(baseline_commit=BASE,request='Move Stanford concepts to the beginning and use simple visuals to connect them to the three Colab cases.',
 concept_block='Slides 1–10 / 12 minutes. Each source figure is followed by a grid application. Slides 11–15 / 7 minutes prepare Colab and run L0–L1.',
 original_source_figure_moves={'WikiChat':'70 to 4','Genie Worksheets':'71 to 6','Language and decision checks':'64 to 8','Accountability questions':'72 to 10'},
 teaching_aids={'5':'Voltage / L2 evidence check','7':'Restoration / L6 service goal','9':'Cyber / L8–L9 fit, trust and checks'},
 reused_slots='Former case checkpoints become the three opening applications. Their discussion prompts remain in the final case notes.',
 other_moves='The recorded P3 trace follows the controller definitions in voltage. The role reminder now precedes the closing pilot.',
 timing='Six minutes released by shorter source explanations and checkpoint integration go to three case debriefs and L10B replay practice.',
 preserved='80 slides, 180 minutes, 13 exact notebook excerpts, 3 four-minute exercises, source images/credits and the unchanged canonical notebook.',
 final_manifest=manifest))
print(json.dumps(manifest,indent=2))
if __name__=='__main__':pass
