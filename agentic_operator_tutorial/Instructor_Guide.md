# Instructor guide — agentic AI for power systems

80 static slides in one integrated 165-minute teaching route. Evidence reviewed 17 October 2026.

All slide content is visible at once. There are no slide transitions, motion effects, click reveals or tables. Each exercise is followed by a worked-answer slide. Show the question first, then advance for the debrief. The separate Full Reading Guide is untimed.

Every slide belongs to the session. The paper studies address power-system analysis, operation, planning or evidence tasks. LangGraph and DAG concepts are taught through those applications. The next workshop contains the detailed three GridGuard use cases.

## Cumulative teaching route

- 00:00–00:30 · 1. Agentic AI for Utility Operators (0.5 min)
- 00:30–02:00 · 2. What is agentic AI? (1.5 min)
- 02:00–03:30 · 3. Generative AI creates content (1.5 min)
- 03:30–05:00 · 4. What is an AI agent? (1.5 min)
- 05:00–06:30 · 5. An agent chooses a step. A tool runs it. (1.5 min)
- 06:30–09:30 · 6. Watch: how an agent chooses its next step (3 min)
- 09:30–11:00 · 7. An agent needs a clear goal and limits (1.5 min)
- 11:00–12:30 · 8. A model can use records, tools and memory (1.5 min)
- 12:30–14:30 · 9. PJM uses HyperQ to review connection applications (2 min)
- 14:30–16:30 · 10. HyperQ: what the reported numbers measure (2 min)
- 16:30–19:00 · 11. CAISO/OATI: agents help review planned outages (2.5 min)
- 19:00–21:30 · 12. Duke and AWS: agents help prepare planning studies (2.5 min)
- 21:30–23:30 · 13. Siemens announces agents for PSS E planning studies (2 min)
- 23:30–25:30 · 14. National Grid reports agents checking project plans (2 min)
- 25:30–27:00 · 15. NYPA: better data for agent use (1.5 min)
- 27:00–28:30 · 16. Eversource: adding agentic skills to grid studies (1.5 min)
- 28:30–30:00 · 17. GE Vernova: a platform that can connect grid tools (1.5 min)
- 30:00–32:00 · 18. Operators often work against a deadline (2 min)
- 32:00–33:30 · 19. Three checks for a useful recommendation (1.5 min)
- 33:30–35:00 · 20. A clear task makes success easier to test (1.5 min)
- 35:00–37:00 · 21. An LLM agent acts, reads the result and decides again (2 min)
- 37:00–38:30 · 22. When data are stale, the next step is to stop (1.5 min)
- 38:30–40:00 · 23. Unit checks catch a kV versus p.u. mistake (1.5 min)
- 40:00–41:30 · 24. A study must match the current grid connections (1.5 min)
- 41:30–43:30 · 25. A solver result depends on the problem it solves (2 min)
- 43:30–48:30 · 26. Exercise 1: check three returned data packets (5 min)
- 48:30–49:30 · 27. Exercise 1 answer: C passes the first checks (1 min)
- 49:30–51:00 · 28. Power-system papers test different tasks (1.5 min)
- 51:00–53:00 · 29. Harvard PowerAgent: models, tools and study workflows (2 min)
- 53:00–55:00 · 30. PowerAgent example: what changes when load is added? (2 min)
- 55:00–57:00 · 31. DrAgent: reading a recorded grid fault (2 min)
- 57:00–59:00 · 32. DrAgent selects tools to answer a fault question (2 min)
- 59:00–61:00 · 33. DrAgent: more correct answers, with errors still present (2 min)
- 61:00–63:00 · 34. Three kinds of graph have different jobs (2 min)
- 63:00–65:00 · 35. A DAG shows which result must come first (2 min)
- 65:00–67:00 · 36. LangGraph can pause to inspect a run (2 min)
- 67:00–69:30 · 37. LangGraph demo: pause, inspect and continue (2.5 min)
- 69:30–71:30 · 38. Saved state must identify the study and its evidence (2 min)
- 71:30–73:30 · 39. A checkpoint lets a workflow pause and resume (2 min)
- 73:30–75:30 · 40. Parallel outage studies must account for every case (2 min)
- 75:30–77:30 · 41. PowerDAG checks the steps needed before a tool runs (2 min)
- 77:30–79:30 · 42. PowerDAG: solve the grid before checking its voltage (2 min)
- 79:30–81:30 · 43. PowerDAG results: the same queries, four setups (2 min)
- 81:30–83:30 · 44. PowerDAG: what can others check and reuse? (2 min)
- 83:30–85:30 · 45. Simulation agents find functions, run code and repair errors (2 min)
- 85:30–87:30 · 46. Simulation-agent results: points, not a pass rate (2 min)
- 87:30–90:00 · 47. Trying again can repeat the same software error (2.5 min)
- 90:00–94:00 · 48. Siemens PSS E: agentic transmission planning (4 min)
- 94:00–96:00 · 49. GridMind 2025 connects typed agents to solvers (2 min)
- 96:00–98:00 · 50. GridMind: reported answers need independent checks (2 min)
- 98:00–100:30 · 51. GridMind 2026 reuses results when their inputs still match (2.5 min)
- 100:30–102:30 · 52. GridMind: which changes need a new run? (2 min)
- 102:30–105:00 · 53. GridMind results: fewer stages and less time are different (2.5 min)
- 105:00–111:00 · 54. Exercise 2: check whether saved weather-risk results still apply (6 min)
- 111:00–113:00 · 55. Exercise 2 answer: rerun what changed (2 min)
- 113:00–115:30 · 56. PowerAgentBench-Dyn allows only specific model changes (2.5 min)
- 115:30–118:00 · 57. PowerAgentBench-Dyn results: passed sessions and updates (2.5 min)
- 118:00–120:30 · 58. PowerAgentBench-Dyn also checks grid response to faults (2.5 min)
- 120:30–122:30 · 59. VeraGrid-Agent uses solver results to answer a question (2 min)
- 122:30–124:30 · 60. VeraGrid-Agent results: the same models with and without tools (2 min)
- 124:30–126:30 · 61. AgentiGrid: what does one reported run mean? (2 min)
- 126:30–128:30 · 62. A lower cost can come from solving the wrong task (2 min)
- 128:30–131:00 · 63. Successful tool calls can still miss a critical outage (2.5 min)
- 131:00–133:30 · 64. Show both trial counts and uncertainty (2.5 min)
- 133:30–135:30 · 65. PowerBench finds answers across linked records (2 min)
- 135:30–137:30 · 66. PowerBench results: complete answers and partial credit (2 min)
- 137:30–139:30 · 67. A strong average can hide a weak task group (2 min)
- 139:30–141:30 · 68. What do ten successful trials tell us? (2 min)
- 141:30–143:30 · 69. More required steps can lower overall reliability (2 min)
- 143:30–146:00 · 70. The answer changes when we change what we count (2.5 min)
- 146:00–148:30 · 71. Zero test failures do not prove perfect performance (2.5 min)
- 148:30–150:30 · 72. Choose tests that can reveal failures (2 min)
- 150:30–152:30 · 73. MCP connects a workflow to its tools (2 min)
- 152:30–154:30 · 74. A retrieved document cannot give itself permission (2 min)
- 154:30–156:30 · 75. Measure the whole job, including human review (2 min)
- 156:30–158:30 · 76. Test whether the assistant helps on comparable tasks (2 min)
- 158:30–160:00 · 77. Power-sector testbeds provide places to evaluate agents (1.5 min)
- 160:00–162:00 · 78. GridGuard: what should this prototype prove? (2 min)
- 162:00–163:00 · 79. Next tutorial: check the proposed action (1 min)
- 163:00–165:00 · 80. Discussion and full sources (2 min)

## 1. Agentic AI for Utility Operators

**Timing:** 00:00–00:30 (0.5 minutes).

All slides belong to the main presentation. The opening distinguishes systems in use, utility statements and product announcements. Every agent-research paper covers a power-system task. We explain LangGraph and task dependency graphs through fault analysis and weather-risk studies. A separate follow-on workshop covers the detailed GridGuard cases on voltage, restoration and cyber events.

**Full sources:**

IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources

## 2. What is agentic AI?

**Timing:** 00:30–02:00 (1.5 minutes).

The first sentence is our summary, not a quotation or a standard definition. Anthropic includes both programmed workflows and LLM-directed agents under agentic systems. Wooldridge and Jennings also discuss different definitions of an agent. The later examples focus on engineering systems using large language models, or LLMs. “Agentic” describes how the whole system pursues a task. It is not another software component beside the agent. A system can use just one agent. Source: NVIDIA Technical Blog, Figure 1. The three examples show interaction patterns, not a universal taxonomy or a claim that tool use alone proves autonomy. Source figure locator: Figure 1. Original source URL: https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/

**Full sources:**

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

Michael Wooldridge, Nicholas R. Jennings. Intelligent agents: theory and practice. The Knowledge Engineering Review, 10(2), pp. 115–152. 1995.
Full source: https://doi.org/10.1017/S0269888900008122
Full paper: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95.pdf

Eduardo Alvarez, Benjamin Klieger, Graham Steele. Building for the Rising Complexity of Agentic Systems with Extreme Co-Design. NVIDIA Technical Blog. May 5, 2026.
Full source: https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/

## 3. Generative AI creates content

**Timing:** 02:00–03:30 (1.5 minutes).

NIST AI 600-1 describes generative AI in terms of producing synthetic content, including text, images, audio and other media. This diagram shows one generation call: selected records and a request enter a model, which produces a draft. It does not say every generative-AI application is a single call. An LLM-based agent can use a generative model inside a repeated decision process. These categories describe different roles, not three mutually exclusive technologies or stages of a historical evolution. Generated wording is not itself numerical grid evidence; a study report should cite the engineering records used.

**Full sources:**

National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. NIST AI 600-1. July 2024.
Full source: https://doi.org/10.6028/NIST.AI.600-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

## 4. What is an AI agent?

**Timing:** 03:30–05:00 (1.5 minutes).

The equation is teaching notation: the policy uses the history of observations to choose the next action. It is not the textbook’s exact notation. The agent function is this abstract mapping, and a program implements it. A grid-study agent may observe case files and solver logs, then call a tool, ask for information or return a report. This classical definition predates LLMs. It also includes many older forms of automation. The linked sample chapter is from the second edition, even though its URL says fourth edition. The reading guide records that difference. Teaching notation: a_t = pi(o_1, ..., o_t), a rule mapping past observations to the next action. The original textbook figure replaces the teaching redraw. The question mark represents the agent’s decision mechanism; observations enter through sensors and actions leave through actuators. This is the author-hosted older chapter draft, cited as second edition.

**Full sources:**

Stuart J. Russell, Peter Norvig. Artificial Intelligence: A Modern Approach, Chapter 2: Intelligent Agents. Prentice Hall, second edition, Chapter 2, pp. 32–58. 2003.
Full source: https://aima.cs.berkeley.edu/2nd-ed/
Full paper: https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf

## 5. An agent chooses a step. A tool runs it.

**Timing:** 05:00–06:30 (1.5 minutes).

A run_pf request should identify the study case. Its response should include status, numerical results and an evidence ID. The solver computes the electrical result. After an error, an LLM may choose another allowed check or stop and ask for help. The runtime software saves progress and carries out those choices. This example gives no permission to switch live equipment. A service may contain its own agents and still act as a tool for the agent calling it. Source: NVIDIA Technical Blog, Figure 1. This is a published conceptual design; separate memory or planning modules are not required in every AI agent. Source figure locator: Figure 1: General components of an agent. Original source URL: https://developer.nvidia.com/blog/introduction-to-llm-agents/

**Full sources:**

LangChain maintainers. Tools. Docs by LangChain, Python open-source documentation. Accessed 17 October 2026.
Full source: https://docs.langchain.com/oss/python/langchain/tools

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

Stuart J. Russell, Peter Norvig. Artificial Intelligence: A Modern Approach, Chapter 2: Intelligent Agents. Prentice Hall, second edition, Chapter 2, pp. 32–58. 2003.
Full source: https://aima.cs.berkeley.edu/2nd-ed/
Full paper: https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf

Tanay Varshney. Introduction to LLM Agents. NVIDIA Technical Blog. November 30, 2023.
Full source: https://developer.nvidia.com/blog/introduction-to-llm-agents/

## 6. Watch: how an agent chooses its next step

**Timing:** 06:30–09:30 (3 minutes).

Play 0:43 to 3:28, a two-minute-forty-five-second excerpt. The publisher’s chapters cover the meaning of agentic behavior and workflow examples. Explain the distinction: a fixed workflow follows routes set in code; a model-based agent chooses some next steps using the information returned so far. Connect this to our grid example: an operator states a study goal, the agent calls a numerical solver, reads the result and either requests another allowed step or reports back. The solver performs the engineering calculation. The operator keeps the operating decision. These grid roles are our teaching analogy, rather than a claim that the video demonstrates grid control.

**Full sources:**

Aja Hammerly, Jason Davenport. Agentic AI: Workflows vs. agents. Google Cloud Tech / YouTube. 19 March 2025.
Full source: https://www.youtube.com/watch?v=Qd6anWv0mv0

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

## 7. An agent needs a clear goal and limits

**Timing:** 09:30–11:00 (1.5 minutes).

This is an illustrative advisory-study policy informed by classical work on agency. Wooldridge and Jennings discuss autonomy, response to change, initiative and interaction; they do not prescribe this grid-operator approval process. The example gives the agent permission to run agreed studies and prepare evidence. The operator can request changes, stop the process or approve a later operating action. This diagram does not give the agent direct control of physical equipment. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. This is a generic software demonstration, not an operator dispatch interface or a utility deployment. Source figure locator: Interrupt response schema / Studio form. Original source URL: https://docs.langchain.com/oss/python/langgraph/interrupts

**Full sources:**

Michael Wooldridge, Nicholas R. Jennings. Intelligent agents: theory and practice. The Knowledge Engineering Review, 10(2), pp. 115–152. 1995.
Full source: https://doi.org/10.1017/S0269888900008122
Full paper: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95.pdf

Stuart J. Russell, Peter Norvig. Artificial Intelligence: A Modern Approach, Chapter 2: Intelligent Agents. Prentice Hall, second edition, Chapter 2, pp. 32–58. 2003.
Full source: https://aima.cs.berkeley.edu/2nd-ed/
Full paper: https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf

LangChain documentation maintainers. LangGraph Interrupts. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/interrupts

## 8. A model can use records, tools and memory

**Timing:** 11:00–12:30 (1.5 minutes).

These names refer to different roles. LangGraph can run both fixed workflows and processes where a model chooses steps. PowerAgent develops power-system models, tool interfaces and workflows. Later slides show a specific LangGraph example in its PowerWF repository. PowerDAG has its own supervisory design. A platform name alone does not establish numerical accuracy or deployment at a utility. The published figure shows an augmented language model. Retrieval, tools and memory are supporting capabilities; they are not mandatory in every agent. The diagram is reproduced from Anthropic with only empty margins trimmed in the display. The original image bytes are retained.

**Full sources:**

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

LangChain maintainers. LangGraph overview. Docs by LangChain, Python open-source documentation. Undated live documentation; accessed 2026-10-17.
Full source: https://docs.langchain.com/oss/python/langgraph/overview

Power and AI Initiative / PowerAgent community, Harvard SEAS. PowerAgent — Open-Source Agentic AI for Power Grids. Official Harvard project website. Live project page reviewed 17 October 2026.
Full source: https://poweragent.seas.harvard.edu/

Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4

## 9. PJM uses HyperQ to review connection applications

**Timing:** 12:30–14:30 (2 minutes).

Tapestry’s 11 June report covers 811 generation applications. Agents perform limited document and evidence tasks. The report does not establish an agent making a power-flow conclusion or an automatic regulatory decision. The system guides the agents’ work and records evidence citations. The article describes migration to Google ADK as future work, so do not label the deployed system an established ADK implementation. Tapestry, HyperQ Field Notes, June 11, 2026 Supplier report of deployment. PJM separately confirmed earlier testing. The hero is a still captured from the publisher's animation, not an independently verified live PJM application record. Original page: https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1

**Takeaway:** A numerical study needs reliable input evidence.

**Full sources:**

Tapestry. Field Notes  /  HyperQ deployment in PJM’s Cycle 1. 2026-06-11; deployment entry 2026-04-29.
Full source: https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1

Tapestry. How agentic AI can help grid operators speed up interconnection. 2025.
Full source: https://www.tapestryenergy.com/en/projects/how-agentic-ai-can-help-grid-operators-speed-up-interconnection

PJM Interconnection. Successful Interconnection Reforms, Other PJM Initiatives Seek To Maximize Electricity Supplies. 2026-03-16.
Full source: https://insidelines.pjm.com/connected/

## 10. HyperQ: what the reported numbers measure

**Timing:** 14:30–16:30 (2 minutes).

The supplier reports grouping 4,581 raw site-control documents into 2,328 bundles and checking four criteria. The graphic’s 9,312 macro-assessments are not 9,312 projects. The full interconnection process also includes document transfer and human review. The report gives no confusion matrix or accuracy denominator. We omit its historical 20x headline because it compares manual work with computer processing using different work and timing boundaries.

**Full sources:**

Tapestry. Field Notes  /  HyperQ deployment in PJM’s Cycle 1. 2026-06-11; deployment entry 2026-04-29.
Full source: https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1

## 11. CAISO/OATI: agents help review planned outages

**Timing:** 16:30–19:00 (2.5 minutes).

California ISO’s July 2025 account described a pilot. OATI’s 2026 field report describes daily production use but gives no exact production start date. The reported inequalities imply more than 62.5 requests per minute for the batch. They do not describe individual request latency. Do not compare eight machine-minutes with a separate analyst-hours figure as though both came from the same trial. The work prepares outage analysis and operating evidence. Reviewers make final decisions.

**Takeaway:** A processing rate needs a clear work boundary and a measure of the review left for people.

**Full sources:**

California ISO. Exploring AI to support smarter grid management. 2025-07-28.
Full source: https://www.caiso.com/about/news/energy-matters-blog/exploring-ai-to-support-smarter-grid-management

OATI. Generative and Agentic AI in Grid Operations: Field Lessons from OATI, CAISO, PNNL, and EPRI. 2026 (exact publication day not displayed).
Full source: https://www.oati.com/ai-for-energy/

OATI (California ISO control-room photograph). California ISO control room, image published by OATI: California ISO control room with operators seated at curved desks facing a long wall of grid displays. Image accessed 17 October 2026.
Full source: https://www.oati.com/ai-genie/

## 12. Duke and AWS: agents help prepare planning studies

**Timing:** 19:00–21:30 (2.5 minutes).

AWS’s 17 September 2026 announcement names Duke engineers using agents to coordinate studies. The agents prepare inputs and coordinate existing physics software, models and scripts. The report says data preparation fell from two weeks of manual work to hours. It gives neither the final number of hours nor a sample count. It identifies no SDK, model or runtime. Do not infer Strands or AgentCore from the cloud provider. Engineers make final decisions.

**Takeaway:** Faster preparation alone does not establish a shorter full regulatory process.

**Full sources:**

Amazon Web Services. AWS Launches Agentic Grid Planning Program to Accelerate Interconnection Studies. 2026-09-17.
Full source: https://press.aboutamazon.com/aws/2026/9/aws-launches-agentic-grid-planning-program-to-accelerate-interconnection-studies

Amazon Web Services. Agentic Grid Planning on AWS. Undated; reviewed 17 October 2026.
Full source: https://aws.amazon.com/energy-utilities/agentic-grid-planning/

Duke Energy / illumination. Duke Energy, illumination, August 2, 2022: Duke Energy grid operator Howard Greene seated before many control-room displays. Image accessed 17 October 2026.
Full source: https://illumination.duke-energy.com/articles/meet-the-team-that-monitors-the-grid-and-keeps-the-lights-on

## 13. Siemens announces agents for PSS E planning studies

**Timing:** 21:30–23:30 (2 minutes).

The same release describes Alliander’s migration to the platform. That shows platform adoption, not use of the newly announced agentic PSS E features. The claim of up to 50% faster study response has no disclosed benchmark method, so we do not plot it. The announcement shows a possible integration path: agents coordinate an established simulation environment. Siemens AG, press release, May 5, 2026 Product announcement. The separately named Alliander platform migration does not prove production use of the new agentic PSS E capability. Original page: https://press.siemens.com/global/en/pressrelease/siemens-gridscale-x-redefines-system-operations-and-agentic-transmission-planning

**Takeaway:** Check product features and measured utility results separately.

**Full sources:**

Siemens. Siemens’ Gridscale X redefines system operations and agentic transmission planning. 2026-05-05.
Full source: https://press.siemens.com/global/en/pressrelease/siemens-gridscale-x-redefines-system-operations-and-agentic-transmission-planning

## 14. National Grid reports agents checking project plans

**Timing:** 23:30–25:30 (2 minutes).

The CEO’s 14 May 2026 results transcript reports agentic project-assurance use. “Capital control tower” names the system supporting project checks. Later comments about optimizing access outages describe future plans. Do not attribute nearby FLISR, outage-minute or gas-crew results to this agent. The source verifies reported use without supporting a numerical performance estimate.

**Full sources:**

National Grid. National Grid Full Year Results 2025/26: Video Webcast Transcript. 2026-05-14.
Full source: https://www.nationalgrid.com/document/577036/download

## 15. NYPA: better data for agent use

**Timing:** 25:30–27:00 (1.5 minutes).

This supplier-hosted webinar discusses NYPA’s quality checks for frequently arriving meter data. The separate demo uses Genie and an Ataccama MCP service with a product/reorder table. MCP, the Model Context Protocol, is a standard way to connect AI systems to tools and data. Keep the NYPA implementation and the generic agent demo separate. We use October 2026 because the fetched event and on-demand report show adjacent dates. These sources support the discussion of data agents need, without establishing a production grid-command agent at NYPA. We excluded the earlier governance-agenda search result because the full original was unavailable. Ataccama, original webinar report with NYPA Data Quality Lead Saptaparna Gupta, October 14, 2026 NYPA discusses meter-data quality checks. The separate product/reorder demo does not establish a production NYPA grid-control agent. Original page: https://www.ataccama.com/webinar/on-demand-trust-driven-medallion-architecture

**Full sources:**

Session speakers: Saptaparna Gupta (NYPA), Oleksandra Bovkun (Databricks), Eliza Pochinova (Ataccama). On demand: Trust-driven medallion architecture: How to make your CDEs ready for AI. Ataccama. 2026.
Full source: https://www.ataccama.com/webinar/on-demand-trust-driven-medallion-architecture

Saptaparna Gupta (NYPA), Oleksandra Bovkun (Databricks), Eliza Pochinova (Ataccama). Trust-driven medallion architecture: how to make your CDEs ready for AI. Ataccama. 2026-10-13, 11:00 AM EDT (date displayed on fetched event page).
Full source: https://www.ataccama.com/events/trust-driven-medallion-architecture

## 16. Eversource: adding agentic skills to grid studies

**Timing:** 27:00–28:30 (1.5 minutes).

The April 2025 MathWorks report describes probabilistic distribution studies. These use Monte Carlo sampling and parallel numerical simulations to examine many possible conditions. Its timing improvement belongs to conventional simulation automation, so we do not show it as an agent result. Eversource’s October 2026 posting concerns distribution-system modeling and automation and explicitly mentions agentic MATLAB workflows. It shows the company seeking this capability for an existing simulation environment. Eversource Energy, official engineering vacancy, October 5, 2026 Engineering skill requirement and integration intent. The posting later explicitly mentions agentic MATLAB workflows, but a vacancy does not prove deployment. Original page: https://jobs.eversource.com/job/east-berlin/distribution-system-modeling-and-automation-engineer-hybrid-schedule/7774/101576695504

**Full sources:**

Eversource Energy (employer). Distribution System Modeling and Automation Engineer (Hybrid Schedule). Eversource Energy. 2026-10-05.
Full source: https://jobs.eversource.com/job/east-berlin/distribution-system-modeling-and-automation-engineer-hybrid-schedule/7774/101576695504

MathWorks; named Eversource engineer John Kreso quoted. Eversource Energy Collaborates with MathWorks to Incorporate Renewable Energy Sources into System Planning Process Using Probabilistic Load Flow Automation. MathWorks. 2025-04-29.
Full source: https://www.mathworks.com/company/newsroom/eversource-energy-collaborates-with-mathworks-to-incorporate-renewable-energy-sources-into-system-planning-process-using-probabilistic-load-flow-automation.html

## 17. GE Vernova: a platform that can connect grid tools

**Timing:** 28:30–30:00 (1.5 minutes).

This GE example concerns GE Vernova’s electric-power business. The February 2026 GridOS announcement names a utility context. It does not establish a specific autonomous LLM controller. Our teaching example explains what an integrated agent would also need: clear tool interfaces, saved state, evidence checks and limits on its authority.

**Takeaway:** For each case, identify the customer, task, agent’s role and measured result.

**Full sources:**

GE Vernova. GE Vernova Launches GridOS for Distribution, the Industry's First Unified Solution for Grid Orchestration. 2026-02-03.
Full source: https://www.gevernova.com/news/press-releases/ge-vernova-launches-gridos-distribution-industrys

GE Vernova. GE Vernova: GE Vernova GridOS promotional control-room composite with people and grid software displays. Image accessed 17 October 2026.
Full source: https://www.gevernova.com/software/products/gridos

## 18. Operators often work against a deadline

**Timing:** 30:00–32:00 (2 minutes).

The 61% is an average share of tasks performed or supported. It is not the percentage of operators. The source gives neither the task denominator nor variance. Twenty respondents do not support a binomial interval for that 61%. Seventy-five survey items do not imply 1,500 independent timing observations. This small self-report study is not a national estimate. Ask which tasks need quick decisions and which allow more investigation.

**Takeaway:** Measure the operator’s total effort and deadline alongside AI response time.

**Full sources:**

Corey Fallon, Brett Jefferson, Tyler Ryan. An Analysis of Grid Operators. Pacific Northwest National Laboratory. 2023-04-19.
Full source: https://www.pnnl.gov/sites/default/files/media/file/PNNL_workshop_Presentation_Human_Factors_Virtual_Workshop_March_2023.pdf

PJM Interconnection. What Happens in the Control Room. 2026-04-16.
Full source: https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/fact-sheets/what-happens-in-the-control-room-fact-sheet.pdf

Duke Energy / illumination. Duke Energy, illumination, August 2, 2022: Duke Energy employees in an Energy Control Center, with one pointing toward a display. Image accessed 17 October 2026.
Full source: https://illumination.duke-energy.com/articles/meet-the-team-that-monitors-the-grid-and-keeps-the-lights-on

## 19. Three checks for a useful recommendation

**Timing:** 32:00–33:30 (1.5 minutes).

These are separate checks. A correctly formatted call may still use old grid connections. An optimization may converge after changing a variable the user was not allowed to change. A correct result may still leave part of the decision unanswered. These checks form the acceptance contract: the agreed conditions a result must meet. We reuse it in the examples and exercises. This original utility screenshot provides a concrete example of displayed evidence to inspect. It is conventional situational-awareness software, not an agent implementation or a claim that the slide’s three checks were measured by CAISO.

**Takeaway:** Agree on acceptance checks for the whole task.

**Full sources:**

John Phipps. Control center modernization is enhancing reliability. California ISO. 2025-09-10.
Full source: https://www.caiso.com/about/news/energy-matters-blog/control-center-modernization-is-enhancing-reliability

## 20. A clear task makes success easier to test

**Timing:** 33:30–35:00 (1.5 minutes).

All F12 records and policies are invented teaching data, not utility operating rules. A snapshot identifies the data time, grid-connection version and model revision. Start by identifying the user, the result they need and the actions they may take. Success means meeting these agreed requirements. Answer length and the number of tool calls do not establish success. The real product screen illustrates the grid information a bounded task may use. The acceptance contract on this slide remains an original teaching example.

**Takeaway:** A clear task gives us a clear way to check success.

**Full sources:**

GE Vernova. GridOS Visual Intelligence product screens. Accessed 17 October 2026.
Full source: https://www.gevernova.com/software/products/gridos/visual-intelligence

## 21. An LLM agent acts, reads the result and decides again

**Timing:** 35:00–37:00 (2 minutes).

The equation describes a software interface. It does not assume we observe the full physical system or that the history has the Markov property, meaning it contains everything needed to predict the next state. The model chooses a request using the goal and previous evidence. The software runs a service against a specific input snapshot. A historian, which stores time-stamped measurements, returns measured data. A simulator returns model results. Selecting either tool does not turn its output into a command to physical equipment. This is the original published conceptual agent pattern, not a measured utility or PowerAgent implementation. The display trims only empty margins. Feedback does not automatically mean model weights are being retrained.

**Takeaway:** Check the tool requests, their inputs and their results.

**Full sources:**

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).
Full source: https://arxiv.org/pdf/2512.20789v1

## 22. When data are stale, the next step is to stop

**Timing:** 37:00–38:30 (1.5 minutes).

A trace records the sequence of tool requests and results. Use the gate in this published figure to discuss an application check. As a spoken example, a study trace should record case IDs, data times and the returned results. When required data are unavailable or out of date, the system should say so. It must not invent a value or silently reuse an older one. Check whether the agent detects the problem and asks for the right update. A trace makes this inspection possible but does not itself prove the work is correct. Source: Anthropic, Building effective agents (December 19, 2024). A generic content-workflow pattern, not a physical-feasibility or utility-safety guarantee. Source figure locator: Workflow: Prompt chaining. Original source URL: https://www.anthropic.com/engineering/building-effective-agents

**Full sources:**

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

## 23. Unit checks catch a kV versus p.u. mistake

**Timing:** 38:30–40:00 (1.5 minutes).

The software interface must enforce units. Prompt wording alone is insufficient. The same number can mean very different physical quantities. Check unit labels, the chosen base and the asset ID in software. A valid type or unit still does not prove that the measurement or model is accurate. The diagram shows both the error and the information needed to fix it.

## 24. A study must match the current grid connections

**Timing:** 40:00–41:30 (1.5 minutes).

Point to the switch that changed. The old result represents different grid connections, rather than simply an older timestamp. Version matching is a necessary consistency check. It still leaves two questions: does the model represent the real grid accurately, and do the refreshed measurements represent the event?

## 25. A solver result depends on the problem it solves

**Timing:** 41:30–43:30 (2 minutes).

Keep solver status, equation errors (residuals) and modeled limit checks separate from whether the analysis covers the full request. A solver can converge on the wrong problem. The study requirements must state constraints and tolerances, meaning the allowed numerical error. This slide sets no universal voltage or loading limit. Permission to act remains a separate software and organizational decision. Source: Anthropic, Building effective agents (December 19, 2024). The picture illustrates routing; it does not establish an implemented power-system workflow. Source figure locator: Workflow: Routing. Original source URL: https://www.anthropic.com/engineering/building-effective-agents

**Takeaway:** Report the problem and assumptions together with the solver result.

**Full sources:**

Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1

GridGuard project / local source snapshot. GridGuard current project: README and graph source snapshot. 2026.
Full source: ../research/GridGuard_source_snapshot.txt

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

## 26. Exercise 1: check three returned data packets

**Timing:** 43:30–48:30 (5 minutes).

Show only the question during the activity. Use the following worked-answer slide for the debrief. Allow 1 minute to inspect, 2 minutes in pairs, 2 minutes to share and 1 minute to debrief. age_s means age in seconds. Only C passes the stated initial checks. A has the wrong grid version. B has the wrong unit. C still needs the right asset mapping, a valid model, the required engineering checks, enough scenario coverage and an explanation people can review. The user may advise but cannot execute actions. The 60-second rule is made up for this exercise. It is not a general operating standard.

## 27. Exercise 1 answer: C passes the first checks

**Timing:** 48:30–49:30 (1 minutes).

Reveal after the pairs share their decisions. A is recent but uses v42. B is recent and uses v43, but has kV instead of p.u. C is 45 seconds old, uses v43 and has p.u. units. C passes the three stated checks only. Asset mapping, model validity, engineering checks and scenario coverage remain necessary. Recommendation permission does not authorize execution.

## 28. Power-system papers test different tasks

**Timing:** 49:30–51:00 (1.5 minutes).

Every paper that follows concerns power systems. They measure different outcomes, so their percentages cannot form a ranking across papers. The numerical solver computes the engineering result. The language model selects tools and helps interpret the returned evidence. This source photograph introduces the power-sector research context. It does not picture the paper experiments.

**Full sources:**

Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

Mengshuo Jia, Zeyu Cui, Gabriela Hug. Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework. IEEE Transactions on Smart Grid, volume 16, issue 6, pages 5556–5572. 2025.
Full source: https://doi.org/10.1109/TSG.2025.3589114
Full paper: https://arxiv.org/pdf/2411.16707v3

Yan Zhang, Ahmad Mohammad Saber, Amr Youssef, Deepa Kundur. Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control. arXiv preprint. 2025-09-08 (v3); first submitted 2025-08-07.
Full source: https://arxiv.org/pdf/2508.05702v3

Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).
Full source: https://arxiv.org/abs/2609.34492v1
Full paper: https://arxiv.org/pdf/2609.34492v1

NVIDIA. Image published by NVIDIA with its EPRI Open Power AI Consortium announcement, March 20, 2025: Transmission towers and power lines with city lights in the background at dusk. Image accessed 17 October 2026.
Full source: https://blogs.nvidia.com/blog/open-power-ai-consortium/

## 29. Harvard PowerAgent: models, tools and study workflows

**Timing:** 51:00–53:00 (2 minutes).

Full citation: Qian Zhang and Le Xie, PowerAgent: A Road Map Toward Agentic Intelligence in Power Systems: Foundation Model, Model Context Protocol, and Workflow, IEEE Power and Energy Magazine 23(5), 93–101, September–October 2025, DOI 10.1109/MPE.2025.3579718. A foundation model is a pretrained model intended for reuse across tasks. We verified the architecture through the authors’ full ERCOT presentation and official project page. The publisher/preprint download was unavailable, so we attribute no uninspected experimental results to the article. The community and repositories keep changing. Their current features are not a fixed 2025 benchmark. Le Xie; slides credit Le Xie and Qian Zhang; A Roadmap Towards Agentic Intelligence in Power Systems; Author presentation slide 11 Roadmap from the December2025 author presentation; not a measured deployment or a frozen specification of every current PowerAgent repository. Source locator: Author presentation slide 11; three layer panels in the left column. Original URL: https://www.ercot.com/files/docs/2025/12/01/4-Guest-Presentation-A-Roadmap-toward-Agentic-Intelligence-in-Power-Systems.pdf

**Full sources:**

Qian Zhang, Le Xie. PowerAgent: A Road Map Toward Agentic Intelligence in Power Systems: Foundation Model, Model Context Protocol, and Workflow. IEEE Power and Energy Magazine, volume 23, issue 5, pages 93–101. 2025.
Full source: https://doi.org/10.1109/MPE.2025.3579718

Le Xie; slides credit Le Xie and Qian Zhang. A Roadmap Towards Agentic Intelligence in Power Systems. ERCOT Technology and Security Committee guest presentation. 8 December 2025.
Full source: https://www.ercot.com/files/docs/2025/12/01/4-Guest-Presentation-A-Roadmap-toward-Agentic-Intelligence-in-Power-Systems.pdf

Power and AI Initiative / PowerAgent community, Harvard SEAS. PowerAgent — Open-Source Agentic AI for Power Grids. Official Harvard project website. Live project page reviewed 17 October 2026.
Full source: https://poweragent.seas.harvard.edu/

Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1

## 30. PowerAgent example: what changes when load is added?

**Timing:** 53:00–55:00 (2 minutes).

This is a specific current workflow maintained by the authors. It does not establish one SDK for the whole PowerAgent initiative. In the code, graph.py imports StateGraph and ToolNode, saves workflow flags and returns from the shared tools node to the relevant step. A bus is a connection point in the model. The author presentation discusses load-growth and data-center studies using power flow, congestion, voltage and N−1 checks, which examine single-component outages. The code and demonstrations show the workflow. They provide no controlled utility timing or reliability estimate. The reading guide links the exact source file. Le Xie; slides credit Le Xie and Qian Zhang; A Roadmap Towards Agentic Intelligence in Power Systems; Author presentation slide 14, right-hand grid-impact process A conceptual author demonstration. It is not an exact diagram of the later PowerWF graph.py or a utility performance trial. Source locator: Author presentation slide 14, right-hand grid-impact process. Original URL: https://www.ercot.com/files/docs/2025/12/01/4-Guest-Presentation-A-Roadmap-toward-Agentic-Intelligence-in-Power-Systems.pdf

**Full sources:**

PowerAgent / PowerWF community contributors. PowerWF Grid Impact Evaluation — LangGraph workflow source. Author-maintained source code, Grid Impact Evaluation/src/agent/graph.py. Live source inspected 17 October 2026.
Full source: https://github.com/Power-Agent/PowerWF/blob/main/Grid%20Impact%20Evaluation/src/agent/graph.py

Le Xie; slides credit Le Xie and Qian Zhang. A Roadmap Towards Agentic Intelligence in Power Systems. ERCOT Technology and Security Committee guest presentation. 8 December 2025.
Full source: https://www.ercot.com/files/docs/2025/12/01/4-Guest-Presentation-A-Roadmap-toward-Agentic-Intelligence-in-Power-Systems.pdf

PowerAgent community contributors. Power-Agent/PowerWF. Author-maintained GitHub repository. Live source repository reviewed 17 October 2026.
Full source: https://github.com/Power-Agent/PowerWF

## 31. DrAgent: reading a recorded grid fault

**Timing:** 55:00–57:00 (2 minutes).

The Hitachi Energy paper studies disturbance analysis on transmission lines. This is an original figure extracted from the research paper, not an invented event or a live operating screen. First identify how the curve changes. Numerical tools return a sample index or current measurement. The task still requires an engineering interpretation of those values.

**Full sources:**

Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

## 32. DrAgent selects tools to answer a fault question

**Timing:** 57:00–59:00 (2 minutes).

ReWOO plans the work before running tools that use earlier results. COMTRADE is a format for recorded power-system disturbances. The implementation uses Gemini 1.5Pro for planning, a dozen domain functions and retrieval-augmented generation (RAG) over 138 product manuals. RAG retrieves relevant source text for the model. The displayed picture is the paper’s original architecture. The following dependency example is a spoken teaching example. To convert a fault’s starting sample to seconds, the system first needs both the sample index and sampling rate. This dependency motivates the next graph explanation. Barun Kumar Saha, Aarthi V, O. D. Naidu; DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models; Figure 1, PDF page 2 Paper architecture based on ReWOO; the picture does not establish utility deployment or autonomous command authority. Source locator: Figure 1, PDF page 2. Original URL: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf

**Full sources:**

Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

## 33. DrAgent: more correct answers, with errors still present

**Timing:** 59:00–61:00 (2 minutes).

Fault inception: baseline 12/18, agent 18/18. Maximum current: baseline 16/18, agent 18/18. Clearance/timing: baseline 4/18, agent 13/18. The paper allows 3 ms timing error and 5% current error. One expert graded the answers. Q6 footnote 8 accepts a correctly labeled duration, so these are not strictly clearance-timestamp accuracy counts. The printed Q6 mean conflicts with the individual cells. This chart therefore uses the audited cell counts.

**Full sources:**

Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

## 34. Three kinds of graph have different jobs

**Timing:** 61:00–63:00 (2 minutes).

A radial feeder has a tree-like electrical layout, but its software can still contain loops. A calculation graph without loops can analyze a meshed electrical network. State which graph you mean before discussing a node, connection or loop. A software architecture drawing is not the electrical model.

**Full sources:**

Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

## 35. A DAG shows which result must come first

**Timing:** 63:00–65:00 (2 minutes).

Every task must follow the tasks that produce its inputs. This is a valid topological order. Fault-start sample and sampling rate must both exist before the time conversion runs. Finding maximum current can run independently of that conversion when both use the same unchanged record. Dependencies determine which tasks can run together. The positions of boxes in a drawing do not.

**Full sources:**

Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

## 36. LangGraph can pause to inspect a run

**Timing:** 65:00–67:00 (2 minutes).

LangGraph is software for running workflows. It can support loops, unlike a DAG. StateGraph defines stored state fields and workflow nodes. Application-defined reducers specify how updates from parallel steps combine. A node may call an engineering tool with fixed rules or an AI model. The application must define validation, stopping and permissions. Running the graph does not prove that an electrical solution is feasible. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. A static debug breakpoint differs from a dynamic interrupt requesting human input. Source figure locator: Debugging with interrupts. Original source URL: https://docs.langchain.com/oss/python/langgraph/interrupts

**Full sources:**

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

LangChain documentation maintainers. LangGraph Interrupts. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/interrupts

## 37. LangGraph demo: pause, inspect and continue

**Timing:** 67:00–69:30 (2.5 minutes).

Use the remaining fifty-one seconds to connect the inspected state to engineering checks. Play only 3:34–5:13, the 99-second breakpoint-and-improvement segment of LangChain’s official debugging demo. The publisher’s chapter markers identify breakpoints at 3:34, iterative prompt improvement at 4:10, and completing graph execution at 5:00. The excerpt ends before the summary at 5:13. Explain that pausing and inspecting software state helps a developer understand a run. This is a developer breakpoint demonstration, not a utility approval screen. In a grid application, the solver remains responsible for the electrical calculation and the application must check its result before continuing. Play the embedded video on click. Pause to identify the workflow state, returned output and next step. Ask: Does resuming a workflow prove that the power-flow result is valid? Answer: No. The application still needs the correct inputs, convergence and engineering-limit checks before operator review.

**Full sources:**

LangChain. Strategies for debugging agents with LangGraph Studio. LangChain / YouTube. 26 March 2025.
Full source: https://www.youtube.com/watch?v=5vEC0Y4sV8g

## 38. Saved state must identify the study and its evidence

**Timing:** 69:30–71:30 (2 minutes).

The published figure shows generic LangGraph software state. For a spoken grid-study example, imagine an application-specific expected-case set that includes outage_34 while the returned evidence lacks that case. Those case fields are tutorial requirements, not a built-in LangGraph power-system schema. Default update behavior does not guarantee that all branch results survive a merge. Define and test the reducer, or an external evidence store, to preserve case IDs and detect duplicates or missing outputs. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. The extra grid identifiers are tutorial requirements; they are not fields proven by this generic illustration. Source figure locator: Get state history. Original source URL: https://docs.langchain.com/oss/python/langgraph/checkpointers

**Takeaway:** Saved state identifies the evidence. The application still has to check it.

**Full sources:**

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

LangChain documentation maintainers. LangGraph Persistence. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/persistence

LangChain documentation maintainers. Checkpointers. Docs by LangChain, Python LangGraph documentation. Undated live documentation; accessed October 18, 2026.
Full source: https://docs.langchain.com/oss/python/langgraph/checkpointers

## 39. A checkpoint lets a workflow pause and resume

**Timing:** 71:30–73:30 (2 minutes).

An interrupt can pause for outside review and later resume in the same thread. Current LangGraph documentation says the interrupted node restarts from its beginning. Actions before the interrupt can therefore happen again. Use stable step IDs or other idempotency controls, which prevent repeated execution from applying the same change twice. This example grants no permission to command live grid equipment. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. Saved software state does not prove that an external grid snapshot remains current. Source figure locator: Opening checkpoint illustration. Original source URL: https://docs.langchain.com/oss/python/langgraph/checkpointers

**Full sources:**

LangChain documentation maintainers. LangGraph Persistence. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/persistence

LangChain documentation maintainers. LangGraph Interrupts. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/interrupts

LangChain documentation maintainers. Checkpointers. Docs by LangChain, Python LangGraph documentation. Undated live documentation; accessed October 18, 2026.
Full source: https://docs.langchain.com/oss/python/langgraph/checkpointers

## 40. Parallel outage studies must account for every case

**Timing:** 73:30–75:30 (2 minutes).

Independent outage studies should use the same frozen starting case. Collect results by outage ID, compare the returned IDs with the requested set, and preserve failed or missing studies as unresolved. The original parallel-workflow figure illustrates coordination; it does not establish complete electrical coverage.

**Full sources:**

Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

## 41. PowerDAG checks the steps needed before a tool runs

**Timing:** 75:30–77:30 (2 minutes).

Use the inspected v4 dated 5 July 2026: Emmanuel O. Badmus and Amritanshu Pandey, PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. Earlier versions have different titles and performance headlines. Its four network models are Rochester, Stowe, Glover and South Hero. The graph identifies required earlier tools and gates calls while the agent continues choosing steps. A tool can run successfully in the wrong study state if earlier work is missing. The gate addresses that workflow problem. Emmanuel O. Badmus, Amritanshu Pandey; PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis; Figure 2, v4 PDF page 3 This is the v4 research architecture. Formal supervision checks encoded prior Write-tool names; it does not establish all freshness, parameter or physical-safety checks. Source locator: Figure 2, v4 PDF page 3. Original URL: https://arxiv.org/pdf/2603.17418v4

**Full sources:**

Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4

Emmanuel O. Badmus and contributors. DistGrid-AgentBench: A Distribution Grid Benchmark for Agentic AI. Author-maintained GitHub repository. Live repository reviewed 17 October 2026.
Full source: https://github.com/emmanuelbadmus/DistGrid-AgentBench

## 42. PowerDAG: solve the grid before checking its voltage

**Timing:** 77:30–79:30 (2 minutes).

Section IV-C uses voltage-violation checks to explain these requirements. Equation 9 checks whether required Write-tool names appear among executed tool names. That alone does not check whether their outputs match the current grid version. The diagram adds current-v43 freshness as a teaching condition. The introduction also explains how missing a network update can leave a solver using the wrong state. Appendix B reports this Stowe execution order: load_load, load_solar, load_distribution_network, create_and_initialize_model, build_constraints, build_objective, solve, update_network_voltages and plot_network_data. This is a reported order, not a claimed minimal set of dependency links. The authors curate the rules. Tools without rules remain executable. Passing the gate does not prove numerical feasibility or safety.

**Full sources:**

Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4

## 43. PowerDAG results: the same queries, four setups

**Timing:** 79:30–81:30 (2 minutes).

The reported Pass@1 scores are ReAct 77.33%, retrieval-only PowerChain-AR 92.67%, JIT supervision only 96.00%, and full PowerDAG 98.00%. Each setup runs 150 queries. Across the full study, six setups and ten model backends produce 9,000 query runs. Full PowerDAG scores 97.33% with Gemini 3.1 Pro and 92.67% with Qwen 3.6-27B. Pass@1 is an automated check against expert workflows. The test queries were kept out of the example set, but they use the same ten task families; this is a within-family test. These scores do not measure outage avoidance or the reliability of live commands. The comparison tests complete setups as built. It does not isolate the effect of one graph edge.

**Full sources:**

Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4

## 44. PowerDAG: what can others check and reuse?

**Timing:** 81:30–83:30 (2 minutes).

The author README names BESS, basicPV and GFI as the three task groups that can run from the public download. The other seven need private feeder data, geographic data (GIS) and network-tool code. Public workflow records let readers inspect the work, but do not make every experiment reproducible from the public files alone. This is a distribution-study research benchmark using real feeder models. It does not show a named utility running PowerDAG in a control room. Keep the task population and score definition with every reported percentage.

**Full sources:**

Emmanuel O. Badmus and contributors. DistGrid-AgentBench: A Distribution Grid Benchmark for Agentic AI. Author-maintained GitHub repository. Live repository reviewed 17 October 2026.
Full source: https://github.com/emmanuelbadmus/DistGrid-AgentBench

Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4

## 45. Simulation agents find functions, run code and repair errors

**Timing:** 83:30–85:30 (2 minutes).

Jia, Cui and Hug test DALINE and MATPOWER simulation tasks. The paper does not identify LangGraph as its software framework. Its run-and-repair loop is an example of using feedback. The engineering check must compare the actual study and settings with the requested task. A MATLAB run without an error is not enough. Mengshuo Jia, Zeyu Cui, Gabriela Hug; Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework; Figure 5, author-preprint PDF page 7 Published workflow module, not evidence that error-free execution satisfies the requested engineering settings. Source locator: Figure 5, author-preprint PDF page 7. Original URL: https://doi.org/10.1109/TSG.2025.3589114

**Full sources:**

Mengshuo Jia, Zeyu Cui, Gabriela Hug. Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework. IEEE Transactions on Smart Grid, volume 16, issue 6, pages 5556–5572. 2025.
Full source: https://doi.org/10.1109/TSG.2025.3589114
Full paper: https://arxiv.org/pdf/2411.16707v3

## 46. Simulation-agent results: points, not a pass rate

**Timing:** 85:30–87:30 (2 minutes).

Each attempt scores 100 when it meets every requirement without extra settings, 50 when unnecessary settings remain, and 0 when a requirement is missed. The score averages the allowed attempt slots. If attempts are unused, the last score fills those slots. The API setups use gpt-4o-2024-05-13. The built-in ChatGPT-RAG setup runs in a different product. These are comparisons of complete systems, so they do not isolate the effect of one feature. In the related MATPOWER test, the full setup scores 96.85 over 35 tasks with up to five attempts per task.

**Full sources:**

Mengshuo Jia, Zeyu Cui, Gabriela Hug. Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework. IEEE Transactions on Smart Grid, volume 16, issue 6, pages 5556–5572. 2025.
Full source: https://doi.org/10.1109/TSG.2025.3589114
Full paper: https://arxiv.org/pdf/2411.16707v3

## 47. Trying again can repeat the same software error

**Timing:** 87:30–90:00 (2.5 minutes).

The paper asks for a load of 100 MW and 10 Mvar. The Mvar part is reactive load; leaving it out changes the study. A cache stores past results for reuse. Its key tells the software which inputs produced a result. If the key ignores reactive load, a corrected request can still return the old result. Asking the model to try harder will not fix that software error. Test the tool adapter and cache. The key must include every input that can affect the result, including relevant model and topology versions. Source: Anthropic, Building effective agents (December 19, 2024). An LLM evaluator does not prove grid feasibility, permission or fresh input data. Source figure locator: Workflow: Evaluator-optimizer. Original source URL: https://www.anthropic.com/engineering/building-effective-agents

**Takeaway:** Reliable agents also need correct tool adapters, caches and other software.

**Full sources:**

Eve Tsybina, Samim Konjicija, Slaven Peles. Agentic Artificial Intelligence for Power Systems: Strategies to Identify and Close Capability Gaps. arXiv. 30 July 2026; v1.
Full source: https://arxiv.org/abs/2607.28822v1
Full paper: https://arxiv.org/pdf/2607.28822v1

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

## 48. Siemens PSS E: agentic transmission planning

**Timing:** 90:00–94:00 (4 minutes).

Play the full 79-second product video linked from Siemens’ agentic transmission-planning page. This is a supplier overview of Gridscale X PSS E, rather than a complete recorded engineering study. Connect its planning message to three separate jobs: preparing a study, computing the electrical result and interpreting it. The solver remains essential. In our lab we inspect those steps explicitly. A product video alone does not establish field accuracy or deployment at a named utility. After the video, ask which study inputs and numerical checks a planner would need. The overview does not show a complete tool-call trace. Question: Which part must still be checked by a power engineer? Answer: The study inputs, the solver’s convergence and limits, and whether the result supports the proposed decision.

**Full sources:**

Siemens. Gridscale X PSS E: agentic transmission planning — product video. Undated video; accessed 26 October 2026.
Full source: https://video.sw.siemens.com/embed/682ca322-5d0b-47a0-8d18-77bf9d0fb016
Publication: https://www.siemens.com/en-gb/products/pss-software/gridscale-x-pss-e/agentic-transmission-planning/

## 49. GridMind 2025 connects typed agents to solvers

**Timing:** 94:00–96:00 (2 minutes).

The 2025 paper tests 14-, 30-, 118- and 300-bus systems. Figure 3 compares ACOPF success and run time on case 118. The timing distributions use five repeats; do not invent a larger denominator for the success claim. PydanticAI supports structured, typed inputs and outputs. This system is different from the 2026 GridMind weather workflow, which uses LangGraph. Keep the year and paper title clear. Hongwei Jin, Kibaek Kim, Jonghwan Kwon; GridMind: LLMs-Powered Agents for Power System Analysis and Operations; Figure 2, PDF page 2 This is the2025 PydanticAI/pandapower study, not the separate2026 LangGraph weather-risk system. Source locator: Figure 2, PDF page 2. Original URL: https://arxiv.org/abs/2509.02494v1

**Takeaway:** A correct result for one task does not validate every related task.

**Full sources:**

Hongwei Jin, Kibaek Kim, Jonghwan Kwon. GridMind: LLMs-Powered Agents for Power System Analysis and Operations. arXiv; published as SC Workshops 2025, DOI 10.1145/3731599.3767409. 2025-09-02 (arXiv v1); SC Workshops 2025.
Full source: https://arxiv.org/abs/2509.02494v1
Full paper: https://arxiv.org/pdf/2509.02494v1

## 50. GridMind: reported answers need independent checks

**Timing:** 96:00–98:00 (2 minutes).

These are the paper's tool results and interpretations, not a new experiment. The differences may reflect which cases were studied, how they were listed or how results were read. The table does not establish which answer covers every required outage. Ask for the same case definitions and an independent reference study. Do not assume the majority is right or calculate a failure probability from six different model setups. Hongwei Jin, Kibaek Kim, Jonghwan Kwon; GridMind: LLMs-Powered Agents for Power System Analysis and Operations; Figure 8, PDF page 10, baseline and coverage portion of agent response This is an example response, not independent ground truth or the Table1 comparison. Its own output reports a power-balance issue; an answer still needs engineering review. Source locator: Figure 8, PDF page 10, baseline and coverage portion of agent response. Original URL: https://arxiv.org/abs/2509.02494v1

**Full sources:**

Hongwei Jin, Kibaek Kim, Jonghwan Kwon. GridMind: LLMs-Powered Agents for Power System Analysis and Operations. arXiv; published as SC Workshops 2025, DOI 10.1145/3731599.3767409. 2025-09-02 (arXiv v1); SC Workshops 2025.
Full source: https://arxiv.org/abs/2509.02494v1
Full paper: https://arxiv.org/pdf/2509.02494v1

## 51. GridMind 2026 reuses results when their inputs still match

**Timing:** 98:00–100:30 (2.5 minutes).

AERIS supplies weather data. LUMINA or pandapower runs the base OPF. A LUMINA surrogate screens cases, and EPFast uses a reduced-order DC model for cascade simulation. A surrogate is a faster approximation of a more detailed calculation. Which stages need to rerun depends on the actual inputs each stage uses. Here, the contingency stage reads outage schedules directly, so an ACOPF change alone does not require every later-looking stage to rerun. The fingerprints are content hashes of declared inputs. They can show that those inputs match; they do not prove correctness or detect changes that were never recorded.

**Takeaway:** Reuse a result only when the inputs it depends on still match.

**Full sources:**

D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

Argonne GridAI project team. GridAI — AI Foundation Models & Agents for the Power Grid. Live project page reviewed 17 October 2026.
Full source: https://argonne-gridfm.github.io/

## 52. GridMind: which changes need a new run?

**Timing:** 100:30–102:30 (2 minutes).

The five stages are line-wind, outages, ACOPF, contingency and cascade. These dependencies belong to this implementation. Its contingency stage reads outage schedules directly, rather than taking ACOPF output. Returning to exactly the same inputs can allow reuse of an earlier result. Every input that affects a result must be included in its identity; otherwise, the cache may return an out-of-date result.

**Full sources:**

D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

## 53. GridMind results: fewer stages and less time are different

**Timing:** 102:30–105:00 (2.5 minutes).

The 60% reduction is in stage runs, not time. The measured time reduction is about 52.7%, because stages take different amounts of time. The gain comes from the workflow and reuse of saved results; it is not just a faster language model. This is one seven-query session, with no interval for variation across repeated sessions. The study uses surrogate and reduced-order simulations. Their results still need engineering validation before utility use.

**Full sources:**

D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

## 54. Exercise 2: check whether saved weather-risk results still apply

**Timing:** 105:00–111:00 (6 minutes).

Show only the question during the activity. Use the following worked-answer slide for the debrief. Allow 2 minutes to think alone, 2 to compare in groups, 2 for discussion and 2 for the debrief. If only k changes, rerun cascade and retain the other results that still apply. If forecast initialization shifts, rerun all five stages in the cited workflow. If a required stage fails, return an incomplete or unresolved result. Include the case and stage IDs, input versions, tool error and conclusions that remain missing. Do not issue an all-clear report. F0 and v43 are teaching labels. Another implementation may have different dependencies.

**Full sources:**

D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

LangChain documentation maintainers. LangGraph Persistence. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/persistence

## 55. Exercise 2 answer: rerun what changed

**Timing:** 111:00–113:00 (2 minutes).

Reveal after group discussion. Only k changing leaves the four other stage inputs unchanged in the cited trace. Shifting forecast initialization affects all five stages. A failed required simulation cannot support an all-clear report. Preserve the input versions, failed stage, tool error and any conclusions that remain unsupported.

**Full sources:**

D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

LangChain documentation maintainers. LangGraph Persistence. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/persistence

## 56. PowerAgentBench-Dyn allows only specific model changes

**Timing:** 113:00–115:30 (2.5 minutes).

Authors from Harvard SEAS, Politecnico di Milano and UBITECH make the permitted changes explicit and testable. A gain is a controller setting that affects its response. This task diagnoses and repairs a simulation model; it does not authorize a utility controller change. The starting model fails all eight tests. Allowing four gains to change does not mean every other engineering property has been validated. The author repository provides a test harness, but it needs licensed PSS/E and external DMView software. Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie; PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies; Figure 1, PDF page 2 Benchmark architecture, not the full PowerAgent roadmap or an operating utility deployment. Source locator: Figure 1, PDF page 2. Original URL: https://arxiv.org/abs/2606.20401v1

**Takeaway:** The agent must pass the tests and stay within the allowed changes.

**Full sources:**

Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1

PowerAgent Community. Power-Agent/PowerAgentBench. Live author repository reviewed 17 October 2026.
Full source: https://github.com/Power-Agent/PowerAgentBench

## 57. PowerAgentBench-Dyn results: passed sessions and updates

**Timing:** 115:30–118:00 (2.5 minutes).

The three models are Opus 4.8, Sonnet 4.6 and Haiku 4.5. The reported sessions all use one modified WECC solar-PV model. There is no matched human or fixed-search baseline, so the results do not establish a comparative speedup. Show the counts to make the sample size and failures visible. The number of model updates is a different measure from total operator time. A 10/10 row still has the small-sample limits explained later.

**Full sources:**

Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1

## 58. PowerAgentBench-Dyn also checks grid response to faults

**Timing:** 118:00–120:30 (2.5 minutes).

This dynamic-security task is different from the model-quality task. It uses Opus 4.7, not Opus 4.8. Tables III–VI report Opus 4.7 at 9/10, Sonnet 4.6 at 9/10, Haiku 4.5 at 7/10, Gemini 3.1 Pro at 10/10, GPT-5.5 at 10/10 and Qwen 2.5-Coder-7B at 0/10. A pass requires the whole workflow: execute the study, match the offline reference for critical cases, correctly flag L02–25 at 160 ms as unstable, and assess only the allowed synchronous-condenser mitigation options (section IV-C / Table IV). These counts measure more than fault selection. A run may fail during tool execution before it reaches an engineering finding. Do not combine counts from different tasks or call them field reliability.

**Takeaway:** Different tasks in one benchmark can fail in different ways.

**Full sources:**

Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1

## 59. VeraGrid-Agent uses solver results to answer a question

**Timing:** 120:30–122:30 (2 minutes).

The test uses one balanced, radial 8-bus feeder, 33 question templates and 150 questions: 50 at each of three difficulty levels. Reference answers come from the same solver and circuit. The repository provides a test harness and saved reports. Its current interfaces do not prove which SDK the original paper used. AC OPF is AC optimal power flow, a constrained numerical study. Reading its output to answer a question is different from learning a general policy for feeder control. Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi; VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge; Figure 2, PDF page 2 A research question-answering workflow on one feeder. It is not a general feeder-control policy. Source locator: Figure 2, PDF page 2. Original URL: https://arxiv.org/pdf/2607.25155v1

**Full sources:**

Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi. VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge. arXiv preprint. 2026-07-28 (v1).
Full source: https://arxiv.org/pdf/2607.25155v1

Shivanshu Tripathi / VeraGrid-Agent authors. Shivanshu-11/veragrid-llm-benchmark. Author GitHub repository. Reviewed 2026-10-17.
Full source: https://github.com/Shivanshu-11/veragrid-llm-benchmark

## 60. VeraGrid-Agent results: the same models with and without tools

**Timing:** 122:30–124:30 (2 minutes).

The no-tool setup receives feeder and distributed-energy-resource information. The agent adds solver runs, reading tools and repeated feedback. This compares complete systems, not equal amounts of computation. The paper gives correct-answer counts out of 150, but no estimate of variation across repeated runs. Running the solver and interpreting its results are separate steps that can fail. The paper records some remaining agent errors.

**Full sources:**

Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi. VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge. arXiv preprint. 2026-07-28 (v1).
Full source: https://arxiv.org/pdf/2607.25155v1

## 61. AgentiGrid: what does one reported run mean?

**Timing:** 124:30–126:30 (2 minutes).

The three applications are dispatch exploration, outage screening and studies with uncertain inputs. A run with no fatal JSON errors has not necessarily completed its task correctly. Check whether the agent stayed within the allowed changes, studied every required case and described solver evidence correctly. This paper studies one prototype on a modeled grid. It is not a live-utility reliability study. Samim Konjicija, Slaven Peles; Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning; Figure 1, PDF page 2 Prototype architecture for modeled studies. Twelve reported searches are different backend/application settings, not twelve repeats of one task. Source locator: Figure 1, PDF page 2. Original URL: https://arxiv.org/abs/2609.04544v1

**Takeaway:** Explain what one run represents before reporting a success rate.

**Full sources:**

Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1

## 62. A lower cost can come from solving the wrong task

**Timing:** 126:30–128:30 (2 minutes).

Use the paper's unspecified objective units; do not invent dollars per hour. The reported objective falls by about 36.9%, but the agent changes a type of decision outside the task. Unit commitment determines which units are on; dispatch sets their output. Other model setups keep to dispatch-only changes and report no improvement from the given base. A valid comparison checks what was changed, not just whether the objective fell.

**Takeaway:** Judge the objective value together with the allowed decisions.

**Full sources:**

Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1

## 63. Successful tool calls can still miss a critical outage

**Timing:** 128:30–131:00 (2.5 minutes).

All four searches identify the highest-cost outage, 187–189. Three identify infeasible outage 29–30, and none identifies infeasible outage 15–16. Infeasible means the specified study has no solution that meets its constraints. These results show gaps in case coverage. They do not give a stable failure probability for a model. Do not add binomial confidence intervals to these four different setups.

**Full sources:**

Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1

## 64. Show both trial counts and uncertainty

**Timing:** 131:00–133:30 (2.5 minutes).

Six shown cells are 10/10 and two are 5/10. In the tested code version, higher-complexity tasks and larger grids have no reported numerical result cells. The authors discuss later fixes without giving a complete new set of counts. Missing results must not be plotted as zeroes. These are synthetic grids, not utility operating systems. Wilson intervals describe sampling uncertainty under independent pass/fail trials at fixed settings. That assumption is not established by the paper. The intervals teach uncertainty; they do not establish readiness for deployment.

**Full sources:**

Eve Tsybina, Samim Konjicija, Slaven Peles. Agentic Artificial Intelligence for Power Systems: Strategies to Identify and Close Capability Gaps. arXiv. 30 July 2026; v1.
Full source: https://arxiv.org/abs/2607.28822v1
Full paper: https://arxiv.org/pdf/2607.28822v1

National Institute of Standards and Technology, SEMATECH. 7.2.4.1. Confidence intervals. NIST/SEMATECH e-Handbook of Statistical Methods. Undated live handbook section; reviewed 17 October 2026.
Full source: https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm

## 65. PowerBench finds answers across linked records

**Timing:** 133:30–135:30 (2 minutes).

An answer can have the correct format but refer to the wrong asset or time period. This makes the test relevant to evidence work in a control room, without establishing simulation or control ability. The three task groups contain 60, 90 and 150 questions. The paper reports generated data for 761 devices and 24,939 documents. At review, the linked repository showed only README and LICENSE files. We did not verify a runnable public release. Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng; PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems; Figure 1, PDF page 4 Synthetic benchmark data, not utility operational records, simulation results or a live grid database. Source locator: Figure 1, PDF page 4. Original URL: https://arxiv.org/abs/2609.34492v1

**Takeaway:** Finding a useful record is one step. The complete answer still needs checking.

**Full sources:**

Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).
Full source: https://arxiv.org/abs/2609.34492v1
Full paper: https://arxiv.org/pdf/2609.34492v1

## 66. PowerBench results: complete answers and partial credit

**Timing:** 135:30–137:30 (2 minutes).

GPT-5.6-Sol is the leading row in this 2026 paper version. Macro joint accuracy, or Macro-JA, takes the average of the three task-group accuracies, giving each group equal weight. It is not the number of correct answers divided by 300. Overall field accuracy averages the fraction of correct fields in each question. Bootstrap intervals are made by resampling the data. Overlap of separate model intervals does not, by itself, test whether a paired model difference is statistically significant. These synthetic evidence questions do not test physical-grid safety.

**Full sources:**

Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).
Full source: https://arxiv.org/abs/2609.34492v1
Full paper: https://arxiv.org/pdf/2609.34492v1

## 67. A strong average can hide a weak task group

**Timing:** 137:30–139:30 (2 minutes).

The task groups contain 60, 90 and 150 questions. Equal weighting gives the smallest group as much influence as the largest. This is an intentional metric choice, not a calculation error. It answers a different question from counting all correct questions together. In a utility pilot, show results for each important task so weak performance cannot disappear inside the average. Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng; PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems; Figure 2, PDF page 6 Illustrates three task families; the metric gives them equal weight even though their sizes are60,90 and150 questions. Source locator: Figure 2, PDF page 6. Original URL: https://arxiv.org/abs/2609.34492v1

**Takeaway:** Choose the averaging rule carefully and show the tasks that matter to the operator.

**Full sources:**

Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).
Full source: https://arxiv.org/abs/2609.34492v1
Full paper: https://arxiv.org/pdf/2609.34492v1

## 68. What do ten successful trials tell us?

**Timing:** 139:30–141:30 (2 minutes).

An interval shows uncertainty under a statistical model. With repeated use on comparable samples, the Wilson method aims for 95% coverage of the fixed success probability. It does not assign a 95% probability to the fixed parameter lying in this one observed interval. These calculations use small hypothetical or reported counts and a binomial model for independent pass/fail trials. Different tasks, settings and linked errors add uncertainty beyond that model. Keep these two-sided Wilson intervals separate from the later exact one-sided bound on failures.

**Takeaway:** Report the trial count, tested tasks and interval method with a percentage.

**Full sources:**

National Institute of Standards and Technology, SEMATECH. 7.2.4.1. Confidence intervals. NIST/SEMATECH e-Handbook of Statistical Methods. Undated live handbook section; reviewed 17 October 2026.
Full source: https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm

## 69. More required steps can lower overall reliability

**Timing:** 141:30–143:30 (2 minutes).

The curves show why strong results for individual steps can still leave a lower chance of completing the whole task. Retrying may reuse the same wrong context, cache or tool adapter, so it may not be a fresh independent chance. The exact chain rule multiplies conditional probabilities. The plotted q^L assumes the same success probability for every step and independence between steps. It motivates whole-task measurement and code-enforced checks. It does not predict the performance of a real utility agent.

## 70. The answer changes when we change what we count

**Timing:** 143:30–146:00 (2.5 minutes).

Feasible means a case meets the stated constraints. Of 80 feasible cases, 70 are accepted and 10 rejected. Of 20 infeasible cases, two are wrongly accepted and 18 rejected. Among accepted cases, 70/72, or 97.2%, are feasible. Yet the false-approval rate among infeasible cases is 2/20, or 10%. Overall, 88/100 classifications are correct. Choose the error that matters before choosing a headline metric. Rejecting more cases may reduce false approvals but also make the assistant less useful. Measure both effects.

## 71. Zero test failures do not prove perfect performance

**Timing:** 146:00–148:30 (2.5 minutes).

Explain the calculation in words. If each trial has failure probability p, the chance of zero failures in n independent trials is (1-p)^n. Set that chance to 0.05 and solve for p. This gives the stated one-sided 95% upper confidence bound under the test assumptions. It is not certification. It does not establish performance after a topology, model or task change. The approximation 3/n gives a useful quick estimate.

**Full sources:**

National Institute of Standards and Technology. EXACT BINOMIAL. NIST Dataplot Reference Manual. Last updated 16 November 2015; reviewed 17 October 2026.
Full source: https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbino.htm

## 72. Choose tests that can reveal failures

**Timing:** 148:30–150:30 (2 minutes).

Repeating one prompt is not a broad test of different tasks. Report shared networks, scenarios and other links between trials. An independent check should do more than ask the same model whether it is right. Do not use the final test cases to tune prompts or tool adapters. This is a proposed testing method, not a certification process.

**Takeaway:** Show failures by stage and case type, along with the number tested.

**Full sources:**

Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1

Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).
Full source: https://arxiv.org/abs/2609.34492v1
Full paper: https://arxiv.org/pdf/2609.34492v1

Eve Tsybina, Samim Konjicija, Slaven Peles. Agentic Artificial Intelligence for Power Systems: Strategies to Identify and Close Capability Gaps. arXiv. 30 July 2026; v1.
Full source: https://arxiv.org/abs/2607.28822v1
Full paper: https://arxiv.org/pdf/2607.28822v1

Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi. VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge. arXiv preprint. 2026-07-28 (v1).
Full source: https://arxiv.org/pdf/2607.25155v1

## 73. MCP connects a workflow to its tools

**Timing:** 150:30–152:30 (2 minutes).

MCP standardizes messages between an application and its tool servers. It does not select the correct study, validate a solver result or authorize an operating action. Those checks belong to the application and operator.

**Full sources:**

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

Model Context Protocol. MCP Architecture overview. 2026-07-28 documentation revision.
Full source: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture

Model Context Protocol. MCP Security Best Practices. 2026-07-28 documentation revision.
Full source: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices

## 74. A retrieved document cannot give itself permission

**Timing:** 152:30–154:30 (2 minutes).

The hostile instruction is invented for teaching. A retrieved document is evidence, not an instruction source with authority over the task. A separate service check must enforce allowed actions, regardless of what a document says. Test whether hostile text changes the case scope, triggers a forbidden call or puts false instructions into a report. Save the rejected action and the reason it was rejected.

**Full sources:**

Model Context Protocol. MCP Security Best Practices. 2026-07-28 documentation revision.
Full source: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices

## 75. Measure the whole job, including human review

**Timing:** 154:30–156:30 (2 minutes).

The equation is a proposed way to split time for a task whose stages run in sequence. If stages run in parallel, measure the path that determines completion time instead of adding every stage. Include operator attention and time spent recovering from errors. Audit turnaround, batch throughput and time saved in review are different measures. Choose useful timing percentiles and workload measures for the actual job. This original conventional monitoring screenshot illustrates the human interpretation stage. It is not evidence that an agent was used or that the tutorial’s time metric was measured at CAISO. Teaching timing identity: total task time = data preparation + agent execution + human review + rework.

**Takeaway:** Measure the operator's completed job, including the work needed to check and correct it.

**Full sources:**

Corey Fallon, Brett Jefferson, Tyler Ryan. An Analysis of Grid Operators. Pacific Northwest National Laboratory. 2023-04-19.
Full source: https://www.pnnl.gov/sites/default/files/media/file/PNNL_workshop_Presentation_Human_Factors_Virtual_Workshop_March_2023.pdf

Google Cloud. AES: Scaling energy safety audits with Claude on Google Cloud. Undated; reviewed 17 October 2026.
Full source: https://cloud.google.com/customers/aes

Amazon Web Services. TC Energy increases office productivity with automation on Amazon Bedrock. Undated; reviewed 17 October 2026.
Full source: https://aws.amazon.com/solutions/case-studies/tcenergy-bedrock/

John Phipps. Control center modernization is enhancing reliability. California ISO. 2025-09-10.
Full source: https://www.caiso.com/about/news/energy-matters-blog/control-center-modernization-is-enhancing-reliability

## 76. Test whether the assistant helps on comparable tasks

**Timing:** 156:30–158:30 (2 minutes).

This is a proposed pilot design, not a standard approval process. When practical, randomize task order or balance which condition is tried first to reduce order effects. After tuning, keep a fixed final test set. Record disagreements with independent checks. A pilot only supports conclusions about the tasks, tools, settings and users that it actually tested. The real training-facility photograph provides context for the proposed evaluation. The slide’s matched-task comparison is a tutorial recommendation, not a reported CAISO agent trial.

**Takeaway:** Build the assistant, then separately test the claim that it helps.

**Full sources:**

Tricia Johnstone, Director, Operational Readiness. ISO now has expanded training and emergency operations facilities. California ISO. 2025-02-20.
Full source: https://www.caiso.com/about/news/energy-matters-blog/iso-now-has-expanded-training-and-emergency-operations-facilities

## 77. Power-sector testbeds provide places to evaluate agents

**Timing:** 158:30–160:00 (1.5 minutes).

A testbed is a controlled environment for testing a system. It can make tool failures, state changes and engineering effects easier to observe. It still needs to represent the task being tested. Keep DOE, LLNL, ORNL and EPRI roles clear. The existence of a testbed or guidance program does not prove that a particular agent performs well.

**Full sources:**

U.S. Department of Energy. CESER Releases New Testbed to Advance LLM and Agentic AI Evaluation for Critical Infrastructure. 2026-07-16.
Full source: https://www.energy.gov/ceser/articles/ceser-releases-new-testbed-advance-llm-and-agentic-ai-evaluation-critical

EPRI via GlobeNewswire. EPRI Launches Effort to Reduce Risk in AI Power Sector Deployment. 2026-08-06.
Full source: https://www.globenewswire.com/news-release/2026/08/06/3340219/0/en/epri-launches-effort-to-reduce-risk-in-ai-power-sector-deployment.html

EPRI. SAFERai.power. Undated; reviewed 17 October 2026.
Full source: https://msites.epri.com/saferai

Oak Ridge National Laboratory, U.S. Department of Energy. Oak Ridge National Laboratory, U.S. Department of Energy: Researchers at ORNL GOAL facing a large display of U.S. grid and geographic data. Image accessed 17 October 2026.
Full source: https://www.ornl.gov/grid-operations-and-analytics-laboratory-goal/

## 78. GridGuard: what should this prototype prove?

**Timing:** 160:00–162:00 (2 minutes).

The prototype cannot issue live DMS commands. Test measurable outcomes: correct feasible proposals, false approvals, engineering-limit violations, time and reviewer corrections. Keep failed attempts and actions outside the allowed scope in the record. Plausible-sounding actions alone are not evidence of benefit. This prepares the next tutorial, where the three numerical case studies are worked through.

**Takeaway:** Useful proposals have assumptions and evidence that an operator can inspect.

**Full sources:**

GridGuard project / local source snapshot. GridGuard current project: README and graph source snapshot. 2026.
Full source: ../research/GridGuard_source_snapshot.txt

Local workshop source snapshot. Existing three-use-case GridGuard workshop: instructor route and synthetic-feeder context. Snapshot 17 October 2026.
Full source: ../research/Follow_on_workshop_source.txt

## 79. Next tutorial: check the proposed action

**Timing:** 162:00–163:00 (1 minutes).

Take three questions into the detailed workshop: Are the data valid? Is the engineering result valid? Is the decision justified? For each performance claim, ask what was tested, how many cases there were and which case was rejected. The next tutorial contains the exact experiments and results.

**Full sources:**

Local workshop source snapshot. Existing three-use-case GridGuard workshop: instructor route and synthetic-feeder context. Snapshot 17 October 2026.
Full source: ../research/Follow_on_workshop_source.txt

## 80. Discussion and full sources

**Timing:** 163:00–165:00 (2 minutes).

All slides belong to one integrated session. Return to the opening real-world examples and separate evidence that a company uses a system from evidence that it performs an engineering task well. The next tutorial applies these checks to voltage support, restoration and cyber response. Full sources are in the reading guide. Answers to both exercises are in the instructor guide.

**Takeaway:** A credible claim states the task, number tested, assumptions, failures and remaining human work.
