---
theme: default
title: "Agentic AI: Three Operator Cases"
info: Understand three operator problems, agent choices, numerical evidence and human review through prepared examples
author: Alaa Selim (MIT/Dartmouth) and Mohamed Chehada (UT Austin)
transition: none
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
fonts:
  sans: Latin Modern Roman
  serif: Latin Modern Roman
  mono: Latin Modern Mono
  provider: none
mdc: false
drawings:
  persist: false
download: false
---

<div class="lesson teaching rigorous cover-slide cover">

<h1>Agentic AI:<br>Three Operator Cases</h1>
<p>Understand the problem, follow the agent and review the evidence.</p>
<p>90 minutes / three what-if discussions</p>
<div class="presenters"><div><strong>Alaa Selim</strong><span>MIT/Dartmouth</span></div><div><strong>Mohamed Chehada</strong><span>UT Austin</span></div></div>
<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup"><small>Independent educational material · IEEE ComSoc theme adaptation</small>
<span class="pageno">1 / 50</span></div>

<!--
**Say**

Understand the problem, follow the agent and review the evidence. 90 minutes / three what-if discussions The examples are self-contained. No computer or software setup is needed. We will follow a goal, the agent’s requests, numerical evidence and a human decision. The results come from reduced or synthetic studies; they are examples for learning.

**Show**

Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>An agent chooses what to try next</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_agent_loop.svg" alt="Teaching diagram: the model requests a tool and uses the returned evidence." style="height:310px;max-height:310px"><figcaption>Teaching diagram: the model requests a tool and uses the returned evidence.</figcaption></figure><ul><li>Give the agent a goal. It requests a tool, reads the result and chooses the next step.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.</a></div>
<span class="pageno">2 / 50</span></div>

<!--
**Say**

Give the agent a goal. It requests a tool, reads the result and chooses the next step. The agent does not calculate the electrical result by writing a confident answer. It chooses a permitted tool, reads the result and decides whether another request or human review is needed. Trace the feedback arrow once with the audience.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>The agent asks; the tool calculates</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_agentic_capabilities.png" alt="Original Stanford figure: one function call and a multi-step workflow." style="max-height:330px;height:auto"><figcaption>Original Stanford figure: one function call and a multi-step workflow.</figcaption></figure></div><ul><li>A tool does one job. An agent can connect several jobs using their results.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.</a></div>
<span class="pageno">3 / 50</span></div>

<!--
**Say**

A tool does one job. An agent can connect several jobs using their results. The Stanford figure distinguishes one function call from a longer agentic workflow. A function can perform one calculation. An agentic workflow connects requests and uses returned results to decide what comes next.

**Show**

Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Solar settings: which option should we try?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_voltage.svg" alt="The tool calculates; the agent coordinates the next request." style="height:340px;max-height:340px"><figcaption>The tool calculates; the agent coordinates the next request.</figcaption></figure><ul><li>Compare possible settings, then check voltage and line current.</li><li>The agent can organize these trials and report the checked options.</li></ul></div>
<span class="pageno">4 / 50</span></div>

<!--
**Say**

Compare possible settings, then check voltage and line current. The agent can organize these trials and report the checked options. Suppose an operator needs new solar settings. Different settings affect voltage, current and useful solar output. The agent organizes a bounded study; the numerical tool supplies the engineering evidence.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.
Full source: https://aclanthology.org/2023.findings-emnlp.157/
Full paper: https://aclanthology.org/2023.findings-emnlp.157.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Give the agent a goal and clear limits</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_rules.svg" alt="Grid teaching adaptation of Stanford’s task-specification concept." style="height:310px;max-height:310px"><figcaption>Grid teaching adaptation of Stanford’s task-specification concept.</figcaption></figure><ul><li>State the goal, allowed tools and stopping rules.</li><li>Keep the operator’s review step explicit.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40.</a></div>
<span class="pageno">5 / 50</span></div>

<!--
**Say**

State the goal, allowed tools and stopping rules. Keep the operator’s review step explicit. A useful request states the operating goal, available tools and stopping conditions. The agent needs to know when it must ask for review rather than continue trying options. The operator defines these boundaries.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.
Full source: https://aclanthology.org/2025.acl-long.1323/
Full paper: https://aclanthology.org/2025.acl-long.1323.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Restoration: who should get power first?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_restoration.svg" alt="Same network and limits, different service goals." style="height:340px;max-height:340px"><figcaption>Same network and limits, different service goals.</figcaption></figure><ul><li>The operator sets the service priority.</li><li>That priority changes the study the agent requests.</li></ul></div>
<span class="pageno">6 / 50</span></div>

<!--
**Say**

The operator sets the service priority. That priority changes the study the agent requests. When supply is limited, restoring the greatest total power can differ from protecting essential services. The operator chooses that priority. The agent must preserve it when requesting and comparing studies.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.
Full source: https://aclanthology.org/2025.acl-long.1323/
Full paper: https://aclanthology.org/2025.acl-long.1323.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Keep three jobs clear</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_three_jobs.svg" alt="Adapted principle: language, calculation and human review have different jobs." style="height:310px;max-height:310px"><figcaption>Adapted principle: language, calculation and human review have different jobs.</figcaption></figure><ul><li>The agent requests a study. The tool calculates. The operator reviews the result.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53.</a></div>
<span class="pageno">7 / 50</span></div>

<!--
**Say**

The agent requests a study. The tool calculates. The operator reviews the result. Keep the jobs separate. The agent coordinates requests. The numerical tool calculates. The operator reviews the evidence and decides the next authorized step. A tool passing its checks is not operating permission.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Wrong readings can still fit a model</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_cyber.svg" alt="Model fit and trusted information answer different questions." style="height:340px;max-height:340px"><figcaption>Model fit and trusted information answer different questions.</figcaption></figure><ul><li>A good fit alone does not prove that the readings are true.</li><li>The agent can organize checks and flag missing evidence.</li></ul></div>
<span class="pageno">8 / 50</span></div>

<!--
**Say**

A good fit alone does not prove that the readings are true. The agent can organize checks and flag missing evidence. Readings may fit a model and still be wrong. An alarm test measures one kind of mismatch. The agent can request additional checks and identify missing information, but its explanation cannot make a data source trustworthy.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Case 1: which solar settings should we use?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_voltage_problem.svg" alt="Concept sketch: choose settings, then calculate their effects." style="height:310px;max-height:310px"><figcaption>Concept sketch: choose settings, then calculate their effects.</figcaption></figure><ul><li>Use solar generation while keeping voltage and line current within the allowed range.</li><li>An agent can organize the trials and return checked options.</li></ul></div>
<span class="pageno">9 / 50</span></div>

<!--
**Say**

Choose settings that keep voltage and line current within the allowed range. An agent can organize the trials and return checked options. Start with the physical problem: choose solar controls that respect voltage, current and equipment capacity while serving the stated generation goal. The agent can organize trials and return a checked option. It does not replace the solver or the operator.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2.0 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.
Full source: https://data.openei.org/submissions/2981
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Two tools suggest different settings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_two_proposals.svg" alt="MPC: model predictive control. SAC: soft actor-critic. Both proposals need the same checks." style="height:310px;max-height:310px"><figcaption>MPC: model predictive control. SAC: soft actor-critic. Both proposals need the same checks.</figcaption></figure><ul><li>MPC plans with a model. SAC uses a previously trained controller.</li><li>Treat both outputs as proposals that need the same electrical checks.</li></ul></div>
<span class="pageno">10 / 50</span></div>

<!--
**Say**

MPC plans with a model. SAC uses a previously trained controller. Treat both outputs as proposals that need the same electrical checks. MPC means model predictive control: it plans with a model. SAC means soft actor-critic: it uses a previously trained policy. Both produce proposals. Apply the same electrical checks to each before comparing cost or usefulness.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.
Full source: https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.
Full source: https://proceedings.mlr.press/v80/haarnoja18b.html

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>How the agent helps with solar settings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_voltage_agent.svg" alt="The agent uses returned checks to choose the next permitted step." style="height:310px;max-height:310px"><figcaption>The agent uses returned checks to choose the next permitted step.</figcaption></figure><ul><li>The agent requests a study and reads the returned checks.</li><li>It can try another allowed option or ask the operator for help.</li></ul></div>
<span class="pageno">11 / 50</span></div>

<!--
**Say**

The agent requests a study and reads the returned checks. It can try another allowed option or ask the operator for help. Read the loop from left to right. The operator supplies a goal. The agent requests an allowed trial. The tool calculates voltage and current. The checks decide whether it can be compared. A failed trial can lead to another permitted request or a request for help.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 3.0 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Two solar settings change the result</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_solar_controls.svg" alt="Active power and voltage support share equipment capacity." style="height:310px;max-height:310px"><figcaption>Active power and voltage support share equipment capacity.</figcaption></figure><ul><li>One setting controls solar power output. The other provides voltage support.</li><li>The tool checks voltage, line current and the solar unit’s capacity.</li></ul></div>
<span class="pageno">12 / 50</span></div>

<!--
**Say**

One setting controls solar power output. The other provides voltage support. The tool checks voltage, line current and the solar unit’s capacity. The two controls are active-power output and voltage support. The source model represents them as a and b. They share inverter capacity, so reducing one effect can change another. Use the tool to calculate those effects rather than infer safety from the control names.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Both proposals face the same checks</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_solar_checks.svg" alt="Both proposals need the same voltage, current and capacity checks." style="height:330px;max-height:330px"><figcaption>Both proposals need the same voltage, current and capacity checks.</figcaption></figure><ul><li>The tool calculates the effect of each proposal.</li><li>Compare their scores only after voltage, current and capacity checks pass.</li></ul></div>
<span class="pageno">13 / 50</span></div>

<!--
**Say**

The tool calculates the effect of each proposal. Compare their scores only after voltage, current and capacity checks pass. The same checks apply to both candidates. Check voltage, line current and inverter capacity first. Only a passing proposal is eligible for cost comparison. The agent’s next request should be based on the returned checks.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.
Full source: https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.
Full source: https://proceedings.mlr.press/v80/haarnoja18b.html
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Read the voltage and current checks</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_plot.png" alt="Calculated example at the original current allowance." style="max-height:345px;height:auto"><figcaption>Calculated example at the original current allowance.</figcaption></figure></div><ul><li>Left: voltages should stay in the allowed band.</li><li>Right: current should stay below 100% of the allowance.</li></ul></div>
<span class="pageno">14 / 50</span></div>

<!--
**Say**

Left: voltages should stay in the allowed band. Right: current should stay below 100% of the allowance. The left plot shows the voltage distribution. The right compares current use with the allowed current. Both pass this model’s checks. The curves on the left are sorted separately, so their horizontal rank is not a matched physical location.

**Show**

Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Both pass, but the trade-off is different</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_solar_result.svg" alt="Calculated example: both electrical checks pass." style="height:330px;max-height:330px"><figcaption>Calculated example: both electrical checks pass.</figcaption></figure><ul><li>MPC uses 73.62% of the current allowance; SAC uses 51.68%.</li><li>MPC has the lower overall score because current is only one part of the goal.</li></ul></div>
<span class="pageno">15 / 50</span></div>

<!--
**Say**

MPC uses 73.62% of the current allowance; SAC uses 51.68%. MPC has the lower overall score because current is only one part of the goal. The current-use values are 73.62% for MPC and 51.68% for saved SAC. Their scores are approximately 0.03110 and 0.43643. Lower score is preferred after all checks pass. SAC uses less current here partly because it also uses less active power.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide has-diagram">

<h1>What if we allow less current?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_current_change.svg" alt="Discuss the scenario, then advance to the calculated result." style="height:330px;max-height:330px;width:86%;margin:0 auto"><figcaption>Discuss the scenario, then advance to the calculated result.</figcaption></figure><ul><li>Reduce the allowance from 80% to 75% of nominal current.</li><li>Which proposal might fail? Which would you choose if both pass?</li><li>What must the agent ask the tool to check again?</li></ul></div>
<span class="pageno">16 / 50</span></div>

<!--
**Say**

Reduce the allowance from 80% to 75% of nominal current. Which proposal might fail? Which would you choose if both pass? What must the agent ask the tool to check again? Ask people to predict without doing any calculation. Make the rule change explicit: allowed current decreases from 80% to 75% of nominal. Give pairs time to explain what must be checked again and why the lowest current is not automatically the best proposal. Advance only after the discussion.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: DISCUSS**

Invite a prediction and one reason. Advance only after the discussion.

**Ask**

Reduce the allowance from 80% to 75% of nominal current. Which proposal might fail? Which would you choose if both pass? What must the agent ask the tool to check again?

**Answer**

MPC has the lower score. SAC uses less current and less solar output. These results cover the medium-voltage model. A wider grid needs a wider study.
Nominal duration: 6 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Both proposals pass the new current check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/exercise_voltage_solution.svg" alt="Same load; the allowed current has been reduced to 75% of nominal." style="height:310px;max-height:310px"><figcaption>Same load; the allowed current has been reduced to 75% of nominal.</figcaption></figure><ul><li>MPC has the lower score. SAC uses less current and less solar output.</li><li>These results cover the medium-voltage model. A wider grid needs a wider study.</li></ul></div>
<span class="pageno">17 / 50</span></div>

<!--
**Say**

MPC has the lower score. SAC uses less current and less solar output. These results cover the medium-voltage model. A wider grid needs a wider study. The numerical study has already been calculated for this changed allowance. MPC uses about 78.53% of the new allowance and SAC about 54.85%; both pass. Their scores are about 0.03110 and 0.43246. MPC has the lower score. These checks cover the medium-voltage model, not the entire distribution system.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: REVEAL**

Use the prepared result to explain the answer and its limits.
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Less current does not mean the best option</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_voltage_tradeoff.svg" alt="Active-power settings use inverter rating as their base." style="height:310px;max-height:310px"><figcaption>Active-power settings use inverter rating as their base.</figcaption></figure><ul><li>Here SAC also uses less solar output.</li><li>The operator’s goal values solar generation as well as operating limits.</li></ul></div>
<span class="pageno">18 / 50</span></div>

<!--
**Say**

Here SAC also uses less solar output. The operator’s goal values solar generation as well as operating limits. In the changed-allowance example, the active-power setting is about 96% of inverter rating for MPC and 34% for SAC. These percentages use inverter rating as the base. Less current comes with a generation trade-off, so the operator’s objective matters.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A PASS covers only the checked model</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_scope.svg" alt="A passing result applies to the model and conditions actually checked." style="height:330px;max-height:330px"><figcaption>A passing result applies to the model and conditions actually checked.</figcaption></figure><ul><li>A study of the medium-voltage network cannot confirm a whole-grid claim.</li><li>The agent should request the missing study or return HOLD.</li></ul></div>
<span class="pageno">19 / 50</span></div>

<!--
**Say**

A study of the medium-voltage network cannot confirm a whole-grid claim. The agent should request the missing study or return HOLD. The model’s scope travels with its result. A passing medium-voltage study does not establish low-voltage or whole-feeder safety. When the request is wider than the evidence, the useful response is a missing-study request or HOLD.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: the first option fails</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_1.png" alt="Recorded full-feeder study; different inputs from the earlier comparison." style="max-height:380px;height:auto"><figcaption>Recorded full-feeder study; different inputs from the earlier comparison.</figcaption></figure></div><ul><li>Llama requests a check of the saved SAC proposal.</li><li>The numerical tool reports too much current and rejects it.</li></ul></div>
<span class="pageno">20 / 50</span></div>

<!--
**Say**

Llama requests a check of the saved SAC proposal. The numerical tool reports too much current and rejects it. This is a separate recorded full-feeder study, with different inputs from the earlier numerical comparison. Read the actual Llama request and returned tool result. The SAC trial reaches about 111.97% of allowed current, so it fails. The tool result determines eligibility.

**Show**

Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: another option is checked</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_2.png" alt="Recorded full-feeder study: the requested fallback passes the checks." style="max-height:380px;height:auto"><figcaption>Recorded full-feeder study: the requested fallback passes the checks.</figcaption></figure></div><ul><li>Llama requests a check of the existing MPC fallback.</li><li>The returned electrical checks pass for this recorded case.</li></ul></div>
<span class="pageno">21 / 50</span></div>

<!--
**Say**

Llama requests a check of the existing MPC fallback. The returned electrical checks pass for this recorded case. The agent requests a check of an existing MPC fallback. It does not invent or solve MPC. The historical electrical check returns about 99.60% of allowed current and no listed violations. That makes the option eligible for review within this study’s stated scope.

**Show**

Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: the operator receives a proposal</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_3.png" alt="Recorded workflow result; human review remains pending." style="max-height:380px;height:auto"><figcaption>Recorded workflow result; human review remains pending.</figcaption></figure></div><ul><li>The agent returns the checked proposal and its conditions.</li><li>The operator still reviews it before any authorized action.</li></ul></div>
<span class="pageno">22 / 50</span></div>

<!--
**Say**

The agent returns the checked proposal and its conditions. The operator still reviews it before any authorized action. The recorded workflow returns the checked proposal, while human acknowledgement remains pending and no equipment command is sent. Ask what evidence the operator receives and what remains outside the study, including permissions and protection checks.

**Show**

Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Case 2: who gets power after a fault?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_restoration_problem.svg" alt="Six-node example. Cyan marks critical loads; dashed links are backup paths." style="height:310px;max-height:310px"><figcaption>Six-node example. Cyan marks critical loads; dashed links are backup paths.</figcaption></figure><ul><li>A fault removes a supply path. Available capacity limits what can be restored.</li><li>The operator sets priorities; the agent can request and check restoration options.</li></ul></div>
<span class="pageno">23 / 50</span></div>

<!--
**Say**

A fault removes a supply path. Available capacity limits what can be restored. The operator sets priorities; the agent can request and check restoration options. A fault removes one supply path in the six-node network. The available backup capacity limits which loads can be restored. Cyan marks the critical loads. The operator defines priorities, while the agent can request alternative restoration studies.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2.0 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>How the agent helps restore service</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_restoration_agent.svg" alt="The operator sets the priority. The agent requests the matching study." style="height:310px;max-height:310px"><figcaption>The operator sets the priority. The agent requests the matching study.</figcaption></figure><ul><li>Choose the goal: critical loads first, or the most total power.</li><li>The agent can request a study, read the trade-off and ask for a new study when limits change.</li></ul></div>
<span class="pageno">24 / 50</span></div>

<!--
**Say**

Choose the goal: critical loads first, or the most total power. The agent can request a study, read the trade-off and ask for a new study when limits change. The goal changes the requested optimization. The agent should keep the operator’s priority, ask the tool for a plan, read service and capacity checks, and request a new study when inputs change. The solver decides which whole loads fit the network constraints.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>The service goal changes the study request</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_service_request.svg" alt="Two possible operator goals for the same fault and available network." style="height:330px;max-height:330px"><figcaption>Two possible operator goals for the same fault and available network.</figcaption></figure><ul><li>Critical-first gives more weight to essential service.</li><li>Most-total-power aims to restore the largest amount of power.</li></ul></div>
<span class="pageno">25 / 50</span></div>

<!--
**Say**

Critical-first gives more weight to essential service. Most-total-power aims to restore the largest amount of power. Critical-first assigns more value to essential service. Most-total-power maximizes total restored kW. Both still need the same network constraints. The agent translates the selected goal into the appropriate permitted study request; the solver performs the optimization.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>The goal changes who receives power</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_plot.png" alt="Calculated restoration results for the same network and limits." style="max-height:345px;height:auto"><figcaption>Calculated restoration results for the same network and limits.</figcaption></figure></div><ul><li>Critical-first: 130 kW total, including 90 kW for critical loads.</li><li>Most-total-power: 140 kW total, including 30 kW for critical loads.</li></ul></div>
<span class="pageno">26 / 50</span></div>

<!--
**Say**

Critical-first: 130 kW total, including 90 kW for critical loads. Most-total-power: 140 kW total, including 30 kW for critical loads. At a 40 kW backup tie, the critical-first result restores 130 kW total, including 90 kW critical. The total-power result restores 140 kW, including only 30 kW critical. Neither objective removes the need to explain the service trade-off. In the plots, overlapping markers indicate equal outcomes.

**Show**

Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Check the restoration plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_restoration_checks.svg" alt="Active-power model checks. Voltage, protection and field switching require separate work." style="height:310px;max-height:310px"><figcaption>Active-power model checks. Voltage, protection and field switching require separate work.</figcaption></figure><ul><li>Keep the faulted branch out of service. Check supply paths and capacity.</li><li>Voltage, protection and field switching need separate studies.</li></ul></div>
<span class="pageno">27 / 50</span></div>

<!--
**Say**

Keep the faulted branch out of service. Check supply paths and capacity. Voltage, protection and field switching need separate studies. Check that the fault stays isolated, supply paths connect and capacities are respected. This teaching exercise uses an active-power service model. AC voltages, protection coordination and the order of physical switching require separate studies and procedures.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.
Full source: https://arxiv.org/abs/1912.05185v3
Full paper: https://arxiv.org/pdf/1912.05185v3

Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.
Full source: https://doi.org/10.1109/TPWRS.2017.2720122
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide has-diagram">

<h1>What if the backup path can carry more power?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_capacity_change.svg" alt="Discuss the scenario, then advance to the calculated result." style="height:330px;max-height:330px;width:86%;margin:0 auto"><figcaption>Discuss the scenario, then advance to the calculated result.</figcaption></figure><ul><li>Increase its capacity from 40 kW to 180 kW. Keep the fault and loads the same.</li><li>Would the two service goals still give different results?</li><li>What should the agent recalculate before reporting the new plan?</li></ul></div>
<span class="pageno">28 / 50</span></div>

<!--
**Say**

Increase its capacity from 40 kW to 180 kW. Keep the fault and loads the same. Would the two service goals still give different results? What should the agent recalculate before reporting the new plan? Change only backup capacity in the scenario, from 40 to 180 kW. Ask whether the two service goals must always disagree. Invite participants to explain what the agent should recalculate before presenting a new plan. No software is needed to make the prediction.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: DISCUSS**

Invite a prediction and one reason. Advance only after the discussion.

**Ask**

Increase its capacity from 40 kW to 180 kW. Keep the fault and loads the same. Would the two service goals still give different results? What should the agent recalculate before reporting the new plan?

**Answer**

At 40 kW, critical-first serves 90 kW of critical load instead of 30 kW. At 180 kW, both goals serve 250 kW total, including all 90 kW of critical load.
Nominal duration: 6 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>More capacity removes this service trade-off</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/exercise_restoration_solution.svg" alt="Calculated results with the same fault, loads and service goals." style="height:310px;max-height:310px"><figcaption>Calculated results with the same fault, loads and service goals.</figcaption></figure><ul><li>At 40 kW, critical-first serves 90 kW of critical load instead of 30 kW.</li><li>At 180 kW, both goals serve 250 kW total, including all 90 kW of critical load.</li></ul></div>
<span class="pageno">29 / 50</span></div>

<!--
**Say**

At 40 kW, critical-first serves 90 kW of critical load instead of 30 kW. At 180 kW, both goals serve 250 kW total, including all 90 kW of critical load. At 180 kW the two goals both restore 250 kW total, including 90 kW critical. Among the sampled capacities, the first agreement is at 80 kW. That discrete sweep does not establish an exact continuous crossover. More capacity removes the trade-off in this example.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: REVEAL**

Use the prepared result to explain the answer and its limits.
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A new limit needs a new study</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_stale_result.svg" alt="A changed limit requires evidence calculated for the new request." style="height:310px;max-height:310px"><figcaption>A changed limit requires evidence calculated for the new request.</figcaption></figure><ul><li>Now reduce the allowed backup capacity from 40 kW to 20 kW.</li><li>The old result no longer supports the request. The agent must request a new study.</li></ul></div>
<span class="pageno">30 / 50</span></div>

<!--
**Say**

Now reduce the allowed backup capacity from 40 kW to 20 kW. The old result no longer supports the request. The agent must request a new study. Now imagine a stricter request: the backup capacity falls from 40 to 20 kW. Evidence calculated for the old capacity no longer matches the request. The agent should hold the old proposal and obtain a new constrained study. A failed evidence match does not itself prove that every new plan will fail.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>The agent keeps the operator’s goal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_plan.svg" alt="The operator’s priority stays fixed while the tool selects a feasible plan." style="height:305px;max-height:305px"><figcaption>The operator’s priority stays fixed while the tool selects a feasible plan.</figcaption></figure><ul><li>The operator sets priorities. The solver selects loads.</li><li>The agent can request the solve and explain the returned service trade-off.</li></ul></div>
<span class="pageno">31 / 50</span></div>

<!--
**Say**

The operator sets priorities. The solver selects loads. The agent can request the solve and explain the returned service trade-off. In the illustrated priority plan, loads 1, 2 and 5 receive service: 130 kW total and 90 kW critical. The operator sets the goal. The numerical solver selects loads. The agent can request the solve and explain the returned trade-off without changing the goal.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: another plan restores more service</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_14.png" alt="Recorded larger-feeder example, separate from the six-node network." style="max-height:380px;height:auto"><figcaption>Recorded larger-feeder example, separate from the six-node network.</figcaption></figure></div><ul><li>In this separate larger-feeder study, Llama requests another plan.</li><li>The tool reports more service and passing electrical checks.</li></ul></div>
<span class="pageno">32 / 50</span></div>

<!--
**Say**

In this separate larger-feeder study, Llama requests another plan. The tool reports more service and passing electrical checks. This recorded larger-feeder example is separate from the six-node illustration. Llama requests another catalog option. The tool returns about 1,843.61 kW total and 474.04 kW critical service, with current at about 91.87% of its allowance. A proposed improvement becomes evidence only after the check.

**Show**

Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: the tool rejects a trial</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_15.png" alt="Recorded larger-feeder example: the overloaded trial is rejected." style="max-height:380px;height:auto"><figcaption>Recorded larger-feeder example: the overloaded trial is rejected.</figcaption></figure></div><ul><li>The next trial carries too much current.</li><li>It cannot replace the previous passing option.</li></ul></div>
<span class="pageno">33 / 50</span></div>

<!--
**Say**

The next trial carries too much current. It cannot replace the previous passing option. The next recorded trial restores more load but reaches about 111.01% of allowed current. It is rejected. The agent must keep the earlier passing option eligible rather than replace it with an overloaded plan.

**Show**

Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: a wrong ranking is corrected</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_16.png" alt="Recorded larger-feeder example. Lower cost is preferred, including negative costs." style="max-height:380px;height:auto"><figcaption>Recorded larger-feeder example. Lower cost is preferred, including negative costs.</figcaption></figure></div><ul><li>Llama puts two passing plans in the wrong cost order.</li><li>Python keeps the lower-cost plan and checks it again.</li></ul></div>
<span class="pageno">34 / 50</span></div>

<!--
**Say**

Llama puts two passing plans in the wrong cost order. Python keeps the lower-cost plan and checks it again. The model ranks two passing plans in the wrong cost order. Since smaller cost is preferred, negative 6109 is lower than negative 5509. Python keeps the lower-cost passing plan and rechecks it. This example shows why the workflow needs a numerical guard.

**Show**

Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Case 3: can we trust these readings?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_cyber_problem.svg" alt="Concept sketch using a small four-bus model." style="height:310px;max-height:310px"><figcaption>Concept sketch using a small four-bus model.</figcaption></figure><ul><li>Wrong readings can still look consistent with the model.</li><li>The agent can request checks, but action still needs a trusted basis.</li></ul></div>
<span class="pageno">35 / 50</span></div>

<!--
**Say**

Wrong readings can still look consistent with the model. The agent can request checks, but action still needs a trusted basis. Wrong measurements can look consistent with a grid model. The operating question is whether the evidence supports a correction, not whether the agent can write a convincing explanation. Data trust and model coverage remain explicit conditions.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2.0 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>How the agent helps with suspicious readings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_cyber_agent.svg" alt="The agent requests checks and preserves missing evidence." style="height:310px;max-height:310px"><figcaption>The agent requests checks and preserves missing evidence.</figcaption></figure><ul><li>The agent can request the checks and keep missing evidence visible.</li><li>The operator reviews trust, model coverage and the proposed correction.</li></ul></div>
<span class="pageno">36 / 50</span></div>

<!--
**Say**

The agent can request the checks and keep missing evidence visible. The operator reviews trust, model coverage and the proposed correction. The agent can request the permitted checks, read the results and report missing evidence. A required missing trust condition should lead to HOLD. The operator reviews the data basis, model scope and proposed adjustment.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 3.0 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Mismatch is only one check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_mismatch.svg" alt="Mismatch measures model fit; state error measures estimation accuracy." style="height:310px;max-height:310px"><figcaption>Mismatch measures model fit; state error measures estimation accuracy.</figcaption></figure><ul><li>Mismatch J measures how well the model fits the readings.</li><li>The simulation lets us measure how wrong the estimate is (state error).</li></ul></div>
<span class="pageno">37 / 50</span></div>

<!--
**Say**

Mismatch J measures how well the model fits the readings. The simulation lets us measure how wrong the estimate is (state error). Mismatch J measures how well the model fits the readings. It is different from the control-cost score used in the solar case. The simulation also supplies a known true state, allowing an estimation error to be measured. That true state is not normally available to a real operator.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Two patterns of wrong readings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_bad_readings.svg" alt="Concept illustration of two patterns used in the numerical comparison." style="height:330px;max-height:330px"><figcaption>Concept illustration of two patterns used in the numerical comparison.</figcaption></figure><ul><li>One wrong reading may conflict with the other readings.</li><li>Coordinated changes may still look consistent with the model.</li></ul></div>
<span class="pageno">38 / 50</span></div>

<!--
**Say**

One wrong reading may conflict with the other readings. Coordinated changes may still look consistent with the model. One biased reading can disagree with the remaining data. Coordinated changes can agree with one another and still move the estimated state away from truth. This is a conceptual illustration of the two tested patterns; it is not an instruction for creating an attack.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Read the alarm and the estimation error</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L8_plot.png" alt="Calculated model-fit and state-error results." style="max-height:345px;height:auto"><figcaption>Calculated model-fit and state-error results.</figcaption></figure></div><ul><li>Left: mismatch and its alarm threshold. Right: error against the simulation’s known truth.</li><li>A quiet alarm can appear alongside a growing error.</li></ul></div>
<span class="pageno">39 / 50</span></div>

<!--
**Say**

Left: mismatch and its alarm threshold. Right: error against the simulation’s known truth. A quiet alarm can appear alongside a growing error. The left plot compares mismatch with the alarm threshold. The right compares the state estimate with known simulation truth. A quiet alarm can coexist with a growing error. The agent should preserve this distinction when summarizing results.

**Show**

Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A coordinated change can escape the alarm</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_hidden_error.svg" alt="The known state is available inside the simulation for this comparison." style="height:310px;max-height:310px"><figcaption>The known state is available inside the simulation for this comparison.</figcaption></figure><ul><li>At scale 1, one biased reading gives mismatch J=277.50 and an alarm.</li><li>A coordinated change gives J=3.92, no alarm, and 0.02678 rad of state error.</li></ul></div>
<span class="pageno">40 / 50</span></div>

<!--
**Say**

At scale 1, one biased reading gives mismatch J=277.50 and an alarm. A coordinated change gives J=3.92, no alarm, and 0.02678 rad of state error. At the reference change size, an isolated bias gives mismatch about 277.50 and triggers the alarm. A coordinated change gives about 3.92, no alarm, and about 0.02678 radians of state error. A low mismatch is incomplete evidence about data trust.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.
Full source: https://doi.org/10.1145/1952982.1952995
Full paper: https://reitermk.github.io/papers/2011/TISSEC2.pdf
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide has-diagram">

<h1>What if the data change is small?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_bias_change.svg" alt="Discuss the scenario, then advance to the calculated result." style="height:330px;max-height:330px;width:86%;margin:0 auto"><figcaption>Discuss the scenario, then advance to the calculated result.</figcaption></figure><ul><li>Reduce the change to one tenth of the reference size.</li><li>Will the alarm always detect the error?</li><li>What else would the operator need before trusting the readings?</li></ul></div>
<span class="pageno">41 / 50</span></div>

<!--
**Say**

Reduce the change to one tenth of the reference size. Will the alarm always detect the error? What else would the operator need before trusting the readings? Ask pairs to predict what a smaller error does to the alarm. Use one tenth of the reference change size. The question is whether a quiet alarm proves correct readings and what independent information an operator would need. Reveal the calculated example on the next slide.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: DISCUSS**

Invite a prediction and one reason. Advance only after the discussion.

**Ask**

Reduce the change to one tenth of the reference size. Will the alarm always detect the error? What else would the operator need before trusting the readings?

**Answer**

Neither example triggers this alarm at one tenth of the reference size. Both estimates still contain error. No alarm alone does not establish data trust.
Nominal duration: 6 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A quiet alarm can still hide an error</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/exercise_cyber_solution.svg" alt="Calculated results at one tenth of the reference change size." style="height:310px;max-height:310px"><figcaption>Calculated results at one tenth of the reference change size.</figcaption></figure><ul><li>Neither example triggers this alarm at one tenth of the reference size.</li><li>Both estimates still contain error. No alarm alone does not establish data trust.</li></ul></div>
<span class="pageno">42 / 50</span></div>

<!--
**Say**

Neither example triggers this alarm at one tenth of the reference size. Both estimates still contain error. No alarm alone does not establish data trust. For the smaller change, mismatch is about 10.14 for isolated bias and 3.92 for the coordinated pattern. Both are below the threshold of about 15.09. Both estimates still contain error. No alarm means this test has not crossed its threshold; it does not authenticate the readings.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: REVEAL**

Use the prepared result to explain the answer and its limits.
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Trusted information is needed before recovery</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_trust_choice.svg" alt="Additional trustworthy readings are assumed in this example." style="height:310px;max-height:310px"><figcaption>Additional trustworthy readings are assumed in this example.</figcaption></figure><ul><li>Without the required trusted readings, the response is HOLD.</li><li>With readings assumed trustworthy, the tool can calculate a proposal for review.</li></ul></div>
<span class="pageno">43 / 50</span></div>

<!--
**Say**

Without the required trusted readings, the response is HOLD. With readings assumed trustworthy, the tool can calculate a proposal for review. The recovery example assumes additional trustworthy readings are available. Without that required condition the result is HOLD. With the assumption, the tool can calculate a bounded proposal. Neither the fitting algorithm nor Llama authenticates those channels.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>The tool calculates a small correction</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_correction.svg" alt="Per-unit values share the same model base." style="height:310px;max-height:310px"><figcaption>Per-unit values share the same model base.</figcaption></figure><ul><li>The solver finds the smallest allowed adjustment that meets the checked branch limits.</li><li>Predicted flow: 0.17000 p.u. Offline check: 0.17046 p.u. Limit: 0.18000 p.u.</li></ul></div>
<span class="pageno">44 / 50</span></div>

<!--
**Say**

The solver finds the smallest allowed adjustment that meets the checked branch limits. Predicted flow: 0.17000 p.u. Offline check: 0.17046 p.u. Limit: 0.18000 p.u. The fixed recovery example proposes an adjustment of about 0.121694 per unit. The model predicts a monitored flow of 0.17000, while the offline synthetic-truth check gives 0.17046; both are below the 0.18000 limit. Per unit expresses values relative to a common model base. The offline truth check is an experimental aid, not guaranteed field information.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: request the recovery tool</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_7.png" alt="Recorded recovery request and numerical tool result." style="max-height:380px;height:auto"><figcaption>Recorded recovery request and numerical tool result.</figcaption></figure></div><ul><li>Llama requests the supplied recovery tool.</li><li>Python calculates a correction using the assumed trusted readings.</li></ul></div>
<span class="pageno">45 / 50</span></div>

<!--
**Say**

Llama requests the supplied recovery tool. Python calculates a correction using the assumed trusted readings. Read the actual recorded Llama request. The task already supplies a permitted recovery tool and the trusted-reading assumption. Python estimates the state and calculates the correction. The language model routes the request; it does not provide the numerical estimate.

**Show**

Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: keep human review</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_8.png" alt="Recorded workflow result; human review remains pending." style="max-height:350px;height:auto"><figcaption>Recorded workflow result; human review remains pending.</figcaption></figure></div><ul><li>The model checks pass; human review is still pending.</li><li>Data trust and operating permission still need review.</li></ul></div>
<span class="pageno">46 / 50</span></div>

<!--
**Say**

The model checks pass; human review is still pending. Data trust and operating permission still need review. The recorded model checks pass, but the overall result remains REVIEW and human acknowledgement is pending. The operator still needs a trusted data basis and operating authority. The fixed workflow obtains the same numerical correction, so this is not evidence that Llama improves estimation.

**Show**

Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Review must refer to the same proposal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_review_match.svg" alt="Illustrative proposal IDs. Review is separate from equipment operation." style="height:330px;max-height:330px"><figcaption>Illustrative proposal IDs. Review is separate from equipment operation.</figcaption></figure><ul><li>The proposal ID and model scope must match the checked study.</li><li>A different proposal or wider scope needs a new review.</li></ul></div>
<span class="pageno">47 / 50</span></div>

<!--
**Say**

The proposal ID and model scope must match the checked study. A different proposal or wider scope needs a new review. A reviewer must refer to the same proposal and scope that were checked. A changed proposal ID or a wider request cannot inherit an earlier passing result. In the teaching example, readback is simulated and sends no equipment command.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>The operator chooses the next step</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_review.svg" alt="The operator reviews the study and chooses the next authorized step." style="height:330px;max-height:330px"><figcaption>The operator reviews the study and chooses the next authorized step.</figcaption></figure><ul><li>Review the case, tool results, checked limits and missing work.</li><li>Request another study, reject the proposal or take the next authorized step.</li></ul></div>
<span class="pageno">48 / 50</span></div>

<!--
**Say**

Review the case, tool results, checked limits and missing work. Request another study, reject the proposal or take the next authorized step. The operator can request more evidence, reject the proposal or continue with a defined authorized step. Review the case, returned limits, model coverage and missing studies. Acceptance of a study is separate from issuing a field command.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.
Full source: https://doi.org/10.6028/NIST.AI.100-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Multi-agent framework used in these cases</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/workshop_multi_agent.svg" alt="Implemented five-role workflow with a case-specific numerical tool." style="height:360px;max-height:360px"><figcaption>Implemented five-role workflow with a case-specific numerical tool.</figcaption></figure><ul><li>The five roles share the same case facts and checked results.</li><li>One Llama model handles planning and refinement. Python calculates and checks.</li></ul></div>
<span class="pageno">49 / 50</span></div>

<!--
**Say**

The five roles share the same case facts and checked results. One Llama model handles planning and refinement. Python calculates and checks. Awareness reads the shared case. Planning prepares permitted options and uses Llama to choose a study. Simulation calculates. Verification checks limits and case identity. The Llama optimizer requests a bounded change or ranks passing options. Every changed trial returns for simulation and verification. Python guards the final choice before operator review. One Llama model fills two roles; this is not five independent language models. The implementation uses case-specific numerical tools behind the same stages.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.

**Ask**

Which roles use Llama, and who checks a revised proposal?

**Answer**

Planning and the optimizer use one Llama model. Python performs fresh simulation, verification and a final guarded check before operator review.
Nominal duration: 4.0 minutes.

Full sources:
Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py
Publication: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json

Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Explain one case in your own words</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/concept_case_summary.svg" alt="Explain the idea first. Practice material is available separately." style="height:330px;max-height:330px"><figcaption>Explain the idea first. Practice material is available separately.</figcaption></figure><ul><li>What is the operator’s problem, and what should the agent request next?</li><li>Which tool result supports the proposal, and what must the operator still decide?</li></ul></div>
<span class="pageno">50 / 50</span></div>

<!--
**Say**

What is the operator’s problem, and what should the agent request next? Which tool result supports the proposal, and what must the operator still decide? Ask participants to choose one case and explain the complete loop in their own words. They should name the problem, an agent request, a returned numerical fact and a remaining human decision. Optional practice materials can be used after the concept tutorial, but no account or code is needed for this discussion.

**Show**

Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN**

Connect the visual to the operator’s next decision.
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->
