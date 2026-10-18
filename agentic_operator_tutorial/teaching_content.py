"""Ninety-minute teaching tutorial; worked GridGuard cases follow separately."""
SLIDES = []
EXTRA_READING_REFS = ['H02', 'H08', 'H12', 'U02', 'T03', 'T07', 'V02']

def add(title, points, *, minutes=2, refs=(), image=None, caption='', diagram=None,
        kind='normal', eyebrow='', note='', takeaway=''):
    SLIDES.append(dict(title=title, points=list(points), minutes=minutes,
                       refs=list(refs), image=image, caption=caption, diagram=diagram,
                       kind=kind, eyebrow=eyebrow, note=note, takeaway=takeaway))

add('Agentic AI for Utility Operators', [
    'Concepts, deployed systems and engineering evidence',
    '90-minute tutorial with two group exercises',
    'IEEE ComSoc theme · Evidence reviewed 17 October 2026'],
    minutes=.5, refs=['B01'], kind='cover',
    note='Introduce the session as a foundation for the separate GridGuard workshop. The audience will learn how agents use tools, what named companies report, and what evidence an operator needs. The following workshop owns the detailed voltage-support, restoration and cyber-response experiments.')

add('What you will be able to explain', [
    'Trace an agent’s task through data, tools, checks and operator review.',
    'Explain real utility and energy cases, including the frameworks they disclose.',
    'Design a bounded assistant task and challenge a recommendation with incomplete evidence.'],
    minutes=1.5,
    note='Give the route verbally: operator context and foundations, exercise one, utility deployments, reusable frameworks and research, then evaluation and exercise two. There is no coding prerequisite. Ask participants to keep one task from their own operating environment in mind. The reading guide is separate and does not count toward the 90 minutes.',
    takeaway='Use the cases to understand the mechanism, not just the product name.')

add('Inside a utility control room', [
    'PJM’s operating team covers the system 24 hours a day, seven days a week.',
    'Operators balance supply and demand, monitor overloads and anticipate weather impacts.',
    'A Duke Energy profile describes an operator working with a dozen monitors.'],
    refs=['O01','I02'], image='duke_control_room.jpg', kind='photo',
    caption='Duke Energy control room, 2022. Real operating-context photograph.',
    note='Coverage describes the team, not the length of one person’s shift. The monitor count comes from one historical Duke profile and is not a universal staffing standard. Explain why the same event may appear differently in the alarm list, topology display and operating log. An assistant is useful only if it helps reconcile this evidence.',
    takeaway='The task is to form a current operating picture from several sources.')

add('Different desks need different assistance', [
    'Generation dispatch follows balance and reserves; transmission dispatch follows security, outages and voltage.',
    'Reliability engineers prepare next-day studies; supervisors coordinate work across the shift.',
    'A useful assistant has a named user, a defined question and a clear decision owner.'],
    refs=['O02'],
    note='These responsibilities summarize PJM’s published desk descriptions. The positions do not map one-to-one to NERC functional titles, and other organizations divide work differently. Use a concrete contrast: a reserve exception summary and a transmission-outage study packet require different tools and outputs. Do not design a generic assistant for every desk at once.',
    takeaway='Begin with one recurring task at one operating desk.')

add('The operator already has analytical tools', [
    'CAISO combines wildfire maps, transmission overlays and camera views.',
    'Its published Real-Time Contingency Analysis cycle is every five minutes.',
    'An agent can help assemble relevant outputs and procedures around a specific question.'],
    minutes=1.5, refs=['O05'], image='caiso_watch_duty.png', kind='photo',
    caption='Actual Watch Duty screenshot published by California ISO, 2025.',
    note='Explain a wildfire question: which assets are nearby, which are already out, and what analysis is current? The existing systems supply the map and engineering analysis. An assistant could coordinate their evidence. Five minutes is the published RTCA cycle, not a guaranteed agent response time. Suggested agent behavior is a teaching proposal.',
    takeaway='Tool coordination can add value without replacing the engineering tools.')

add('Why planning assumptions keep changing', [
    'PJM’s January 2026 report projects 3.6% average annual summer-peak growth over ten years.',
    'The report evaluates 403 weather scenarios; the chart compares two forecast vintages.'],
    refs=['M01'], image='framework_pjm_summer_peak.png', kind='figure',
    caption='Original PJM summer-peak forecast chart, printed p. 9. MW; forecasts are not observations.',
    note='Point out the historical portion and the two future trajectories. A result can change because its inputs changed, even if the calculation is identical. The motivation for agents is organizing repeated analysis and its assumptions. The forecast itself does not demonstrate an agent benefit or describe how many scenarios one operator handles per shift.',
    takeaway='Every analysis needs its input dates, assumptions and model version.')

add('A bounded task: prepare a shift briefing', [
    'Request: summarize open alarms and changes since the previous shift, with source links.',
    'Return each open item’s status, time, owner and unresolved evidence gaps.',
    'The incoming operator reconciles the draft with the official log and outgoing operator.'],
    diagram='evidence_path', kind='diagram',
    caption='Illustrative assistant design; this is not a disclosed feature of the pictured utilities.',
    note='Walk through the inputs in the diagram. A log establishes reported events; telemetry shows measurements; procedures define the relevant response. The assistant should preserve disagreement, not blend conflicting records into a confident story. Its output is a draft briefing. The operator still conducts the handover required by the organization.',
    takeaway='A source-linked briefing is a concrete first task.')

add('The agent loop', [
    'The model proposes a tool call; the application checks and executes the request.',
    'The returned observation can change the next action, trigger review or end the task.'],
    refs=['T01','T04'], diagram='agent_loop', kind='diagram',
    caption='Teaching schematic of goal-directed tool use and feedback.',
    note='Follow one loop: ask for relevant alarms, inspect the returned interval, notice a missing asset record, and request it. The model does not measure voltage or solve power flow by writing a sentence. Tools perform those operations. Bound the loop with a task scope, permitted tools, resource limits and a stopping condition. A conventional automatic controller can be highly automated without using this pattern.',
    takeaway='Agentic behavior is the process of choosing and revising actions using feedback.')

add('Workflows and agent choices', [
    'A workflow specifies the route; an agent can choose its next step from the result.',
    'A utility application can combine flexible investigation with fixed engineering checks.'],
    refs=['T01','V01'], image='framework_langgraph_workflow.png', kind='figure',
    caption='Original workflow/agent comparison in the LangGraph documentation.',
    note='Point to the predefined paths on the left and the action/feedback loop on the right. Do not explain every mini-diagram. For example, allow the assistant to select relevant evidence, but require the same data-validity and review checks before it issues a recommendation. Fixed rules and model choices solve different parts of the task.',
    takeaway='Choose flexibility only where the task requires it.')

add('Retrieval and computation answer different questions', [
    'Retrieval finds what an approved document says and where it says it.',
    'A calculation tool evaluates a model using explicit inputs, units and assumptions.',
    'The recommendation should cite both the procedure and the computed result.'],
    diagram='rag_tools', kind='diagram',
    caption='Proposed utility architecture: document evidence and numerical evidence meet at review.',
    refs=['T01','L01'],
    note='Use voltage as a verbal example without teaching the next workshop’s numerical case. A procedure may describe the permissible action, while OpenDSS estimates a candidate’s effect in a model. A retrieved paragraph is not proof of electrical feasibility. A converged calculation is also insufficient if it used the wrong topology or stale data.',
    takeaway='A citation and a simulation result support different parts of a decision.')

add('State makes a long task reviewable', [
    'Keep the case ID, asset identity, input times, model version and completed tool results.',
    'A checkpoint preserves progress while the operator reviews a proposed next step.',
    'Before resuming, check whether the operating state or permission has changed.'],
    refs=['T01','T03'], diagram='state_resume', kind='diagram',
    caption='Illustrative checkpoint and human-review workflow.',
    note='Distinguish task state from a conversational memory that merely recalls earlier words. A saved result has a timestamp and a specific input snapshot. Resuming an interrupted task does not make the old result current. Ask what should happen if a breaker changed state during review: refresh the affected inputs and repeat the relevant checks.',
    takeaway='A checkpoint preserves work; a freshness check establishes whether it is still usable.')

add('Authority belongs to the application', [
    'Reading evidence, recommending an option and preparing a work item require different permissions.',
    'An execution request crosses a separate authorization boundary.',
    'Tools enforce identity and scope even when the model asks for more access.'],
    diagram='authority', kind='diagram',
    caption='Teaching model of increasing authority; actual procedures determine the permitted boundary.',
    note='This is an illustrative ladder, not an industry standard. Explain that an instruction in a retrieved document cannot grant a new permission. The service that connects to an operating system must check the user and action independently. A human review should show the exact proposed target, units, reason and expected effect rather than a vague approve button.',
    takeaway='A prompt describes the role; the application must enforce it.')

add('Exercise 1: design a shift-briefing assistant', [
    'In pairs, choose three inputs the assistant needs and one output the operator should receive.',
    'Specify two actions it may take and one action it must leave to the operator.',
    'Name one reason it should stop and request help. Be ready to justify the boundary.'],
    minutes=6, kind='exercise', eyebrow='Active learning · 6 minutes · pairs',
    note='Facilitation: 1 minute individual thinking, 2 minutes in pairs, 2 minutes sharing, 1 minute debrief. Suggested answer: read the official event log, recent telemetry and the approved procedure revision; return a draft list of open items with times, owners and source links. Permitted actions: query records and ask for clarification. Excluded action: issue a switching command. Stop on missing coverage, conflicting asset IDs or unauthorized access. Accept other bounded designs when the evidence and owner are clear. Do not require a specific framework name.',
    takeaway='Explain the task boundary before choosing a framework.')

add('What counts as deployment evidence?', [
    'Look for a named organization, an actual task and a clear statement of operational use.',
    'A named framework reveals implementation choices; a product announcement alone does not.',
    'Keep the reported metric, its scope and the person who still makes the decision together.'],
    minutes=1.5, refs=['C01','C02','U01','U04'],
    note='Set up the case section. A supplier customer story is useful primary evidence of a disclosed system, but is not an independent causal evaluation. A pilot, a launched program and ongoing production use have different evidential meanings. The next cases identify those differences directly. Do not infer a framework from the presence of a familiar cloud provider.',
    takeaway='Ask what the agent actually does and what evidence supports the claim.')

add('CAISO: planned-outage review assistance', [
    'CAISO described a RAG and multi-agent pilot for planned-outage review in 2025.',
    'OATI’s 2026 field report describes production assistance with reviewers retaining the decision.',
    'The supplier reports processing 500+ next-day requests in a nightly batch in under eight minutes.'],
    refs=['C01','C02','I06'], image='caiso_control_room.jpg', kind='photo',
    caption='California ISO control room. Context photograph published by OATI.',
    note='Separate the customer’s pilot account from the supplier’s later production report. The timing is batch-processing throughput, not a bound on every task or evidence of fewer outages. It is an example of fitting evidence assembly into an existing reviewed process. It does not establish autonomous switching or an independently measured reliability improvement.',
    takeaway='The operator’s review process can be the place where an agent’s output is used.')

add('CAISO: what the implementation teaches', [
    'Ground the analysis in relevant operating material rather than an unsupported model answer.',
    'Use the review queue to organize proposed findings and exceptions for a human reviewer.',
    'The public accounts support a multi-agent pattern; they do not identify LangGraph or another open SDK.'],
    refs=['C01','C02'],
    note='Distinguish what is disclosed from the teaching interpretation. RAG means retrieving relevant source material for the model; it does not mean every generated inference is correct. The general design lesson is to produce a reviewable packet in the system where work already happens. Do not add undocumented agent names, prompts or data connections to this case.',
    takeaway='Transfer the reviewed workflow, while keeping undisclosed implementation details explicit.')

add('AES: agents for safety-program audits', [
    'Operational agents compare safety-program documents with audit requirements.',
    'The disclosed stack uses Anthropic Claude through Google Cloud, with coordinated specialized agents.',
    'Human examination remains part of the audit process.'],
    refs=['U01'], diagram='aes_audit', kind='diagram',
    caption='Simplified teaching diagram based on Google Cloud’s AES case; the full original figure is linked in the guide.',
    note='AES is a U.S.-based power company with operations in several countries. This case concerns safety-document auditing, not live grid dispatch. Trace inputs, specialized review and the resulting report. Use provider-neutral wording for the cloud platform because the live customer page has changed its branding over time.',
    takeaway='Specialized agents can divide a document task while retaining a common audit objective.')

add('AES: interpret the reported result', [
    'After more than 50 agent audits, the customer story reports results in one hour instead of 14 days.',
    'AES says agents handle half of the workload while human examination remains.',
    'This is a reported audit-process result, not evidence of autonomous operations or universal accuracy.'],
    minutes=1.5, refs=['U01'],
    note='Ask the audience what else they would request before transferring the approach: the audit definition, sample of errors and reviewer effort. Avoid converting elapsed process time into an unsupported labor-saving estimate. The teaching point is to measure the actual task and its remaining human work.',
    takeaway='Time saved is useful only when the task and review scope are understood.')

add('Duke Energy and AWS: grid-planning agents', [
    'AWS’s September 2026 program was developed in collaboration with Duke Energy.',
    'The agents coordinate existing grid models, scripts and physics-based simulation software.',
    'Engineers direct the work and confirm or override proposed steps.'],
    refs=['U02','U03','I03'], image='duke_operator.jpg', kind='photo',
    caption='Duke Energy operator photograph, 2022. Context only; the cited agent program concerns planning.',
    note='Label this accurately as a launched AWS-managed program and named utility collaboration. It is not a claim that every Duke control room operates it. Distinguish the agent that coordinates a study from the solver that performs deterministic analysis. The public program account does not name an open-source orchestration SDK.',
    takeaway='The engineering environment can remain the source of numerical results.')

add('Duke/AWS: study execution with checkpoints', [
    'Agents prepare cases, coordinate power-flow and contingency studies, and draft reports.',
    'The launch announcement reports Duke’s data-preparation tasks taking hours instead of two weeks.',
    'This is a reported preparation-task result, not the duration of an entire interconnection study.'],
    refs=['U02','U03'], diagram='duke_study', kind='diagram',
    caption='Teaching schematic of the publicly described workflow; engineers review the proposed work.',
    note='Read the flow as an ordered study with human checkpoints. Changed inputs require a rerun. The public description emphasizes versioned artifacts and recorded decisions. The named-utility timing applies to preparing data. Completing engineering analysis, reviewing results and processing an interconnection request remain distinct activities.',
    takeaway='A reusable study workflow needs traceable inputs, outputs and review decisions.')

add('TC Energy: verifying pipeline records', [
    'Pipeline IQ’s PIPER assistant checks material-test reports against weld and pressure-test records.',
    'The AWS customer story reports more than 100 active users and 85% less document-review time.',
    'Engineers inspect the cited source material and conduct the final review.'],
    refs=['U04'],
    eyebrow='North American energy infrastructure · Canadian-headquartered company',
    note='This broadens the lesson beyond electric utilities; do not call TC Energy a U.S.-headquartered electric utility. A heat number is a steel-material traceability code. Matching it across records is a specific, inspectable task. Reported early accuracy applies to a tested document scope, so it is omitted as a general headline here. Avoided future capital cost is a projection, not realized savings.',
    takeaway='A narrow verification task can expose the evidence an engineer must check.')

add('TC Energy: a disclosed framework stack', [
    'Strands Agents SDK builds the agents; Bedrock AgentCore hosts agents and tools.',
    'Textract extracts documents, Claude analyzes them, and Step Functions coordinates processing.',
    'The result links findings back to records for engineer review.'],
    refs=['U04'], diagram='tc_piper', kind='diagram',
    caption='Simplified teaching schematic of the stack disclosed in the AWS customer story.',
    note='Separate the SDK from the hosting platform, workflow service, document extractor and language model. They are complementary layers, not five competing frameworks. AgentCore Memory is also disclosed, but memory does not replace the record of source evidence. This is a concrete example of a named agent SDK used in an operational energy-sector application.',
    takeaway='A deployed agent is a system of services around a defined task.')

add('What the utility cases have in common', [
    'CAISO organizes outage-review evidence; AES reviews audit documents; Duke/AWS coordinates studies.',
    'The agent works through existing information or analytical systems.',
    'A person receives a concrete result to inspect, rather than a free-standing conversational answer.'],
    minutes=2, refs=['C01','C02','U01','U03','U04'],
    note='This slide is a teaching synthesis of the cases, not an additional deployment announcement. Ask which existing workflow would accept the output in the participant’s organization. The agent can be useful in planning, compliance and operations support before it is given execution authority. Do not imply that every case has the same level of deployment evidence.',
    takeaway='Design around the work product and the review process.')

add('GE Vernova: the operational foundation', [
    'GE Vernova names Alabama Power as an early adopter of GridOS distribution orchestration.',
    'The platform connects operational information and applications used for grid work.',
    'This disclosure does not establish an LLM agent controlling Alabama Power’s system.'],
    minutes=1.5, refs=['C07','I01'], image='ge_gridos_control_room.jpg', kind='photo',
    caption='Official GE Vernova GridOS promotional composite; not a photograph of an agent deployment.',
    note='The example explains why an agent needs an existing operational foundation: asset identity, topology, applications and controlled access. Grid orchestration and LLM agency are different claims. Preserve the named utility evidence while avoiding a claim the source does not make.',
    takeaway='An agent needs dependable domain systems to connect to.')

add('GE Aerospace: an adjacent agentic case', [
    'GE Aerospace reports selected supply-chain agentic applications using Palantir AIP.',
    'The setting is aerospace supply-chain work, distinct from GE Vernova’s utility products.',
    'Use it as a company deployment example, without transferring its claims to grid control.'],
    minutes=1.5, refs=['C05','I07'], image='ge_aerospace_services.jpg', kind='photo',
    caption='GE Aerospace services photograph from its AI overview.',
    note='Keep the two GE businesses distinct. The source supports selected agentic supply-chain deployment. It does not isolate a quantified causal gain from one agent, and it does not describe a utility operating room. The reusable lesson is a defined task, connected business tools and a reviewable outcome.',
    takeaway='A company name alone does not establish the operating domain or the agent’s authority.')

add('Siemens: engineering tasks with validation', [
    'The April 2026 Eigen Engineering Agent release names U.S. pilot customer Prism Systems.',
    'The described process assigns an engineering task, changes code, validates and iterates.',
    'Engineer review remains part of the workflow.'],
    minutes=1.5, refs=['C09'], image='siemens_eigen.jpg', kind='photo',
    caption='Official Siemens press visual. Product imagery, not a photograph of Prism’s pilot.',
    note='This is an industrial engineering example, not another electric-utility control deployment. The useful connection is observable execution and testing. A generated answer, a code change and a validated result are distinct outputs. Keep the named pilot status visible when discussing reported capability.',
    takeaway='Useful agent behavior includes acting through tools and checking the result.')

add('Frameworks occupy different layers', [
    'The operator application defines the task, identity and user interaction.',
    'An orchestration framework routes work and tracks state.',
    'Typed adapters connect approved data, simulators and work systems.'],
    refs=['T01','T02','T04','T06'], diagram='framework_layers', kind='diagram',
    caption='Teaching architecture; the named SDKs are examples rather than a single required stack.',
    note='Connect this diagram to TC Energy’s disclosed stack. A model is not the orchestrator, and an SDK is not the utility’s operating platform. The framework does not provide the correct asset IDs, data access policy or electrical model automatically. Choose by required behavior and integration, rather than by logo.',
    takeaway='The application supplies the domain meaning and the framework organizes the process.')

add('LangGraph: state and controlled continuation', [
    'Represent a task as a graph of model steps, tool operations and explicit routes.',
    'Persist state with checkpoints and interrupt the run for human input.',
    'Teaching example: gather evidence, pause for a study request, then resume after review.'],
    refs=['T01'],
    note='Return verbally to the checkpoint diagram rather than repeat it. An interrupt is a control point in the application, not a sentence asking politely for approval. Persistence and resumption still require correct storage and application design. This slide explains documented framework capabilities; it does not claim the earlier utility cases used LangGraph.',
    takeaway='Choose stateful orchestration when tasks must pause, recover or continue across steps.')

add('Microsoft Agent Framework: agents and workflows', [
    'Build agents with tools and connect them through defined workflows.',
    'Workflows support structured coordination, checkpoints and human participation.',
    'Teaching example: a document specialist and a study service contribute to one reviewed case.'],
    minutes=1.5, refs=['T02','T03'],
    note='Explain the separation between a flexible model interaction and a workflow that controls the overall task. Identity, connectors and storage must fit the deployment environment. This is a development framework overview rather than evidence that a named U.S. utility has adopted this particular SDK. The reading guide links the current overview and checkpoint documentation.',
    takeaway='A workflow can coordinate people, deterministic services and model-driven steps.')

add('OpenAI Agents SDK: tools, handoffs and traces', [
    'Define an agent’s instructions and tools, then run its tool-use loop in your application.',
    'Use a handoff when a specialist should take ownership of part of the interaction.',
    'Inspect traces of calls and handoffs; validate the returned result separately.'],
    minutes=1.5, refs=['T04'],
    note='The SDK and a managed agent service are different deployment choices. Explain ownership with a briefing assistant handing a question to a specialist, versus calling that specialist as a tool and retaining responsibility. A trace is observable execution evidence; it does not prove correctness or require exposing hidden model chain-of-thought. Sensitive utility records require the organization’s configured data controls.',
    takeaway='Orchestration makes the work visible; engineering checks establish whether the result is usable.')

add('Google ADK: compose and evaluate agents', [
    'ADK provides agent construction, tools and workflow composition.',
    'Its evaluation tools let developers test behavior against expected task results.',
    'Do not infer that AES used ADK: the AES customer story discloses Claude on Google Cloud.'],
    minutes=1.5, refs=['T06','T07','U01'],
    note='This distinction is worth teaching explicitly: a cloud service can host models used by several different frameworks. The current ADK documentation is linked for readers who want implementation detail. A local evaluation should include correct tool parameters, evidence freshness and review behavior as well as answer quality.',
    takeaway='A disclosed cloud platform does not automatically identify the SDK used to build the agent.')

add('MCP: a consistent interface to tools', [
    'Model Context Protocol connects an application to tools and contextual resources.',
    'A utility adapter might expose a governed historian query or procedure reader.',
    'The service still checks asset scope, user identity and allowed operations.'],
    minutes=1.5, refs=['T08','T09'],
    note='Use a concrete contract: query asset F12, a defined time interval and explicit units; return records with timestamps and quality flags. This utility adapter is hypothetical. A protocol describes communication. It does not grant access, validate a power-system model or turn retrieved text into an instruction with authority.',
    takeaway='Interoperability and permission are separate engineering responsibilities.')

add('A2A: coordinate separately managed agents', [
    'Agent2Agent supports exchanging tasks and results between independent agents.',
    'Example: an operating assistant requests a study from a separately managed planning service.',
    'Agree on the task status, returned artifact, provenance and failure response.'],
    minutes=1.5, refs=['T10'],
    note='The example is a proposed design. Contrast it with MCP’s application-to-tool connection. Many applications need only local tools and one orchestrator; adding multiple agents introduces handoff and consistency questions. Keep a named owner for the final recommendation, especially when separate agents disagree.',
    takeaway='Use another agent when there is a real boundary of responsibility or capability.')

add('Harvard-led ToolUniverse', [
    'A Harvard Medical School-led team built an open platform for scientific agents.',
    'Models connect to scientific databases, software and simulation tools.',
    'For utilities, the transferable idea is a consistent interface to domain capabilities.'],
    refs=['H01','H04','H05'], image='framework_tooluniverse_ecosystem.png', kind='photo',
    caption='Original ToolUniverse ecosystem figure, Harvard Kempner Institute, October 2025.',
    note='Identify this as scientific research infrastructure, not a validated utility-control product. The current paper version reviewed is dated August 2026; older figure counts are historical. The motivation is that general language capability becomes more useful when connected to relevant tools with testable input and output contracts.',
    takeaway='Domain tools provide the capabilities that a general model does not contain by itself.')

add('ToolUniverse: discover, then execute', [
    'Tool Finder locates a relevant capability; Tool Caller validates the request format and executes it.',
    'Utility use would require asset identities, units, permissions and domain-specific checks.'],
    minutes=1.5, refs=['H03','H05'], image='framework_tooluniverse_protocol.png', kind='figure',
    caption='Original ToolUniverse Find Tool / Call Tool schematic from Harvard Kempner Institute.',
    note='Read the right-hand message sequence: request capabilities, receive the tool list, call a tool and receive a response. Format validation does not establish scientific or electrical correctness. Distinguishing discovery from execution helps explain a large tool collection without implying the model can call everything freely.',
    takeaway='Finding the right tool and executing it correctly are separate operations.')

add('TxAgent: specialize the evidence and tools', [
    'Harvard-led TxAgent research focuses on therapeutic reasoning with biomedical evidence and tools.',
    'A narrow domain makes relevant data, tool behavior and evaluation questions more explicit.',
    'The utility lesson is to build around approved operating knowledge and engineering semantics.'],
    minutes=1.5, refs=['H06','H07'],
    note='This is a research analogy, not a recommendation to deploy TxAgent in a utility or clinical workflow. Domain transfer changes the data, tools, constraints and evaluation. A biomedical tool collection does not become a feeder operating model by changing the prompt. Use this example to motivate the need for a domain-specific prototype such as GridGuard.',
    takeaway='Transfer the architectural lesson and validate the new domain independently.')

add('POPPER: challenge a proposed explanation', [
    'The Stanford–Harvard collaboration proposes and executes tests that could falsify a claim.',
    'It combines statistical evidence under stated assumptions; this is not an electrical-safety guarantee.'],
    refs=['H09','H10','H11'], image='framework_popper_architecture.png', kind='figure',
    caption='Architecture portion of the authors’ ICML 2025 POPPER figure; full publication is linked.',
    note='Harvard affiliation applies to co-author Ying Jin; do not attribute the entire project to Harvard alone. Explain the upper pipeline rather than every mathematical symbol. The utility analogy is to search for reasons a candidate action should be rejected: incorrect assumptions, infeasibility or contradictory evidence. Statistical and physical checks are different mechanisms.',
    takeaway='An agent should seek evidence against its proposed explanation as well as evidence for it.')

add('AgentiGrid: agent-guided power-flow research', [
    'The September 2026 research framework connects an LLM agent to the ExaGO analysis toolkit.',
    'The agent proposes parameter changes, invokes analysis and uses results to choose the next step.',
    'Interactive steering and reports support study exploration; this is research, not a utility deployment claim.'],
    refs=['R01'],
    note='Authors are Samim Konjicija of the University of Sarajevo and Slaven Peles of Oak Ridge National Laboratory. The paper studies multi-scenario power-flow tasks and supports several model backends. Explain the direct connection to this tutorial: the solver performs numerical analysis while the agent manages iterative exploration. Do not generalize the paper’s reported success to arbitrary grids or live control.',
    takeaway='Power-sector research already studies the same propose–compute–inspect loop.')

add('Current research also exposes capability gaps', [
    'A July 2026 study tested an agent prototype across six task-complexity levels and four grid scales.',
    'Only the two lowest complexity levels were solvable on some tested grid sizes.',
    'A convincing demonstration must state task difficulty, system scale and repeated-run results.'],
    refs=['R02'],
    note='The finding applies to this study’s prototype and test suite, not every future agent. The paper reports that recommendations can disagree with solver numbers, illustrating why fluent interpretation needs checking. Contrast a bounded iterative experiment with a broad operational-readiness claim. The two AgentiGrid-related papers use different experimental questions, so their reported findings should not be treated as directly interchangeable.',
    takeaway='Benchmark the complete task at the scale and difficulty that matter.')

add('Evaluate the decision process', [
    'Check the proposed action against the correct model, current inputs and explicit constraints.',
    'Preserve tool failures, missing information and checks that were not performed.',
    'Record what the operator accepted, changed or rejected and why.'],
    refs=['R02','T12','T14'], diagram='evaluation', kind='diagram',
    caption='Proposed evaluation flow for an operator-facing utility agent.',
    note='Include ordinary tasks, stale inputs, failed tools and malicious text returned from retrieval. AgentDojo studies injection through tool content; tau2-bench studies coordinated tasks. They are useful research examples, not grid certification. Measure task success with denominators, engineering violations, reviewer corrections and time spent. A single successful walkthrough cannot establish dependable behavior.',
    takeaway='The evaluation unit is the whole task, including tools and human review.')

add('Exercise 2: would you accept this packet?', [
    'At 15:05, the assistant recommends an action after an alarm at 15:02. Inspect the input times.',
    'Choose: accept, request fresh analysis, or reject. Name the evidence that determines your choice.',
    'Specify the next tool request and what the operator must review before proceeding.'],
    minutes=6, kind='exercise', eyebrow='Active learning · 6 minutes · pairs',
    diagram='exercise_packet',
    caption='Invented teaching scenario. No freshness threshold or utility operating rule is implied.',
    note='Facilitation: 1 minute silent inspection, 2 minutes pair discussion, 2 minutes sharing, 1 minute debrief. Suggested answer: request fresh analysis. Telemetry at 14:35 and a study at 14:40 precede the 15:02 event; their age alone is not a universal violation, but the packet does not establish relevance to the current state. Request current measurements, topology/event reconciliation and a study on a consistent snapshot. Inspect quality flags, model version, scope, limits and resulting checks. Reject or escalate if current evidence cannot be established. A conditional, explicitly labeled historical result could still support investigation, not an unqualified current action.',
    takeaway='Name the missing evidence and the next step instead of accepting a fluent recommendation.')

add('Power-sector evaluation infrastructure', [
    'DOE CESER announced LLNL’s Stormbreaker AI evaluation testbed in July 2026.',
    'EPRI’s SAFERai.power initiative is developing assessment and risk guidance.',
    'A domain test environment helps examine the agent’s scope, tools and failure behavior.'],
    minutes=1.5, refs=['C15','C11','C12','I05'], image='ornl_goal.jpg', kind='photo',
    caption='ORNL GOAL laboratory. Research-context photograph; this is not LLNL’s Stormbreaker interface.',
    note='Keep the institutions distinct. Stormbreaker is the cited LLNL testbed; the photograph is ORNL. The EPRI assessment effort is under development. These efforts motivate domain evaluation but do not certify the specific prototype in the next workshop. Evaluation still needs a task definition and evidence the test environment represents the target conditions.',
    takeaway='Test the intended behavior in a relevant domain environment.')

add('Why this motivates GridGuard', [
    'General frameworks coordinate work; they do not determine feeder feasibility.',
    'GridGuard’s current prototype checks proposed actions using OpenDSS in simulation.',
    'The research question is whether tool-guided proposals can become useful, traceable recommendations.'],
    refs=['L01','L02'], image='gridguard_research_feeder.png', kind='photo',
    caption='Existing workshop figure: synthetic SMART-DS Greensboro feeder udt8894.',
    note='The model is synthetic, not a live utility circuit. The current prototype accepts changes in simulation and does not command a live DMS. Relate this to the deployed cases: a defined work product, domain tools, observable evidence and a reviewer. Leave detailed results and the three engineering experiments to the next tutorial.',
    takeaway='Combine flexible proposals with explicit domain checks and a reviewable record.')

add('What an operator should receive', [
    'Context: case and asset IDs, data times, topology and model version.',
    'Evidence: proposed action with units, tool results, passed checks and unresolved limits.',
    'Disposition: the named reviewer’s decision, reason and need for revalidation.'],
    minutes=1.5,
    note='This is a proposed output contract. Give one verbal example: a proposed setpoint is incomplete without the target device, units, current state and the checks supporting it. A concise rationale should connect the action to observable evidence. Hidden model chain-of-thought is not required. If the operating state changes, indicate which results must be refreshed.',
    takeaway='Make the basis and limits of the recommendation inspectable.')

add('Next tutorial: the three engineering cases', [
    'Voltage support: test a candidate against feeder operating constraints.',
    'Service restoration: examine topology, switching feasibility and restored service.',
    'Cyber response: examine uncertain data, quarantine and recovery evidence.'],
    minutes=1.5, refs=['L02'],
    note='The next workshop follows the existing source and provides the detailed experiments. Ask participants to carry three questions into it: what tools did the agent use, what evidence can we inspect, and who owns the decision? Do not introduce numerical results or solve those cases in this foundation tutorial.',
    takeaway='Use the same evidence and review questions across all three cases.')

add('Discussion and further reading', [
    'Which bounded task would you try first, and where would its output enter the existing workflow?',
    'What evidence would persuade you that it helps the operator?',
    'The separate reading guide contains full sources, papers, documentation and diagram credits.'],
    minutes=2, kind='closing',
    note='Reserve these two minutes for final questions. The full 90 minutes includes the two six-minute exercises and their debriefs. Open the reading guide only if needed; it is not an additional timed lecture section. Direct implementation questions to the linked framework documentation and engineering-case questions to the next workshop.',
    takeaway='Start with a useful task, defined authority and evidence that can be checked.')

assert len(SLIDES) == 46
assert sum(s['minutes'] for s in SLIDES) == 90
assert sum(s['kind'] == 'exercise' for s in SLIDES) == 2
