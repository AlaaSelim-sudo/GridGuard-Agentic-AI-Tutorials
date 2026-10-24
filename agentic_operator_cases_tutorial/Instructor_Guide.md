# Instructor Guide: Hands-on Three Operator Cases

80 static slides / 180.0 minutes. Getting started and agent basics: 10 slides / 12.0 minutes; Voltage support: 22 slides / 48.5 minutes; Service restoration: 17 slides / 36.5 minutes; Cyber response: 18 slides / 38.0 minutes; Llama walkthrough and operator practice: 13 slides / 45.0 minutes. Follow the L labels and stable notebook cell IDs; predict, run, edit and interpret each result. The three exercises have separate teacher notes and debriefs. Numerical calculations and archived model replies remain distinct. No tables, transitions or click reveals.

## 1. Hands-on: Three Operator Cases

00:00–00:30 / 0.5 minutes.

Open Classroom Labs before the workshop. Participants will run fresh numerical calculations and inspect clearly labeled archived model replies. Use the same notebook for all three cases. If devices are limited, work in pairs: one person runs the cells while the other checks the evidence. The deck uses the IEEE ComSoc theme. The classroom cycle is run, change, check and explain. This expanded edition includes a new L10B replay and a proposed control-room advisory pilot. The scheduled teaching time is 180 minutes; allow breaks outside that total. The presenter affiliations are supplied by the presenters. The new Stanford teaching bridge is an adaptation of general reliability ideas, not a claim that the lab implements those Stanford frameworks. Use the six-page Participant Lab Guide for the exact activity steps. The first five slides take five minutes and make the agentic loop explicit before setup. The opening as a whole takes 12 minutes. Case-level replay slides preview saved examples; learners run L10B later in the guided notebook order. Original Stanford lecture figures appear on slides 3, 64, 70 and 71. Adapted grid teaching diagrams cite the relevant lecture page. Full author, title, institution, date, page and reading link appear with the source material.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources

## 2. What is agentic AI?

00:30–01:30 / 1 minutes.

Use the architectural definition in Anthropic, Building effective agents: an agent lets the LLM direct its process and tool use. Agentic AI is a broad term; here it means a system organized around this bounded loop. An AI agent is the component that chooses and follows steps. A tool is a permitted software function that returns a result. Point to the goal, model choice, executable tool, returned evidence and feedback arrow. The application stores case facts and prior results as the context supplied at the next model request. If a required check is missing, the outcome remains HOLD. Stop or return a proposal only under the fixed workflow rules. Do not imply that feedback alone establishes agency: conventional programs can also branch and loop. Our default notebook calculates engineering results now but replays the actual old Llama choices. No live model service is needed. Stanford source: Monica Lam, CS224V Agentic AI, Lecture 1: Introduction, Fall 2026, p.2 describes function calling and agentic workflows. The goal-and-feedback drawing is our grid teaching adaptation, supported by the separate bounded-agent architecture citation. This is not an original Stanford power-system diagram.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 3. Stanford: tool calls become a workflow

01:30–02:30 / 1 minutes.

Show the two original capability panels from Monica Lam’s Stanford CS224V introduction, p.2. The left panel introduces model-selected function calling. The right panel describes multi-step planning, tool use and self-correction. Our plain-language sentence connects the panels to the preceding bounded-loop teaching drawing. The next slide supplies a real recorded grid example. In that example Llama requests a named action and Python validates the JSON choice before calling an existing function; it does not use a native tool_calls protocol. Conventional software can also loop, and a chatbot may itself contain an agent. Here we identify the agentic feature by the model’s permitted next-step choice based on returned evidence. The class replays those old model choices while numerical cells calculate current results. Source lecture figure is shown unchanged within the documented crop.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 4. A real agent changes its next step

02:30–04:00 / 1.5 minutes.

This is an actual saved Llama 3.1:8b voltage episode, not a fabricated interactive exchange. Call 1 selects VERIFY_SAC_FIRST; the numerical check returns 111.966607 percent of allowed current and two current violations. Call 2 selects USE_MPC_PLAN; its numerical check returns 99.604410 percent of allowed current and no recorded violations. The SAC and MPC tools already exist; Llama does not invent or solve the power flow. The arrows show tool-request, result, next-request, result. Call 3 selects REVIEW_EVIDENCE. Human acknowledgment remains PENDING and equipment_dispatch is False. This separate P3 MV/LV OpenDSS archive differs from the fresh L2 exercise and from L3 test_01. Later voltage slides display the exact public returned reasons; learners can replay the source in L10B after completing the three cases. The fixed comparator reaches the same numerical outcome, so the trace illustrates coordination rather than a proven performance improvement.

Full sources:

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 5. Llama chooses; tools calculate; people decide

04:00–05:00 / 1 minutes.

Use the three symbols to assign responsibilities: the speech box is Llama making a permitted choice and returning a public reason; the function is Python and OpenDSS calculating physical results and enforcing workflow limits; the person is the operator reviewing evidence and retaining operating authority. The Llama wrappers use constrained JSON interpreted by the application, rather than native tool_calls. Language explanations are not proof of physical correctness. In our replay the model may say REVIEW but the human acknowledgment is still PENDING. For each exercise work in pairs: one person runs while the other checks, then swap. Save the input, result, check and next decision. Stanford p.53 separates language understanding from checking a formal decision model in a clinical-trial example. The lab adaptation separates Llama coordination from Python numerical checks and operator review. This lab does not run SMT or MaxSAT, and the analogy supplies no formal guarantee about the grid model.

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

## 6. One notebook covers all three cases

05:00–06:00 / 1 minutes.

Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

## 7. Get ready in four small steps

06:00–07:30 / 1.5 minutes.

For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or LLM download. If setup stops, reconnect the runtime and rerun setup before starting L0.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.
Full source: https://research.google.com/colaboratory/faq.html

## 8. Run a cell, then read what it returns

07:30–09:00 / 1.5 minutes.

Point to the three parts: editable input, run control and returned output. The illustrated input lines are the first two lines of the actual L2 cell, not a complete standalone program. The full cell calls the voltage helper and draws two plots. The runtime remembers variables from earlier cells, which is why we run the lesson in order. If NameError reports a missing variable, return to setup/L0 and rerun the required earlier cells. Do not treat a previously displayed output as the result of a number just edited until you rerun its cell. Use the L labels instead of numerical cell indexes. Later cells need earlier variables.

Full sources:

Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.
Full source: https://research.google.com/colaboratory/faq.html

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 9. Run L0: choose the classroom route

09:00–10:00 / 1 minutes.

Run all of L0 to import the helpers, configure the plots and initialize the timing record. Keep RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. These settings skip the optional full-feeder OpenDSS route and local model service. They do not make the calculations prerecorded: L2 and L4 through L9 run fresh numerical calculations or checks, while L12 checks the evidence binding and simulated readback.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L0 (classroom-002), source lines 11–14.):

```python
RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / 'data/lindistflow3_network.json').exists(), 'Start Jupyter in the tutorial folder'
```

## 10. Run L1: does the evidence still match?

10:00–12:00 / 2 minutes.

Evidence binding means matching a checked record to the exact inputs, proposed command and returned result, using content hashes. Treat L1 as a same-content check, not a test that a physical action passes its limits. The first row keeps the request and command unchanged. The next two rows change a request field or command field, so binding_pass is True, False, False. A failed match calls for new evidence; it does not prove the changed action fails its limits. A matching hash also does not authenticate a sensor.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 11. Voltage: open L2

12:00–14:00 / 2 minutes.

The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The command sets active- and reactive-power participation for an inverter fleet. MPC, model predictive control, uses a system model and a short forecast to calculate a plan under limits; here the proposed command is the first step of that plan. SAC, Soft Actor–Critic, is a saved controller learned from rewards. It produces a proposal from old weights without training again. The default calculation covers medium-voltage (MV) phases and MV line currents, with simplified low-voltage (LV) aggregation. Feasible means the proposal passes the limits represented by that model. Compare the penalty score J only after checking those limits; smaller J is preferred for this stated objective. Run L0 and L1 first.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.
Full source: https://data.openei.org/submissions/2981

## 12. MPC plans; SAC proposes

14:00–15:30 / 1.5 minutes.

MPC uses a model and a short forecast to optimize a plan; this lab applies its first action. SAC is a saved policy learned through reinforcement learning; it produces a new control proposal using old weights, without training again. Neither is the coordinating LLM. The outer agent can choose which permitted study to request. L2 calls both tools directly and displays their checks; this cell alone is not a live LLM agent. Later recorded P3 figures illustrate Llama coordinating the existing tools. Define per unit when the control-limit slide introduces the voltage scale: 1.0 p.u. is the stated base value. Explain MILP and WLS only in their respective cases.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.
Full source: https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.
Full source: https://proceedings.mlr.press/v80/haarnoja18b.html

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

## 13. Control settings and limits

15:30–17:30 / 2 minutes.

Active power delivers net energy; reactive power supports the AC voltage and current balance. The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltages must be between 0.95 and 1.05 per unit (p.u.), where values are divided by a stated base. RATING_FRACTION=0.80 sets allowed current to 80% of the nominal rating. The displayed current percentage uses this reduced allowance as its denominator. Passing the inverter bounds alone does not show that network limits pass.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 14. A tool is a Python function in this lab

17:30–19:00 / 1.5 minutes.

Find the actual function call on the next slide. The first two cell lines set the load scale and current allowance; the helper returns numerical proposals, checks and a table for plotting. A tool can be an optimizer, simulator, estimator, lookup or evidence checker. It is not the LLM itself. The student initiates this direct function call with the play button. In the separate recorded workflow Llama selects a named action, the Python application validates that action and its inputs, then invokes a permitted numerical function. Do not claim that the L2 helper uses a live agent gateway. Saving a notebook is separate from keeping a runtime: after a reset, rerun setup and earlier cells.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 15. Run L2 with the default inputs

19:00–21:00 / 2 minutes.

Start with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. The saved SAC actor produces a new proposal by inference; it is not trained in this cell. Both proposals pass the default classroom checks. MPC has the lower current-step J for this case and objective. This single result does not establish a universal control advantage. The output field feasible reports whether the modeled limits pass; current_step_J is this step’s penalty score, and max_allowed_current_pct is maximum current as a percentage of the reduced allowance.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.
Full source: https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.
Full source: https://proceedings.mlr.press/v80/haarnoja18b.html

Exact displayed excerpt (Classroom_Labs.ipynb L2 (classroom-007), source lines 1–4.):

```python
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)
```

## 16. Read the voltage and current plots

21:00–24:00 / 3 minutes.

The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 17. Check limits before comparing scores

24:00–26:00 / 2 minutes.

In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J. Both voltage extrema are within the stated 0.95–1.05 p.u. band for this represented MV model.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 18. A rule and a tool result answer different questions

26:00–27:30 / 1.5 minutes.

Stanford connection: the lecture’s WikiChat discussion, pp.17–25, separates finding material from checking factual claims. Apply the habit to a grid study: retrieving a current limit is different from calculating current for a candidate. The displayed 99.604410% value belongs to the separate archived P3 OpenDSS replay, not to the learner’s fresh L2 result. This example supports only that current check under its recorded model. A sentence, retrieved document or citation does not establish full-network feasibility. Treat the input limits as the task policy. A text source describes the rule; the solver evaluates the particular proposal.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.
Full source: https://aclanthology.org/2023.findings-emnlp.157/
Full paper: https://aclanthology.org/2023.findings-emnlp.157.pdf

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

## 19. Exercise 1: tighten the current allowance

27:30–31:30 / 4 minutes.

Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 20. Change one number and explain the difference

31:30–35:00 / 3.5 minutes.

Use this visual immediately after the first exercise debrief. It shows the measured reference MPC outputs, rounded to two decimal places, for RATING_FRACTION 0.80 and 0.75. The SAC result is also computed in the notebook but is not drawn here. Both proposals pass this particular tighter test. The result is not a general guarantee for other loads or limits. Ask pairs to explain the denominator in the percentage. Restore the default before moving to L3’s independent archived case. This combines the original numerical debrief with the visual explanation. Compare both methods before restoring RATING_FRACTION=0.80.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 21. Reset L2 before reading old model choices

35:00–37:00 / 2 minutes.

Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.):

```python
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
```

## 22. What runs now and what was recorded

37:00–39:00 / 2 minutes.

Point to these evidence modes throughout the session. Default classroom cells calculate fresh results without a live language-model call. L10B displays verified historical Llama choices, original reasons and associated recorded results. Changing your L2 or L6 input does not change those old replies. The final control-room diagrams are a proposed teaching design, not evidence of a deployed utility platform. No new equipment operation occurs in any of these modes. FRESH means calculated during the current execution. SAVED POLICY means old weights used for new inference. ARCHIVED ACTUAL LLM means an old reply with its original inputs and timing. This slide comes just before L3 so the distinction is applied immediately.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## 23. L3 opens a separate recorded case

39:00–41:00 / 2 minutes.

The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.):

```python
pool = lab.saved_pool('test_01')
display(pd.DataFrame(pool['responses'])[['model_id', 'operation_id', 'reason', 'seconds', 'source']])
```

## 24. What did the models choose?

41:00–43:00 / 2 minutes.

The three old replies reduce to two distinct operations after matching their tool names and numerical parameters. The vote keeps one contribution per model. In test_01, two models vote for the Q-relaxation trial, which relaxes a reactive-power restriction in that declared test. This diagram shows the old input and choices; it is not a new vote after a learner edits L2. Grouping matching trials avoids counting different wording as different physical proposals.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 25. Run L4: check the old choice again

43:00–45:00 / 2 minutes.

The selector is frozen and makes no training updates in this lesson. L4 applies the archived selected operation to its original test context and runs a fresh numerical check. This is a replay with new verification, not a new language-model decision or an online learning experiment. LinUCB is a learned selector that scores the available choices from context; its saved settings stay fixed here.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.):

```python
started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings['L4 new verification of archived choices'] = time.perf_counter() - started
display(selected_trials['table'])
assert pool['frozen'] and pool['training_updates'] == 24
```

## 26. Separate the old choice from the new check

45:00–47:00 / 2 minutes.

The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 27. Run L5: check what the model covers

47:00–49:00 / 2 minutes.

L5 rebuilds the original test_01 case and runs a new check on its original MV-MPC incumbent, meaning the baseline plan saved with that case. This is not the reactive-power-relaxation candidate checked in L4. With RUN_OPENDSS=False, L5 checks only the reduced model and reports that OpenDSS is disabled. This CPU route performs no new full-feeder AC check. A wider-model study saved earlier is not a result calculated today. Model scope means the network parts and physical effects that a check represents.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.):

```python
started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings['L5 selected model scope checks'] = time.perf_counter() - started
display(scope_audit['table'])
```

## 28. A PASS covers only the model checked

49:00–51:00 / 2 minutes.

Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 29. Voltage: Llama asks to check the saved controller

51:00–53:30 / 2.5 minutes.

Read the exact reason. The model was offered VERIFY_SAC_FIRST or REVIEW. The application then checks the saved SAC action in OpenDSS. 111.966607% refers to the allowed current, which was 80% of nominal, so this exceeds the configured allowance. The numerical result records two current violations. This P3 full supplied MV/LV study is separate from L2 and L3 test_01. Ask the audience to predict the next allowed step before advancing. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

Full sources:

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 30. Voltage: Llama chooses the existing fallback plan

53:30–56:00 / 2.5 minutes.

The model selects USE_MPC_PLAN from two allowed choices, the other being REVIEW. It does not invent or solve MPC. The recorded context already supplies a plan and its eligibility. The application performs a fresh numerical check at that historical time. The result is just below the allowed current threshold. No operating permission follows from this check alone. Ask which evidence, rather than wording, makes the fallback eligible for review. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

Full sources:

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 31. Voltage: the checks pass and human review remains

56:00–58:30 / 2.5 minutes.

Read the exact REVIEW_EVIDENCE choice and distinguish it from the overall status. The proposed controls are 2387.157 kW and +325.738 kvar. The supplied full MV/LV feeder check returned voltage 1.001783–1.035026 p.u. and zero listed violations. The fixed supervisor used the same SAC-to-MPC sequence with identical numerical output. Recorded workflow intervals were 0.346053 s fixed and 3.110454 s agentic, excluding precomputed MPC/SAC preparation. These are single recorded timings, not performance distributions or a measured reduction in operator workload. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

Full sources:

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 32. Voltage checkpoint: say what ran

58:30–60:30 / 2 minutes.

Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates an MPC plan and a saved-policy proposal for the current classroom inputs. L3 displays old model replies. L4 runs new checks of the selected trials; L5 checks the original archived plan and its model coverage. Numerical tools provide the physical evidence. The old model choices select a permitted trial; they do not replace these checks. The operator receives an advisory record whose stated coverage must match the request. The three P3 previews are an additional separate archive. Contrast their saved Llama decisions with your current direct function calls.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 33. Restoration: open L6

60:30–61:30 / 1 minutes.

This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks. A tie is an alternative connection that can supply load; CAPACITIES_KW sets its transfer limit in kilowatts.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 34. Choose the service goal before the plan

61:30–63:30 / 2 minutes.

Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective is the service goal encoded as a score. The priority score gives more weight to these critical loads, while the comparison score maximizes total kW. The difference in selected service comes from that goal. Both numerical methods use the same graph, capacities and whole-load pickup rules. Neither needs a language model to solve this declared problem.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 35. Run L6: change the tie capacity

63:30–65:30 / 2 minutes.

MILP means mixed-integer linear programming. Here it is a whole-load chooser: on/off choices decide which load blocks are served, while linear constraints enforce the stated network rules. Start with tie capacities of 40, 60, 80, 100 and 120 kW. The solver enforces active-power balance, capacity limits, connection to a source, no loops in the energized graph, and exclusion of the faulted branch. An independent exhaustive search checks the priority score on this small graph. Agreement supports this formulation; it does not check the AC physics left out of the model.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.):

```python
CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings['L6 fresh MILP sweep + independent enumeration'] = time.perf_counter() - started
display(restoration['table'].drop(columns='pickup'))
```

## 36. Read both service plots

65:30–68:30 / 3 minutes.

The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 37. The tradeoff at a 40 kW tie limit

68:30–70:30 / 2 minutes.

Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 38. How Python checks the plan

70:30–72:30 / 2 minutes.

Numerical checks and same-content evidence matching answer different questions. A record can match the inputs exactly while still omitting AC voltage, reactive-power or protection limits. Comparing the MILP score with every permitted plan is an independent check of this small stated problem. Minimizing energized branches does not calculate the number or order of physical switching steps.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.
Full source: https://arxiv.org/abs/1912.05185v3
Full paper: https://arxiv.org/pdf/1912.05185v3

Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.
Full source: https://doi.org/10.1109/TPWRS.2017.2720122

## 39. Exercise 2: add more tie capacity

72:30–76:30 / 4 minutes.

Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 40. Debrief: the tradeoff disappears here

76:30–78:30 / 2 minutes.

Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 41. Reset the capacity list, then run L7

78:30–80:30 / 2 minutes.

Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.):

```python
rest_record = restoration['records'][0]['weighted']
rest_request = {'task': 'restoration', 'capacity_kw': CAPACITIES_KW[0],
                'critical_nodes': [2, 5], 'model': 'six_node_active_transport', 'revision': 1}
```

## 42. Read the evidence-match test

80:30–82:30 / 2 minutes.

This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 43. Changed inputs need a new check

82:30–84:30 / 2 minutes.

Evidence binding asks whether a record matches the exact request, proposed plan and returned result. The diagram’s extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision; students do not change topology in that cell. Old evidence is unusable for a changed request even if the old plan might still pass its limits. Ask which new numerical check would establish that for the changed request.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 44. Proposed agent role: keep the service goal

84:30–86:30 / 2 minutes.

This is a proposed role for an agent, not a new model decision in the default notebook. The current supervisor is ordinary Python. A future language-model agent could request the allowed solve and explain the returned tradeoff. It must preserve the operator’s service goal and limits, rather than quietly changing weights or making up load values. A different service goal requires an explicit new request and solve. The numerical difference here comes from the optimization objective.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 45. What this model does not check

86:30–87:30 / 1 minutes.

State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 46. Restoration: Llama chooses a useful new trial

87:30–90:00 / 2.5 minutes.

Switch L10B to restoration. This is the separate L10 feeder-catalog restoration study, not the L6 six-node MILP. The recorded protocol requires a first refinement but Llama chooses between the offered fractions. SHED_075 disconnects 75% of the ordered noncritical load objects, not 75% of load kW. The exact reason calls improvement a possibility. Python evaluates the trial and finds improved service while the tie loading remains 91.867215% of its allowance. A useful hypothesis becomes evidence only after that check. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

Full sources:

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 47. Restoration: the next trial crosses the current limit

90:00–92:30 / 2.5 minutes.

Keep the actual returned reason visible. It refers to a target in the objective, but its claim should not be accepted as a proved fact. In this record the next trial is numerically rejected for a thermal failure. Restoring more load does not make a failed current check acceptable. Ask participants to explain why the previous passed candidate must remain in the case record. The model’s trial budget is bounded. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

Full sources:

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 48. Restoration: catch Llama’s wrong ranking

92:30–95:00 / 2.5 minutes.

Let pairs answer before discussing the result. Smaller cost is better, so E03 must rank before E02. Llama returns [E02,E03] while its explanation claims lowest score first. The recorded language_order_agrees_with_cost field is False. A deterministic guard retains E03 and rechecks it as E05, with no recorded failures. Human acknowledgment and dispatch remain False. The paired fixed workflow reaches the same final action and cost. This example motivates verification rather than an unsupported superiority claim. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

Full sources:

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 49. Restoration checkpoint: name the next step

95:00–97:00 / 2 minutes.

Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation. Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 50. Cyber: open L8

97:00–98:00 / 1 minutes.

The separate four-bus linear DC model has three unknown voltage angles, measured relative to a reference bus, and eight readings. This DC approximation is not a full AC estimator, malware detector or sensor-authentication system. Synthetic truth is known for the offline classroom comparison only. A residual checks how well the estimate fits the supplied readings; state error checks how far the estimate is from the known teaching truth.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 51. Best fit and true state are different

98:00–100:00 / 2 minutes.

WLS means weighted least squares: find the state that best fits the readings, giving more influence to readings with smaller stated uncertainty. That weighting does not authenticate a reading. Here J is the residual mismatch statistic, not the voltage case’s penalty score. Its chi-square alarm threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. An operator does not have the synthetic truth used to calculate the plotted state error. A small J does not establish that the readings are authentic.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678

## 52. Run L8: compare two data attacks

100:00–102:00 / 2 minutes.

L8 runs new WLS calculations. An isolated bias changes one reading. The coordinated Hc shift changes readings in a pattern consistent with a different modeled state. This counterexample assumes knowledge of the linear measurement matrix H and access to the modeled unprotected channels. It is a declared defensive teaching model, not evidence of an incident at a utility.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.):

```python
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings['L8 fresh WLS attack sweep'] = time.perf_counter() - started
display(cyber['table'])
```

## 53. Read both cyber plots

102:00–105:00 / 3 minutes.

The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 54. At scale 1, the alarm misses a state error

105:00–107:00 / 2 minutes.

The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace. The state error is measured in radians; it is available here because this is an offline test with known synthetic truth.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.
Full source: https://doi.org/10.1145/1952982.1952995
Full paper: https://reitermk.github.io/papers/2011/TISSEC2.pdf

## 55. Exercise 3: add a small isolated bias

107:00–111:00 / 4 minutes.

Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 56. Debrief: no alarm does not prove truth

111:00–113:00 / 2 minutes.

Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 57. Reset L8 before the recovery example

113:00–114:00 / 1 minutes.

Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.):

```python
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
```

## 58. L9 uses a fixed recovery case

114:00–116:00 / 2 minutes.

The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 59. Trusted readings are an assumption

116:00–118:00 / 2 minutes.

The example assumes three protected angle readings determine the three unknown angles, leaving zero residual degrees of freedom. Independent trusted information must come from a justified source outside this numerical calculation. A zero residual in this exactly determined system adds no detection guarantee. Neither a good model fit nor a language-model explanation establishes authenticity.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 60. Run L9: compare HOLD and PROPOSE

118:00–120:00 / 2 minutes.

The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.):

```python
without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)
```

## 61. Read the two decision states

120:00–122:00 / 2 minutes.

Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 62. Check the numerical correction

122:00–124:00 / 2 minutes.

QP means quadratic programming: this numerical solver minimizes a quadratic effort score while enforcing the declared branch limits and a 0.01 p.u. margin. The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. Predicted flow12 is 0.17000 p.u.; the offline actual flow is about 0.17046 p.u., below the 0.18000 p.u. rating. The actual-flow comparison uses synthetic truth for this fixed case. It does not guarantee AC behavior omitted by the model or trustworthy field telemetry.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 63. What makes the recovery possible?

124:00–126:00 / 2 minutes.

Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 64. Stanford: language and decision checks

126:00–128:00 / 2 minutes.

This original diagram selection comes from the function row on p.53 of Monica Lam’s introduction. It shows a clinical-trial example, not a power-system experiment. The language model translates written facts into an SMT representation; a separate solver derives a decision from those constraints. SMT means satisfiability modulo theories, a way to express and solve logical constraints. MaxSAT supports the lecture’s search for conditions that change a decision. The lecture also states that the formalization may not be completely faithful, so correctness remains relative to the represented constraints. Our application is an analogy: Llama requests the permitted estimate or control tool and Python checks numerical limits. An operator must still confirm the trust assumption and review the proposed action. Our notebook does not run an SMT/MaxSAT solver or prove formal electrical safety. Keep the previously calculated HOLD/PROPOSE outcomes tied to their stated numerical model and trusted-data assumption.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 65. Cyber: Llama selects the tool already allowed

128:00–130:30 / 2.5 minutes.

Switch L10B to cyber. This standard four-bus DC record is separate from L10’s proposal-complete cyber record, and matches the Agent Trace notebook T6 archive. The route is narrow: the prompt already authorizes the tool and supplies the trusted-sensor assumption. The three angle readings give full rank but zero residual redundancy, so a good fit is not an independent trust test. u is the flexible injection correction in per unit. Offline synthetic-truth flow is available to the experimenter, not guaranteed available to a real operator. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

Full sources:

Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 66. Cyber: a passing calculation still needs review

130:30–133:00 / 2.5 minutes.

Read the actual reply, including the REVIEW choice. Numerical verification is PASS, but the overall result remains REVIEW and human acknowledgment is PENDING. The fixed comparator obtains the same numerical state estimate and correction without Llama. This replay demonstrates permitted tool routing and a report decision. It does not demonstrate better estimation, authenticated measurements, AC network security or operating authority. Run L11 with the default False setting, then proceed to L12. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

Full sources:

Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 67. Cyber checkpoint: explain why PROPOSE is allowed

133:00–135:00 / 2 minutes.

Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.' Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 68. Run L10 before the Llama walkthrough

135:00–138:00 / 3 minutes.

L10 reads the archived proposal_complete_workflow study. It includes feeder-catalog restoration and is separate from the L6 six-node MILP and your edited classroom inputs. L10B, inserted immediately after L10, then gives readable verified replay episodes for all three cases. Run L11 after those replays; the default False setting skips a new local model request.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 69. Run L10B: watch Llama choose a tool

138:00–141:30 / 3.5 minutes.

Run L10 first. In the new L10B cell the helper validates the original JSON reply against the parsed journal and trace, then displays the recorded episode. Change only SCENARIO to inspect the other two episodes. Earlier case slides previewed selected fields from these replays. Now inspect the full episodes in the same notebook. This cell makes no model request and performs no new electrical solve. At the end, run L11 at its default False setting before L12. Llama reasons are historical public returned text. Their correctness must be judged against the input and tool results. SCENARIO can be voltage, restoration or cyber. The full cell is shown.

Full sources:

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.
Full source: https://docs.ollama.com/capabilities/structured-outputs

Exact displayed excerpt (Classroom_Labs.ipynb L10B (classroom-llama-walkthrough), source lines 1–5.):

```python
SCENARIO = "voltage"  # Change to "restoration" or "cyber", then rerun this cell.
from IPython.display import HTML, display
from src.llama_walkthrough import load_episodes, render_episode_html
replay_episodes = load_episodes(ROOT)
display(HTML(render_episode_html(replay_episodes[SCENARIO])))
```

## 70. Stanford example: check before you write

141:30–144:30 / 3 minutes.

The displayed figure is an original excerpt from Monica Lam’s Stanford CS224V introduction, p.19. Follow its retrieval, claim checking and writing steps. The WikiChat paper is fully cited in the reading guide. Our application to grid studies is a teaching analogy: read the stated limits, run the appropriate numerical check and summarize the actual returned result. Ask which lab step would detect a current violation. The classroom notebook does not run WikiChat; its dialogue factuality measurements are not electrical performance results.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.
Full source: https://aclanthology.org/2023.findings-emnlp.157/
Full paper: https://aclanthology.org/2023.findings-emnlp.157.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 71. Stanford example: tools need clear rules

144:30–147:00 / 2.5 minutes.

Stanford connection: Lam p.40 and the published Genie Worksheets paper emphasize developer-defined workflows and knowledge sources. The published framework uses an algorithmic runtime to enforce a supplied policy, with LLMs used for language understanding and response generation. Our lab uses custom Python functions, not Genie Worksheets. The application analogy is to specify the task and prevent a language reply from silently changing its limits or filling missing required inputs. A passed calculation does not prove that the task description was correct. The figure shown here is an actual excerpt from the supplied Stanford lecture. Ask the audience to point to the claim-checking or policy step, then identify the corresponding Python check in our lab. We borrow the design habit; the notebook does not run WikiChat or Genie. Their non-grid benchmarks are not electrical performance results.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.
Full source: https://aclanthology.org/2025.acl-long.1323/
Full paper: https://aclanthology.org/2025.acl-long.1323.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 72. Ask four questions about a study result

147:00–149:00 / 2 minutes.

Lam’s pp.52–53 distinguish verifiable rationale, explicit assumptions, policy consistency and actionable next conditions. Translate these into four plain questions: which tool supports this claim, which inputs and model were used, were the same limits and service priorities kept, and what must the operator review next? Our power-flow, optimization and evidence-binding checks are numerical/software checks. They do not inherit the lecture’s SMT correctness claims. Ask pairs to apply the questions to one L10B explanation and to the full-scope HOLD at L12. We show only the actual public returned reasons, not hidden chain-of-thought.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 73. Finish L12: practice the readback

149:00–154:00 / 5 minutes.

This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record. Readback means repeating the recommendation ID and conditions so the acknowledgment can be matched to the same proposal. In this exercise it is simulated. Check the wrong-ID rejection, the correct simulated acknowledgment and equipment_dispatch=False.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.):

```python
wrong_id = lab.acknowledge(mv_scope, 'wrong-id', 'Student operator')
readback = lab.acknowledge(mv_scope, mv_scope['recommendation_id'], 'Student operator')
```

## 74. Read the two readback outcomes

154:00–157:00 / 3 minutes.

After running the complete L12 cell, compare these reference outputs with your own. The full MV/LV request remains HOLD because the checked model covers only MV phases. An explicit MV teaching request can pass the simulated readback after the recommendation ID matches. The wrong-ID attempt is rejected. Acknowledgment records a classroom review step and does not operate equipment.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 75. Start a control-room pilot with a clear study request

157:00–161:00 / 4 minutes.

Proposed advisory pilot, not a deployment claim. F12 is an illustrative teaching feeder name. Read the study request aloud: compare the allowed voltage-support options, keep the stated current and voltage limits, show the worst margins and missing checks, and return a recommendation for review. The data owner defines acceptable age, source and quality rules. L1 and L7 illustrate matching inputs to results, but hashes alone do not authenticate those sources.

Full sources:

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 76. Give the assistant a small, controlled tool list

161:00–165:00 / 4 minutes.

Proposed advisory pilot. Walk through the lanes: operator, assistant, application-controlled tool gateway and engineering tools. Llama requests one permitted function; the application checks the request and executes the tool. A snapshot identifier binds the result to the input. The workshop Python functions are teaching counterparts, not SCADA adapters. NIST OT guidance supports controlled information flows, least privilege and logging. The exact pilot architecture is our teaching recommendation, not a NIST-certified design.

Full sources:

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.
Full source: https://docs.ollama.com/capabilities/structured-outputs

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 77. Check three things before returning a proposal

165:00–169:00 / 4 minutes.

Proposed advisory pilot. Current data and a matching evidence packet are the first gate. The second gate checks stated engineering limits with approved tools. The third asks whether the calculations cover the request, including excluded low-voltage parts or required protection and dynamic studies. This is not a universal complete security checklist. It illustrates why L12 can produce a passing local calculation and still HOLD a broader request. Make missing evidence visible instead of allowing fluent text to fill the gap.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## 78. Give the operator a short evidence packet

169:00–173:00 / 4 minutes.

Proposed advisory pilot. Use three review questions: Does this match the current equipment, inputs and model? Did the required checks pass, with missing checks clear? What exactly am I approving, who owns the next step, and where is the record? Record the reviewer, reason, case snapshot and tool versions. Accepting a study result does not itself issue an equipment command. Authorized operating procedures and roles determine any later physical action. L12 practices only a simulated ID-bound readback.

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

## 79. Adopt it in stages and measure the benefit

173:00–177:00 / 4 minutes.

Proposed advisory pilot. Historical replay lets engineers define expected outcomes and failure cases. Shadow use compares recommendations alongside the existing process without relying on them for equipment control. A limited pilot needs a named owner, training, an agreed scope and a way to stop use. Measure end-to-end elapsed time including review, correct completed studies, missed or stale inputs, overlooked limits and reviewer changes. Compare the same engineering tools with and without Llama. Our paired records show identical final numerical results, so there is no basis yet to promise higher accuracy, less operator workload or faster decisions. NIST AI RMF supports human roles, evaluation under realistic conditions and deactivation; these particular pilot metrics are our recommendation.

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

## 80. Save a workshop record others can repeat

177:00–180:00 / 3 minutes.

Use the final three minutes for pair reports and saving. Each pair names one changed parameter, compares its predicted and observed result, and states one evidence limit. Another person should be able to repeat the experiment from the saved notebook. The reading guide supplies the full source links, stable cell map and debrief answers.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

