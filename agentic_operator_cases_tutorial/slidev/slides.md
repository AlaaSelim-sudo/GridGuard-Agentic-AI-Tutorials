---
theme: default
title: "Hands-on: Three Operator Cases"
info: Follow Classroom Labs through voltage support, service restoration and cyber response, with three exercises
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

<h1>Hands-on:<br>Three Operator Cases</h1>
<p>Run one notebook to understand three operator studies.</p>
<p>90 minutes / three short exercises / no coding experience required</p>
<div class="presenters"><div><strong>Alaa Selim</strong><span>MIT/Dartmouth</span></div><div><strong>Mohamed Chehada</strong><span>UT Austin</span></div></div>
<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup"><small>Independent educational material · IEEE ComSoc theme adaptation</small>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">1 / 80</span></div>

<!--
Open the one required Classroom Labs notebook. This hands-on workshop uses 80 slides and 180 teaching minutes, with breaks outside that total. Start with a twelve-minute Stanford concept block: show each original source figure, then its simple grid adaptation. The next seven minutes prepare Colab and run L0–L1. Learners calculate fresh numerical results and inspect separately labeled saved Llama replies. No default cell calls an LLM or operates equipment. Keep the notebook in order and run L10B only after L10. Work in pairs and use the six-page participant guide. Presenter affiliations were supplied by the presenters. The IEEE ComSoc theme is an independent educational adaptation.
Takeaway: 
Nominal duration: 0.5 minutes.

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

<h1>What is agentic AI?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_goal_loop.svg" alt="Grid teaching adaptation of the Stanford lecture, p.2. Model choices are recorded; calculations can run now." style="height:350px;max-height:350px"><figcaption>Grid teaching adaptation of the Stanford lecture, p.2. Model choices are recorded; calculations can run now.</figcaption></figure><ul><li>An LLM agent works toward a goal by choosing tools, reading their results and choosing what to do next.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.</a></div>
<span class="pageno">2 / 80</span></div>

<!--
Use the architectural definition in Anthropic, Building effective agents: an agent lets the LLM direct its process and tool use. Agentic AI is a broad term; here it means a system organized around this bounded loop. An AI agent is the component that chooses and follows steps. A tool is a permitted software function that returns a result. Point to the goal, model choice, executable tool, returned evidence and feedback arrow. The application stores case facts and prior results as the context supplied at the next model request. If a required check is missing, the outcome remains HOLD. Stop or return a proposal only under the fixed workflow rules. Do not imply that feedback alone establishes agency: conventional programs can also branch and loop. Our default notebook calculates engineering results now but replays the actual old Llama choices. No live model service is needed. Stanford source: Monica Lam, CS224V Agentic AI, Lecture 1: Introduction, Fall 2026, p.2 describes function calling and agentic workflows. The goal-and-feedback drawing is our grid teaching adaptation, supported by the separate bounded-agent architecture citation. This is not an original Stanford power-system diagram.
Takeaway: 
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

<h1>Stanford: tool calls become a workflow</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_agentic_capabilities.png" alt="Original Stanford lecture excerpt, p.2. Next, connect tool use to evidence, task rules and decision checks." style="max-height:330px;height:auto"><figcaption>Original Stanford lecture excerpt, p.2. Next, connect tool use to evidence, task rules and decision checks.</figcaption></figure></div><p class="activity-link"><a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=2">Read the Stanford lecture, p.2</a></p><ul><li>A tool call runs one step. An agentic workflow links steps and uses their results to continue or stop.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.</a></div>
<span class="pageno">3 / 80</span></div>

<!--
Show the two original capability panels from Monica Lam’s Stanford CS224V introduction, p.2. The left panel introduces model-selected function calling. The right panel describes multi-step planning, tool use and self-correction. Our plain-language sentence connects the panels to the preceding bounded-loop teaching drawing. The following source-and-lab pairs show why tool results, explicit goals and checked evidence matter in each case. In that example Llama requests a named action and Python validates the JSON choice before calling an existing function; it does not use a native tool_calls protocol. Conventional software can also loop, and a chatbot may itself contain an agent. Here we identify the agentic feature by the model’s permitted next-step choice based on returned evidence. The class replays those old model choices while numerical cells calculate current results. Source lecture figure is shown unchanged within the documented crop.
Takeaway: 
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

<h1>Stanford example: check before you write</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_wikichat_steps.png" alt="Original Stanford lecture excerpt, p.19. WikiChat checks claims before drafting a reply." style="max-height:350px;height:auto"><figcaption>Original Stanford lecture excerpt, p.19. WikiChat checks claims before drafting a reply.</figcaption></figure></div><p class="activity-link"><a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=19">Read the Stanford lecture, p.19</a></p><ul><li>Grid lab takeaway: check the numerical result before writing the study summary.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.19.</a></div>
<span class="pageno">4 / 80</span></div>

<!--
The displayed figure is an original excerpt from Monica Lam’s Stanford CS224V introduction, p.19. Follow its retrieval, claim checking and writing steps. The WikiChat paper is fully cited in the reading guide. Our application to grid studies is a teaching analogy: read the stated limits, run the appropriate numerical check and summarize the actual returned result. Ask which lab step would detect a current violation. The classroom notebook does not run WikiChat; its dialogue factuality measurements are not electrical performance results. This source figure is now in the opening. Spend about one minute on the check-before-writing idea. The next slide maps it to L2; do not run a cell yet.
Takeaway: 
Nominal duration: 1.25 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.
Full source: https://aclanthology.org/2023.findings-emnlp.157/
Full paper: https://aclanthology.org/2023.findings-emnlp.157.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Stanford idea / Colab preview: L2</div>
<h1>Voltage: a proposal needs a numerical check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_voltage.svg" alt="Our grid adaptation of WikiChat’s checking habit. L2 calls Python directly; L10B replays saved Llama choices." style="height:340px;max-height:340px"><figcaption>Our grid adaptation of WikiChat’s checking habit. L2 calls Python directly; L10B replays saved Llama choices.</figcaption></figure><ul><li>L2 lets you test the numerical check. The saved L10B episode shows Llama choosing the next tool.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.19; Classroom Labs L2.</a></div>
<span class="pageno">5 / 80</span></div>

<!--
Connect the preceding original WikiChat figure to a grid claim. A text answer might say that a proposed plan fits the limits; a numerical tool must calculate the supporting result. The reference bar is the default L2 MPC result: maximum allowed-current utilization 73.619901%, rounded to 73.62%, at LOAD_SCALE=1.0 and RATING_FRACTION=0.80. It passes this current allowance; modeled voltage and required model coverage must also be checked. The default medium-voltage calculation is not proof for the full MV/LV system. This visual previews the lab; do not run L2 before setup, L0 and L1. L2 calls numerical functions directly. The separate P3 L10B archive later shows Llama requesting a check, reading a failed result and selecting a fallback. Our application is an analogy to evidence checking, not a claim that the notebook runs WikiChat.
Takeaway: 
Nominal duration: 1.5 minutes.

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

<div class="lesson teaching rigorous figure-slide">

<h1>Stanford example: tools need clear rules</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_genie_specification.png" alt="Original Stanford lecture excerpt, p.40. The lab adopts the idea of explicit rules in Python." style="max-height:315px;height:auto"><figcaption>Original Stanford lecture excerpt, p.40. The lab adopts the idea of explicit rules in Python.</figcaption></figure></div><p class="activity-link"><a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=40">Read the Stanford lecture, p.40</a></p><ul><li>Write down the required inputs, permitted tools, limits and stop rules.</li><li>Our lab keeps those rules in Python. A language reply cannot change the limits.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40.</a></div>
<span class="pageno">6 / 80</span></div>

<!--
Stanford connection: Lam p.40 and the published Genie Worksheets paper emphasize developer-defined workflows and knowledge sources. The published framework uses an algorithmic runtime to enforce a supplied policy, with LLMs used for language understanding and response generation. Our lab uses custom Python functions, not Genie Worksheets. The application analogy is to specify the task and prevent a language reply from silently changing its limits or filling missing required inputs. A passed calculation does not prove that the task description was correct. The figure shown here is an actual excerpt from the supplied Stanford lecture. Ask the audience to point to the claim-checking or policy step, then identify the corresponding Python check in our lab. We borrow the design habit; the notebook does not run WikiChat or Genie. Their non-grid benchmarks are not electrical performance results.
Takeaway: 
Nominal duration: 1.25 minutes.

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

<div class="eyebrow">Stanford idea / Colab preview: L6</div>
<h1>Restoration: the service goal shapes the plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_restoration.svg" alt="Our grid adaptation of explicit task rules. L6 uses the same 40 kW varied tie and 100 kW fixed tie for both goals." style="height:340px;max-height:340px"><figcaption>Our grid adaptation of explicit task rules. L6 uses the same 40 kW varied tie and 100 kW fixed tie for both goals.</figcaption></figure><ul><li>An agent must keep the stated service goal. L6 lets you see how that goal changes the plan.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40; Classroom Labs L6.</a></div>
<span class="pageno">7 / 80</span></div>

<!--
The preceding Genie excerpt motivates writing down the task and its rules before calling a function. In L6 the goal is part of the optimization problem: priority weighting serves 130 total kW, including 90 critical kW; maximizing total service gives 140 total kW, including 30 critical kW. The 40 kW limit belongs to one varied tie, while another tie stays fixed at 100 kW. Totals also include the 40 kW load at node 1 upstream of those ties. A 40 kW varied-tie limit is not a cap on total system service. Each stacked bar uses the same scale. Critical service is cyan; other service is blue. Ask which goal better matches an illustrative request to prioritize a hospital. The numerical model uses abstract critical loads, not an actual hospital dataset. Later learners run both goals and change the tie capacity. L6 is a direct Python calculation, not a live LLM agent. An agent coordinating such a study must preserve the requested goal and explain the returned tradeoff. The separate L10B feeder-catalog archive supplies actual saved Llama choices; it differs from this six-node L6 model. Our notebook does not implement Genie Worksheets.
Takeaway: 
Nominal duration: 1.5 minutes.

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

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Stanford source example / grid teaching analogy</div>
<h1>Stanford: language and decision checks</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_language_decision.png" alt="Clinical-trial research example. SMT represents logical constraints; MaxSAT helps find decision-changing conditions." style="max-height:190px;height:auto"><figcaption>Clinical-trial research example. SMT represents logical constraints; MaxSAT helps find decision-changing conditions.</figcaption></figure></div><p class="activity-link"><a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=53">Read the Stanford lecture, p.53</a></p><ul><li>The lecture turns written facts into constraints, then uses a solver to check a decision.</li><li>Our grid adaptation: Llama requests a study, Python checks its results, and the operator reviews the proposal.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53.</a></div>
<span class="pageno">8 / 80</span></div>

<!--
This original diagram selection comes from the function row on p.53 of Monica Lam’s introduction. It shows a clinical-trial example, not a power-system experiment. The language model translates written facts into an SMT representation; a separate solver derives a decision from those constraints. SMT means satisfiability modulo theories, a way to express and solve logical constraints. MaxSAT supports the lecture’s search for conditions that change a decision. The lecture also states that the formalization may not be completely faithful, so correctness remains relative to the represented constraints. Our application is an analogy: Llama requests the permitted estimate or control tool and Python checks numerical limits. An operator must still confirm the trust assumption and review the proposed action. Our notebook does not run an SMT/MaxSAT solver or prove formal electrical safety. Preview the HOLD/PROPOSE distinction now; participants will calculate the L9 outcomes later with their stated model and trusted-data assumption.
Takeaway: 
Nominal duration: 1.25 minutes.

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

<div class="eyebrow">Stanford idea / Colab preview: L8–L9</div>
<h1>Cyber: a clear answer still needs evidence</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_cyber.svg" alt="Our grid adaptation of separating language from checks. The fixed L9 example returns HOLD or PROPOSE under stated assumptions." style="height:340px;max-height:340px"><figcaption>Our grid adaptation of separating language from checks. The fixed L9 example returns HOLD or PROPOSE under stated assumptions.</figcaption></figure><ul><li>L8 tests whether readings can look consistent but be wrong. L9 adds a trust assumption and recovery checks.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53; Classroom Labs L8–L9.</a></div>
<span class="pageno">9 / 80</span></div>

<!--
Relate the original Stanford clinical example to this lab without importing a formal guarantee. L8 fits readings to a four-bus DC model using WLS, weighted least squares. Its small residual is a measure of fit, not proof of sensor truth; the known simulation truth is used only for teaching error comparisons. L9 is a separate fixed recovery fixture. Without trusted replacement data it returns HOLD. With three additional readings assumed trusted and a successful modeled recovery check, it returns PROPOSE. The yes branch depicts this fixed example with passing numerical checks; a real study also needs every required check to pass. The calculation does not authenticate the extra readings. Later learners run L8, vary the attack scale, then reset before the independent L9 example. Python performs these calculations now. A coordinating agent should request evidence and retain HOLD when a required premise is missing; saved L10B replies show a separate recorded cyber case. Our code uses numerical checks, not the Stanford SMT/MaxSAT runtime.
Takeaway: 
Nominal duration: 1.5 minutes.

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

<h1>Ask four questions about a study result</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_review_questions.svg" alt="Grid teaching adaptation of Monica Lam’s accountability concepts, Stanford CS224V introduction, pp.52–53." style="height:330px;max-height:330px"><figcaption>Grid teaching adaptation of Monica Lam’s accountability concepts, Stanford CS224V introduction, pp.52–53.</figcaption></figure><p class="activity-link"><a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=52">Read the Stanford lecture, p.52</a></p><ul><li>Find the tool result, assumptions, rules and the operator’s next step.</li><li>If a claim has no supporting result, leave it unresolved and request the missing check.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, pp.52–53.</a></div>
<span class="pageno">10 / 80</span></div>

<!--
Lam’s pp.52–53 distinguish verifiable rationale, explicit assumptions, policy consistency and actionable next conditions. Translate these into four plain questions: which tool supports this claim, which inputs and model were used, were the same limits and service priorities kept, and what must the operator review next? Our power-flow, optimization and evidence-binding checks are numerical/software checks. They do not inherit the lecture’s SMT correctness claims. Ask pairs to apply the questions to one L10B explanation and to the full-scope HOLD at L12. We show only the actual public returned reasons, not hidden chain-of-thought. This closes the twelve-minute opening concept block. Point out that all three labs will use these questions; participants do not need to memorize a framework or run ahead.
Takeaway: 
Nominal duration: 1.25 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>One notebook covers all three cases</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_one_notebook.svg" alt="Only Classroom Labs is required. The graph and trace notebooks are companion material." style="height:330px;max-height:330px"><figcaption>Only Classroom Labs is required. The graph and trace notebooks are companion material.</figcaption></figure><p class="activity-link"><a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Open Classroom Labs in Google Colab</a></p><ul><li>Save a copy in Drive. Keep this same notebook open for all three cases.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">11 / 80</span></div>

<!--
Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Get ready in four small steps</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_ready.svg" alt="Setup prepares the runtime. Then follow each named lesson cell with the slides." style="height:315px;max-height:315px"><figcaption>Setup prepares the runtime. Then follow each named lesson cell with the slides.</figcaption></figure><ul><li>Open the notebook, save your copy, connect a CPU and run setup.</li><li>Wait for Ready. Then run L0 and L1 before starting the three cases.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">12 / 80</span></div>

<!--
For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or LLM download. If setup stops, reconnect the runtime and rerun setup before starting L0.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.
Full source: https://research.google.com/colaboratory/faq.html
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Run a cell, then read what it returns</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_cell_loop.svg" alt="Teaching illustration, not a Colab screenshot. Input lines match L2; run the full L2 cell." style="height:330px;max-height:330px"><figcaption>Teaching illustration, not a Colab screenshot. Input lines match L2; run the full L2 cell.</figcaption></figure><ul><li>Find the L heading. Use the play button to run the whole matching code cell.</li><li>Wait, then read the table or plot underneath it. Editing an input alone does not update output.</li></ul></div>
<div class="sources">Source: <a href="https://research.google.com/colaboratory/faq.html">Google Colab FAQ; Classroom Labs L2, cell classroom-007.</a></div>
<span class="pageno">13 / 80</span></div>

<!--
Point to the three parts: editable input, run control and returned output. The illustrated input lines are the first two lines of the actual L2 cell, not a complete standalone program. The full cell calls the voltage helper and draws two plots. The runtime remembers variables from earlier cells, which is why we run the lesson in order. If NameError reports a missing variable, return to setup/L0 and rerun the required earlier cells. Do not treat a previously displayed output as the result of a number just edited until you rerun its cell. Use the L labels instead of numerical cell indexes. Later cells need earlier variables.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.
Full source: https://research.google.com/colaboratory/faq.html

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L0 · classroom-002</div>
<h1>Run L0: choose the classroom route</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L0 (classroom-002), source lines 11–14.</p><pre class="teaching-code">RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / &#x27;data/lindistflow3_network.json&#x27;).exists(), &#x27;Start Jupyter in the tutorial folder&#x27;</pre><ul><li>Keep both switches False: new numerical checks, saved controller and archived model replies.</li><li>If the data check fails, rerun setup before continuing.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">14 / 80</span></div>

<!--
Run all of L0 to import the helpers, configure the plots and initialize the timing record. Keep RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. These settings skip the optional full-feeder OpenDSS route and local model service. They do not make the calculations prerecorded: L2 and L4 through L9 run fresh numerical calculations or checks, while L12 checks the evidence binding and simulated readback.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L1 · classroom-004</div>
<h1>Run L1: does the evidence still match?</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L1_binding.png" alt="Reference L1 output: only the unchanged request and command match the evidence." style="max-height:345px;height:auto"><figcaption>Reference L1 output: only the unchanged request and command match the evidence.</figcaption></figure></div><ul><li>Read binding_pass: does the record match the same inputs and command?</li><li>Expect True, False, False. Changing the load or command breaks that match.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">15 / 80</span></div>

<!--
Evidence binding means matching a checked record to the exact inputs, proposed command and returned result, using content hashes. Treat L1 as a same-content check, not a test that a physical action passes its limits. The first row keeps the request and command unchanged. The next two rows change a request field or command field, so binding_pass is True, False, False. A failed match calls for new evidence; it does not prove the changed action fails its limits. A matching hash also does not authenticate a sensor.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Voltage: open L2</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/feeder.png" alt="Synthetic SMART-DS teaching feeder; not an operating utility circuit." style="max-height:345px;height:auto"><figcaption>Synthetic SMART-DS teaching feeder; not an operating utility circuit.</figcaption></figure></div><ul><li>MPC makes a forecast-based plan. SAC is a saved learned controller.</li><li>Check limits first. Then compare penalty score J; smaller is preferred after the checks pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">16 / 80</span></div>

<!--
The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The command sets active- and reactive-power participation for an inverter fleet. MPC, model predictive control, uses a system model and a short forecast to calculate a plan under limits; here the proposed command is the first step of that plan. SAC, Soft Actor–Critic, is a saved controller learned from rewards. It produces a proposal from old weights without training again. The default calculation covers medium-voltage (MV) phases and MV line currents, with simplified low-voltage (LV) aggregation. Feasible means the proposal passes the limits represented by that model. Compare the penalty score J only after checking those limits; smaller J is preferred for this stated objective. Run L0 and L1 first.
Takeaway: 
Nominal duration: 2 minutes.

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

<h1>MPC plans; SAC proposes</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_mpc_sac.svg" alt="MPC: model predictive control. SAC: Soft Actor–Critic. These are control tools inside the larger workflow." style="height:350px;max-height:350px"><figcaption>MPC: model predictive control. SAC: Soft Actor–Critic. These are control tools inside the larger workflow.</figcaption></figure><ul><li>Both tools propose control settings. The same numerical check tests their voltage and current limits.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">17 / 80</span></div>

<!--
MPC uses a model and a short forecast to optimize a plan; this lab applies its first action. SAC is a saved policy learned through reinforcement learning; it produces a new control proposal using old weights, without training again. Neither is the coordinating LLM. The outer agent can choose which permitted study to request. L2 calls both tools directly and displays their checks; this cell alone is not a live LLM agent. Later recorded P3 figures illustrate Llama coordinating the existing tools. Define per unit when the control-limit slide introduces the voltage scale: 1.0 p.u. is the stated base value. Explain MILP and WLS only in their respective cases.
Takeaway: 
Nominal duration: 1.5 minutes.

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

<div class="eyebrow">Recorded P3 example / separate from the L2 calculation</div>
<h1>A real agent changes its next step</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_recorded_trace.svg" alt="Recorded P3 example, separate from L2. 111.966607% and 99.604410% are rounded here." style="height:350px;max-height:350px"><figcaption>Recorded P3 example, separate from L2. 111.966607% and 99.604410% are rounded here.</figcaption></figure><ul><li>The failed tool result leads to a fallback check. Passing the checks still leaves human review.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json">Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.</a></div>
<span class="pageno">18 / 80</span></div>

<!--
This is an actual saved Llama 3.1:8b voltage episode, not a fabricated interactive exchange. Call 1 selects VERIFY_SAC_FIRST; the numerical check returns 111.966607 percent of allowed current and two current violations. Call 2 selects USE_MPC_PLAN; its numerical check returns 99.604410 percent of allowed current and no recorded violations. The SAC and MPC tools already exist; Llama does not invent or solve the power flow. The arrows show tool-request, result, next-request, result. Call 3 selects REVIEW_EVIDENCE. Human acknowledgment remains PENDING and equipment_dispatch is False. This separate P3 MV/LV OpenDSS archive differs from the fresh L2 exercise and from L3 test_01. Later voltage slides display the exact public returned reasons; learners can replay the source in L10B after completing the three cases. The fixed comparator reaches the same numerical outcome, so the trace illustrates coordination rather than a proven performance improvement. This recorded example now follows the MPC/SAC definition slide in the voltage case, after Colab setup. It remains a preview; run the complete episode in L10B later.
Takeaway: 
Nominal duration: 1.5 minutes.

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

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Control settings and limits</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_capability.svg" alt="Active and reactive settings share the inverter’s power limit." style="height:305px;max-height:305px"><figcaption>Active and reactive settings share the inverter’s power limit.</figcaption></figure><ul><li>a sets active-power participation; b sets reactive-power participation.</li><li>Check the inverter limits, modeled voltages and allowed line current.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">19 / 80</span></div>

<!--
Active power delivers net energy; reactive power supports the AC voltage and current balance. The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltages must be between 0.95 and 1.05 per unit (p.u.), where values are divided by a stated base. RATING_FRACTION=0.80 sets allowed current to 80% of the nominal rating. The displayed current percentage uses this reduced allowance as its denominator. Passing the inverter bounds alone does not show that network limits pass.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A tool is a Python function in this lab</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_python_tool.svg" alt="L2 calls lab.voltage_lab(LOAD_SCALE, RATING_FRACTION) directly. Recorded agent coordination is separate." style="height:350px;max-height:350px"><figcaption>L2 calls lab.voltage_lab(LOAD_SCALE, RATING_FRACTION) directly. Recorded agent coordination is separate.</figcaption></figure><ul><li>A tool takes defined inputs and returns evidence. The notebook lets you see both.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">20 / 80</span></div>

<!--
Find the actual function call on the next slide. The first two cell lines set the load scale and current allowance; the helper returns numerical proposals, checks and a table for plotting. A tool can be an optimizer, simulator, estimator, lookup or evidence checker. It is not the LLM itself. The student initiates this direct function call with the play button. In the separate recorded workflow Llama selects a named action, the Python application validates that action and its inputs, then invokes a permitted numerical function. Do not claim that the L2 helper uses a live agent gateway. Saving a notebook is separate from keeping a runtime: after a reset, rerun setup and earlier cells.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Run L2 with the default inputs</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L2 (classroom-007), source lines 1–4.</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)</pre><ul><li>Run all of L2 to calculate the MPC plan and check the saved SAC controller’s proposal.</li><li>Read feasible, current_step_J and max_allowed_current_pct.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">21 / 80</span></div>

<!--
Start with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. The saved SAC actor produces a new proposal by inference; it is not trained in this cell. Both proposals pass the default classroom checks. MPC has the lower current-step J for this case and objective. This single result does not establish a universal control advantage. The output field feasible reports whether the modeled limits pass; current_step_J is this step’s penalty score, and max_allowed_current_pct is maximum current as a percentage of the reduced allowance.
Takeaway: 
Nominal duration: 2 minutes.

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

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Read the voltage and current plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_plot.png" alt="Reference L2 plots; rerun L2 to calculate plots for your inputs." style="max-height:345px;height:auto"><figcaption>Reference L2 plots; rerun L2 to calculate plots for your inputs.</figcaption></figure></div><ul><li>Left: compare the sorted modeled voltages with the allowed band.</li><li>Right: compare line current with the 100% allowed-current limit.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">22 / 80</span></div>

<!--
The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Check limits before comparing scores</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_table.png" alt="Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80." style="max-height:345px;height:auto"><figcaption>Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80.</figcaption></figure></div><ul><li>Default MPC passes: current use 73.62%, penalty score J about 0.03110.</li><li>Default saved SAC passes: current use 51.68%, J about 0.43643.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">23 / 80</span></div>

<!--
In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J. Both voltage extrema are within the stated 0.95–1.05 p.u. band for this represented MV model.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A rule and a tool result answer different questions</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_claim_evidence.svg" alt="Teaching analogy. The number shown comes from the recorded P3 replay, which is separate from L2." style="height:330px;max-height:330px"><figcaption>Teaching analogy. The number shown comes from the recorded P3 replay, which is separate from L2.</figcaption></figure><ul><li>A document can tell us the limit. A numerical tool tells us how the proposal compares with it.</li><li>Keep the source, the measured or calculated value, and the remaining checks together.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, pp.17–25; recorded P3 current check.</a></div>
<span class="pageno">24 / 80</span></div>

<!--
Stanford connection: the lecture’s WikiChat discussion, pp.17–25, separates finding material from checking factual claims. Apply the habit to a grid study: retrieving a current limit is different from calculating current for a candidate. The displayed 99.604410% value belongs to the separate archived P3 OpenDSS replay, not to the learner’s fresh L2 result. This example supports only that current check under its recorded model. A sentence, retrieved document or citation does not establish full-network feasibility. Treat the input limits as the task policy. A text source describes the rule; the solver evaluates the particular proposal.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.
Full source: https://aclanthology.org/2023.findings-emnlp.157/
Full paper: https://aclanthology.org/2023.findings-emnlp.157.pdf

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Exercise 1: tighten the current allowance</h1>
<div class="content"><pre class="source-excerpt">RATING_FRACTION = 0.75</pre><ul><li>In L2, change only RATING_FRACTION from 0.80 to 0.75. Predict, then rerun.</li><li>For each method, report feasible, allowed-current use and current_step_J.</li><li>Does a PASS cover the full medium- and low-voltage network? Explain.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">25 / 80</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Change one number and explain the difference</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_try_observe.svg" alt="Reference L2 exercise: MPC uses 73.62% of the default allowance and 78.53% after the change." style="height:330px;max-height:330px"><figcaption>Reference L2 exercise: MPC uses 73.62% of the default allowance and 78.53% after the change.</figcaption></figure><ul><li>A tighter allowance makes the same current a larger percentage of that allowance.</li><li>At 0.75, MPC uses 78.53% and SAC 54.85%. Both pass this particular test.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L2, cell classroom-007; verified default and exercise outputs.</a></div>
<span class="pageno">26 / 80</span></div>

<!--
Use this visual immediately after the first exercise debrief. It shows the measured reference MPC outputs, rounded to two decimal places, for RATING_FRACTION 0.80 and 0.75. The SAC result is also computed in the notebook but is not drawn here. Both proposals pass this particular tighter test. The result is not a general guarantee for other loads or limits. Ask pairs to explain the denominator in the percentage. Restore the default before moving to L3’s independent archived case. This combines the original numerical debrief with the visual explanation. Compare both methods before restoring RATING_FRACTION=0.80.
Takeaway: 
Nominal duration: 4.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Reset L2 before reading old model choices</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80</pre><ul><li>Restore the default values and rerun L2.</li><li>L3–L5 use the original test_01 case, separate from your changed L2 experiment.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">27 / 80</span></div>

<!--
Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>What runs now and what was recorded</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_modes.svg" alt="Three explicitly labeled teaching modes used throughout this workshop." style="height:330px;max-height:330px"><figcaption>Three explicitly labeled teaching modes used throughout this workshop.</figcaption></figure><ul><li>The current cell calculates new results. The saved Llama reply keeps its original inputs.</li><li>Changing your lab input does not rewrite the recorded agent study.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md">Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">28 / 80</span></div>

<!--
Point to these evidence modes throughout the session. Default classroom cells calculate fresh results without a live language-model call. L10B displays verified historical Llama choices, original reasons and associated recorded results. Changing your L2 or L6 input does not change those old replies. The final control-room diagrams are a proposed teaching design, not evidence of a deployed utility platform. No new equipment operation occurs in any of these modes. FRESH means calculated during the current execution. SAVED POLICY means old weights used for new inference. ARCHIVED ACTUAL LLM means an old reply with its original inputs and timing. This slide comes just before L3 so the distinction is applied immediately.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L3 · classroom-010</div>
<h1>L3 opens a separate recorded case</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.</p><pre class="teaching-code">pool = lab.saved_pool(&#x27;test_01&#x27;)
display(pd.DataFrame(pool[&#x27;responses&#x27;])[[&#x27;model_id&#x27;, &#x27;operation_id&#x27;, &#x27;reason&#x27;, &#x27;seconds&#x27;, &#x27;source&#x27;]])</pre><ul><li>Run L3. Read the original case ID, requested operations and recorded seconds.</li><li>These reasons are old model replies. Displaying them makes no new model call.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">29 / 80</span></div>

<!--
The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L3 · classroom-010</div>
<h1>What did the models choose?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_canonical_trial.svg" alt="Three old replies request two distinct operations; two votes select reactive-power relaxation." style="height:305px;max-height:305px"><figcaption>Three old replies request two distinct operations; two votes select reactive-power relaxation.</figcaption></figure><ul><li>Different wording can request the same tool and numbers.</li><li>The notebook groups matching trials. An explanation alone does not show that limits pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">30 / 80</span></div>

<!--
The three old replies reduce to two distinct operations after matching their tool names and numerical parameters. The vote keeps one contribution per model. In test_01, two models vote for the Q-relaxation trial, which relaxes a reactive-power restriction in that declared test. This diagram shows the old input and choices; it is not a new vote after a learner edits L2. Grouping matching trials avoids counting different wording as different physical proposals.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L4 · classroom-013</div>
<h1>Run L4: check the old choice again</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.</p><pre class="teaching-code">started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings[&#x27;L4 new verification of archived choices&#x27;] = time.perf_counter() - started
display(selected_trials[&#x27;table&#x27;])
assert pool[&#x27;frozen&#x27;] and pool[&#x27;training_updates&#x27;] == 24</pre><ul><li>After L3, run L4. Python checks the selected proposal again for its original case.</li><li>Compare majority vote with the saved LinUCB selector on that same case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">31 / 80</span></div>

<!--
The selector is frozen and makes no training updates in this lesson. L4 applies the archived selected operation to its original test context and runs a fresh numerical check. This is a replay with new verification, not a new language-model decision or an online learning experiment. LinUCB is a learned selector that scores the available choices from context; its saved settings stay fixed here.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L4 · classroom-013</div>
<h1>Separate the old choice from the new check</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L4_checks.png" alt="Reference L4 output: old selector choices, new numerical checks of the original case." style="max-height:345px;height:auto"><figcaption>Reference L4 output: old selector choices, new numerical checks of the original case.</figcaption></figure></div><ul><li>Both selectors choose the same reactive-power relaxation trial and pass the new MV check.</li><li>Predicted reward is a learned score. Read new_check_passes for the engineering check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">32 / 80</span></div>

<!--
The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>Run L5: check what the model covers</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.</p><pre class="teaching-code">started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings[&#x27;L5 selected model scope checks&#x27;] = time.perf_counter() - started
display(scope_audit[&#x27;table&#x27;])</pre><ul><li>Keep RUN_OPENDSS=False. Run L5 and read the table and optional_mode message.</li><li>L5 checks the original test_01 MV-MPC plan. OpenDSS is disabled.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">33 / 80</span></div>

<!--
L5 rebuilds the original test_01 case and runs a new check on its original MV-MPC incumbent, meaning the baseline plan saved with that case. This is not the reactive-power-relaxation candidate checked in L4. With RUN_OPENDSS=False, L5 checks only the reduced model and reports that OpenDSS is disabled. This CPU route performs no new full-feeder AC check. A wider-model study saved earlier is not a result calculated today. Model scope means the network parts and physical effects that a check represents.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>A PASS covers only the model checked</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L5_scope.png" alt="Reference L5 output: a medium-voltage check with OpenDSS disabled." style="max-height:345px;height:auto"><figcaption>Reference L5 output: a medium-voltage check with OpenDSS disabled.</figcaption></figure></div><ul><li>This check covers medium-voltage (MV) phases and currents, not all low-voltage (LV) equipment.</li><li>For a full MV/LV request, get the wider check or HOLD.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">34 / 80</span></div>

<!--
Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Recorded agent example · separate P3 study</div>
<h1>Voltage: Llama asks to check the saved controller</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_1.png" alt="Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later." style="max-height:380px;height:auto"><figcaption>Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.</figcaption></figure></div><ul><li>Llama identifies the missing check. The current failure forces a new trial.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 1; full record in source guide.</a></div>
<span class="pageno">35 / 80</span></div>

<!--
Read the exact reason. The model was offered VERIFY_SAC_FIRST or REVIEW. The application then checks the saved SAC action in OpenDSS. 111.966607% refers to the allowed current, which was 80% of nominal, so this exceeds the configured allowance. The numerical result records two current violations. This P3 full supplied MV/LV study is separate from L2 and L3 test_01. Ask the audience to predict the next allowed step before advancing. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.
Takeaway: 
Nominal duration: 2.5 minutes.

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

<div class="eyebrow">Recorded agent example · separate P3 study</div>
<h1>Voltage: Llama chooses the existing fallback plan</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_2.png" alt="Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later." style="max-height:380px;height:auto"><figcaption>Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.</figcaption></figure></div><ul><li>Llama chooses an existing MPC plan. Python checks whether the result passes.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 2; full record in source guide.</a></div>
<span class="pageno">36 / 80</span></div>

<!--
The model selects USE_MPC_PLAN from two allowed choices, the other being REVIEW. It does not invent or solve MPC. The recorded context already supplies a plan and its eligibility. The application performs a fresh numerical check at that historical time. The result is just below the allowed current threshold. No operating permission follows from this check alone. Ask which evidence, rather than wording, makes the fallback eligible for review. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.
Takeaway: 
Nominal duration: 2.5 minutes.

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

<div class="eyebrow">Recorded agent example · separate P3 study</div>
<h1>Voltage: the checks pass and human review remains</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_3.png" alt="Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later." style="max-height:380px;height:auto"><figcaption>Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.</figcaption></figure></div><ul><li>Human review remains pending. The fixed script returned the same numerical result.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 3; full record in source guide.</a></div>
<span class="pageno">37 / 80</span></div>

<!--
Read the exact REVIEW_EVIDENCE choice and distinguish it from the overall status. The proposed controls are 2387.157 kW and +325.738 kvar. The supplied full MV/LV feeder check returned voltage 1.001783–1.035026 p.u. and zero listed violations. The fixed supervisor used the same SAC-to-MPC sequence with identical numerical output. Recorded workflow intervals were 0.346053 s fixed and 3.110454 s agentic, excluding precomputed MPC/SAC preparation. These are single recorded timings, not performance distributions or a measured reduction in operator workload. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation. End-of-case partner check: L2 makes new proposals; L3 shows old replies; L4–L5 run new checks on test_01. Report the inputs, proposal, model coverage and result before naming the next step. Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates an MPC plan and a saved-policy proposal for the current classroom inputs. L3 displays old model replies. L4 runs new checks of the selected trials; L5 checks the original archived plan and its model coverage. Numerical tools provide the physical evidence. The old model choices select a permitted trial; they do not replace these checks. The operator receives an advisory record whose stated coverage must match the request. The three P3 previews are an additional separate archive. Contrast their saved Llama decisions with your current direct function calls.
Takeaway: 
Nominal duration: 2.5 minutes.

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

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Restoration: open L6</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_fault_map.svg" alt="Six-node active-power teaching graph with whole-load pickup and one unavailable branch." style="height:305px;max-height:305px"><figcaption>Six-node active-power teaching graph with whole-load pickup and one unavailable branch.</figcaption></figure><ul><li>Use the six-node teaching graph. Keep the faulted branch unavailable.</li><li>Compare total restored load with restored critical load.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">38 / 80</span></div>

<!--
This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks. A tie is an alternative connection that can supply load; CAPACITIES_KW sets its transfer limit in kilowatts.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Choose the service goal before the plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_priority.svg" alt="Different service goals can select different loads on the same network." style="height:305px;max-height:305px"><figcaption>Different service goals can select different loads on the same network.</figcaption></figure><ul><li>The priority goal gives more weight to two critical loads.</li><li>The comparison goal serves the most total kW, using the same network and pickup rules.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">39 / 80</span></div>

<!--
Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective is the service goal encoded as a score. The priority score gives more weight to these critical loads, while the comparison score maximizes total kW. The difference in selected service comes from that goal. Both numerical methods use the same graph, capacities and whole-load pickup rules. Neither needs a language model to solve this declared problem.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Run L6: change the tie capacity</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.</p><pre class="teaching-code">CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings[&#x27;L6 fresh MILP sweep + independent enumeration&#x27;] = time.perf_counter() - started
display(restoration[&#x27;table&#x27;].drop(columns=&#x27;pickup&#x27;))</pre><ul><li>Run all of L6. MILP chooses whole loads; an exhaustive search checks its priority score.</li><li>Read served_kw, critical_kw and MILP_matches_exhaustive_check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">40 / 80</span></div>

<!--
MILP means mixed-integer linear programming. Here it is a whole-load chooser: on/off choices decide which load blocks are served, while linear constraints enforce the stated network rules. Start with tie capacities of 40, 60, 80, 100 and 120 kW. The solver enforces active-power balance, capacity limits, connection to a source, no loops in the energized graph, and exclusion of the faulted branch. An independent exhaustive search checks the priority score on this small graph. Agreement supports this formulation; it does not check the AC physics left out of the model.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Read both service plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_plot.png" alt="Reference L6 plots; rerun L6 to compare your chosen tie capacities." style="max-height:345px;height:auto"><figcaption>Reference L6 plots; rerun L6 to compare your chosen tie capacities.</figcaption></figure></div><ul><li>Left: total load served in kW. Right: critical load served in kW.</li><li>Overlapping markers mean the two plans give the same result at that tested capacity.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">41 / 80</span></div>

<!--
The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>The tradeoff at a 40 kW tie limit</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_table.png" alt="Reference L6 results at a 40 kW tie limit: compare total and critical load served." style="max-height:345px;height:auto"><figcaption>Reference L6 results at a 40 kW tie limit: compare total and critical load served.</figcaption></figure></div><ul><li>Priority goal: 130 kW total, including 90 kW of critical load.</li><li>Most-total-kW goal: 140 kW total, including 30 kW of critical load.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">42 / 80</span></div>

<!--
Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>How Python checks the plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_verify.svg" alt="Python checks the stated graph constraints, then compares the priority score independently." style="height:305px;max-height:305px"><figcaption>Python checks the stated graph constraints, then compares the priority score independently.</figcaption></figure><ul><li>Check paths to a source, capacity limits, power balance and the faulted branch.</li><li>Then compare the MILP service score with the independent exhaustive search.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">43 / 80</span></div>

<!--
Numerical checks and same-content evidence matching answer different questions. A record can match the inputs exactly while still omitting AC voltage, reactive-power or protection limits. Comparing the MILP score with every permitted plan is an independent check of this small stated problem. Minimizing energized branches does not calculate the number or order of physical switching steps.
Takeaway: 
Nominal duration: 2 minutes.

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

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Exercise 2: add more tie capacity</h1>
<div class="content"><pre class="source-excerpt">CAPACITIES_KW = (40., 60., 80., 100., 120., 180.)</pre><ul><li>Add 180. to CAPACITIES_KW, keeping 40. first. Predict, then rerun L6.</li><li>Compare total and critical load served at 40 and 180 kW.</li><li>At which of these two capacities do the service goals give the same result?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">44 / 80</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Debrief: the tradeoff disappears here</h1>
<div class="content"><p class="callout">250 kW total / 90 kW critical</p><ul><li>At 180 kW, both methods serve 250 kW total and 90 kW of critical load.</li><li>Priority helps in the constrained case. It does not improve every case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">45 / 80</span></div>

<!--
Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Reset the capacity list, then run L7</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.</p><pre class="teaching-code">rest_record = restoration[&#x27;records&#x27;][0][&#x27;weighted&#x27;]
rest_request = {&#x27;task&#x27;: &#x27;restoration&#x27;, &#x27;capacity_kw&#x27;: CAPACITIES_KW[0],
                &#x27;critical_nodes&#x27;: [2, 5], &#x27;model&#x27;: &#x27;six_node_active_transport&#x27;, &#x27;revision&#x27;: 1}</pre><ul><li>Restore the original CAPACITIES_KW list and rerun L6.</li><li>L7 checks the first 40 kW record, then changes the request to 20 kW.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">46 / 80</span></div>

<!--
Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Read the evidence-match test</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L7_binding.png" alt="Reference L7 output: changed request, unchanged evidence, so a new check is needed." style="max-height:345px;height:auto"><figcaption>Reference L7 output: changed request, unchanged evidence, so a new check is needed.</figcaption></figure></div><ul><li>Original request: True. Changed rating with the old evidence: False.</li><li>HOLD the old recommendation and request a new solve.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">47 / 80</span></div>

<!--
This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Changed inputs need a new check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_stale.svg" alt="L7 changes capacity and revision; extra topology labels are teaching examples." style="height:305px;max-height:305px"><figcaption>L7 changes capacity and revision; extra topology labels are teaching examples.</figcaption></figure><ul><li>“The evidence is old” does not mean “the changed plan fails its limits.”</li><li>Update the request, solve and check it, then match the new evidence to that request.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">48 / 80</span></div>

<!--
Evidence binding asks whether a record matches the exact request, proposed plan and returned result. The diagram’s extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision; students do not change topology in that cell. Old evidence is unusable for a changed request even if the old plan might still pass its limits. Ask which new numerical check would establish that for the changed request.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Proposed agent role: keep the service goal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_plan.svg" alt="Proposed agent responsibilities; the current notebook cell runs Python." style="height:305px;max-height:305px"><figcaption>Proposed agent responsibilities; the current notebook cell runs Python.</figcaption></figure><ul><li>This cell runs Python: the operator sets the goal and limits; MILP chooses the whole loads.</li><li>A proposed agent would request that solve and explain the returned tradeoff.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">49 / 80</span></div>

<!--
This is a proposed role for an agent, not a new model decision in the default notebook. The current supervisor is ordinary Python. A future language-model agent could request the allowed solve and explain the returned tradeoff. It must preserve the operator’s service goal and limits, rather than quietly changing weights or making up load values. A different service goal requires an explicit new request and solve. The numerical difference here comes from the optimization objective.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>What this model does not check</h1>
<div class="content"><ul><li>This active-power graph does not check AC voltage, reactive power or protection.</li><li>The energized branches do not give the order of field switching steps.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">50 / 80</span></div>

<!--
State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Recorded agent example · separate feeder study</div>
<h1>Restoration: Llama chooses a useful new trial</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_14.png" alt="Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later." style="max-height:380px;height:auto"><figcaption>Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.</figcaption></figure></div><ul><li>The new trial serves more load, keeps critical service and passes the current check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 14; full record in source guide.</a></div>
<span class="pageno">51 / 80</span></div>

<!--
Switch L10B to restoration. This is the separate L10 feeder-catalog restoration study, not the L6 six-node MILP. The recorded protocol requires a first refinement but Llama chooses between the offered fractions. SHED_075 disconnects 75% of the ordered noncritical load objects, not 75% of load kW. The exact reason calls improvement a possibility. Python evaluates the trial and finds improved service while the tie loading remains 91.867215% of its allowance. A useful hypothesis becomes evidence only after that check. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.
Takeaway: 
Nominal duration: 2.5 minutes.

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

<div class="eyebrow">Recorded agent example · separate feeder study</div>
<h1>Restoration: the next trial crosses the current limit</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_15.png" alt="Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later." style="max-height:380px;height:auto"><figcaption>Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.</figcaption></figure></div><ul><li>The next trial fails the current limit. Keep the previous passed candidate.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 15; full record in source guide.</a></div>
<span class="pageno">52 / 80</span></div>

<!--
Keep the actual returned reason visible. It refers to a target in the objective, but its claim should not be accepted as a proved fact. In this record the next trial is numerically rejected for a thermal failure. Restoring more load does not make a failed current check acceptable. Ask participants to explain why the previous passed candidate must remain in the case record. The model’s trial budget is bounded. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.
Takeaway: 
Nominal duration: 2.5 minutes.

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

<div class="eyebrow">Recorded agent example · separate feeder study</div>
<h1>Restoration: catch Llama’s wrong ranking</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_16.png" alt="Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later." style="max-height:380px;height:auto"><figcaption>Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.</figcaption></figure></div><ul><li>The returned order is wrong. Python chooses the smaller cost and rechecks the plan.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 16; full record in source guide.</a></div>
<span class="pageno">53 / 80</span></div>

<!--
Let pairs answer before discussing the result. Smaller cost is better, so E03 must rank before E02. Llama returns [E02,E03] while its explanation claims lowest score first. The recorded language_order_agrees_with_cost field is False. A deterministic guard retains E03 and rechecks it as E05, with no recorded failures. Human acknowledgment and dispatch remain False. The paired fixed workflow reaches the same final action and cost. This example motivates verification rather than an unsupported superiority claim. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation. End-of-case partner check: At 40 kW, explain 130 total / 90 critical versus 140 total / 30 critical, all in kW. For a changed request, keep HOLD until evidence for the current request is available. Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation. Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.
Takeaway: 
Nominal duration: 2.5 minutes.

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

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Cyber: open L8</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_network.svg" alt="Four-bus linear DC teaching model; known synthetic truth is used only for offline comparison." style="height:305px;max-height:305px"><figcaption>Four-bus linear DC teaching model; known synthetic truth is used only for offline comparison.</figcaption></figure><ul><li>Use the separate four-bus DC model and its supplied readings.</li><li>Compare a residual alarm, which checks fit, with error against the known teaching truth.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">54 / 80</span></div>

<!--
The separate four-bus linear DC model has three unknown voltage angles, measured relative to a reference bus, and eight readings. This DC approximation is not a full AC estimator, malware detector or sensor-authentication system. Synthetic truth is known for the offline classroom comparison only. A residual checks how well the estimate fits the supplied readings; state error checks how far the estimate is from the known teaching truth.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Best fit and true state are different</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_residual.svg" alt="A good fit to readings does not show that those readings are authentic." style="height:305px;max-height:305px"><figcaption>A good fit to readings does not show that those readings are authentic.</figcaption></figure><ul><li>WLS finds the best fit to readings, giving more weight to lower stated uncertainty.</li><li>Residual J measures fit mismatch. State error uses teaching truth unavailable to an operator.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">55 / 80</span></div>

<!--
WLS means weighted least squares: find the state that best fits the readings, giving more influence to readings with smaller stated uncertainty. That weighting does not authenticate a reading. Here J is the residual mismatch statistic, not the voltage case’s penalty score. Its chi-square alarm threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. An operator does not have the synthetic truth used to calculate the plotted state error. A small J does not establish that the readings are authentic.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Run L8: compare two data attacks</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings[&#x27;L8 fresh WLS attack sweep&#x27;] = time.perf_counter() - started
display(cyber[&#x27;table&#x27;])</pre><ul><li>Run all of L8 with its default scale list.</li><li>Compare one biased reading with the coordinated Hc shift in the table and plots.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">56 / 80</span></div>

<!--
L8 runs new WLS calculations. An isolated bias changes one reading. The coordinated Hc shift changes readings in a pattern consistent with a different modeled state. This counterexample assumes knowledge of the linear measurement matrix H and access to the modeled unprotected channels. It is a declared defensive teaching model, not evidence of an incident at a utility.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Read both cyber plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L8_plot.png" alt="Reference L8 plots; rerun L8 to calculate results for your chosen attack scales." style="max-height:345px;height:auto"><figcaption>Reference L8 plots; rerun L8 to calculate results for your chosen attack scales.</figcaption></figure></div><ul><li>Left: residual J and its alarm threshold. Right: error against the known teaching truth.</li><li>Follow the coordinated curve across both plots before calling a quiet alarm reassuring.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">57 / 80</span></div>

<!--
The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>At scale 1, the alarm misses a state error</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_stealth.svg" alt="Simple consistency illustration; the numerical values come from the eight-reading L8 model." style="height:305px;max-height:305px"><figcaption>Simple consistency illustration; the numerical values come from the eight-reading L8 model.</figcaption></figure><ul><li>One biased reading: J about 277.50, so the residual alarm is True.</li><li>Coordinated Hc: J about 3.92, no alarm, but state error is about 0.02678 rad.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">58 / 80</span></div>

<!--
The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace. The state error is measured in radians; it is available here because this is an offline test with known synthetic truth.
Takeaway: 
Nominal duration: 2 minutes.

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

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Exercise 3: add a small isolated bias</h1>
<div class="content"><pre class="source-excerpt">ATTACK_SCALES = (0., .10, .25, .5, 1., 1.5)</pre><ul><li>Add .10 to ATTACK_SCALES. Predict, then rerun L8.</li><li>At scale 0.10, read J, the alarm flag and the error against known teaching truth.</li><li>Does “no alarm” mean the reading is correct? Use both plots to explain.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">59 / 80</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Debrief: no alarm does not prove truth</h1>
<div class="content"><p class="callout">10.14 &lt; 15.09 → no residual alarm</p><ul><li>At scale 0.10, the isolated-bias J is about 10.14, below the 15.09 threshold.</li><li>A small bias can miss the threshold. A coordinated shift can preserve the fit.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">60 / 80</span></div>

<!--
Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Reset L8 before the recovery example</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)</pre><ul><li>Restore the original ATTACK_SCALES list and rerun L8.</li><li>L9 uses a fixed recovery case, separate from the scale you changed.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">61 / 80</span></div>

<!--
Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>L9 uses a fixed recovery case</h1>
<div class="content"><ul><li>Check the same case with and without replacement readings assumed to be trusted.</li><li>Its control value does not follow your L8 scale change.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">62 / 80</span></div>

<!--
The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Trusted readings are an assumption</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_trusted.svg" alt="Three trusted angle readings are assumed, not authenticated by this calculation." style="height:305px;max-height:305px"><figcaption>Three trusted angle readings are assumed, not authenticated by this calculation.</figcaption></figure><ul><li>The example assumes three independent angle readings are trustworthy.</li><li>The residual check and a model’s explanation cannot authenticate those readings.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">63 / 80</span></div>

<!--
The example assumes three protected angle readings determine the three unknown angles, leaving zero residual degrees of freedom. Independent trusted information must come from a justified source outside this numerical calculation. A zero residual in this exactly determined system adds no detection guarantee. Neither a good model fit nor a language-model explanation establishes authenticity.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Run L9: compare HOLD and PROPOSE</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.</p><pre class="teaching-code">without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)</pre><ul><li>Run the whole L9 cell, including its assertions.</li><li>Read status first, then the proposed injection and the offline limit-violation count.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">64 / 80</span></div>

<!--
The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Read the two decision states</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L9_trust.png" alt="Reference L9 output for the fixed recovery case, not the edited L8 scale." style="max-height:325px;height:auto"><figcaption>Reference L9 output for the fixed recovery case, not the edited L8 scale.</figcaption></figure></div><ul><li>No trusted replacement readings: HOLD, with no proposed injection.</li><li>Trusted readings assumed: PROPOSE; u ≈ 0.121694 p.u.; zero offline toy-model violations.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">65 / 80</span></div>

<!--
Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Check the numerical correction</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_qp.svg" alt="Fixed L9 correction: compare the predicted branch flow with the offline truth check." style="height:305px;max-height:305px"><figcaption>Fixed L9 correction: compare the predicted branch flow with the offline truth check.</figcaption></figure><ul><li>The QP solver minimizes effort, subject to branch limits and a 0.01 p.u. margin.</li><li>Predicted flow12: 0.17000; offline actual: about 0.17046, below the 0.18000 rating.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">66 / 80</span></div>

<!--
QP means quadratic programming: this numerical solver minimizes a quadratic effort score while enforcing the declared branch limits and a 0.01 p.u. margin. The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. Predicted flow12 is 0.17000 p.u.; the offline actual flow is about 0.17046 p.u., below the 0.18000 p.u. rating. The actual-flow comparison uses synthetic truth for this fixed case. It does not guarantee AC behavior omitted by the model or trustworthy field telemetry.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>What makes the recovery possible?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_handoff.svg" alt="Trusted information and numerical checks have separate roles." style="height:305px;max-height:305px"><figcaption>Trusted information and numerical checks have separate roles.</figcaption></figure><ul><li>Assumed trusted readings support the estimate. The solver calculates a limited correction.</li><li>The explanation must keep those conditions clear and leave the proposal for review.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">67 / 80</span></div>

<!--
Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Recorded agent example · separate recovery study</div>
<h1>Cyber: Llama selects the tool already allowed</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_7.png" alt="Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later." style="max-height:380px;height:auto"><figcaption>Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later.</figcaption></figure></div><ul><li>The task supplies the tool and trust assumption. Python computes the correction.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: cyber replay, recorded call 7; full record in source guide.</a></div>
<span class="pageno">68 / 80</span></div>

<!--
Switch L10B to cyber. This standard four-bus DC record is separate from L10’s proposal-complete cyber record, and matches the Agent Trace notebook T6 archive. The route is narrow: the prompt already authorizes the tool and supplies the trusted-sensor assumption. The three angle readings give full rank but zero residual redundancy, so a good fit is not an independent trust test. u is the flexible injection correction in per unit. Offline synthetic-truth flow is available to the experimenter, not guaranteed available to a real operator. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.
Takeaway: 
Nominal duration: 2.5 minutes.

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

<div class="eyebrow">Recorded agent example · separate recovery study</div>
<h1>Cyber: a passing calculation still needs review</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_8.png" alt="Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later." style="max-height:350px;height:auto"><figcaption>Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later.</figcaption></figure></div><ul><li>Keep REVIEW visible. The operator must resolve the trust assumption and missing checks.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: cyber replay, recorded call 8; full record in source guide.</a></div>
<span class="pageno">69 / 80</span></div>

<!--
Read the actual reply, including the REVIEW choice. Numerical verification is PASS, but the overall result remains REVIEW and human acknowledgment is PENDING. The fixed comparator obtains the same numerical state estimate and correction without Llama. This replay demonstrates permitted tool routing and a report decision. It does not demonstrate better estimation, authenticated measurements, AC network security or operating authority. Run L11 with the default False setting, then proceed to L12. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation. End-of-case partner check: Report the trust assumption, model, proposed u and the checks that passed or failed. Without independent trusted information, keep HOLD and name what is missing. Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.' Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.
Takeaway: 
Nominal duration: 2.5 minutes.

Full sources:
Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L10 · classroom-028</div>
<h1>Run L10 before the Llama walkthrough</h1>
<div class="content"><ul><li>Run L10 to inspect its separate archived five-stage study.</li><li>Continue to L10B for the recorded Llama choices, then run L11 with its default False setting.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.</a></div>
<span class="pageno">70 / 80</span></div>

<!--
L10 reads the archived proposal_complete_workflow study. It includes feeder-catalog restoration and is separate from the L6 six-node MILP and your edited classroom inputs. L10B, inserted immediately after L10, then gives readable verified replay episodes for all three cases. Run L11 after those replays; the default False setting skips a new local model request.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L10B · classroom-llama-walkthrough</div>
<h1>Run L10B: watch Llama choose a tool</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L10B (classroom-llama-walkthrough), source lines 1–5.</p><pre class="teaching-code">SCENARIO = &quot;voltage&quot;  # Change to &quot;restoration&quot; or &quot;cyber&quot;, then rerun this cell.
from IPython.display import HTML, display
from src.llama_walkthrough import load_episodes, render_episode_html
replay_episodes = load_episodes(ROOT)
display(HTML(render_episode_html(replay_episodes[SCENARIO])))</pre><ul><li>Now replay the three saved episodes: set SCENARIO to voltage, restoration and cyber, rerunning each time.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10B; cell classroom-llama-walkthrough; src/llama_walkthrough.py.</a></div>
<span class="pageno">71 / 80</span></div>

<!--
Run L10 first. In the new L10B cell the helper validates the original JSON reply against the parsed journal and trace, then displays the recorded episode. Change only SCENARIO to inspect the other two episodes. Earlier case slides previewed selected fields from these replays. Now inspect the full episodes in the same notebook. This cell makes no model request and performs no new electrical solve. At the end, run L11 at its default False setting before L12. Llama reasons are historical public returned text. Their correctness must be judged against the input and tool results. SCENARIO can be voltage, restoration or cyber. The full cell is shown. Allow about two minutes per scenario: one partner identifies the model choice, the other finds its tool result and the unresolved operator decision. These additional minutes replace removed checkpoint slides and the longer source explanations.
Takeaway: 
Nominal duration: 6.5 minutes.

Full sources:
Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.
Full source: https://docs.ollama.com/capabilities/structured-outputs
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L12 · classroom-033</div>
<h1>Finish L12: practice the readback</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.</p><pre class="teaching-code">wrong_id = lab.acknowledge(mv_scope, &#x27;wrong-id&#x27;, &#x27;Student operator&#x27;)
readback = lab.acknowledge(mv_scope, mv_scope[&#x27;recommendation_id&#x27;], &#x27;Student operator&#x27;)</pre><ul><li>Run all of L12 after completing L0–L11 in notebook order.</li><li>Check wrong-ID rejection, simulated acknowledgment and equipment_dispatch=False.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">72 / 80</span></div>

<!--
This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record. Readback means repeating the recommendation ID and conditions so the acknowledgment can be matched to the same proposal. In this exercise it is simulated. Check the wrong-ID rejection, the correct simulated acknowledgment and equipment_dispatch=False.
Takeaway: 
Nominal duration: 5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs / L12 / simulated readback</div>
<h1>Read the two readback outcomes</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L12_packet.png" alt="Reference L12 output. Run L12 here, after the three cases and the L10B replay." style="max-height:345px;height:auto"><figcaption>Reference L12 output. Run L12 here, after the three cases and the L10B replay.</figcaption></figure></div><ul><li>Full MV/LV request: HOLD. The explicit MV teaching request allows a simulated readback.</li><li>A wrong recommendation ID is rejected. equipment_dispatch stays False.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">73 / 80</span></div>

<!--
After running the complete L12 cell, compare these reference outputs with your own. The full MV/LV request remains HOLD because the checked model covers only MV phases. An explicit MV teaching request can pass the simulated readback after the recommendation ID matches. The wrong-ID attempt is rejected. Acknowledgment records a classroom review step and does not operate equipment.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Llama chooses; tools calculate; people decide</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_roles_simple.svg" alt="Our grid teaching adaptation of the language/checking distinction in Stanford Lecture 1, p.53." style="height:350px;max-height:350px"><figcaption>Our grid teaching adaptation of the language/checking distinction in Stanford Lecture 1, p.53.</figcaption></figure><ul><li>The agent coordinates a study. Numerical tools supply the checks. The operator reviews the proposal.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53.</a></div>
<span class="pageno">74 / 80</span></div>

<!--
Use the three symbols to assign responsibilities: the speech box is Llama making a permitted choice and returning a public reason; the function is Python and OpenDSS calculating physical results and enforcing workflow limits; the person is the operator reviewing evidence and retaining operating authority. The Llama wrappers use constrained JSON interpreted by the application, rather than native tool_calls. Language explanations are not proof of physical correctness. In our replay the model may say REVIEW but the human acknowledgment is still PENDING. For each exercise work in pairs: one person runs while the other checks, then swap. Save the input, result, check and next decision. Stanford p.53 separates language understanding from checking a formal decision model in a clinical-trial example. The lab adaptation separates Llama coordination from Python numerical checks and operator review. This lab does not run SMT or MaxSAT, and the analogy supplies no formal guarantee about the grid model. This role reminder now introduces the closing advisory-pilot discussion, after the L12 readback.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.
Full source: https://docs.ollama.com/capabilities/structured-outputs
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Start a control-room pilot with a clear study request</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_request_snapshot.svg" alt="Proposed advisory pilot — teaching design. F12 is an illustrative identifier." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. F12 is an illustrative identifier.</figcaption></figure><ul><li>Use an approved copy of the network data with a time stamp, topology version and limits.</li><li>If required data are missing or too old, return HOLD and name the missing information.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.6028/NIST.SP.800-82r3">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">75 / 80</span></div>

<!--
Proposed advisory pilot, not a deployment claim. F12 is an illustrative teaching feeder name. Read the study request aloud: compare the allowed voltage-support options, keep the stated current and voltage limits, show the worst margins and missing checks, and return a recommendation for review. The data owner defines acceptable age, source and quality rules. L1 and L7 illustrate matching inputs to results, but hashes alone do not authenticate those sources.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Give the assistant a small, controlled tool list</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_tool_boundary.svg" alt="Proposed advisory pilot — teaching design. Classroom functions are not live control-room interfaces." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. Classroom functions are not live control-room interfaces.</figcaption></figure><ul><li>An approved interface supplies read-only data and study tools. Log every request and result.</li><li>Keep equipment commands in the utility’s separate authorized operating process.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.6028/NIST.SP.800-82r3">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">76 / 80</span></div>

<!--
Proposed advisory pilot. Walk through the lanes: operator, assistant, application-controlled tool gateway and engineering tools. Llama requests one permitted function; the application checks the request and executes the tool. A snapshot identifier binds the result to the input. The workshop Python functions are teaching counterparts, not SCADA adapters. NIST OT guidance supports controlled information flows, least privilege and logging. The exact pilot architecture is our teaching recommendation, not a NIST-certified design.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.
Full source: https://docs.ollama.com/capabilities/structured-outputs

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Check three things before returning a proposal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_three_gates.svg" alt="Proposed advisory pilot — teaching design. A PASS is limited to its tested model and inputs." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. A PASS is limited to its tested model and inputs.</figcaption></figure><ul><li>Check that the inputs match, the required limits pass and the required network parts were modeled.</li><li>Example: an MV-only PASS stays on HOLD when the request requires the full MV/LV network.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">77 / 80</span></div>

<!--
Proposed advisory pilot. Current data and a matching evidence packet are the first gate. The second gate checks stated engineering limits with approved tools. The third asks whether the calculations cover the request, including excluded low-voltage parts or required protection and dynamic studies. This is not a universal complete security checklist. It illustrates why L12 can produce a passing local calculation and still HOLD a broader request. Make missing evidence visible instead of allowing fluent text to fill the gap.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Give the operator a short evidence packet</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_review.svg" alt="Proposed advisory pilot — teaching design. Review of a study is distinct from operating equipment." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. Review of a study is distinct from operating equipment.</figcaption></figure><ul><li>Show the input snapshot, selected option, worst margins, rejected trials and missing checks.</li><li>The reviewer can ask for another study, reject the proposal or accept it for the next review step.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">78 / 80</span></div>

<!--
Proposed advisory pilot. Use three review questions: Does this match the current equipment, inputs and model? Did the required checks pass, with missing checks clear? What exactly am I approving, who owns the next step, and where is the record? Record the reviewer, reason, case snapshot and tool versions. Accepting a study result does not itself issue an equipment command. Authorized operating procedures and roles determine any later physical action. L12 practices only a simulated ID-bound readback.
Takeaway: 
Nominal duration: 4 minutes.

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

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>Adopt it in stages and measure the benefit</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_pilot.svg" alt="Proposed advisory pilot — teaching design. Benefits must be measured against an appropriate baseline." style="height:330px;max-height:330px"><figcaption>Proposed advisory pilot — teaching design. Benefits must be measured against an appropriate baseline.</figcaption></figure><ul><li>Begin with past cases, then read-only shadow work, then a limited pilot with named reviewers.</li><li>Compare against the same tools in a fixed script: correct studies, missed checks, time and rework.</li></ul></div>
<div class="sources">Source: <a href="https://doi.org/10.6028/NIST.AI.100-1">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">79 / 80</span></div>

<!--
Proposed advisory pilot. Historical replay lets engineers define expected outcomes and failure cases. Shadow use compares recommendations alongside the existing process without relying on them for equipment control. A limited pilot needs a named owner, training, an agreed scope and a way to stop use. Measure end-to-end elapsed time including review, correct completed studies, missed or stale inputs, overlooked limits and reviewer changes. Compare the same engineering tools with and without Llama. Our paired records show identical final numerical results, so there is no basis yet to promise higher accuracy, less operator workload or faster decisions. NIST AI RMF supports human roles, evaluation under realistic conditions and deactivation; these particular pilot metrics are our recommendation.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.
Full source: https://doi.org/10.6028/NIST.AI.100-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json
-->

---
transition: none
---

<div class="lesson teaching rigorous closing-slide closing">

<h1>Save a workshop record others can repeat</h1>
<div class="content"><p class="activity-link"><a href="https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/downloads/participant-lab-guide.pdf">Get the Participant Lab Guide</a></p><ul><li>Save your changed inputs and results, labeled new, archived or simulated.</li><li>Explain the request, tool call, result, checks and next decision.</li></ul></div>
<p class="reading-link"><a href="/Full_Reading_Guide.html">Open the Full Reading Guide</a></p>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">80 / 80</span></div>

<!--
Use the final three minutes for pair reports and saving. Each pair names one changed parameter, compares its predicted and observed result, and states one evidence limit. Another person should be able to repeat the experiment from the saved notebook. The reading guide supplies the full source links, stable cell map and debrief answers.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->
