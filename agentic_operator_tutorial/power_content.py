"""Integrated power-system tutorial: current deployments, research and agent workflows."""
from pathlib import Path
from copy import deepcopy
import json
import re

ROOT=Path(__file__).resolve().parent
RETAINED=json.loads((ROOT/'power_retained_content.json').read_text(encoding='utf-8'))
SLIDES=[]
def old(key,minutes=2,**changes):
    item=deepcopy(RETAINED[key]);item.update(minutes=minutes,**changes)
    item.pop('extension',None)
    return item
def make(title,points=(),minutes=2,refs=(),**extra):
    item=dict(title=title,points=list(points),minutes=minutes,refs=list(refs),kind='normal',
              note='',takeaway='',caption='')
    item.update(extra)
    return item
def add(*args,**kwargs):SLIDES.append(make(*args,**kwargs))
def take(key,minutes=2,**changes):SLIDES.append(old(key,minutes,**changes))

take('base_1',.5,points=['Power-sector deployments, engineering tools and measured research results',
    'One integrated teaching session · two worked exercises',
    'IEEE ComSoc theme · Evidence reviewed 17 October 2026'],
    note='All slides are part of the presentation. The opening separates named operational workflows, utility disclosures and product announcements. Every agent-research paper studied concerns a power-system task. LangGraph and dependency DAGs are explained through disturbance analysis and weather-risk studies. The separate follow-on workshop retains the detailed GridGuard voltage, restoration and cyber cases.')
add('The engineering question behind the news',[
    'Which part of a power-system task can an agent coordinate, and which result must come from a trusted tool?',
    'We will follow real deployment disclosures, inspect research workflows, then build a testable operator acceptance contract.'],minutes=1.5,
    note='The topic is the full engineering workflow. Treat a named deployment, an announced capability, a research demonstration and a controlled evaluation as different evidence. The cases ahead show input preparation, outage analysis and planning support before the tutorial examines numerical tool orchestration.')
add('April–June 2026: HyperQ enters PJM’s application workflow',[
    'Tapestry reports HyperQ deployed for PJM Cycle 1 on 29 April; PJM had confirmed testing in March.',
    'Gemini agents reconcile site-control agreements, parcels and tariff evidence; engineers make final determinations.',
    'This is application-readiness work before the downstream electrical study.'],refs=['N01','N02','N06'],
    eyebrow='United States · supplier-reported deployment and customer-confirmed testing',
    note='Tapestry’s June11 report describes811 generation applications. Agents perform bounded document and evidence tasks. This does not establish an agent making a power-flow conclusion or an automatic regulatory decision. The architecture uses guided orchestration and evidence citations; the article describes migration to Google ADK as future work, so the deployed system must not be labeled an established ADK implementation.',
    takeaway='The study depends on reliable evidence before the numerical solver starts.')
add('HyperQ: the reported computational workload',[
    'These are computational timings for 811 applications. Document-transfer latency and human validation are excluded.'],refs=['N01'],
    kind='figure',image='power_news_hyperq_dashboard.png',visual_height_cm=3.65,visual_height_px=335,
    caption='Original Tapestry performance graphic, June2026. Computational runtime is distinct from the full interconnection timeline.',
    note='The supplier describes4,581 raw site-control documents grouped into2,328 bundles and evaluated against four criteria. It does not publish a confusion matrix or accuracy denominator. The historical20x headline is an unmatched manual-versus-compute comparison and is not used here. Read each denominator literally; these are811 applications, not9,312 projects.')
take('base_13',2.5,title='2026 CAISO/OATI report: agents in daily outage review',
    main_ref='C02',
    points=['OATI’s AI Genie uses Workflow, Advisor and Recon agents with a shared orchestrator; operators retain final authority.',
            'The supplier reports 500+ next-day requests processed nightly in under eight minutes; request latency and reviewer effort are not supplied.'],
    note='California ISO’s July2025 customer account described a pilot; OATI’s2026 field report describes production daily use. The exact production start date is not supplied. Batch throughput exceeds62.5 requests/minute from the stated inequalities. Do not compare eight machine-minutes with a separate analyst-hours context as if this were a matched trial. The work prepares outage analysis and operating evidence; final decisions remain with reviewers.')
take('base_17',2.5,title='September 2026: Duke and AWS coordinate planning studies',
    note='AWS’s17September2026 announcement names Duke engineers using agentic study coordination. Agents prepare inputs and coordinate existing physics software, models and scripts. The reported change is data preparation from two weeks of manual work to hours, without an exact final-hour value or sample count. The public report does not identify an SDK, model or runtime; do not infer Strands or AgentCore from the cloud provider. Engineers own final decisions.')
add('May 2026: agentic PSS E capabilities are unveiled',[
    'Siemens’ Gridscale X announcement places agentic workflow automation around transmission-planning simulations.',
    'The target includes large-load and data-center connection studies, with integration through open APIs.',
    'This release is product evidence; it does not identify a production user of the newly unveiled agentic PSS E capabilities.'],refs=['N03'],
    eyebrow='Product announcement · 5 May2026',
    note='The release separately describes Alliander’s platform migration. That establishes platform adoption, not deployment of this newly unveiled agentic PSS E capability. The up-to50% study-response claim lacks a disclosed benchmark protocol and is not plotted. Use the announcement to identify a practical integration direction: an agent coordinates a trusted simulation environment.',
    takeaway='Platform integration, task scope and measured field outcomes need separate evidence.')
add('May 2026: National Grid reports agentic project assurance',[
    'A capital control tower already checks early project options and stage-gate documents, according to the results transcript.',
    'Project managers receive feedback while plans can still change.',
    'The group discloses neither an agent framework nor an agent-specific timing or accuracy result.'],refs=['N04'],
    eyebrow='Current-use disclosure · UK/US group; rollout geography unspecified',
    note='The14May2026 CEO transcript is evidence of agentic project-assurance use. Later remarks about access-outage optimization describe future plans. Nearby FLISR, outage-minute or gas-crew metrics must not be attributed to this agent. A useful case can verify adoption without supporting a numerical performance estimate.')
take('base_18',1.5,title='GE Vernova: the grid platform supporting integration',refs=['C07','I01'],
    points=['GridOS for Distribution at Alabama Power provides a named operational-platform example.',
            'Its shared grid-orchestration context helps explain where study tools and operator workflows can connect.',
            'The public disclosure does not isolate an agent-specific utility reliability result.'],
    caption='Official GridOS promotional composite. Platform deployment and agent-specific evaluation are distinct evidence.',
    note='Retain the requested GE example in its electric-power business. The February2026 GridOS disclosure is a platform announcement with a named utility context. It does not establish a specific autonomous LLM controller. The tutorial’s contribution is to show the additional tool, state, evidence and authority contracts required when agents are integrated into such workflows.')
take('base_3',2)
take('base_2',1.5)
take('base_5',1.5)
take('base_6',2,refs=['LG01','E01'])
take('base_7',1.5)
take('base_8',1.5)
take('base_9',1.5)
take('base_11',2)
take('base_12',6)

add('Power-system research asks different engineering questions',[
    'Fault analysis extracts events from recorded waveforms; simulation assistants configure and run studies.',
    'Control prototypes propose actions in modeled networks; benchmarks test evidence retrieval or numerical questions.',
    'A paper’s result transfers only with its task, tools, action space and evaluation distribution.'],minutes=1.5,refs=['D01','E02','E03','P02'],
    note='The following papers are all power-system applications. They measure different outcomes, so their percentages do not form a cross-paper ranking. Keep the numerical solver’s responsibility separate from the language model’s tool selection and interpretation.')
add('DrAgent: a recorded fault becomes a sequence of questions',[
    'Read the third current trace: the dashed markers locate inception, maximum fault current and clearance.'],refs=['D01'],
    kind='figure',image='power_dragent_waveform.png',visual_height_cm=4.15,visual_height_px=365,
    caption='Original DrAgent Figure2, PDF p.4: a sample disturbance record; the third current channel shows the fault.',
    note='The Hitachi Energy paper studies transmission-line disturbance analysis. The visual is an extracted original scientific figure, not a synthetic utility event or a live operating display. Read the curve change before discussing the architecture. A numerical extraction tool supplies a sample index or current measurement; interpreting its engineering meaning remains part of the task.')
add('DrAgent: a plan connects domain-specific tools',[
    'The paper implements a ReWOO-style plan with LangChain/LangGraph and Python tools for COMTRADE analysis.',
    'One tool’s evidence can supply a later argument; argument repair addresses syntax, while domain checks address meaning.'],refs=['D01','LG01'],
    excerpt=['Illustrative dependency from the paper’s task:',
             'inception_sample = find_fault_inception(record)',
             'inception_seconds = inception_sample / sampling_rate',
             'report uses timing plus measured current evidence'],
    note='The implementation names Gemini1.5Pro for planning, a dozen domain functions and RAG over138 product manuals. The code excerpt is simplified teaching notation. The architecture plans before executing evidence-dependent calls. It motivates the next DAG explanation: the time conversion cannot execute correctly before the sample index and sampling rate exist.')
add('DrAgent result: numerical tools help, but errors remain',[
    'These calculated counts treat expert scores of at least2 as correct, using the paper’s18 recorded cases.',
    'Clearance/timing remains weaker; its rubric also accepts correctly labeled fault duration.'],refs=['D01'],
    kind='figure',image='power_dragent_counts.png',visual_height_cm=3.9,visual_height_px=350,
    caption='Counts derived from TableIV and the Appendix; these are not new experiments or the paper’s mean-score metric.',
    note='Inception:12/18 baseline versus18/18 agent; maximum current:16/18 versus18/18; clearance/timing:4/18 versus13/18. The reported tolerance is3ms for timing and5% for current. One expert graded answers. Q6 footnote8 accepts correctly identified duration; do not claim strict clearance-timestamp accuracy. Its printed mean is inconsistent with the individual cells, so this figure uses audited cell counts.')

add('Three graphs describe different parts of the study',[
    'The physical network graph connects buses and electrical equipment.',
    'A task dependency graph connects calculations through the artifacts they consume.',
    'A LangGraph execution graph connects workflow steps through state and routing rules.'],refs=['D01','P03','LG01'],
    note='A radial feeder does not imply that its software workflow is acyclic. Conversely, a fixed calculation DAG can analyze a meshed power network. Name the graph before discussing a node, edge or loop. These distinctions prevent an architecture drawing from being mistaken for an electrical model.')
add('A DAG exposes the prerequisites of a calculation',[
    'DAG means directed acyclic graph: edges connect required artifacts to the tasks that consume them.',
    'Run independent branches when inputs exist; join after all required evidence arrives.'],refs=['D01'],
    diagram='power_fault_dag',kind='diagram',
    caption='Original teaching adaptation of DrAgent’s tool dependencies; it is not a reproduction of its exact execution graph.',
    note='A valid topological order places every predecessor before its consumer. The inception index and sampling rate must precede time conversion. The maximum-current computation can be independent of that conversion when both read the same immutable record. Parallelism follows declared dependencies, not the visual placement of boxes.')
add('LangGraph supports state and conditional cycles',[
    'Nodes read state and return updates; conditional edges can route execution back to an earlier node.',
    'Bound the repair loop, then finish with a success or unresolved status.'],refs=['LG01','D01','P03'],
    diagram='power_stateful_route',kind='diagram',
    caption='Original educational routing pattern, with an illustrative two-retry budget. It is not a paper’s exact source code.',
    note='LangGraph is a runtime framework rather than a synonym for DAG. StateGraph defines state channels and nodes; application-defined reducers determine how concurrent updates combine. A node can call a deterministic engineering tool or a model. The application defines validation, stopping and permission rules; graph execution alone cannot establish feasibility.')
add('State must identify the study being resumed',[
    'Store the case identity and input versions with evidence, status and the attempt count.',
    'Keep returned artifacts keyed by case or contingency ID so a parallel merge cannot hide a missing result.'],refs=['LG01','LG02'],
    excerpt=['case_id = C17; topology = v43; model = m7',
             'evidence = {outage_6:R1, outage_7:R2}',
             'expected = {outage_6, outage_7, outage_34}',
             'status = INCOMPLETE; attempts = 1'],
    note='These are invented state fields. They illustrate an application contract, not a built-in LangGraph power schema. The default update behavior is not a guarantee of complete evidence merging. Define and test the reducer or external artifact store so branch results remain identifiable and duplicates or missing outputs can be detected.',
    takeaway='State preserves evidence identity; the application establishes its validity.')
add('A checkpoint preserves state across a pause',[
    'A checkpointer persists execution state and thread_id identifies the workflow history.',
    'If topology changes before resumption, the application must invalidate affected results before relying on them.'],refs=['LG02','LG03'],
    diagram='power_checkpoint_revalidation',kind='diagram',
    caption='Illustrative topology versions and evidence IDs; checkpointing does not automatically establish freshness.',
    note='An interrupt can pause for external review and later resume with the same thread context. Current documentation says the interrupted node restarts from its beginning. Side effects before the interrupt can therefore repeat: design writes and tool operations with stable step IDs or other idempotency controls. This example grants no live grid-command permission.')
add('Parallel contingency studies need an explicit join',[
    'Each selected outage runs on a consistent copy of the same declared base case.',
    'A failed or missing result is an unresolved scenario; a join must compare returned IDs with the expected set.'],refs=['E01','R01','LG01'],
    diagram='power_contingency_join',kind='diagram',
    caption='Invented three-case teaching example. Numerical results are not calculated in this illustration.',
    note='The goal is complete evidence for the selected scope, not simply a count of finished software nodes. If C2 fails, the artifact should name C2, its failure and what remains unknown. This operationalizes AgentiGrid’s incomplete-coverage lesson without asserting that a successful selected-outage search exhausts N−1 contingencies.')

add('Feedback-driven simulation agents retrieve functions and options',[
    'The IEEE TSG framework separates function and parameter needs, retrieves toolbox knowledge, then generates MATLAB studies.',
    'Execution errors trigger retrieval and code repair; executable but wrong parameter choices may still pass through.'],refs=['E02'],
    excerpt=['Task requirements → function and option retrieval',
             'structured toolbox knowledge → MATLAB study code',
             'execution error → retrieve again and repair',
             'no exception → still check task requirements'],
    note='Jia, Cui and Hug evaluate DALINE and MATPOWER simulation tasks. The paper does not identify LangGraph as its implementation framework. Its control pattern can nevertheless be understood through stateful feedback. The engineering check must compare the executed study against the task’s requested options; an error-free MATLAB run is insufficient.')
add('Simulation-agent result: a graded score, not a pass fraction',[
    'The34-task DALINE score averages graded attempts and penalizes unnecessary settings;93.13 is not a binary pass rate.'],refs=['E02'],
    kind='figure',image='power_study_feedback.png',visual_height_cm=3.9,visual_height_px=350,
    caption='Reported DALINE scheme comparison, author preprint Figure8 / sectionV. Up to three attempts per task.',
    note='The rubric assigns100 for all requirements without irrelevant settings,50 when unnecessary settings remain, and0 when a requirement is unmet. Scores average over allowed attempt slots, repeating the last score in unused slots. The API schemes use gpt-4o-2024-05-13; the built-in ChatGPT-RAG scheme is a different product runtime. These are complete-package comparisons, not isolated causal effects. The corresponding MATPOWER full score is96.85 over35 tasks and a five-attempt budget.')
take('base_10',2.5)

add('X-GridAgent separates planning, coordination and tool actions',[
    'A planner decomposes a grid request; a coordinator routes work and preserves intermediate artifacts.',
    'Action agents call eight specialized MCP servers, with pandapower supplying numerical analyses.'],refs=['E01'],
    excerpt=['118-bus example: AC flow → numeric loading sort',
             'select line indices6,7,34 for outage studies',
             'initialize the declared case → execute each outage',
             'save numerical evidence → report selected-scope findings'],
    note='The services cover retrieval, power flow, OPF, contingency, short circuit, topology, editing and plotting. The paper does not name LangGraph or another open orchestration SDK. MCP supplies an interface; it does not implement the physics or guarantee that the right cases were selected. This top-three example is separate from the paper’s top-five query.')
add('X-GridAgent result: nonconvergence remains part of the answer',[
    'The39-bus AC OPF converges for the base case and outage. Doubled load produces no converged solution or objective.'],refs=['E01'],
    kind='figure',image='power_study_xgrid.png',visual_height_cm=3.9,visual_height_px=350,
    caption='X-GridAgent TableI, Q10. Objective units are unspecified; a failed solve is not a zero-cost solution.',
    note='The reported objective rises from41,872.3 to42,115.34 for line11 out of service, a difference of243.04 in the table’s objective units. The doubled-load AC OPF does not converge. The authors report100% success on their selected repeated-query evaluation against manually obtained conventional solutions; it does not establish random-task or live-utility reliability.')

take('gridmind2025_3',2)
take('gridmind2025_4',2)
take('power_5',2.5)
add('GridMind: changed inputs determine which stages rerun',[
    'Only k changes: rerun cascade. Forecast shifts by six hours: rerun all five stages.',
    'An ACOPF solver change reruns ACOPF only, under this implementation’s dependencies.'],refs=['P03'],
    diagram='power_gridmind_invalidation',kind='diagram',
    caption='Teaching rendering of the affected-stage sets reported in GridMind2026 Table1; no unreported dependency edges are assumed.',
    note='The five stages are line-wind, outages, ACOPF, contingency and cascade. The dependency structure is implementation-specific; contingency consumes outage schedules directly rather than requiring ACOPF output. An exact input reversion can reuse existing artifacts. Every relevant dependency must participate in artifact identity, or a cache can return an obsolete result.')
take('power_6',2.5)
add('Exercise2: revalidate a saved weather-risk workflow',[
    'A saved run uses forecast F0, topology v43 and cascade fan-out k=50. A new request changes only k to200: what reruns?',
    'A second request shifts the forecast by six hours. Which of the five cached stage outputs remain applicable?',
    'One required simulation fails. What status and evidence should the operator receive?'],minutes=8,kind='exercise',
    eyebrow='Active learning · 8 minutes · small groups',refs=['P03','LG02'],
    note='Use2 minutes individual annotation,2 minutes group comparison,2 minutes discussion and2 minutes debrief. For k-only change, rerun cascade and retain the other applicable outputs. A forecast-init shift changes the upstream input and reruns all five stages in the cited workflow. A failed required stage yields an incomplete or unresolved result with its case/stage ID, input versions, tool error and missing conclusions; it does not justify an all-clear report. The forecast and topology IDs are teaching labels. Do not generalize these exact dependencies to a different implementation.')

take('power_0',2.5)
take('power_1',2.5)
take('power_dsr',2.5,title='PowerAgentBench-Dyn also tests dynamic-security screening',
    points=['The screening task uses PowerMCP/PowerFactory to assess ten candidate faults and identify three critical cases.',
            'Six backends achieve0/10–10/10 full-workflow successes, covering execution, critical cases, instability and allowed mitigation.'],
    note='This is a different task from the model-quality test, and its Opus version is4.7 rather than4.8. TablesIII–VI report9/10 Opus4.7,9/10 Sonnet4.6,7/10 Haiku4.5,10/10 Gemini3.1Pro,10/10 GPT-5.5 and0/10 Qwen2.5-Coder-7B. Success means the full workflow completes, matches the offline critical-case reference, correctly flags L02–25 at160ms as unstable and evaluates only permitted synchronous-condenser mitigation options (sectionIV-C/TableIV). These counts do not measure fault selection alone. Do not pool counts across tasks or call them field reliability. A failure can concern tool execution before the engineering conclusion exists.')

add('Grid-Agent: modeled actions are validated in a sandbox',[
    'A topology agent identifies violations, a planner proposes structured actions, and an executor applies them to a sandbox.',
    'A validator reruns power flow, retains useful changes and rolls back unsuccessful modeled changes.'],refs=['E03'],
    excerpt=['Available examples: switch update, battery, curtailment',
             'copy case → apply proposed action → run power flow',
             'validate against declared violations',
             'keep modeled change or restore prior sandbox state'],
    note='The paper evaluates voltage, thermal and disconnected-bus violations. The numerical-solver brand and orchestration SDK are not specified in the inspected v3. A software rollback restores a simulation copy; it does not imply that physical switching is reversible or authorized. Each action’s physical semantics, limits and permissions need a separate implementation contract.')
add('Grid-Agent result: feasible repair needs a stated denominator',[
    'The paper reports44%–100% scenario-resolution rates across planners, but does not disclose the exact aggregate trial count.',
    'Formal optimality and comparison with a numerical optimizer remain future work in that study.'],refs=['E03'],
    callout='Resolved violations ≠ proved optimal control',
    note='Seven scenarios are named, but the repetition and aggregation protocol is insufficient to reconstruct successes/7 or confidence intervals. Four planner rows report100%, Flash-Lite63% and GPT-4.1-Nano44%. The CIGRE bus count differs between prose and a table, so it is not repeated as a precise figure here. The architectural idea is useful; the reporting limits prevent a broad reliability claim.',
    takeaway='Report the action set, constraints, scenario population and comparator with a control claim.')
add('VeraGrid-Agent: an answer points to solved output',[
    'The agent writes feeder inputs, runs VeraGrid AC OPF, inspects the result index and reads selected output lines.',
    'A bounded correction loop can repair tool errors before it returns a multiple-choice answer.'],refs=['E04','E04C'],
    excerpt=['isolated workspace for each benchmark question',
             'write JSON input → execute VeraGrid',
             'read result table of contents → select relevant rows',
             'choose answer or return unresolved within budget'],
    note='The benchmark uses a single balanced8-bus radial feeder,33 templates and150 questions split50/50/50 by difficulty. Ground truth comes from the same solver/circuit. The repository exposes a harness and recorded reports, but repository execution interfaces are not proof of an SDK used in the historical paper. Inspecting a solver output is different from learning a general feeder-control policy.')
add('VeraGrid-Agent result: computation changes matched-model answers',[
    'The150 questions share one frozen feeder; improved MCQ answers do not establish general dispatch or field performance.'],refs=['E04'],
    kind='figure',image='power_study_veragrid.png',visual_height_cm=3.9,visual_height_px=350,
    caption='VeraGrid-Agent TableI: selected same-model comparisons. Missing or malformed answers count as incorrect.',
    note='The no-tool condition receives feeder/DER information; the agent adds execution, reading and iterative feedback, so this is a system comparison rather than equal inference compute. The study supplies explicit numerators and denominators. Repeated-run uncertainty is not disclosed. Solver execution and correct interpretation can still fail separately; the paper records residual agent errors.')

take('base_20',2)
take('base_21',2)
take('base_22',2.5)
take('base_23',2.5)
take('power_2',2)
take('power_3',2)
take('power_4',2)
take('base_24',2)
take('base_25',2)
take('base_26',2.5)
take('base_27',2.5)
take('base_29',2,refs=['P01','P02','R02','E04'])
add('MCP connects tools to the workflow graph',[
    'X-GridAgent’s MCP servers expose specialized grid capabilities; the planner chooses and coordinates calls.',
    'LangGraph can orchestrate state and routing, while the called numerical service retains its engineering method.'],refs=['E01','LG01','T08','T09'],
    excerpt=['workflow node: assess_selected_outages(state)',
             'tool interface: network ID + outage IDs + parameters',
             'returned artifact: solver status + results + provenance'],
    note='MCP is an interoperability interface, not an agent planner or a power-flow model. A tool description should make the task scope and arguments clear. Authentication, permitted actions and semantic validation remain application responsibilities. No particular SDK is inferred for X-GridAgent from the existence of MCP servers.')
take('base_33',2,refs=['T09'],
    note='The malicious retrieved instruction is an invented teaching example. Treat returned documents as evidence rather than authority. A service gate should enforce allowed actions independently of the content it returns. Test whether hostile content changes case scope, attempts a forbidden call or contaminates a report, and preserve the rejected action and reason.')
take('base_37',2)
take('base_38',2)
take('base_39',1.5)
take('base_40',2)
take('base_41',1)
take('base_42',2,points=['Which power-system paper supplies the closest task and tool chain to your proposed application?',
    'Where must the operator see unresolved cases, changed inputs and authority limits?',
    'The full reading guide links original papers, deployment sources, documentation and editable visual data.'],
    note='Every slide has been part of one integrated session. Revisit the opening real-world workflows and ask participants to distinguish adoption evidence from engineering performance. The next tutorial applies these methods to voltage support, restoration and cyber response. Use the reading guide for complete sources and the instructor guide for both exercise answers.')

EXTRA_READING_REFS=['R03','R04','P01C','P02C','P03A','P03M','LG01','LG02','LG03','N02','N06','PA04']

# Small typography normalization without rewriting asset IDs or source keys.
from revision_content import integrate
SLIDES=integrate(SLIDES)

def human(text):
    text=re.sub(r"(?<=[’']s)(?=\d)",' ',text)
    text=re.sub(r';(?=\S)','; ',text)
    text=re.sub(r'%,(?=\S)','%, ',text)
    text=re.sub(r'\b([A-Za-z][a-z]{1,})(?=\d)',r'\1 ',text)
    text=re.sub(r'\b(GridMind|Exercise|Table|Figure)(?=\d)',r'\1 ',text)
    return text
for item in SLIDES:
    if item.get('image') in {'power_dragent_counts.png','power_study_xgrid.png','power_study_veragrid.png',
                             'rigor_r01_coverage.png','rigor_zero_failure_bound.png'}:
        item['visual_height_cm']=3.65
    for field in ('title','note','caption','eyebrow','takeaway','callout'):
        if field in item:item[field]=human(item[field])
    item['points']=[human(p) for p in item['points']]
    if 'excerpt' in item:item['excerpt']=[human(p) for p in item['excerpt']]
    item.pop('extension',None)

from visual_revision import revise
SLIDES=revise(SLIDES)
from real_image_revision import revise as add_source_images
SLIDES=add_source_images(SLIDES)
from platform_revision import revise as add_platform_demos
SLIDES=add_platform_demos(SLIDES)
from exercise_revision import revise as add_worked_answers
SLIDES=add_worked_answers(SLIDES)

assert len(SLIDES)<=80
assert sum(s['kind']=='exercise' for s in SLIDES)==2
assert not any(s.get('extension') for s in SLIDES)
assert not any(key.startswith(('F0','H0','H1')) for s in SLIDES for key in s['refs'])

# Presenter names and affiliations supplied for both tutorial title slides.
SLIDES[0]["presenters"] = [{'name': 'Alaa Selim', 'affiliation': 'MIT/Dartmouth'}, {'name': 'Mohamed Chehada', 'affiliation': 'UT Austin'}]
SLIDES[0]["points"] = ["Real power-sector uses, engineering tools and measured research results", "90 minutes / two worked exercises"]
