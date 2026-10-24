# Teaching and Source Guide

Hands-on: Three Operator Cases — notebook-aligned tutorial. Evidence reviewed 24 October 2026. The full reading guide is separate from the timed main talk. Corporate issuers are listed when no individual author is recorded. Original figures, page locations and image-source credits are included. Attribution alone is not a blanket reuse license.

## How to teach this hands-on session

**Format:** 59 static slides / 120.0 minutes. Opening: 9 slides / 12.0 minutes; Voltage support: 17 slides / 36 minutes; Service restoration: 14 slides / 28 minutes; Cyber response: 16 slides / 32 minutes; Closing: 3 slides / 12 minutes.

**Prerequisite:** Use the foundations tutorial first. This session follows the current Classroom Labs notebook through voltage support, service restoration and cyber response.

**Evidence modes:** Run the selected numerical cells to calculate results for your inputs. Archived model-response pools and historical evaluation records remain separately labeled. Editing L2 does not change the archived test_01 used by L3–L5, and editing the L8 sweep does not change the fixed L9 recovery fixture. No default cell calls an LLM or operates equipment.

**Preparation:** Open the linked notebook in Google Colab, sign in and use a standard CPU runtime. Run the first setup cell, wait for Ready, then follow the L labels in order. Keep optional OpenDSS and local-model switches at the stated defaults. The default route needs no API key, model download or GPU.

**Facilitation:** Follow each slide’s lab label and stable cell ID. Read the code, predict the result, run it, change the stated parameter and explain what changed. Each exercise has its own timed prompt; answers belong in the teacher notes and following debrief.

## 1. Hands-on: Three Operator Cases

**Timing:** 00:00–00:30 (0.5 minutes)

**Slide content:** Run voltage support, service restoration and cyber response in Classroom Labs
120 minutes · one CPU notebook · three short exercises
IEEE ComSoc theme / Run, change, check and explain

**Teaching notes:** Open Classroom Labs before the workshop. Participants will run fresh numerical calculations and inspect clearly labeled archived model replies. Use the same notebook for all three cases. If devices are limited, work in pairs: one person runs the cells while the other checks the evidence.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[B01] IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.:** [https://www.comsoc.org/about/brand-experience/resources](https://www.comsoc.org/about/brand-experience/resources)

## 2. Open one notebook for all three cases

**Timing:** 00:30–02:00 (1.5 minutes)

**Slide content:** Open Classroom Labs using the source link below or the website’s first Colab button.
Save a copy in Drive so you can keep your parameter changes and outputs.

**Teaching notes:** Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 3. Connect a CPU and run the setup cell

**Timing:** 02:00–04:00 (2 minutes)

**Slide content:** Connect a standard CPU runtime. Run “Set up Google Colab (CPU)” and wait for Ready.
Setup retrieves the supporting data, saved weights and records. It installs the required packages.

**Teaching notes:** For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or model download. If setup stops, reconnect the runtime and rerun setup before starting L0.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 4. Find cells by L label, not by cell number

**Timing:** 04:00–05:00 (1 minutes)

**Slide content:** Use the section headings L0 through L12 to find the next task.
Run a whole code cell with its play button or Shift+Enter. Later cells use earlier variables.

**Teaching notes:** The added Colab setup cells changed the numerical cell positions. Use the L headings and stable cell IDs to find the same source in Colab, Jupyter and these slides. A slide shows only the relevant code fragment. Students should run the complete matching notebook cell.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 5. Run L0: choose the classroom route

**Timing:** 05:00–07:00 (2 minutes)

**Slide content:** Keep both switches False. The class uses fresh linear-model calculations and saved model replies.
If the data check fails, rerun the setup cell before continuing.

**Teaching notes:** Run all of L0 to import the helpers, configure the plots and initialize the timing record. Keep RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. These settings skip the optional full-feeder OpenDSS route and local model service. They do not make the calculations prerecorded: L2 and L4 through L9 run fresh numerical calculations or checks, while L12 checks the evidence binding and simulated readback.

**Exact source excerpt:** Classroom_Labs.ipynb L0 (classroom-002), source lines 11–14.
RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / 'data/lindistflow3_network.json').exists(), 'Start Jupyter in the tutorial folder'

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 6. Know which evidence you are reading

**Timing:** 07:00–08:30 (1.5 minutes)

**Slide content:** FRESH: calculated now. SAVED POLICY: old weights used for a new proposal.
ARCHIVED ACTUAL LLM: a previously recorded reply, with its original input and timing.

**Teaching notes:** The diagram shows responsibilities. Ordinary Python functions perform the engineering calculations; this notebook does not run through LangGraph. A model reply remains an archived event when displayed today. A language model does not replace the power-flow solver, MILP or state estimator.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/common_operator_loop.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 7. Run L1: does old evidence still match?

**Timing:** 08:30–10:00 (1.5 minutes)

**Slide content:** Run the cell, then read binding_pass for all three rows.
Expect True, False, False: changing the load or command invalidates this evidence binding.

**Teaching notes:** Treat this first check as a content-consistency test, not a physical feasibility test. The first row keeps the request and command unchanged. The next two rows change a request field or command field. A failed binding requires fresh evidence, but does not prove the changed action is infeasible. A matching hash does not authenticate a sensor.

**Figure scope:** Actual executed notebook output; source cell classroom-004. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L1_binding.png

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 8. Use the same cycle in every case

**Timing:** 10:00–11:00 (1 minutes)

**Slide content:** Predict → run the default → read the result → change one input → rerun.
Finish by naming the permitted next step and the evidence that supports it.

**Teaching notes:** Pause before showing each output. Ask pairs to write one sentence predicting the change, then compare it with the calculated result. Keep the input values and evidence together. Change only one parameter in the first experiment.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/common_evidence_binding.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 9. Keep a short experiment record

**Timing:** 11:00–12:00 (1 minutes)

**Slide content:** Record the cell label and parameter value you changed.
Record one result, its model scope and your next decision: continue, recheck or HOLD.

**Teaching notes:** Participants can add a text cell below an output or use paper notes; no extra software is needed. Each pair should finish with one changed-input experiment that another person can repeat. Explain the result and one limit on the claim. The three cases use different networks and do not form a single utility deployment study.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 10. Voltage: start with L2

**Timing:** 12:00–14:00 (2 minutes)

**Slide content:** Study one synthetic feeder. The command controls fleet active and reactive participation.
Your task: check feasibility first, then compare the current-step objective.

**Teaching notes:** The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The default backend models MV phases and MV line currents, with idealized LV aggregation. Run L0 and L1 before this cell.

**Figure scope:** Synthetic SMART-DS feeder model used by the voltage example; not an operational utility circuit.

**Figure asset:** images/feeder.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VCASE] Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

## 11. Read the control and limits

**Timing:** 14:00–16:00 (2 minutes)

**Slide content:** a sets active-power participation; b sets reactive-power participation.
The notebook checks the inverter bounds, modeled voltage range and allowed current.

**Teaching notes:** The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltage bounds are 0.95 to 1.05 p.u. RATING_FRACTION=0.80 sets the allowed current to 80% of the nominal rating. The displayed current percentage uses that reduced allowance as its denominator. Passing the inverter bounds alone does not establish network feasibility.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/voltage_capability.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 12. Run L2 with the default inputs

**Timing:** 16:00–18:00 (2 minutes)

**Slide content:** Run the whole L2 cell. It solves MPC, evaluates the saved SAC proposal and checks both.
Find feasible, current_step_J and max_allowed_current_pct in the output.

**Teaching notes:** Start with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. The saved SAC actor produces a new proposal by inference; it is not trained in this cell. Both proposals pass the default classroom checks. MPC has the lower current-step J for this case and objective. This single result does not establish a universal control advantage.

**Exact source excerpt:** Classroom_Labs.ipynb L2 (classroom-007), source lines 1–4.
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

**[VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

## 13. Read your voltage plots

**Timing:** 18:00–20:00 (2 minutes)

**Slide content:** Left: compare the sorted modeled voltage distributions with the allowed band.
Right: compare current use with the 100% allowed-current line.

**Teaching notes:** The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.

**Figure scope:** Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L2_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 14. Read feasibility before cost

**Timing:** 20:00–22:00 (2 minutes)

**Slide content:** Default MPC: PASS, current use 73.62%, current-step J about 0.03110.
Default saved SAC: PASS, current use 51.68%, J about 0.43643.

**Teaching notes:** In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J.

**Figure scope:** Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L2_table.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 15. Exercise 1: tighten the current allowance

**Timing:** 22:00–26:00 (4 minutes)

**Slide content:** In L2, change only RATING_FRACTION from 0.80 to 0.75. Predict, then rerun L2.
For each method, report feasible, allowed-current use and current_step_J.
Does passing this check establish full MV/LV feasibility? Explain your answer.

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 16. Debrief: a tighter allowance can still pass

**Timing:** 26:00–28:00 (2 minutes)

**Slide content:** At 0.75, both candidates still pass: MPC about 78.53%, SAC about 54.85%.
A stricter allowance raises utilization here, but it does not force a failure.

**Teaching notes:** An incorrect prediction is useful evidence, not a failed exercise. Compare the hypothesis with the actual output. Both candidates retain enough headroom in this case. An optimizer may change its command when a constraint changes, so a simple fixed-ratio argument does not apply to every scenario. The model scope has not expanded.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 17. Reset L2 before the recorded-choice lesson

**Timing:** 28:00–30:00 (2 minutes)

**Slide content:** Restore the default values and rerun L2 to keep your baseline easy to reproduce.
L3–L5 use the original test_01 context. They do not inherit your edited L2 experiment.

**Teaching notes:** Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.

**Exact source excerpt:** Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 18. L3 starts a separate recorded context

**Timing:** 30:00–32:00 (2 minutes)

**Slide content:** Run L3. Read the original context ID, model operations and recorded seconds.
The displayed reasons were recorded earlier. Opening them makes no new model call.

**Teaching notes:** The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.

**Exact source excerpt:** Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.
pool = lab.saved_pool('test_01')
display(pd.DataFrame(pool['responses'])[['model_id', 'operation_id', 'reason', 'seconds', 'source']])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 19. What did the language models choose?

**Timing:** 32:00–34:00 (2 minutes)

**Slide content:** Different wording can request the same tool and parameters.
The notebook groups identical physical trials; an explanation does not prove feasibility.

**Teaching notes:** The three recorded replies reduce to two distinct canonical operations. The vote retains one contribution per model identity. In test_01, the Q-relaxation trial receives two votes. This diagram represents the archived input; it is not a new vote after a learner edits L2.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/voltage_canonical_trial.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 20. Run L4: check the recorded choice again

**Timing:** 34:00–36:00 (2 minutes)

**Slide content:** Run L4 after L3. Python performs a fresh numerical check on the original selected candidate.
Compare majority vote with frozen LinUCB on the same original context.

**Teaching notes:** The selector is frozen and makes no training updates in this lesson. L4 applies the archived selected operation to its original test context and runs a fresh numerical check. This is a replay with new verification, not a new language-model decision or an online learning experiment.

**Exact source excerpt:** Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.
started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings['L4 new verification of archived choices'] = time.perf_counter() - started
display(selected_trials['table'])
assert pool['frozen'] and pool['training_updates'] == 24

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H04] Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 21. Separate the old choice from the new check

**Timing:** 36:00–38:00 (2 minutes)

**Slide content:** Both selectors choose the same Q-relaxation trial and pass the fresh MV check.
The predicted reward is not a feasibility result; read new_check_passes.

**Teaching notes:** The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.

**Figure scope:** Actual executed notebook output; source cell classroom-013. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L4_checks.png

**Notebook / source locator:** Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H04] Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 22. Run L5: identify the model scope

**Timing:** 38:00–40:00 (2 minutes)

**Slide content:** Leave RUN_OPENDSS=False and run L5. Read both the table and optional_mode message.
This checks the archived test_01 MV-MPC incumbent, with OpenDSS disabled.

**Teaching notes:** L5 reconstructs the original test_01 context and freshly checks its archived MV-MPC incumbent. This is not the Q-relaxation candidate checked in L4. With RUN_OPENDSS=False, it checks only the reduced model and reports that OpenDSS is disabled. It produces no fresh full-feeder audit in this CPU route. A separate recorded broader-model study is not a result calculated today.

**Exact source excerpt:** Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.
started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings['L5 selected model scope checks'] = time.perf_counter() - started
display(scope_audit['table'])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 23. A PASS belongs to the model that produced it

**Timing:** 40:00–42:00 (2 minutes)

**Slide content:** The default output checks MV phases and current. It does not cover all LV equipment.
If the request needs full MV/LV coverage, request a broader-model check or HOLD.

**Teaching notes:** Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.

**Figure scope:** Actual executed notebook output; source cell classroom-016. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L5_scope.png

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 24. Preview the handoff you will build at L12

**Timing:** 42:00–44:00 (2 minutes)

**Slide content:** L12 uses selected_trials from L4, not the fresh L2 comparison.
Finish L6–L11 first. Run L12 at the end of the workshop, in notebook order.

**Teaching notes:** Preview the purpose of the final handoff without asking participants to jump ahead. L12 will use selected_trials from L4, not the fresh L2 comparison. It contrasts a full MV/LV request with an explicit MV-only teaching request. Continue to L6 after the voltage checkpoint, finish L6–L11, and run L12 once in the closing section. The readback is a simulated teaching event with no equipment dispatch.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/voltage_operator_packet.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 25. Preview: the two handoff outcomes

**Timing:** 44:00–46:00 (2 minutes)

**Slide content:** Full MV/LV request: HOLD. Explicit MV teaching scope: simulated readback can succeed.
A wrong recommendation ID is rejected. equipment_dispatch stays False.

**Teaching notes:** This screenshot previews the executed default L12 result; students have not run L12 yet. At the final step they will check the returned state and acknowledgment fields. The full-coverage request remains HOLD; the explicit MV teaching scope allows a simulated readback. The simulation does not complete human approval of an archived study and does not dispatch equipment.

**Figure scope:** Actual executed notebook output; source cell classroom-033. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L12_packet.png

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 26. Voltage checkpoint: state exactly what ran

**Timing:** 46:00–48:00 (2 minutes)

**Slide content:** L2: fresh MPC and saved-policy proposals. L3: old model replies. L4–L5: fresh checks of test_01.
Report the input, candidate, model scope and outcome before proposing the next step.

**Teaching notes:** Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates proposals for the current classroom inputs. L3 displays archived replies, L4 rechecks selected trials, and L5 checks the archived incumbent's model scope. Numerical tools provide the physical evidence; the bounded model choice selects a permitted trial. The operator receives a scoped advisory record.

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 27. Restoration: open L6

**Timing:** 48:00–49:00 (1 minutes)

**Slide content:** Use the six-node classroom graph. Keep the faulted branch unavailable.
Your task: compare total restored load with service to critical loads.

**Teaching notes:** This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/restoration_fault_map.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 28. Read the objective before choosing a plan

**Timing:** 49:00–51:00 (2 minutes)

**Slide content:** The priority plan weights two critical loads more heavily.
The baseline maximizes total kW with the same graph, capacities and pickup rules.

**Teaching notes:** Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective expresses a service policy. The difference between the plans comes from that objective. Neither numerical optimizer needs a language model to solve this declared problem.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/restoration_priority.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 29. Run L6: sweep the tie capacity

**Timing:** 51:00–53:00 (2 minutes)

**Slide content:** Run the whole L6 cell. It solves each capacity and checks the priority MILP by enumeration.
Read served_kw, critical_kw and MILP_matches_exhaustive_check.

**Teaching notes:** Start with capacities of 40, 60, 80, 100 and 120 kW. The solver enforces active-power balance, capacity limits, source connectivity, radiality and fault exclusion. Independent enumeration checks the priority objective on this small graph. Agreement supports this formulation; it does not check omitted AC physics.

**Exact source excerpt:** Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.
CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings['L6 fresh MILP sweep + independent enumeration'] = time.perf_counter() - started
display(restoration['table'].drop(columns='pickup'))

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 30. Read the two service plots together

**Timing:** 53:00–55:00 (2 minutes)

**Slide content:** Left: total served kW. Right: critical served kW.
Coincident markers mean equal outcomes at that sampled capacity.

**Teaching notes:** The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.

**Figure scope:** Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L6_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 31. Explain the 40 kW tradeoff

**Timing:** 55:00–57:00 (2 minutes)

**Slide content:** Priority objective: 130 kW total, including 90 kW critical.
Maximum-total-kW objective: 140 kW total, including only 30 kW critical.

**Teaching notes:** Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.

**Figure scope:** Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L6_table.png

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 32. How Python checks the plan

**Timing:** 57:00–59:00 (2 minutes)

**Slide content:** Check available source paths, capacities, balance and the faulted branch.
Then compare the MILP objective with the independent exhaustive check.

**Teaching notes:** Numerical verification and evidence binding answer different questions. A correctly bound record may still omit AC voltage, reactive-power or protection constraints. Minimizing energized branches does not calculate the number or order of physical switching operations.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/restoration_verify.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[RSTL01] Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.:** [https://arxiv.org/abs/1912.05185v3](https://arxiv.org/abs/1912.05185v3)

**[RSTL02] Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.:** [https://doi.org/10.1109/TPWRS.2017.2720122](https://doi.org/10.1109/TPWRS.2017.2720122)

## 33. Exercise 2: add more tie capacity

**Timing:** 59:00–63:00 (4 minutes)

**Slide content:** Append 180. to CAPACITIES_KW, keeping 40. as the first entry. Predict, then rerun L6.
Compare total and critical service at 40 and 180 kW.
At which of these settings do the two objectives agree?

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 34. Debrief: enough capacity removes this tradeoff

**Timing:** 63:00–65:00 (2 minutes)

**Slide content:** At 180 kW, both methods serve 250 kW total and 90 kW critical.
The priority policy matters under constrained capacity; it does not improve every setting.

**Teaching notes:** Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 35. Reset the sweep; then run L7

**Timing:** 65:00–67:00 (2 minutes)

**Slide content:** Restore the original CAPACITIES_KW list and rerun L6 before L7.
L7 binds the first 40 kW plan, then changes the request to 20 kW.

**Teaching notes:** Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.

**Exact source excerpt:** Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.
rest_record = restoration['records'][0]['weighted']
rest_request = {'task': 'restoration', 'capacity_kw': CAPACITIES_KW[0],
                'critical_nodes': [2, 5], 'model': 'six_node_active_transport', 'revision': 1}

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 36. Read the changed-evidence test

**Timing:** 67:00–69:00 (2 minutes)

**Slide content:** Original contract: True. Changed rating with old evidence: False.
The stated next step is HOLD the old recommendation and request a fresh solve.

**Teaching notes:** This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.

**Figure scope:** Actual executed notebook output; source cell classroom-021. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L7_binding.png

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 37. A failed binding asks for a new check

**Timing:** 69:00–71:00 (2 minutes)

**Slide content:** “The old evidence is stale” and “the new case is infeasible” are different claims.
Update the request, solve the changed case, verify it and bind the new evidence.

**Teaching notes:** The diagram's extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision. Do not say that participants changed topology in the notebook. Ask which numerical step would establish feasibility for the changed request.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/restoration_stale.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 38. The agent must preserve the service policy

**Timing:** 71:00–73:00 (2 minutes)

**Slide content:** The operator specifies the objective and constraints; the MILP returns the pickup plan.
The agent can request the right solve and explain its tradeoff using the returned evidence.

**Teaching notes:** A language model must not silently change priority weights or invent pickup values. A different service policy needs an explicit request and a new solve. This classroom supervisor uses ordinary Python. The numerical difference comes from the optimization objective.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/restoration_plan.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 39. State what the model leaves out

**Timing:** 73:00–74:00 (1 minutes)

**Slide content:** This active-power graph does not certify AC voltage, reactive-power feasibility or protection.
Its energized branches do not define a field switching sequence.

**Teaching notes:** State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 40. Restoration checkpoint: name the next action

**Timing:** 74:00–76:00 (2 minutes)

**Slide content:** For the 40 kW request, explain the 130/90 versus 140/30 service tradeoff.
For a changed request, retain HOLD until current evidence is available.

**Teaching notes:** Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation.

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 41. Cyber: open L8

**Timing:** 76:00–77:00 (1 minutes)

**Slide content:** Use the separate four-bus DC model and its supplied measurement data.
Your task: distinguish a residual alarm from evidence about the true state.

**Teaching notes:** The four-bus model has three non-slack voltage angles and eight measurements. It is not an AC estimator, malware detector or sensor-authentication system. Synthetic truth is available only for the offline classroom comparison.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/cyber_network.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 42. Read residual and state error separately

**Timing:** 77:00–79:00 (2 minutes)

**Slide content:** J measures consistency between readings and the fitted model.
State error compares the estimate with known synthetic truth; an operator does not get that truth.

**Teaching notes:** The chi-square threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. A small J does not establish that the measurements are authentic.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/cyber_residual.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY01] Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.:** [https://doi.org/10.1109/TPAS.1970.292678](https://doi.org/10.1109/TPAS.1970.292678)

## 43. Run L8: compare two attack patterns

**Timing:** 79:00–81:00 (2 minutes)

**Slide content:** Run the whole L8 cell with its default scale list.
Compare isolated bias with coordinated Hc in both the table and plots.

**Teaching notes:** This cell runs fresh weighted-least-squares calculations. The coordinated counterexample assumes knowledge of the linear measurement matrix and access to the modeled unprotected channels. It is a declared defensive teaching model, not evidence of an incident at a utility.

**Exact source excerpt:** Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings['L8 fresh WLS attack sweep'] = time.perf_counter() - started
display(cyber['table'])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 44. Read your two plots together

**Timing:** 81:00–83:00 (2 minutes)

**Slide content:** Left: residual J and the alarm threshold. Right: offline state error.
Follow the coordinated curve across both panels before interpreting a quiet alarm.

**Teaching notes:** The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.

**Figure scope:** Actual executed notebook output; source cell classroom-023. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L8_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 45. At scale 1, what does the alarm miss?

**Timing:** 83:00–85:00 (2 minutes)

**Slide content:** Isolated bias: J about 277.50, so the residual alarm is True.
Coordinated Hc: J about 3.92, no alarm, but offline state error is about 0.02678 rad.

**Teaching notes:** The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/cyber_stealth.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY02] Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.:** [https://doi.org/10.1145/1952982.1952995](https://doi.org/10.1145/1952982.1952995)

## 46. Exercise 3: add a small isolated bias

**Timing:** 85:00–89:00 (4 minutes)

**Slide content:** Add .10 to ATTACK_SCALES. Predict, then rerun L8.
At scale 0.10, read J, the alarm flag and the offline state error.
Does “no alarm” mean the reading is correct? Use the two panels to explain.

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 47. Debrief: a quiet alarm is not proof of truth

**Timing:** 89:00–91:00 (2 minutes)

**Slide content:** At scale 0.10, the isolated-bias residual is about 10.14, below the 15.09 threshold.
A threshold can miss a small inconsistency. Coordinated corruption creates a different limitation.

**Teaching notes:** Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 48. Reset the sweep before recovery

**Timing:** 91:00–92:00 (1 minutes)

**Slide content:** Restore the original ATTACK_SCALES list and rerun L8.
Next, L9 uses a fixed trusted-recovery fixture, not the scale you edited.

**Teaching notes:** Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.

**Exact source excerpt:** Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 49. L9 is a fixed recovery example

**Timing:** 92:00–94:00 (2 minutes)

**Slide content:** The same supplied recovery case is checked with and without trusted replacement channels.
Its control value does not track your L8 sweep-scale edit.

**Teaching notes:** The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 50. Where do the trusted readings come from?

**Timing:** 94:00–96:00 (2 minutes)

**Slide content:** The fixture assumes three independent angle readings are trustworthy.
Neither the residual test nor a language-model explanation authenticates them.

**Teaching notes:** Three protected angle readings determine three unknown angles, leaving zero residual degrees of freedom. A zero residual in this exactly determined system provides no new detection guarantee. The trust premise must be justified outside this numerical example.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/cyber_trusted.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 51. Run L9: compare HOLD with PROPOSE

**Timing:** 96:00–98:00 (2 minutes)

**Slide content:** Run the full L9 cell, including its assertions.
Read status before comparing the returned injection or offline violation count.

**Teaching notes:** The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.

**Exact source excerpt:** Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.
without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 52. Read the two decision states

**Timing:** 98:00–100:00 (2 minutes)

**Slide content:** No trusted replacement channels: HOLD, with no proposed injection.
Trusted channels assumed: PROPOSE, u about 0.121694 p.u., zero offline toy-model violations.

**Teaching notes:** Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.

**Figure scope:** Actual executed notebook output; source cell classroom-026. Fresh numerical calculation unless explicitly marked archived.

**Figure asset:** images/hands_on_L9_trust.png

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 53. Check the numerical correction

**Timing:** 100:00–102:00 (2 minutes)

**Slide content:** The QP minimizes effort while enforcing the declared branch limits and 0.01 p.u. margin.
Predicted flow12 is 0.17000; offline actual is about 0.17046, below the 0.18000 rating.

**Teaching notes:** The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. The offline actual flow is an audit against synthetic truth for this fixed case. It does not guarantee unmodeled AC behavior or trustworthy field telemetry.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/cyber_qp.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 54. Trace what caused the improvement

**Timing:** 102:00–104:00 (2 minutes)

**Slide content:** Independent trusted information supplies a usable estimate; the constrained solver supplies the action.
The explanation must preserve those conditions and the remaining need for review.

**Teaching notes:** Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.

**Figure scope:** Teaching diagram of the model or check used at this notebook step.

**Editable figure:** diagrams/cyber_handoff.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 55. Agent request, tool result, operator decision

**Timing:** 104:00–106:00 (2 minutes)

**Slide content:** Agent role: request the allowed estimator/control tool and explain its returned conditions.
Operator role: resolve the trust premise and review the bounded proposal through the authorized process.

**Teaching notes:** The default classroom calls are deterministic Python functions. The archived model explanations shown in L10 belong to a separate historical study. A real agent implementation would need to bind an allowed request to these tools. This default route makes no new language-model decisions.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 56. Cyber checkpoint: state the condition behind PROPOSE

**Timing:** 106:00–108:00 (2 minutes)

**Slide content:** Report the measurement-trust assumption, model, proposed u and failed or passed checks.
If independent trusted information is unavailable, retain HOLD and name the missing evidence.

**Teaching notes:** Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.'

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 57. Run L10–L11 with the evidence labels visible

**Timing:** 108:00–111:00 (3 minutes)

**Slide content:** L10 displays a separate archived five-stage study. It does not replay your edited L2, L6 or L8 inputs.
Run L11 with RUN_LOCAL_LLAMA=False. The expected message says the new model call is skipped.

**Teaching notes:** L10 reads the archived proposal_complete_workflow study, which has its own models and includes feeder-catalog restoration. It is not the L6 six-node MILP. Use L10 to inspect returned stage evidence and original timings, not as the result of a learner's edited L2, L6 or L8 inputs. In this CPU workshop, L11 explicitly skips the optional model call. This route generates no new LLM reply.

**Notebook / source locator:** Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 58. Finish L12: practice the operator readback

**Timing:** 111:00–115:00 (4 minutes)

**Slide content:** Run the full L12 cell now, after completing L0–L11 in notebook order.
Check wrong-ID rejection, correct simulated acknowledgment and equipment_dispatch=False.

**Teaching notes:** This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record.

**Exact source excerpt:** Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.
wrong_id = lab.acknowledge(mv_scope, 'wrong-id', 'Student operator')
readback = lab.acknowledge(mv_scope, mv_scope['recommendation_id'], 'Student operator')

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 59. Save a reproducible workshop record

**Timing:** 115:00–120:00 (5 minutes)

**Slide content:** Save your notebook copy with the parameter changes and outputs.
Explain one case using: input → tool call → result → check → next decision.
Keep fresh calculations, archived model replies and simulated readbacks clearly labeled.

**Teaching notes:** Use the final five minutes for pair reports and saving. Each pair names one changed parameter, compares its predicted and observed result, and states one evidence limit. Another person should be able to repeat the experiment from the saved notebook. The reading guide supplies the full source links, stable cell map and debrief answers.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## [H00] Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## [B01] IEEE Communications Society: official resources and network presentation template

**Authors / issuer:** IEEE Communications Society

**Publisher / venue:** IEEE Communications Society

**Date:** Reviewed 17 October 2026

**Theme assets:** comsoc-lockup.png and image7.png; independent educational adaptation

**Full source URL:** [https://www.comsoc.org/about/brand-experience/resources](https://www.comsoc.org/about/brand-experience/resources)

## [H01] Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H02] Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [VCASE] Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope

**Authors / issuer:** Existing GridGuard workshop / SMART-DS synthetic-feeder extraction

**Publisher / venue:** data.openei.org

**Date:** Existing teaching snapshot reviewed 18 October 2026

**Type:** Existing local scientific model figure; external URL is the dataset reference retained by the original workshop

**Full source URL:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

## [VMPC] Model Predictive Control: Theory, Computation, and Design, second edition

**Authors / issuer:** James B. Rawlings; David Q. Mayne; Moritz M. Diehl

**Publisher / venue:** Nob Hill Publishing

**Date:** 2017

**Type:** Primary author-hosted textbook

**Full source URL:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

## [VSAC] Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

**Authors / issuer:** Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine

**Publisher / venue:** Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870

**Date:** 2018

**Type:** Primary research paper

**Full source URL:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

## [H03] Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H04] Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H05] Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H12] Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H06] Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [RSTL01] On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems

**Authors / issuer:** Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang

**Publisher / venue:** Author preprint, arXiv:1912.05185v3

**Date:** 15 March2020(v3); first submitted11 December2019

**Full source URL:** [https://arxiv.org/abs/1912.05185v3](https://arxiv.org/abs/1912.05185v3)

**Full paper PDF:** [https://arxiv.org/pdf/1912.05185v3](https://arxiv.org/pdf/1912.05185v3)

## [RSTL02] Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids

**Authors / issuer:** Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry

**Publisher / venue:** IEEE Transactions on Power Systems33(2),1507–1520

**Date:** March2018

**Full source URL:** [https://doi.org/10.1109/TPWRS.2017.2720122](https://doi.org/10.1109/TPWRS.2017.2720122)

## [H07] Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H08] Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [CY01] Power System Static-State Estimation, Part I: Exact Model

**Authors / issuer:** Fred C. Schweppe, J. Wildes

**Publisher / venue:** IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125

**Date:** January 1970

**Full source URL:** [https://doi.org/10.1109/TPAS.1970.292678](https://doi.org/10.1109/TPAS.1970.292678)

## [CY02] False Data Injection Attacks against State Estimation in Electric Power Grids

**Authors / issuer:** Yao Liu, Peng Ning, Michael K. Reiter

**Publisher / venue:** ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages

**Date:** May 2011

**Full source URL:** [https://doi.org/10.1145/1952982.1952995](https://doi.org/10.1145/1952982.1952995)

**Full paper PDF:** [https://reitermk.github.io/papers/2011/TISSEC2.pdf](https://reitermk.github.io/papers/2011/TISSEC2.pdf)

## [H09] Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H10] Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; notebook cells checked against revision 4fa0e70

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## Visual credit: hands_on_L1_binding.png

**Caption:** Actual executed notebook output; source cell classroom-004. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 7. Run L1: does old evidence still match?

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-004. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L1_binding.png](research/evidence/replots/hands_on_L1_binding.png)

## Visual credit: feeder.png

**Caption:** Synthetic SMART-DS feeder model used by the voltage example; not an operational utility circuit.

**Credit:** Existing GridGuard workshop numerical figure

**Used on:** 10. Voltage: start with L2

**Asset type:** Synthetic feeder visualization

**Transformation:** Unchanged original plot.

**Evidence limit:** Synthetic SMART-DS feeder model used by the voltage example; not an operational utility circuit.

**Original source / page:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

**Original figure / image URL:** [research/evidence/replots/feeder.png](research/evidence/replots/feeder.png)

## Visual credit: hands_on_L2_plot.png

**Caption:** Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 13. Read your voltage plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_plot.png](research/evidence/replots/hands_on_L2_plot.png)

## Visual credit: hands_on_L2_table.png

**Caption:** Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 14. Read feasibility before cost

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-007. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_table.png](research/evidence/replots/hands_on_L2_table.png)

## Visual credit: hands_on_L4_checks.png

**Caption:** Actual executed notebook output; source cell classroom-013. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 21. Separate the old choice from the new check

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-013. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L4_checks.png](research/evidence/replots/hands_on_L4_checks.png)

## Visual credit: hands_on_L5_scope.png

**Caption:** Actual executed notebook output; source cell classroom-016. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 23. A PASS belongs to the model that produced it

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-016. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L5_scope.png](research/evidence/replots/hands_on_L5_scope.png)

## Visual credit: hands_on_L12_packet.png

**Caption:** Actual executed notebook output; source cell classroom-033. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 25. Preview: the two handoff outcomes

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-033. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L12_packet.png](research/evidence/replots/hands_on_L12_packet.png)

## Visual credit: hands_on_L6_plot.png

**Caption:** Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 30. Read the two service plots together

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_plot.png](research/evidence/replots/hands_on_L6_plot.png)

## Visual credit: hands_on_L6_table.png

**Caption:** Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 31. Explain the 40 kW tradeoff

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-018. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_table.png](research/evidence/replots/hands_on_L6_table.png)

## Visual credit: hands_on_L7_binding.png

**Caption:** Actual executed notebook output; source cell classroom-021. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 36. Read the changed-evidence test

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-021. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L7_binding.png](research/evidence/replots/hands_on_L7_binding.png)

## Visual credit: hands_on_L8_plot.png

**Caption:** Actual executed notebook output; source cell classroom-023. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 44. Read your two plots together

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-023. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L8_plot.png](research/evidence/replots/hands_on_L8_plot.png)

## Visual credit: hands_on_L9_trust.png

**Caption:** Actual executed notebook output; source cell classroom-026. Fresh numerical calculation unless explicitly marked archived.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 52. Read the two decision states

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Actual executed notebook output; source cell classroom-026. Fresh numerical calculation unless explicitly marked archived.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L9_trust.png](research/evidence/replots/hands_on_L9_trust.png)
