"""Engineering tutorial: measured evidence, worked mechanisms and explicit assumptions."""
SLIDES=[]
EXTRA_READING_REFS=['H02','H06','H08','H11','T02','T04','T06','T07','C11','C12','Q02','R03','R04','V02']

def add(title, points=(), *, minutes=2, refs=(), image=None, caption='', diagram=None,
        kind='normal', note='', takeaway='', **extra):
    SLIDES.append(dict(title=title,points=list(points),minutes=minutes,refs=list(refs),
                       image=image,caption=caption,diagram=diagram,kind=kind,
                       note=note,takeaway=takeaway,**extra))

add('Agentic AI for Utility Operators', [
    'Engineering mechanisms, measured results and evaluation',
    '90 minutes · two worked exercises',
    'IEEE ComSoc theme · Evidence reviewed 17 October 2026'],
    minutes=.5,refs=['B01'],kind='cover',
    note='Pitch this version at utility engineers and researchers. The aim is to distinguish a successful API call, a valid modeled result and a justified operating recommendation. The following workshop provides the detailed GridGuard voltage, restoration and cyber cases. This tutorial supplies the mechanisms and evidence needed to assess them.')

add('Three questions behind a usable recommendation', [
    'Data validity: do identity, units, time and topology match the question?',
    'Engineering validity: was the requested problem solved within its declared constraints?',
    'Decision validity: is the evidence complete enough for the permitted next action?'],
    minutes=1.5,
    note='These are three independent questions. A syntactically valid call can use an old topology. A converged optimization can change a forbidden variable. A correct result can still be incomplete for the operator’s decision. Introduce these as an acceptance contract that will be reused in the examples and exercises, rather than as an abstract architecture.',
    takeaway='Judge the whole task against an explicit acceptance contract.')

add('Operator attention is a scarce resource', [
    'A PNNL survey of 20 control-room operators reported an average 61% of tasks requiring completion in under 30 minutes.',
    'The 75-item survey did not publish the task denominator or variance behind that average.',
    'Assistance should reduce evidence-search and review effort within the actual task window.'],
    refs=['Q01','O01','I02'],image='duke_control_room.jpg',kind='photo',
    caption='Duke Energy control room, 2022. PNNL’s survey is a separate study.',
    note='The statistic is an average share of tasks performed or supported, not the share of operators. Twenty respondents do not justify a binomial interval for the reported 61%, and 75 items do not imply 1,500 independent timing observations. It is a small self-report study, not a national estimate. Ask participants which tasks are deadline-sensitive and which can tolerate a longer investigation.',
    takeaway='Measure the operator’s total effort and the task deadline, not only model response time.')

add('Changing assumptions create repeated study work', [
    'PJM’s 2026 forecast projects 3.6% annual summer-peak growth over ten years and considers 403 weather scenarios.',
    'The two forecast vintages illustrate why a result needs a reproducible input snapshot.'],
    minutes=1.5,refs=['M01'],image='framework_pjm_summer_peak.png',kind='figure',
    caption='Original PJM forecast, printed p. 9. Forecast MW, not observed future demand.',
    note='Do not claim that all 403 weather scenarios are one operator’s daily workload. The engineering issue is versioned assumptions: a conclusion changes when the underlying load, weather, network or model changes. Repeated procedural work is a possible agent task; deciding whether the assumptions represent the intended study remains an engineering responsibility.')

add('Define the task before selecting the model', [
    'Task: assess whether a previously computed result remains relevant after a new event.',
    'Return evidence or request missing inputs; stop on a changed snapshot, failed tool, exhausted budget or missing permission.'],
    excerpt=['case = F12 / event at 15:02 / review at 15:05',
             'snapshot = {data_time, topology_hash, model_revision}',
             'allowed_output = recommendation or request_for_evidence'],
    note='All F12 records and policies in the worked examples are invented teaching data. They are not utility operating rules. Identify the user, expected artifact and permitted action first. Success means satisfying this contract, not producing an answer of a particular length or making a fixed number of tool calls.',
    takeaway='A bounded engineering task provides a testable definition of success.')

add('An agent chooses calls; tools produce observations', [
    'a is a tool invocation; h is the recorded interaction history; nu identifies the input snapshot.',
    'The application checks the call before execution and appends the returned evidence to the history.'],
    minutes=2.5,refs=['T01','T04'],
    math_tex=r'\[\begin{gathered}a_t\sim\pi_\theta(\,\cdot\mid g,h_t),\qquad r_t=T(a_t;\nu)\\h_{t+1}=(h_t,a_t,r_t)\end{gathered}\]',
    math_html='a<sub>t</sub> ∼ π<sub>θ</sub>(· | g, h<sub>t</sub>) &nbsp; ; &nbsp; r<sub>t</sub> = T(a<sub>t</sub>; ν)<br>h<sub>t+1</sub> = (h<sub>t</sub>, a<sub>t</sub>, r<sub>t</sub>)',
    note='Read the equation as an interface, not a claim that the complete physical state is observed or that the history is Markovian. The model chooses a call conditioned on the goal and previous evidence. The application invokes a service against a particular snapshot. A historian returns measurements; a simulator returns modeled quantities. Neither result becomes an actuator command merely because the model selected the call.',
    takeaway='Inspect calls, parameters and observations rather than relying on a fluent final explanation.')

add('A useful trace includes the branch that stops', [
    'Asset resolution succeeds, but the measurement query returns a stale-quality flag.',
    'The correct next step is to request current evidence; the original task is still unresolved.'],
    diagram='executed_trace',kind='diagram',
    caption='Invented trace illustrating observable call arguments, return values and a stopping decision.',
    note='Walk through the actual identifiers and timestamps in the drawing. A failed data precondition is a legitimate task outcome, not a reason to invent a measurement or silently substitute the last available value. Measure whether the agent detected the failure and returned a useful next request. A trace is necessary for this inspection but does not itself prove correctness.')

add('A typed contract prevents a concrete unit error', [
    '12.47 kV equals 1.00 p.u. only when the selected voltage base is 12.47 kV.',
    'A tool expecting p.u. must reject a raw value labeled kV or require explicit conversion metadata.'],
    diagram='typed_contract',kind='diagram',
    caption='Illustrative contract; values are teaching data, not a recommended operating limit.',
    note='Dimensional consistency is part of the tool interface, not a prompt preference. The same numeral can describe very different quantities. Unit tags, base values and asset identity should be validated by software. Type validation still cannot establish that the underlying measurement or model is correct. The diagram intentionally shows both a failure and the information needed to repair it.')

add('A new topology invalidates the old result’s scope', [
    'The old study used a closed switch and topology v42; the event produces topology v43.',
    'Fresh prose cannot update the old numerical result. Refresh the snapshot and repeat affected checks.'],
    diagram='snapshot_consistency',kind='diagram',
    caption='Invented before/after network illustrating result invalidation; no power flow is calculated.',
    note='Point to the changed switch rather than following a generic process arrow. The problem is not simply that the result is a number of minutes old: it represents a different network. Matching version tokens is a necessary consistency check. It does not replace checking whether the versioned model is accurate or whether the refreshed measurements represent the event.')

add('A retry can repeat the same software error', [
    'R02 reports a reactive-load parameter omitted from an agent request and from the cache fingerprint.',
    'Correcting the request still reused the old sweep result because the cache key had not changed.'],
    minutes=2.5,refs=['R02'],diagram='cache_key_failure',kind='diagram',
    caption='Schematic of the failure described in R02, section IV. Key syntax is illustrative.',
    note='The paper’s load task includes 100 MW and 10 Mvar. A missing reactive component changes the study. A cache that ignores that parameter can return the wrong result even after the model corrects its call. Explain why asking the model to try harder is insufficient: the adapter and cache need tests. A valid cache fingerprint must represent every input that can change the result, including relevant model and topology versions.',
    takeaway='Agent reliability depends on ordinary software correctness around the model.')

add('Convergence is conditional engineering evidence', [
    'u is the candidate decision; x is the modeled state; m and tau identify the model and topology.',
    'A feasible solution satisfies the declared equations and inequalities. It does not prove scenario coverage or authorization.'],
    refs=['R01','L01'],
    math_tex=r'\[\begin{gathered}\mathcal F(m,\tau)=\{u:\ \exists x\ \text{such that}\\f(x,u;m,\tau)=0,\quad g(x,u;m,\tau)\le0\}\end{gathered}\]',
    math_html='F(m, τ) = {u : there exists x with<br>f(x,u;m,τ) = 0 and g(x,u;m,τ) ≤ 0}',
    note='Separate solver status, residuals and modeled limit checks from the completeness of the requested analysis. A solution of the wrong problem can converge perfectly. The constraints and tolerances must be part of the study contract; no universal voltage or loading limit is asserted here. Authority to act remains a separate application and organizational question.',
    takeaway='Report the solved problem and its assumptions alongside the solver status.')

add('Exercise 1: audit three returned packets', [
    'Illustrative prechecks: age at most 60 s, topology v43 and p.u. values. The user may recommend, not execute.',
    'Which packet passes these prechecks? Explain the rejection reason for each other packet.',
    'Does passing these checks establish complete engineering validity or permission to execute?'],
    minutes=6,kind='exercise',eyebrow='Active learning · 6 minutes · pairs',
    excerpt=['A = {age_s:20, topology:v42, unit:pu}',
             'B = {age_s:15, topology:v43, unit:kV}',
             'C = {age_s:45, topology:v43, unit:pu}'],
    note='Give 1 minute to inspect, 2 minutes in pairs, 2 minutes to share and 1 minute to debrief. C alone passes these stated prechecks. A has the wrong topology; B has the wrong unit contract. C still needs correct asset mapping, a valid model, the required engineering checks, adequate scenario coverage and a reviewable interpretation. The user’s advisory role does not permit execution. Do not teach 60 seconds as a general operating standard: it is a made-up policy for this exercise.')

add('CAISO/OATI: distinguish throughput from latency', [
    'The supplier reports 500+ next-day requests processed in a nightly batch in under eight minutes.',
    'This implies batch throughput above 62.5 requests/minute; it does not reveal request latency or reviewer effort.'],
    refs=['C01','C02','I06'],image='caiso_control_room.jpg',kind='photo',
    caption='Real California ISO control room. Batch result and later production status are supplier-reported.',
    note='CAISO’s own 2025 account describes a planned-outage pilot using retrieval and multiple agents; OATI’s later account reports production assistance. The throughput is an explicitly calculated lower bound, 500 divided by 8. The source does not disclose the number of nights tested, a latency distribution or independently measured reliability effects. The decision stays with reviewers.',
    takeaway='A processing-rate claim needs its batch boundary and remaining review work.')

add('The same throughput can hide very different waits', [
    'Both invented patterns finish 500 requests in 480 seconds: 1.04 results/s in each case.',
    'Mean wait is 240.48 s for sequential completions and 480 s when every result arrives at the end.'],
    image='rigor_batch_throughput.png',kind='figure',
    caption='Mathematical illustration; these completion patterns are not measured CAISO data.',
    note='All requests arrive at time zero. Sequential results complete at 0.96, 1.92 and so on through 480 seconds; their mean is 240.48 seconds. In the second pattern all finish at 480 seconds. The amortized 0.96 seconds per output is not the time a user waits. This is why throughput, time-to-first-result, tail latency and human completion time need separate measurement.')

add('AES: a report-generation result with an audit boundary', [
    'Operational Claude agents on Google Cloud review safety-program evidence; the story reports more than 50 agent audits.',
    'Reported turnaround changes from 14 days to about one hour; human examination remains.',
    'The day convention, timing distribution and accuracy denominator are not disclosed.'],
    minutes=2.5,refs=['U01','Q02'],callout='14 days → about 1 hour',
    note='The source names coordinated specialized agents and document review. Do not turn this into a measured labor-hour reduction or a universal speedup ratio: elapsed days and employee-active hours are different quantities. Vendor headlines differ on percentage timing reductions, so retain the native before/after description. The evidence supports an operational audit workflow, not autonomous grid control.',
    takeaway='Keep the reported task boundary attached to the headline result.')

add('TC Energy: verify a chain of material evidence', [
    'PIPER checks material reports, weld records and pressure-test documentation, with engineer review.',
    'The AWS story reports 85% less review time and 100+ active users; users are not the timing-test sample.'],
    minutes=2.5,refs=['U04'],eyebrow='North American pipeline infrastructure · Canadian-headquartered company',
    excerpt=['Illustrative material report: heat H548',
             'Illustrative weld record: segment S12 uses heat H845',
             'Required conclusion: mismatch with source references'],
    note='The H548/H845 records are invented to illustrate the disclosed task. A plausible summary is insufficient if the identifiers do not join. The source discloses Strands Agents, Bedrock AgentCore, Claude, Textract and Step Functions. Its early 95–100% accuracy claim lacks a fully specified denominator and error protocol, so it is not plotted as a general accuracy estimate. The 85% review-time claim lacks an absolute baseline and timing-test sample.',
    takeaway='Judge whether the assistant preserves the evidence needed to detect a mismatch.')

add('Duke/AWS: automate the study procedure', [
    'Duke engineers use AWS-managed agents to coordinate case preparation and interconnection-study work.',
    'The September 2026 announcement reports data preparation moving from two weeks to hours.',
    'The final number of hours is unspecified; engineers retain final engineering decisions.'],
    refs=['U02','U03','I03'],image='duke_operator.jpg',kind='photo',
    caption='Duke operator, 2022, for context. The cited agents support planning, not this pictured operating desk.',
    note='The simulator performs deterministic numerical analysis while agents coordinate the procedure. The public sources do not name an open SDK, so do not label the system LangGraph or Strands. The timing concerns data preparation, not the complete interconnection process. Rerun provenance, scenario coverage and review decisions remain central engineering evidence.',
    takeaway='A workflow benefit does not establish a shorter end-to-end regulatory process.')

add('GE: distinguish the business and the technical claim', [
    'GE Vernova’s GridOS deployment at Alabama Power establishes an operational platform, not a disclosed LLM control agent.',
    'GE Aerospace reports selected supply-chain agentic applications using Palantir AIP.',
    'Neither disclosure isolates an agent-specific causal reliability improvement for a utility.'],
    refs=['C07','C05','I01'],image='ge_gridos_control_room.jpg',kind='photo',
    caption='Official GridOS promotional composite. The two GE businesses and application domains are distinct.',
    note='Keep this requested GE example, but use it to teach claim identification. A named customer, platform deployment, selected agent task and controlled performance evaluation are different levels of evidence. Do not transfer an aerospace supply-chain result to electric-grid control. Siemens’ engineering-agent pilot remains in the reading guide as an adjacent example rather than repeating another generic company slide.',
    takeaway='Identify the customer, task, agent mechanism and measured outcome separately.')

add('What the deployment statistics do and do not establish', [
    'CAISO/OATI reports batch processing; AES reports audit turnaround; Duke reports preparation time; TC reports relative review time.',
    'Their units and task boundaries differ, so a cross-company speedup ranking would be misleading.',
    'Ask for timing samples, error definitions, reviewer effort and the distribution of difficult cases.'],
    minutes=1.5,refs=['C02','U01','U02','U04'],
    note='This is the evidence appraisal step. These are useful primary customer and supplier disclosures, but not randomized comparative trials. Do not invent uncertainty bars when a denominator or variance is unavailable. The next section contrasts these operational reports with papers that disclose experimental settings and repeated counts.',
    takeaway='An honest missing denominator is more informative than a precise-looking unsupported percentage.')

add('AgentiGrid: inspect the experimental unit', [
    'The September 2026 paper evaluates four model backends across three applications on one 200-bus test system.',
    'Those 12 searches are different experimental settings, not 12 repeated trials of one task.',
    'ExaGO supplies numerical analyses; the agent chooses modifications and interprets results.'],
    refs=['R01'],
    note='The applications include dispatch exploration, contingency screening and stochastic studies. Avoid treating no fatal JSON errors as task success. The relevant questions are whether the agent respected the allowed action space, enumerated the required scenarios and accurately described solver evidence. This is research on a specified prototype and modeled network, not an operating-utility reliability study.',
    takeaway='Define exactly what one reported run represents before calculating a success rate.')

add('A lower objective can solve the wrong problem', [
    'R01 reports costs of 27,564 before and 17,398 after one backend changed unit commitment.',
    'The requested task allowed dispatch changes. Relaxing the decision space makes the apparent gain invalid for that task.'],
    refs=['R01'],
    math_tex=r'\[\begin{gathered}\mathcal U_{\rm dispatch}\subseteq\mathcal U_{\rm expanded}\\\min_{u\in\mathcal U_{\rm expanded}}J(u)\le\min_{u\in\mathcal U_{\rm dispatch}}J(u)\end{gathered}\]',
    math_html='U<sub>dispatch</sub> ⊆ U<sub>expanded</sub><br>min<sub>u ∈ Uexpanded</sub> J(u) ≤ min<sub>u ∈ Udispatch</sub> J(u)',
    note='The numbers use the paper’s objective units; do not invent dollars per hour. A 36.9% lower reported objective looks attractive but came from changing a variable class outside the stated task. Other backends retained dispatch-only scope and found no improvement from the reported base. A valid evaluation checks action semantics, not only objective reduction.',
    takeaway='Optimization success is defined by both the objective and the allowed decision space.')

add('Successful calls can still miss an infeasible contingency', [
    'All four backend runs identified the highest-cost outage; none identified a second infeasible outage.',
    'These are four settings on one test grid, not independent repeated reliability trials.'],
    minutes=2.5,refs=['R01'],image='rigor_r01_coverage.png',kind='figure',
    caption='Counts derived from R01 Table III and section IV. Outage labels are bus pairs in that test system.',
    note='The plotted outcomes are economic-critical outage 187 to 189 identified by 4 of 4, infeasible outage 29 to 30 by 3 of 4, and infeasible outage 15 to 16 by 0 of 4. The lesson is incomplete evidence coverage, not a stable estimate of any model’s failure probability. Do not add binomial confidence intervals to these heterogeneous settings.')

add('Repeated results need counts and uncertainty', [
    'R02 reports ten attempts per displayed setting on synthetic 100- and 1,000-bus grids.',
    'The intervals shown are calculated Wilson 95% intervals; the paper itself reports counts.'],
    minutes=2.5,refs=['R02','R03'],image='rigor_r02_capability.png',kind='figure',
    caption='R02 Table II. L1: 100 MW + 10 Mvar load siting; L2: reactive adequacy for 100 MW + 50 Mvar generation.',
    note='Six of the eight displayed cells are 10/10 and two are 5/10. The tested code snapshot produced no results at higher complexity and larger scales; later fixes are discussed without complete new counts. Do not redraw the unreported cells as a matrix of zeroes. The grids are synthetic, not utility operating systems. Intervals assume independent fixed-setting Bernoulli outcomes and illustrate sampling uncertainty, not deployment readiness.')

add('Ten successes do not locate the rate precisely', [
    'The calculated two-sided Wilson 95% interval for 10/10 is approximately 72.2% to 100%.',
    'For 5/10 it is approximately 23.7% to 76.3%. Reusing one easy case also misses distributional uncertainty.'],
    minutes=1.5,refs=['R03'],callout='Observed score ≠ known success probability',
    note='Explain the interval as a method with repeated-sampling coverage, not a 95% posterior probability that this fixed parameter lies inside this particular interval. These are calculations from small hypothetical or paper counts under the binomial model. Wider task diversity, configuration changes and dependencies add uncertainty beyond this model. Keep Wilson two-sided intervals distinct from the one-sided exact failure bound introduced shortly.',
    takeaway='Report trial counts, task distribution and interval method with a benchmark percentage.')

add('Workflow reliability compounds across required steps', [
    'With independent identical 99%-successful steps, 20 required steps all succeed only 81.8% of the time.',
    'Real errors can share a cause; measure the complete workflow rather than assuming independence.'],
    minutes=2.5,image='rigor_reliability_chain.png',kind='figure',
    caption='Illustrative probability model, not measured agent performance: P(all L steps succeed) = q^L.',
    note='Use the three curves to show why a good local score can coexist with weaker task completion. A retry may share the same incorrect context, cache or tool adapter and therefore not be an independent fresh chance. The exact general chain rule multiplies conditional probabilities; the plotted q to the L is a simplified identical-independent model. It motivates end-to-end measurement and deterministic checks, not a forecast of an actual utility agent.')

add('The denominator changes the safety-relevant result', [
    'In this invented test, two infeasible cases are accepted: 2/20 = 10% false approval among infeasible cases.',
    'Calling the same two errors “2% of all 100 cases” hides the conditional failure rate.'],
    minutes=2.5,image='rigor_eval_outcomes.png',kind='figure',
    caption='Invented test set: 80 feasible and 20 infeasible cases. Counts illustrate metric definitions, not a deployment result.',
    note='Seventy of 80 feasible cases are accepted; 10 are rejected. Two of 20 infeasible cases are accepted; 18 are rejected. Accepted-result precision is 70/72, or 97.2%, yet the false-approval rate in the critical infeasible stratum is 10%. Overall correct classification is 88/100. Define the error that matters before choosing a headline metric. More rejection can reduce false approvals while making the assistant less useful; measure both sides.')

add('Zero observed failures still leaves uncertainty', [
    'After zero failures in n independent fixed-setting trials, the exact one-sided 95% upper bound is 1 − 0.05^(1/n).',
    'Zero in 300 gives a bound near 0.994%; the bound does not cover a new task distribution.'],
    minutes=2.5,refs=['R04'],image='rigor_zero_failure_bound.png',kind='figure',
    caption='Calculated binomial bound. Fixed failure definition, independent trials and stable test conditions are required.',
    note='Derive it verbally: if the failure probability were p, the probability of seeing no failures in n independent trials would be (1-p)^n. Set this to 0.05 and solve. This bounds failure under the assumed test distribution; it is not certification and does not establish performance after a topology, model or task change. The approximation 3/n is useful for a quick mental estimate.')

add('Exercise 2: can you support a 1% failure claim?', [
    'A fixed simulator test yields zero false approvals in 60 independent trials drawn from the target infeasible-case distribution.',
    'Can you support a failure probability below 1% at one-sided 95% confidence? Estimate the required zero-failure sample.',
    'What changes if the 60 runs reuse one topology and the deployed task distribution changes?'],
    minutes=6,kind='exercise',eyebrow='Active learning · 6 minutes · pairs',
    math_tex=r'\[\begin{gathered}p_U=1-0.05^{1/n}\ \approx\ 3/n\\n\ge\log(0.05)/\log(0.99)\end{gathered}\]',
    math_html='p<sub>U</sub> = 1 − 0.05<sup>1/n</sup> ≈ 3/n<br>n ≥ log(0.05) / log(0.99)',
    refs=['R04'],
    note='Give 1 minute individual work, 2 minutes in pairs, 2 minutes discussion and 1 minute debrief. At n=60 the exact bound is 4.8703%, so the proposed 1% claim is unsupported. The sample requirement is at least 299 zero-failure independent trials under the stated fixed setting and distribution; 300 is a convenient rounded answer. If participants give about 300 using 3/n, accept it. Tests must sample the infeasible cases that define the false-approval denominator. Repeated seeds on one topology need not represent topology diversity; a distribution shift invalidates an unqualified transfer of the bound.')

add('Build an evaluation set that can expose failure', [
    'Stratify by task complexity, grid scale, stale inputs, tool failures and feasible versus infeasible cases.',
    'Use an independent reference check and keep tuning cases separate from final evaluation.',
    'Record a case ID, configuration, snapshot, tool evidence, disposition and human corrections for every trial.'],
    refs=['R02','T12','T14'],
    note='Do not call repetitions of one prompt a broad test distribution. Count dependencies such as shared networks and scenarios, and report them. An independent checker should not merely ask the same model whether its answer is correct. Hold out cases when adjusting prompts or adapters. A local test matrix is a proposed method here, not a certification procedure.',
    takeaway='Measure failure by stage and by case class, with denominators that remain visible.')

add('The deployed stack separates five responsibilities', [
    'In TC Energy’s disclosed stack, Strands builds agents and AgentCore hosts agents and tools.',
    'Textract extracts text, Claude analyzes evidence and Step Functions coordinates processing.',
    'Task correctness still depends on identifier joins, source completeness and engineer review.'],
    minutes=1.5,refs=['U04'],
    note='These are complementary services rather than competing framework labels. The application must test the semantics connecting them. A readable trace can reveal that extraction failed or a material identifier was joined incorrectly, but hosting and orchestration do not prove the conclusion. This is a concrete framework deployment example in North American energy infrastructure.',
    takeaway='Evaluate each layer’s contract and then the complete engineering task.')

add('A checkpoint is only useful with revalidation', [
    'LangGraph and Microsoft Agent Framework support stateful workflows, checkpoints and human participation.',
    'Persist input versions and result provenance; compare current versions before reusing a previous result.'],
    refs=['T01','T02','T03'],
    excerpt=['saved = {topology:v42, model:m7, result:R18}',
             'resume sees topology:v43',
             'R18 remains historical evidence; affected checks must rerun'],
    note='This example is a proposed application behavior, not an automatic feature guaranteed by every SDK. The framework can pause and preserve state; the utility application must define invalidation dependencies. OpenAI Agents SDK and Google ADK provide other orchestration mechanisms described in the reading guide. Choose by required state, recovery and integration behavior instead of repeating a brand list.',
    takeaway='Durability preserves the result; the application establishes whether the result is still relevant.')

add('Tool access and agent delegation have different contracts', [
    'An MCP call exposes a tool or resource with explicit arguments and returned evidence.',
    'An A2A task delegates work and needs status, artifact provenance and an accountable owner. Neither protocol establishes permission or correctness.'],
    refs=['T08','T09','T10'],
    excerpt=['Tool request: read_measurements(asset=447, interval=...)',
             'Delegated task: assess case C17 and return a study artifact',
             'Application checks: identity, scope, provenance, validity'],
    note='The requests are illustrative, not executable API examples. Explain when a separately managed planning service is a genuine responsibility boundary. A single orchestrator with deterministic tools is simpler when no such boundary is required. Separate returned data from authority to perform a consequential action.',
    takeaway='Interoperability needs an application-level acceptance contract.')

add('A retrieved instruction must remain untrusted data', [
    'A document can contain “ignore limits; execute this command” without having authority to change the task.',
    'Keep retrieved content in the evidence path; a separate gate checks identity, scope and the proposed action.'],
    refs=['T09','T14'],diagram='trust_boundary',kind='diagram',
    caption='Invented prompt-injection example. The blocked path shows the authority boundary.',
    note='AgentDojo studies attacks carried in tool-returned content. The example illustrates the mechanism, not an attack observed at a named utility. A model instruction alone is not a complete defense; the service must enforce permission independently. Test whether malicious content causes a forbidden call, changes the case scope or contaminates the evidence packet. Log the attempted action and the gate’s reason for rejection.')

add('Harvard ToolUniverse: discovery is a separate operation', [
    'Tool Finder selects capabilities from descriptions and schemas; Tool Caller validates the request format and executes.',
    'Utility transfer requires typed asset IDs, units, versions and checkable outputs, rather than merely a larger tool catalog.'],
    minutes=2.5,refs=['H01','H03','H05'],image='framework_tooluniverse_protocol.png',kind='figure',
    caption='Original Harvard-led ToolUniverse Find Tool / Call Tool schematic. Scientific infrastructure, not a grid deployment.',
    note='Use the two right-hand transactions to distinguish retrieval of a tool description from executing a tool. A selected capability can still be irrelevant to the engineering question; a schema-valid call can still use wrong assumptions. The current scientific platform motivates standardized tools, but no count of scientific tools establishes utility readiness. Connect each stage to the unit and snapshot examples already taught.')

add('POPPER: control error while choosing tests adaptively', [
    'Stanford–Harvard POPPER chooses falsification tests adaptively; each evidence factor needs conditional calibration.',
    'Illustrative factors 2, 3 and 4 give cumulative evidence 24, above the threshold 20 at alpha = 0.05.'],
    minutes=2.5,refs=['H09','H10'],
    math_tex=r'\[\begin{gathered}\mathbb E[e_i\mid\mathcal D_{i-1}]\le1\quad\text{under }H_0\\E_t=\prod_{i=1}^{t}e_i,\qquad E_t\ge1/\alpha=20\end{gathered}\]',
    math_html='E[e<sub>i</sub> | D<sub>i−1</sub>] ≤ 1 under H<sub>0</sub><br>E<sub>t</sub> = ∏<sub>i=1…t</sub> e<sub>i</sub> &nbsp; ; &nbsp; E<sub>t</sub> ≥ 1/α = 20',
    note='The paper converts valid p-values into e-values and uses a sequential evidence rule. D is the prior test data; each nonnegative e-value has conditional mean at most one under the appropriate null. The factors 2, 3 and 4 are invented to make the multiplication concrete, not reported experimental values. The guarantee requires the paper’s logical implication and statistical assumptions plus a valid stopping rule. Arbitrary adaptively collected p-values are insufficient. Statistical error control does not establish physical feasibility or authority to act.',
    takeaway='A rigorous framework states both the stopping rule and the assumptions behind its guarantee.')

add('Domain specialization changes what must be tested', [
    'Harvard-led TxAgent specializes tools and evidence for therapeutic reasoning.',
    'A utility counterpart needs its own semantics: assets, topology, engineering units, constraints and accepted references.',
    'Transfer architecture and evaluation discipline; revalidate every domain-specific contract.'],
    minutes=1,refs=['H06','H07'],
    note='This is a research analogy, not a proposal to use biomedical software in a control room. The concrete lesson is that an adapter needs more than a natural-language description. The failure modes already shown—wrong units, stale topology and an incomplete cache key—are domain and application questions a general framework cannot answer.',
    takeaway='Domain tooling and domain evaluation are part of the agent system.')

add('Measure human value at the task boundary', [
    'Record total task time, reviewer corrections and false approvals, including failed or escalated attempts.',
    'A faster draft can increase review effort. Report distributions and difficult cases, including escalations.'],
    refs=['Q01','U01','U04'],
    math_tex=r'T_{\rm task}=T_{\rm data}+T_{\rm agent}+T_{\rm review}+T_{\rm rework}',
    math_html='T<sub>task</sub> = T<sub>data</sub> + T<sub>agent</sub> + T<sub>review</sub> + T<sub>rework</sub>',
    note='This is a proposed measurement decomposition for a serial task; parallel stages need critical-path timing rather than a naive sum. Include the operator’s attention and the time to recover from an error. This explains why audit turnaround, batch throughput and review-time reduction cannot be treated as the same metric. Choose latency percentiles and workload measures appropriate to the actual task.',
    takeaway='The operator’s completed work product is the unit of value.')

add('A useful pilot compares like with like', [
    'Begin in shadow mode: record proposed outputs without changing the operating decision.',
    'Compare matched tasks with and without assistance; account for operator learning, task difficulty and carryover.',
    'Predefine stopping rules, error classes, review obligations and the evidence required to expand scope.'],
    note='This is a proposed evaluation design, not an industry-standard approval process. Randomized or counterbalanced task order can reduce order effects when feasible. Keep a fixed final evaluation set after tuning. Record disagreements between the agent and independent reference checks. A pilot result transfers only to conditions represented by the tested task, tools, configurations and users.',
    takeaway='Separate building the assistant from testing the claim that it helps.')

add('Power-sector test environments support this work', [
    'DOE CESER’s July 2026 announcement describes LLNL’s Stormbreaker evaluation testbed.',
    'EPRI’s SAFERai.power work addresses assessment and risk guidance; neither constitutes certification of this prototype.'],
    minutes=1,refs=['C15','C11','C12','I05'],image='ornl_goal.jpg',kind='photo',
    caption='ORNL GOAL research laboratory for context. This photograph is not the LLNL testbed.',
    note='The right environment makes tool failures, changing states and engineering consequences observable under controlled conditions. A testbed must still be configured to represent the task being evaluated. Keep the institutional roles distinct and avoid treating the existence of an evaluation initiative as proof of an individual agent’s performance.')

add('GridGuard: a testable engineering proposition', [
    'The current prototype checks candidate actions in OpenDSS simulation on a synthetic feeder.',
    'The claim to test is improved task outcomes under fixed constraints, not whether the model can produce plausible actions.',
    'Retain proposal, snapshot, solver evidence, rejected candidates and reviewer disposition.'],
    refs=['L01','L02'],image='gridguard_research_feeder.png',kind='photo',
    caption='Existing workshop figure: synthetic SMART-DS Greensboro feeder udt8894; not a live utility circuit.',
    note='The current prototype has no live DMS command authority. State the hypothesis with measurable outcomes: correct feasible proposals, false approvals, engineering violations, time and reviewer corrections. Record non-results and scope violations. This supplies a rigorous motivation for the next tutorial without teaching its three numerical case studies here.',
    takeaway='The contribution is useful proposals whose assumptions and evidence can be inspected.')

add('Next tutorial: apply the acceptance contract', [
    'Voltage support: was the declared candidate feasible under the intended model?',
    'Restoration: were topology, switching constraints and served load checked completely?',
    'Cyber response: did uncertain or malicious information change authority or corrupt the evidence?'],
    minutes=1,refs=['L02'],
    note='Carry the three opening questions into the detailed workshop: data validity, engineering validity and decision validity. Ask participants to identify a denominator and a rejected case for every performance claim. The exact experiments and results belong to that next tutorial.')

add('Discussion and full sources', [
    'Which failure mechanism would your first evaluation need to expose?',
    'What would count as success for the operator’s complete task?',
    'The separate guide links full papers, case disclosures, methods and editable visual sources.'],
    minutes=1.5,kind='closing',
    note='The 90-minute schedule includes the two six-minute exercises and this discussion. Use the reading guide for the original papers and metric definitions. End by asking for one concrete acceptance criterion rather than another proposed agent feature.',
    takeaway='A credible claim names the task, denominator, assumptions, failures and remaining human work.')

assert len(SLIDES)==42
assert sum(s['minutes'] for s in SLIDES)==90
assert sum(s['kind']=='exercise' for s in SLIDES)==2
