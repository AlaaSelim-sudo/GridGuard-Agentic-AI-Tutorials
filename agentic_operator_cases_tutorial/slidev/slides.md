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
<p>Help an operator compare options, check results and decide the next step.</p>
<p>One notebook / 90 minutes / three short exercises</p>
<div class="presenters"><div><strong>Alaa Selim</strong><span>MIT/Dartmouth</span></div><div><strong>Mohamed Chehada</strong><span>UT Austin</span></div></div>
<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup"><small>Independent educational material · IEEE ComSoc theme adaptation</small>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">1 / 69</span></div>

<!--
**Say**

Help an operator compare options, check results and decide the next step. One notebook / 90 minutes / three short exercises

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

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

<h1>An agent chooses what to try next</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_agent_loop.svg" alt="Teaching diagram: the model requests a tool and uses the returned evidence." style="height:310px;max-height:310px"><figcaption>Teaching diagram: the model requests a tool and uses the returned evidence.</figcaption></figure><ul><li>Give the agent a goal. It requests a tool, reads the result and chooses the next step.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.</a></div>
<span class="pageno">2 / 69</span></div>

<!--
**Say**

Give the agent a goal. It requests a tool, reads the result and chooses the next step. The agent coordinates the work. The numerical tool supplies the engineering result. An error can also guide the next request.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

Who calculates the electrical result?

**Answer**

The numerical tool. The agent coordinates the requests and reads the returned evidence.
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
<span class="pageno">3 / 69</span></div>

<!--
**Say**

A tool does one job. An agent can connect several jobs using their results. A solver can answer a well-defined study request. The agent’s job is deciding which permitted request should come next.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

What does the agent add to one tool call?

**Answer**

It can choose and connect permitted next steps using the returned results.
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
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_voltage.svg" alt="Teaching adaptation. L2 runs Python; L10B replays saved model choices." style="height:340px;max-height:340px"><figcaption>Teaching adaptation. L2 runs Python; L10B replays saved model choices.</figcaption></figure><ul><li>Compare possible settings, then check voltage and line current.</li><li>The agent can organize these trials and report the checked options.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.19; Classroom Labs L2.</a></div>
<span class="pageno">4 / 69</span></div>

<!--
**Say**

Compare possible settings, then check voltage and line current. The agent can organize these trials and report the checked options. Think of several possible solar settings on the operator’s desk. Each candidate needs the same limit checks before comparison.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 19; keep the notebook in order.

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

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Give the agent a goal and clear limits</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_rules.svg" alt="Grid teaching adaptation of Stanford’s task-specification concept." style="height:310px;max-height:310px"><figcaption>Grid teaching adaptation of Stanford’s task-specification concept.</figcaption></figure><ul><li>State the goal, allowed tools and stopping rules.</li><li>Keep the operator’s review step explicit.</li></ul></div>
<div class="sources">Source: <a href="https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40.</a></div>
<span class="pageno">5 / 69</span></div>

<!--
**Say**

State the goal, allowed tools and stopping rules. Keep the operator’s review step explicit. These rules belong to the application and operating process. A persuasive model response cannot change them.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

Who sets the limits and allowed actions?

**Answer**

The application and operating process, with the operator’s stated task and authority.
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
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_restoration.svg" alt="L6: same network and limits, different service goals." style="height:340px;max-height:340px"><figcaption>L6: same network and limits, different service goals.</figcaption></figure><ul><li>The operator sets the service priority.</li><li>That priority changes what we ask the restoration tool to do.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40; Classroom Labs L6.</a></div>
<span class="pageno">6 / 69</span></div>

<!--
**Say**

The operator sets the service priority. That priority changes what we ask the restoration tool to do. For example, serving more total power can differ from serving more critical demand. The operator must state the intended goal.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY**

Show the slide only. Run L6 later on slide 37; keep the notebook in order.

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

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Keep three jobs clear</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_three_jobs.svg" alt="Adapted principle: language, calculation and human review have different jobs." style="height:310px;max-height:310px"><figcaption>Adapted principle: language, calculation and human review have different jobs.</figcaption></figure><ul><li>The agent requests a study. The tool calculates. The operator reviews the result.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53.</a></div>
<span class="pageno">7 / 69</span></div>

<!--
**Say**

The agent requests a study. The tool calculates. The operator reviews the result. Keep the three responsibilities separate when reading the examples. A fluent explanation is not a substitute for the calculation.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

Which job belongs to the operator?

**Answer**

Reviewing the evidence and deciding the next authorized step.
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
<div class="content"><figure class="native-diagram"><img src="/diagrams/stanford_colab_cyber.svg" alt="L8 checks fit. L9 requires a trust assumption before proposing recovery." style="height:340px;max-height:340px"><figcaption>L8 checks fit. L9 requires a trust assumption before proposing recovery.</figcaption></figure><ul><li>A good fit alone does not prove the readings are true.</li><li>The agent can organize checks and flag missing evidence.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53; Classroom Labs L8–L9.</a></div>
<span class="pageno">8 / 69</span></div>

<!--
**Say**

A good fit alone does not prove the readings are true. The agent can organize checks and flag missing evidence. Later we will change readings in a small model and compare the alarm with the resulting estimation error.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY**

Show the slide only. Run L8 later on slide 51; keep the notebook in order.

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

<h1>Use one notebook for all three cases</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_one_notebook.svg" alt="Classroom Labs is the only required notebook." style="height:330px;max-height:330px"><figcaption>Classroom Labs is the only required notebook.</figcaption></figure><p class="activity-link"><a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Open Classroom Labs in Google Colab</a></p><ul><li>Open Classroom Labs and save your own copy.</li><li>We will use it throughout the workshop.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">9 / 69</span></div>

<!--
**Say**

Open Classroom Labs and save your own copy. We will use it throughout the workshop. Other notebooks on the website are supporting resources. Classroom Labs is the one required notebook for this session.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN**

Open Classroom Labs and save a copy. Run setup on slide 10, not the later lesson cells.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Start Colab in three steps</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_ready.svg" alt="Setup first, then L0 and L1." style="height:315px;max-height:315px"><figcaption>Setup first, then L0 and L1.</figcaption></figure><ul><li>Save a copy, connect a CPU and run setup.</li><li>Wait for Ready, then run L0 and L1.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">10 / 69</span></div>

<!--
**Say**

Save a copy, connect a CPU and run setup. Wait for Ready, then run L0 and L1. Colab gives you a temporary computer. After a runtime reset, rerun setup and the earlier cells to recreate their variables.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

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

<h1>Run a cell, then read its output</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_cell_loop.svg" alt="Illustration of a code cell. Run the full L2 cell." style="height:330px;max-height:330px"><figcaption>Illustration of a code cell. Run the full L2 cell.</figcaption></figure><ul><li>Find the L heading and run the whole cell.</li><li>After changing an input, run that cell again.</li></ul></div>
<div class="sources">Source: <a href="https://research.google.com/colaboratory/faq.html">Google Colab FAQ; Classroom Labs L2, cell classroom-007.</a></div>
<span class="pageno">11 / 69</span></div>

<!--
**Say**

Find the L heading and run the whole cell. After changing an input, run that cell again. The play button runs the cell. The output below it belongs to the last completed run, so an edit alone changes nothing.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 19; keep the notebook in order.

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

<h1>Python runs the default lab</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11</pre><ul><li>In Colab, run L0 with both switches False. Python runs the calculations.</li><li>The Llama examples use saved replies. No live model is needed.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">12 / 69</span></div>

<!--
**Say**

In Colab, run L0 with both switches False. Python runs the calculations. The Llama examples use saved replies. No live model is needed.

**Show**

Locate L0 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

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

<h1>Does the saved result still match?</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L1_binding.png" alt="Reference L1 output. Only the unchanged request and command match." style="max-height:345px;height:auto"><figcaption>Reference L1 output. Only the unchanged request and command match.</figcaption></figure></div><ul><li>Run L1. Only the unchanged request should match its saved result.</li><li>Changed inputs or actions need a new check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">13 / 69</span></div>

<!--
**Say**

Run L1. Only the unchanged request should match its saved result. Changed inputs or actions need a new check.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

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

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Case 1: which solar settings should we use?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_voltage_problem.svg" alt="Concept sketch. First run the tools; later replay saved agent decisions." style="height:310px;max-height:310px"><figcaption>Concept sketch. First run the tools; later replay saved agent decisions.</figcaption></figure><ul><li>Choose settings that keep voltage and line current within the allowed range.</li><li>An agent can organize the trials and return checked options.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">14 / 69</span></div>

<!--
**Say**

Imagine an operator comparing possible settings for solar units. Each choice changes power flows. The job is to find an acceptable option while respecting voltage, line-current and unit limits. An agent can organize the requests and responses, while the tool calculates the electrical effects. We first learn those tools in Colab, then inspect saved agent decisions.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 19; keep the notebook in order.

**Expected result**

No new notebook output on this slide.

**Ask**

What must a proposed solar setting respect?

**Answer**

The checked voltage, line-current and solar-unit limits for the stated model.
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

<h1>Two tools suggest different settings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_two_proposals.svg" alt="MPC: model predictive control. SAC: soft actor-critic. Both proposals need the same checks." style="height:310px;max-height:310px"><figcaption>MPC: model predictive control. SAC: soft actor-critic. Both proposals need the same checks.</figcaption></figure><ul><li>MPC plans with a model. SAC uses a previously trained controller.</li><li>Treat both outputs as proposals that need the same electrical checks.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">15 / 69</span></div>

<!--
**Say**

MPC plans with a model. SAC uses a previously trained controller. Treat both outputs as proposals that need the same electrical checks. MPC means model predictive control. SAC means soft actor-critic, a learned controller. You do not need their algorithms to follow this lab: both simply supply settings for the same check.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

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

<h1>How the agent helps with solar settings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_voltage_agent.svg" alt="Concept map. Colab runs the tools; L10B replays the agent decisions." style="height:310px;max-height:310px"><figcaption>Concept map. Colab runs the tools; L10B replays the agent decisions.</figcaption></figure><ul><li>The agent requests a study and reads the returned checks.</li><li>It can try another allowed option or ask the operator for help.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json">Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.</a></div>
<span class="pageno">16 / 69</span></div>

<!--
**Say**

Follow the arrows from the operator’s goal to the returned result. If a check fails, the agent can request another permitted trial. If evidence is missing, it can stop and ask. The useful behavior is the choice made after reading the tool result. The tool still performs the electrical calculation.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

What can happen after a failed trial?

**Answer**

Request another permitted trial, ask for missing evidence or stop for review.
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

<h1>The study changes two solar settings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_solar_controls.svg" alt="Teaching view of the model’s two controls. Inverter capacity is also a limit." style="height:310px;max-height:310px"><figcaption>Teaching view of the model’s two controls. Inverter capacity is also a limit.</figcaption></figure><ul><li>a sets active-power output. b sets voltage-support output.</li><li>The tool checks voltage, line current and the solar unit’s capacity.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">17 / 69</span></div>

<!--
**Say**

a sets active-power output. b sets voltage-support output. The tool checks voltage, line current and the solar unit’s capacity. Active power supplies energy. Reactive power supports voltage. The inverter’s shared capacity means these settings cannot be chosen independently without checking.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 19; keep the notebook in order.

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

<h1>A Python function can be a tool</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/agent_python_tool.svg" alt="L2 calls lab.voltage_lab directly. Agent coordination is shown in the saved study." style="height:350px;max-height:350px"><figcaption>L2 calls lab.voltage_lab directly. Agent coordination is shown in the saved study.</figcaption></figure><ul><li>It receives inputs, runs calculations and returns results.</li><li>L2 calls this function directly. The saved agent example shows who requests it.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">18 / 69</span></div>

<!--
**Say**

It receives inputs, runs calculations and returns results. L2 calls this function directly. The saved agent example shows who requests it. A tool does not have to be another AI model. Here it is ordinary Python code that calls the numerical study and returns structured results.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY**

Show the slide only. Run L2 later on slide 19; keep the notebook in order.

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

<h1>Two solar proposals, one set of checks</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)</pre><ul><li>Run L2 with the default settings.</li><li>Look for pass/fail, current used and score J. Lower J is better after checks pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">19 / 69</span></div>

<!--
**Say**

Run L2 with the default settings. Look for pass/fail, current used and score J. Lower J is better after checks pass. Look for feasible, max_allowed_current_pct and current_step_J in the notebook. These mean the checked limits pass, current used and the comparison score.

**Show**

Locate L2 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN**

Run the full L2 cell at LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

Exact cells: classroom-007. Run the whole cell, not only the slide excerpt.

**Expected result**

Both default proposals pass; current use is about 73.62% for MPC and 51.68% for SAC.
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
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_plot.png" alt="Reference L2 plots. Rerun for your chosen inputs." style="max-height:345px;height:auto"><figcaption>Reference L2 plots. Rerun for your chosen inputs.</figcaption></figure></div><ul><li>Left: voltages should stay in the allowed band.</li><li>Right: current should stay below 100% of the allowance.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">20 / 69</span></div>

<!--
**Say**

Left: voltages should stay in the allowed band. Right: current should stay below 100% of the allowance. A value below the current line does not replace the voltage check. The same candidate must satisfy every required check.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

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

<h1>Both pass; MPC has the lower score</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_table.png" alt="Reference L2 output at load scale 1.0 and current allowance 0.80." style="max-height:345px;height:auto"><figcaption>Reference L2 output at load scale 1.0 and current allowance 0.80.</figcaption></figure></div><ul><li>MPC: 73.62% current use; score J about 0.03110.</li><li>Saved SAC: 51.68% current use; score J about 0.43643.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">21 / 69</span></div>

<!--
**Say**

MPC: 73.62% current use; score J about 0.03110. Saved SAC: 51.68% current use; score J about 0.43643. SAC uses less current, but MPC has the lower cost score. This is why we must name the goal instead of selecting the smallest number in any column.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

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

<div class="lesson teaching rigorous exercise-slide">

<h1>Exercise 1: lower the current allowance</h1>
<div class="content"><pre class="source-excerpt">RATING_FRACTION = 0.75</pre><ul><li>In L2, change RATING_FRACTION from 0.80 to 0.75. Predict, then rerun.</li><li>Compare pass/fail, current use and score J for both methods.</li><li>Does this check cover the whole medium- and low-voltage network?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">22 / 69</span></div>

<!--
**Say**

In L2, change RATING_FRACTION from 0.80 to 0.75. Predict, then rerun. Compare pass/fail, current use and score J for both methods. Does this check cover the whole medium- and low-voltage network?

**Show**

Show the question for three minutes: predict for one, then edit and run for two. Advance once for the worked answer.

**Colab: EDIT AND RERUN**

Change only RATING_FRACTION to 0.75. Predict, then rerun all of L2. Give this exercise four minutes.

Exact cells: classroom-007. Run the whole cell, not only the slide excerpt.

**Expected result**

MPC current use is about 78.53%; SAC about 54.85%; both pass this MV test.

**Ask**

In L2, change RATING_FRACTION from 0.80 to 0.75. Predict, then rerun. Compare pass/fail, current use and score J for both methods. Does this check cover the whole medium- and low-voltage network?

**Answer**

MPC has the lower score; SAC uses less current. The score considers more than current alone. This check covers the medium-voltage model. The wider network needs a wider study. At the exercise settings, MPC uses 78.53% of the allowance and SAC uses 54.85%. Both pass. Their current-step scores are about 0.03110 and 0.43246.
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Exercise 1 answer: both options still pass</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/exercise_voltage_solution.svg" alt="Fresh L2 exercise results. Current is shown relative to the changed allowance." style="height:310px;max-height:310px"><figcaption>Fresh L2 exercise results. Current is shown relative to the changed allowance.</figcaption></figure><ul><li>MPC has the lower score; SAC uses less current. The score considers more than current alone.</li><li>This check covers the medium-voltage model. The wider network needs a wider study.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; fresh numerical check at rating fraction 0.75.</a></div>
<span class="pageno">23 / 69</span></div>

<!--
**Say**

MPC has the lower score; SAC uses less current. The score considers more than current alone. This check covers the medium-voltage model. The wider network needs a wider study. At the exercise settings, MPC uses 78.53% of the allowance and SAC uses 54.85%. Both pass. Their current-step scores are about 0.03110 and 0.43246.

**Show**

Advance from the exercise only after learners try it. Read the verified values, explain why the outcome occurs and answer every part of the question.

**Colab: INSPECT / RESET**

Use the output already produced for the exercise. Restore RATING_FRACTION=0.80 and rerun all of L2 before continuing.

**Expected result**

MPC has the lower score J. The saved SAC actor uses less current; current use alone is not the objective. Both checks cover the default MV model. They do not establish full MV/LV or dynamic performance.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Less current does not mean the best option</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_voltage_tradeoff.svg" alt="Exercise values at RATING_FRACTION=0.75; a uses inverter rating as its base." style="height:310px;max-height:310px"><figcaption>Exercise values at RATING_FRACTION=0.75; a uses inverter rating as its base.</figcaption></figure><ul><li>Here SAC also uses less solar output.</li><li>The goal values generation as well as limits. Compare the score after checks pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L2, cell classroom-007; verified default and exercise outputs.</a></div>
<span class="pageno">24 / 69</span></div>

<!--
**Say**

Here SAC also uses less solar output. The goal values generation as well as limits. Compare the score after checks pass. The active-power setting is about 0.9603 for MPC and 0.3431 for SAC in this exercise. Lower solar output can reduce current but also increase the stated cost.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

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

<h1>Back to the starting values</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80</pre><ul><li>Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Rerun L2.</li><li>The next cells use a separate saved case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">25 / 69</span></div>

<!--
**Say**

Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Rerun L2. The next cells use a separate saved case. Resetting keeps the class together. The following saved case has its own original inputs; your changed L2 settings do not rewrite it.

**Show**

Locate L2 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

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

<h1>Separate a new calculation from a replay</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_run_replay.svg" alt="A replay keeps its original inputs, decisions and results." style="height:310px;max-height:310px"><figcaption>A replay keeps its original inputs, decisions and results.</figcaption></figure><ul><li>Your inputs produce new numerical results.</li><li>Saved replies show past model decisions; editing L2 does not change them.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md">Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.</a></div>
<span class="pageno">26 / 69</span></div>

<!--
**Say**

Your inputs produce new numerical results. Saved replies show past model decisions; editing L2 does not change them. A fresh calculation answers the inputs you just supplied. A replay shows what happened previously. Both are useful, but they answer different questions.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

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

<h1>What did the saved models choose?</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">pool = lab.saved_pool(&#x27;test_01&#x27;)</pre><ul><li>Run L3 to see what the models requested for the saved case.</li><li>This displays old replies; it makes no new model call.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">27 / 69</span></div>

<!--
**Say**

Run L3 to see what the models requested for the saved case. This displays old replies; it makes no new model call. Read the request, reason and recorded time as a historical record. The model is not responding to your new L2 input.

**Show**

Locate L3 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

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

<h1>Different replies can request the same action</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_canonical_trial.svg" alt="Three saved replies request two different trials." style="height:305px;max-height:305px"><figcaption>Three saved replies request two different trials.</figcaption></figure><ul><li>Group requests that describe the same settings.</li><li>A vote chooses what to test next. The electrical check still has to run.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">28 / 69</span></div>

<!--
**Say**

Group requests that describe the same settings. A vote chooses what to test next. The electrical check still has to run. Wording alone should not create extra votes for the same physical operation. The numerical check still determines whether the selected setting passes.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>A fresh check of the chosen proposal</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">selected_trials = lab.trial_saved_selection(pool)</pre><ul><li>Run L4 to check the chosen proposal again in its original case.</li><li>Both selectors choose the same action here, and the fresh electrical checks pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">29 / 69</span></div>

<!--
**Say**

Run L4 to check the chosen proposal again in its original case. Both selectors choose the same action here, and the fresh electrical checks pass. The selection score and the engineering check do different jobs. A selected action must still be checked.

**Show**

Locate L4 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN**

Run L4 after L3 without changing the case ID.

Exact cells: classroom-013. Run the whole cell, not only the slide excerpt.

**Expected result**

Both selectors choose RELAX_Q_10_PERCENT. Both new electrical checks pass.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Which part of the grid was checked?</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)</pre><ul><li>Run L5 with the default settings.</li><li>It checks the medium-voltage (MV) part of the saved case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">30 / 69</span></div>

<!--
**Say**

Run L5 with the default settings. It checks the medium-voltage (MV) part of the saved case. The wider OpenDSS study is disabled by default. This cell therefore supports a medium-voltage claim only.

**Show**

Locate L5 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

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

<h1>A PASS covers only what was checked</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L5_scope.png" alt="Reference L5 result covers medium voltage only." style="max-height:345px;height:auto"><figcaption>Reference L5 result covers medium voltage only.</figcaption></figure></div><ul><li>A limited model cannot answer a wider grid question.</li><li>Request the missing study or return HOLD.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">31 / 69</span></div>

<!--
**Say**

A limited model cannot answer a wider grid question. Request the missing study or return HOLD. A checked part of a network does not stand for every device or every operating limit. Ask for the check needed by the actual decision.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

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

<h1>Recorded example: the first option fails</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_1.png" alt="" style="max-height:380px;height:auto"><figcaption></figcaption></figure></div><ul><li>This saved study is different from your L2 run.</li><li>Llama asks for a SAC check. The tool reports too much current.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 1; full record in source guide.</a></div>
<span class="pageno">32 / 69</span></div>

<!--
**Say**

This saved study is different from your L2 run. Llama asks for a SAC check. The tool reports too much current. This is a preview of a different saved study, not a continuation of the passing L2 results. The recorded tool result reports a current-limit failure. The next agent choice follows that evidence.

**Show**

Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 64; keep the notebook in order.

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

<h1>Recorded example: request another option</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_2.png" alt="" style="max-height:380px;height:auto"><figcaption></figcaption></figure></div><ul><li>Llama asks the tool to check the existing MPC fallback.</li><li>The returned electrical checks pass for this saved case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 2; full record in source guide.</a></div>
<span class="pageno">33 / 69</span></div>

<!--
**Say**

Llama asks the tool to check the existing MPC fallback. The returned electrical checks pass for this saved case. The agent requests a plan that already exists rather than inventing its electrical outcome. The tool calculates the check and returns the evidence.

**Show**

Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 64; keep the notebook in order.

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

<h1>Recorded example: return to the operator</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_voltage_3.png" alt="" style="max-height:380px;height:auto"><figcaption></figcaption></figure></div><ul><li>The agent returns the checked proposal and its conditions.</li><li>Human review is still pending. No equipment command is sent.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: voltage replay, recorded call 3; full record in source guide.</a></div>
<span class="pageno">34 / 69</span></div>

<!--
**Say**

The agent returns the checked proposal and its conditions. Human review is still pending. No equipment command is sent. The result is a recommendation for review. The record still shows human acknowledgement pending and equipment dispatch disabled.

**Show**

Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 64; keep the notebook in order.

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

<h1>Case 2: who gets power after a fault?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_restoration_problem.svg" alt="Six-node lab graph. Cyan marks critical loads; dashed links are backup options." style="height:310px;max-height:310px"><figcaption>Six-node lab graph. Cyan marks critical loads; dashed links are backup options.</figcaption></figure><ul><li>A fault removes a supply path. Available capacity limits what can be restored.</li><li>The operator sets priorities; the agent can request and check restoration options.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">35 / 69</span></div>

<!--
**Say**

A fault removes one normal supply path. Alternative paths have limited capacity, so the operator must choose what to restore. Serving critical demand first can differ from maximizing the total power served. The agent can carry that priority into a study request, collect the result and request a new study when the situation changes.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY**

Show the slide only. Run L6 later on slide 37; keep the notebook in order.

**Expected result**

No new notebook output on this slide.

**Ask**

Could most total power and most critical service differ?

**Answer**

Yes. Limited capacity can force a trade-off, so the goal must be stated.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>How the agent helps restore service</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_restoration_agent.svg" alt="Concept map. L6 runs the solver directly; L10B replays a separate saved agent study." style="height:310px;max-height:310px"><figcaption>Concept map. L6 runs the solver directly; L10B replays a separate saved agent study.</figcaption></figure><ul><li>Choose the goal: critical loads first, or the most total power.</li><li>The agent can request a study, read the trade-off and ask for a new study when limits change.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">36 / 69</span></div>

<!--
**Say**

The operator supplies the goal. The numerical solver chooses loads under the network rules. An agent could manage the study request and read its result, but it should not invent the service priority. L6 runs the tools directly; the recorded agent example comes later.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY**

Show the slide only. Run L6 later on slide 37; keep the notebook in order.

**Expected result**

No new notebook output on this slide.

**Ask**

Who chooses the service priority?

**Answer**

The operator supplies the priority; the solver and agent must preserve it.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Two goals for restoring power</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)</pre><ul><li>Run L6 to choose which loads receive power under each goal.</li><li>MILP chooses whole loads; a separate calculation checks its result.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">37 / 69</span></div>

<!--
**Say**

Run L6 to choose which loads receive power under each goal. MILP chooses whole loads; a separate calculation checks its result. MILP is a solver for choices such as whether an entire load is restored. The independent search checks the small teaching model’s objective result.

**Show**

Locate L6 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN**

Run L6 with CAPACITIES_KW=(40.,60.,80.,100.,120.).

Exact cells: classroom-018. Run the whole cell, not only the slide excerpt.

**Expected result**

The priority MILP agrees with exhaustive enumeration. At 40 kW, compare 130/90 with 140/30 kW total/critical.
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<h1>Read total and critical service</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_plot.png" alt="Reference L6 results. Both goals use the same network." style="max-height:345px;height:auto"><figcaption>Reference L6 results. Both goals use the same network.</figcaption></figure></div><ul><li>Critical-first goal: 130 kW total, including 90 kW for critical loads.</li><li>Most-total-power goal: 140 kW total, including 30 kW for critical loads.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">38 / 69</span></div>

<!--
**Say**

Critical-first goal: 130 kW total, including 90 kW for critical loads. Most-total-power goal: 140 kW total, including 30 kW for critical loads. Read the 40 kW tie setting first. The left chart shows total service and the right shows critical service. The network is the same; the service goal changes the result.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

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

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Check the restoration plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_restoration_checks.svg" alt="Checks on the active-power model. AC and field-operation checks remain separate." style="height:310px;max-height:310px"><figcaption>Checks on the active-power model. AC and field-operation checks remain separate.</figcaption></figure><ul><li>Keep the faulted branch out of service. Check supply paths and capacity.</li><li>Voltage, protection and field switching need separate studies.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">39 / 69</span></div>

<!--
**Say**

Keep the faulted branch out of service. Check supply paths and capacity. Voltage, protection and field switching need separate studies. This small exercise uses an active-power service model. The agent can request and compare its results, while the operator must review the remaining work.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

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

<h1>Exercise 2: increase tie capacity</h1>
<div class="content"><pre class="source-excerpt">CAPACITIES_KW = (40., 60., 80., 100., 120., 180.)</pre><ul><li>Add 180. to CAPACITIES_KW. Keep 40. first. Predict, then rerun L6.</li><li>Compare total and critical power at 40 and 180 kW.</li><li>At which tested capacity do the two goals first give the same result?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">40 / 69</span></div>

<!--
**Say**

Add 180. to CAPACITIES_KW. Keep 40. first. Predict, then rerun L6. Compare total and critical power at 40 and 180 kW. At which tested capacity do the two goals first give the same result?

**Show**

Show the question for three minutes: predict for one, then edit and run for two. Advance once for the worked answer.

**Colab: EDIT AND RERUN**

Append 180. to CAPACITIES_KW, keeping 40. first. Rerun all of L6. Give this exercise four minutes.

Exact cells: classroom-018. Run the whole cell, not only the slide excerpt.

**Expected result**

At 180 kW, both goals serve 250 kW total and 90 kW critical.

**Ask**

Add 180. to CAPACITIES_KW. Keep 40. first. Predict, then rerun L6. Compare total and critical power at 40 and 180 kW. At which tested capacity do the two goals first give the same result?

**Answer**

At 40 kW, the priority goal serves 90 kW critical instead of 30 kW, with less total service. The goals first match at the tested 80 kW. At 180 kW, both serve 250 kW total and 90 kW critical. The goals first match at 80 kW among the tested capacities. At 180 kW both restore 250 kW total, including 90 kW critical. This discrete sweep does not identify an exact continuous crossover.
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Exercise 2 answer: capacity changes the trade-off</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/exercise_restoration_solution.svg" alt="Fresh L6 results. Cyan shows critical service; blue shows other service." style="height:310px;max-height:310px"><figcaption>Fresh L6 results. Cyan shows critical service; blue shows other service.</figcaption></figure><ul><li>At 40 kW, the priority goal serves 90 kW critical instead of 30 kW, with less total service.</li><li>The goals first match at the tested 80 kW. At 180 kW, both serve 250 kW total and 90 kW critical.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; fresh MILP and exhaustive-check sweep.</a></div>
<span class="pageno">41 / 69</span></div>

<!--
**Say**

At 40 kW, the priority goal serves 90 kW critical instead of 30 kW, with less total service. The goals first match at the tested 80 kW. At 180 kW, both serve 250 kW total and 90 kW critical. The goals first match at 80 kW among the tested capacities. At 180 kW both restore 250 kW total, including 90 kW critical. This discrete sweep does not identify an exact continuous crossover.

**Show**

Advance from the exercise only after learners try it. Read the verified values, explain why the outcome occurs and answer every part of the question.

**Colab: INSPECT / RESET**

Use the exercise output. Keep 40 first; restore the original list and rerun L6 before L7.

**Expected result**

At 40 kW, priorities give more critical service: 90 kW instead of 30 kW, with less total service. The goals match from 80 kW in the tested list. At 180 kW, both serve 250 kW total, including 90 kW critical.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>A changed request needs a new check</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">print(&#x27;Original contract:&#x27;, lab.bound_to(rest_request, rest_candidate, rest_evidence))
print(&#x27;Changed rating with old evidence:&#x27;, lab.bound_to(new_rest_request, rest_candidate, rest_evidence))</pre><ul><li>Restore the original capacity list and rerun L6.</li><li>Run L7: the requested capacity changes from 40 kW to 20 kW.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">42 / 69</span></div>

<!--
**Say**

Restore the original capacity list and rerun L6. Run L7: the requested capacity changes from 40 kW to 20 kW. Run the complete L7 cell after restoring L6. It compares an old checked result with a request that now has a smaller capacity.

**Show**

Locate L7 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

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

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>A new limit needs a new study</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_stale_result.svg" alt="A failed input match asks for a new study; it does not establish physical infeasibility." style="height:310px;max-height:310px"><figcaption>A failed input match asks for a new study; it does not establish physical infeasibility.</figcaption></figure><ul><li>The original request matches the old result. The changed request does not.</li><li>Hold the old proposal, calculate again and check the new result.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">43 / 69</span></div>

<!--
**Say**

The original request matches the old result. The changed request does not. Hold the old proposal, calculate again and check the new result. The two L7 match tests return True and False. This tests whether evidence belongs to the request; it does not prove that a new plan is physically feasible.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

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

<h1>The agent keeps the operator’s goal</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_plan.svg" alt="Proposed agent use. L6 itself runs Python." style="height:305px;max-height:305px"><figcaption>Proposed agent use. L6 itself runs Python.</figcaption></figure><ul><li>The operator sets priorities. The solver selects loads.</li><li>The agent can request the solve and explain the returned service trade-off.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">44 / 69</span></div>

<!--
**Say**

The operator sets priorities. The solver selects loads. The agent can request the solve and explain the returned service trade-off. Keeping the goal fixed matters when many studies are requested. The agent should return the achieved total and critical service with each result.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY**

Show the slide only. Run L6 later on slide 37; keep the notebook in order.

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

<div class="lesson teaching rigorous figure-slide">

<h1>Recorded example: try more service</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_14.png" alt="" style="max-height:380px;height:auto"><figcaption></figcaption></figure></div><ul><li>This saved feeder study is different from L6.</li><li>Llama requests another plan. The tool reports more service and passing checks.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 14; full record in source guide.</a></div>
<span class="pageno">45 / 69</span></div>

<!--
**Say**

This saved feeder study is different from L6. Llama requests another plan. The tool reports more service and passing checks. The saved feeder example is larger than the L6 exercise and has different numbers. Watch the request, returned check and next choice rather than comparing its total kW with L6.

**Show**

Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 64; keep the notebook in order.

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

<h1>Recorded example: the tool rejects a trial</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_15.png" alt="" style="max-height:380px;height:auto"><figcaption></figcaption></figure></div><ul><li>The next trial carries too much current.</li><li>It cannot replace the previous passing option.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 15; full record in source guide.</a></div>
<span class="pageno">46 / 69</span></div>

<!--
**Say**

The next trial carries too much current. It cannot replace the previous passing option. The numerical guard excludes the overloaded trial. Restoring more load is useful only when the required checks also pass.

**Show**

Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 64; keep the notebook in order.

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

<h1>Recorded example: correct a wrong ranking</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_restoration_16.png" alt="" style="max-height:380px;height:auto"><figcaption></figcaption></figure></div><ul><li>Llama puts two passing plans in the wrong order.</li><li>Python keeps the lower-cost plan and checks it again.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: restoration replay, recorded call 16; full record in source guide.</a></div>
<span class="pageno">47 / 69</span></div>

<!--
**Say**

Llama puts two passing plans in the wrong order. Python keeps the lower-cost plan and checks it again. Here the lower costs are negative: about minus 6109 is lower than minus 5509. The model’s order is wrong, so Python corrects it and rechecks the retained plan.

**Show**

Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 64; keep the notebook in order.

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

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Case 3: can we trust these readings?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_cyber_problem.svg" alt="Concept sketch. L8 uses a small four-bus DC model." style="height:310px;max-height:310px"><figcaption>Concept sketch. L8 uses a small four-bus DC model.</figcaption></figure><ul><li>Wrong readings can still look consistent with the model.</li><li>The agent can request checks, but action still needs a trusted basis.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">48 / 69</span></div>

<!--
**Say**

The operator sees measurements, not the true system state. Several altered readings can agree with each other and still lead to a wrong estimate. An agent can request tests and organize the evidence, but it cannot create a trusted measurement source. The lab uses known simulated changes so that we can compare fit with actual estimation error.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY**

Show the slide only. Run L8 later on slide 51; keep the notebook in order.

**Expected result**

No new notebook output on this slide.

**Ask**

Does a good fit prove a reading is true?

**Answer**

No. Coordinated wrong readings can fit the model while giving a wrong estimated state.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>How the agent helps with suspicious readings</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_cyber_agent.svg" alt="Concept map. L9 calculates; L10B replays saved Llama requests and returned tool evidence." style="height:310px;max-height:310px"><figcaption>Concept map. L9 calculates; L10B replays saved Llama requests and returned tool evidence.</figcaption></figure><ul><li>The agent can request the checks and keep missing evidence visible.</li><li>The operator reviews trust, model coverage and the proposed correction.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">49 / 69</span></div>

<!--
**Say**

Follow the information from the readings to the proposed correction. Without the required trusted data, the workflow returns HOLD. With that assumption, the tool can calculate a candidate. The agent can request these steps and explain missing checks; the operator must still assess the premise and decide the authorized next step.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

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

<h1>Mismatch is only one check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_mismatch.svg" alt="Mismatch J here has a different meaning from control cost J in the voltage lab." style="height:310px;max-height:310px"><figcaption>Mismatch J here has a different meaning from control cost J in the voltage lab.</figcaption></figure><ul><li>Mismatch J measures how well the model fits the readings.</li><li>The simulation lets us measure how wrong the estimate is (state error).</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">50 / 69</span></div>

<!--
**Say**

Mismatch J measures how well the model fits the readings. The simulation lets us measure how wrong the estimate is (state error). In the cyber lab, J is a mismatch statistic, not the control cost used in the voltage lab. A low mismatch says the model fits the readings; it does not authenticate them.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY**

Show the slide only. Run L8 later on slide 51; keep the notebook in order.

**Expected result**

No new notebook output on this slide.

**Ask**

What does a low mismatch tell us?

**Answer**

That the model fits the supplied readings, not that the readings are authentic.
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

<h1>Two ways readings can be misleading</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)</pre><ul><li>Run L8 with the default settings.</li><li>Compare one biased reading with a coordinated change across several readings.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">51 / 69</span></div>

<!--
**Say**

Run L8 with the default settings. Compare one biased reading with a coordinated change across several readings. The isolated pattern changes one reading. The coordinated pattern changes several together. We compare the same two questions: did the alarm trigger, and how wrong was the estimated state?

**Show**

Locate L8 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN**

Run L8 with ATTACK_SCALES=(0.,.25,.5,1.,1.5).

Exact cells: classroom-023. Run the whole cell, not only the slide excerpt.

**Expected result**

A coordinated Hc attack preserves a small residual while offline state error grows.
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
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L8_plot.png" alt="Reference L8 plots: model fit and estimation error are different checks." style="max-height:345px;height:auto"><figcaption>Reference L8 plots: model fit and estimation error are different checks.</figcaption></figure></div><ul><li>Left: mismatch and its alarm threshold. Right: error against the simulation’s known truth.</li><li>A quiet alarm can appear alongside a growing error.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">52 / 69</span></div>

<!--
**Say**

Left: mismatch and its alarm threshold. Right: error against the simulation’s known truth. A quiet alarm can appear alongside a growing error. The right plot uses truth known inside the simulation. A real operator usually cannot read that error directly from a live system.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

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

<h1>A coordinated change can escape the alarm</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_hidden_error.svg" alt="L8 reference values at attack scale 1. Simulation truth supplies the state error." style="height:310px;max-height:310px"><figcaption>L8 reference values at attack scale 1. Simulation truth supplies the state error.</figcaption></figure><ul><li>At scale 1, one biased reading gives mismatch J=277.50 and an alarm.</li><li>A coordinated change gives J=3.92, no alarm, and 0.02678 rad of state error.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">53 / 69</span></div>

<!--
**Say**

At scale 1, one biased reading gives mismatch J=277.50 and an alarm. A coordinated change gives J=3.92, no alarm, and 0.02678 rad of state error. The coordinated changes preserve a small mismatch even as the estimate moves away from the known state. This is the reason a quiet alarm is incomplete evidence.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

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

<h1>Exercise 3: test a small bias</h1>
<div class="content"><pre class="source-excerpt">ATTACK_SCALES = (0., .10, .25, .5, 1., 1.5)</pre><ul><li>Add .10 to ATTACK_SCALES. Predict, then rerun L8.</li><li>At scale 0.10, compare mismatch J, the alarm and state error.</li><li>Does no alarm prove that the readings are correct?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">54 / 69</span></div>

<!--
**Say**

Add .10 to ATTACK_SCALES. Predict, then rerun L8. At scale 0.10, compare mismatch J, the alarm and state error. Does no alarm prove that the readings are correct?

**Show**

Show the question for three minutes: predict for one, then edit and run for two. Advance once for the worked answer.

**Colab: EDIT AND RERUN**

Add .10 to ATTACK_SCALES. Rerun all of L8 and inspect the isolated-bias row. Give this exercise four minutes.

Exact cells: classroom-023. Run the whole cell, not only the slide excerpt.

**Expected result**

At isolated scale 0.10, J is about 10.14, below the 15.09 threshold; no alarm is not proof of truth.

**Ask**

Add .10 to ATTACK_SCALES. Predict, then rerun L8. At scale 0.10, compare mismatch J, the alarm and state error. Does no alarm prove that the readings are correct?

**Answer**

Both alarms are False at scale 0.10, but both estimates still have error. No alarm means the mismatch is below this threshold. It does not establish data trust. At scale 0.10, the isolated mismatch is about 10.143 and the coordinated mismatch is about 3.920. Both are below 15.086, while their state errors are nonzero.
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Exercise 3 answer: no alarm can hide an error</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/exercise_cyber_solution.svg" alt="Fresh L8 exercise. The error uses truth known inside the simulation." style="height:310px;max-height:310px"><figcaption>Fresh L8 exercise. The error uses truth known inside the simulation.</figcaption></figure><ul><li>Both alarms are False at scale 0.10, but both estimates still have error.</li><li>No alarm means the mismatch is below this threshold. It does not establish data trust.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; fresh four-bus DC residual check at scale 0.10.</a></div>
<span class="pageno">55 / 69</span></div>

<!--
**Say**

Both alarms are False at scale 0.10, but both estimates still have error. No alarm means the mismatch is below this threshold. It does not establish data trust. At scale 0.10, the isolated mismatch is about 10.143 and the coordinated mismatch is about 3.920. Both are below 15.086, while their state errors are nonzero.

**Show**

Advance from the exercise only after learners try it. Read the verified values, explain why the outcome occurs and answer every part of the question.

**Colab: INSPECT / RESET**

Use the output already produced for the exercise. Restore the original ATTACK_SCALES and rerun L8 before the separate fixed L9 recovery case.

**Expected result**

At scale 0.10, both alarms are False. Both state estimates still have error; the coordinated shift has the larger error here. No alarm means J is below this threshold. It does not prove correct data or trusted sensors.
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Back to the original data-bias settings</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)</pre><ul><li>Restore the original attack scales and rerun L8.</li><li>L9 uses a separate fixed recovery case.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">56 / 69</span></div>

<!--
**Say**

Restore the original attack scales and rerun L8. L9 uses a separate fixed recovery case. L9 is deliberately a fixed recovery example. Your L8 sweep is a separate experiment and does not select the L9 correction.

**Show**

Locate L8 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

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

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Trusted readings must come from somewhere</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_trust_choice.svg" alt="The extra readings are assumed trustworthy for this experiment." style="height:310px;max-height:310px"><figcaption>The extra readings are assumed trustworthy for this experiment.</figcaption></figure><ul><li>This example assumes extra trustworthy readings are available.</li><li>Neither the fitting tool nor Llama proves that these readings are authentic.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">57 / 69</span></div>

<!--
**Say**

This example assumes extra trustworthy readings are available. Neither the fitting tool nor Llama proves that these readings are authentic. The lesson supplies a trust assumption so that the numerical task can be studied. The calculation is not a method for proving sensor identity or integrity.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY**

Show the slide only. Run L9 later on slide 58; keep the notebook in order.

**Expected result**

No new notebook output on this slide.

**Ask**

Does Llama authenticate the extra readings?

**Answer**

No. Their trustworthiness is an explicit assumption of this example.
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Does the result say HOLD or PROPOSE?</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)</pre><ul><li>Run L9 and read the status before the proposed adjustment.</li><li>Then check the model’s returned limits and remaining assumptions.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">58 / 69</span></div>

<!--
**Say**

Run L9 and read the status before the proposed adjustment. Then check the model’s returned limits and remaining assumptions. HOLD means a required condition is absent. PROPOSE means the tool can offer a model-based correction for review, not permission to operate equipment.

**Show**

Locate L9 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

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

<h1>Missing trust means HOLD</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L9_trust.png" alt="Reference L9 output for the fixed recovery example." style="max-height:325px;height:auto"><figcaption>Reference L9 output for the fixed recovery example.</figcaption></figure></div><ul><li>Without trusted replacement readings: HOLD.</li><li>With the trust assumption: PROPOSE a 0.121694 p.u. adjustment; the offline model checks pass.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">59 / 69</span></div>

<!--
**Say**

Without trusted replacement readings: HOLD. With the trust assumption: PROPOSE a 0.121694 p.u. adjustment; the offline model checks pass. The passing result depends on the declared trust premise and the simplified model. Zero offline violations is a model result, not a field guarantee.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

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

<h1>The tool calculates a small correction</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/plain_correction.svg" alt="Per unit (p.u.) scales a value by a model base. These flows use the same base." style="height:310px;max-height:310px"><figcaption>Per unit (p.u.) scales a value by a model base. These flows use the same base.</figcaption></figure><ul><li>The solver finds the smallest allowed adjustment that meets the checked branch limits.</li><li>Predicted flow: 0.17000 p.u. Offline check: 0.17046 p.u. Limit: 0.18000 p.u.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">60 / 69</span></div>

<!--
**Say**

The solver finds the smallest allowed adjustment that meets the checked branch limits. Predicted flow: 0.17000 p.u. Offline check: 0.17046 p.u. Limit: 0.18000 p.u. Per unit, written p.u., expresses a value relative to a chosen model base. Compare the predicted and offline checked flow with the same 0.18 limit.

**Show**

Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

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

<h1>Recorded example: request the recovery tool</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_7.png" alt="" style="max-height:380px;height:auto"><figcaption></figcaption></figure></div><ul><li>Llama requests the supplied recovery tool.</li><li>Python calculates a correction using the assumed trusted readings.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: cyber replay, recorded call 7; full record in source guide.</a></div>
<span class="pageno">61 / 69</span></div>

<!--
**Say**

Llama requests the supplied recovery tool. Python calculates a correction using the assumed trusted readings. The permitted tool is already supplied in this example. Llama chooses to request it; Python performs the estimation and correction calculation.

**Show**

Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 64; keep the notebook in order.

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

<h1>Recorded example: keep human review</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/llama_cyber_8.png" alt="" style="max-height:350px;height:auto"><figcaption></figcaption></figure></div><ul><li>The model checks pass; human review is still pending.</li><li>Data trust and operating permission still need review.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom Labs L10B: cyber replay, recorded call 8; full record in source guide.</a></div>
<span class="pageno">62 / 69</span></div>

<!--
**Say**

The model checks pass; human review is still pending. Data trust and operating permission still need review. A model check, human review and permission to operate equipment are separate steps. The record has not completed the latter two.

**Show**

Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY**

Show the slide only. Run L10B later on slide 64; keep the notebook in order.

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

<h1>The saved agent workflow</h1>
<div class="content"><ul><li>Run L10 to inspect the recorded planning, calculation and checking stages.</li><li>Llama chooses and refines trials. Python calculates and checks them.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.</a></div>
<span class="pageno">63 / 69</span></div>

<!--
**Say**

Run L10 to inspect the recorded planning, calculation and checking stages. Llama chooses and refines trials. Python calculates and checks them. The framework summary near the end shows all five roles together. This cell replays saved stages and makes no new model call.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: RUN**

Run all of L10 after L9. Read the case and stage columns in the saved trace.

Exact cells: classroom-028. Run the whole cell, not only the slide excerpt.

**Expected result**

Five stage names appear. Planning and optimizer rows contain actual saved Llama replies; other stages contain Python results.
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>How Llama chooses the next tool</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">SCENARIO = &quot;voltage&quot;  # Change to &quot;restoration&quot; or &quot;cyber&quot;, then rerun this cell.</pre><ul><li>Set SCENARIO to voltage, restoration or cyber, then rerun this cell.</li><li>Read the model’s request and the tool’s response. This is a saved replay.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10B; cell classroom-llama-walkthrough; src/llama_walkthrough.py.</a></div>
<span class="pageno">64 / 69</span></div>

<!--
**Say**

Set SCENARIO to voltage, restoration or cyber, then rerun this cell. Read the model’s request and the tool’s response. This is a saved replay. Run this full cell once for each scenario. The displayed words and tool evidence were recorded earlier; this default demonstration makes no fresh Llama call.

**Show**

Locate L10B in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: REPLAY THREE TIMES**

After L10, run the whole L10B cell for SCENARIO="voltage", then "restoration", then "cyber". Change only that string between runs.

Exact cells: classroom-llama-walkthrough. Run the whole cell, not only the slide excerpt.

**Expected result**

Input, exact model choice and public reason, saved tool result and next step appear. No new LLM call or electrical solve runs.
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

<h1>The operator checks the recommendation ID</h1>
<div class="content code-content"><p class="code-caption">Run the whole cell in Colab</p><pre class="teaching-code">wrong_id = lab.acknowledge(mv_scope, &#x27;wrong-id&#x27;, &#x27;Student operator&#x27;)
readback = lab.acknowledge(mv_scope, mv_scope[&#x27;recommendation_id&#x27;], &#x27;Student operator&#x27;)</pre><ul><li>Leave L11 disabled, then run L12.</li><li>Compare the wrong ID with the matching ID. Equipment control stays off.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">65 / 69</span></div>

<!--
**Say**

Leave L11 disabled, then run L12. Compare the wrong ID with the matching ID. Equipment control stays off. Readback means acknowledging the specific recommendation being reviewed. The wrong identifier must not acknowledge a different recommendation.

**Show**

Locate L12 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

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

<h1>Approval must match the checked study</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L12_packet.png" alt="Reference L12 output. Readback is simulated." style="max-height:345px;height:auto"><figcaption>Reference L12 output. Readback is simulated.</figcaption></figure></div><ul><li>The wider-grid request returns HOLD. The limited teaching request permits a simulated readback.</li><li>A wrong ID fails. This practice sends no equipment commands.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">66 / 69</span></div>

<!--
**Say**

The wider-grid request returns HOLD. The limited teaching request permits a simulated readback. A wrong ID fails. This practice sends no equipment commands. The wider request requires checks the default study does not supply. The narrower teaching packet supports only a simulated acknowledgement, with equipment dispatch remaining False.

**Show**

Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN**

Read the output from the previous run. Compare it with the reference figure; no new cell is needed.
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
<div class="content"><figure class="native-diagram"><img src="/diagrams/ops_review.svg" alt="Proposed control-room use. Study review does not operate equipment." style="height:330px;max-height:330px"><figcaption>Proposed control-room use. Study review does not operate equipment.</figcaption></figure><ul><li>Review the case, tool results, checked limits and missing work.</li><li>Request another study, reject the proposal or take the next authorized step.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Teaching proposal informed by NIST OT guidance and the cited notebook checks.</a></div>
<span class="pageno">67 / 69</span></div>

<!--
**Say**

Review the case, tool results, checked limits and missing work. Request another study, reject the proposal or take the next authorized step. Ask whether the evidence belongs to this case, whether all needed checks are present and what remains unresolved. Those questions support the next human decision.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

What should happen when a required check is missing?

**Answer**

Return the unresolved condition and request the missing study or review before proceeding.
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

<h1>Multi-agent framework used in this workshop</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/workshop_multi_agent.svg" alt="Saved five-role Python workflow. L10 replays its recorded trace." style="height:345px;max-height:345px"><figcaption>Saved five-role Python workflow. L10 replays its recorded trace.</figcaption></figure><ul><li>The five roles share the same case facts and checked results.</li><li>One Llama model handles planning and refinement. Python calculates and checks.</li></ul></div>
<div class="sources">Source: <a href="https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py">Workshop authors. Five-role operator study workflow: proposal_workflow.py and proposal_complete_workflow.json. Public reproducible teaching code, 2026.</a></div>
<span class="pageno">68 / 69</span></div>

<!--
**Say**

This is the framework implemented for the saved study. Awareness reads the case facts. Planning prepares options and uses Llama to select an allowed study. Simulation calculates the result. Verification checks the limits and whether the result matches the case. The Llama optimizer can request a small change or rank passing options. A changed trial loops back through calculation and checking. Python guards the final choice, then the operator reviews it. One Llama model fills two roles. The same framework connects different numerical tools for solar settings, restoration and suspicious readings. L10 displays its saved trace; the default Colab does not launch a live agent team.

**Show**

Trace the five named roles, then the feedback loop. Ask learners to name the numerical tool used in each case. Finish at the final Python check and operator review.

**Colab: NO NEW RUN**

Explain the figure or discuss the output already produced. Do not run ahead.

**Ask**

Which roles use Llama, and what happens after a trial changes?

**Answer**

Planning and the optimizer use the same Llama model. A changed trial needs fresh simulation and verification; Python checks the final choice before operator review.
Nominal duration: 2.5 minutes.

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

<div class="lesson teaching rigorous normal-slide has-diagram">

<h1>Try one change and explain the result</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/lab_one_notebook.svg" alt="Keep the saved replies separate from your new experiment." style="height:310px;max-height:310px"><figcaption>Keep the saved replies separate from your new experiment.</figcaption></figure><p class="activity-link"><a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Open the three cases in Colab</a></p><ul><li>Choose one case. Change one input, rerun and save the result.</li><li>Explain the problem, agent choice, tool result and operator decision.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">69 / 69</span></div>

<!--
**Say**

Choose one case. Change one input, rerun and save the result. Explain the problem, agent choice, tool result and operator decision. Use one case to explain the complete story. State the problem, the agent’s choice, the tool’s returned fact and the operator’s remaining decision.

**Show**

Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN**

No required new run. Learners may repeat one case afterward and save their changed inputs and outputs.

**Ask**

What are the four parts of your explanation?

**Answer**

Problem, agent choice, tool result and operator decision.
Nominal duration: 2.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->
