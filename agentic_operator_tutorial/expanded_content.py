"""Paper-based teaching edition. The 90-minute route precedes optional studies."""
from copy import deepcopy
from rigorous_content import SLIDES as BASE, EXTRA_READING_REFS as BASE_REFS

FOUNDATION=[]
SCIENCE=[]
POWER=[]
EXTENSION=[]
def slide(title, points=(), *, minutes=1.5, refs=(), **extra):
    result=dict(title=title,points=list(points),minutes=minutes,refs=list(refs),kind='normal',
                note='',takeaway='',caption='')
    result.update(extra)
    return result
def add(target,title,points=(),**kwargs):
    target.append(slide(title,points,**kwargs))

add(FOUNDATION,'ReAct: observations change the next tool call',[
    'The model interleaves task reasoning with actions and returned observations; the next action can depend on new evidence.',
    'In a utility adaptation, a missing asset ID triggers resolution before the measurement or solver call.'],refs=['F01'],
    excerpt=['Illustrative grid adaptation, not a paper experiment:',
             'resolve_asset("F12") → asset_id 447',
             'read_measurements(447) → quality STALE',
             'next action → request refreshed evidence'],
    note='ReAct is a prompting and interaction pattern, not a hosting service. The external observation changes the information available for the next step. The displayed grid example is invented and maps the method to the stale-data failure taught earlier. An explanation written after a fixed tool chain does not provide this adaptive interaction. The application still determines which calls are allowed. The paper and author code are linked in the reading guide.',
    takeaway='The central mechanism is feedback from the environment into action selection.')
add(FOUNDATION,'ReAct result: a controlled action-only comparison',[
    'On 500 WebShop test instructions, reported success rises from 30.1% to 40.0% with ReAct.',
    'This PaLM-540B experiment isolates the interaction pattern within that setup; it does not estimate grid-task reliability.'],refs=['F01'],
    kind='figure',image='expanded_foundation_react.png',
    caption='ReAct Table4: WebShop success, same PaLM-540B backbone. Author-reported rounded percentages.',
    note='The gain is9.9 percentage points, not9.9% relative improvement. WebShop is a simulated shopping environment; successful purchase completion differs from engineering feasibility. Neither rounded percentage should be converted into an exact integer count. The next methods modify different parts of the agent system, so their scores should not be ranked against this one.')
add(FOUNDATION,'Toolformer: learning when an API call is useful',[
    'Training inserts candidate API calls, executes them, and retains calls whose results improve prediction of subsequent text.',
    'The language model then learns call placement and arguments from this filtered data.'],refs=['F02'],
    excerpt=['Illustrative training example:',
             'candidate call: calculator("19 * 23") → 437',
             'compare continuation loss with and without the result',
             'retain useful examples → fine-tune the model'],
    note='Toolformer changes model training; ReAct changes the interaction context at inference. Calculator, search and other APIs supply information the model need not memorize. Loss improvement concerns token prediction, not compliance with a physical constraint. This invented arithmetic example explains the filter without claiming to reproduce a released training sample. Utilities still need validated engineering adapters and permission checks.',
    takeaway='A learned tool-use policy and a prompted tool-use policy require different training evidence.')
add(FOUNDATION,'Toolformer result: enabling calls on the same model',[
    'MAWPS first-number answer accuracy is15.0% with API calls disabled and44.0% with calls enabled for the same fine-tuned model.',
    'The table does not disclose an evaluated sample count; the experiment allows one API call per input.'],refs=['F02'],
    kind='figure',image='expanded_foundation_toolformer.png',
    caption='Toolformer Table3: MAWPS first-number answer accuracy, fine-tuned GPT-J; one call per input.',
    note='The paper checks the first number generated, except that when an equals sign appears it checks the first number after that sign. This is answer extraction, not full-solution correctness. It compares tool access within the same fine-tuned model. The evaluated item count is not disclosed in the table. The single-call arithmetic setting does not establish robust long-horizon planning or engineering validation.')
add(FOUNDATION,'Reflexion: memory changes the next attempt',[
    'After feedback, a reflection summarizes the previous failure and is stored as text for the next attempt.',
    'The retry uses this memory without a model-weight update. Incorrect feedback can preserve an incorrect lesson.'],refs=['F03'],
    excerpt=['Illustrative engineering adaptation:',
             'test feedback: reactive-load argument was omitted',
             'memory: verify both P and Q in request and cache key',
             'retry: reconstruct the request, then rerun the check'],
    note='The memory is part of the next prompt, not a learned guarantee. The worked cache defect shows why feedback must identify the real cause: the model can fix a request while an adapter still reuses a wrong result. A useful retry changes the failed condition and measures the new outcome. This is an invented adaptation, not a Reflexion utility deployment.',
    takeaway='Reflection is useful only when the feedback points toward a valid repair.')
add(FOUNDATION,'Reflexion result: reflection needs grounded feedback',[
    'On 50 difficult HumanEval Rust tasks, the full tests-plus-reflection setup reaches68%; reflection without tests reaches52%.',
    'The60% baseline makes this a useful counterexample to “self-critique always improves performance.”'],refs=['F03'],
    kind='figure',image='expanded_foundation_reflexion.png',
    caption='Reflexion Table3: selected50-task ablation. Success metric and retry setup belong to that experiment.',
    note='The selected50 Rust tasks yield baseline60%, reflection without tests52%, tests without reflection60%, and the complete system68%. Reported pass@1 scores one selected final program after internal tests and revisions; the baseline is one code-generation sample, so this does not hold compute constant. The91% Python headline is a different setting. In a utility adaptation, feedback must come from validated checks rather than confidence alone.')
add(FOUNDATION,'LATS: searching alternative trajectories within one task',[
    'Language Agent Tree Search branches over candidate continuations and uses feedback and reflection to direct further exploration.',
    'A search budget buys alternative trajectories; the reward or evaluator determines what the search favors.'],refs=['F04'],
    excerpt=['One task: identify an evidence-supported answer',
             'branch A → query a source → incomplete evidence',
             'branch B → query another source → candidate answer',
             'evaluate, revisit or expand branches within budget'],
    note='Unlike a single ReAct trajectory, LATS can revisit a partial trajectory and explore another continuation. The paper assumes the environment can revert to earlier states; use a simulator or reversible workspace when transferring this idea. More exploration increases model and tool calls. A mistaken evaluator can favor invalid answers. The simplified trace illustrates branching, not the exact paper algorithm.',
    takeaway='Search quality depends on both the branching policy and the validity of the evaluator.')
add(FOUNDATION,'LATS result: task score is not task success',[
    'On50 WebShop instructions with GPT-3.5, LATS reports75.9 task score versus64.2 for Reflexion.',
    'The score is100 × mean reward; it is not the percentage of fully successful shopping tasks.'],refs=['F04'],
    kind='figure',image='expanded_foundation_lats.png',
    caption='LATS Table6: WebShop task score, k=30. Separate protocol from the original ReAct comparison.',
    note='The11.7-point score difference uses partial-credit rewards. Original ReAct used500 instructions and PaLM-540B, so the two figures cannot produce a valid cross-paper ranking. In an engineering search, an objective score can also improve while a hard constraint remains violated; the acceptance contract must separate these quantities. Tool and inference costs belong in the comparison.')
add(FOUNDATION,'AFlow: searching the workflow before deployment',[
    'AFlow generates and revises executable workflows built from operations such as generation, testing and revision.',
    'Validation feedback selects a workflow offline; that selected workflow then handles held-out tasks.'],refs=['F05'],
    excerpt=['Workflow search: propose a program of model/tool operations',
             'evaluate candidate on validation tasks',
             'revise operators or control flow and evaluate again',
             'freeze the selected workflow → evaluate held-out tasks'],
    note='LATS searches a trajectory inside one task; AFlow searches the procedure used across tasks. The offline search can involve a more capable optimizer model and substantial evaluation cost. Report search and execution costs separately. In an engineering adaptation, validation cases used to tune a workflow must not become the final independent evaluation set.',
    takeaway='A workflow found by search needs a held-out test just as a manually designed workflow does.')
add(FOUNDATION,'AFlow result: the executor is held fixed',[
    'With GPT-4o-mini as executor, MBPP pass@1 is83.4% versus73.6% for the best tested manual baselines.',
    'The paper reports means over three evaluation runs; the evaluated MBPP item count is not disclosed in that table.'],refs=['F05'],
    kind='figure',image='expanded_foundation_aflow.png',
    caption='AFlow Table1: MBPP pass@1, mean of three evaluation runs; GPT-4o-mini executor.',
    note='CoT self-consistency, MedPrompt and MultiPersona tie at73.6%. The9.8-percentage-point comparison holds the executor model fixed but includes offline optimization. It does not establish dominance over every manual design. A utility adaptation needs a valid feasibility checker, a fixed action space and held-out cases. Report search costs separately from workflow execution.')

add(SCIENCE,'ToolUniverse result: tool access under a matched agent',[
    'DbQA improves by21.6 percentage points; SeqQA improves by5.2 points in the reported Claude Code comparison.',
    'The evaluation uses60 database questions and70 sequence questions; these are biomedical benchmark tasks.'],refs=['H02'],
    kind='figure',image='expanded_science_tooluniverse.png',
    caption='ToolUniverse v3, supplementary S8 / FigureS2. Same Claude Opus4.8 agent with and without ToolUniverse.',
    note='These reported point estimates support the usefulness of access to scientific tools for these tasks. They do not isolate the effect of each ToolUniverse module. The paper counts refusal or unparsable output as incorrect. Use the matched comparison to teach experimental design: retain the agent, model, questions and scoring while changing tool availability. Do not transfer its magnitude to a utility setting.')
add(SCIENCE,'TxAgent: specialized training plus retrieved tools',[
    'TxAgent combines a fine-tuned8B model, ToolRAG for capability retrieval, and211 biomedical tools.',
    'Tool retrieval selects a capability; execution returns source evidence that informs the next step.'],refs=['H07','H08'],
    excerpt=['Question → retrieve relevant tool descriptions',
             'select a typed tool and provide arguments',
             'execute tool → inspect returned evidence',
             'continue or answer with the source-grounded result'],
    note='The official project and code describe a specialized agent with a toolbox and retriever. This is a research system for therapeutic reasoning, not grid software. The utility analogy is a domain-specific tool catalog: selecting a simulator is distinct from choosing the network, units and constraints passed to it. Those choices still need an engineering acceptance contract. The2025 toolbox size is tied to that study, not the larger2026 ToolUniverse release.')
add(SCIENCE,'TxAgent result: a strong system-level comparison',[
    'The paper reports92.1% open-ended DrugPC accuracy on a3,168-question benchmark.',
    'The25.8-point advantage over GPT-4o compares complete systems with different training and tool access.'],refs=['H06'],
    kind='figure',image='expanded_science_txagent.png',
    caption='TxAgent v1 Results / Figure1d. DrugPC:3,168 questions; benchmark accuracy differs from clinical effectiveness.',
    note='Open-ended answers are generated without options, then mapped back to an original multiple-choice option for scoring (Methods5.2, PDF p.61). This is not direct semantic grading of free text. The complete-system comparison does not isolate size, training, retrieval or tools. The next slide uses a targeted ablation. Figure1d / Results PDF p.10 supply the overall numbers.')
add(SCIENCE,'TxAgent ablation: a plausible tool reply is insufficient',[
    'On multiple-choice DrugPC, actual tools score93.8%; model-generated imitations score72.7% and68.7%.',
    'The agent needs external evidence, not a fluent substitute for a database or simulator result.'],refs=['H06'],
    kind='figure',image='expanded_science_txagent_ablation.png',
    caption='TxAgent v1: Results p.17, Figure3c pp.27–28, Methods6.1 pp.61–62. Multiple-choice DrugPC.',
    note='The experiment replaces actual services with language models prompted to mimic them. In a utility adaptation, asking a language model to invent a power-flow output would likewise remove the numerical evidence the contract requires. This analogy is an inference for teaching; it is not a measured grid result. Real tools can also be wrong, so their inputs, numerical methods and returned status still require checks.')
add(SCIENCE,'POPPER result: power and false verification together',[
    'On DiscoveryBench, POPPER reports63.8% power and10.3% Type-I error at nominal alpha=10%.',
    'Whiskers show standard deviation across five runs; empirical averages do not replace the theorem’s assumptions.'],refs=['H09','H10'],
    kind='figure',image='expanded_science_popper.png',
    caption='POPPER Table3:86 non-null and86 constructed-null cases/run;5 runs, mean±SD. Nominal alpha=10%.',
    note='DiscoveryBench has86 non-null and86 constructed-null cases per run. Claude-Sonnet-3.5 uses at most three tests per hypothesis. Repeated runs do not create430 independent hypotheses. ReAct has lower power on non-null cases; removing relevance checks increases observed false verification. POPPER’s10.3% mean slightly exceeds nominal10%; the paper uses a within-one-SD empirical criterion. The formal guarantee requires conditional validity and logical relevance. Per-hypothesis Type-I control does not imply FDR control or a posterior probability that a validated claim is true.')
add(EXTENSION,'POPPER failure analysis: statistics can fail semantically',[
    'Among128 failed experiment logs,35.9% include p-value context errors and17.2% include broken logical implication.',
    'These are labels conditional on a failed experiment; one log can receive several labels.'],refs=['H10'],
    kind='figure',image='expanded_science_popper_failures.png',minutes=2,
    caption='POPPER AppendixD / Figure5: selected failure categories, automatically labeled and partly checked by humans.',
    note='The authors manually inspected20 logs to develop the taxonomy, used o1 to label128 failed logs and checked30 labeled logs with93.3% agreement. These percentages do not describe all system attempts. In a grid study, the parallel semantic failure is testing a convenient surrogate whose truth does not establish the requested engineering property. A correctly computed statistic can still answer the wrong question.')

add(POWER,'PowerAgentBench-Dyn: repair within an explicit action space',[
    'The Harvard-led benchmark gives the agent a modified solar-PV dynamic model and feedback from eight DMView/PSS/E quality tests.',
    'Only four REECAU1 controller gains may change; all other fields are locked, with at most five update attempts.'],refs=['P01','P01C'],
    excerpt=['Allowed fields: Kqp, Kqi, Kvp, Kvi',
             'run quality-test suite → inspect failed tests',
             'propose permitted gain update → rerun full suite',
             'success = all tests pass within budget and scope'],
    note='Harvard SEAS, Politecnico di Milano and UBITECH authors make the action boundary testable. This is model diagnosis and repair in a benchmark, not approval to change a utility controller. The initial modified model fails all eight tests. Four editable gains do not mean all other engineering properties have been validated. The author repository includes a harness and requires licensed PSS/E plus external DMView.',
    takeaway='A successful engineering agent satisfies the test suite and the allowed-edit contract.')
add(POWER,'PowerAgentBench-Dyn result: counts and update effort',[
    'Across ten independent sessions per model, compliant full-suite success is10/10,10/10 and9/10.',
    'Median update counts are1,1 and2; one corrupted model and small samples limit generalization.'],refs=['P01'],
    kind='figure',image='expanded_power_dynamic.png',
    caption='PowerAgentBench-Dyn TableII: dynamic-model-quality task. Other dynamic-study tasks use different models and criteria.',
    note='The three backends are Opus4.8, Sonnet4.6 and Haiku4.5. These are reported sessions on one modified WECC solar-PV model. No matched human or deterministic search baseline establishes a comparative speedup. Counts reveal both the sample and failures; an update count says something different from end-to-end operator time. The10/10 rows inherit the small-sample limitations explained later.')
add(POWER,'PowerBench: evidence retrieval across linked records',[
    'The300-question benchmark combines synthetic asset records, documents and telemetry; tools search, read files, read time series and execute Python.',
    'Each attempt has a50-tool-call and300-second retrieval/reasoning budget; physical power flow is outside its evaluated task.'],refs=['P02'],
    excerpt=['Illustrative evidence chain, not a benchmark question:',
             'resolve device clue → unique device record',
             'read linked maintenance document and telemetry',
             'compute required fields → return answer plus evidence'],
    note='An answer can be schema-valid yet use a wrong linked asset or time interval. This makes the benchmark relevant to control-room evidence work without claiming simulation or control capability. The three task families contain60,90 and150 questions. The paper reports generated datasets with761 devices and24,939 documents. At review, the linked public repository exposed only README and LICENSE; runnable release was not independently verified.',
    takeaway='Retrieving a relevant record is an intermediate result; the complete answer still needs checking.')
add(POWER,'PowerBench result: complete answers versus partial credit',[
    'The leading reported macro joint accuracy is74.2%[69.5,78.7]; overall field accuracy is82.7%[79.4,85.8].',
    'Joint accuracy requires a schema-valid answer with all required fields correct; field accuracy can reward an incomplete answer.'],refs=['P02'],
    kind='figure',image='expanded_power_benchmark.png',
    caption='PowerBench Table4: selected models, author-reported95% bootstrap intervals. Metrics use different aggregation rules.',
    note='The best row is GPT-5.6-Sol in this2026 paper snapshot. Macro joint accuracy equally averages the three task-family accuracies; it is not a correct-count divided by300. Overall field accuracy averages per-question field fractions. Marginal bootstrap intervals do not by themselves establish a significant paired difference. Synthetic evidence questions do not test physical-grid safety.')
add(POWER,'PowerBench: the difficult family is hidden by an average',[
    'For the leading row, family joint accuracies are85.0%,88.9% and48.7%.',
    'The equal-family average is74.2%; fewer than half of the Comparative Retrieval and Reasoning questions receive complete answers.'],refs=['P02'],
    math_tex=r'\[\operatorname{Macro\!\text{-}\!JA}=\frac{85.0+88.9+48.7}{3}=74.2\%\]',
    math_html='Macro-JA = (85.0 +88.9 +48.7) /3 =74.2%',
    note='Families have unequal sizes60,90 and150. Equal weighting makes the smallest family as influential as the largest. This is a deliberately defined metric, not a mistake; it answers a different question from pooled question accuracy. In a utility pilot, publish per-task results so a weak critical capability cannot disappear inside an overall average.',
    takeaway='Choose aggregation deliberately and inspect the task families that matter to the operator.')
add(POWER,'GridMind: dependency-aware reuse of scientific stages',[
    'The2026 weather-risk workflow uses LangGraph to coordinate weather, outage, OPF, screening and cascade-analysis stages.',
    'Content hashes identify reusable artifacts; a changed upstream forecast invalidates dependent stages.'],refs=['P03','P03A'],
    excerpt=['Reported seven-query session on synthetic Texas2000:',
             'increase cascade fan-out k → rerun cascade stage',
             'shift weather forecast by6 h → rerun all five stages',
             'exactly restore first inputs → reuse prior artifacts'],
    note='AERIS supplies weather, LUMINA or pandapower handles base OPF, a LUMINA surrogate screens, and EPFast provides reduced-order DC cascade simulation. The exact dependency graph matters: in this implementation the contingency stage consumes outage schedules directly, so changing ACOPF alone does not require rerunning every later-looking stage. Hashes establish identity of declared inputs, not correctness or unrecorded external freshness.',
    takeaway='Reuse is justified by explicit dependencies, not by asking whether a previous answer sounds relevant.')
add(POWER,'GridMind result: stage savings differ from time savings',[
    'Across the same seven queries, reuse reduces executed stages from35 to14 and wall time from1,432.6s to677.1s.',
    'That is60% fewer stages and a calculated2.12× session speedup, based on one reported ablation.'],refs=['P03'],
    kind='figure',image='expanded_power_gridmind.png',
    caption='GridMind2026 Table1: fresh-namespace reruns versus artifact reuse on a synthetic2,000-bus hurricane-risk workflow.',
    note='Do not call this60% less wall time: the measured reduction is about52.7%. Stages have different costs. The result combines workflow design and artifact reuse, not merely a faster language model. The single-session comparison provides no repeated-session confidence interval. Surrogate and reduced-order simulation results also need domain validation before a utility could use them.')

add(EXTENSION,'Dynamic security screening is a different benchmark task',[
    'PowerAgentBench-Dyn also asks agents to screen ten candidate faults and identify three critical cases through PowerMCP/PowerFactory.',
    'Reported success ranges from0/10 to10/10 across six backends; these outcomes cannot be pooled with dynamic-model repair.'],refs=['P01'],minutes=2,
    note='TablesIII–VI define a distinct Dynamic Security Risk Screening task and use Opus4.7, not the4.8 model-quality row. The reported counts are9/10 Opus4.7,9/10 Sonnet4.6,7/10 Haiku4.5,10/10 Gemini3.1Pro,10/10 GPT-5.5 and0/10 Qwen2.5-Coder-7B. Failures include simulator-tool execution. A count should retain the task, tools, configuration and success definition; it is not a vendor reliability ranking.',
    takeaway='A benchmark family contains distinct engineering tasks with distinct failure modes.')
add(EXTENSION,'GridMind2025: typed agents around numerical solvers',[
    'The earlier GridMind uses PydanticAI and pandapower for ACOPF and contingency work.',
    'It reports100% ACOPF success on case118 across six backends; this is a narrower claim than complete contingency discovery.'],refs=['P04'],minutes=2,
    note='The2025 paper tests14-,30-,118- and300-bus grids, with Figure3’s case118 success and execution-time comparison. The time distributions use five repetitions; do not invent a larger success denominator. This implementation differs from the2026 LangGraph weather workflow. Preserve the year and paper title when discussing either system.',
    takeaway='A numerical reference can establish one task’s result without validating every related task.')
add(EXTENSION,'GridMind2025: conflicting contingency conclusions',[
    'For case118, one backend reports a maximum-overload metric of165%; five others report137%, with different critical-line sets.',
    'The paper does not supply exhaustive contingency ground truth for that table; agreement alone cannot resolve correctness.'],refs=['P04'],minutes=2,
    excerpt=['Table1, IEEE118 contingency study:',
             'GPT-5 Mini → MaxOverload165%, set includes line9',
             'five other backends →137%, set includes line6',
             'required next evidence → independent exhaustive reference'],
    note='These are paper-reported interpretations and tool results, not a new experiment. Differences could arise from scope, enumeration or interpretation; the table does not establish which result is complete. The appropriate lesson is to request comparable case definitions and an independent reference. Do not infer that the majority is right or calculate a failure probability from six heterogeneous backend rows.')

EXTRA_READING_REFS=list(BASE_REFS)+['H04','H08','H11','P02C','P03M']

def original(number, minutes=None):
    result=deepcopy(BASE[number-1])
    result['original_slide']=number
    if minutes is not None:result['minutes']=minutes
    return result

# Main teaching route: substantive paper pairs are integrated before evaluation.
SLIDES=[original(n,t) for n,t in [(1,.5),(2,1),(3,1.5),(5,1),(6,1.5),
        (7,1),(8,1),(9,1),(10,1.5),(11,1.5),(12,6)]]
SLIDES += [original(n,t) for n,t in [(13,1.5),(15,1.5),(16,1.5),(17,1.5),(18,1)]]
SLIDES += FOUNDATION
for index in (0,1,2,3,5,6):
    POWER[index]['minutes']=2
    SLIDES.append(POWER[index])
SLIDES += [original(n,t) for n,t in [(20,1),(21,1.5),(22,1.5),(23,1.5),
        (25,1.5),(26,2),(27,1.5),(28,6),(29,1.5),(30,1),(33,1.5)]]
SLIDES += [original(34,1.5),SCIENCE[0],SCIENCE[1],SCIENCE[2],SCIENCE[3],original(35,2)]
SCIENCE[4]['minutes']=2
SLIDES += [SCIENCE[4]]
SLIDES += [original(n,t) for n,t in [(37,1.5),(38,1.5),(40,1.5),(41,.5),(42,1.5)]]
CORE_SLIDES=len(SLIDES)

# Optional extension keeps the main route at 90 minutes and the total below 80.
EXTENSION += [original(n,2) for n in (4,14,19,24,31,32,39)]
EXTENSION.insert(1,POWER[4])
for item in EXTENSION:
    item['extension']=True
    item['eyebrow']='Research extension · optional discussion'
SLIDES += EXTENSION
SLIDES[0]['points']=['Engineering mechanisms and measured paper results',
    '90-minute teaching route · two worked exercises · research extension',
    'IEEE ComSoc theme · Evidence reviewed17 October2026']
SLIDES[0]['note']='This edition integrates concept/result pairs for ReAct, Toolformer, Reflexion, LATS and AFlow; three additional power-system studies; and Harvard-led scientific systems. Present the main route in90 minutes including two six-minute exercises. Optional studies follow the discussion; use them for longer sessions or substitute a relevant study. The next workshop covers the detailed voltage, restoration and cyber cases.'
SLIDES[CORE_SLIDES-1]['points']=['Which failure mechanism should your first evaluation expose?',
    'Which paper supplies the closest task, tools and evaluation protocol?',
    'Full papers and author code are linked in the reading guide; optional studies follow.']
SLIDES[CORE_SLIDES-1]['note']='This concludes the90-minute main route, including both six-minute exercises. The remaining slides are optional research studies and elaborations. Ask participants to name one mechanism, one measured result and one limitation that affect their proposed utility task. Full paper PDFs, code when available, figure data and source limitations are in the reading guide.'

# Readable typography in prose; preserve asset IDs and reference tokens.
import re
def human(text):
    text=re.sub(r'\b([A-Za-z][a-z]{1,})(?=\d)',r'\1 ',text)
    text=re.sub(r'\b(202\d)(?=[A-Za-z])',r'\1 ',text)
    return text
for item in SLIDES:
    for field in ('title','note','takeaway','caption','eyebrow','callout'):
        if field in item:item[field]=human(item[field])
    item['points']=[human(p) for p in item['points']]
    if 'excerpt' in item:item['excerpt']=[human(p) for p in item['excerpt']]
    if (item.get('image') or '').startswith(('expanded_foundation_','expanded_power_','expanded_science_')):
        item['visual_height_cm']=3.9
        item['visual_height_px']=350

# The result itself stays in the plot; one interpretation below avoids repetition.
FIGURE_POINTS={
 'expanded_foundation_react.png':'The 9.9-point gain is measured on 500 shopping instructions; it does not estimate grid-task reliability.',
 'expanded_foundation_toolformer.png':'Enabling calls adds 29 points in this single-call arithmetic setting; this does not test long-horizon planning.',
 'expanded_foundation_reflexion.png':'Reflection without tests falls below the baseline here; useful feedback matters more than critique alone.',
 'expanded_foundation_lats.png':'Score means 100 × mean reward, not fully successful tasks. This 50-instruction setup differs from the ReAct experiment.',
 'expanded_foundation_aflow.png':'The 9.8-point gain holds the executor fixed; offline workflow-search cost is additional.',
 'expanded_power_dynamic.png':'Success requires all eight tests within five permitted updates; one modified model limits generalization.',
 'expanded_power_benchmark.png':'Joint accuracy requires all fields and a valid schema; field accuracy gives partial credit. Macro-JA weights families equally.',
 'expanded_power_gridmind.png':'The same seven queries use 60% fewer stages and 52.7% less wall time; stage costs differ.',
 'expanded_science_tooluniverse.png':'The matched agent gains 21.6 points on database questions and 5.2 on sequence questions; utility transfer needs new tests.',
 'expanded_science_txagent.png':'The 25.8-point advantage compares complete systems; training and tool access both differ.',
 'expanded_science_txagent_ablation.png':'Actual tools outperform generated imitations here. This multiple-choice setting differs from the prior open-ended result.',
 'expanded_science_popper.png':'POPPER has higher power than ReAct here; observed error control remains conditional on valid tests and logical relevance.',
 'expanded_science_popper_failures.png':'These labels describe 128 failed logs; one log can have several labels. They are not failure rates over all attempts.'}
for item in SLIDES:
    if item.get('image') in FIGURE_POINTS:
        item['points']=[FIGURE_POINTS[item['image']]]
    if item.get('extension') and item.get('image'):
        item['visual_height_cm']=3.65
    if item.get('original_slide')==4:
        item['points']=[]
        item['visual_height_cm']=5.2
        item['visual_height_px']=450
        item['caption']='Original PJM forecast, p.9: 2025 vintage (blue), 2026 vintage (green). Forecast MW, not observed future demand.'

assert len(SLIDES)<=80
assert CORE_SLIDES==55
assert sum(s['minutes'] for s in SLIDES if not s.get('extension'))==90
assert sum(s['kind']=='exercise' for s in SLIDES)==2
