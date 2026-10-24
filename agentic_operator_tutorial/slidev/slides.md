---
theme: default
title: Agentic AI for Utility Operators — Power Systems and Agent Workflows
info: Integrated power-system tutorial with deployment news, LangGraph, DAGs, measured paper results and complete readings
author: Alaa Selim (MIT/Dartmouth) and Mohamed Chehada (UT Austin)
transition: none
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
fonts:
  sans: Arial
  provider: none
mdc: false
drawings:
  persist: false
download: false
---

<div class="lesson teaching rigorous cover-slide cover">

<h1>Agentic AI for<br>Utility Operators</h1>
<p>Real power-sector uses, engineering tools and measured research results</p>
<p>165 minutes / two worked exercises</p>
<div class="presenters"><div><strong>Alaa Selim</strong><span>MIT/Dartmouth</span></div><div><strong>Mohamed Chehada</strong><span>UT Austin</span></div></div>
<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup"><small>Independent educational material · IEEE ComSoc theme adaptation</small>
<div class="sources">Source: <a href="https://www.comsoc.org/about/brand-experience/resources">IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.</a></div>
<span class="pageno">1 / 80</span></div>

<!--
All slides belong to the main presentation. The opening distinguishes systems in use, utility statements and product announcements. Every agent-research paper covers a power-system task. We explain LangGraph and task dependency graphs through fault analysis and weather-risk studies. A separate follow-on workshop covers the detailed GridGuard cases on voltage, restoration and cyber events.
Takeaway: 
Nominal duration: 0.5 minutes.

Full sources:
IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>What is agentic AI?</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_framework_nvidia_interaction_patterns.svg" alt="Original NVIDIA interaction patterns. The same generative model can be part of a chat or an agentic system." style="max-height:360px;height:auto"><figcaption>Original NVIDIA interaction patterns. The same generative model can be part of a chat or an agentic system.</figcaption></figure></div><ul><li>An agentic system uses feedback to choose and adjust actions toward a goal. One agent may be enough.</li></ul></div>
<div class="sources">Source: <a href="https://www.anthropic.com/engineering/building-effective-agents">Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.</a></div>
<span class="pageno">2 / 80</span></div>

<!--
The first sentence is our summary, not a quotation or a standard definition. Anthropic includes both programmed workflows and LLM-directed agents under agentic systems. Wooldridge and Jennings also discuss different definitions of an agent. The later examples focus on engineering systems using large language models, or LLMs. “Agentic” describes how the whole system pursues a task. It is not another software component beside the agent. A system can use just one agent. Source: NVIDIA Technical Blog, Figure 1. The three examples show interaction patterns, not a universal taxonomy or a claim that tool use alone proves autonomy. Source figure locator: Figure 1. Original source URL: https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

Michael Wooldridge, Nicholas R. Jennings. Intelligent agents: theory and practice. The Knowledge Engineering Review, 10(2), pp. 115–152. 1995.
Full source: https://doi.org/10.1017/S0269888900008122
Full paper: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95.pdf

Eduardo Alvarez, Benjamin Klieger, Graham Steele. Building for the Rising Complexity of Agentic Systems with Extreme Co-Design. NVIDIA Technical Blog. May 5, 2026.
Full source: https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Generative AI creates content</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/va_generation_call.svg" alt="Illustrative report-drafting example. Generative models can also be components of agents." style="height:315px;max-height:315px"><figcaption>Illustrative report-drafting example. Generative models can also be components of agents.</figcaption></figure><ul><li>Generative AI makes text, images and other content. Large language models (LLMs) are used for text.</li><li>A single call can create a draft. An agent system can use the same model to choose steps.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.6028/NIST.AI.600-1">National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. NIST AI 600-1. July 2024.</a></div>
<span class="pageno">3 / 80</span></div>

<!--
NIST AI 600-1 describes generative AI in terms of producing synthetic content, including text, images, audio and other media. This diagram shows one generation call: selected records and a request enter a model, which produces a draft. It does not say every generative-AI application is a single call. An LLM-based agent can use a generative model inside a repeated decision process. These categories describe different roles, not three mutually exclusive technologies or stages of a historical evolution. Generated wording is not itself numerical grid evidence; a study report should cite the engineering records used.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. NIST AI 600-1. July 2024.
Full source: https://doi.org/10.6028/NIST.AI.600-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>What is an AI agent?</h1>
<div class="content source-focus"><figure><img src="/images/real_concept_classical_agent.png" alt="Russell and Norvig’s original agent diagram, Figure 2.1. A software agent’s sensors and actuators can be software interfaces." style="max-height:425px;height:auto"><figcaption>Russell and Norvig’s original agent diagram, Figure 2.1. A software agent’s sensors and actuators can be software interfaces.</figcaption></figure><div><ul><li>An agent observes an environment and chooses actions that affect it.</li><li>In a study, an engineering solver calculates grid behavior. The agent reads its results and chooses the next tool call.</li></ul></div></div>
<div class="sources">Source: <a href="https://aima.cs.berkeley.edu/2nd-ed/">Stuart J. Russell, Peter Norvig. Artificial Intelligence: A Modern Approach, Chapter 2: Intelligent Agents. Prentice Hall, second edition, Chapter 2, pp. 32–58. 2003.</a></div>
<span class="pageno">4 / 80</span></div>

<!--
The equation is teaching notation: the policy uses the history of observations to choose the next action. It is not the textbook’s exact notation. The agent function is this abstract mapping, and a program implements it. A grid-study agent may observe case files and solver logs, then call a tool, ask for information or return a report. This classical definition predates LLMs. It also includes many older forms of automation. The linked sample chapter is from the second edition, even though its URL says fourth edition. The reading guide records that difference. Teaching notation: a_t = pi(o_1, ..., o_t), a rule mapping past observations to the next action. The original textbook figure replaces the teaching redraw. The question mark represents the agent’s decision mechanism; observations enter through sensors and actions leave through actuators. This is the author-hosted older chapter draft, cited as second edition.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Stuart J. Russell, Peter Norvig. Artificial Intelligence: A Modern Approach, Chapter 2: Intelligent Agents. Prentice Hall, second edition, Chapter 2, pp. 32–58. 2003.
Full source: https://aima.cs.berkeley.edu/2nd-ed/
Full paper: https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>An agent chooses a step. A tool runs it.</h1>
<div class="content source-focus"><figure><img src="/images/real_framework_nvidia_agent_components.svg" alt="Original NVIDIA agent design: the core connects a request with tools, planning and memory. Other designs can combine these roles." style="max-height:425px;height:auto"><figcaption>Original NVIDIA agent design: the core connects a request with tools, planning and memory. Other designs can combine these roles.</figcaption></figure><div><ul><li>The agent chooses an allowed step. A tool carries out the request.</li><li>An engineering solver calculates grid behavior. The agent uses the returned evidence.</li></ul></div></div>
<div class="sources">Source: <a href="https://developer.nvidia.com/blog/introduction-to-llm-agents/">Tanay Varshney. Introduction to LLM Agents. NVIDIA Technical Blog. November 30, 2023.</a></div>
<span class="pageno">5 / 80</span></div>

<!--
A run_pf request should identify the study case. Its response should include status, numerical results and an evidence ID. The solver computes the electrical result. After an error, an LLM may choose another allowed check or stop and ask for help. The runtime software saves progress and carries out those choices. This example gives no permission to switch live equipment. A service may contain its own agents and still act as a tool for the agent calling it. Source: NVIDIA Technical Blog, Figure 1. This is a published conceptual design; separate memory or planning modules are not required in every AI agent. Source figure locator: Figure 1: General components of an agent. Original source URL: https://developer.nvidia.com/blog/introduction-to-llm-agents/
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
LangChain maintainers. Tools. Docs by LangChain, Python open-source documentation. Accessed 17 October 2026.
Full source: https://docs.langchain.com/oss/python/langchain/tools

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

Stuart J. Russell, Peter Norvig. Artificial Intelligence: A Modern Approach, Chapter 2: Intelligent Agents. Prentice Hall, second edition, Chapter 2, pp. 32–58. 2003.
Full source: https://aima.cs.berkeley.edu/2nd-ed/
Full paper: https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf

Tanay Varshney. Introduction to LLM Agents. NVIDIA Technical Blog. November 30, 2023.
Full source: https://developer.nvidia.com/blog/introduction-to-llm-agents/
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Workflow or agent: who chooses the next step?</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_framework_langgraph_workflow_agent.svg" alt="Original LangGraph documentation figure. The model chooses an action, receives feedback and can choose again." style="max-height:310px;height:auto"><figcaption>Original LangGraph documentation figure. The model chooses an action, receives feedback and can choose again.</figcaption></figure></div><ul><li>In a fixed workflow, code sets the steps and branches.</li><li>In an LLM agent, the model chooses some next steps from the allowed actions, using the results so far.</li></ul></div>
<div class="sources">Source: <a href="https://www.anthropic.com/engineering/building-effective-agents">Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.</a></div>
<span class="pageno">6 / 80</span></div>

<!--
This distinction comes from Anthropic’s practitioner account. It is useful engineering language, not a universal definition. Its workflow patterns include routing, orchestrator-workers and evaluator-optimizer loops. A system can combine fixed requirements with an LLM choosing among allowed next steps. PowerDAG later shows this combination. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. This documentation convention concerns LLM applications, not all classical AI agents. Source figure locator: Opening workflow comparison: selected Agent panel. Original source URL: https://docs.langchain.com/oss/python/langgraph/workflows-agents
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

LangChain maintainers. LangGraph overview. Docs by LangChain, Python open-source documentation. Undated live documentation; accessed 2026-10-17.
Full source: https://docs.langchain.com/oss/python/langgraph/overview

LangChain documentation maintainers. Workflows and agents. Docs by LangChain, Python LangGraph documentation. Undated live documentation; accessed October 18, 2026.
Full source: https://docs.langchain.com/oss/python/langgraph/workflows-agents
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>An agent needs a clear goal and limits</h1>
<div class="content source-focus"><figure><img src="/images/real_framework_langgraph_review_detail.svg" alt="Original LangGraph Studio review-form excerpt. This is a generic demo, not a utility interface." style="max-height:425px;height:auto"><figcaption>Original LangGraph Studio review-form excerpt. This is a generic demo, not a utility interface.</figcaption></figure><div><ul><li>The agent can run agreed studies and prepare a report with evidence.</li><li>The operator reviews the findings and decides whether an operating action is allowed.</li></ul></div></div>
<div class="sources">Source: <a href="https://docs.langchain.com/oss/python/langgraph/interrupts">LangChain documentation maintainers. LangGraph Interrupts. Official LangChain documentation. Accessed 2026-10-17; live documentation.</a></div>
<span class="pageno">7 / 80</span></div>

<!--
This is an illustrative advisory-study policy informed by classical work on agency. Wooldridge and Jennings discuss autonomy, response to change, initiative and interaction; they do not prescribe this grid-operator approval process. The example gives the agent permission to run agreed studies and prepare evidence. The operator can request changes, stop the process or approve a later operating action. This diagram does not give the agent direct control of physical equipment. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. This is a generic software demonstration, not an operator dispatch interface or a utility deployment. Source figure locator: Interrupt response schema / Studio form. Original source URL: https://docs.langchain.com/oss/python/langgraph/interrupts
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Michael Wooldridge, Nicholas R. Jennings. Intelligent agents: theory and practice. The Knowledge Engineering Review, 10(2), pp. 115–152. 1995.
Full source: https://doi.org/10.1017/S0269888900008122
Full paper: https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/ker95.pdf

Stuart J. Russell, Peter Norvig. Artificial Intelligence: A Modern Approach, Chapter 2: Intelligent Agents. Prentice Hall, second edition, Chapter 2, pp. 32–58. 2003.
Full source: https://aima.cs.berkeley.edu/2nd-ed/
Full paper: https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap02.pdf

LangChain documentation maintainers. LangGraph Interrupts. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/interrupts
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>A model can use records, tools and memory</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/source_anthropic_augmented_llm_wide.svg" alt="Original Anthropic building-block figure. It is a general pattern, not a diagram of PowerAgent or PowerDAG." style="max-height:350px;height:auto"><figcaption>Original Anthropic building-block figure. It is a general pattern, not a diagram of PowerAgent or PowerDAG.</figcaption></figure></div><ul><li>Retrieval finds records; tools run tasks; memory keeps useful context.</li><li>LangGraph can manage the steps. PowerAgent supplies power-domain components; PowerDAG is one specific system.</li></ul></div>
<div class="sources">Source: <a href="https://www.anthropic.com/engineering/building-effective-agents">Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.</a></div>
<span class="pageno">8 / 80</span></div>

<!--
These names refer to different roles. LangGraph can run both fixed workflows and processes where a model chooses steps. PowerAgent develops power-system models, tool interfaces and workflows. Later slides show a specific LangGraph example in its PowerWF repository. PowerDAG has its own supervisory design. A platform name alone does not establish numerical accuracy or deployment at a utility. The published figure shows an augmented language model. Retrieval, tools and memory are supporting capabilities; they are not mandatory in every agent. The diagram is reproduced from Anthropic with only empty margins trimmed in the display. The original image bytes are retained.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

LangChain maintainers. LangGraph overview. Docs by LangChain, Python open-source documentation. Undated live documentation; accessed 2026-10-17.
Full source: https://docs.langchain.com/oss/python/langgraph/overview

Power and AI Initiative / PowerAgent community, Harvard SEAS. PowerAgent — Open-Source Agentic AI for Power Grids. Official Harvard project website. Live project page reviewed 17 October 2026.
Full source: https://poweragent.seas.harvard.edu/

Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<div class="eyebrow">United States / Supplier reports deployment / PJM confirms earlier testing</div>
<h1>PJM uses HyperQ to review connection applications</h1>
<div class="content"><div class="with-photo"><div><ul><li>Tapestry’s June 2026 report says HyperQ entered PJM Cycle 1 on 29 April. PJM confirmed testing in March.</li><li>Gemini agents check site-control agreements (rights to use land), property parcels and tariff evidence. Engineers make final decisions.</li><li>This work checks application readiness before the electrical study begins.</li></ul></div><figure><img src="/images/real_news_pjm_hyperq_header.png" alt="Original Tapestry article and published animation still. Supplier report, June 2026." style="max-height:345px;height:auto"><figcaption>Original Tapestry article and published animation still. Supplier report, June 2026.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1">Tapestry. Field Notes  /  HyperQ deployment in PJM’s Cycle 1. 2026-06-11; deployment entry 2026-04-29.</a></div>
<div class="takeaway">A numerical study needs reliable input evidence.</div>
<span class="pageno">9 / 80</span></div>

<!--
Tapestry’s 11 June report covers 811 generation applications. Agents perform limited document and evidence tasks. The report does not establish an agent making a power-flow conclusion or an automatic regulatory decision. The system guides the agents’ work and records evidence citations. The article describes migration to Google ADK as future work, so do not label the deployed system an established ADK implementation. Tapestry, HyperQ Field Notes, June 11, 2026 Supplier report of deployment. PJM separately confirmed earlier testing. The hero is a still captured from the publisher's animation, not an independently verified live PJM application record. Original page: https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1
Takeaway: A numerical study needs reliable input evidence.
Nominal duration: 2 minutes.

Full sources:
Tapestry. Field Notes  /  HyperQ deployment in PJM’s Cycle 1. 2026-06-11; deployment entry 2026-04-29.
Full source: https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1

Tapestry. How agentic AI can help grid operators speed up interconnection. 2025.
Full source: https://www.tapestryenergy.com/en/projects/how-agentic-ai-can-help-grid-operators-speed-up-interconnection

PJM Interconnection. Successful Interconnection Reforms, Other PJM Initiatives Seek To Maximize Electricity Supplies. 2026-03-16.
Full source: https://insidelines.pjm.com/connected/
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>HyperQ: what the reported numbers measure</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/power_news_hyperq_dashboard.png" alt="Original Tapestry performance graphic, June 2026. The timing covers only computer processing." style="max-height:335px;height:auto"><figcaption>Original Tapestry performance graphic, June 2026. The timing covers only computer processing.</figcaption></figure></div><ul><li>The timings cover computer processing for 811 applications. They exclude document-transfer time and human validation.</li></ul></div>
<div class="sources">Source: <a href="https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1">Tapestry. Field Notes  /  HyperQ deployment in PJM’s Cycle 1. 2026-06-11; deployment entry 2026-04-29.</a></div>
<span class="pageno">10 / 80</span></div>

<!--
The supplier reports grouping 4,581 raw site-control documents into 2,328 bundles and checking four criteria. The graphic’s 9,312 macro-assessments are not 9,312 projects. The full interconnection process also includes document transfer and human review. The report gives no confusion matrix or accuracy denominator. We omit its historical 20x headline because it compares manual work with computer processing using different work and timing boundaries.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Tapestry. Field Notes  /  HyperQ deployment in PJM’s Cycle 1. 2026-06-11; deployment entry 2026-04-29.
Full source: https://www.tapestryenergy.com/en/projects/field-notes-hyperq-deployment-in-pjm-s-cycle-1
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>CAISO/OATI: agents help review planned outages</h1>
<div class="content"><div class="with-photo"><div><ul><li>OATI’s AI Genie uses Workflow, Advisor and Recon agents under one coordinator. Operators keep final authority.</li><li>The supplier reports processing 500+ next-day requests nightly in under eight minutes. It gives no per-request time or reviewer-effort result.</li></ul></div><figure><img src="/images/caiso_control_room.jpg" alt="Real California ISO control room. OATI supplies the batch result and later production-use claim." style="max-height:360px;height:auto"><figcaption>Real California ISO control room. OATI supplies the batch result and later production-use claim.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.oati.com/ai-for-energy/">OATI. Generative and Agentic AI in Grid Operations: Field Lessons from OATI, CAISO, PNNL, and EPRI. 2026 (exact publication day not displayed).</a></div>
<div class="takeaway">A processing rate needs a clear work boundary and a measure of the review left for people.</div>
<span class="pageno">11 / 80</span></div>

<!--
California ISO’s July 2025 account described a pilot. OATI’s 2026 field report describes daily production use but gives no exact production start date. The reported inequalities imply more than 62.5 requests per minute for the batch. They do not describe individual request latency. Do not compare eight machine-minutes with a separate analyst-hours figure as though both came from the same trial. The work prepares outage analysis and operating evidence. Reviewers make final decisions.
Takeaway: A processing rate needs a clear work boundary and a measure of the review left for people.
Nominal duration: 2.5 minutes.

Full sources:
California ISO. Exploring AI to support smarter grid management. 2025-07-28.
Full source: https://www.caiso.com/about/news/energy-matters-blog/exploring-ai-to-support-smarter-grid-management

OATI. Generative and Agentic AI in Grid Operations: Field Lessons from OATI, CAISO, PNNL, and EPRI. 2026 (exact publication day not displayed).
Full source: https://www.oati.com/ai-for-energy/

OATI (California ISO control-room photograph). California ISO control room, image published by OATI: California ISO control room with operators seated at curved desks facing a long wall of grid displays. Image accessed 17 October 2026.
Full source: https://www.oati.com/ai-genie/
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>Duke and AWS: agents help prepare planning studies</h1>
<div class="content"><div class="with-photo"><div><ul><li>Duke engineers use AWS-managed agents to prepare study cases and coordinate interconnection studies for new grid connections.</li><li>A September 2026 AWS announcement reports data preparation falling from two weeks of manual work to hours.</li><li>The final number of hours is unspecified. Engineers keep final responsibility for engineering decisions.</li></ul></div><figure><img src="/images/duke_operator.jpg" alt="Duke operator, 2022, shown for context. The reported agents support planning, rather than this pictured operating desk." style="max-height:360px;height:auto"><figcaption>Duke operator, 2022, shown for context. The reported agents support planning, rather than this pictured operating desk.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://press.aboutamazon.com/aws/2026/9/aws-launches-agentic-grid-planning-program-to-accelerate-interconnection-studies">Amazon Web Services. AWS Launches Agentic Grid Planning Program to Accelerate Interconnection Studies. 2026-09-17.</a></div>
<div class="takeaway">Faster preparation alone does not establish a shorter full regulatory process.</div>
<span class="pageno">12 / 80</span></div>

<!--
AWS’s 17 September 2026 announcement names Duke engineers using agents to coordinate studies. The agents prepare inputs and coordinate existing physics software, models and scripts. The report says data preparation fell from two weeks of manual work to hours. It gives neither the final number of hours nor a sample count. It identifies no SDK, model or runtime. Do not infer Strands or AgentCore from the cloud provider. Engineers make final decisions.
Takeaway: Faster preparation alone does not establish a shorter full regulatory process.
Nominal duration: 2.5 minutes.

Full sources:
Amazon Web Services. AWS Launches Agentic Grid Planning Program to Accelerate Interconnection Studies. 2026-09-17.
Full source: https://press.aboutamazon.com/aws/2026/9/aws-launches-agentic-grid-planning-program-to-accelerate-interconnection-studies

Amazon Web Services. Agentic Grid Planning on AWS. Undated; reviewed 17 October 2026.
Full source: https://aws.amazon.com/energy-utilities/agentic-grid-planning/

Duke Energy / illumination. Duke Energy, illumination, August 2, 2022: Duke Energy grid operator Howard Greene seated before many control-room displays. Image accessed 17 October 2026.
Full source: https://illumination.duke-energy.com/articles/meet-the-team-that-monitors-the-grid-and-keeps-the-lights-on
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<div class="eyebrow">Product announcement / 5 May 2026</div>
<h1>Siemens announces agents for PSS E planning studies</h1>
<div class="content"><div class="with-photo"><div><ul><li>Siemens’ Gridscale X announcement describes agents coordinating transmission-planning simulations.</li><li>The targets include connection studies for large loads and data centers, using open software interfaces (APIs).</li><li>The announcement does not name a production user of the new agentic PSS E features.</li></ul></div><figure><img src="/images/real_news_siemens_gridscale_header.png" alt="Original Siemens press-release header, 2026. This is an announced product capability." style="max-height:360px;height:auto"><figcaption>Original Siemens press-release header, 2026. This is an announced product capability.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://press.siemens.com/global/en/pressrelease/siemens-gridscale-x-redefines-system-operations-and-agentic-transmission-planning">Siemens. Siemens’ Gridscale X redefines system operations and agentic transmission planning. 2026-05-05.</a></div>
<div class="takeaway">Check product features and measured utility results separately.</div>
<span class="pageno">13 / 80</span></div>

<!--
The same release describes Alliander’s migration to the platform. That shows platform adoption, not use of the newly announced agentic PSS E features. The claim of up to 50% faster study response has no disclosed benchmark method, so we do not plot it. The announcement shows a possible integration path: agents coordinate an established simulation environment. Siemens AG, press release, May 5, 2026 Product announcement. The separately named Alliander platform migration does not prove production use of the new agentic PSS E capability. Original page: https://press.siemens.com/global/en/pressrelease/siemens-gridscale-x-redefines-system-operations-and-agentic-transmission-planning
Takeaway: Check product features and measured utility results separately.
Nominal duration: 2 minutes.

Full sources:
Siemens. Siemens’ Gridscale X redefines system operations and agentic transmission planning. 2026-05-05.
Full source: https://press.siemens.com/global/en/pressrelease/siemens-gridscale-x-redefines-system-operations-and-agentic-transmission-planning
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Reported current use / UK–US group / Rollout location unspecified</div>
<h1>National Grid reports agents checking project plans</h1>
<div class="content"><ul><li>The results transcript says its “capital control tower” already checks early project options and documents at approval stages.</li><li>Project managers get feedback while they can still change their plans.</li><li>The group reports no agent framework, timing result or accuracy result.</li></ul></div>
<div class="sources">Source: <a href="https://www.nationalgrid.com/document/577036/download">National Grid. National Grid Full Year Results 2025/26: Video Webcast Transcript. 2026-05-14.</a></div>
<span class="pageno">14 / 80</span></div>

<!--
The CEO’s 14 May 2026 results transcript reports agentic project-assurance use. “Capital control tower” names the system supporting project checks. Later comments about optimizing access outages describe future plans. Do not attribute nearby FLISR, outage-minute or gas-crew results to this agent. The source verifies reported use without supporting a numerical performance estimate.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
National Grid. National Grid Full Year Results 2025/26: Video Webcast Transcript. 2026-05-14.
Full source: https://www.nationalgrid.com/document/577036/download
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">NYPA data-quality lead / Webinar, 14 October 2026</div>
<h1>NYPA: better data for agent use</h1>
<div class="content source-focus"><figure><img src="/images/real_news_nypa_webinar_detail.svg" alt="Original Ataccama webinar artwork. The NYPA speaker appears at lower right." style="max-height:400px;height:auto"><figcaption>Original Ataccama webinar artwork. The NYPA speaker appears at lower right.</figcaption></figure><div><ul><li>NYPA describes Databricks and Ataccama checks for meter data before AI uses it.</li><li>A separate demo connects Genie to Ataccama through the Model Context Protocol (MCP). Its product-data example does not establish NYPA grid control.</li></ul></div></div>
<div class="sources">Source: <a href="https://www.ataccama.com/webinar/on-demand-trust-driven-medallion-architecture">Session speakers: Saptaparna Gupta (NYPA), Oleksandra Bovkun (Databricks), Eliza Pochinova (Ataccama). On demand: Trust-driven medallion architecture: How to make your CDEs ready for AI. Ataccama. 2026.</a></div>
<span class="pageno">15 / 80</span></div>

<!--
This supplier-hosted webinar discusses NYPA’s quality checks for frequently arriving meter data. The separate demo uses Genie and an Ataccama MCP service with a product/reorder table. MCP, the Model Context Protocol, is a standard way to connect AI systems to tools and data. Keep the NYPA implementation and the generic agent demo separate. We use October 2026 because the fetched event and on-demand report show adjacent dates. These sources support the discussion of data agents need, without establishing a production grid-command agent at NYPA. We excluded the earlier governance-agenda search result because the full original was unavailable. Ataccama, original webinar report with NYPA Data Quality Lead Saptaparna Gupta, October 14, 2026 NYPA discusses meter-data quality checks. The separate product/reorder demo does not establish a production NYPA grid-control agent. Original page: https://www.ataccama.com/webinar/on-demand-trust-driven-medallion-architecture
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Session speakers: Saptaparna Gupta (NYPA), Oleksandra Bovkun (Databricks), Eliza Pochinova (Ataccama). On demand: Trust-driven medallion architecture: How to make your CDEs ready for AI. Ataccama. 2026.
Full source: https://www.ataccama.com/webinar/on-demand-trust-driven-medallion-architecture

Saptaparna Gupta (NYPA), Oleksandra Bovkun (Databricks), Eliza Pochinova (Ataccama). Trust-driven medallion architecture: how to make your CDEs ready for AI. Ataccama. 2026-10-13, 11:00 AM EDT (date displayed on fetched event page).
Full source: https://www.ataccama.com/events/trust-driven-medallion-architecture
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide has-pair">

<div class="eyebrow">Eversource / Existing simulation tools and a stated engineering direction</div>
<h1>Eversource: adding agentic skills to grid studies</h1>
<div class="content"><div class="source-focus news-detail"><figure><img src="/images/real_news_eversource_job_header.png" alt="Original Eversource vacancy, 5 October 2026." style="max-height:330px;height:auto"><figcaption>Original Eversource vacancy, 5 October 2026.</figcaption></figure><div><ul><li>Eversource uses MATLAB and Synergi Electric for distribution-network studies.</li><li>Its October 2026 engineering vacancy asks for agentic and AI-based workflows in MATLAB. The vacancy shows hiring intent, not deployment.</li></ul></div></div><div class="news-strip"><figure><img src="/images/real_news_eversource_agentic_line.svg" alt="Original requirement excerpt. Hiring and integration intent; deployment is not established." style="max-height:44px;height:auto"><figcaption>Original requirement excerpt. Hiring and integration intent; deployment is not established.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://jobs.eversource.com/job/east-berlin/distribution-system-modeling-and-automation-engineer-hybrid-schedule/7774/101576695504">Eversource Energy (employer). Distribution System Modeling and Automation Engineer (Hybrid Schedule). Eversource Energy. 2026-10-05.</a></div>
<span class="pageno">16 / 80</span></div>

<!--
The April 2025 MathWorks report describes probabilistic distribution studies. These use Monte Carlo sampling and parallel numerical simulations to examine many possible conditions. Its timing improvement belongs to conventional simulation automation, so we do not show it as an agent result. Eversource’s October 2026 posting concerns distribution-system modeling and automation and explicitly mentions agentic MATLAB workflows. It shows the company seeking this capability for an existing simulation environment. Eversource Energy, official engineering vacancy, October 5, 2026 Engineering skill requirement and integration intent. The posting later explicitly mentions agentic MATLAB workflows, but a vacancy does not prove deployment. Original page: https://jobs.eversource.com/job/east-berlin/distribution-system-modeling-and-automation-engineer-hybrid-schedule/7774/101576695504
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Eversource Energy (employer). Distribution System Modeling and Automation Engineer (Hybrid Schedule). Eversource Energy. 2026-10-05.
Full source: https://jobs.eversource.com/job/east-berlin/distribution-system-modeling-and-automation-engineer-hybrid-schedule/7774/101576695504

MathWorks; named Eversource engineer John Kreso quoted. Eversource Energy Collaborates with MathWorks to Incorporate Renewable Energy Sources into System Planning Process Using Probabilistic Load Flow Automation. MathWorks. 2025-04-29.
Full source: https://www.mathworks.com/company/newsroom/eversource-energy-collaborates-with-mathworks-to-incorporate-renewable-energy-sources-into-system-planning-process-using-probabilistic-load-flow-automation.html
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>GE Vernova: a platform that can connect grid tools</h1>
<div class="content"><div class="with-photo"><div><ul><li>Alabama Power’s use of GridOS for Distribution gives a named example of GE Vernova’s grid platform.</li><li>GridOS provides shared software for coordinating grid work. This shows where study tools and operator workflows could connect.</li><li>The public statement does not separate out a reliability improvement caused by agents.</li></ul></div><figure><img src="/images/ge_gridos_control_room.jpg" alt="Official GridOS promotional composite. The platform example does not establish a measured agent-specific result." style="max-height:360px;height:auto"><figcaption>Official GridOS promotional composite. The platform example does not establish a measured agent-specific result.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.gevernova.com/news/press-releases/ge-vernova-launches-gridos-distribution-industrys">GE Vernova. GE Vernova Launches GridOS for Distribution, the Industry&#x27;s First Unified Solution for Grid Orchestration. 2026-02-03.</a></div>
<div class="takeaway">For each case, identify the customer, task, agent’s role and measured result.</div>
<span class="pageno">17 / 80</span></div>

<!--
This GE example concerns GE Vernova’s electric-power business. The February 2026 GridOS announcement names a utility context. It does not establish a specific autonomous LLM controller. Our teaching example explains what an integrated agent would also need: clear tool interfaces, saved state, evidence checks and limits on its authority.
Takeaway: For each case, identify the customer, task, agent’s role and measured result.
Nominal duration: 1.5 minutes.

Full sources:
GE Vernova. GE Vernova Launches GridOS for Distribution, the Industry's First Unified Solution for Grid Orchestration. 2026-02-03.
Full source: https://www.gevernova.com/news/press-releases/ge-vernova-launches-gridos-distribution-industrys

GE Vernova. GE Vernova: GE Vernova GridOS promotional control-room composite with people and grid software displays. Image accessed 17 October 2026.
Full source: https://www.gevernova.com/software/products/gridos
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>Operators often work against a deadline</h1>
<div class="content"><div class="with-photo"><div><ul><li>A PNNL survey of 20 control-room operators reported that, on average, 61% of tasks needed completion in under 30 minutes.</li><li>The survey had 75 questions. It gives no task count or statistical spread behind that average.</li><li>An assistant should reduce the time people spend finding and reviewing evidence within the task’s deadline.</li></ul></div><figure><img src="/images/duke_control_room.jpg" alt="Duke Energy control room, 2022. The PNNL survey is a separate study." style="max-height:360px;height:auto"><figcaption>Duke Energy control room, 2022. The PNNL survey is a separate study.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.pnnl.gov/sites/default/files/media/file/PNNL_workshop_Presentation_Human_Factors_Virtual_Workshop_March_2023.pdf">Corey Fallon, Brett Jefferson, Tyler Ryan. An Analysis of Grid Operators. Pacific Northwest National Laboratory. 2023-04-19.</a></div>
<div class="takeaway">Measure the operator’s total effort and deadline alongside AI response time.</div>
<span class="pageno">18 / 80</span></div>

<!--
The 61% is an average share of tasks performed or supported. It is not the percentage of operators. The source gives neither the task denominator nor variance. Twenty respondents do not support a binomial interval for that 61%. Seventy-five survey items do not imply 1,500 independent timing observations. This small self-report study is not a national estimate. Ask which tasks need quick decisions and which allow more investigation.
Takeaway: Measure the operator’s total effort and deadline alongside AI response time.
Nominal duration: 2 minutes.

Full sources:
Corey Fallon, Brett Jefferson, Tyler Ryan. An Analysis of Grid Operators. Pacific Northwest National Laboratory. 2023-04-19.
Full source: https://www.pnnl.gov/sites/default/files/media/file/PNNL_workshop_Presentation_Human_Factors_Virtual_Workshop_March_2023.pdf

PJM Interconnection. What Happens in the Control Room. 2026-04-16.
Full source: https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/fact-sheets/what-happens-in-the-control-room-fact-sheet.pdf

Duke Energy / illumination. Duke Energy, illumination, August 2, 2022: Duke Energy employees in an Energy Control Center, with one pointing toward a display. Image accessed 17 October 2026.
Full source: https://illumination.duke-energy.com/articles/meet-the-team-that-monitors-the-grid-and-keeps-the-lights-on
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>Three checks for a useful recommendation</h1>
<div class="content"><div class="with-photo"><div><ul><li>Data: do the asset, units, time and grid connections (topology) match the question?</li><li>Engineering: does the solution meet the requested equations and limits?</li><li>Decision: is there enough evidence for the next step the user is allowed to take?</li></ul></div><figure><img src="/images/caiso_watch_duty.png" alt="Real CAISO Watch Duty display. It combines fire and transmission-line information for operator awareness." style="max-height:360px;height:auto"><figcaption>Real CAISO Watch Duty display. It combines fire and transmission-line information for operator awareness.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.caiso.com/about/news/energy-matters-blog/control-center-modernization-is-enhancing-reliability">John Phipps. Control center modernization is enhancing reliability. California ISO. 2025-09-10.</a></div>
<div class="takeaway">Agree on acceptance checks for the whole task.</div>
<span class="pageno">19 / 80</span></div>

<!--
These are separate checks. A correctly formatted call may still use old grid connections. An optimization may converge after changing a variable the user was not allowed to change. A correct result may still leave part of the decision unanswered. These checks form the acceptance contract: the agreed conditions a result must meet. We reuse it in the examples and exercises. This original utility screenshot provides a concrete example of displayed evidence to inspect. It is conventional situational-awareness software, not an agent implementation or a claim that the slide’s three checks were measured by CAISO.
Takeaway: Agree on acceptance checks for the whole task.
Nominal duration: 1.5 minutes.

Full sources:
John Phipps. Control center modernization is enhancing reliability. California ISO. 2025-09-10.
Full source: https://www.caiso.com/about/news/energy-matters-blog/control-center-modernization-is-enhancing-reliability
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>A clear task makes success easier to test</h1>
<div class="content"><div class="with-photo"><div><ul><li>The task is to check whether an earlier study result still applies after a new event.</li><li>Return evidence or ask for missing data. Stop if inputs change, a tool fails, the work budget runs out or permission is missing.</li></ul></div><figure><img src="/images/ge_gridos_visual_intelligence.png" alt="GE Vernova’s published GridOS Visual Intelligence screen. This product image supplies task context, not an agent result." style="max-height:360px;height:auto"><figcaption>GE Vernova’s published GridOS Visual Intelligence screen. This product image supplies task context, not an agent result.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.gevernova.com/software/products/gridos/visual-intelligence">GE Vernova. GridOS Visual Intelligence product screens. Accessed 17 October 2026.</a></div>
<div class="takeaway">A clear task gives us a clear way to check success.</div>
<span class="pageno">20 / 80</span></div>

<!--
All F12 records and policies are invented teaching data, not utility operating rules. A snapshot identifies the data time, grid-connection version and model revision. Start by identifying the user, the result they need and the actions they may take. Success means meeting these agreed requirements. Answer length and the number of tool calls do not establish success. The real product screen illustrates the grid information a bounded task may use. The acceptance contract on this slide remains an original teaching example.
Takeaway: A clear task gives us a clear way to check success.
Nominal duration: 1.5 minutes.

Full sources:
GE Vernova. GridOS Visual Intelligence product screens. Accessed 17 October 2026.
Full source: https://www.gevernova.com/software/products/gridos/visual-intelligence
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>An LLM agent acts, reads the result and decides again</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/source_anthropic_autonomous_agent_wide.svg" alt="Original Anthropic agent-loop figure. In a grid study, feedback can be solver results or a failed check." style="max-height:350px;height:auto"><figcaption>Original Anthropic agent-loop figure. In a grid study, feedback can be solver results or a failed check.</figcaption></figure></div><ul><li>After an action, the agent reads what happened before choosing the next step.</li><li>It can call another allowed tool, ask a person or stop. An error is also useful feedback.</li></ul></div>
<div class="sources">Source: <a href="https://www.anthropic.com/engineering/building-effective-agents">Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.</a></div>
<span class="pageno">21 / 80</span></div>

<!--
The equation describes a software interface. It does not assume we observe the full physical system or that the history has the Markov property, meaning it contains everything needed to predict the next state. The model chooses a request using the goal and previous evidence. The software runs a service against a specific input snapshot. A historian, which stores time-stamped measurements, returns measured data. A simulator returns model results. Selecting either tool does not turn its output into a command to physical equipment. This is the original published conceptual agent pattern, not a measured utility or PowerAgent implementation. The display trims only empty margins. Feedback does not automatically mean model weights are being retrained.
Takeaway: Check the tool requests, their inputs and their results.
Nominal duration: 2 minutes.

Full sources:
Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).
Full source: https://arxiv.org/pdf/2512.20789v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>When data are stale, the next step is to stop</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_framework_anthropic_prompt_chain.svg" alt="Original Anthropic gated workflow. In our study example, a stale input should fail the check and stop the sequence." style="max-height:310px;height:auto"><figcaption>Original Anthropic gated workflow. In our study example, a stale input should fail the check and stop the sequence.</figcaption></figure></div><ul><li>The asset lookup succeeds, but the measurement request marks the data as stale, meaning out of date.</li><li>Ask for current evidence. The original task remains unresolved.</li></ul></div>
<div class="sources">Source: <a href="https://www.anthropic.com/engineering/building-effective-agents">Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.</a></div>
<span class="pageno">22 / 80</span></div>

<!--
A trace records the sequence of tool requests and results. Use the gate in this published figure to discuss an application check. As a spoken example, a study trace should record case IDs, data times and the returned results. When required data are unavailable or out of date, the system should say so. It must not invent a value or silently reuse an older one. Check whether the agent detects the problem and asks for the right update. A trace makes this inspection possible but does not itself prove the work is correct. Source: Anthropic, Building effective agents (December 19, 2024). A generic content-workflow pattern, not a physical-feasibility or utility-safety guarantee. Source figure locator: Workflow: Prompt chaining. Original source URL: https://www.anthropic.com/engineering/building-effective-agents
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Unit checks catch a kV versus p.u. mistake</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/typed_contract.svg" alt="Teaching example with invented values. These values are not recommended operating limits." style="height:330px;max-height:330px"><figcaption>Teaching example with invented values. These values are not recommended operating limits.</figcaption></figure><ul><li>12.47 kV is 1.00 per unit (p.u.) only with a 12.47 kV base. Per unit means value divided by base.</li><li>A tool expecting p.u. must reject a raw kV value or require explicit information for converting it.</li></ul></div>
<span class="pageno">23 / 80</span></div>

<!--
The software interface must enforce units. Prompt wording alone is insufficient. The same number can mean very different physical quantities. Check unit labels, the chosen base and the asset ID in software. A valid type or unit still does not prove that the measurement or model is accurate. The diagram shows both the error and the information needed to fix it.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:

-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A study must match the current grid connections</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/snapshot_consistency.svg" alt="Invented before-and-after network. This illustration does not calculate power flow." style="height:330px;max-height:330px"><figcaption>Invented before-and-after network. This illustration does not calculate power flow.</figcaption></figure><ul><li>The old study used a closed switch and grid version v42. The event opens the switch and creates version v43.</li><li>Update the inputs and repeat the affected calculations. Rewriting the explanation does not update the numerical result.</li></ul></div>
<span class="pageno">24 / 80</span></div>

<!--
Point to the switch that changed. The old result represents different grid connections, rather than simply an older timestamp. Version matching is a necessary consistency check. It still leaves two questions: does the model represent the real grid accurately, and do the refreshed measurements represent the event?
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:

-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>A solver result depends on the problem it solves</h1>
<div class="content source-focus"><figure><img src="/images/real_framework_anthropic_routing.svg" alt="Original Anthropic routing pattern. Choosing an engineering study also requires selecting the right problem and tool." style="max-height:425px;height:auto"><figcaption>Original Anthropic routing pattern. Choosing an engineering study also requires selecting the right problem and tool.</figcaption></figure><div><ul><li>Choose the study first: power flow, optimal dispatch and dynamic simulation answer different questions.</li><li>A solver’s success flag covers that problem. Also check the requested cases, grid limits and permission to act.</li></ul></div></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2609.04544v1">Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.</a></div>
<span class="pageno">25 / 80</span></div>

<!--
Keep solver status, equation errors (residuals) and modeled limit checks separate from whether the analysis covers the full request. A solver can converge on the wrong problem. The study requirements must state constraints and tolerances, meaning the allowed numerical error. This slide sets no universal voltage or loading limit. Permission to act remains a separate software and organizational decision. Source: Anthropic, Building effective agents (December 19, 2024). The picture illustrates routing; it does not establish an implemented power-system workflow. Source figure locator: Workflow: Routing. Original source URL: https://www.anthropic.com/engineering/building-effective-agents
Takeaway: Report the problem and assumptions together with the solver result.
Nominal duration: 2 minutes.

Full sources:
Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1

GridGuard project / local source snapshot. GridGuard current project: README and graph source snapshot. 2026.
Full source: ../research/GridGuard_source_snapshot.txt

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Work in pairs / 6 minutes</div>
<h1>Exercise 1: check three returned data packets</h1>
<div class="content"><pre class="source-excerpt">A = {age_s:20, topology:v42, unit:pu}
B = {age_s:15, topology:v43, unit:kV}
C = {age_s:45, topology:v43, unit:pu}</pre><ul><li>For this exercise, data must be at most 60 s old, use topology v43 and use p.u. The user can recommend actions only.</li><li>Which packet passes? Explain why each other packet fails.</li><li>Does passing these checks establish complete engineering validity or permission to execute an action?</li></ul></div>
<span class="pageno">26 / 80</span></div>

<!--
Allow 1 minute to inspect, 2 minutes in pairs, 2 minutes to share and 1 minute to debrief. age_s means age in seconds. Only C passes the stated initial checks. A has the wrong grid version. B has the wrong unit. C still needs the right asset mapping, a valid model, the required engineering checks, enough scenario coverage and an explanation people can review. The user may advise but cannot execute actions. The 60-second rule is made up for this exercise. It is not a general operating standard.
Takeaway: 
Nominal duration: 6 minutes.

Full sources:

-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>Power-system papers test different tasks</h1>
<div class="content"><div class="with-photo"><div><ul><li>Fault-analysis tools find events in recorded waveforms. Simulation assistants set up and run studies.</li><li>Control prototypes suggest actions in model grids. Benchmarks test how well systems find evidence or answer numerical questions.</li><li>Each result applies to the tested task, tools, allowed actions and test cases.</li></ul></div><figure><img src="/images/epri_open_power_ai_grid.png" alt="Image accompanying the EPRI Open Power AI Consortium announcement, published by NVIDIA, 20 March 2025." style="max-height:360px;height:auto"><figcaption>Image accompanying the EPRI Open Power AI Consortium announcement, published by NVIDIA, 20 March 2025.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf">Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.</a></div>
<span class="pageno">27 / 80</span></div>

<!--
Every paper that follows concerns power systems. They measure different outcomes, so their percentages cannot form a ranking across papers. The numerical solver computes the engineering result. The language model selects tools and helps interpret the returned evidence. This source photograph introduces the power-sector research context. It does not picture the paper experiments.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
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
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Harvard PowerAgent: models, tools and study workflows</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_poweragent_three_layers.png" alt="Original Harvard author roadmap: workflows, tool connections and foundation models. Three-layer excerpt." style="max-height:420px;height:auto"><figcaption>Original Harvard author roadmap: workflows, tool connections and foundation models. Three-layer excerpt.</figcaption></figure><div><ul><li>PowerAgent’s 2025 IEEE roadmap links AI models, power tools and study workflows.</li><li>PowerFM supports modeling. PowerMCP connects tools. PowerWF manages workflows. PowerAgentBench-Dyn is a later benchmark, not the whole initiative.</li></ul></div></div>
<div class="sources">Source: <a href="https://doi.org/10.1109/MPE.2025.3579718">Qian Zhang, Le Xie. PowerAgent: A Road Map Toward Agentic Intelligence in Power Systems: Foundation Model, Model Context Protocol, and Workflow. IEEE Power and Energy Magazine, volume 23, issue 5, pages 93–101. 2025.</a></div>
<span class="pageno">28 / 80</span></div>

<!--
Full citation: Qian Zhang and Le Xie, PowerAgent: A Road Map Toward Agentic Intelligence in Power Systems: Foundation Model, Model Context Protocol, and Workflow, IEEE Power and Energy Magazine 23(5), 93–101, September–October 2025, DOI 10.1109/MPE.2025.3579718. A foundation model is a pretrained model intended for reuse across tasks. We verified the architecture through the authors’ full ERCOT presentation and official project page. The publisher/preprint download was unavailable, so we attribute no uninspected experimental results to the article. The community and repositories keep changing. Their current features are not a fixed 2025 benchmark. Le Xie; slides credit Le Xie and Qian Zhang; A Roadmap Towards Agentic Intelligence in Power Systems; Author presentation slide 11 Roadmap from the December2025 author presentation; not a measured deployment or a frozen specification of every current PowerAgent repository. Source locator: Author presentation slide 11; three layer panels in the left column. Original URL: https://www.ercot.com/files/docs/2025/12/01/4-Guest-Presentation-A-Roadmap-toward-Agentic-Intelligence-in-Power-Systems.pdf
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Qian Zhang, Le Xie. PowerAgent: A Road Map Toward Agentic Intelligence in Power Systems: Foundation Model, Model Context Protocol, and Workflow. IEEE Power and Energy Magazine, volume 23, issue 5, pages 93–101. 2025.
Full source: https://doi.org/10.1109/MPE.2025.3579718

Le Xie; slides credit Le Xie and Qian Zhang. A Roadmap Towards Agentic Intelligence in Power Systems. ERCOT Technology and Security Committee guest presentation. 8 December 2025.
Full source: https://www.ercot.com/files/docs/2025/12/01/4-Guest-Presentation-A-Roadmap-toward-Agentic-Intelligence-in-Power-Systems.pdf

Power and AI Initiative / PowerAgent community, Harvard SEAS. PowerAgent — Open-Source Agentic AI for Power Grids. Official Harvard project website. Live project page reviewed 17 October 2026.
Full source: https://poweragent.seas.harvard.edu/

Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>PowerAgent example: what changes when load is added?</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_poweragent_impact_workflow.png" alt="Original Harvard concept for grid-impact studies. The separate PowerWF example uses LangGraph and PowerWorld; this is not its exact graph." style="max-height:420px;height:auto"><figcaption>Original Harvard concept for grid-impact studies. The separate PowerWF example uses LangGraph and PowerWorld; this is not its exact graph.</figcaption></figure><div><ul><li>It runs power flow and single-outage checks (N−1) for the original case and the added-load case.</li><li>LangGraph manages the steps and saved results. PowerWorld calculates the electrical results.</li></ul></div></div>
<div class="sources">Source: <a href="https://github.com/Power-Agent/PowerWF/blob/main/Grid%20Impact%20Evaluation/src/agent/graph.py">PowerAgent / PowerWF community contributors. PowerWF Grid Impact Evaluation — LangGraph workflow source. Author-maintained source code, Grid Impact Evaluation/src/agent/graph.py. Live source inspected 17 October 2026.</a></div>
<span class="pageno">29 / 80</span></div>

<!--
This is a specific current workflow maintained by the authors. It does not establish one SDK for the whole PowerAgent initiative. In the code, graph.py imports StateGraph and ToolNode, saves workflow flags and returns from the shared tools node to the relevant step. A bus is a connection point in the model. The author presentation discusses load-growth and data-center studies using power flow, congestion, voltage and N−1 checks, which examine single-component outages. The code and demonstrations show the workflow. They provide no controlled utility timing or reliability estimate. The reading guide links the exact source file. Le Xie; slides credit Le Xie and Qian Zhang; A Roadmap Towards Agentic Intelligence in Power Systems; Author presentation slide 14, right-hand grid-impact process A conceptual author demonstration. It is not an exact diagram of the later PowerWF graph.py or a utility performance trial. Source locator: Author presentation slide 14, right-hand grid-impact process. Original URL: https://www.ercot.com/files/docs/2025/12/01/4-Guest-Presentation-A-Roadmap-toward-Agentic-Intelligence-in-Power-Systems.pdf
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
PowerAgent / PowerWF community contributors. PowerWF Grid Impact Evaluation — LangGraph workflow source. Author-maintained source code, Grid Impact Evaluation/src/agent/graph.py. Live source inspected 17 October 2026.
Full source: https://github.com/Power-Agent/PowerWF/blob/main/Grid%20Impact%20Evaluation/src/agent/graph.py

Le Xie; slides credit Le Xie and Qian Zhang. A Roadmap Towards Agentic Intelligence in Power Systems. ERCOT Technology and Security Committee guest presentation. 8 December 2025.
Full source: https://www.ercot.com/files/docs/2025/12/01/4-Guest-Presentation-A-Roadmap-toward-Agentic-Intelligence-in-Power-Systems.pdf

PowerAgent community contributors. Power-Agent/PowerWF. Author-maintained GitHub repository. Live source repository reviewed 17 October 2026.
Full source: https://github.com/Power-Agent/PowerWF
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>DrAgent: reading a recorded grid fault</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/power_dragent_waveform.png" alt="Original DrAgent Figure 2, PDF p.4. The third current channel shows a fault in a sample disturbance record." style="max-height:365px;height:auto"><figcaption>Original DrAgent Figure 2, PDF p.4. The third current channel shows a fault in a sample disturbance record.</figcaption></figure></div><ul><li>The third current trace shows the fault. Dashed lines mark its start, highest current and clearance (when the fault ends).</li></ul></div>
<div class="sources">Source: <a href="https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf">Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.</a></div>
<span class="pageno">30 / 80</span></div>

<!--
The Hitachi Energy paper studies disturbance analysis on transmission lines. This is an original figure extracted from the research paper, not an invented event or a live operating screen. First identify how the curve changes. Numerical tools return a sample index or current measurement. The task still requires an engineering interpretation of those values.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>DrAgent selects tools to answer a fault question</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_dragent_architecture.png" alt="Original DrAgent architecture: planning, tool execution and answer generation." style="max-height:420px;height:auto"><figcaption>Original DrAgent architecture: planning, tool execution and answer generation.</figcaption></figure><div><ul><li>The plan chooses signal-analysis tools or manual search to match the question.</li><li>Signal tools measure the fault. Manual search finds product information in documents.</li></ul></div></div>
<div class="sources">Source: <a href="https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf">Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.</a></div>
<span class="pageno">31 / 80</span></div>

<!--
ReWOO plans the work before running tools that use earlier results. COMTRADE is a format for recorded power-system disturbances. The implementation uses Gemini 1.5Pro for planning, a dozen domain functions and retrieval-augmented generation (RAG) over 138 product manuals. RAG retrieves relevant source text for the model. The displayed picture is the paper’s original architecture. The following dependency example is a spoken teaching example. To convert a fault’s starting sample to seconds, the system first needs both the sample index and sampling rate. This dependency motivates the next graph explanation. Barun Kumar Saha, Aarthi V, O. D. Naidu; DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models; Figure 1, PDF page 2 Paper architecture based on ReWOO; the picture does not establish utility deployment or autonomous command authority. Source locator: Figure 1, PDF page 2. Original URL: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>DrAgent: more correct answers, with errors still present</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/power_dragent_counts.png" alt="Counts reconstructed from Table IV and the Appendix. They are neither new experiments nor the paper’s mean-score measure." style="max-height:350px;height:auto"><figcaption>Counts reconstructed from Table IV and the Appendix. They are neither new experiments nor the paper’s mean-score measure.</figcaption></figure></div><ul><li>We counted scores of 2 or more as correct across the paper’s 18 recorded cases.</li><li>Timing the fault’s end remains harder. The grading rules also accept a correctly labeled fault duration.</li></ul></div>
<div class="sources">Source: <a href="https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf">Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.</a></div>
<span class="pageno">32 / 80</span></div>

<!--
Fault inception: baseline 12/18, agent 18/18. Maximum current: baseline 16/18, agent 18/18. Clearance/timing: baseline 4/18, agent 13/18. The paper allows 3 ms timing error and 5% current error. One expert graded the answers. Q6 footnote 8 accepts a correctly labeled duration, so these are not strictly clearance-timestamp accuracy counts. The printed Q6 mean conflicts with the individual cells. This chart therefore uses the audited cell counts.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Three kinds of graph have different jobs</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/va_three_graphs.svg" alt="Three different meanings of “graph.” These small examples explain connections, not calculated electrical results." style="height:315px;max-height:315px"><figcaption>Three different meanings of “graph.” These small examples explain connections, not calculated electrical results.</figcaption></figure><ul><li>Grid edges show electrical connections. A task DAG (directed acyclic graph) links calculations through the results they need.</li><li>Workflow edges show which software step can run next, including a retry loop.</li></ul></div>
<div class="sources">Source: <a href="https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf">Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.</a></div>
<span class="pageno">33 / 80</span></div>

<!--
A radial feeder has a tree-like electrical layout, but its software can still contain loops. A calculation graph without loops can analyze a meshed electrical network. State which graph you mean before discussing a node, connection or loop. A software architecture drawing is not the electrical model.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654

D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A DAG shows which result must come first</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/power_fault_dag.svg" alt="Original teaching adaptation of DrAgent’s tool dependencies, rather than its exact execution graph." style="height:330px;max-height:330px"><figcaption>Original teaching adaptation of DrAgent’s tool dependencies, rather than its exact execution graph.</figcaption></figure><ul><li>A DAG links results to calculations that need them. Its arrows do not form a loop.</li><li>Run independent calculations when inputs are ready. Wait for every required result before reporting.</li></ul></div>
<div class="sources">Source: <a href="https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf">Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.</a></div>
<span class="pageno">34 / 80</span></div>

<!--
Every task must follow the tasks that produce its inputs. This is a valid topological order. Fault-start sample and sampling rate must both exist before the time conversion runs. Finding maximum current can run independently of that conversion when both use the same unchanged record. Dependencies determine which tasks can run together. The positions of boxes in a drawing do not.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Barun Kumar Saha, Aarthi V, O. D. Naidu. DrAgent: An Agentic Approach to Fault Analysis in Power Grids Using Large Language Models. 2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC), pp. 938–945. 2025-02-18–21.
Full source: https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2025%2Fpresentation%2F1571098105.pdf
Publication: https://doi.org/10.1109/ICAIIC64266.2025.10920654
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>LangGraph can pause to inspect a run</h1>
<div class="content source-focus"><figure><img src="/images/real_framework_langgraph_static_interrupt.svg" alt="Real LangGraph debugger screenshot. A paused run can be inspected before the next software step." style="max-height:425px;height:auto"><figcaption>Real LangGraph debugger screenshot. A paused run can be inspected before the next software step.</figcaption></figure><div><ul><li>A debugger can pause the graph so a developer can inspect it. A failed check can also send execution back to an earlier step.</li><li>Software routing does not check the grid model. The application still checks inputs and engineering results.</li></ul></div></div>
<div class="sources">Source: <a href="https://docs.langchain.com/oss/python/langgraph/graph-api">LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.</a></div>
<span class="pageno">35 / 80</span></div>

<!--
LangGraph is software for running workflows. It can support loops, unlike a DAG. StateGraph defines stored state fields and workflow nodes. Application-defined reducers specify how updates from parallel steps combine. A node may call an engineering tool with fixed rules or an AI model. The application must define validation, stopping and permissions. Running the graph does not prove that an electrical solution is feasible. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. A static debug breakpoint differs from a dynamic interrupt requesting human input. Source figure locator: Debugging with interrupts. Original source URL: https://docs.langchain.com/oss/python/langgraph/interrupts
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
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
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Saved state must identify the study and its evidence</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_framework_langgraph_state.svg" alt="Original LangGraph state diagram. Software checkpoints still need grid-case, time and evidence identifiers." style="max-height:310px;height:auto"><figcaption>Original LangGraph state diagram. Software checkpoints still need grid-case, time and evidence identifiers.</figcaption></figure></div><ul><li>Save the case ID, input versions, evidence, status and attempt count.</li><li>Label each result with its case or outage ID. This helps reveal missing or duplicate results when parallel work comes together.</li></ul></div>
<div class="sources">Source: <a href="https://docs.langchain.com/oss/python/langgraph/graph-api">LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.</a></div>
<span class="pageno">36 / 80</span></div>

<!--
The published figure shows generic LangGraph software state. For a spoken grid-study example, imagine an application-specific expected-case set that includes outage_34 while the returned evidence lacks that case. Those case fields are tutorial requirements, not a built-in LangGraph power-system schema. Default update behavior does not guarantee that all branch results survive a merge. Define and test the reducer, or an external evidence store, to preserve case IDs and detect duplicates or missing outputs. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. The extra grid identifiers are tutorial requirements; they are not fields proven by this generic illustration. Source figure locator: Get state history. Original source URL: https://docs.langchain.com/oss/python/langgraph/checkpointers
Takeaway: Saved state identifies the evidence. The application still has to check it.
Nominal duration: 2 minutes.

Full sources:
LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

LangChain documentation maintainers. LangGraph Persistence. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/persistence

LangChain documentation maintainers. Checkpointers. Docs by LangChain, Python LangGraph documentation. Undated live documentation; accessed October 18, 2026.
Full source: https://docs.langchain.com/oss/python/langgraph/checkpointers
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>A checkpoint lets a workflow pause and resume</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_framework_langgraph_checkpoint.svg" alt="Original LangGraph checkpoint diagram. Saving progress does not prove that the grid data still match." style="max-height:310px;height:auto"><figcaption>Original LangGraph checkpoint diagram. Saving progress does not prove that the grid data still match.</figcaption></figure></div><ul><li>A checkpoint saves progress; thread_id links the saved steps to the same workflow.</li><li>Changed grid connections can make old results invalid. Check them and rerun affected studies.</li></ul></div>
<div class="sources">Source: <a href="https://docs.langchain.com/oss/python/langgraph/persistence">LangChain documentation maintainers. LangGraph Persistence. Official LangChain documentation. Accessed 2026-10-17; live documentation.</a></div>
<span class="pageno">37 / 80</span></div>

<!--
An interrupt can pause for outside review and later resume in the same thread. Current LangGraph documentation says the interrupted node restarts from its beginning. Actions before the interrupt can therefore happen again. Use stable step IDs or other idempotency controls, which prevent repeated execution from applying the same change twice. This example grants no permission to command live grid equipment. Source: LangChain documentation maintainers, official LangGraph documentation. Accessed October 18, 2026. Saved software state does not prove that an external grid snapshot remains current. Source figure locator: Opening checkpoint illustration. Original source URL: https://docs.langchain.com/oss/python/langgraph/checkpointers
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
LangChain documentation maintainers. LangGraph Persistence. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/persistence

LangChain documentation maintainers. LangGraph Interrupts. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/interrupts

LangChain documentation maintainers. Checkpointers. Docs by LangChain, Python LangGraph documentation. Undated live documentation; accessed October 18, 2026.
Full source: https://docs.langchain.com/oss/python/langgraph/checkpointers
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Parallel outage studies must account for every case</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_framework_anthropic_parallel.svg" alt="Original Anthropic parallel workflow. A grid study must also account for missing or failed outage cases." style="max-height:310px;height:auto"><figcaption>Original Anthropic parallel workflow. A grid study must also account for missing or failed outage cases.</figcaption></figure></div><ul><li>Run each selected outage on a separate, consistent copy of the same starting grid case.</li><li>Before combining results, compare the returned case IDs with the expected list. Mark failed or missing cases as unresolved.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2512.20789v1">Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).</a></div>
<span class="pageno">38 / 80</span></div>

<!--
The goal is complete evidence for the selected study scope, rather than a count of completed software steps. In a spoken grid-study example, if a case named C2 fails, the output should name C2, explain its failure and state what remains unknown. This applies AgentiGrid’s lesson about incomplete coverage. Completing a selected set of outages does not prove coverage of every N−1 contingency, meaning every relevant single-component outage. Source: Anthropic, Building effective agents (December 19, 2024). The aggregator picture does not imply that missing results are automatically detected. Source figure locator: Workflow: Parallelization. Original source URL: https://www.anthropic.com/engineering/building-effective-agents
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).
Full source: https://arxiv.org/pdf/2512.20789v1

Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>PowerDAG checks the steps needed before a tool runs</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_powerdag_architecture.png" alt="Original PowerDAG v4 architecture, including the supervisor before environment execution." style="max-height:420px;height:auto"><figcaption>Original PowerDAG v4 architecture, including the supervisor before environment execution.</figcaption></figure><div><ul><li>PowerDAG finds relevant verified workflow examples. It uses a dependency graph and a gate that checks required earlier tool calls.</li><li>The benchmark covers 108 tools, ten task families and four Vermont feeder models (local distribution networks).</li></ul></div></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2603.17418v4">Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.</a></div>
<span class="pageno">39 / 80</span></div>

<!--
Use the inspected v4 dated 5 July 2026: Emmanuel O. Badmus and Amritanshu Pandey, PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. Earlier versions have different titles and performance headlines. Its four network models are Rochester, Stowe, Glover and South Hero. The graph identifies required earlier tools and gates calls while the agent continues choosing steps. A tool can run successfully in the wrong study state if earlier work is missing. The gate addresses that workflow problem. Emmanuel O. Badmus, Amritanshu Pandey; PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis; Figure 2, v4 PDF page 3 This is the v4 research architecture. Formal supervision checks encoded prior Write-tool names; it does not establish all freshness, parameter or physical-safety checks. Source locator: Figure 2, v4 PDF page 3. Original URL: https://arxiv.org/pdf/2603.17418v4
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4

Emmanuel O. Badmus and contributors. DistGrid-AgentBench: A Distribution Grid Benchmark for Agentic AI. Author-maintained GitHub repository. Live repository reviewed 17 October 2026.
Full source: https://github.com/emmanuelbadmus/DistGrid-AgentBench
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>PowerDAG: solve the grid before checking its voltage</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/revision_powerdag_gate.svg" alt="Teaching adaptation: the current-v43 check adds a freshness rule. The paper’s gate checks which required tools have already run." style="height:330px;max-height:330px"><figcaption>Teaching adaptation: the current-v43 check adds a freshness rule. The paper’s gate checks which required tools have already run.</figcaption></figure><ul><li>In the paper’s example, a voltage-violation check needs a solved network state first.</li><li>If an earlier required step is missing, the gate rejects the call and tells the agent what to do first.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2603.17418v4">Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.</a></div>
<span class="pageno">40 / 80</span></div>

<!--
Section IV-C uses voltage-violation checks to explain these requirements. Equation 9 checks whether required Write-tool names appear among executed tool names. That alone does not check whether their outputs match the current grid version. The diagram adds current-v43 freshness as a teaching condition. The introduction also explains how missing a network update can leave a solver using the wrong state. Appendix B reports this Stowe execution order: load_load, load_solar, load_distribution_network, create_and_initialize_model, build_constraints, build_objective, solve, update_network_voltages and plot_network_data. This is a reported order, not a claimed minimal set of dependency links. The authors curate the rules. Tools without rules remain executable. Passing the gate does not prove numerical feasibility or safety.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>PowerDAG results: the same queries, four setups</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/powerdag_revision_result.png" alt="PowerDAG v4, Table II. ReAct: a reason-and-act loop. JIT: prerequisite checks just before a call." style="max-height:315px;height:auto"><figcaption>PowerDAG v4, Table II. ReAct: a reason-and-act loop. JIT: prerequisite checks just before a call.</figcaption></figure></div><ul><li>Each GPT-5.5 setup runs the same 150 test queries once.</li><li>Pass@1 measures first-run workflow success: required tool calls, valid inputs and correct order. It does not measure field reliability.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2603.17418v4">Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.</a></div>
<span class="pageno">41 / 80</span></div>

<!--
The reported Pass@1 scores are ReAct 77.33%, retrieval-only PowerChain-AR 92.67%, JIT supervision only 96.00%, and full PowerDAG 98.00%. Each setup runs 150 queries. Across the full study, six setups and ten model backends produce 9,000 query runs. Full PowerDAG scores 97.33% with Gemini 3.1 Pro and 92.67% with Qwen 3.6-27B. Pass@1 is an automated check against expert workflows. The test queries were kept out of the example set, but they use the same ten task families; this is a within-family test. These scores do not measure outage avoidance or the reliability of live commands. The comparison tests complete setups as built. It does not isolate the effect of one graph edge.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>PowerDAG: what can others check and reuse?</h1>
<div class="content"><ul><li>The public benchmark provides tasks, tool descriptions, workflow records and scoring code.</li><li>Three task groups can run with the public files. Seven need private grid-map data and network tools.</li><li>Reuse the idea of checking required earlier steps. Test the new tools, case state and engineering results.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/emmanuelbadmus/DistGrid-AgentBench">Emmanuel O. Badmus and contributors. DistGrid-AgentBench: A Distribution Grid Benchmark for Agentic AI. Author-maintained GitHub repository. Live repository reviewed 17 October 2026.</a></div>
<span class="pageno">42 / 80</span></div>

<!--
The author README names BESS, basicPV and GFI as the three task groups that can run from the public download. The other seven need private feeder data, geographic data (GIS) and network-tool code. Public workflow records let readers inspect the work, but do not make every experiment reproducible from the public files alone. This is a distribution-study research benchmark using real feeder models. It does not show a named utility running PowerDAG in a control room. Keep the task population and score definition with every reported percentage.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Emmanuel O. Badmus and contributors. DistGrid-AgentBench: A Distribution Grid Benchmark for Agentic AI. Author-maintained GitHub repository. Live repository reviewed 17 October 2026.
Full source: https://github.com/emmanuelbadmus/DistGrid-AgentBench

Emmanuel O. Badmus, Amritanshu Pandey. PowerDAG: Supervisory Agentic AI System for Automating Distribution Grid Analysis. arXiv preprint, version 4. 5 July 2026 (v4); first submitted 18 March 2026.
Full source: https://arxiv.org/pdf/2603.17418v4
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Simulation agents find functions, run code and repair errors</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_paper_daline_feedback.png" alt="Original environmental acting module: simulation errors feed retrieval and code repair." style="max-height:305px;height:auto"><figcaption>Original environmental acting module: simulation errors feed retrieval and code repair.</figcaption></figure></div><ul><li>The agent finds MATLAB functions and settings, writes code and runs the study.</li><li>A software error triggers repair. Code that runs can still use the wrong settings.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.1109/TSG.2025.3589114">Mengshuo Jia, Zeyu Cui, Gabriela Hug. Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework. IEEE Transactions on Smart Grid, volume 16, issue 6, pages 5556–5572. 2025.</a></div>
<span class="pageno">43 / 80</span></div>

<!--
Jia, Cui and Hug test DALINE and MATPOWER simulation tasks. The paper does not identify LangGraph as its software framework. Its run-and-repair loop is an example of using feedback. The engineering check must compare the actual study and settings with the requested task. A MATLAB run without an error is not enough. Mengshuo Jia, Zeyu Cui, Gabriela Hug; Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework; Figure 5, author-preprint PDF page 7 Published workflow module, not evidence that error-free execution satisfies the requested engineering settings. Source locator: Figure 5, author-preprint PDF page 7. Original URL: https://doi.org/10.1109/TSG.2025.3589114
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Mengshuo Jia, Zeyu Cui, Gabriela Hug. Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework. IEEE Transactions on Smart Grid, volume 16, issue 6, pages 5556–5572. 2025.
Full source: https://doi.org/10.1109/TSG.2025.3589114
Full paper: https://arxiv.org/pdf/2411.16707v3
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Simulation-agent results: points, not a pass rate</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/power_study_feedback.png" alt="DALINE comparison reported in the author preprint, Figure 8 / section V. Each task allows up to three attempts." style="max-height:350px;height:auto"><figcaption>DALINE comparison reported in the author preprint, Figure 8 / section V. Each task allows up to three attempts.</figcaption></figure></div><ul><li>Across 34 DALINE tasks, the score averages graded attempts and penalizes extra settings. The 93.13 score is not a pass rate.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.1109/TSG.2025.3589114">Mengshuo Jia, Zeyu Cui, Gabriela Hug. Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework. IEEE Transactions on Smart Grid, volume 16, issue 6, pages 5556–5572. 2025.</a></div>
<span class="pageno">44 / 80</span></div>

<!--
Each attempt scores 100 when it meets every requirement without extra settings, 50 when unnecessary settings remain, and 0 when a requirement is missed. The score averages the allowed attempt slots. If attempts are unused, the last score fills those slots. The API setups use gpt-4o-2024-05-13. The built-in ChatGPT-RAG setup runs in a different product. These are comparisons of complete systems, so they do not isolate the effect of one feature. In the related MATPOWER test, the full setup scores 96.85 over 35 tasks with up to five attempts per task.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Mengshuo Jia, Zeyu Cui, Gabriela Hug. Enhancing LLMs for Power System Simulations: A Feedback-Driven Multi-Agent Framework. IEEE Transactions on Smart Grid, volume 16, issue 6, pages 5556–5572. 2025.
Full source: https://doi.org/10.1109/TSG.2025.3589114
Full paper: https://arxiv.org/pdf/2411.16707v3
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Trying again can repeat the same software error</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_framework_anthropic_evaluator.svg" alt="Original Anthropic feedback pattern. A retry must actually use the repaired code and changed inputs." style="max-height:310px;height:auto"><figcaption>Original Anthropic feedback pattern. A retry must actually use the repaired code and changed inputs.</figcaption></figure></div><ul><li>R02 found that an agent request and its cache key both left out reactive load.</li><li>Fixing the request still returned the old result: the cache key had not changed.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2607.28822v1">Eve Tsybina, Samim Konjicija, Slaven Peles. Agentic Artificial Intelligence for Power Systems: Strategies to Identify and Close Capability Gaps. arXiv. 30 July 2026; v1.</a></div>
<span class="pageno">45 / 80</span></div>

<!--
The paper asks for a load of 100 MW and 10 Mvar. The Mvar part is reactive load; leaving it out changes the study. A cache stores past results for reuse. Its key tells the software which inputs produced a result. If the key ignores reactive load, a corrected request can still return the old result. Asking the model to try harder will not fix that software error. Test the tool adapter and cache. The key must include every input that can affect the result, including relevant model and topology versions. Source: Anthropic, Building effective agents (December 19, 2024). An LLM evaluator does not prove grid feasibility, permission or fresh input data. Source figure locator: Workflow: Evaluator-optimizer. Original source URL: https://www.anthropic.com/engineering/building-effective-agents
Takeaway: Reliable agents also need correct tool adapters, caches and other software.
Nominal duration: 2.5 minutes.

Full sources:
Eve Tsybina, Samim Konjicija, Slaven Peles. Agentic Artificial Intelligence for Power Systems: Strategies to Identify and Close Capability Gaps. arXiv. 30 July 2026; v1.
Full source: https://arxiv.org/abs/2607.28822v1
Full paper: https://arxiv.org/pdf/2607.28822v1

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>X-GridAgent divides a request into jobs and tool calls</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_paper_xgrid_architecture.png" alt="Original X-GridAgent architecture: planning, coordination and MCP-based action services." style="max-height:305px;height:auto"><figcaption>Original X-GridAgent architecture: planning, coordination and MCP-based action services.</figcaption></figure></div><ul><li>The planner breaks down the request. The coordinator passes work to specialized tool services.</li><li>Eight MCP services handle analysis, data and plots. Numerical studies use pandapower.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2512.20789v1">Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).</a></div>
<span class="pageno">46 / 80</span></div>

<!--
The eight services cover retrieval, power flow, optimal power flow (OPF), contingencies, short circuits, topology, editing and plotting. The paper does not name LangGraph or another open workflow SDK. MCP is the tool interface. It does not calculate the electrical result or guarantee that the agent chose the right cases. The separate numerical comparison discussed in this tutorial selects three lines; the architecture figure itself does not show that query. Keep it separate from the paper's different query that selects five. Yihan (Logon) Wen, Xin Chen; X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis; Figure 2, PDF page 3 Architecture diagram of a research assistant. MCP supplies an interface; numerical analyses use pandapower. No LangGraph SDK is inferred. Source locator: Figure 2, PDF page 3. Original URL: https://arxiv.org/pdf/2512.20789v1
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).
Full source: https://arxiv.org/pdf/2512.20789v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>X-GridAgent results: report when a solver does not converge</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/power_study_xgrid.png" alt="X-GridAgent Table I, Q10. The paper does not give objective units. A failed solve is not a zero-cost answer." style="max-height:350px;height:auto"><figcaption>X-GridAgent Table I, Q10. The paper does not give objective units. A failed solve is not a zero-cost answer.</figcaption></figure></div><ul><li>The 39-bus AC optimal power flow (OPF) study solves the base and outage cases. Doubling the load does not converge.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2512.20789v1">Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).</a></div>
<span class="pageno">47 / 80</span></div>

<!--
The reported objective rises from 41,872.3 in the base case to 42,115.34 with line 11 out of service, a difference of 243.04 in the table's unspecified units. The doubled-load AC OPF does not converge. Do not treat nonconvergence as a proof that no feasible solution exists. The authors report 100% success in their selected repeated-query test, using manually obtained conventional solutions as references. That result does not establish reliability on random tasks or in a live utility.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).
Full source: https://arxiv.org/pdf/2512.20789v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>GridMind 2025 connects typed agents to solvers</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_gridmind2025_architecture.png" alt="Original GridMind2025 diagram of specialized agents and numerical analysis tools." style="max-height:420px;height:auto"><figcaption>Original GridMind2025 diagram of specialized agents and numerical analysis tools.</figcaption></figure><div><ul><li>GridMind 2025 uses PydanticAI and pandapower for AC optimal power flow (ACOPF) and outage studies.</li><li>It reports 100% ACOPF success on case 118 across six models. That does not prove complete outage coverage.</li></ul></div></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2509.02494v1">Hongwei Jin, Kibaek Kim, Jonghwan Kwon. GridMind: LLMs-Powered Agents for Power System Analysis and Operations. arXiv; published as SC Workshops 2025, DOI 10.1145/3731599.3767409. 2025-09-02 (arXiv v1); SC Workshops 2025.</a></div>
<span class="pageno">48 / 80</span></div>

<!--
The 2025 paper tests 14-, 30-, 118- and 300-bus systems. Figure 3 compares ACOPF success and run time on case 118. The timing distributions use five repeats; do not invent a larger denominator for the success claim. PydanticAI supports structured, typed inputs and outputs. This system is different from the 2026 GridMind weather workflow, which uses LangGraph. Keep the year and paper title clear. Hongwei Jin, Kibaek Kim, Jonghwan Kwon; GridMind: LLMs-Powered Agents for Power System Analysis and Operations; Figure 2, PDF page 2 This is the2025 PydanticAI/pandapower study, not the separate2026 LangGraph weather-risk system. Source locator: Figure 2, PDF page 2. Original URL: https://arxiv.org/abs/2509.02494v1
Takeaway: A correct result for one task does not validate every related task.
Nominal duration: 2 minutes.

Full sources:
Hongwei Jin, Kibaek Kim, Jonghwan Kwon. GridMind: LLMs-Powered Agents for Power System Analysis and Operations. arXiv; published as SC Workshops 2025, DOI 10.1145/3731599.3767409. 2025-09-02 (arXiv v1); SC Workshops 2025.
Full source: https://arxiv.org/abs/2509.02494v1
Full paper: https://arxiv.org/pdf/2509.02494v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>GridMind: reported answers need independent checks</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_paper_gridmind2025_response.png" alt="A separate published response claims no thermal overloads and flags a balance error. It is not independent ground truth." style="max-height:270px;height:auto"><figcaption>A separate published response claims no thermal overloads and flags a balance error. It is not independent ground truth.</figcaption></figure></div><ul><li>On case 118, one model reports 165% maximum overload; five report 137%. They also name different critical lines.</li><li>The table has no complete independent outage reference. Agreement alone cannot tell us which answer is right.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2509.02494v1">Hongwei Jin, Kibaek Kim, Jonghwan Kwon. GridMind: LLMs-Powered Agents for Power System Analysis and Operations. arXiv; published as SC Workshops 2025, DOI 10.1145/3731599.3767409. 2025-09-02 (arXiv v1); SC Workshops 2025.</a></div>
<span class="pageno">49 / 80</span></div>

<!--
These are the paper's tool results and interpretations, not a new experiment. The differences may reflect which cases were studied, how they were listed or how results were read. The table does not establish which answer covers every required outage. Ask for the same case definitions and an independent reference study. Do not assume the majority is right or calculate a failure probability from six different model setups. Hongwei Jin, Kibaek Kim, Jonghwan Kwon; GridMind: LLMs-Powered Agents for Power System Analysis and Operations; Figure 8, PDF page 10, baseline and coverage portion of agent response This is an example response, not independent ground truth or the Table1 comparison. Its own output reports a power-balance issue; an answer still needs engineering review. Source locator: Figure 8, PDF page 10, baseline and coverage portion of agent response. Original URL: https://arxiv.org/abs/2509.02494v1
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Hongwei Jin, Kibaek Kim, Jonghwan Kwon. GridMind: LLMs-Powered Agents for Power System Analysis and Operations. arXiv; published as SC Workshops 2025, DOI 10.1145/3731599.3767409. 2025-09-02 (arXiv v1); SC Workshops 2025.
Full source: https://arxiv.org/abs/2509.02494v1
Full paper: https://arxiv.org/pdf/2509.02494v1
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>GridMind 2026 reuses results when their inputs still match</h1>
<div class="content"><pre class="source-excerpt">Reported session: seven queries on synthetic Texas 2000
Change cascade fan-out k → rerun cascade
Shift forecast by 6 h → rerun all five stages
Restore the exact old inputs → reuse saved results</pre><ul><li>LangGraph coordinates five stages: weather, outages, OPF, screening and cascade analysis.</li><li>Input fingerprints identify saved results. A changed forecast makes affected results need a new run.</li></ul></div>
<div class="sources">Source: <a href="https://openreview.net/forum?id=Cs5TBzzNym">D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.</a></div>
<div class="takeaway">Reuse a result only when the inputs it depends on still match.</div>
<span class="pageno">50 / 80</span></div>

<!--
AERIS supplies weather data. LUMINA or pandapower runs the base OPF. A LUMINA surrogate screens cases, and EPFast uses a reduced-order DC model for cascade simulation. A surrogate is a faster approximation of a more detailed calculation. Which stages need to rerun depends on the actual inputs each stage uses. Here, the contingency stage reads outage schedules directly, so an ACOPF change alone does not require every later-looking stage to rerun. The fingerprints are content hashes of declared inputs. They can show that those inputs match; they do not prove correctness or detect changes that were never recorded.
Takeaway: Reuse a result only when the inputs it depends on still match.
Nominal duration: 2.5 minutes.

Full sources:
D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

Argonne GridAI project team. GridAI — AI Foundation Models & Agents for the Power Grid. Live project page reviewed 17 October 2026.
Full source: https://argonne-gridfm.github.io/
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>GridMind: which changes need a new run?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/power_gridmind_invalidation.svg" alt="Teaching view of GridMind 2026 Table 1. Only the reported affected stages are shown; no extra dependencies are assumed." style="height:330px;max-height:330px"><figcaption>Teaching view of GridMind 2026 Table 1. Only the reported affected stages are shown; no extra dependencies are assumed.</figcaption></figure><ul><li>Change only k: rerun cascade. Shift the forecast by six hours: rerun all five stages.</li><li>In this implementation, changing the ACOPF solver reruns ACOPF only.</li></ul></div>
<div class="sources">Source: <a href="https://openreview.net/forum?id=Cs5TBzzNym">D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.</a></div>
<span class="pageno">51 / 80</span></div>

<!--
The five stages are line-wind, outages, ACOPF, contingency and cascade. These dependencies belong to this implementation. Its contingency stage reads outage schedules directly, rather than taking ACOPF output. Returning to exactly the same inputs can allow reuse of an earlier result. Every input that affects a result must be included in its identity; otherwise, the cache may return an out-of-date result.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>GridMind results: fewer stages and less time are different</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/expanded_power_gridmind.png" alt="GridMind 2026 Table 1: full reruns in fresh workspaces versus saved-result reuse, on a synthetic 2,000-bus hurricane-risk study." style="max-height:350px;height:auto"><figcaption>GridMind 2026 Table 1: full reruns in fresh workspaces versus saved-result reuse, on a synthetic 2,000-bus hurricane-risk study.</figcaption></figure></div><ul><li>For the same seven queries, reuse cuts stage runs by 60% and total run time by 52.7%. Some stages cost more time than others.</li></ul></div>
<div class="sources">Source: <a href="https://openreview.net/forum?id=Cs5TBzzNym">D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.</a></div>
<span class="pageno">52 / 80</span></div>

<!--
The 60% reduction is in stage runs, not time. The measured time reduction is about 52.7%, because stages take different amounts of time. The gain comes from the workflow and reuse of saved results; it is not just a faster language model. This is one seven-query session, with no interval for variation across repeated sessions. The study uses surrogate and reduced-order simulations. Their results still need engineering validation before utility use.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Group exercise · 8 minutes</div>
<h1>Exercise 2: check whether saved weather-risk results still apply</h1>
<div class="content"><ul><li>A saved run uses forecast F0, topology v43 and cascade setting k=50. Only k changes to 200. What reruns?</li><li>Now shift the forecast by six hours. Which of the five saved stage results still apply?</li><li>A required simulation fails. What status and evidence should the operator receive?</li></ul></div>
<div class="sources">Source: <a href="https://openreview.net/forum?id=Cs5TBzzNym">D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.</a></div>
<span class="pageno">53 / 80</span></div>

<!--
Allow 2 minutes to think alone, 2 to compare in groups, 2 for discussion and 2 for the debrief. If only k changes, rerun cascade and retain the other results that still apply. If forecast initialization shifts, rerun all five stages in the cited workflow. If a required stage fails, return an incomplete or unresolved result. Include the case and stage IDs, input versions, tool error and conclusions that remain missing. Do not issue an all-clear report. F0 and v43 are teaching labels. Another implementation may have different dependencies. Keep these answers in the speaker notes.
Takeaway: 
Nominal duration: 8 minutes.

Full sources:
D. Adrian Maldonado, Jonghwan Kwon, Sunash B. Sharma, Hongwei Jin, Stefano Fenu, Emil Constantinescu, David Sehloff, Parfait Gasana, Duane Rudolph Verner, Kibaek Kim. GridMind: An Agentic Workflow for Weather-Driven Power Grid Risk Assessment. KDD 2026 Workshop on Scientific and Societal Agents / OpenReview. August 2026 workshop; reviewed 17 October 2026.
Full source: https://openreview.net/forum?id=Cs5TBzzNym
Full paper: https://openreview.net/pdf/5ad1c2afd7298f9e6ce3bc25f18e7165555e1ffd.pdf

LangChain documentation maintainers. LangGraph Persistence. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/persistence
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>PowerAgentBench-Dyn allows only specific model changes</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_dynamicbench_overview.png" alt="Original benchmark structure: input package, agentic system, tool calls and evaluation metrics." style="max-height:420px;height:auto"><figcaption>Original benchmark structure: input package, agentic system, tool calls and evaluation metrics.</figcaption></figure><div><ul><li>The Harvard-led test gives an agent a modified solar-PV dynamic model and feedback from eight DMView/PSS/E quality tests.</li><li>It may change only four REECAU1 controller gains. All other fields are locked; at most five updates are allowed.</li></ul></div></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2606.20401v1">Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).</a></div>
<span class="pageno">54 / 80</span></div>

<!--
Authors from Harvard SEAS, Politecnico di Milano and UBITECH make the permitted changes explicit and testable. A gain is a controller setting that affects its response. This task diagnoses and repairs a simulation model; it does not authorize a utility controller change. The starting model fails all eight tests. Allowing four gains to change does not mean every other engineering property has been validated. The author repository provides a test harness, but it needs licensed PSS/E and external DMView software. Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie; PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies; Figure 1, PDF page 2 Benchmark architecture, not the full PowerAgent roadmap or an operating utility deployment. Source locator: Figure 1, PDF page 2. Original URL: https://arxiv.org/abs/2606.20401v1
Takeaway: The agent must pass the tests and stay within the allowed changes.
Nominal duration: 2.5 minutes.

Full sources:
Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1

PowerAgent Community. Power-Agent/PowerAgentBench. Live author repository reviewed 17 October 2026.
Full source: https://github.com/Power-Agent/PowerAgentBench
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>PowerAgentBench-Dyn results: passed sessions and updates</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/expanded_power_dynamic.png" alt="PowerAgentBench-Dyn Table II: model-quality task. Other tasks in this benchmark use different models and checks." style="max-height:350px;height:auto"><figcaption>PowerAgentBench-Dyn Table II: model-quality task. Other tasks in this benchmark use different models and checks.</figcaption></figure></div><ul><li>A session passes only if all eight tests pass within five allowed updates. Testing one modified model limits what we can conclude.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2606.20401v1">Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).</a></div>
<span class="pageno">55 / 80</span></div>

<!--
The three models are Opus 4.8, Sonnet 4.6 and Haiku 4.5. The reported sessions all use one modified WECC solar-PV model. There is no matched human or fixed-search baseline, so the results do not establish a comparative speedup. Show the counts to make the sample size and failures visible. The number of model updates is a different measure from total operator time. A 10/10 row still has the small-sample limits explained later.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>PowerAgentBench-Dyn also checks grid response to faults</h1>
<div class="content"><ul><li>PowerMCP and PowerFactory study ten candidate faults and identify three critical cases.</li><li>Across six models, full-workflow passes range from 0/10 to 10/10. Passing includes correct findings and allowed mitigation.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2606.20401v1">Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).</a></div>
<div class="takeaway">Different tasks in one benchmark can fail in different ways.</div>
<span class="pageno">56 / 80</span></div>

<!--
This dynamic-security task is different from the model-quality task. It uses Opus 4.7, not Opus 4.8. Tables III–VI report Opus 4.7 at 9/10, Sonnet 4.6 at 9/10, Haiku 4.5 at 7/10, Gemini 3.1 Pro at 10/10, GPT-5.5 at 10/10 and Qwen 2.5-Coder-7B at 0/10. A pass requires the whole workflow: execute the study, match the offline reference for critical cases, correctly flag L02–25 at 160 ms as unstable, and assess only the allowed synchronous-condenser mitigation options (section IV-C / Table IV). These counts measure more than fault selection. A run may fail during tool execution before it reaches an engineering finding. Do not combine counts from different tasks or call them field reliability.
Takeaway: Different tasks in one benchmark can fail in different ways.
Nominal duration: 2.5 minutes.

Full sources:
Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).
Full source: https://arxiv.org/abs/2606.20401v1
Full paper: https://arxiv.org/pdf/2606.20401v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Grid-Agent tests proposed actions in a simulation copy</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_gridagent_architecture.png" alt="Original Grid-Agent concept: topology, planning, execution, validation and summary roles." style="max-height:420px;height:auto"><figcaption>Original Grid-Agent concept: topology, planning, execution, validation and summary roles.</figcaption></figure><div><ul><li>One agent finds grid violations, a planner proposes actions, and an executor applies them to a simulation copy.</li><li>A checker reruns power flow. It keeps helpful modeled changes and undoes unsuccessful ones.</li></ul></div></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2508.05702v3">Yan Zhang, Ahmad Mohammad Saber, Amr Youssef, Deepa Kundur. Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control. arXiv preprint. 2025-09-08 (v3); first submitted 2025-08-07.</a></div>
<span class="pageno">57 / 80</span></div>

<!--
The paper studies voltage violations, thermal-limit violations and disconnected buses. The inspected v3 does not name the numerical solver or workflow SDK. A sandbox is an isolated simulation copy. Restoring that copy does not show that a physical switching action is reversible or authorized. Each action still needs a clear physical meaning, limits and permissions. Yan Zhang, Ahmad Mohammad Saber, Amr Youssef, Deepa Kundur; Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control; Figure 1, v3 PDF page 5 The rollback is a simulation operation. The paper does not establish permission to reverse physical switching or a live utility rollout. Source locator: Figure 1, v3 PDF page 5. Original URL: https://arxiv.org/pdf/2508.05702v3
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Yan Zhang, Ahmad Mohammad Saber, Amr Youssef, Deepa Kundur. Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control. arXiv preprint. 2025-09-08 (v3); first submitted 2025-08-07.
Full source: https://arxiv.org/pdf/2508.05702v3
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Grid-Agent results need the number of trials</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_paper_gridagent_reported_results.png" alt="Original reported scenario-resolution and runtime comparison panels." style="max-height:305px;height:auto"><figcaption>Original reported scenario-resolution and runtime comparison panels.</figcaption></figure></div><ul><li>The paper reports 44%–100% scenario-resolution rates across planners, but does not give the exact total trial count.</li><li>It leaves proof of optimality and comparison with a numerical optimizer to future work.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2508.05702v3">Yan Zhang, Ahmad Mohammad Saber, Amr Youssef, Deepa Kundur. Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control. arXiv preprint. 2025-09-08 (v3); first submitted 2025-08-07.</a></div>
<span class="pageno">58 / 80</span></div>

<!--
The paper names seven scenarios, but does not explain repetition and averaging well enough to reconstruct successes out of seven or confidence intervals. Four planner rows report 100%, Flash-Lite 63% and GPT-4.1-Nano 44%. The prose and table give different CIGRE bus counts, so we do not repeat a precise size. Resolving a violation does not prove that the action is the best possible action. The architecture is useful, but the reporting limits prevent a broad reliability claim. Yan Zhang, Ahmad Mohammad Saber, Amr Youssef, Deepa Kundur; Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control; Figure 2 panels (a)–(b), v3 PDF page 7 The exact aggregate trial denominator is not disclosed. The author rates do not prove optimal control or general field reliability. Source locator: Figure 2 panels (a)–(b), v3 PDF page 7. Original URL: https://arxiv.org/pdf/2508.05702v3
Takeaway: State the allowed actions, limits, test cases and comparison method with a control claim.
Nominal duration: 2 minutes.

Full sources:
Yan Zhang, Ahmad Mohammad Saber, Amr Youssef, Deepa Kundur. Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control. arXiv preprint. 2025-09-08 (v3); first submitted 2025-08-07.
Full source: https://arxiv.org/pdf/2508.05702v3
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>VeraGrid-Agent uses solver results to answer a question</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_veragrid_agent_workflow.png" alt="Original VeraGrid-Agent workflow: question, LLM controller, input file, AC-OPF workspace and selected result reads." style="max-height:420px;height:auto"><figcaption>Original VeraGrid-Agent workflow: question, LLM controller, input file, AC-OPF workspace and selected result reads.</figcaption></figure><div><ul><li>The agent writes feeder inputs, runs VeraGrid AC OPF and reads the relevant result rows.</li><li>It can repair tool errors within a fixed budget, then return a multiple-choice answer.</li></ul></div></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2607.25155v1">Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi. VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge. arXiv preprint. 2026-07-28 (v1).</a></div>
<span class="pageno">59 / 80</span></div>

<!--
The test uses one balanced, radial 8-bus feeder, 33 question templates and 150 questions: 50 at each of three difficulty levels. Reference answers come from the same solver and circuit. The repository provides a test harness and saved reports. Its current interfaces do not prove which SDK the original paper used. AC OPF is AC optimal power flow, a constrained numerical study. Reading its output to answer a question is different from learning a general policy for feeder control. Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi; VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge; Figure 2, PDF page 2 A research question-answering workflow on one feeder. It is not a general feeder-control policy. Source locator: Figure 2, PDF page 2. Original URL: https://arxiv.org/pdf/2607.25155v1
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi. VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge. arXiv preprint. 2026-07-28 (v1).
Full source: https://arxiv.org/pdf/2607.25155v1

Shivanshu Tripathi / VeraGrid-Agent authors. Shivanshu-11/veragrid-llm-benchmark. Author GitHub repository. Reviewed 2026-10-17.
Full source: https://github.com/Shivanshu-11/veragrid-llm-benchmark
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>VeraGrid-Agent results: the same models with and without tools</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/power_study_veragrid.png" alt="VeraGrid-Agent Table I: selected comparisons using the same model. Missing or badly formatted answers count as incorrect." style="max-height:350px;height:auto"><figcaption>VeraGrid-Agent Table I: selected comparisons using the same model. Missing or badly formatted answers count as incorrect.</figcaption></figure></div><ul><li>All 150 questions use one fixed feeder. Better multiple-choice answers do not prove general dispatch or field performance.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/pdf/2607.25155v1">Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi. VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge. arXiv preprint. 2026-07-28 (v1).</a></div>
<span class="pageno">60 / 80</span></div>

<!--
The no-tool setup receives feeder and distributed-energy-resource information. The agent adds solver runs, reading tools and repeated feedback. This compares complete systems, not equal amounts of computation. The paper gives correct-answer counts out of 150, but no estimate of variation across repeated runs. Running the solver and interpreting its results are separate steps that can fail. The paper records some remaining agent errors.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi. VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge. arXiv preprint. 2026-07-28 (v1).
Full source: https://arxiv.org/pdf/2607.25155v1
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>AgentiGrid: what does one reported run mean?</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_agentigrid_architecture.png" alt="Original AgentiGrid data flow: loop controller, analysis-controller interface and ExaGO application." style="max-height:420px;height:auto"><figcaption>Original AgentiGrid data flow: loop controller, analysis-controller interface and ExaGO application.</figcaption></figure><div><ul><li>The September 2026 paper tests four models on three applications, using one 200-bus system.</li><li>The 12 searches are 12 different setups, not 12 repeats of one task.</li><li>ExaGO does the numerical analysis. The agent chooses changes and explains the results.</li></ul></div></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2609.04544v1">Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.</a></div>
<span class="pageno">61 / 80</span></div>

<!--
The three applications are dispatch exploration, outage screening and studies with uncertain inputs. A run with no fatal JSON errors has not necessarily completed its task correctly. Check whether the agent stayed within the allowed changes, studied every required case and described solver evidence correctly. This paper studies one prototype on a modeled grid. It is not a live-utility reliability study. Samim Konjicija, Slaven Peles; Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning; Figure 1, PDF page 2 Prototype architecture for modeled studies. Twelve reported searches are different backend/application settings, not twelve repeats of one task. Source locator: Figure 1, PDF page 2. Original URL: https://arxiv.org/abs/2609.04544v1
Takeaway: Explain what one run represents before reporting a success rate.
Nominal duration: 2 minutes.

Full sources:
Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>A lower cost can come from solving the wrong task</h1>
<div class="content"><div class="math-display" role="math">U<sub>dispatch</sub> ⊆ U<sub>expanded</sub><br>min<sub>u ∈ Uexpanded</sub> J(u) ≤ min<sub>u ∈ Udispatch</sub> J(u)</div><ul><li>R01 reports costs of 27,564 before and 17,398 after one model changed unit commitment: which units are on.</li><li>The task allowed only dispatch changes: how much power those units produce. The lower value breaks that task limit.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2609.04544v1">Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.</a></div>
<div class="takeaway">Judge the objective value together with the allowed decisions.</div>
<span class="pageno">62 / 80</span></div>

<!--
Use the paper's unspecified objective units; do not invent dollars per hour. The reported objective falls by about 36.9%, but the agent changes a type of decision outside the task. Unit commitment determines which units are on; dispatch sets their output. Other model setups keep to dispatch-only changes and report no improvement from the given base. A valid comparison checks what was changed, not just whether the objective fell.
Takeaway: Judge the objective value together with the allowed decisions.
Nominal duration: 2 minutes.

Full sources:
Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Successful tool calls can still miss a critical outage</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/rigor_r01_coverage.png" alt="Counts read from R01 Table III and section IV. Each outage label is a pair of bus numbers in this test grid." style="max-height:360px;height:auto"><figcaption>Counts read from R01 Table III and section IV. Each outage label is a pair of bus numbers in this test grid.</figcaption></figure></div><ul><li>All four model runs find the highest-cost outage. None finds a second outage with no feasible solution.</li><li>These are four different setups on one grid, not repeated trials that measure reliability.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2609.04544v1">Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.</a></div>
<span class="pageno">63 / 80</span></div>

<!--
All four searches identify the highest-cost outage, 187–189. Three identify infeasible outage 29–30, and none identifies infeasible outage 15–16. Infeasible means the specified study has no solution that meets its constraints. These results show gaps in case coverage. They do not give a stable failure probability for a model. Do not add binomial confidence intervals to these four different setups.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Samim Konjicija, Slaven Peles. Integrating Agentic Artificial Intelligence with High-Performance Computing for Grid Planning. arXiv; EnergyCon 2026 proceedings forthcoming as described by authors. 3 September 2026; v1.
Full source: https://arxiv.org/abs/2609.04544v1
Full paper: https://arxiv.org/pdf/2609.04544v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Show both trial counts and uncertainty</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/rigor_r02_capability.png" alt="R02 Table II. L1: place a 100 MW + 10 Mvar load. L2: check reactive-power needs for 100 MW + 50 Mvar generation." style="max-height:360px;height:auto"><figcaption>R02 Table II. L1: place a 100 MW + 10 Mvar load. L2: check reactive-power needs for 100 MW + 50 Mvar generation.</figcaption></figure></div><ul><li>R02 reports ten attempts per shown setup on synthetic 100- and 1,000-bus grids.</li><li>We calculated the Wilson 95% intervals. The paper reports the counts, not these intervals.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2607.28822v1">Eve Tsybina, Samim Konjicija, Slaven Peles. Agentic Artificial Intelligence for Power Systems: Strategies to Identify and Close Capability Gaps. arXiv. 30 July 2026; v1.</a></div>
<span class="pageno">64 / 80</span></div>

<!--
Six shown cells are 10/10 and two are 5/10. In the tested code version, higher-complexity tasks and larger grids have no reported numerical result cells. The authors discuss later fixes without giving a complete new set of counts. Missing results must not be plotted as zeroes. These are synthetic grids, not utility operating systems. Wilson intervals describe sampling uncertainty under independent pass/fail trials at fixed settings. That assumption is not established by the paper. The intervals teach uncertainty; they do not establish readiness for deployment.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Eve Tsybina, Samim Konjicija, Slaven Peles. Agentic Artificial Intelligence for Power Systems: Strategies to Identify and Close Capability Gaps. arXiv. 30 July 2026; v1.
Full source: https://arxiv.org/abs/2607.28822v1
Full paper: https://arxiv.org/pdf/2607.28822v1

National Institute of Standards and Technology, SEMATECH. 7.2.4.1. Confidence intervals. NIST/SEMATECH e-Handbook of Statistical Methods. Undated live handbook section; reviewed 17 October 2026.
Full source: https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>PowerBench finds answers across linked records</h1>
<div class="content source-focus"><figure><img src="/images/real_paper_powerbench_dataset.png" alt="Original PowerBench overview linking structured asset state, telemetry, rules, records and queries." style="max-height:420px;height:auto"><figcaption>Original PowerBench overview linking structured asset state, telemetry, rules, records and queries.</figcaption></figure><div><ul><li>Its 300 questions use synthetic asset records, documents and time-series data. Tools search, read and run Python.</li><li>Each attempt allows 50 tool calls and 300 seconds. The test does not run physical power-flow studies.</li></ul></div></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2609.34492v1">Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).</a></div>
<span class="pageno">65 / 80</span></div>

<!--
An answer can have the correct format but refer to the wrong asset or time period. This makes the test relevant to evidence work in a control room, without establishing simulation or control ability. The three task groups contain 60, 90 and 150 questions. The paper reports generated data for 761 devices and 24,939 documents. At review, the linked repository showed only README and LICENSE files. We did not verify a runnable public release. Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng; PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems; Figure 1, PDF page 4 Synthetic benchmark data, not utility operational records, simulation results or a live grid database. Source locator: Figure 1, PDF page 4. Original URL: https://arxiv.org/abs/2609.34492v1
Takeaway: Finding a useful record is one step. The complete answer still needs checking.
Nominal duration: 2 minutes.

Full sources:
Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).
Full source: https://arxiv.org/abs/2609.34492v1
Full paper: https://arxiv.org/pdf/2609.34492v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>PowerBench results: complete answers and partial credit</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/expanded_power_benchmark.png" alt="PowerBench Table 4: selected models and the authors&#x27; 95% bootstrap intervals. The two metrics average results differently." style="max-height:350px;height:auto"><figcaption>PowerBench Table 4: selected models and the authors&#x27; 95% bootstrap intervals. The two metrics average results differently.</figcaption></figure></div><ul><li>Joint accuracy needs every field and the right format. Field accuracy gives partial credit. Macro-JA gives each task group equal weight.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2609.34492v1">Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).</a></div>
<span class="pageno">66 / 80</span></div>

<!--
GPT-5.6-Sol is the leading row in this 2026 paper version. Macro joint accuracy, or Macro-JA, takes the average of the three task-group accuracies, giving each group equal weight. It is not the number of correct answers divided by 300. Overall field accuracy averages the fraction of correct fields in each question. Bootstrap intervals are made by resampling the data. Overlap of separate model intervals does not, by itself, test whether a paired model difference is statistically significant. These synthetic evidence questions do not test physical-grid safety.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).
Full source: https://arxiv.org/abs/2609.34492v1
Full paper: https://arxiv.org/pdf/2609.34492v1
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>A strong average can hide a weak task group</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_paper_powerbench_tasks.png" alt="Original PowerBench task examples. Each task group contributes equally to the reported average." style="max-height:270px;height:auto"><figcaption>Original PowerBench task examples. Each task group contributes equally to the reported average.</figcaption></figure></div><ul><li>The leading PowerBench row scores 85.0%, 88.9% and 48.7% joint accuracy in its three task groups.</li><li>Their equal-weight average is 74.2%. Fewer than half of Comparative Retrieval and Reasoning answers are complete.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2609.34492v1">Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).</a></div>
<span class="pageno">67 / 80</span></div>

<!--
The task groups contain 60, 90 and 150 questions. Equal weighting gives the smallest group as much influence as the largest. This is an intentional metric choice, not a calculation error. It answers a different question from counting all correct questions together. In a utility pilot, show results for each important task so weak performance cannot disappear inside the average. Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng; PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems; Figure 2, PDF page 6 Illustrates three task families; the metric gives them equal weight even though their sizes are60,90 and150 questions. Source locator: Figure 2, PDF page 6. Original URL: https://arxiv.org/abs/2609.34492v1
Takeaway: Choose the averaging rule carefully and show the tasks that matter to the operator.
Nominal duration: 2 minutes.

Full sources:
Xijing Wang, Yinsheng Yao, Jinru Ding, Yidong Jiang, Ziwen Xu, Yiwen Jiang, Jie Xu, Dawei Cheng. PowerBench: A Benchmark for Agentic Retrieval and Reasoning in Power Systems. arXiv. 2026-09-28 (v1).
Full source: https://arxiv.org/abs/2609.34492v1
Full paper: https://arxiv.org/pdf/2609.34492v1
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>What do ten successful trials tell us?</h1>
<div class="content"><p class="callout">Observed score ≠ known success probability</p><ul><li>For 10 passes in 10 trials, the calculated two-sided Wilson 95% interval is about 72.2%–100%.</li><li>For 5 passes in 10 trials, it is about 23.7%–76.3%. Repeating one easy case also leaves other tasks untested.</li></ul></div>
<div class="sources">Source: <a href="https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm">National Institute of Standards and Technology, SEMATECH. 7.2.4.1. Confidence intervals. NIST/SEMATECH e-Handbook of Statistical Methods. Undated live handbook section; reviewed 17 October 2026.</a></div>
<div class="takeaway">Report the trial count, tested tasks and interval method with a percentage.</div>
<span class="pageno">68 / 80</span></div>

<!--
An interval shows uncertainty under a statistical model. With repeated use on comparable samples, the Wilson method aims for 95% coverage of the fixed success probability. It does not assign a 95% probability to the fixed parameter lying in this one observed interval. These calculations use small hypothetical or reported counts and a binomial model for independent pass/fail trials. Different tasks, settings and linked errors add uncertainty beyond that model. Keep these two-sided Wilson intervals separate from the later exact one-sided bound on failures.
Takeaway: Report the trial count, tested tasks and interval method with a percentage.
Nominal duration: 2 minutes.

Full sources:
National Institute of Standards and Technology, SEMATECH. 7.2.4.1. Confidence intervals. NIST/SEMATECH e-Handbook of Statistical Methods. Undated live handbook section; reviewed 17 October 2026.
Full source: https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>More required steps can lower overall reliability</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/rigor_reliability_chain.png" alt="Illustrative calculation, not measured agent performance: P(all L steps succeed) = q^L." style="max-height:360px;height:auto"><figcaption>Illustrative calculation, not measured agent performance: P(all L steps succeed) = q^L.</figcaption></figure></div><ul><li>If each step independently succeeds 99% of the time, all 20 required steps succeed only 81.8% of the time.</li><li>Real errors can have a shared cause. Measure the whole task instead of assuming independent steps.</li></ul></div>
<span class="pageno">69 / 80</span></div>

<!--
The curves show why strong results for individual steps can still leave a lower chance of completing the whole task. Retrying may reuse the same wrong context, cache or tool adapter, so it may not be a fresh independent chance. The exact chain rule multiplies conditional probabilities. The plotted q^L assumes the same success probability for every step and independence between steps. It motivates whole-task measurement and code-enforced checks. It does not predict the performance of a real utility agent.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:

-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>The answer changes when we change what we count</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/rigor_eval_outcomes.png" alt="Invented example: 80 feasible and 20 infeasible cases. These counts explain metrics; they are not deployment results." style="max-height:360px;height:auto"><figcaption>Invented example: 80 feasible and 20 infeasible cases. These counts explain metrics; they are not deployment results.</figcaption></figure></div><ul><li>In this invented test, two of 20 infeasible cases are accepted: a 10% false-approval rate among infeasible cases.</li><li>Calling them only “2% of all 100 cases” hides that error rate in the harder group.</li></ul></div>
<span class="pageno">70 / 80</span></div>

<!--
Feasible means a case meets the stated constraints. Of 80 feasible cases, 70 are accepted and 10 rejected. Of 20 infeasible cases, two are wrongly accepted and 18 rejected. Among accepted cases, 70/72, or 97.2%, are feasible. Yet the false-approval rate among infeasible cases is 2/20, or 10%. Overall, 88/100 classifications are correct. Choose the error that matters before choosing a headline metric. Rejecting more cases may reduce false approvals but also make the assistant less useful. Measure both effects.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:

-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Zero test failures do not prove perfect performance</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/rigor_zero_failure_bound.png" alt="Calculated binomial bound. It needs a fixed failure definition, independent trials and stable test conditions." style="max-height:360px;height:auto"><figcaption>Calculated binomial bound. It needs a fixed failure definition, independent trials and stable test conditions.</figcaption></figure></div><ul><li>Zero failures in n independent, fixed-setting trials gives this exact one-sided 95% upper bound on failure probability: 1 − 0.05^(1/n).</li><li>At n=300, the bound is about 0.994%. It does not cover a different mix of tasks.</li></ul></div>
<div class="sources">Source: <a href="https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbino.htm">National Institute of Standards and Technology. EXACT BINOMIAL. NIST Dataplot Reference Manual. Last updated 16 November 2015; reviewed 17 October 2026.</a></div>
<span class="pageno">71 / 80</span></div>

<!--
Explain the calculation in words. If each trial has failure probability p, the chance of zero failures in n independent trials is (1-p)^n. Set that chance to 0.05 and solve for p. This gives the stated one-sided 95% upper confidence bound under the test assumptions. It is not certification. It does not establish performance after a topology, model or task change. The approximation 3/n gives a useful quick estimate.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
National Institute of Standards and Technology. EXACT BINOMIAL. NIST Dataplot Reference Manual. Last updated 16 November 2015; reviewed 17 October 2026.
Full source: https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbino.htm
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Choose tests that can reveal failures</h1>
<div class="content"><ul><li>Include simple and hard tasks, different grid sizes, old inputs, tool errors, and feasible and infeasible cases.</li><li>Check against an independent reference. Keep the final test cases separate from tuning cases.</li><li>For every trial, save the case ID, settings, input snapshot, tool evidence, final status and human corrections.</li></ul></div>
<div class="sources">Source: <a href="https://arxiv.org/abs/2606.20401v1">Qian Zhang, Andrea Pomarico, Costas Mylonas, Magda Foti, Alberto Berizzi, Le Xie. PowerAgentBench-Dyn: A Benchmark for Agentic AI in Power System Dynamic Studies. arXiv. 2026-06-18 (v1).</a></div>
<div class="takeaway">Show failures by stage and case type, along with the number tested.</div>
<span class="pageno">72 / 80</span></div>

<!--
Repeating one prompt is not a broad test of different tasks. Report shared networks, scenarios and other links between trials. An independent check should do more than ask the same model whether it is right. Do not use the final test cases to tune prompts or tool adapters. This is a proposed testing method, not a certification process.
Takeaway: Show failures by stage and case type, along with the number tested.
Nominal duration: 2 minutes.

Full sources:
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
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>MCP connects a workflow to its tools</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/real_framework_mcp_architecture.png" alt="Original MCP architecture. Clients connect to servers; the engineering tool performs the calculation." style="max-height:310px;height:auto"><figcaption>Original MCP architecture. Clients connect to servers; the engineering tool performs the calculation.</figcaption></figure></div><ul><li>The application hosts MCP clients. Each client connects to a server that exposes tools.</li><li>The server returns a result. The application still checks permissions, versions and engineering meaning.</li></ul></div>
<div class="sources">Source: <a href="https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture">Model Context Protocol. MCP Architecture overview. 2026-07-28 documentation revision.</a></div>
<span class="pageno">73 / 80</span></div>

<!--
MCP, the Model Context Protocol, standardizes how applications connect to tools. It is not a planner or a power-flow model. Tool descriptions should clearly state the job and its inputs. The application still needs to check identity, permissions and whether a call makes engineering sense. MCP servers in X-GridAgent do not establish which orchestration SDK it uses. Source: Model Context Protocol, official documentation revision July 28, 2026. Screenshot captured October 18, 2026. A protocol architecture does not prove numerical correctness or that a utility uses this implementation. Source figure locator: Core concepts: Participants diagram. Original source URL: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Yihan (Logon) Wen, Xin Chen. X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis. arXiv preprint. 2025-12-23 (v1).
Full source: https://arxiv.org/pdf/2512.20789v1

LangChain documentation maintainers. LangGraph Graph API overview. Official LangChain documentation. Accessed 2026-10-17; live documentation.
Full source: https://docs.langchain.com/oss/python/langgraph/graph-api

Model Context Protocol. MCP Architecture overview. 2026-07-28 documentation revision.
Full source: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture

Model Context Protocol. MCP Security Best Practices. 2026-07-28 documentation revision.
Full source: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A retrieved document cannot give itself permission</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/trust_boundary.svg" alt="Invented prompt-injection example: document text tries to act as an instruction. The blocked path marks the authority limit." style="height:330px;max-height:330px"><figcaption>Invented prompt-injection example: document text tries to act as an instruction. The blocked path marks the authority limit.</figcaption></figure><ul><li>Treat instructions inside a retrieved document as data, not permission.</li><li>The application checks who may act and which actions are allowed.</li></ul></div>
<div class="sources">Source: <a href="https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices">Model Context Protocol. MCP Security Best Practices. 2026-07-28 documentation revision.</a></div>
<span class="pageno">74 / 80</span></div>

<!--
The hostile instruction is invented for teaching. A retrieved document is evidence, not an instruction source with authority over the task. A separate service check must enforce allowed actions, regardless of what a document says. Test whether hostile text changes the case scope, triggers a forbidden call or puts false instructions into a report. Save the rejected action and the reason it was rejected.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Model Context Protocol. MCP Security Best Practices. 2026-07-28 documentation revision.
Full source: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>Measure the whole job, including human review</h1>
<div class="content"><div class="with-photo"><div><ul><li>Measure total task time, reviewer corrections and false approvals. Include failed and escalated attempts.</li><li>A faster draft may need more review. Show the spread of times and the hard cases, not just an average.</li></ul></div><figure><img src="/images/real_ops_frequency.png" alt="Real CAISO oscillation-monitoring screens. The operator must still interpret the result and decide what to do." style="max-height:270px;height:auto"><figcaption>Real CAISO oscillation-monitoring screens. The operator must still interpret the result and decide what to do.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.pnnl.gov/sites/default/files/media/file/PNNL_workshop_Presentation_Human_Factors_Virtual_Workshop_March_2023.pdf">Corey Fallon, Brett Jefferson, Tyler Ryan. An Analysis of Grid Operators. Pacific Northwest National Laboratory. 2023-04-19.</a></div>
<div class="takeaway">Measure the operator&#x27;s completed job, including the work needed to check and correct it.</div>
<span class="pageno">75 / 80</span></div>

<!--
The equation is a proposed way to split time for a task whose stages run in sequence. If stages run in parallel, measure the path that determines completion time instead of adding every stage. Include operator attention and time spent recovering from errors. Audit turnaround, batch throughput and time saved in review are different measures. Choose useful timing percentiles and workload measures for the actual job. This original conventional monitoring screenshot illustrates the human interpretation stage. It is not evidence that an agent was used or that the tutorial’s time metric was measured at CAISO. Teaching timing identity: total task time = data preparation + agent execution + human review + rework.
Takeaway: Measure the operator's completed job, including the work needed to check and correct it.
Nominal duration: 2 minutes.

Full sources:
Corey Fallon, Brett Jefferson, Tyler Ryan. An Analysis of Grid Operators. Pacific Northwest National Laboratory. 2023-04-19.
Full source: https://www.pnnl.gov/sites/default/files/media/file/PNNL_workshop_Presentation_Human_Factors_Virtual_Workshop_March_2023.pdf

Google Cloud. AES: Scaling energy safety audits with Claude on Google Cloud. Undated; reviewed 17 October 2026.
Full source: https://cloud.google.com/customers/aes

Amazon Web Services. TC Energy increases office productivity with automation on Amazon Bedrock. Undated; reviewed 17 October 2026.
Full source: https://aws.amazon.com/solutions/case-studies/tcenergy-bedrock/

John Phipps. Control center modernization is enhancing reliability. California ISO. 2025-09-10.
Full source: https://www.caiso.com/about/news/energy-matters-blog/control-center-modernization-is-enhancing-reliability
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>Test whether the assistant helps on comparable tasks</h1>
<div class="content"><div class="with-photo"><div><ul><li>Start in shadow mode: save the proposed answers while the normal operating decision stays in place.</li><li>Compare similar tasks with and without help. Account for task difficulty, learning and practice effects.</li><li>Set stopping rules, error types, review duties and the evidence needed before expanding the pilot.</li></ul></div><figure><img src="/images/real_ops_training.png" alt="California ISO’s operator-training facility. Photo: California ISO, 2025." style="max-height:360px;height:auto"><figcaption>California ISO’s operator-training facility. Photo: California ISO, 2025.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.caiso.com/about/news/energy-matters-blog/iso-now-has-expanded-training-and-emergency-operations-facilities">Tricia Johnstone, Director, Operational Readiness. ISO now has expanded training and emergency operations facilities. California ISO. 2025-02-20.</a></div>
<div class="takeaway">Build the assistant, then separately test the claim that it helps.</div>
<span class="pageno">76 / 80</span></div>

<!--
This is a proposed pilot design, not a standard approval process. When practical, randomize task order or balance which condition is tried first to reduce order effects. After tuning, keep a fixed final test set. Record disagreements with independent checks. A pilot only supports conclusions about the tasks, tools, settings and users that it actually tested. The real training-facility photograph provides context for the proposed evaluation. The slide’s matched-task comparison is a tutorial recommendation, not a reported CAISO agent trial.
Takeaway: Build the assistant, then separately test the claim that it helps.
Nominal duration: 2 minutes.

Full sources:
Tricia Johnstone, Director, Operational Readiness. ISO now has expanded training and emergency operations facilities. California ISO. 2025-02-20.
Full source: https://www.caiso.com/about/news/energy-matters-blog/iso-now-has-expanded-training-and-emergency-operations-facilities
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>Power-sector testbeds provide places to evaluate agents</h1>
<div class="content"><div class="with-photo"><div><ul><li>DOE CESER&#x27;s July 2026 announcement describes LLNL&#x27;s Stormbreaker testbed for evaluation.</li><li>EPRI&#x27;s SAFERai.power develops assessment and risk guidance. Neither certifies this prototype.</li></ul></div><figure><img src="/images/ornl_goal.jpg" alt="ORNL GOAL research laboratory, shown for context. This is not a photograph of LLNL&#x27;s testbed." style="max-height:360px;height:auto"><figcaption>ORNL GOAL research laboratory, shown for context. This is not a photograph of LLNL&#x27;s testbed.</figcaption></figure></div></div>
<div class="sources">Source: <a href="https://www.energy.gov/ceser/articles/ceser-releases-new-testbed-advance-llm-and-agentic-ai-evaluation-critical">U.S. Department of Energy. CESER Releases New Testbed to Advance LLM and Agentic AI Evaluation for Critical Infrastructure. 2026-07-16.</a></div>
<span class="pageno">77 / 80</span></div>

<!--
A testbed is a controlled environment for testing a system. It can make tool failures, state changes and engineering effects easier to observe. It still needs to represent the task being tested. Keep DOE, LLNL, ORNL and EPRI roles clear. The existence of a testbed or guidance program does not prove that a particular agent performs well.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
U.S. Department of Energy. CESER Releases New Testbed to Advance LLM and Agentic AI Evaluation for Critical Infrastructure. 2026-07-16.
Full source: https://www.energy.gov/ceser/articles/ceser-releases-new-testbed-advance-llm-and-agentic-ai-evaluation-critical

EPRI via GlobeNewswire. EPRI Launches Effort to Reduce Risk in AI Power Sector Deployment. 2026-08-06.
Full source: https://www.globenewswire.com/news-release/2026/08/06/3340219/0/en/epri-launches-effort-to-reduce-risk-in-ai-power-sector-deployment.html

EPRI. SAFERai.power. Undated; reviewed 17 October 2026.
Full source: https://msites.epri.com/saferai

Oak Ridge National Laboratory, U.S. Department of Energy. Oak Ridge National Laboratory, U.S. Department of Energy: Researchers at ORNL GOAL facing a large display of U.S. grid and geographic data. Image accessed 17 October 2026.
Full source: https://www.ornl.gov/grid-operations-and-analytics-laboratory-goal/
-->

---
transition: none
---

<div class="lesson teaching rigorous photo-slide">

<h1>GridGuard: what should this prototype prove?</h1>
<div class="content"><div class="with-photo"><div><ul><li>The prototype tests proposed actions in OpenDSS on a synthetic feeder.</li><li>Test whether it improves completed tasks while respecting fixed limits.</li><li>Save each proposal, input snapshot, solver result, rejected option and reviewer decision.</li></ul></div><figure><img src="/images/gridguard_research_feeder.png" alt="Existing workshop figure: synthetic SMART-DS Greensboro feeder udt 8894. This is not a live utility circuit." style="max-height:360px;height:auto"><figcaption>Existing workshop figure: synthetic SMART-DS Greensboro feeder udt 8894. This is not a live utility circuit.</figcaption></figure></div></div>
<div class="sources">Source: <a href="/research/GridGuard_source_snapshot.txt">GridGuard project / local source snapshot. GridGuard current project: README and graph source snapshot. 2026.</a></div>
<div class="takeaway">Useful proposals have assumptions and evidence that an operator can inspect.</div>
<span class="pageno">78 / 80</span></div>

<!--
The prototype cannot issue live DMS commands. Test measurable outcomes: correct feasible proposals, false approvals, engineering-limit violations, time and reviewer corrections. Keep failed attempts and actions outside the allowed scope in the record. Plausible-sounding actions alone are not evidence of benefit. This prepares the next tutorial, where the three numerical case studies are worked through.
Takeaway: Useful proposals have assumptions and evidence that an operator can inspect.
Nominal duration: 2 minutes.

Full sources:
GridGuard project / local source snapshot. GridGuard current project: README and graph source snapshot. 2026.
Full source: ../research/GridGuard_source_snapshot.txt

Local workshop source snapshot. Existing three-use-case GridGuard workshop: instructor route and synthetic-feeder context. Snapshot 17 October 2026.
Full source: ../research/Follow_on_workshop_source.txt
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Next tutorial: check the proposed action</h1>
<div class="content"><ul><li>Voltage support: does the proposed action meet the intended model&#x27;s limits?</li><li>Restoration: have we checked topology, switching limits and the load restored?</li><li>Cyber response: did uncertain or hostile data change permissions or corrupt the evidence?</li></ul></div>
<div class="sources">Source: <a href="/research/Follow_on_workshop_source.txt">Local workshop source snapshot. Existing three-use-case GridGuard workshop: instructor route and synthetic-feeder context. Snapshot 17 October 2026.</a></div>
<span class="pageno">79 / 80</span></div>

<!--
Take three questions into the detailed workshop: Are the data valid? Is the engineering result valid? Is the decision justified? For each performance claim, ask what was tested, how many cases there were and which case was rejected. The next tutorial contains the exact experiments and results.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Local workshop source snapshot. Existing three-use-case GridGuard workshop: instructor route and synthetic-feeder context. Snapshot 17 October 2026.
Full source: ../research/Follow_on_workshop_source.txt
-->

---
transition: none
---

<div class="lesson teaching rigorous closing-slide closing">

<h1>Discussion and full sources</h1>
<div class="content"><ul><li>Which power-system paper studies a task and tool sequence closest to your own?</li><li>How will operators see unresolved cases, changed inputs and limits on allowed actions?</li><li>The reading guide links the papers, deployment sources, documentation and editable chart data.</li></ul></div>
<p class="reading-link"><a href="/Full_Reading_Guide.html">Open the Full Reading Guide</a></p>
<div class="takeaway">A credible claim states the task, number tested, assumptions, failures and remaining human work.</div>
<span class="pageno">80 / 80</span></div>

<!--
All slides belong to one integrated session. Return to the opening real-world examples and separate evidence that a company uses a system from evidence that it performs an engineering task well. The next tutorial applies these checks to voltage support, restoration and cyber response. Full sources are in the reading guide. Answers to both exercises are in the instructor guide.
Takeaway: A credible claim states the task, number tested, assumptions, failures and remaining human work.
Nominal duration: 2 minutes.

Full sources:

-->
