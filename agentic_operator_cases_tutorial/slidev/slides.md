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

<h1>Hands-on:<br>Three Operator Cases</h1>
<p>One notebook. Three operator problems.</p>
<p>90 minutes / three short exercises</p>
<div class="presenters"><div><strong>Alaa Selim</strong><span>MIT/Dartmouth</span></div><div><strong>Mohamed Chehada</strong><span>UT Austin</span></div></div>
<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup"><small>Independent educational material · IEEE ComSoc theme adaptation</small>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">1 / 80</span></div>

<!--
**Say**

We will use one notebook to study three operator problems: voltage support, restoring service and suspicious measurements. For each case, we will look at the input, run a tool, read the result and decide what still needs review. You can follow along now or finish the experiments later. The notebook does not control equipment.

**Show**

Point to the three case names and the one-notebook route.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
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

<h1>What is agentic AI?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_goal_loop.svg" alt="Teaching diagram. Llama choices are saved; Python calculations can run now." style="height:350px;max-height:350px"><figcaption>Teaching diagram. Llama choices are saved; Python calculations can run now.</figcaption></figure><ul><li>An AI agent chooses a tool, reads its result and chooses the next step toward a goal.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.</a></div>
<span class="pageno">2 / 80</span></div>

<!--
**Say**

Here, agentic AI means a model can choose a permitted next step using a tool's returned result. The important part is that the result can change the next choice. The model still works within limits set by the application. In our default lab, Python runs now while the Llama choices come from saved recordings.

**Show**

Trace goal, model choice, tool result and feedback arrow.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

Which component supplies the electrical numbers?

**Answer**

The numerical tool; the model selects an allowed next step.
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

<h1>A tool call and an agent workflow</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_agentic_capabilities.png" alt="Source figure, p.2. Function calling and a multi-step workflow." style="max-height:330px;height:auto"><figcaption>Source figure, p.2. Function calling and a multi-step workflow.</figcaption></figure></div><ul><li>A tool call does one job. An agent links jobs using the returned results.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.</a></div>
<span class="pageno">3 / 80</span></div>

<!--
**Say**

A tool call is one job, such as calculating a power flow. A workflow connects several jobs. In an agentic step, the model helps choose what happens next. A fixed program can also contain loops and checks, so a loop alone does not make a system agentic. Look for the actual model decision.

**Show**

Point to the single-call panel, then the multi-step panel.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
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

<div class="lesson teaching rigorous figure-slide">

<h1>Evidence before an answer</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_wikichat_steps.png" alt="Source figure, p.19. WikiChat checks claims before writing." style="max-height:350px;height:auto"><figcaption>Source figure, p.19. WikiChat checks claims before writing.</figcaption></figure></div><ul><li>WikiChat checks claims before writing. Our lab checks numbers before reporting a result.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.19.</a></div>
<span class="pageno">4 / 80</span></div>

<!--
**Say**

This source example is about checking claims before writing an answer. We use the same design habit in a grid study: calculate first, then explain the returned numbers. We are borrowing the idea, not running WikiChat in this notebook. A fluent report should never replace an electrical check.

**Show**

Follow checking before drafting in the source figure.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
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
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Lab preview: L2</div>
<h1>Voltage: propose, then check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_voltage.svg" alt="Teaching adaptation. L2 runs Python; L10B replays saved model choices." style="height:340px;max-height:340px"><figcaption>Teaching adaptation. L2 runs Python; L10B replays saved model choices.</figcaption></figure><ul><li>L2 calculates and checks proposals. L10B shows saved Llama tool choices.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.19; Classroom Labs L2.</a></div>
<span class="pageno">5 / 80</span></div>

<!--
**Say**

For voltage, a controller proposes settings and an electrical model checks their effects. L2 lets us run those calculations ourselves. Later, L10B shows a saved Llama choice about which existing tool to use. Keep those two activities separate: a new calculation is different from replaying an old model reply.

**Show**

Point to the proposal, electrical check and returned current value.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
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

<div class="lesson teaching rigorous figure-slide">

<h1>Clear rules for tool use</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_genie_specification.png" alt="Source figure, p.40. Task rules define permitted tool use." style="max-height:315px;height:auto"><figcaption>Source figure, p.40. Task rules define permitted tool use.</figcaption></figure></div><ul><li>Set the inputs, allowed tools, limits and stop rules.</li><li>Python keeps these rules fixed when Llama chooses a step.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40.</a></div>
<span class="pageno">6 / 80</span></div>

<!--
**Say**

A useful tool needs a clear contract: required inputs, allowed operations, fixed limits and a stop condition. The language model cannot quietly change those rules to make an answer look better. In this lab, Python owns the rules. If a required input or check is missing, the workflow must stop or request review.

**Show**

Point to the explicit task-rule specification.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
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

<div class="eyebrow">Lab preview: L6</div>
<h1>Restoration: define the service goal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_restoration.svg" alt="L6: same network and limits, different service goals." style="height:340px;max-height:340px"><figcaption>L6: same network and limits, different service goals.</figcaption></figure><ul><li>The goal changes which loads the solver restores. L6 compares two goals.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40; Classroom Labs L6.</a></div>
<span class="pageno">7 / 80</span></div>

<!--
**Say**

Before asking for a restoration plan, define what good service means. Serving the most total power can give a different answer from protecting critical loads. The solver follows the objective we give it. The agent's job is to preserve that goal when requesting a tool and explaining its result.

**Show**

Compare the critical-service segments, then the total kW.

**Colab: PREVIEW ONLY**

Show the slide only. Run L6 later on slide 40; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
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

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Source example / grid application</div>
<h1>Language and decision checks</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/stanford_language_decision.png" alt="Source figure, p.53. Clinical example using logical constraints, not a power-system model." style="max-height:190px;height:auto"><figcaption>Source figure, p.53. Clinical example using logical constraints, not a power-system model.</figcaption></figure></div><ul><li>The source example turns written facts into constraints for a solver.</li><li>In our lab, Llama requests a study. Python checks it. A person reviews it.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53.</a></div>
<span class="pageno">8 / 80</span></div>

<!--
**Say**

The source figure separates language processing from a solver that checks a decision. Our grid example uses a similar separation: Llama requests a permitted study, Python calculates and checks it, and a person reviews the proposal. Our electrical models are not the logical solvers in this source example and do not inherit their guarantees.

**Show**

Follow language input into a separate checked decision.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
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

<div class="eyebrow">Lab preview: L8–L9</div>
<h1>Cyber: good fit can hide bad data</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_cyber.svg" alt="L8 checks fit. L9 requires a trust assumption before proposing recovery." style="height:340px;max-height:340px"><figcaption>L8 checks fit. L9 requires a trust assumption before proposing recovery.</figcaption></figure><ul><li>L8 tests misleading readings. L9 shows when to return HOLD or a proposal.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53; Classroom Labs L8–L9.</a></div>
<span class="pageno">9 / 80</span></div>

<!--
**Say**

Suspicious readings can fit a model and still be wrong. L8 makes that problem visible by comparing a mismatch alarm with known simulation truth. L9 asks a different question: can we propose a correction if extra readings are assumed trustworthy? The trust condition remains an assumption that the operator must review.

**Show**

Point to the quiet residual and the trust-dependent recovery gate.

**Colab: PREVIEW ONLY**

Show the slide only. Run L8 later on slide 56; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
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

<h1>Four questions about any result</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_review_questions.svg" alt="Teaching adaptation of the cited lecture. The lab uses custom Python." style="height:330px;max-height:330px"><figcaption>Teaching adaptation of the cited lecture. The lab uses custom Python.</figcaption></figure><ul><li>Which tool ran? What did it assume? Which limits passed? What should the operator do next?</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, pp.52–53.</a></div>
<span class="pageno">10 / 80</span></div>

<!--
**Say**

Use these four questions throughout the session. Which tool produced this result? What did the tool assume? Which limits did it actually check? What should the operator do next? These questions help us assess both an ordinary software result and a model-generated explanation. Missing evidence stays missing even when the wording sounds confident.

**Show**

Use the four questions to assess one statement from the opening.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

What evidence is missing from a confident answer with no tool result?

**Answer**

The actual calculated or measured result and its assumptions.
Nominal duration: 1 minutes.

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

<h1>One notebook for all three cases</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_one_notebook.svg" alt="Classroom Labs is the only required notebook." style="height:330px;max-height:330px"><figcaption>Classroom Labs is the only required notebook.</figcaption></figure><p class="activity-link"><a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Open Classroom Labs in Google Colab</a></p><ul><li>Open Classroom Labs and save a copy in Drive. Use it throughout.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">11 / 80</span></div>

<!--
**Say**

Classroom Labs is the only required notebook. Save a copy in Drive so you can keep your changes. The voltage, restoration and cyber sections are in this same file. The other notebooks on the website are companions, so you do not need to open several Colabs to follow this workshop.

**Show**

Open the canonical Classroom Labs link and save a Drive copy.

**Colab: NO NEW RUN**

Open Classroom Labs and save a copy. Run setup on slide 12, not the later lesson cells.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Colab setup</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_ready.svg" alt="Setup first, then L0 and L1." style="height:315px;max-height:315px"><figcaption>Setup first, then L0 and L1.</figcaption></figure><ul><li>Save a copy, connect a CPU and run setup.</li><li>Wait for Ready, then run L0 and L1.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">12 / 80</span></div>

<!--
**Say**

Colab gives us a temporary computer called a runtime. Connect a CPU runtime and run the setup cell once. Wait for Ready before continuing. Saving a notebook keeps the text and saved outputs, not the temporary variables. After a runtime reset, rerun setup and the earlier cells. If setup is still running, follow the reference figures and catch up afterward.

**Show**

Show the CPU connection control and setup-cell play button.

**Colab: RUN**

Connect a CPU. Run the whole setup cell once and wait for Ready.

Exact cells: colab-setup. Run the whole cell, not only the slide excerpt.

**Expected result**

Ready appears; the support files and CPU packages are available.
Nominal duration: 2.5 minutes.

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

<h1>Input, run, output</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_cell_loop.svg" alt="Illustration of a code cell. Run the full L2 cell." style="height:330px;max-height:330px"><figcaption>Illustration of a code cell. Run the full L2 cell.</figcaption></figure><ul><li>Find the L heading and run its whole code cell.</li><li>Read the output below it. After any edit, rerun the cell.</li></ul></div>
<div class="sources">Source: <a href="https://research.google.com/colaboratory/faq.html">Google Colab FAQ; Classroom Labs L2, cell classroom-007.</a></div>
<span class="pageno">13 / 80</span></div>

<!--
**Say**

A notebook cell has input code and an output below it. The slide shows selected lines, but we always run the whole matching code cell. First predict the result, then run it and read what appears. Changing a number does not update an old plot until you rerun the cell.

**Show**

Identify the input, run button and output region.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

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
<h1>L0: keep the default settings</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L0 (classroom-002), source lines 11–14.</p><pre class="teaching-code">RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / &#x27;data/lindistflow3_network.json&#x27;).exists(), &#x27;Start Jupyter in the tutorial folder&#x27;</pre><ul><li>Leave both switches False. Python calculates new results; Llama replies come from saved records.</li><li>If data are missing, rerun setup.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">14 / 80</span></div>

<!--
**Say**

Leave both switches False. OpenDSS is off, so the default voltage calculation uses the three-phase linear model. The local Llama call is also off, so there is no new language-model request. Python still makes new numerical calculations, and the saved SAC policy still proposes a new action from its stored weights.

**Show**

Point to both False settings.

**Colab: RUN**

Run L0 with RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False.

Exact cells: classroom-002. Run the whole cell, not only the slide excerpt.

**Expected result**

The data assertion passes. Both optional live-tool paths remain off.
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L1 · classroom-004</div>
<h1>L1: does the result match the request?</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L1_binding.png" alt="Reference L1 output. Only the unchanged request and command match." style="max-height:345px;height:auto"><figcaption>Reference L1 output. Only the unchanged request and command match.</figcaption></figure></div><ul><li>Read binding_pass. Expect True, False, False.</li><li>Changed inputs or commands need a new check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">15 / 80</span></div>

<!--
**Say**

This small test asks whether the result still belongs to the same request and command. The first row should be True. Changing the load or command gives False. That match is necessary before using an old result. The hash detects a changed record; it does not authenticate a sensor or prove that the physical action is safe.

**Show**

Read the three binding_pass results.

**Colab: RUN**

Run the whole L1 cell after L0.

Exact cells: classroom-004. Run the whole cell, not only the slide excerpt.

**Expected result**

binding_pass is True, False, False in row order.
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Case 1: voltage support</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/feeder.png" alt="Synthetic SMART-DS feeder used for teaching." style="max-height:345px;height:auto"><figcaption>Synthetic SMART-DS feeder used for teaching.</figcaption></figure></div><ul><li>MPC plans ahead. SAC uses a saved learned policy.</li><li>Check limits first. Among passing options, a smaller score J is better.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">16 / 80</span></div>

<!--
**Say**

Our first case compares two ways to propose voltage-support settings. MPC plans using a model and a short forecast. SAC uses a policy learned earlier. We send both proposals through the same electrical check. Only after a proposal passes should we compare its penalty score J. These are teaching results on a synthetic feeder.

**Show**

Locate the voltage case on the synthetic feeder figure.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

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

<h1>Two ways to propose settings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_mpc_sac.svg" alt="MPC = model predictive control. SAC = Soft Actor-Critic." style="height:350px;max-height:350px"><figcaption>MPC = model predictive control. SAC = Soft Actor-Critic.</figcaption></figure><ul><li>MPC plans with a model. SAC proposes from learned weights. Both need the same electrical checks.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">17 / 80</span></div>

<!--
**Say**

MPC calculates settings from the model when we run it. The saved SAC policy quickly maps the current conditions to settings. Neither proposal is automatically acceptable. A separate model checks voltage, current and inverter limits. These numerical controllers are tools inside the workflow; they do not become language agents just because a model can call them.

**Show**

Follow both proposal methods into the same checker.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
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

<div class="eyebrow">Recorded P3 example / separate from the L2 calculation</div>
<h1>A tool result changes the next step</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_recorded_trace.svg" alt="Saved P3 OpenDSS example, separate from L2. Values rounded." style="height:350px;max-height:350px"><figcaption>Saved P3 OpenDSS example, separate from L2. Values rounded.</figcaption></figure><ul><li>The first trial fails. Llama requests the fallback. A passing result goes to human review.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json">Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.</a></div>
<span class="pageno">18 / 80</span></div>

<!--
**Say**

This is a saved P3 example, not the new L2 experiment. Llama first asks to check SAC. The tool returns about 111.97 percent of allowed current, so that trial fails. Llama then requests the existing MPC fallback, which returns about 99.60 percent and passes the recorded checks. Human review still remains pending.

**Show**

Follow the two saved current results in order.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

Why can the fallback enter review?

**Answer**

Its stated numerical checks pass; human acknowledgment is still separate.
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
<h1>Two control settings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_capability.svg" alt="Active and reactive power share the inverter capacity." style="height:305px;max-height:305px"><figcaption>Active and reactive power share the inverter capacity.</figcaption></figure><ul><li>a controls active power. b controls reactive power.</li><li>Check inverter capacity, voltage and line current.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">19 / 80</span></div>

<!--
**Say**

There are two control settings. The active-power setting changes how much real power the inverter supplies. The reactive-power setting changes reactive support. They share the inverter's capacity, so changing one affects the room available for the other. The numerical checker tests that capacity together with voltage and line-current limits.

**Show**

Point to active and reactive settings and their shared capacity.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A tool is a callable function</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_python_tool.svg" alt="L2 calls lab.voltage_lab directly. Agent coordination is shown in the saved study." style="height:350px;max-height:350px"><figcaption>L2 calls lab.voltage_lab directly. Agent coordination is shown in the saved study.</figcaption></figure><ul><li>Inputs go in. Calculations run. Results come back. L2 calls this Python function directly.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">20 / 80</span></div>

<!--
**Say**

In the lab, a tool is an ordinary Python function with defined inputs and returned results. L2 calls voltage_lab directly with load scale and current allowance. That lets us inspect what the tool does without a live LLM. In the saved agent workflow, the application validates a model choice before calling an allowed function.

**Show**

Match function inputs to its returned fields.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

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
<h1>L2: run the default case</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L2 (classroom-007), source lines 1–4.</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)</pre><ul><li>Run all of L2. It checks the MPC plan and the saved SAC policy.</li><li>Read feasible, current_step_J and max_allowed_current_pct.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">21 / 80</span></div>

<!--
**Say**

Run the whole L2 cell with load scale 1.0 and current allowance 0.80. The cell makes an MPC plan, runs the saved SAC actor and checks both proposals. Read feasible first. Then inspect maximum allowed-current use and the score J. The plots and table below the cell are new calculations for these inputs.

**Show**

Show the input lines, then the resulting L2 table.

**Colab: RUN**

Run the full L2 cell at LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

Exact cells: classroom-007. Run the whole cell, not only the slide excerpt.

**Expected result**

Both default proposals pass; current use is about 73.62% for MPC and 51.68% for SAC.
Nominal duration: 3 minutes.

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
<h1>L2: voltage and current plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_plot.png" alt="Reference L2 plots. Rerun for your inputs." style="max-height:345px;height:auto"><figcaption>Reference L2 plots. Rerun for your inputs.</figcaption></figure></div><ul><li>Left: voltages should stay inside the allowed band.</li><li>Right: current use should stay below 100% of the allowance.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">22 / 80</span></div>

<!--
**Say**

Read both plots before choosing a method. The voltage plot shows sorted modeled voltages, not the physical order of buses along a feeder. Check that they remain inside the band. The current plot shows the largest use of the allowed current. Its 100 percent line is a limit, not a performance target.

**Show**

Read the voltage band and current allowance line.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>L2: both default proposals pass</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_table.png" alt="Reference L2: load scale 1.0, current allowance 0.80." style="max-height:345px;height:auto"><figcaption>Reference L2: load scale 1.0, current allowance 0.80.</figcaption></figure></div><ul><li>MPC: 73.62% current use, score J about 0.03110.</li><li>Saved SAC: 51.68% current use, score J about 0.43643.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">23 / 80</span></div>

<!--
**Say**

Both default proposals pass this model. MPC uses about 73.62 percent of the allowed current and has J about 0.03110. SAC uses less current, about 51.68 percent, but has a higher penalty score. Lower current alone does not mean a better overall objective. Compare scores only among proposals that pass the stated checks.

**Show**

Compare feasibility first, then current use and score.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

**Ask**

Does less current always mean a smaller objective?

**Answer**

No. J also includes curtailment, reactive effort and other declared penalties.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>The limit and the calculated result</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_claim_evidence.svg" alt="Example uses the separate saved P3 case." style="height:330px;max-height:330px"><figcaption>Example uses the separate saved P3 case.</figcaption></figure><ul><li>A rule states the limit. A tool checks the proposal against it.</li><li>Keep both with the result so the operator can review it.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, pp.17–25; recorded P3 current check.</a></div>
<span class="pageno">24 / 80</span></div>

<!--
**Say**

A rule tells us what is allowed. A numerical tool tells us whether a particular proposal meets that rule in a particular model. We need both. When reporting a result, keep the input case, the limit and the calculated value together. The number in this illustration comes from the separate saved P3 example.

**Show**

Point separately to the rule and returned value.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
Nominal duration: 0.5 minutes.

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
<h1>Exercise 1: lower the current allowance</h1>
<div class="content"><pre class="source-excerpt">RATING_FRACTION = 0.75</pre><ul><li>In L2, change RATING_FRACTION from 0.80 to 0.75. Predict, then rerun.</li><li>Compare feasible, current use and score J for both methods.</li><li>Does this check cover the whole MV/LV network?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">25 / 80</span></div>

<!--
**Say**

Change only RATING_FRACTION from 0.80 to 0.75 in L2. Before running it, predict how the percentage of allowed current will change. Run the whole cell and compare both methods. Record the pass flag, current percentage and score. Then decide whether this model covers a full medium- and low-voltage request.

**Show**

Show only the one parameter to change.

**Colab: EDIT AND RERUN**

Change only RATING_FRACTION to 0.75. Predict, then rerun all of L2. Give this exercise four minutes.

Exact cells: classroom-007. Run the whole cell, not only the slide excerpt.

**Expected result**

MPC current use is about 78.53%; SAC about 54.85%; both pass this MV test.

**Ask**

Does this PASS cover the whole MV/LV network?

**Answer**

No. The default covers MV phases and currents with ideal LV aggregation.
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Exercise 1: both still pass</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_try_observe.svg" alt="Reference L2 experiment. Both proposals pass at 0.75." style="height:330px;max-height:330px"><figcaption>Reference L2 experiment. Both proposals pass at 0.75.</figcaption></figure><ul><li>A smaller allowance makes the same current a larger percentage.</li><li>At 0.75: MPC uses 78.53%, SAC 54.85%. Both pass this test.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L2, cell classroom-007; verified default and exercise outputs.</a></div>
<span class="pageno">26 / 80</span></div>

<!--
**Say**

A smaller allowance makes the same physical current a larger percentage of the allowance. In this example, MPC reaches about 78.53 percent and SAC about 54.85 percent. Both still pass. This particular experiment does not show a rejection, and the MV-only model still does not establish full MV/LV coverage. Compare with your own output before generalizing.

**Show**

Compare the default and changed allowance.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>L2: reset before continuing</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80</pre><ul><li>Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Rerun L2.</li><li>L3-L5 use a separate saved case called test_01.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">27 / 80</span></div>

<!--
**Say**

Restore load scale 1.0 and current allowance 0.80, then rerun L2. This gives everyone the same starting point again. L3 through L5 use a separate archived case called test_01. Your earlier parameter edit does not rewrite that archive, so we must not attach its old Llama explanation to a different new experiment.

**Show**

Show the restored two default inputs.

**Colab: RESET AND RERUN**

Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80; rerun the complete L2 cell.

Exact cells: classroom-007. Run the whole cell, not only the slide excerpt.

**Expected result**

The default output returns. L3-L5 will use their separate original test_01 case.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>New calculations and saved replies</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/bridge_modes.svg" alt="New calculation, saved reply and proposed pilot are different evidence types." style="height:330px;max-height:330px"><figcaption>New calculation, saved reply and proposed pilot are different evidence types.</figcaption></figure><ul><li>Python calculates new results. A saved Llama reply keeps its original inputs.</li><li>Your changed lab input does not change the saved reply.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md">Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">28 / 80</span></div>

<!--
**Say**

We now have two kinds of evidence. A new calculation uses the inputs we just supplied. A saved model reply records what the model said for its original case. Both can be useful, but they answer different questions. A proposed control-room pilot is a third category: a design to evaluate, not evidence of a deployment.

**Show**

Point to new calculation, saved reply and proposed pilot labels.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
Nominal duration: 0.5 minutes.

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
<h1>L3: inspect saved model choices</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.</p><pre class="teaching-code">pool = lab.saved_pool(&#x27;test_01&#x27;)
display(pd.DataFrame(pool[&#x27;responses&#x27;])[[&#x27;model_id&#x27;, &#x27;operation_id&#x27;, &#x27;reason&#x27;, &#x27;seconds&#x27;, &#x27;source&#x27;]])</pre><ul><li>Run L3. Read the case ID, chosen operations and recorded times.</li><li>This cell displays old replies. It makes no new model call.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">29 / 80</span></div>

<!--
**Say**

Run L3 and read the original case ID, each requested operation and its recorded call time. These are actual earlier replies. Displaying them does not call those models again. Different explanations may request exactly the same tool and settings, so the next step groups those matching requests before counting votes.

**Show**

Locate case ID, operation and recorded seconds.

**Colab: RUN**

Run L3. Keep the default test_01 case.

Exact cells: classroom-010. Run the whole cell, not only the slide excerpt.

**Expected result**

Three saved model replies and recorded times appear; no new model request occurs.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L3 · classroom-010</div>
<h1>Different words can request the same trial</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_canonical_trial.svg" alt="Three saved replies request two different trials." style="height:305px;max-height:305px"><figcaption>Three saved replies request two different trials.</figcaption></figure><ul><li>The notebook groups identical tool requests and settings.</li><li>A vote chooses what to test next. It does not prove that limits pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">30 / 80</span></div>

<!--
**Say**

Three replies do not necessarily produce three different physical trials. Here, two replies request the same reactive-power change, so there are two distinct operations. The vote chooses what to test next. It does not certify the choice. A numerical tool must still check the selected settings, regardless of how many models supported them.

**Show**

Count unique tool/settings records rather than sentences.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

How many distinct trials do these three replies request?

**Answer**

Two, because two replies have identical tool/settings records.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L4 · classroom-013</div>
<h1>L4: check the selected trial</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.</p><pre class="teaching-code">started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings[&#x27;L4 new verification of archived choices&#x27;] = time.perf_counter() - started
display(selected_trials[&#x27;table&#x27;])
assert pool[&#x27;frozen&#x27;] and pool[&#x27;training_updates&#x27;] == 24</pre><ul><li>Run L4 after L3. Python checks the selected trial for its original case.</li><li>Compare majority voting with the saved LinUCB selector, which learns which trial to test.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">31 / 80</span></div>

<!--
**Say**

Run L4 after L3. We compare majority voting with a saved LinUCB selector that learned which trial to test. All earlier model calls have already happened. This selection step allocates a numerical trial; it does not decide which model to call or whether the grid limits pass. Python checks the selected original-case proposal now.

**Show**

Locate the two selectors and fresh check calls.

**Colab: RUN**

Run L4 after L3 without changing the case ID.

Exact cells: classroom-013. Run the whole cell, not only the slide excerpt.

**Expected result**

Both selectors choose RELAX_Q_10_PERCENT; new_check_passes is True for both.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L4 · classroom-013</div>
<h1>L4: read the new check</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L4_checks.png" alt="Saved choices, new checks of the original test_01 case." style="max-height:345px;height:auto"><figcaption>Saved choices, new checks of the original test_01 case.</figcaption></figure></div><ul><li>Both selectors choose the same trial and pass the new MV check.</li><li>new_check_passes is the electrical check. Predicted reward is a learned score.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">32 / 80</span></div>

<!--
**Say**

Both selectors choose the same trial in this example and the new MV check passes. Read new_check_passes for that result. Predicted reward is the selector's learned estimate, not an electrical margin. The saved twelve-case comparison tied voting, so this example does not show that learned selection is generally better than a simple rule.

**Show**

Point to new_check_passes and distinguish predicted reward.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>L5: check model coverage</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.</p><pre class="teaching-code">started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings[&#x27;L5 selected model scope checks&#x27;] = time.perf_counter() - started
display(scope_audit[&#x27;table&#x27;])</pre><ul><li>Leave RUN_OPENDSS=False. Run L5 and read the table.</li><li>The default checks the test_01 MPC plan with the MV model.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">33 / 80</span></div>

<!--
**Say**

Run L5 with OpenDSS still off. This cell checks the original test_01 MPC plan with the MV model and reports its scope. Read the model, command and pass columns together. An optional OpenDSS route can add a wider AC audit, but we are not running it in the default classroom route.

**Show**

Read model, command, pass and scope information together.

**Colab: RUN**

Run L5 with RUN_OPENDSS still False.

Exact cells: classroom-016. Run the whole cell, not only the slide excerpt.

**Expected result**

The linear-model check is shown; the optional full-model path is disabled.
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>A PASS has a scope</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L5_scope.png" alt="Default L5 checks MV only. OpenDSS is off." style="max-height:345px;height:auto"><figcaption>Default L5 checks MV only. OpenDSS is off.</figcaption></figure></div><ul><li>This result covers medium-voltage (MV) phases and currents.</li><li>A full medium- and low-voltage (MV/LV) request needs the wider check or a HOLD.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">34 / 80</span></div>

<!--
**Say**

A PASS describes only what the model checked. Here that means MV phases and line currents, with ideal aggregation of LV load. If the actual request needs the full MV/LV circuit, this result is insufficient. The correct response is to obtain the wider study or keep the request on HOLD, not relabel the result.

**Show**

Point to MV coverage and the missing wider check.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Recorded agent example · separate P3 study</div>
<h1>Saved voltage case: check SAC first</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_1.png" alt="Saved P3 case, separate from L2. Replay in L10B." style="max-height:380px;height:auto"><figcaption>Saved P3 case, separate from L2. Replay in L10B.</figcaption></figure></div><ul><li>Llama asks to check SAC. The tool finds a current-limit failure.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 1; full record in source guide.</a></div>
<span class="pageno">35 / 80</span></div>

<!--
**Say**

We return to a saved P3 episode. Llama asks to verify the saved SAC proposal because that check is missing. The electrical tool then finds a current-limit failure. The useful behavior is recognizing which check to request. The failure comes from the numerical tool, not from the confidence of the language explanation.

**Show**

Point to Llama choice, exact public reason and failed result.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 1 minutes.

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
<h1>Saved voltage case: try the MPC fallback</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_2.png" alt="Saved P3 case, separate from L2. Replay in L10B." style="max-height:380px;height:auto"><figcaption>Saved P3 case, separate from L2. Replay in L10B.</figcaption></figure></div><ul><li>Llama requests the existing MPC plan. The electrical tool checks it.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 2; full record in source guide.</a></div>
<span class="pageno">36 / 80</span></div>

<!--
**Say**

After the failure, Llama requests the MPC plan that already exists. It does not calculate the power flow or invent a new controller. Python and OpenDSS evaluate the fallback and return its voltage and current results. We will inspect the complete saved exchange in L10B after the three numerical cases.

**Show**

Point to the MPC fallback choice and returned checks.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 1 minutes.

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
<h1>Saved voltage case: return for review</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_3.png" alt="Saved P3 case, separate from L2. Replay in L10B." style="max-height:380px;height:auto"><figcaption>Saved P3 case, separate from L2. Replay in L10B.</figcaption></figure></div><ul><li>The checks pass. Human review is still pending. A fixed script gets the same final result.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 3; full record in source guide.</a></div>
<span class="pageno">37 / 80</span></div>

<!--
**Say**

The recorded checks pass for the MPC fallback, but the human acknowledgment is still pending. The model's review message is not the operator's approval. A fixed script reaches the same final numerical outcome in this comparison. This episode demonstrates a traceable tool-selection loop, not a measured improvement in the electrical solver.

**Show**

Point to pending acknowledgment and dispatch=False.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 1 minutes.

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
<h1>Case 2: restoring service</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_fault_map.svg" alt="Six-node active-power model. One branch is unavailable." style="height:305px;max-height:305px"><figcaption>Six-node active-power model. One branch is unavailable.</figcaption></figure><ul><li>Use the six-node teaching network with one faulted branch.</li><li>Compare total service with service to critical loads.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">38 / 80</span></div>

<!--
**Say**

The restoration exercise uses a separate six-node graph. One branch is faulted and unavailable. The tool selects whole loads under the stated capacities. We will compare total served power with power served to critical loads. This smaller example makes the objective easy to inspect; it is not the feeder catalog shown in the saved Llama episode.

**Show**

Identify the source, faulted branch, two ties and critical loads.

**Colab: PREVIEW ONLY**

Show the slide only. Run L6 later on slide 40; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Two service goals</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_priority.svg" alt="Different goals can select different loads." style="height:305px;max-height:305px"><figcaption>Different goals can select different loads.</figcaption></figure><ul><li>One goal gives extra weight to critical loads.</li><li>The other restores the most total kW. Both use the same network rules.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">39 / 80</span></div>

<!--
**Say**

The two methods use the same graph, fault and capacity rules. One maximizes total kW. The other gives extra weight to two critical loads. The different result therefore comes from the service goal. Before an agent requests a restoration solve, the operator must state which goal the tool should follow.

**Show**

Compare the two goals on the same network.

**Colab: PREVIEW ONLY**

Show the slide only. Run L6 later on slide 40; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>L6: solve the restoration problem</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.</p><pre class="teaching-code">CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings[&#x27;L6 fresh MILP sweep + independent enumeration&#x27;] = time.perf_counter() - started
display(restoration[&#x27;table&#x27;].drop(columns=&#x27;pickup&#x27;))</pre><ul><li>Run L6. MILP selects whole loads. A separate search checks its priority score.</li><li>Read served_kw, critical_kw and MILP_matches_exhaustive_check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">40 / 80</span></div>

<!--
**Say**

Run L6 with the original capacity list. A mixed-integer linear program chooses which whole loads to serve. A separate exhaustive search checks the priority score on this small graph. Read total kW, critical kW and the agreement flag. Agreement supports this formulation's result; it does not add AC voltage or protection checks.

**Show**

Read total service, critical service and enumeration agreement.

**Colab: RUN**

Run L6 with CAPACITIES_KW=(40.,60.,80.,100.,120.).

Exact cells: classroom-018. Run the whole cell, not only the slide excerpt.

**Expected result**

The priority MILP agrees with exhaustive enumeration. At 40 kW, compare 130/90 with 140/30 kW total/critical.
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
<h1>L6: read both service plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_plot.png" alt="Reference L6 plots. Overlapping markers show equal outcomes." style="max-height:345px;height:auto"><figcaption>Reference L6 plots. Overlapping markers show equal outcomes.</figcaption></figure></div><ul><li>Left: total kW served. Right: critical kW served.</li><li>Overlapping markers mean the two goals give the same result.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">41 / 80</span></div>

<!--
**Say**

Read the two service plots together. The left reports total kW and the right reports critical kW. At some capacities the markers overlap because the objectives give the same outcome. Avoid assuming that a priority objective must improve every operating point. Identify where there is a real service tradeoff before explaining a benefit.

**Show**

Compare the two plotted service measures.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>L6: the tradeoff at 40 kW</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_table.png" alt="Reference L6: 40 kW varied tie, 100 kW fixed tie." style="max-height:345px;height:auto"><figcaption>Reference L6: 40 kW varied tie, 100 kW fixed tie.</figcaption></figure></div><ul><li>Priority goal: 130 kW total, including 90 kW critical.</li><li>Most-total-kW goal: 140 kW total, including 30 kW critical.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">42 / 80</span></div>

<!--
**Say**

At a 40 kW varied tie limit, the priority goal serves 130 kW total, including 90 kW critical. The maximum-total goal serves 140 kW total, including only 30 kW critical. A separate fixed tie remains at 100 kW, so the varied tie rating is not the total served load. The priorities explain this tradeoff.

**Show**

Point to 130/90 versus 140/30, all in kW.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

**Ask**

Which goal would you choose if critical service is the stated priority?

**Answer**

The priority-weighted goal, with the explicit total-service tradeoff.
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
<h1>Restoration checks</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_verify.svg" alt="Checks cover this graph model, not AC operation or field switching." style="height:305px;max-height:305px"><figcaption>Checks cover this graph model, not AC operation or field switching.</figcaption></figure><ul><li>Check source paths, branch capacity, power balance and the fault.</li><li>A separate search checks the priority score.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">43 / 80</span></div>

<!--
**Say**

The graph checks include source connection, power balance, branch capacity and keeping the faulted branch unavailable. The separate enumeration checks the priority objective. Those checks give evidence for this active-power model. They do not establish a field switching order, protection coordination or the voltage behavior of an AC network.

**Show**

Trace connection, balance, capacity and independent score checks.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
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

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Exercise 2: increase tie capacity</h1>
<div class="content"><pre class="source-excerpt">CAPACITIES_KW = (40., 60., 80., 100., 120., 180.)</pre><ul><li>Add 180. to CAPACITIES_KW. Keep 40. first. Predict, then rerun L6.</li><li>Compare total and critical kW at 40 and 180 kW.</li><li>At which capacity do the two goals give the same result?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">44 / 80</span></div>

<!--
**Say**

Append 180. to the capacity list and keep 40. first. Predict whether the two service goals will still disagree, then rerun the full L6 cell. Compare total and critical kW at 40 and 180 kW. Keeping the first entry unchanged matters because L7 later uses the first record in this list.

**Show**

Show the appended 180. entry and keep 40. first.

**Colab: EDIT AND RERUN**

Append 180. to CAPACITIES_KW, keeping 40. first. Rerun all of L6. Give this exercise four minutes.

Exact cells: classroom-018. Run the whole cell, not only the slide excerpt.

**Expected result**

At 180 kW, both goals serve 250 kW total and 90 kW critical.

**Ask**

At which tested capacity do these two goals agree?

**Answer**

They agree at 180 kW in this exercise.
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
<h1>Exercise 2: enough capacity removes this tradeoff</h1>
<div class="content"><p class="callout">250 kW total / 90 kW critical</p><ul><li>At 180 kW, both goals serve 250 kW total and 90 kW critical.</li><li>The priority goal helps at some limits. It does not improve every case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">45 / 80</span></div>

<!--
**Say**

At 180 kW, both goals serve all 250 kW of load and all 90 kW of critical load in this graph. The earlier tradeoff has disappeared. That is why a good explanation states where a method helps rather than claiming an improvement everywhere. These numbers come from conventional optimization, not from Llama.

**Show**

Compare the equal total and critical service at 180 kW.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>L7: test an old result after a change</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.</p><pre class="teaching-code">rest_record = restoration[&#x27;records&#x27;][0][&#x27;weighted&#x27;]
rest_request = {&#x27;task&#x27;: &#x27;restoration&#x27;, &#x27;capacity_kw&#x27;: CAPACITIES_KW[0],
                &#x27;critical_nodes&#x27;: [2, 5], &#x27;model&#x27;: &#x27;six_node_active_transport&#x27;, &#x27;revision&#x27;: 1}</pre><ul><li>Restore the original capacity list and rerun L6.</li><li>Run L7. It changes the first request from 40 kW to 20 kW.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">46 / 80</span></div>

<!--
**Say**

First restore the original capacity list and rerun L6. Then run the whole L7 cell. It matches the first restoration result to its 40 kW request, then changes the request to 20 kW without recomputing the plan. We are testing whether old evidence still matches, not solving the changed problem in this cell.

**Show**

Show the reset list, then the L7 changed request.

**Colab: RESET, THEN RUN**

Restore the original capacity list and rerun L6. Then run the whole L7 cell.

Exact cells: classroom-018, classroom-021. Run the whole cell, not only the slide excerpt.

**Expected result**

Original contract: True. Changed rating with old evidence: False. HOLD requests a fresh solve.
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>L7: the old evidence no longer matches</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L7_binding.png" alt="Reference L7. New inputs require new evidence." style="max-height:345px;height:auto"><figcaption>Reference L7. New inputs require new evidence.</figcaption></figure></div><ul><li>Original request: True. Changed request: False.</li><li>HOLD the old recommendation and request a new solve.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">47 / 80</span></div>

<!--
**Say**

The original request matches and returns True. The changed request returns False because the old evidence describes another set of inputs. Keep the old recommendation on HOLD and request a new solve. This result does not prove that every new plan at 20 kW must fail; it says the old check cannot support the changed request.

**Show**

Read original True and changed-request False.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

**Ask**

Does False prove the new physical plan is infeasible?

**Answer**

No. It detects that the old evidence does not match the changed request.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>New inputs need new evidence</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_stale.svg" alt="L7 changes capacity and revision, then tests the old evidence." style="height:305px;max-height:305px"><figcaption>L7 changes capacity and revision, then tests the old evidence.</figcaption></figure><ul><li>An outdated check does not tell us whether the new plan works.</li><li>Solve again, check again and attach the new result to the new request.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">48 / 80</span></div>

<!--
**Say**

There are two different problems: an electrical limit violation and an outdated result. A mismatch test detects the second. After changing the request, we need a new solve and a new check attached to the new inputs. A confident natural-language explanation cannot turn an old calculation into current evidence.

**Show**

Distinguish an old-evidence mismatch from physical infeasibility.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>The agent keeps the service goal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_plan.svg" alt="Proposed agent use. L6 itself runs Python." style="height:305px;max-height:305px"><figcaption>Proposed agent use. L6 itself runs Python.</figcaption></figure><ul><li>L6 runs Python directly. The operator sets priorities; MILP selects loads.</li><li>An agent could request the solve and explain its returned tradeoff.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">49 / 80</span></div>

<!--
**Say**

L6 itself runs Python directly: the operator supplies priorities and limits, and MILP selects loads. An agent could request that existing tool and explain the returned tradeoff while keeping the goal fixed. We should not describe that possible role as a live LLM action in L6. The saved multi-role restoration workflow is a separate study.

**Show**

Point to the operator goal and numerical load selection.

**Colab: PREVIEW ONLY**

Show the slide only. Run L6 later on slide 40; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Restoration model limits</h1>
<div class="content"><ul><li>This graph checks active power, not AC voltage or protection.</li><li>Selected branches do not specify the order of field switching.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">50 / 80</span></div>

<!--
**Say**

The six-node model is deliberately small. It handles active-power transport and whole-load pickup. It does not check AC voltage, reactive power, protection or a safe order of field operations. A selected set of energized branches is therefore a study result to review, not a complete switching instruction.

**Show**

Name one omitted physical check.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Recorded agent example · separate feeder study</div>
<h1>Saved restoration case: try another plan</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_14.png" alt="Saved feeder-catalog study, separate from L6. Replay in L10B." style="max-height:380px;height:auto"><figcaption>Saved feeder-catalog study, separate from L6. Replay in L10B.</figcaption></figure></div><ul><li>Llama requests a trial that restores more load and passes the current check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 14; full record in source guide.</a></div>
<span class="pageno">51 / 80</span></div>

<!--
**Say**

In the separate saved feeder-catalog case, Llama requests SHED_075. The tool reports more served load than the previous passing plan, while preserving critical service and passing the current check. The operation name describes a setting in this catalog. It is not the capacity edit or MILP result from our six-node exercise.

**Show**

Read the saved SHED_075 result and current percentage.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 1 minutes.

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
<h1>Saved restoration case: reject a failed trial</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_15.png" alt="Saved feeder-catalog study, separate from L6. Replay in L10B." style="max-height:380px;height:auto"><figcaption>Saved feeder-catalog study, separate from L6. Replay in L10B.</figcaption></figure></div><ul><li>The next trial exceeds the current limit. Keep the previous passing plan.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 15; full record in source guide.</a></div>
<span class="pageno">52 / 80</span></div>

<!--
**Say**

Llama next requests SHED_065. That restores more ordinary load but reaches about 111 percent of allowed current, so the verifier rejects it. A larger service number cannot compensate for a failed hard limit. Keep the earlier passing candidate available, record the failure and prevent the rejected trial from entering the final ranking.

**Show**

Point to the failed current check for SHED_065.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

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
<h1>Saved restoration case: correct the ranking</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_16.png" alt="Saved feeder-catalog study, separate from L6. Replay in L10B." style="max-height:380px;height:auto"><figcaption>Saved feeder-catalog study, separate from L6. Replay in L10B.</figcaption></figure></div><ul><li>Python corrects the ranking and rechecks the lowest-cost passing plan.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 16; full record in source guide.</a></div>
<span class="pageno">53 / 80</span></div>

<!--
**Say**

Llama then puts the passing candidates in the wrong cost order. Python checks the numerical costs, keeps the lower-cost passing plan and rechecks it. This is a concrete reason to keep a deterministic ranking guard. A valid JSON answer can still contain a bad decision, so checking the output format is only the first step.

**Show**

Compare Llama order with the numerical cost order.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected result**

No new notebook output on this slide.

**Ask**

Can schema-valid JSON still give the wrong ranking?

**Answer**

Yes. The numerical order must also be checked.
Nominal duration: 1 minutes.

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
<h1>Case 3: suspicious readings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_network.svg" alt="Four-bus DC model. Simulation truth is used only for offline comparison." style="height:305px;max-height:305px"><figcaption>Four-bus DC model. Simulation truth is used only for offline comparison.</figcaption></figure><ul><li>Use the separate four-bus DC teaching model.</li><li>Compare the fit to readings with error against known simulation truth.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">54 / 80</span></div>

<!--
**Say**

The cyber exercise uses a separate four-bus DC model. We can compare an alarm against the true simulated state because this is an offline teaching experiment. A real control-room estimator does not receive that truth for comparison. Keep the alarm's measured consistency separate from our offline measurement of estimation error.

**Show**

Identify the separate four-bus model.

**Colab: PREVIEW ONLY**

Show the slide only. Run L8 later on slide 56; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>What the residual measures</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_residual.svg" alt="A good fit does not authenticate the readings." style="height:305px;max-height:305px"><figcaption>A good fit does not authenticate the readings.</figcaption></figure><ul><li>Weighted least squares (WLS) fits the readings. Residual J measures the mismatch.</li><li>The true state is known in this simulation, not in a live control room.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">55 / 80</span></div>

<!--
**Say**

Weighted least squares finds a state that fits the supplied readings, with more weight on readings declared less uncertain. Residual J measures the remaining mismatch. It does not establish where the data came from. The state-error plot is possible here because the simulation supplies a known truth, which remains outside the estimator and Llama inputs.

**Show**

Distinguish measured residual from offline truth error.

**Colab: PREVIEW ONLY**

Show the slide only. Run L8 later on slide 56; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
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

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>L8: run two data attacks</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings[&#x27;L8 fresh WLS attack sweep&#x27;] = time.perf_counter() - started
display(cyber[&#x27;table&#x27;])</pre><ul><li>Run L8 with the default scales.</li><li>Compare one biased reading with a coordinated change across readings.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">56 / 80</span></div>

<!--
**Say**

Run the default L8 cell. One attack biases a single reading. The other coordinates changes so that they remain consistent with the modeled measurement relationships. Compare both the residual and state-error plots. Before looking at the curves, predict whether a larger data attack must always create a larger residual alarm.

**Show**

Show the two attack types and default scale list.

**Colab: RUN**

Run L8 with ATTACK_SCALES=(0.,.25,.5,1.,1.5).

Exact cells: classroom-023. Run the whole cell, not only the slide excerpt.

**Expected result**

A coordinated Hc attack preserves a small residual while offline state error grows.
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
<h1>L8: read both cyber plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L8_plot.png" alt="Reference L8 plots. State error uses known simulation truth." style="max-height:345px;height:auto"><figcaption>Reference L8 plots. State error uses known simulation truth.</figcaption></figure></div><ul><li>Left: mismatch J and the alarm threshold. Right: error against simulation truth.</li><li>A quiet alarm can appear alongside a growing state error.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">57 / 80</span></div>

<!--
**Say**

The coordinated curve is the important one to follow across both panels. Its state error can grow while the residual stays small. The left panel therefore tells us about fit to the model, not the truth of the data. Read the threshold and the offline error together before calling a quiet alarm reassuring.

**Show**

Follow one coordinated curve across both panels.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
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
<h1>L8: a coordinated attack escapes the alarm</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_stealth.svg" alt="Values from the eight-reading L8 model." style="height:305px;max-height:305px"><figcaption>Values from the eight-reading L8 model.</figcaption></figure><ul><li>At scale 1, one biased reading gives J=277.50 and an alarm.</li><li>The coordinated attack gives J=3.92, no alarm, and 0.02678 rad of state error.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">58 / 80</span></div>

<!--
**Say**

At scale one, the isolated bias gives J about 277.50 and triggers the alarm. The coordinated attack gives J about 3.92, below the threshold, while the state error is about 0.02678 radians. This attack assumes knowledge of the model and control of the modeled unprotected channels. It is a defined teaching threat, not every possible attack.

**Show**

Compare alarm, residual and state error at scale 1.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
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

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Exercise 3: test a small bias</h1>
<div class="content"><pre class="source-excerpt">ATTACK_SCALES = (0., .10, .25, .5, 1., 1.5)</pre><ul><li>Add .10 to ATTACK_SCALES. Predict, then rerun L8.</li><li>At scale 0.10, compare J, the alarm flag and state error.</li><li>Does no alarm mean the data are correct?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">59 / 80</span></div>

<!--
**Say**

Add .10 to the attack-scale list and rerun L8. Focus on the isolated-bias row at that scale. Read J, the alarm flag and state error. Use the two plots to answer whether no alarm means the reading is correct. Change only the scale list so the comparison stays clear.

**Show**

Show the single new .10 entry.

**Colab: EDIT AND RERUN**

Add .10 to ATTACK_SCALES. Rerun all of L8 and inspect the isolated-bias row. Give this exercise four minutes.

Exact cells: classroom-023. Run the whole cell, not only the slide excerpt.

**Expected result**

At isolated scale 0.10, J is about 10.14, below the 15.09 threshold; no alarm is not proof of truth.

**Ask**

Does no alarm mean the reading is true?

**Answer**

No. The threshold can miss a small bias, and coordinated changes can preserve the fit.
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
<h1>Exercise 3: a small bias can miss the threshold</h1>
<div class="content"><p class="callout">10.14 &lt; 15.09 → no residual alarm</p><ul><li>At scale 0.10, J is about 10.14, below the 15.09 alarm threshold.</li><li>A quiet alarm alone cannot prove that readings are true.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">60 / 80</span></div>

<!--
**Say**

At isolated scale 0.10, J is about 10.14, below the 15.09 alarm threshold. A small inconsistent bias can therefore miss the threshold. The coordinated attack illustrates a different problem: it can preserve the fit by design. These examples show why a residual alarm alone cannot establish measurement authenticity.

**Show**

Point to 10.14 below 15.09.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>L8: reset before recovery</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)</pre><ul><li>Restore the original attack scales and rerun L8.</li><li>L9 uses a separate fixed recovery case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">61 / 80</span></div>

<!--
**Say**

Restore the original attack-scale list and rerun L8. This resets the shared notebook state before continuing. L9 uses a fixed recovery case rather than the last point from your scale sweep. Changing a plotted scale in L8 therefore does not automatically change the correction calculated in L9.

**Show**

Show the original scale list restored.

**Colab: RESET AND RERUN**

Restore ATTACK_SCALES=(0.,.25,.5,1.,1.5) and rerun all of L8.

Exact cells: classroom-023. Run the whole cell, not only the slide excerpt.

**Expected result**

The default sweep returns. L9 remains a separate fixed recovery fixture.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>L9: one fixed recovery case</h1>
<div class="content"><ul><li>Compare the same case with and without readings assumed to be trusted.</li><li>Your L8 scale change does not change this case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">62 / 80</span></div>

<!--
**Say**

We will compare the same recovery case under two information conditions. In one, the extra trusted readings are unavailable. In the other, three angle readings are assumed trustworthy. The numerical fixture stays fixed. We are testing the effect of that information assumption, not making the solver recover from every attack scale we just plotted.

**Show**

Keep the same fixed recovery case while changing data availability.

**Colab: PREVIEW ONLY**

Show the slide only. Run L9 later on slide 64; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Data trust is an assumption</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_trusted.svg" alt="Three extra angle readings are assumed trustworthy." style="height:305px;max-height:305px"><figcaption>Three extra angle readings are assumed trustworthy.</figcaption></figure><ul><li>This example assumes three extra angle readings are trustworthy.</li><li>Neither WLS nor Llama authenticates them.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">63 / 80</span></div>

<!--
**Say**

The word trusted has a specific meaning here: the example assumes three independent angle readings are trustworthy. No authentication system is implemented. Neither a small residual nor a good Llama explanation can create that trust. In an actual operator study, the source and protection of those readings would need independent evidence.

**Show**

Point to the assumed trusted angle channels.

**Colab: PREVIEW ONLY**

Show the slide only. Run L9 later on slide 64; keep the notebook in order.

**Expected result**

No new notebook output on this slide.

**Ask**

Which tool authenticates these three readings?

**Answer**

None in this fixture; their trust is an external assumption.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>L9: HOLD or PROPOSE</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.</p><pre class="teaching-code">without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)</pre><ul><li>Run all of L9. Read status first.</li><li>Then read the proposed injection and the offline violation count.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">64 / 80</span></div>

<!--
**Say**

Run all of L9. First read the status for each condition. Without the assumed trusted replacement readings, the result is HOLD and no correction is proposed. With them, a quadratic-program solver calculates a constrained correction and returns PROPOSE. The offline check uses simulation truth to assess the outcome afterward.

**Show**

Read status before looking at the correction.

**Colab: RUN**

Run all of L9 after resetting L8.

Exact cells: classroom-026. Run the whole cell, not only the slide excerpt.

**Expected result**

No trusted replacement readings: HOLD. With assumed trusted readings: PROPOSE, u about 0.121694 p.u., zero offline violations.
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>L9: two outcomes</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L9_trust.png" alt="Reference L9 output for the fixed recovery case, not the edited L8 scale." style="max-height:325px;height:auto"><figcaption>Reference L9 output for the fixed recovery case, not the edited L8 scale.</figcaption></figure></div><ul><li>Without trusted replacement readings: HOLD.</li><li>With assumed trusted readings: PROPOSE, u about 0.121694 p.u., zero offline model violations.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">65 / 80</span></div>

<!--
**Say**

With the trust assumption, the proposed flexible injection is about 0.121694 per unit and the offline model reports zero violations. Per unit means a value relative to the model's stated base, not a direct MW command. PROPOSE is a study outcome for review. It does not say that the sensors have been authenticated or that equipment may operate.

**Show**

Compare HOLD, PROPOSE and the offline violation count.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>L9: check the correction</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_qp.svg" alt="Fixed L9 correction: compare the predicted branch flow with the offline truth check." style="height:305px;max-height:305px"><figcaption>Fixed L9 correction: compare the predicted branch flow with the offline truth check.</figcaption></figure><ul><li>A quadratic-program (QP) solver finds the smallest allowed injection that meets the branch limits.</li><li>One flow: predicted 0.17000 p.u., offline actual 0.17046 p.u., limit 0.18000 p.u.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">66 / 80</span></div>

<!--
**Say**

The solver looks for the smallest permitted correction that meets the modeled branch limits with a margin. One predicted flow is 0.17000 per unit. The offline actual value is about 0.17046, below the 0.18000 limit. Those are model-specific results. They do not add protection, dynamic or equipment-permission checks.

**Show**

Locate predicted flow, offline actual flow and the limit.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>A proposal depends on its assumptions</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_handoff.svg" alt="A numerical proposal still needs human review." style="height:305px;max-height:305px"><figcaption>A numerical proposal still needs human review.</figcaption></figure><ul><li>Assumed trusted data support the estimate. The solver calculates a correction.</li><li>The operator still reviews data trust, model coverage and missing checks.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">67 / 80</span></div>

<!--
**Say**

The recovery proposal depends on assumed trusted data, the four-bus model and the stated limits. The numerical tool supplies the correction and its checks. The operator must still review those assumptions and any missing studies. If the required information is unavailable, the useful assistant response is a clear HOLD with the missing requirement identified.

**Show**

Point to assumptions, checks and the operator-review step.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Recorded agent example · separate recovery study</div>
<h1>Saved cyber case: request the allowed tool</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_7.png" alt="Saved four-bus study. Replay in L10B." style="max-height:380px;height:auto"><figcaption>Saved four-bus study. Replay in L10B.</figcaption></figure></div><ul><li>Llama selects the supplied recovery tool. Python calculates the correction.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: cyber replay, recorded call 7; full record in source guide.</a></div>
<span class="pageno">68 / 80</span></div>

<!--
**Say**

This saved standard cyber episode already supplies the allowed recovery tool and the trust assumption. Llama selects that tool, and Python calculates the correction. The model does not discover a trusted sensor source. This recording is separate from the five-role cyber archive in L10, even though both use related four-bus teaching methods.

**Show**

Read the supplied tool choice and trust condition.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 0.5 minutes.

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
<h1>Saved cyber case: keep human review</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_8.png" alt="Saved four-bus study. Replay in L10B." style="max-height:350px;height:auto"><figcaption>Saved four-bus study. Replay in L10B.</figcaption></figure></div><ul><li>The model check passes. The operator must still review trust and missing checks.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: cyber replay, recorded call 8; full record in source guide.</a></div>
<span class="pageno">69 / 80</span></div>

<!--
**Say**

The recorded numerical check passes, but the language result still asks for review. The operator's acknowledgment is pending. This is the right distinction to keep visible: a passed calculation, a model's review message and a person's decision are different events. The fixed comparator gives the same numerical outcome in this saved episode.

**Show**

Read PASS, REVIEW and pending human acknowledgment separately.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected result**

No new notebook output on this slide.
Nominal duration: 1 minutes.

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
<h1>L10: inspect the five-role workflow</h1>
<div class="content"><ul><li>Run L10 to see every recorded stage and result.</li><li>The stages share case facts, proposals and check results. The next slides explain their jobs.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.</a></div>
<span class="pageno">70 / 80</span></div>

<!--
**Say**

Run L10 to inspect every stage in the saved five-role workflow. Read a case, role, returned choice and result rather than only the model's explanation. One Llama model fills the planning and optimizer roles; Python performs the other stages. This cell reads the saved trace. It does not launch five new agents or call a model.

**Show**

Expand the saved trace and find all five distinct stage names.

**Colab: RUN**

Run all of L10 after L9. Read the case and stage columns in the saved trace.

Exact cells: classroom-028. Run the whole cell, not only the slide excerpt.

**Expected result**

Five stage names appear. Planning and optimizer rows contain actual saved Llama replies; other stages contain Python results.
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L10B · classroom-llama-walkthrough</div>
<h1>L10B: replay the three Llama examples</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L10B (classroom-llama-walkthrough), source lines 1–5.</p><pre class="teaching-code">SCENARIO = &quot;voltage&quot;  # Change to &quot;restoration&quot; or &quot;cyber&quot;, then rerun this cell.
from IPython.display import HTML, display
from src.llama_walkthrough import load_episodes, render_episode_html
replay_episodes = load_episodes(ROOT)
display(HTML(render_episode_html(replay_episodes[SCENARIO])))</pre><ul><li>Set SCENARIO to voltage, restoration and cyber. Rerun for each.</li><li>These are saved replies and tool results. No new Llama call runs here.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10B; cell classroom-llama-walkthrough; src/llama_walkthrough.py.</a></div>
<span class="pageno">71 / 80</span></div>

<!--
**Say**

Run the full L10B cell for voltage, then change SCENARIO to restoration and cyber, rerunning each time. Follow input facts, allowed choice, exact public reason, tool result and next step. Find the failed voltage trial or wrong restoration ranking. These are saved, source-checked episodes; replaying them performs no new Llama call or electrical solve.

**Show**

Follow one full replay from facts to next decision.

**Colab: REPLAY THREE TIMES**

After L10, run the whole L10B cell for SCENARIO="voltage", then "restoration", then "cyber". Change only that string between runs.

Exact cells: classroom-llama-walkthrough. Run the whole cell, not only the slide excerpt.

**Expected result**

Input, exact model choice and public reason, saved tool result and next step appear. No new LLM call or electrical solve runs.
Nominal duration: 4.5 minutes.

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
<h1>L12: practice operator readback</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.</p><pre class="teaching-code">wrong_id = lab.acknowledge(mv_scope, &#x27;wrong-id&#x27;, &#x27;Student operator&#x27;)
readback = lab.acknowledge(mv_scope, mv_scope[&#x27;recommendation_id&#x27;], &#x27;Student operator&#x27;)</pre><ul><li>Leave L11 disabled, then run L12.</li><li>Check the wrong ID, the matching ID and equipment_dispatch=False.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">72 / 80</span></div>

<!--
**Say**

Leave the live-model switch False and run L11; SKIPPED is expected. Then run L12. It returns to the original voltage test_01 result, not the restoration or cyber sweeps. Compare a full MV/LV request with an explicit MV teaching request, then inspect the wrong-ID and correct-ID readback tests. This remains a simulation.

**Show**

Locate the wrong-ID assertion, the matching readback and equipment_dispatch.

**Colab: SKIP LIVE CALL, THEN RUN**

Keep RUN_LOCAL_LLAMA=False. Run L11 and expect SKIPPED. Then run all of L12.

Exact cells: classroom-030, classroom-033. Run the whole cell, not only the slide excerpt.

**Expected result**

The table shows HOLD for full MV/LV and an acknowledged MV teaching request. The assertions confirm wrong-ID rejection; equipment_dispatch remains False.
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs / L12 / simulated readback</div>
<h1>L12: approval must match the checked scope</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L12_packet.png" alt="Reference L12 output. Readback is simulated." style="max-height:345px;height:auto"><figcaption>Reference L12 output. Readback is simulated.</figcaption></figure></div><ul><li>Full MV/LV request: HOLD. The MV teaching request allows a simulated readback.</li><li>A wrong ID fails. This exercise never sends equipment commands.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">73 / 80</span></div>

<!--
**Say**

The full MV/LV request stays on HOLD because the evidence only covers MV. The narrower teaching request can accept a simulated readback when the recommendation ID matches. A wrong ID fails. Check that equipment_dispatch remains False. Human acknowledgment records which study was reviewed; it cannot repair a missing engineering check or authorize field switching here.

**Show**

Compare scope matching before acknowledgment.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

**Ask**

Can a correct recommendation ID repair missing LV coverage?

**Answer**

No. Scope must match before a readback can be accepted.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Recorded five-role study / L10</div>
<h1>Our multi-agent design: five roles</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/multi_agent_roles.svg" alt="Custom Python workflow, one Llama model in two roles. L10 displays its saved trace." style="height:365px;max-height:365px"><figcaption>Custom Python workflow, one Llama model in two roles. L10 displays its saved trace.</figcaption></figure><ul><li>The roles pass structured results to each other. Llama handles planning and refinement; Python runs the other stages.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py">Five-role implementation: src/proposal_workflow.py; recorded results: proposal_complete_workflow.json.</a></div>
<span class="pageno">74 / 80</span></div>

<!--
**Say**

The multi-agent design here means five named responsibilities in one Python workflow. Awareness reads the case. Planning prepares candidates and asks Llama whether to proceed. Simulation calculates their effects. Verification applies fixed checks. The optimizer asks Llama for an allowed new trial or ranking. Changed trials return for calculation and checking, and the selected option gets a final recheck before human review.

**Show**

Follow the five roles and the return path for a changed trial.

**Colab: NO NEW RUN**

Use the saved L10 trace already displayed. Map the five roles without making a new model call.

**Ask**

Are these five separate LLMs?

**Answer**

No. One Llama model fills two roles; Python runs awareness, simulation and verification.
Nominal duration: 1.5 minutes.

Full sources:
Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py
Publication: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json

Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Recorded five-role study / L10</div>
<h1>Five roles in the voltage case</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/multi_agent_voltage.svg" alt="L10 MV voltage archive, separate from L2 and the P3 replay in L10B." style="height:365px;max-height:365px"><figcaption>L10 MV voltage archive, separate from L2 and the P3 replay in L10B.</figcaption></figure><ul><li>Llama asks for less reactive power, then more solar output. Python checks each new trial.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py">Five-role implementation: src/proposal_workflow.py; recorded results: proposal_complete_workflow.json.</a></div>
<span class="pageno">75 / 80</span></div>

<!--
**Say**

For the saved L10 voltage case, awareness keeps the load and limits. Numerical planning tools supply MPC and SAC candidates. Simulation calculates voltage and current, and verification tests the limits. Llama requests less reactive power and then more solar output. Python rechecks each change. The final current use is about 50.75 percent in the MV-only model; operator review is still separate.

**Show**

Map each role to the saved voltage inputs, calculations and final result.

**Colab: NO NEW RUN**

Use the saved L10 trace already displayed. Map the five roles without making a new model call.
Nominal duration: 1 minutes.

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

<div class="eyebrow">Recorded five-role study / L10</div>
<h1>Five roles in the restoration case</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/multi_agent_restoration.svg" alt="L10 feeder catalog, separate from the six-node L6 exercise." style="height:365px;max-height:365px"><figcaption>L10 feeder catalog, separate from the six-node L6 exercise.</figcaption></figure><ul><li>The goal stays fixed. A failed trial cannot enter the final ranking, and Python corrects a wrong cost order.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py">Five-role implementation: src/proposal_workflow.py; recorded results: proposal_complete_workflow.json.</a></div>
<span class="pageno">76 / 80</span></div>

<!--
**Say**

For L10 restoration, awareness records the fault, available ties and critical loads. Planning supplies catalog options. Simulation measures service and current. Verification rejects the SHED_065 trial that exceeds the current limit. Llama's optimizer also ranks passing plans incorrectly. Python corrects the cost order and rechecks the chosen plan: about 1,843.61 kW total and 474.04 kW critical, with 91.87 percent current use.

**Show**

Map each role to the saved catalog trial, failure and corrected ranking.

**Colab: NO NEW RUN**

Use the saved L10 trace already displayed. Map the five roles without making a new model call.
Nominal duration: 1 minutes.

Full sources:
Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py
Publication: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json

Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Recorded five-role study / L10</div>
<h1>Five roles in the cyber case</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/multi_agent_cyber.svg" alt="L10 four-bus DC cyber_stealth archive. Trusted channels are assumed." style="height:365px;max-height:365px"><figcaption>L10 four-bus DC cyber_stealth archive. Trusted channels are assumed.</figcaption></figure><ul><li>The workflow keeps the trust assumption visible. It cannot create trusted data from a convincing answer.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py">Five-role implementation: src/proposal_workflow.py; recorded results: proposal_complete_workflow.json.</a></div>
<span class="pageno">77 / 80</span></div>

<!--
**Say**

For L10 cyber response, awareness preserves the readings and declared trust assumption. Planning supplies allowed response candidates. Simulation estimates the state and calculates corrections. Verification tests the trust condition, flows and model scope. Llama requests bounded refinements, including the trusted-data QP. The final selected injection is about 0.121694 per unit. None of these roles authenticates the sensors or replaces human review.

**Show**

Map each role to data trust, the QP correction and flow checks.

**Colab: NO NEW RUN**

Use the saved L10 trace already displayed. Map the five roles without making a new model call.
Nominal duration: 1 minutes.

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

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>The operator reviews one evidence packet</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_review.svg" alt="Proposed control-room use. Study review does not operate equipment." style="height:330px;max-height:330px"><figcaption>Proposed control-room use. Study review does not operate equipment.</figcaption></figure><ul><li>Review the inputs, proposal, worst margins and missing checks.</li><li>Request another study, reject the proposal or accept it for the next authorized step.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">78 / 80</span></div>

<!--
**Say**

An operator needs a short evidence packet: which case and data were used, which proposal was selected, the worst margins and the missing checks. The person can request another study, reject the proposal or accept it for a defined next step. Reviewing a study is different from issuing an equipment command through an authorized operating process.

**Show**

Point to the study packet and the three review choices.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
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

<div class="eyebrow">Proposed advisory pilot · teaching design</div>
<h1>What the evidence shows</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_pilot.svg" alt="L10 comparison: same tools and trial budgets. No general performance gain is established." style="height:330px;max-height:330px"><figcaption>L10 comparison: same tools and trial budgets. No general performance gain is established.</figcaption></figure><ul><li>In L10, five paired final costs tied; one Llama route was worse.</li><li>Start with past cases and read-only use. Measure benefit against the same tools in a fixed script.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">79 / 80</span></div>

<!--
**Say**

We should measure useful benefit rather than assume it. In L10's six paired comparisons, five final costs tied and one Llama route was worse. Model calls also added time. Start with past cases and read-only studies. Compare completed work, missed checks, time and review effort against a fixed script using the same numerical tools and budgets.

**Show**

Keep the paired study result separate from a proposed pilot benefit.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

What useful benefit should a new pilot measure?

**Answer**

Completed correct studies, missed checks, elapsed time and reviewer effort against a fixed-script baseline.
Nominal duration: 1 minutes.

Full sources:
Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py
Publication: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json

Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.
Full source: https://doi.org/10.6028/NIST.AI.100-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide has-diagram">

<h1>Questions and your next lab run</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_one_notebook.svg" alt="Keep the saved replies separate from your new experiment." style="height:310px;max-height:310px"><figcaption>Keep the saved replies separate from your new experiment.</figcaption></figure><p class="activity-link"><a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Open the three cases in Colab</a></p><ul><li>Choose one case. Change one input, rerun and save the result.</li><li>Explain the agent choice, tool result, check and operator decision.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">80 / 80</span></div>

<!--
**Say**

Choose one case you can repeat after the session. Change one input, run the relevant cell and save the result. Explain the model's choice where a saved episode is used, the numerical tool result, the check and the operator's remaining decision. Keep your new experiment separate from the saved reply's original inputs. We can now use questions to revisit any part of that loop.

**Show**

Point to the Colab link and invite one repeatable experiment.

**Colab: NO NEW RUN**

No required new run. Learners may repeat one case afterward and save their changed inputs and outputs.

**Ask**

Can you explain one case using input, tool, result, check and operator decision?

**Answer**

Accept an answer only when it distinguishes new calculations from saved model replies and states a remaining limit.
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->
