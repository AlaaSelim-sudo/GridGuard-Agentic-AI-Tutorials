---
theme: default
title: "Hands-on: Three Operator Cases"
info: Follow Classroom Labs through voltage support, service restoration and cyber response, with three exercises
author: GridGuard teaching tutorial
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
<p>Run voltage support, service restoration and cyber response in Classroom Labs</p>
<p>120 minutes · one CPU notebook · three short exercises</p>
<p>IEEE ComSoc theme / Run, change, check and explain</p>
<img class="cover-logo" src="/branding/comsoc-lockup.png" alt="IEEE Communications Society lockup"><small>Independent educational material · IEEE ComSoc theme adaptation</small>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">1 / 59</span></div>

<!--
Open Classroom Labs before the workshop. Participants will run fresh numerical calculations and inspect clearly labeled archived model replies. Use the same notebook for all three cases. If devices are limited, work in pairs: one person runs the cells while the other checks the evidence.
Takeaway: 
Nominal duration: 0.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Open one notebook for all three cases</h1>
<div class="content"><p class="activity-link"><a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Open Classroom Labs in Google Colab</a></p><p class="callout">Classroom_Labs.ipynb</p><ul><li>Open Classroom Labs using the source link below or the website’s first Colab button.</li><li>Save a copy in Drive so you can keep your parameter changes and outputs.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">2 / 59</span></div>

<!--
Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Connect a CPU and run the setup cell</h1>
<div class="content"><ul><li>Connect a standard CPU runtime. Run “Set up Google Colab (CPU)” and wait for Ready.</li><li>Setup retrieves the supporting data, saved weights and records. It installs the required packages.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">3 / 59</span></div>

<!--
For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or model download. If setup stops, reconnect the runtime and rerun setup before starting L0.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Find cells by L label, not by cell number</h1>
<div class="content"><ul><li>Use the section headings L0 through L12 to find the next task.</li><li>Run a whole code cell with its play button or Shift+Enter. Later cells use earlier variables.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">4 / 59</span></div>

<!--
The added Colab setup cells changed the numerical cell positions. Use the L headings and stable cell IDs to find the same source in Colab, Jupyter and these slides. A slide shows only the relevant code fragment. Students should run the complete matching notebook cell.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
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
assert (ROOT / &#x27;data/lindistflow3_network.json&#x27;).exists(), &#x27;Start Jupyter in the tutorial folder&#x27;</pre><ul><li>Keep both switches False. The class uses fresh linear-model calculations and saved model replies.</li><li>If the data check fails, rerun the setup cell before continuing.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">5 / 59</span></div>

<!--
Run all of L0 to import the helpers, configure the plots and initialize the timing record. Keep RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. These settings skip the optional full-feeder OpenDSS route and local model service. They do not make the calculations prerecorded: L2 and L4 through L9 run fresh numerical calculations or checks, while L12 checks the evidence binding and simulated readback.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Know which evidence you are reading</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/common_operator_loop.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>FRESH: calculated now. SAVED POLICY: old weights used for a new proposal.</li><li>ARCHIVED ACTUAL LLM: a previously recorded reply, with its original input and timing.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">6 / 59</span></div>

<!--
The diagram shows responsibilities. Ordinary Python functions perform the engineering calculations; this notebook does not run through LangGraph. A model reply remains an archived event when displayed today. A language model does not replace the power-flow solver, MILP or state estimator.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L1 · classroom-004</div>
<h1>Run L1: does old evidence still match?</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L1_binding.png" alt="Actual executed notebook output; source cell classroom-004. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-004. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Run the cell, then read binding_pass for all three rows.</li><li>Expect True, False, False: changing the load or command invalidates this evidence binding.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">7 / 59</span></div>

<!--
Treat this first check as a content-consistency test, not a physical feasibility test. The first row keeps the request and command unchanged. The next two rows change a request field or command field. A failed binding requires fresh evidence, but does not prove the changed action is infeasible. A matching hash does not authenticate a sensor.
Takeaway: 
Nominal duration: 1.5 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<h1>Use the same cycle in every case</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/common_evidence_binding.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>Predict → run the default → read the result → change one input → rerun.</li><li>Finish by naming the permitted next step and the evidence that supports it.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.</a></div>
<span class="pageno">8 / 59</span></div>

<!--
Pause before showing each output. Ask pairs to write one sentence predicting the change, then compare it with the calculated result. Keep the input values and evidence together. Change only one parameter in the first experiment.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<h1>Keep a short experiment record</h1>
<div class="content"><ul><li>Record the cell label and parameter value you changed.</li><li>Record one result, its model scope and your next decision: continue, recheck or HOLD.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">9 / 59</span></div>

<!--
Participants can add a text cell below an output or use paper notes; no extra software is needed. Each pair should finish with one changed-input experiment that another person can repeat. Explain the result and one limit on the claim. The three cases use different networks and do not form a single utility deployment study.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Voltage: start with L2</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/feeder.png" alt="Synthetic SMART-DS feeder model used by the voltage example; not an operational utility circuit." style="max-height:345px;height:auto"><figcaption>Synthetic SMART-DS feeder model used by the voltage example; not an operational utility circuit.</figcaption></figure></div><ul><li>Study one synthetic feeder. The command controls fleet active and reactive participation.</li><li>Your task: check feasibility first, then compare the current-step objective.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">10 / 59</span></div>

<!--
The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The default backend models MV phases and MV line currents, with idealized LV aggregation. Run L0 and L1 before this cell.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.
Full source: https://data.openei.org/submissions/2981
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Read the control and limits</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_capability.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>a sets active-power participation; b sets reactive-power participation.</li><li>The notebook checks the inverter bounds, modeled voltage range and allowed current.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">11 / 59</span></div>

<!--
The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltage bounds are 0.95 to 1.05 p.u. RATING_FRACTION=0.80 sets the allowed current to 80% of the nominal rating. The displayed current percentage uses that reduced allowance as its denominator. Passing the inverter bounds alone does not establish network feasibility.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
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
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)</pre><ul><li>Run the whole L2 cell. It solves MPC, evaluates the saved SAC proposal and checks both.</li><li>Find feasible, current_step_J and max_allowed_current_pct in the output.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">12 / 59</span></div>

<!--
Start with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. The saved SAC actor produces a new proposal by inference; it is not trained in this cell. Both proposals pass the default classroom checks. MPC has the lower current-step J for this case and objective. This single result does not establish a universal control advantage.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
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
<h1>Read your voltage plots</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_plot.png" alt="Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Left: compare the sorted modeled voltage distributions with the allowed band.</li><li>Right: compare current use with the 100% allowed-current line.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">13 / 59</span></div>

<!--
The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Read feasibility before cost</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L2_table.png" alt="Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Default MPC: PASS, current use 73.62%, current-step J about 0.03110.</li><li>Default saved SAC: PASS, current use 51.68%, J about 0.43643.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">14 / 59</span></div>

<!--
In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous exercise-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Exercise 1: tighten the current allowance</h1>
<div class="content"><pre class="source-excerpt">RATING_FRACTION = 0.75</pre><ul><li>In L2, change only RATING_FRACTION from 0.80 to 0.75. Predict, then rerun L2.</li><li>For each method, report feasible, allowed-current use and current_step_J.</li><li>Does passing this check establish full MV/LV feasibility? Explain your answer.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">15 / 59</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Debrief: a tighter allowance can still pass</h1>
<div class="content"><p class="callout">Both candidates still pass</p><ul><li>At 0.75, both candidates still pass: MPC about 78.53%, SAC about 54.85%.</li><li>A stricter allowance raises utilization here, but it does not force a failure.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">16 / 59</span></div>

<!--
An incorrect prediction is useful evidence, not a failed exercise. Compare the hypothesis with the actual output. Both candidates retain enough headroom in this case. An optimizer may change its command when a constraint changes, so a simple fixed-ratio argument does not apply to every scenario. The model scope has not expanded.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L2 · classroom-007</div>
<h1>Reset L2 before the recorded-choice lesson</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.</p><pre class="teaching-code">LOAD_SCALE = 1.0
RATING_FRACTION = 0.80</pre><ul><li>Restore the default values and rerun L2 to keep your baseline easy to reproduce.</li><li>L3–L5 use the original test_01 context. They do not inherit your edited L2 experiment.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.</a></div>
<span class="pageno">17 / 59</span></div>

<!--
Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L3 · classroom-010</div>
<h1>L3 starts a separate recorded context</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.</p><pre class="teaching-code">pool = lab.saved_pool(&#x27;test_01&#x27;)
display(pd.DataFrame(pool[&#x27;responses&#x27;])[[&#x27;model_id&#x27;, &#x27;operation_id&#x27;, &#x27;reason&#x27;, &#x27;seconds&#x27;, &#x27;source&#x27;]])</pre><ul><li>Run L3. Read the original context ID, model operations and recorded seconds.</li><li>The displayed reasons were recorded earlier. Opening them makes no new model call.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">18 / 59</span></div>

<!--
The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L3 · classroom-010</div>
<h1>What did the language models choose?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_canonical_trial.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>Different wording can request the same tool and parameters.</li><li>The notebook groups identical physical trials; an explanation does not prove feasibility.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.</a></div>
<span class="pageno">19 / 59</span></div>

<!--
The three recorded replies reduce to two distinct canonical operations. The vote retains one contribution per model identity. In test_01, the Q-relaxation trial receives two votes. This diagram represents the archived input; it is not a new vote after a learner edits L2.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L4 · classroom-013</div>
<h1>Run L4: check the recorded choice again</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.</p><pre class="teaching-code">started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings[&#x27;L4 new verification of archived choices&#x27;] = time.perf_counter() - started
display(selected_trials[&#x27;table&#x27;])
assert pool[&#x27;frozen&#x27;] and pool[&#x27;training_updates&#x27;] == 24</pre><ul><li>Run L4 after L3. Python performs a fresh numerical check on the original selected candidate.</li><li>Compare majority vote with frozen LinUCB on the same original context.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">20 / 59</span></div>

<!--
The selector is frozen and makes no training updates in this lesson. L4 applies the archived selected operation to its original test context and runs a fresh numerical check. This is a replay with new verification, not a new language-model decision or an online learning experiment.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L4 · classroom-013</div>
<h1>Separate the old choice from the new check</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L4_checks.png" alt="Actual executed notebook output; source cell classroom-013. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-013. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Both selectors choose the same Q-relaxation trial and pass the fresh MV check.</li><li>The predicted reward is not a feasibility result; read new_check_passes.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.</a></div>
<span class="pageno">21 / 59</span></div>

<!--
The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>Run L5: identify the model scope</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.</p><pre class="teaching-code">started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings[&#x27;L5 selected model scope checks&#x27;] = time.perf_counter() - started
display(scope_audit[&#x27;table&#x27;])</pre><ul><li>Leave RUN_OPENDSS=False and run L5. Read both the table and optional_mode message.</li><li>This checks the archived test_01 MV-MPC incumbent, with OpenDSS disabled.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">22 / 59</span></div>

<!--
L5 reconstructs the original test_01 context and freshly checks its archived MV-MPC incumbent. This is not the Q-relaxation candidate checked in L4. With RUN_OPENDSS=False, it checks only the reduced model and reports that OpenDSS is disabled. It produces no fresh full-feeder audit in this CPU route. A separate recorded broader-model study is not a result calculated today.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>A PASS belongs to the model that produced it</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L5_scope.png" alt="Actual executed notebook output; source cell classroom-016. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-016. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>The default output checks MV phases and current. It does not cover all LV equipment.</li><li>If the request needs full MV/LV coverage, request a broader-model check or HOLD.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">23 / 59</span></div>

<!--
Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Preview · L12 after all three cases</div>
<h1>Preview the handoff you will build at L12</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/voltage_operator_packet.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>L12 uses selected_trials from L4, not the fresh L2 comparison.</li><li>Finish L6–L11 first. Run L12 at the end of the workshop, in notebook order.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">24 / 59</span></div>

<!--
Preview the purpose of the final handoff without asking participants to jump ahead. L12 will use selected_trials from L4, not the fresh L2 comparison. It contrasts a full MV/LV request with an explicit MV-only teaching request. Continue to L6 after the voltage checkpoint, finish L6–L11, and run L12 once in the closing section. The readback is a simulated teaching event with no equipment dispatch.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Preview · L12 · run at the end</div>
<h1>Preview: the two handoff outcomes</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L12_packet.png" alt="Actual executed notebook output; source cell classroom-033. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-033. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Full MV/LV request: HOLD. Explicit MV teaching scope: simulated readback can succeed.</li><li>A wrong recommendation ID is rejected. equipment_dispatch stays False.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">25 / 59</span></div>

<!--
This screenshot previews the executed default L12 result; students have not run L12 yet. At the final step they will check the returned state and acknowledgment fields. The full-coverage request remains HOLD; the explicit MV teaching scope allows a simulated readback. The simulation does not complete human approval of an archived study and does not dispatch equipment.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L5 · classroom-016</div>
<h1>Voltage checkpoint: state exactly what ran</h1>
<div class="content"><ul><li>L2: fresh MPC and saved-policy proposals. L3: old model replies. L4–L5: fresh checks of test_01.</li><li>Report the input, candidate, model scope and outcome before proposing the next step.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.</a></div>
<span class="pageno">26 / 59</span></div>

<!--
Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates proposals for the current classroom inputs. L3 displays archived replies, L4 rechecks selected trials, and L5 checks the archived incumbent's model scope. Numerical tools provide the physical evidence; the bounded model choice selects a permitted trial. The operator receives a scoped advisory record.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Restoration: open L6</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_fault_map.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>Use the six-node classroom graph. Keep the faulted branch unavailable.</li><li>Your task: compare total restored load with service to critical loads.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">27 / 59</span></div>

<!--
This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Read the objective before choosing a plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_priority.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>The priority plan weights two critical loads more heavily.</li><li>The baseline maximizes total kW with the same graph, capacities and pickup rules.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">28 / 59</span></div>

<!--
Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective expresses a service policy. The difference between the plans comes from that objective. Neither numerical optimizer needs a language model to solve this declared problem.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Run L6: sweep the tie capacity</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.</p><pre class="teaching-code">CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings[&#x27;L6 fresh MILP sweep + independent enumeration&#x27;] = time.perf_counter() - started
display(restoration[&#x27;table&#x27;].drop(columns=&#x27;pickup&#x27;))</pre><ul><li>Run the whole L6 cell. It solves each capacity and checks the priority MILP by enumeration.</li><li>Read served_kw, critical_kw and MILP_matches_exhaustive_check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">29 / 59</span></div>

<!--
Start with capacities of 40, 60, 80, 100 and 120 kW. The solver enforces active-power balance, capacity limits, source connectivity, radiality and fault exclusion. Independent enumeration checks the priority objective on this small graph. Agreement supports this formulation; it does not check omitted AC physics.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Read the two service plots together</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_plot.png" alt="Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Left: total served kW. Right: critical served kW.</li><li>Coincident markers mean equal outcomes at that sampled capacity.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">30 / 59</span></div>

<!--
The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Explain the 40 kW tradeoff</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L6_table.png" alt="Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Priority objective: 130 kW total, including 90 kW critical.</li><li>Maximum-total-kW objective: 140 kW total, including only 30 kW critical.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">31 / 59</span></div>

<!--
Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>How Python checks the plan</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_verify.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>Check available source paths, capacities, balance and the faulted branch.</li><li>Then compare the MILP objective with the independent exhaustive check.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">32 / 59</span></div>

<!--
Numerical verification and evidence binding answer different questions. A correctly bound record may still omit AC voltage, reactive-power or protection constraints. Minimizing energized branches does not calculate the number or order of physical switching operations.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
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
<div class="content"><pre class="source-excerpt">CAPACITIES_KW = (40., 60., 80., 100., 120., 180.)</pre><ul><li>Append 180. to CAPACITIES_KW, keeping 40. as the first entry. Predict, then rerun L6.</li><li>Compare total and critical service at 40 and 180 kW.</li><li>At which of these settings do the two objectives agree?</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">33 / 59</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>Debrief: enough capacity removes this tradeoff</h1>
<div class="content"><p class="callout">250 kW total / 90 kW critical</p><ul><li>At 180 kW, both methods serve 250 kW total and 90 kW critical.</li><li>The priority policy matters under constrained capacity; it does not improve every setting.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">34 / 59</span></div>

<!--
Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Reset the sweep; then run L7</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.</p><pre class="teaching-code">rest_record = restoration[&#x27;records&#x27;][0][&#x27;weighted&#x27;]
rest_request = {&#x27;task&#x27;: &#x27;restoration&#x27;, &#x27;capacity_kw&#x27;: CAPACITIES_KW[0],
                &#x27;critical_nodes&#x27;: [2, 5], &#x27;model&#x27;: &#x27;six_node_active_transport&#x27;, &#x27;revision&#x27;: 1}</pre><ul><li>Restore the original CAPACITIES_KW list and rerun L6 before L7.</li><li>L7 binds the first 40 kW plan, then changes the request to 20 kW.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">35 / 59</span></div>

<!--
Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Read the changed-evidence test</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L7_binding.png" alt="Actual executed notebook output; source cell classroom-021. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-021. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Original contract: True. Changed rating with old evidence: False.</li><li>The stated next step is HOLD the old recommendation and request a fresh solve.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">36 / 59</span></div>

<!--
This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>A failed binding asks for a new check</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_stale.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>“The old evidence is stale” and “the new case is infeasible” are different claims.</li><li>Update the request, solve the changed case, verify it and bind the new evidence.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">37 / 59</span></div>

<!--
The diagram's extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision. Do not say that participants changed topology in the notebook. Ask which numerical step would establish feasibility for the changed request.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>The agent must preserve the service policy</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/restoration_plan.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>The operator specifies the objective and constraints; the MILP returns the pickup plan.</li><li>The agent can request the right solve and explain its tradeoff using the returned evidence.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">38 / 59</span></div>

<!--
A language model must not silently change priority weights or invent pickup values. A different service policy needs an explicit request and a new solve. This classroom supervisor uses ordinary Python. The numerical difference comes from the optimization objective.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L6 · classroom-018</div>
<h1>State what the model leaves out</h1>
<div class="content"><ul><li>This active-power graph does not certify AC voltage, reactive-power feasibility or protection.</li><li>Its energized branches do not define a field switching sequence.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.</a></div>
<span class="pageno">39 / 59</span></div>

<!--
State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L7 · classroom-021</div>
<h1>Restoration checkpoint: name the next action</h1>
<div class="content"><ul><li>For the 40 kW request, explain the 130/90 versus 140/30 service tradeoff.</li><li>For a changed request, retain HOLD until current evidence is available.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.</a></div>
<span class="pageno">40 / 59</span></div>

<!--
Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Cyber: open L8</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_network.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>Use the separate four-bus DC model and its supplied measurement data.</li><li>Your task: distinguish a residual alarm from evidence about the true state.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">41 / 59</span></div>

<!--
The four-bus model has three non-slack voltage angles and eight measurements. It is not an AC estimator, malware detector or sensor-authentication system. Synthetic truth is available only for the offline classroom comparison.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Read residual and state error separately</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_residual.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>J measures consistency between readings and the fitted model.</li><li>State error compares the estimate with known synthetic truth; an operator does not get that truth.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">42 / 59</span></div>

<!--
The chi-square threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. A small J does not establish that the measurements are authentic.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Run L8: compare two attack patterns</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings[&#x27;L8 fresh WLS attack sweep&#x27;] = time.perf_counter() - started
display(cyber[&#x27;table&#x27;])</pre><ul><li>Run the whole L8 cell with its default scale list.</li><li>Compare isolated bias with coordinated Hc in both the table and plots.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">43 / 59</span></div>

<!--
This cell runs fresh weighted-least-squares calculations. The coordinated counterexample assumes knowledge of the linear measurement matrix and access to the modeled unprotected channels. It is a declared defensive teaching model, not evidence of an incident at a utility.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Read your two plots together</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L8_plot.png" alt="Actual executed notebook output; source cell classroom-023. Fresh numerical calculation unless explicitly marked archived." style="max-height:345px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-023. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>Left: residual J and the alarm threshold. Right: offline state error.</li><li>Follow the coordinated curve across both panels before interpreting a quiet alarm.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">44 / 59</span></div>

<!--
The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>At scale 1, what does the alarm miss?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_stealth.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>Isolated bias: J about 277.50, so the residual alarm is True.</li><li>Coordinated Hc: J about 3.92, no alarm, but offline state error is about 0.02678 rad.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">45 / 59</span></div>

<!--
The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
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
<div class="content"><pre class="source-excerpt">ATTACK_SCALES = (0., .10, .25, .5, 1., 1.5)</pre><ul><li>Add .10 to ATTACK_SCALES. Predict, then rerun L8.</li><li>At scale 0.10, read J, the alarm flag and the offline state error.</li><li>Does “no alarm” mean the reading is correct? Use the two panels to explain.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">46 / 59</span></div>

<!--
Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Debrief: a quiet alarm is not proof of truth</h1>
<div class="content"><p class="callout">10.14 &lt; 15.09 → no residual alarm</p><ul><li>At scale 0.10, the isolated-bias residual is about 10.14, below the 15.09 threshold.</li><li>A threshold can miss a small inconsistency. Coordinated corruption creates a different limitation.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">47 / 59</span></div>

<!--
Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L8 · classroom-023</div>
<h1>Reset the sweep before recovery</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.</p><pre class="teaching-code">ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)</pre><ul><li>Restore the original ATTACK_SCALES list and rerun L8.</li><li>Next, L9 uses a fixed trusted-recovery fixture, not the scale you edited.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.</a></div>
<span class="pageno">48 / 59</span></div>

<!--
Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.
Takeaway: 
Nominal duration: 1 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>L9 is a fixed recovery example</h1>
<div class="content"><ul><li>The same supplied recovery case is checked with and without trusted replacement channels.</li><li>Its control value does not track your L8 sweep-scale edit.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">49 / 59</span></div>

<!--
The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Where do the trusted readings come from?</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_trusted.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>The fixture assumes three independent angle readings are trustworthy.</li><li>Neither the residual test nor a language-model explanation authenticates them.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">50 / 59</span></div>

<!--
Three protected angle readings determine three unknown angles, leaving zero residual degrees of freedom. A zero residual in this exactly determined system provides no new detection guarantee. The trust premise must be justified outside this numerical example.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Run L9: compare HOLD with PROPOSE</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.</p><pre class="teaching-code">without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)</pre><ul><li>Run the full L9 cell, including its assertions.</li><li>Read status before comparing the returned injection or offline violation count.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">51 / 59</span></div>

<!--
The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous figure-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Read the two decision states</h1>
<div class="content"><div class="wide-figure"><figure><img src="/images/hands_on_L9_trust.png" alt="Actual executed notebook output; source cell classroom-026. Fresh numerical calculation unless explicitly marked archived." style="max-height:325px;height:auto"><figcaption>Actual executed notebook output; source cell classroom-026. Fresh numerical calculation unless explicitly marked archived.</figcaption></figure></div><ul><li>No trusted replacement channels: HOLD, with no proposed injection.</li><li>Trusted channels assumed: PROPOSE, u about 0.121694 p.u., zero offline toy-model violations.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">52 / 59</span></div>

<!--
Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Check the numerical correction</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_qp.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>The QP minimizes effort while enforcing the declared branch limits and 0.01 p.u. margin.</li><li>Predicted flow12 is 0.17000; offline actual is about 0.17046, below the 0.18000 rating.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">53 / 59</span></div>

<!--
The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. The offline actual flow is an audit against synthetic truth for this fixed case. It does not guarantee unmodeled AC behavior or trustworthy field telemetry.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous diagram-slide has-diagram">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Trace what caused the improvement</h1>
<div class="content"><figure class="native-diagram"><img src="/diagrams/cyber_handoff.svg" alt="Teaching diagram of the model or check used at this notebook step." style="height:305px;max-height:305px"><figcaption>Teaching diagram of the model or check used at this notebook step.</figcaption></figure><ul><li>Independent trusted information supplies a usable estimate; the constrained solver supplies the action.</li><li>The explanation must preserve those conditions and the remaining need for review.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">54 / 59</span></div>

<!--
Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Agent request, tool result, operator decision</h1>
<div class="content"><ul><li>Agent role: request the allowed estimator/control tool and explain its returned conditions.</li><li>Operator role: resolve the trust premise and review the bounded proposal through the authorized process.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">55 / 59</span></div>

<!--
The default classroom calls are deterministic Python functions. The archived model explanations shown in L10 belong to a separate historical study. A real agent implementation would need to bind an allowed request to these tools. This default route makes no new language-model decisions.
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L9 · classroom-026</div>
<h1>Cyber checkpoint: state the condition behind PROPOSE</h1>
<div class="content"><ul><li>Report the measurement-trust assumption, model, proposed u and failed or passed checks.</li><li>If independent trusted information is unavailable, retain HOLD and name the missing evidence.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.</a></div>
<span class="pageno">56 / 59</span></div>

<!--
Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.'
Takeaway: 
Nominal duration: 2 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L10 · classroom-028</div>
<h1>Run L10–L11 with the evidence labels visible</h1>
<div class="content"><ul><li>L10 displays a separate archived five-stage study. It does not replay your edited L2, L6 or L8 inputs.</li><li>Run L11 with RUN_LOCAL_LLAMA=False. The expected message says the new model call is skipped.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.</a></div>
<span class="pageno">57 / 59</span></div>

<!--
L10 reads the archived proposal_complete_workflow study, which has its own models and includes feeder-catalog restoration. It is not the L6 six-node MILP. Use L10 to inspect returned stage evidence and original timings, not as the result of a learner's edited L2, L6 or L8 inputs. In this CPU workshop, L11 explicitly skips the optional model call. This route generates no new LLM reply.
Takeaway: 
Nominal duration: 3 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous normal-slide">

<div class="eyebrow">Classroom Labs · L12 · classroom-033</div>
<h1>Finish L12: practice the operator readback</h1>
<div class="content code-content"><p class="code-caption">Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.</p><pre class="teaching-code">wrong_id = lab.acknowledge(mv_scope, &#x27;wrong-id&#x27;, &#x27;Student operator&#x27;)
readback = lab.acknowledge(mv_scope, mv_scope[&#x27;recommendation_id&#x27;], &#x27;Student operator&#x27;)</pre><ul><li>Run the full L12 cell now, after completing L0–L11 in notebook order.</li><li>Check wrong-ID rejection, correct simulated acknowledgment and equipment_dispatch=False.</li></ul></div>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.</a></div>
<span class="pageno">58 / 59</span></div>

<!--
This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record.
Takeaway: 
Nominal duration: 4 minutes.

Full sources:
Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
-->

---
transition: none
---

<div class="lesson teaching rigorous closing-slide closing">

<h1>Save a reproducible workshop record</h1>
<div class="content"><ul><li>Save your notebook copy with the parameter changes and outputs.</li><li>Explain one case using: input → tool call → result → check → next decision.</li><li>Keep fresh calculations, archived model replies and simulated readbacks clearly labeled.</li></ul></div>
<p class="reading-link"><a href="/Full_Reading_Guide.html">Open the Full Reading Guide</a></p>
<div class="sources">Source: <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.</a></div>
<span class="pageno">59 / 59</span></div>

<!--
Use the final five minutes for pair reports and saving. Each pair names one changed parameter, compares its predicted and observed result, and states one evidence limit. Another person should be able to repeat the experiment from the saved notebook. The reading guide supplies the full source links, stable cell map and debrief answers.
Takeaway: 
Nominal duration: 5 minutes.

Full sources:
Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
-->
