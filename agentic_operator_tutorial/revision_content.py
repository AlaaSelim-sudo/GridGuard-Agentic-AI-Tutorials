"""Literature definitions, utility updates and PowerAgent/PowerDAG studies."""
from copy import deepcopy

def slide(title,points=(),minutes=1.5,refs=(),**extra):
    item=dict(title=title,points=list(points),minutes=minutes,refs=list(refs),kind='normal',
              note='',takeaway='',caption='')
    item.update(extra)
    return item

INTRO=[
slide('What is agentic AI?',[
    'Here: a system in which AI helps choose and revise actions toward a goal using feedback.',
    'The complete system combines a decision model, state, callable tools and an execution policy.',
    'This is a working definition; the literature uses “agent” and “agentic system” in several ways.'],
    refs=['DEF03','DEF02'],eyebrow='A literature-grounded working definition',
    note='The first sentence is an original synthesis, not a quotation or standardized definition. Anthropic describes both engineered workflows and LLM-directed agents under agentic systems. Wooldridge and Jennings explicitly discuss variation in agent definitions. We use a narrower LLM-engineering scope in the applications that follow. Agentic describes how an assembled system pursues work; it is not an additional software component beside an agent. Multiple agents are not required.'),
slide('What is an AI agent?',[
    'Russell and Norvig describe an agent through its observations of an environment and its actions on that environment.',
    'The decision mechanism can use rules, planning, optimization or learning. An LLM is one possible implementation.'],
    refs=['DEF01'],
    math_tex=r'a_t=\pi(o_1,\ldots,o_t)',
    math_html='a<sub>t</sub> = π(o<sub>1</sub>, …, o<sub>t</sub>)',
    note='The formula is teaching notation for a policy mapping observation history to the next action, not a quotation of the textbook notation. An agent function is the abstract mapping; a program implements it. For a grid-study assistant, observations include case files and solver logs, while actions can be tool calls, requests for information or a report. This broad classical lens predates LLMs and does not by itself distinguish modern agent applications from older automation. The cited accessible chapter is the older second-edition sample despite its present fourth-edition URL; the guide records that version detail.'),
slide('An agent chooses actions; a tool exposes a capability',[
    'The agent uses observations to choose a permitted next step; the tool executes a call through a defined interface.',
    'A tool may wrap a solver, database or another agent. “Tool” describes its role for the caller.'],
    refs=['DEF06','DEF03','DEF01'],kind='diagram',diagram='revision_agent_roles',
    caption='Original teaching example: read-only diagnostics of a frozen case. The solver and tool interface are distinct roles.',
    note='A run_pf call should declare its case identity and return status, numerical outputs and an evidence identifier. The solver computes the electrical result. An LLM can choose another allowed diagnostic after seeing an error, or stop and escalate. A runtime carries state and executes those choices. No live switching permission is implied. A large or internally agentic service can still be exposed to this caller as a tool.'),
slide('Workflow and agent: who directs the next step?',[
    'In Anthropic’s terminology, a workflow follows code-defined paths; an agent lets the LLM direct some process and tool choices.',
    'Routing, parallel workers and repair loops can also be programmed workflows. A loop alone does not establish agency.'],
    refs=['DEF03','DEF04'],
    excerpt=['Programmed: load case → run flow → validate → report',
             'Model-directed: observe failure → choose a diagnostic',
             'Both still need code-enforced limits and stopping rules'],
    note='Attribute the fixed-code-path versus dynamic-direction distinction to this practitioner account. It is useful engineering terminology, not a universal taxonomy. Their workflow patterns include routing, orchestrator-workers and evaluator-optimizer loops. A supervisor may therefore combine deterministic prerequisites with an LLM selecting among permitted next tasks. This is the pattern later seen in PowerDAG.'),
slide('Agency is relative to a goal and an operating boundary',[
    'Wooldridge and Jennings emphasize autonomy, reactivity, goal-directed initiative and interaction with others.',
    'For a study assistant, autonomy may cover choosing diagnostics while the operator retains authority over operational actions.',
    'Specify observed evidence, permitted actions, a budget and the success or escalation condition.'],
    refs=['DEF02','DEF01'],
    note='These are the authors’ historical properties of their weak notion of agency, paraphrased as behavioral questions. Autonomy is relative to the assigned task; it does not imply unrestricted physical action. A rational action is judged against the available evidence and performance measure, rather than guaranteed eventual success. For a frozen v43 case, a complete unresolved report can satisfy an advisory contract when the study cannot be solved within its allowed diagnostic scope.'),
slide('Framework, platform and application identify different roles',[
    'LangGraph is an orchestration runtime for state, routing, persistence and execution.',
    'Harvard’s PowerAgent names a power-domain community and platform; PowerDAG is a specific research system.',
    'A numerical solver remains the component that evaluates the electrical model.'],
    refs=['DEF04','PA02','PD01'],
    note='These names occupy different levels and should not be treated as interchangeable agentic AI tools. LangGraph can execute both fixed and model-directed processes. PowerAgent develops domain models, interfaces and workflows; later slides identify a particular LangGraph example in its PowerWF repository. PowerDAG provides a distinct supervisory architecture. Naming a platform alone supplies neither a numerical-method guarantee nor a field-deployment result.'),
]

NEWS=[
slide('NYPA: agentic AI discussion and the data foundation',[
    'An October 2026 webinar features NYPA’s data-quality lead describing Databricks and Ataccama gates for meter data.',
    'The session separately demonstrates Genie requesting a data-trust assessment through Ataccama’s MCP service.',
    'NYPA’s contribution concerns meter-data pipelines; the agent demo uses a product/reorder table.'],
    refs=['N09','N10'],eyebrow='New York Power Authority · named speaker and implementation context',
    note='In this supplier-hosted webinar, NYPA’s data-quality lead describes quality controls for frequent meter data. The same session demonstrates a Genie assistant calling an Ataccama MCP service, but that demonstration uses a product/reorder data table rather than NYPA grid dispatch. Keep those evidence boundaries separate. October 2026 is used because the fetched live event and on-demand report show adjacent dates. These sources support a discussion of the data infrastructure agents need, not a production grid-command agent at NYPA. The earlier governance-agenda search result was excluded because the full original was unavailable.'),
slide('Eversource: an engineering path toward agentic workflows',[
    'Eversource has an established MATLAB–Synergi Electric workflow for probabilistic distribution studies.',
    'An October 2026 engineering vacancy explicitly calls for integrating agentic and AI-based workflows in MATLAB.',
    'This shows capability-building intent around grid studies; a vacancy does not prove an agent platform is deployed.'],
    refs=['N07','N11'],eyebrow='Eversource · existing simulation automation and a stated engineering direction',
    note='The April 2025 MathWorks account describes conventional Monte Carlo and parallel simulation automation. Its timing reduction must not be relabeled an agent result, so no agent-performance percentage is plotted. The October 2026 company posting names distribution-system modeling and automation and explicitly mentions agentic MATLAB workflows. It supports a narrower and more useful claim than invented deployment: the company is seeking to add this capability to an existing simulation environment.'),
]

POWERAGENT=[
slide('Harvard PowerAgent: a roadmap and domain ecosystem',[
    'Zhang and Xie’s 2025 IEEE roadmap organizes the effort around foundation models, tool interfaces and workflows.',
    'PowerFM targets domain modeling, PowerMCP connects capabilities, and PowerWF supplies study workflows.',
    'PowerAgent is the broader initiative; PowerAgentBench-Dyn later tests particular dynamic-study tasks.'],
    minutes=2,refs=['PA01','PA03','PA02','P01'],
    note='Full bibliographic identity: Qian Zhang and Le Xie, PowerAgent: A Road Map Toward Agentic Intelligence in Power Systems: Foundation Model, Model Context Protocol, and Workflow, IEEE Power and Energy Magazine 23(5), 93–101, September–October 2025, DOI 10.1109/MPE.2025.3579718. The concrete roadmap architecture here is supported by the full author presentation to ERCOT and official project page. The publisher/preprint download was unavailable during this review, so the slide does not attribute uninspected experimental results to that article. The community and its component repositories evolve; their live capabilities should not be treated as a frozen 2025 benchmark.'),
slide('PowerAgent example: study the impact of added load',[
    'The PowerWF Grid Impact Evaluation code implements a LangGraph study around PowerWorld.',
    'It compares baseline and modified-load power flow and contingencies, then summarizes the evidence.'],
    minutes=2,refs=['PA06','PA03','PA05'],main_ref='PA06',
    excerpt=['Inputs: PowerWorld case + bus + added MW',
             'baseline flow → baseline contingencies',
             'change load → flow → modified contingencies',
             'summary of the baseline / modified study'],
    note='This is a specific current author-maintained workflow example, not an inferred SDK for the entire PowerAgent initiative. Its graph.py imports StateGraph and ToolNode, stores workflow flags and routes the shared tools node back to the relevant step. The author presentation discusses data-center/load-growth studies with power-flow, congestion, voltage and N−1 evidence. Code and demonstrations establish the workflow structure; they do not provide a controlled utility timing or reliability estimate. The exact source file is linked in the full sources.'),
]

POWERDAG=[
slide('PowerDAG: supervise a distribution-grid tool workflow',[
    'PowerDAG combines workflow-aware exemplar retrieval with a prerequisite graph and a gate before execution.',
    'Its benchmark spans 108 tools, ten task families and four Vermont feeder models.'],
    minutes=2,refs=['PD01','PD02'],
    excerpt=['Retrieve relevant verified workflow examples',
             'propose a tool call with current arguments',
             'check required earlier Write-tool names',
             'execute, or return missing prerequisites'],
    note='Use the latest inspected v4, July 5, 2026: Emmanuel O. Badmus and Amritanshu Pandey, PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. Do not reuse the first version’s title or performance headlines. Four network models are Rochester, Stowe, Glover and South Hero. The system’s prerequisite graph guides tool context and gates calls while the supervising process remains iterative. Tool documentation alone may allow executable calls in the wrong study state; the gate addresses that workflow problem.'),
slide('PowerDAG checks prerequisites before a call executes',[
    'The paper’s example requires a solved network state before voltage-violation checks.',
    'A rejected call identifies the missing prerequisite so the agent can obtain it before retrying.'],
    minutes=2,refs=['PD01'],kind='diagram',diagram='revision_powerdag_gate',
    caption='Teaching adaptation: the current-v43 freshness condition adds an application check to the paper’s tool-history gate.',
    note='Section IV-C uses voltage-violation checking to illustrate stateful preconditions. Equation 9 formally checks required Write-tool names against executed tool names; that alone does not establish version-aware freshness. The diagram’s current-v43 requirement is an additional illustrative application condition. The introduction also explains how skipping a required network update can let a solver run on the wrong state. Appendix B provides a longer reported Stowe execution order: load_load, load_solar, load_distribution_network, create_and_initialize_model, build_constraints, build_objective, solve, update_network_voltages and plot_network_data. That listed order is not claimed to be the minimal set of dependency edges. Rule coverage is curated and unruled tools remain executable. Passing a declared prerequisite gate is not a numerical feasibility or safety proof.'),
slide('PowerDAG result: a controlled workflow comparison',[
    'Each GPT-5.5 configuration answers the same 150 held-out queries, with one run per query.',
    'Pass@1 checks expert workflow requirements, compatible arguments and dependency order; it is not field reliability.'],
    minutes=2,refs=['PD01'],kind='figure',image='powerdag_revision_result.png',
    visual_height_cm=3.55,visual_height_px=315,
    caption='PowerDAG v4, Table II: GPT-5.5 configurations. Whole-system ablation; no repeated-run interval is reported.',
    note='The four shown configurations score ReAct 77.33%, retrieval-only PowerChain-AR 92.67%, JIT-only 96.00% and full PowerDAG 98.00% (150 queries each). The study evaluates six configurations across ten model backends, totaling 9,000 query runs. Full PowerDAG reaches 97.33% with Gemini 3.1 Pro and 92.67% with Qwen 3.6-27B. Pass@1 is an automated workflow-correctness score against expert references. The held-out queries share the same ten task families as the exemplars; this is within-family holdout. It does not estimate field outage avoidance or command reliability. The comparison measures configurations as implemented and should not be interpreted as an isolated causal effect of one graph edge.'),
slide('PowerDAG: what is reproducible and what transfers?',[
    'The public benchmark includes tasks, tool documentation, an evaluator and workflow records.',
    'Three task families are fully runnable publicly; seven require proprietary feeder/GIS data and network tools.',
    'Transfer the prerequisite-checking idea, then validate the new tool contracts, case state and engineering acceptance tests.'],
    minutes=2,refs=['PD02','PD01'],
    note='The author README identifies BESS, basicPV and GFI as the three fully runnable public task families. The remaining seven depend on proprietary network functionality and feeder/GIS data. Public workflow records support inspection without proving every experiment can be rerun from a clean public download. The benchmark is a distribution-analysis research study using real feeder models, not evidence of a named utility operating a PowerDAG control-room agent. Later evaluation slides explain why a high score must retain its task population and definition.'),
]

def integrate(original):
    result=[]
    for index,item in enumerate(original):
        result.append(deepcopy(item))
        if index==0:result.extend(deepcopy(INTRO))
        if item['title']=='May 2026: National Grid reports agentic project assurance':result.extend(deepcopy(NEWS))
        if item['title']=='Power-system research asks different engineering questions':result.extend(deepcopy(POWERAGENT))
        if item['title']=='Parallel contingency studies need an explicit join':result.extend(deepcopy(POWERDAG))
    assert len(result)==len(original)+14
    return result
