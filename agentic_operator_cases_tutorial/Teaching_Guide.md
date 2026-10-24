# Teaching and Source Guide

Hands-on: Three Operator Cases — notebook-aligned tutorial. Evidence reviewed 24 October 2026. The full reading guide is separate from the timed main talk. Corporate issuers are listed when no individual author is recorded. Original figures, page locations and image-source credits are included. Attribution alone is not a blanket reuse license.

## How to teach this hands-on session

**Format:** 80 static slides / 180.0 minutes. Getting started and agent basics: 10 slides / 12.0 minutes; Voltage support: 22 slides / 48.5 minutes; Service restoration: 17 slides / 36.5 minutes; Cyber response: 18 slides / 38.0 minutes; Llama walkthrough and operator practice: 13 slides / 45.0 minutes.

**Prerequisite:** Use the foundations tutorial first. This session follows the current Classroom Labs notebook through voltage support, service restoration and cyber response.

**Evidence modes:** Run the selected numerical cells to calculate results for your inputs. Archived model-response pools and historical evaluation records remain separately labeled. Editing L2 does not change the archived test_01 used by L3–L5, and editing the L8 sweep does not change the fixed L9 recovery fixture. No default cell calls an LLM or operates equipment.

**Preparation:** Give participants Participant_Lab_Guide.pdf. Open the one required notebook in Google Colab, sign in and use a standard CPU runtime. Run setup, wait for Ready, then follow the L labels in order. Keep both model switches at the stated defaults. The default route needs no API key, LLM download or GPU.

**Opening and replay route:** The first five slides teach the goal, model choice, tool result, feedback and human review in five minutes. The opening totals twelve minutes. Case slides preview saved Llama episodes beside the relevant engineering calculation. Run the canonical notebook in order: only execute L10B after L10, then L11 and L12.

**Stanford teaching bridge:** Original grid teaching diagrams adapt task decomposition, evidence checking and explicit workflow specification from Monica Lam’s CS224V Lecture 1, with full lecture and paper references below. This notebook does not run WikiChat, Genie Worksheets or a theorem prover.

**Facilitation:** Follow each slide’s lab label and stable cell ID. Read the code, predict the result, run it, change the stated parameter and explain what changed. Each exercise has its own timed prompt; answers belong in the teacher notes and following debrief.

## 1. Hands-on: Three Operator Cases

**Timing:** 00:00–00:30 (0.5 minutes)

**Slide content:** Run one notebook to understand three operator studies.
180 minutes / three short exercises / no coding experience required

**Teaching notes:** Open Classroom Labs before the workshop. Participants will run fresh numerical calculations and inspect clearly labeled archived model replies. Use the same notebook for all three cases. If devices are limited, work in pairs: one person runs the cells while the other checks the evidence. The deck uses the IEEE ComSoc theme. The classroom cycle is run, change, check and explain. This expanded edition includes a new L10B replay and a proposed control-room advisory pilot. The scheduled teaching time is 180 minutes; allow breaks outside that total. The presenter affiliations are supplied by the presenters. The new Stanford teaching bridge is an adaptation of general reliability ideas, not a claim that the lab implements those Stanford frameworks. Use the six-page Participant Lab Guide for the exact activity steps. The first five slides take five minutes and make the agentic loop explicit before setup. The opening as a whole takes 12 minutes. Case-level replay slides preview saved examples; learners run L10B later in the guided notebook order.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[B01] IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.:** [https://www.comsoc.org/about/brand-experience/resources](https://www.comsoc.org/about/brand-experience/resources)

## 2. What is agentic AI?

**Timing:** 00:30–01:30 (1 minutes)

**Slide content:** An LLM agent works toward a goal by choosing tools, reading their results and choosing what to do next.

**Teaching notes:** Use the architectural definition in Anthropic, Building effective agents: an agent lets the LLM direct its process and tool use. Agentic AI is a broad term; here it means a system organized around this bounded loop. An AI agent is the component that chooses and follows steps. A tool is a permitted software function that returns a result. Point to the goal, model choice, executable tool, returned evidence and feedback arrow. The application stores case facts and prior results as the context supplied at the next model request. If a required check is missing, the outcome remains HOLD. Stop or return a proposal only under the fixed workflow rules. Do not imply that feedback alone establishes agency: conventional programs can also branch and loop. Our default notebook calculates engineering results now but replays the actual old Llama choices. No live model service is needed.

**Figure scope:** A bounded agentic loop. In this workshop, Llama choices are recorded; Python calculations can run now.

**Editable figure:** diagrams/agent_goal_loop.tex

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 3. From a text answer to a tool loop

**Timing:** 01:30–02:30 (1 minutes)

**Slide content:** The key change: the model chooses a permitted next step using the result returned by a tool.

**Teaching notes:** Trace the first row once, then follow the lower feedback arrow. In the text-only interaction the immediate product is a reply. In the illustrated agentic interaction the model can request a calculation, read its returned facts and select another allowed action. A chatbot may itself contain such an agent; the interface name does not determine the architecture. A fixed program can branch, retry and optimize too. The narrow feature in the recorded examples is that Llama selects among an explicitly permitted set of next actions. The wrappers validate its JSON and then call functions; they do not execute arbitrary generated code. This is bounded model choice, not unrestricted control or a claim of superior numerical results.

**Figure scope:** Two interaction patterns. Tools and feedback can also be used in ordinary software.

**Editable figure:** diagrams/agent_text_tool.tex

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 4. A real agent changes its next step

**Timing:** 02:30–04:00 (1.5 minutes)

**Slide content:** The failed tool result leads to a fallback check. Passing the checks still leaves human review.

**Teaching notes:** This is an actual saved Llama 3.1:8b voltage episode, not a fabricated interactive exchange. Call 1 selects VERIFY_SAC_FIRST; the numerical check returns 111.966607 percent of allowed current and two current violations. Call 2 selects USE_MPC_PLAN; its numerical check returns 99.604410 percent of allowed current and no recorded violations. The SAC and MPC tools already exist; Llama does not invent or solve the power flow. The arrows show tool-request, result, next-request, result. Call 3 selects REVIEW_EVIDENCE. Human acknowledgment remains PENDING and equipment_dispatch is False. This separate P3 MV/LV OpenDSS archive differs from the fresh L2 exercise and from L3 test_01. Later voltage slides display the exact public returned reasons; learners can replay the source in L10B after completing the three cases. The fixed comparator reaches the same numerical outcome, so the trace illustrates coordination rather than a proven performance improvement.

**Figure scope:** Recorded P3 example, separate from L2. 111.966607% and 99.604410% are rounded here.

**Editable figure:** diagrams/agent_recorded_trace.tex

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 5. Llama chooses; tools calculate; people decide

**Timing:** 04:00–05:00 (1 minutes)

**Slide content:** The agent coordinates a study. Numerical tools supply the checks. The operator reviews the proposal.

**Teaching notes:** Use the three symbols to assign responsibilities: the speech box is Llama making a permitted choice and returning a public reason; the function is Python and OpenDSS calculating physical results and enforcing workflow limits; the person is the operator reviewing evidence and retaining operating authority. The Llama wrappers use constrained JSON interpreted by the application, rather than native tool_calls. Language explanations are not proof of physical correctness. In our replay the model may say REVIEW but the human acknowledgment is still PENDING. For each exercise work in pairs: one person runs while the other checks, then swap. Save the input, result, check and next decision.

**Figure scope:** Default class route: new numerical results plus saved Llama replies. No equipment commands.

**Editable figure:** diagrams/agent_roles_simple.tex

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[OLL1] Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

## 6. One notebook covers all three cases

**Timing:** 05:00–06:00 (1 minutes)

**Slide content:** Save a copy in Drive. Keep this same notebook open for all three cases.

**Teaching notes:** Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.

**Figure scope:** Only Classroom Labs is required. The graph and trace notebooks are companion material.

**Editable figure:** diagrams/lab_one_notebook.tex

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 7. Get ready in four small steps

**Timing:** 06:00–07:30 (1.5 minutes)

**Slide content:** Open the notebook, save your copy, connect a CPU and run setup.
Wait for Ready. Then run L0 and L1 before starting the three cases.

**Teaching notes:** For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or LLM download. If setup stops, reconnect the runtime and rerun setup before starting L0.

**Figure scope:** Setup prepares the runtime. Then follow each named lesson cell with the slides.

**Editable figure:** diagrams/lab_ready.tex

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[COL01] Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

## 8. Run a cell, then read what it returns

**Timing:** 07:30–09:00 (1.5 minutes)

**Slide content:** Find the L heading. Use the play button to run the whole matching code cell.
Wait, then read the table or plot underneath it. Editing an input alone does not update output.

**Teaching notes:** Point to the three parts: editable input, run control and returned output. The illustrated input lines are the first two lines of the actual L2 cell, not a complete standalone program. The full cell calls the voltage helper and draws two plots. The runtime remembers variables from earlier cells, which is why we run the lesson in order. If NameError reports a missing variable, return to setup/L0 and rerun the required earlier cells. Do not treat a previously displayed output as the result of a number just edited until you rerun its cell. Use the L labels instead of numerical cell indexes. Later cells need earlier variables.

**Figure scope:** Teaching illustration, not a Colab screenshot. Input lines match L2; run the full L2 cell.

**Editable figure:** diagrams/lab_cell_loop.tex

**Notebook / source locator:** Google Colab FAQ; Classroom Labs L2, cell classroom-007.

**[COL01] Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 9. Run L0: choose the classroom route

**Timing:** 09:00–10:00 (1 minutes)

**Slide content:** Keep both switches False: new numerical checks, saved controller and archived model replies.
If the data check fails, rerun setup before continuing.

**Teaching notes:** Run all of L0 to import the helpers, configure the plots and initialize the timing record. Keep RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. These settings skip the optional full-feeder OpenDSS route and local model service. They do not make the calculations prerecorded: L2 and L4 through L9 run fresh numerical calculations or checks, while L12 checks the evidence binding and simulated readback.

**Exact source excerpt:** Classroom_Labs.ipynb L0 (classroom-002), source lines 11–14.
RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / 'data/lindistflow3_network.json').exists(), 'Start Jupyter in the tutorial folder'

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 10. Run L1: does the evidence still match?

**Timing:** 10:00–12:00 (2 minutes)

**Slide content:** Read binding_pass: does the record match the same inputs and command?
Expect True, False, False. Changing the load or command breaks that match.

**Teaching notes:** Evidence binding means matching a checked record to the exact inputs, proposed command and returned result, using content hashes. Treat L1 as a same-content check, not a test that a physical action passes its limits. The first row keeps the request and command unchanged. The next two rows change a request field or command field, so binding_pass is True, False, False. A failed match calls for new evidence; it does not prove the changed action fails its limits. A matching hash also does not authenticate a sensor.

**Figure scope:** Reference L1 output: only the unchanged request and command match the evidence.

**Figure asset:** images/hands_on_L1_binding.png

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 11. Voltage: open L2

**Timing:** 12:00–14:00 (2 minutes)

**Slide content:** MPC makes a forecast-based plan. SAC is a saved learned controller.
Check limits first. Then compare penalty score J; smaller is preferred after the checks pass.

**Teaching notes:** The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The command sets active- and reactive-power participation for an inverter fleet. MPC, model predictive control, uses a system model and a short forecast to calculate a plan under limits; here the proposed command is the first step of that plan. SAC, Soft Actor–Critic, is a saved controller learned from rewards. It produces a proposal from old weights without training again. The default calculation covers medium-voltage (MV) phases and MV line currents, with simplified low-voltage (LV) aggregation. Feasible means the proposal passes the limits represented by that model. Compare the penalty score J only after checking those limits; smaller J is preferred for this stated objective. Run L0 and L1 first.

**Figure scope:** Synthetic SMART-DS teaching feeder; not an operating utility circuit.

**Figure asset:** images/feeder.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VCASE] Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

## 12. MPC plans; SAC proposes

**Timing:** 14:00–15:30 (1.5 minutes)

**Slide content:** Both tools propose control settings. The same numerical check tests their voltage and current limits.

**Teaching notes:** MPC uses a model and a short forecast to optimize a plan; this lab applies its first action. SAC is a saved policy learned through reinforcement learning; it produces a new control proposal using old weights, without training again. Neither is the coordinating LLM. The outer agent can choose which permitted study to request. L2 calls both tools directly and displays their checks; this cell alone is not a live LLM agent. Later recorded P3 figures illustrate Llama coordinating the existing tools. Define per unit when the control-limit slide introduces the voltage scale: 1.0 p.u. is the stated base value. Explain MILP and WLS only in their respective cases.

**Figure scope:** MPC: model predictive control. SAC: Soft Actor–Critic. These are control tools inside the larger workflow.

**Editable figure:** diagrams/agent_mpc_sac.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

**[VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

## 13. Control settings and limits

**Timing:** 15:30–17:30 (2 minutes)

**Slide content:** a sets active-power participation; b sets reactive-power participation.
Check the inverter limits, modeled voltages and allowed line current.

**Teaching notes:** Active power delivers net energy; reactive power supports the AC voltage and current balance. The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltages must be between 0.95 and 1.05 per unit (p.u.), where values are divided by a stated base. RATING_FRACTION=0.80 sets allowed current to 80% of the nominal rating. The displayed current percentage uses this reduced allowance as its denominator. Passing the inverter bounds alone does not show that network limits pass.

**Figure scope:** Active and reactive settings share the inverter’s power limit.

**Editable figure:** diagrams/voltage_capability.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 14. A tool is a Python function in this lab

**Timing:** 17:30–19:00 (1.5 minutes)

**Slide content:** A tool takes defined inputs and returns evidence. The notebook lets you see both.

**Teaching notes:** Find the actual function call on the next slide. The first two cell lines set the load scale and current allowance; the helper returns numerical proposals, checks and a table for plotting. A tool can be an optimizer, simulator, estimator, lookup or evidence checker. It is not the LLM itself. The student initiates this direct function call with the play button. In the separate recorded workflow Llama selects a named action, the Python application validates that action and its inputs, then invokes a permitted numerical function. Do not claim that the L2 helper uses a live agent gateway. Saving a notebook is separate from keeping a runtime: after a reset, rerun setup and earlier cells.

**Figure scope:** L2 calls lab.voltage_lab(LOAD_SCALE, RATING_FRACTION) directly. Recorded agent coordination is separate.

**Editable figure:** diagrams/agent_python_tool.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 15. Run L2 with the default inputs

**Timing:** 19:00–21:00 (2 minutes)

**Slide content:** Run all of L2 to calculate the MPC plan and check the saved SAC controller’s proposal.
Read feasible, current_step_J and max_allowed_current_pct.

**Teaching notes:** Start with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. The saved SAC actor produces a new proposal by inference; it is not trained in this cell. Both proposals pass the default classroom checks. MPC has the lower current-step J for this case and objective. This single result does not establish a universal control advantage. The output field feasible reports whether the modeled limits pass; current_step_J is this step’s penalty score, and max_allowed_current_pct is maximum current as a percentage of the reduced allowance.

**Exact source excerpt:** Classroom_Labs.ipynb L2 (classroom-007), source lines 1–4.
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

**[VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

## 16. Read the voltage and current plots

**Timing:** 21:00–24:00 (3 minutes)

**Slide content:** Left: compare the sorted modeled voltages with the allowed band.
Right: compare line current with the 100% allowed-current limit.

**Teaching notes:** The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.

**Figure scope:** Reference L2 plots; rerun L2 to calculate plots for your inputs.

**Figure asset:** images/hands_on_L2_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 17. Check limits before comparing scores

**Timing:** 24:00–26:00 (2 minutes)

**Slide content:** Default MPC passes: current use 73.62%, penalty score J about 0.03110.
Default saved SAC passes: current use 51.68%, J about 0.43643.

**Teaching notes:** In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J. Both voltage extrema are within the stated 0.95–1.05 p.u. band for this represented MV model.

**Figure scope:** Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

**Figure asset:** images/hands_on_L2_table.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 18. A rule and a tool result answer different questions

**Timing:** 26:00–27:30 (1.5 minutes)

**Slide content:** A document can tell us the limit. A numerical tool tells us how the proposal compares with it.
Keep the source, the measured or calculated value, and the remaining checks together.

**Teaching notes:** Stanford connection: the lecture’s WikiChat discussion, pp.17–25, separates finding material from checking factual claims. Apply the habit to a grid study: retrieving a current limit is different from calculating current for a candidate. The displayed 99.604410% value belongs to the separate archived P3 OpenDSS replay, not to the learner’s fresh L2 result. This example supports only that current check under its recorded model. A sentence, retrieved document or citation does not establish full-network feasibility. Treat the input limits as the task policy. A text source describes the rule; the solver evaluates the particular proposal.

**Figure scope:** Teaching analogy. The number shown comes from the recorded P3 replay, which is separate from L2.

**Editable figure:** diagrams/lab_claim_evidence.tex

**Notebook / source locator:** Monica Lam, CS224V Lecture 1, pp.17–25; recorded P3 current check.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

## 19. Exercise 1: tighten the current allowance

**Timing:** 27:30–31:30 (4 minutes)

**Slide content:** In L2, change only RATING_FRACTION from 0.80 to 0.75. Predict, then rerun.
For each method, report feasible, allowed-current use and current_step_J.
Does a PASS cover the full medium- and low-voltage network? Explain.

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 20. Change one number and explain the difference

**Timing:** 31:30–35:00 (3.5 minutes)

**Slide content:** A tighter allowance makes the same current a larger percentage of that allowance.
At 0.75, MPC uses 78.53% and SAC 54.85%. Both pass this particular test.

**Teaching notes:** Use this visual immediately after the first exercise debrief. It shows the measured reference MPC outputs, rounded to two decimal places, for RATING_FRACTION 0.80 and 0.75. The SAC result is also computed in the notebook but is not drawn here. Both proposals pass this particular tighter test. The result is not a general guarantee for other loads or limits. Ask pairs to explain the denominator in the percentage. Restore the default before moving to L3’s independent archived case. This combines the original numerical debrief with the visual explanation. Compare both methods before restoring RATING_FRACTION=0.80.

**Figure scope:** Reference L2 exercise: MPC uses 73.62% of the default allowance and 78.53% after the change.

**Editable figure:** diagrams/lab_try_observe.tex

**Notebook / source locator:** Classroom Labs L2, cell classroom-007; verified default and exercise outputs.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 21. Reset L2 before reading old model choices

**Timing:** 35:00–37:00 (2 minutes)

**Slide content:** Restore the default values and rerun L2.
L3–L5 use the original test_01 case, separate from your changed L2 experiment.

**Teaching notes:** Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.

**Exact source excerpt:** Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 22. What runs now and what was recorded

**Timing:** 37:00–39:00 (2 minutes)

**Slide content:** The current cell calculates new results. The saved Llama reply keeps its original inputs.
Changing your lab input does not rewrite the recorded agent study.

**Teaching notes:** Point to these evidence modes throughout the session. Default classroom cells calculate fresh results without a live language-model call. L10B displays verified historical Llama choices, original reasons and associated recorded results. Changing your L2 or L6 input does not change those old replies. The final control-room diagrams are a proposed teaching design, not evidence of a deployed utility platform. No new equipment operation occurs in any of these modes. FRESH means calculated during the current execution. SAVED POLICY means old weights used for new inference. ARCHIVED ACTUAL LLM means an old reply with its original inputs and timing. This slide comes just before L3 so the distinction is applied immediately.

**Figure scope:** Three explicitly labeled teaching modes used throughout this workshop.

**Editable figure:** diagrams/bridge_modes.tex

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

## 23. L3 opens a separate recorded case

**Timing:** 39:00–41:00 (2 minutes)

**Slide content:** Run L3. Read the original case ID, requested operations and recorded seconds.
These reasons are old model replies. Displaying them makes no new model call.

**Teaching notes:** The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.

**Exact source excerpt:** Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.
pool = lab.saved_pool('test_01')
display(pd.DataFrame(pool['responses'])[['model_id', 'operation_id', 'reason', 'seconds', 'source']])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 24. What did the models choose?

**Timing:** 41:00–43:00 (2 minutes)

**Slide content:** Different wording can request the same tool and numbers.
The notebook groups matching trials. An explanation alone does not show that limits pass.

**Teaching notes:** The three old replies reduce to two distinct operations after matching their tool names and numerical parameters. The vote keeps one contribution per model. In test_01, two models vote for the Q-relaxation trial, which relaxes a reactive-power restriction in that declared test. This diagram shows the old input and choices; it is not a new vote after a learner edits L2. Grouping matching trials avoids counting different wording as different physical proposals.

**Figure scope:** Three old replies request two distinct operations; two votes select reactive-power relaxation.

**Editable figure:** diagrams/voltage_canonical_trial.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 25. Run L4: check the old choice again

**Timing:** 43:00–45:00 (2 minutes)

**Slide content:** After L3, run L4. Python checks the selected proposal again for its original case.
Compare majority vote with the saved LinUCB selector on that same case.

**Teaching notes:** The selector is frozen and makes no training updates in this lesson. L4 applies the archived selected operation to its original test context and runs a fresh numerical check. This is a replay with new verification, not a new language-model decision or an online learning experiment. LinUCB is a learned selector that scores the available choices from context; its saved settings stay fixed here.

**Exact source excerpt:** Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.
started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings['L4 new verification of archived choices'] = time.perf_counter() - started
display(selected_trials['table'])
assert pool['frozen'] and pool['training_updates'] == 24

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H04] Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 26. Separate the old choice from the new check

**Timing:** 45:00–47:00 (2 minutes)

**Slide content:** Both selectors choose the same reactive-power relaxation trial and pass the new MV check.
Predicted reward is a learned score. Read new_check_passes for the engineering check.

**Teaching notes:** The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.

**Figure scope:** Reference L4 output: old selector choices, new numerical checks of the original case.

**Figure asset:** images/hands_on_L4_checks.png

**Notebook / source locator:** Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H04] Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 27. Run L5: check what the model covers

**Timing:** 47:00–49:00 (2 minutes)

**Slide content:** Keep RUN_OPENDSS=False. Run L5 and read the table and optional_mode message.
L5 checks the original test_01 MV-MPC plan. OpenDSS is disabled.

**Teaching notes:** L5 rebuilds the original test_01 case and runs a new check on its original MV-MPC incumbent, meaning the baseline plan saved with that case. This is not the reactive-power-relaxation candidate checked in L4. With RUN_OPENDSS=False, L5 checks only the reduced model and reports that OpenDSS is disabled. This CPU route performs no new full-feeder AC check. A wider-model study saved earlier is not a result calculated today. Model scope means the network parts and physical effects that a check represents.

**Exact source excerpt:** Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.
started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings['L5 selected model scope checks'] = time.perf_counter() - started
display(scope_audit['table'])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 28. A PASS covers only the model checked

**Timing:** 49:00–51:00 (2 minutes)

**Slide content:** This check covers medium-voltage (MV) phases and currents, not all low-voltage (LV) equipment.
For a full MV/LV request, get the wider check or HOLD.

**Teaching notes:** Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.

**Figure scope:** Reference L5 output: a medium-voltage check with OpenDSS disabled.

**Figure asset:** images/hands_on_L5_scope.png

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 29. Voltage: Llama asks to check the saved controller

**Timing:** 51:00–53:30 (2.5 minutes)

**Slide content:** Llama identifies the missing check. The current failure forces a new trial.

**Teaching notes:** Read the exact reason. The model was offered VERIFY_SAC_FIRST or REVIEW. The application then checks the saved SAC action in OpenDSS. 111.966607% refers to the allowed current, which was 80% of nominal, so this exceeds the configured allowance. The numerical result records two current violations. This P3 full supplied MV/LV study is separate from L2 and L3 test_01. Ask the audience to predict the next allowed step before advancing. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Figure asset:** images/llama_voltage_1.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 1; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 30. Voltage: Llama chooses the existing fallback plan

**Timing:** 53:30–56:00 (2.5 minutes)

**Slide content:** Llama chooses an existing MPC plan. Python checks whether the result passes.

**Teaching notes:** The model selects USE_MPC_PLAN from two allowed choices, the other being REVIEW. It does not invent or solve MPC. The recorded context already supplies a plan and its eligibility. The application performs a fresh numerical check at that historical time. The result is just below the allowed current threshold. No operating permission follows from this check alone. Ask which evidence, rather than wording, makes the fallback eligible for review. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Figure asset:** images/llama_voltage_2.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 2; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 31. Voltage: the checks pass and human review remains

**Timing:** 56:00–58:30 (2.5 minutes)

**Slide content:** Human review remains pending. The fixed script returned the same numerical result.

**Teaching notes:** Read the exact REVIEW_EVIDENCE choice and distinguish it from the overall status. The proposed controls are 2387.157 kW and +325.738 kvar. The supplied full MV/LV feeder check returned voltage 1.001783–1.035026 p.u. and zero listed violations. The fixed supervisor used the same SAC-to-MPC sequence with identical numerical output. Recorded workflow intervals were 0.346053 s fixed and 3.110454 s agentic, excluding precomputed MPC/SAC preparation. These are single recorded timings, not performance distributions or a measured reduction in operator workload. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Figure asset:** images/llama_voltage_3.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 3; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 32. Voltage checkpoint: say what ran

**Timing:** 58:30–60:30 (2 minutes)

**Slide content:** L2 makes new proposals; L3 shows old replies; L4–L5 run new checks on test_01.
Report the inputs, proposal, model coverage and result before naming the next step.

**Teaching notes:** Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates an MPC plan and a saved-policy proposal for the current classroom inputs. L3 displays old model replies. L4 runs new checks of the selected trials; L5 checks the original archived plan and its model coverage. Numerical tools provide the physical evidence. The old model choices select a permitted trial; they do not replace these checks. The operator receives an advisory record whose stated coverage must match the request. The three P3 previews are an additional separate archive. Contrast their saved Llama decisions with your current direct function calls.

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 33. Restoration: open L6

**Timing:** 60:30–61:30 (1 minutes)

**Slide content:** Use the six-node teaching graph. Keep the faulted branch unavailable.
Compare total restored load with restored critical load.

**Teaching notes:** This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks. A tie is an alternative connection that can supply load; CAPACITIES_KW sets its transfer limit in kilowatts.

**Figure scope:** Six-node active-power teaching graph with whole-load pickup and one unavailable branch.

**Editable figure:** diagrams/restoration_fault_map.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 34. Choose the service goal before the plan

**Timing:** 61:30–63:30 (2 minutes)

**Slide content:** The priority goal gives more weight to two critical loads.
The comparison goal serves the most total kW, using the same network and pickup rules.

**Teaching notes:** Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective is the service goal encoded as a score. The priority score gives more weight to these critical loads, while the comparison score maximizes total kW. The difference in selected service comes from that goal. Both numerical methods use the same graph, capacities and whole-load pickup rules. Neither needs a language model to solve this declared problem.

**Figure scope:** Different service goals can select different loads on the same network.

**Editable figure:** diagrams/restoration_priority.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 35. Run L6: change the tie capacity

**Timing:** 63:30–65:30 (2 minutes)

**Slide content:** Run all of L6. MILP chooses whole loads; an exhaustive search checks its priority score.
Read served_kw, critical_kw and MILP_matches_exhaustive_check.

**Teaching notes:** MILP means mixed-integer linear programming. Here it is a whole-load chooser: on/off choices decide which load blocks are served, while linear constraints enforce the stated network rules. Start with tie capacities of 40, 60, 80, 100 and 120 kW. The solver enforces active-power balance, capacity limits, connection to a source, no loops in the energized graph, and exclusion of the faulted branch. An independent exhaustive search checks the priority score on this small graph. Agreement supports this formulation; it does not check the AC physics left out of the model.

**Exact source excerpt:** Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.
CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings['L6 fresh MILP sweep + independent enumeration'] = time.perf_counter() - started
display(restoration['table'].drop(columns='pickup'))

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 36. Read both service plots

**Timing:** 65:30–68:30 (3 minutes)

**Slide content:** Left: total load served in kW. Right: critical load served in kW.
Overlapping markers mean the two plans give the same result at that tested capacity.

**Teaching notes:** The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.

**Figure scope:** Reference L6 plots; rerun L6 to compare your chosen tie capacities.

**Figure asset:** images/hands_on_L6_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 37. The tradeoff at a 40 kW tie limit

**Timing:** 68:30–70:30 (2 minutes)

**Slide content:** Priority goal: 130 kW total, including 90 kW of critical load.
Most-total-kW goal: 140 kW total, including 30 kW of critical load.

**Teaching notes:** Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.

**Figure scope:** Reference L6 results at a 40 kW tie limit: compare total and critical load served.

**Figure asset:** images/hands_on_L6_table.png

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 38. How Python checks the plan

**Timing:** 70:30–72:30 (2 minutes)

**Slide content:** Check paths to a source, capacity limits, power balance and the faulted branch.
Then compare the MILP service score with the independent exhaustive search.

**Teaching notes:** Numerical checks and same-content evidence matching answer different questions. A record can match the inputs exactly while still omitting AC voltage, reactive-power or protection limits. Comparing the MILP score with every permitted plan is an independent check of this small stated problem. Minimizing energized branches does not calculate the number or order of physical switching steps.

**Figure scope:** Python checks the stated graph constraints, then compares the priority score independently.

**Editable figure:** diagrams/restoration_verify.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[RSTL01] Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.:** [https://arxiv.org/abs/1912.05185v3](https://arxiv.org/abs/1912.05185v3)

**[RSTL02] Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.:** [https://doi.org/10.1109/TPWRS.2017.2720122](https://doi.org/10.1109/TPWRS.2017.2720122)

## 39. Exercise 2: add more tie capacity

**Timing:** 72:30–76:30 (4 minutes)

**Slide content:** Add 180. to CAPACITIES_KW, keeping 40. first. Predict, then rerun L6.
Compare total and critical load served at 40 and 180 kW.
At which of these two capacities do the service goals give the same result?

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 40. Debrief: the tradeoff disappears here

**Timing:** 76:30–78:30 (2 minutes)

**Slide content:** At 180 kW, both methods serve 250 kW total and 90 kW of critical load.
Priority helps in the constrained case. It does not improve every case.

**Teaching notes:** Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 41. Reset the capacity list, then run L7

**Timing:** 78:30–80:30 (2 minutes)

**Slide content:** Restore the original CAPACITIES_KW list and rerun L6.
L7 checks the first 40 kW record, then changes the request to 20 kW.

**Teaching notes:** Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.

**Exact source excerpt:** Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.
rest_record = restoration['records'][0]['weighted']
rest_request = {'task': 'restoration', 'capacity_kw': CAPACITIES_KW[0],
                'critical_nodes': [2, 5], 'model': 'six_node_active_transport', 'revision': 1}

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 42. Read the evidence-match test

**Timing:** 80:30–82:30 (2 minutes)

**Slide content:** Original request: True. Changed rating with the old evidence: False.
HOLD the old recommendation and request a new solve.

**Teaching notes:** This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.

**Figure scope:** Reference L7 output: changed request, unchanged evidence, so a new check is needed.

**Figure asset:** images/hands_on_L7_binding.png

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 43. Changed inputs need a new check

**Timing:** 82:30–84:30 (2 minutes)

**Slide content:** “The evidence is old” does not mean “the changed plan fails its limits.”
Update the request, solve and check it, then match the new evidence to that request.

**Teaching notes:** Evidence binding asks whether a record matches the exact request, proposed plan and returned result. The diagram’s extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision; students do not change topology in that cell. Old evidence is unusable for a changed request even if the old plan might still pass its limits. Ask which new numerical check would establish that for the changed request.

**Figure scope:** L7 changes capacity and revision; extra topology labels are teaching examples.

**Editable figure:** diagrams/restoration_stale.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 44. Proposed agent role: keep the service goal

**Timing:** 84:30–86:30 (2 minutes)

**Slide content:** This cell runs Python: the operator sets the goal and limits; MILP chooses the whole loads.
A proposed agent would request that solve and explain the returned tradeoff.

**Teaching notes:** This is a proposed role for an agent, not a new model decision in the default notebook. The current supervisor is ordinary Python. A future language-model agent could request the allowed solve and explain the returned tradeoff. It must preserve the operator’s service goal and limits, rather than quietly changing weights or making up load values. A different service goal requires an explicit new request and solve. The numerical difference here comes from the optimization objective.

**Figure scope:** Proposed agent responsibilities; the current notebook cell runs Python.

**Editable figure:** diagrams/restoration_plan.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 45. What this model does not check

**Timing:** 86:30–87:30 (1 minutes)

**Slide content:** This active-power graph does not check AC voltage, reactive power or protection.
The energized branches do not give the order of field switching steps.

**Teaching notes:** State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 46. Restoration: Llama chooses a useful new trial

**Timing:** 87:30–90:00 (2.5 minutes)

**Slide content:** The new trial serves more load, keeps critical service and passes the current check.

**Teaching notes:** Switch L10B to restoration. This is the separate L10 feeder-catalog restoration study, not the L6 six-node MILP. The recorded protocol requires a first refinement but Llama chooses between the offered fractions. SHED_075 disconnects 75% of the ordered noncritical load objects, not 75% of load kW. The exact reason calls improvement a possibility. Python evaluates the trial and finds improved service while the tie loading remains 91.867215% of its allowance. A useful hypothesis becomes evidence only after that check. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Figure asset:** images/llama_restoration_14.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 14; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 47. Restoration: the next trial crosses the current limit

**Timing:** 90:00–92:30 (2.5 minutes)

**Slide content:** The next trial fails the current limit. Keep the previous passed candidate.

**Teaching notes:** Keep the actual returned reason visible. It refers to a target in the objective, but its claim should not be accepted as a proved fact. In this record the next trial is numerically rejected for a thermal failure. Restoring more load does not make a failed current check acceptable. Ask participants to explain why the previous passed candidate must remain in the case record. The model’s trial budget is bounded. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Figure asset:** images/llama_restoration_15.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 15; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 48. Restoration: catch Llama’s wrong ranking

**Timing:** 92:30–95:00 (2.5 minutes)

**Slide content:** The returned order is wrong. Python chooses the smaller cost and rechecks the plan.

**Teaching notes:** Let pairs answer before discussing the result. Smaller cost is better, so E03 must rank before E02. Llama returns [E02,E03] while its explanation claims lowest score first. The recorded language_order_agrees_with_cost field is False. A deterministic guard retains E03 and rechecks it as E05, with no recorded failures. Human acknowledgment and dispatch remain False. The paired fixed workflow reaches the same final action and cost. This example motivates verification rather than an unsupported superiority claim. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Figure asset:** images/llama_restoration_16.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 16; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 49. Restoration checkpoint: name the next step

**Timing:** 95:00–97:00 (2 minutes)

**Slide content:** At 40 kW, explain 130 total / 90 critical versus 140 total / 30 critical, all in kW.
For a changed request, keep HOLD until evidence for the current request is available.

**Teaching notes:** Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation. Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 50. Cyber: open L8

**Timing:** 97:00–98:00 (1 minutes)

**Slide content:** Use the separate four-bus DC model and its supplied readings.
Compare a residual alarm, which checks fit, with error against the known teaching truth.

**Teaching notes:** The separate four-bus linear DC model has three unknown voltage angles, measured relative to a reference bus, and eight readings. This DC approximation is not a full AC estimator, malware detector or sensor-authentication system. Synthetic truth is known for the offline classroom comparison only. A residual checks how well the estimate fits the supplied readings; state error checks how far the estimate is from the known teaching truth.

**Figure scope:** Four-bus linear DC teaching model; known synthetic truth is used only for offline comparison.

**Editable figure:** diagrams/cyber_network.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 51. Best fit and true state are different

**Timing:** 98:00–100:00 (2 minutes)

**Slide content:** WLS finds the best fit to readings, giving more weight to lower stated uncertainty.
Residual J measures fit mismatch. State error uses teaching truth unavailable to an operator.

**Teaching notes:** WLS means weighted least squares: find the state that best fits the readings, giving more influence to readings with smaller stated uncertainty. That weighting does not authenticate a reading. Here J is the residual mismatch statistic, not the voltage case’s penalty score. Its chi-square alarm threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. An operator does not have the synthetic truth used to calculate the plotted state error. A small J does not establish that the readings are authentic.

**Figure scope:** A good fit to readings does not show that those readings are authentic.

**Editable figure:** diagrams/cyber_residual.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY01] Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.:** [https://doi.org/10.1109/TPAS.1970.292678](https://doi.org/10.1109/TPAS.1970.292678)

## 52. Run L8: compare two data attacks

**Timing:** 100:00–102:00 (2 minutes)

**Slide content:** Run all of L8 with its default scale list.
Compare one biased reading with the coordinated Hc shift in the table and plots.

**Teaching notes:** L8 runs new WLS calculations. An isolated bias changes one reading. The coordinated Hc shift changes readings in a pattern consistent with a different modeled state. This counterexample assumes knowledge of the linear measurement matrix H and access to the modeled unprotected channels. It is a declared defensive teaching model, not evidence of an incident at a utility.

**Exact source excerpt:** Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings['L8 fresh WLS attack sweep'] = time.perf_counter() - started
display(cyber['table'])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 53. Read both cyber plots

**Timing:** 102:00–105:00 (3 minutes)

**Slide content:** Left: residual J and its alarm threshold. Right: error against the known teaching truth.
Follow the coordinated curve across both plots before calling a quiet alarm reassuring.

**Teaching notes:** The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.

**Figure scope:** Reference L8 plots; rerun L8 to calculate results for your chosen attack scales.

**Figure asset:** images/hands_on_L8_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 54. At scale 1, the alarm misses a state error

**Timing:** 105:00–107:00 (2 minutes)

**Slide content:** One biased reading: J about 277.50, so the residual alarm is True.
Coordinated Hc: J about 3.92, no alarm, but state error is about 0.02678 rad.

**Teaching notes:** The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace. The state error is measured in radians; it is available here because this is an offline test with known synthetic truth.

**Figure scope:** Simple consistency illustration; the numerical values come from the eight-reading L8 model.

**Editable figure:** diagrams/cyber_stealth.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY02] Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.:** [https://doi.org/10.1145/1952982.1952995](https://doi.org/10.1145/1952982.1952995)

## 55. Exercise 3: add a small isolated bias

**Timing:** 107:00–111:00 (4 minutes)

**Slide content:** Add .10 to ATTACK_SCALES. Predict, then rerun L8.
At scale 0.10, read J, the alarm flag and the error against known teaching truth.
Does “no alarm” mean the reading is correct? Use both plots to explain.

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 56. Debrief: no alarm does not prove truth

**Timing:** 111:00–113:00 (2 minutes)

**Slide content:** At scale 0.10, the isolated-bias J is about 10.14, below the 15.09 threshold.
A small bias can miss the threshold. A coordinated shift can preserve the fit.

**Teaching notes:** Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 57. Reset L8 before the recovery example

**Timing:** 113:00–114:00 (1 minutes)

**Slide content:** Restore the original ATTACK_SCALES list and rerun L8.
L9 uses a fixed recovery case, separate from the scale you changed.

**Teaching notes:** Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.

**Exact source excerpt:** Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 58. L9 uses a fixed recovery case

**Timing:** 114:00–116:00 (2 minutes)

**Slide content:** Check the same case with and without replacement readings assumed to be trusted.
Its control value does not follow your L8 scale change.

**Teaching notes:** The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 59. Trusted readings are an assumption

**Timing:** 116:00–118:00 (2 minutes)

**Slide content:** The example assumes three independent angle readings are trustworthy.
The residual check and a model’s explanation cannot authenticate those readings.

**Teaching notes:** The example assumes three protected angle readings determine the three unknown angles, leaving zero residual degrees of freedom. Independent trusted information must come from a justified source outside this numerical calculation. A zero residual in this exactly determined system adds no detection guarantee. Neither a good model fit nor a language-model explanation establishes authenticity.

**Figure scope:** Three trusted angle readings are assumed, not authenticated by this calculation.

**Editable figure:** diagrams/cyber_trusted.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 60. Run L9: compare HOLD and PROPOSE

**Timing:** 118:00–120:00 (2 minutes)

**Slide content:** Run the whole L9 cell, including its assertions.
Read status first, then the proposed injection and the offline limit-violation count.

**Teaching notes:** The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.

**Exact source excerpt:** Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.
without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 61. Read the two decision states

**Timing:** 120:00–122:00 (2 minutes)

**Slide content:** No trusted replacement readings: HOLD, with no proposed injection.
Trusted readings assumed: PROPOSE; u ≈ 0.121694 p.u.; zero offline toy-model violations.

**Teaching notes:** Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.

**Figure scope:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Figure asset:** images/hands_on_L9_trust.png

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 62. Check the numerical correction

**Timing:** 122:00–124:00 (2 minutes)

**Slide content:** The QP solver minimizes effort, subject to branch limits and a 0.01 p.u. margin.
Predicted flow12: 0.17000; offline actual: about 0.17046, below the 0.18000 rating.

**Teaching notes:** QP means quadratic programming: this numerical solver minimizes a quadratic effort score while enforcing the declared branch limits and a 0.01 p.u. margin. The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. Predicted flow12 is 0.17000 p.u.; the offline actual flow is about 0.17046 p.u., below the 0.18000 p.u. rating. The actual-flow comparison uses synthetic truth for this fixed case. It does not guarantee AC behavior omitted by the model or trustworthy field telemetry.

**Figure scope:** Fixed L9 correction: compare the predicted branch flow with the offline truth check.

**Editable figure:** diagrams/cyber_qp.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 63. What makes the recovery possible?

**Timing:** 124:00–126:00 (2 minutes)

**Slide content:** Assumed trusted readings support the estimate. The solver calculates a limited correction.
The explanation must keep those conditions clear and leave the proposal for review.

**Teaching notes:** Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.

**Figure scope:** Trusted information and numerical checks have separate roles.

**Editable figure:** diagrams/cyber_handoff.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 64. Proposed agent role: request and explain

**Timing:** 126:00–128:00 (2 minutes)

**Slide content:** This cell runs Python. A proposed agent would request the approved estimate and control check.
The operator must confirm the trust basis and review the returned proposal.

**Teaching notes:** The default classroom calls are ordinary deterministic Python functions, so this cell makes no new language-model decision. The slide states a proposed agent responsibility: request the allowed estimator and control tool, then explain the exact conditions returned. The operator must establish the basis for trusting the replacement readings and review the limited proposal through the authorized process. The old model explanations in L10 come from a separate historical study and are not replies to this participant’s changed inputs.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 65. Cyber: Llama selects the tool already allowed

**Timing:** 128:00–130:30 (2.5 minutes)

**Slide content:** The task supplies the tool and trust assumption. Python computes the correction.

**Teaching notes:** Switch L10B to cyber. This standard four-bus DC record is separate from L10’s proposal-complete cyber record, and matches the Agent Trace notebook T6 archive. The route is narrow: the prompt already authorizes the tool and supplies the trusted-sensor assumption. The three angle readings give full rank but zero residual redundancy, so a good fit is not an independent trust test. u is the flexible injection correction in per unit. Offline synthetic-truth flow is available to the experimenter, not guaranteed available to a real operator. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later.

**Figure asset:** images/llama_cyber_7.png

**Notebook / source locator:** Classroom Labs L10B: cyber replay, recorded call 7; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 66. Cyber: a passing calculation still needs review

**Timing:** 130:30–133:00 (2.5 minutes)

**Slide content:** Keep REVIEW visible. The operator must resolve the trust assumption and missing checks.

**Teaching notes:** Read the actual reply, including the REVIEW choice. Numerical verification is PASS, but the overall result remains REVIEW and human acknowledgment is PENDING. The fixed comparator obtains the same numerical state estimate and correction without Llama. This replay demonstrates permitted tool routing and a report decision. It does not demonstrate better estimation, authenticated measurements, AC network security or operating authority. Run L11 with the default False setting, then proceed to L12. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later.

**Figure asset:** images/llama_cyber_8.png

**Notebook / source locator:** Classroom Labs L10B: cyber replay, recorded call 8; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 67. Cyber checkpoint: explain why PROPOSE is allowed

**Timing:** 133:00–135:00 (2 minutes)

**Slide content:** Report the trust assumption, model, proposed u and the checks that passed or failed.
Without independent trusted information, keep HOLD and name what is missing.

**Teaching notes:** Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.' Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 68. Run L10 before the Llama walkthrough

**Timing:** 135:00–138:00 (3 minutes)

**Slide content:** Run L10 to inspect its separate archived five-stage study.
Continue to L10B for the recorded Llama choices, then run L11 with its default False setting.

**Teaching notes:** L10 reads the archived proposal_complete_workflow study. It includes feeder-catalog restoration and is separate from the L6 six-node MILP and your edited classroom inputs. L10B, inserted immediately after L10, then gives readable verified replay episodes for all three cases. Run L11 after those replays; the default False setting skips a new local model request.

**Notebook / source locator:** Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 69. Run L10B: watch Llama choose a tool

**Timing:** 138:00–141:30 (3.5 minutes)

**Slide content:** Now replay the three saved episodes: set SCENARIO to voltage, restoration and cyber, rerunning each time.

**Teaching notes:** Run L10 first. In the new L10B cell the helper validates the original JSON reply against the parsed journal and trace, then displays the recorded episode. Change only SCENARIO to inspect the other two episodes. Earlier case slides previewed selected fields from these replays. Now inspect the full episodes in the same notebook. This cell makes no model request and performs no new electrical solve. At the end, run L11 at its default False setting before L12. Llama reasons are historical public returned text. Their correctness must be judged against the input and tool results. SCENARIO can be voltage, restoration or cyber. The full cell is shown.

**Exact source excerpt:** Classroom_Labs.ipynb L10B (classroom-llama-walkthrough), source lines 1–5.
SCENARIO = "voltage"  # Change to "restoration" or "cyber", then rerun this cell.
from IPython.display import HTML, display
from src.llama_walkthrough import load_episodes, render_episode_html
replay_episodes = load_episodes(ROOT)
display(HTML(render_episode_html(replay_episodes[SCENARIO])))

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L10B; cell classroom-llama-walkthrough; src/llama_walkthrough.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[OLL1] Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

## 70. Stanford example: check before you write

**Timing:** 141:30–144:30 (3 minutes)

**Slide content:** WikiChat checks claims against retrieved text before drafting its reply.
Our grid version: run the numerical check before writing the study summary.

**Teaching notes:** Stanford connection: Lam’s CS224V introduction, pp.19–20, uses WikiChat to illustrate splitting a response into retrieval, claim checking and writing. Our diagram is an original power-system teaching adaptation. Follow the voltage path: read the current allowance, choose a permitted candidate, calculate its result, check limits and explain the outcome. This is an analogy across domains, not evidence that WikiChat is a power-system controller. Ask pairs to name which step would detect a current violation. The figure shown here is an actual excerpt from the supplied Stanford lecture. Ask the audience to point to the claim-checking or policy step, then identify the corresponding Python check in our lab. We borrow the design habit; the notebook does not run WikiChat or Genie. Their non-grid benchmarks are not electrical performance results.

**Figure scope:** Monica Lam, Stanford CS224V, Lecture 1, Fall 2026, p.19. Original excerpt; full reference in the guide.

**Figure asset:** images/stanford_wikichat_steps.png

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.19.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 71. Stanford example: tools need clear rules

**Timing:** 144:30–147:00 (2.5 minutes)

**Slide content:** Write down the required inputs, permitted tools, limits and stop rules.
Our lab keeps those rules in Python. A language reply cannot change the limits.

**Teaching notes:** Stanford connection: Lam p.40 and the published Genie Worksheets paper emphasize developer-defined workflows and knowledge sources. The published framework uses an algorithmic runtime to enforce a supplied policy, with LLMs used for language understanding and response generation. Our lab uses custom Python functions, not Genie Worksheets. The application analogy is to specify the task and prevent a language reply from silently changing its limits or filling missing required inputs. A passed calculation does not prove that the task description was correct. The figure shown here is an actual excerpt from the supplied Stanford lecture. Ask the audience to point to the claim-checking or policy step, then identify the corresponding Python check in our lab. We borrow the design habit; the notebook does not run WikiChat or Genie. Their non-grid benchmarks are not electrical performance results.

**Figure scope:** Monica Lam, Stanford CS224V, Lecture 1, Fall 2026, p.40. Original excerpt; full reference in the guide.

**Figure asset:** images/stanford_genie_specification.png

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST03] Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.:** [https://aclanthology.org/2025.acl-long.1323/](https://aclanthology.org/2025.acl-long.1323/)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 72. Ask four questions about a study result

**Timing:** 147:00–149:00 (2 minutes)

**Slide content:** Find the tool result, assumptions, rules and the operator’s next step.
If a claim has no supporting result, leave it unresolved and request the missing check.

**Teaching notes:** Lam’s pp.52–53 distinguish verifiable rationale, explicit assumptions, policy consistency and actionable next conditions. Translate these into four plain questions: which tool supports this claim, which inputs and model were used, were the same limits and service priorities kept, and what must the operator review next? Our power-flow, optimization and evidence-binding checks are numerical/software checks. They do not inherit the lecture’s SMT correctness claims. Ask pairs to apply the questions to one L10B explanation and to the full-scope HOLD at L12. We show only the actual public returned reasons, not hidden chain-of-thought.

**Figure scope:** Grid teaching adaptation of Monica Lam’s accountability concepts, Stanford CS224V introduction, pp.52–53.

**Editable figure:** diagrams/lab_review_questions.tex

**Notebook / source locator:** Monica Lam, CS224V Lecture 1, pp.52–53; grid teaching adaptation and Classroom Labs L12.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 73. Finish L12: practice the readback

**Timing:** 149:00–154:00 (5 minutes)

**Slide content:** Run all of L12 after completing L0–L11 in notebook order.
Check wrong-ID rejection, simulated acknowledgment and equipment_dispatch=False.

**Teaching notes:** This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record. Readback means repeating the recommendation ID and conditions so the acknowledgment can be matched to the same proposal. In this exercise it is simulated. Check the wrong-ID rejection, the correct simulated acknowledgment and equipment_dispatch=False.

**Exact source excerpt:** Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.
wrong_id = lab.acknowledge(mv_scope, 'wrong-id', 'Student operator')
readback = lab.acknowledge(mv_scope, mv_scope['recommendation_id'], 'Student operator')

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 74. Read the two readback outcomes

**Timing:** 154:00–157:00 (3 minutes)

**Slide content:** Full MV/LV request: HOLD. The explicit MV teaching request allows a simulated readback.
A wrong recommendation ID is rejected. equipment_dispatch stays False.

**Teaching notes:** After running the complete L12 cell, compare these reference outputs with your own. The full MV/LV request remains HOLD because the checked model covers only MV phases. An explicit MV teaching request can pass the simulated readback after the recommendation ID matches. The wrong-ID attempt is rejected. Acknowledgment records a classroom review step and does not operate equipment.

**Figure scope:** Reference L12 output. Run L12 here, after the three cases and the L10B replay.

**Figure asset:** images/hands_on_L12_packet.png

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 75. Start a control-room pilot with a clear study request

**Timing:** 157:00–161:00 (4 minutes)

**Slide content:** Use an approved copy of the network data with a time stamp, topology version and limits.
If required data are missing or too old, return HOLD and name the missing information.

**Teaching notes:** Proposed advisory pilot, not a deployment claim. F12 is an illustrative teaching feeder name. Read the study request aloud: compare the allowed voltage-support options, keep the stated current and voltage limits, show the worst margins and missing checks, and return a recommendation for review. The data owner defines acceptable age, source and quality rules. L1 and L7 illustrate matching inputs to results, but hashes alone do not authenticate those sources.

**Figure scope:** Proposed advisory pilot — teaching design. F12 is an illustrative identifier.

**Editable figure:** diagrams/ops_request_snapshot.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 76. Give the assistant a small, controlled tool list

**Timing:** 161:00–165:00 (4 minutes)

**Slide content:** An approved interface supplies read-only data and study tools. Log every request and result.
Keep equipment commands in the utility’s separate authorized operating process.

**Teaching notes:** Proposed advisory pilot. Walk through the lanes: operator, assistant, application-controlled tool gateway and engineering tools. Llama requests one permitted function; the application checks the request and executes the tool. A snapshot identifier binds the result to the input. The workshop Python functions are teaching counterparts, not SCADA adapters. NIST OT guidance supports controlled information flows, least privilege and logging. The exact pilot architecture is our teaching recommendation, not a NIST-certified design.

**Figure scope:** Proposed advisory pilot — teaching design. Classroom functions are not live control-room interfaces.

**Editable figure:** diagrams/ops_tool_boundary.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**[OLL1] Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 77. Check three things before returning a proposal

**Timing:** 165:00–169:00 (4 minutes)

**Slide content:** Check that the inputs match, the required limits pass and the required network parts were modeled.
Example: an MV-only PASS stays on HOLD when the request requires the full MV/LV network.

**Teaching notes:** Proposed advisory pilot. Current data and a matching evidence packet are the first gate. The second gate checks stated engineering limits with approved tools. The third asks whether the calculations cover the request, including excluded low-voltage parts or required protection and dynamic studies. This is not a universal complete security checklist. It illustrates why L12 can produce a passing local calculation and still HOLD a broader request. Make missing evidence visible instead of allowing fluent text to fill the gap.

**Figure scope:** Proposed advisory pilot — teaching design. A PASS is limited to its tested model and inputs.

**Editable figure:** diagrams/ops_three_gates.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

## 78. Give the operator a short evidence packet

**Timing:** 169:00–173:00 (4 minutes)

**Slide content:** Show the input snapshot, selected option, worst margins, rejected trials and missing checks.
The reviewer can ask for another study, reject the proposal or accept it for the next review step.

**Teaching notes:** Proposed advisory pilot. Use three review questions: Does this match the current equipment, inputs and model? Did the required checks pass, with missing checks clear? What exactly am I approving, who owns the next step, and where is the record? Record the reviewer, reason, case snapshot and tool versions. Accepting a study result does not itself issue an equipment command. Authorized operating procedures and roles determine any later physical action. L12 practices only a simulated ID-bound readback.

**Figure scope:** Proposed advisory pilot — teaching design. Review of a study is distinct from operating equipment.

**Editable figure:** diagrams/ops_review.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**[EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

## 79. Adopt it in stages and measure the benefit

**Timing:** 173:00–177:00 (4 minutes)

**Slide content:** Begin with past cases, then read-only shadow work, then a limited pilot with named reviewers.
Compare against the same tools in a fixed script: correct studies, missed checks, time and rework.

**Teaching notes:** Proposed advisory pilot. Historical replay lets engineers define expected outcomes and failure cases. Shadow use compares recommendations alongside the existing process without relying on them for equipment control. A limited pilot needs a named owner, training, an agreed scope and a way to stop use. Measure end-to-end elapsed time including review, correct completed studies, missed or stale inputs, overlooked limits and reviewer changes. Compare the same engineering tools with and without Llama. Our paired records show identical final numerical results, so there is no basis yet to promise higher accuracy, less operator workload or faster decisions. NIST AI RMF supports human roles, evaluation under realistic conditions and deactivation; these particular pilot metrics are our recommendation.

**Figure scope:** Proposed advisory pilot — teaching design. Benefits must be measured against an appropriate baseline.

**Editable figure:** diagrams/ops_pilot.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

## 80. Save a workshop record others can repeat

**Timing:** 177:00–180:00 (3 minutes)

**Slide content:** Save your changed inputs and results, labeled new, archived or simulated.
Explain the request, tool call, result, checks and next decision.

**Teaching notes:** Use the final three minutes for pair reports and saving. Each pair names one changed parameter, compares its predicted and observed result, and states one evidence limit. Another person should be able to repeat the experiment from the saved notebook. The reading guide supplies the full source links, stable cell map and debrief answers.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## [H00] Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## [B01] IEEE Communications Society: official resources and network presentation template

**Authors / issuer:** IEEE Communications Society

**Publisher / venue:** IEEE Communications Society

**Date:** Reviewed 17 October 2026

**Theme assets:** comsoc-lockup.png and image7.png; independent educational adaptation

**Full source URL:** [https://www.comsoc.org/about/brand-experience/resources](https://www.comsoc.org/about/brand-experience/resources)

## [DEF03] Building effective agents

**Authors / issuer:** Erik S., Barry Zhang

**Publisher / venue:** Anthropic Engineering

**Date:** 2024-12-19

**Type:** Official practitioner architecture account by the system maintainers

**Location:** What are agents?; Agents; Workflow: Routing; Workflow: Orchestrator-workers; Workflow: Evaluator-optimizer

**Version note:** The live page now warns that tooling has changed since the original publication. Use its conceptual distinction, not its present SDK list as a claim about the 2024 implementation.

**Full source URL:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

## [LR0] L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py

**Authors / issuer:** Classroom Labs notebook and Python helper

**Publisher / venue:** Public reproducible teaching material

**Date:** 24 October 2026

**Type:** Verified historical reply replay

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [LRV] Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 27 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/workshop_run_opendss.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/workshop_run_opendss.json)

## [OLL1] Structured Outputs: generating structured JSON with a schema

**Authors / issuer:** Ollama documentation maintainers

**Publisher / venue:** Official Ollama documentation

**Date:** Reviewed 24 October 2026

**Type:** Official API documentation

**Full source URL:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

## [COL01] Frequently Asked Questions: Using Colab, notebook storage and execution state

**Authors / issuer:** Google Colaboratory

**Publisher / venue:** Google Research

**Date:** Reviewed 24 October 2026

**Type:** Official product documentation

**Full source URL:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

## [H02] Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H01] Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

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

## [ST01] CS224V Agentic AI, Lecture 1: Introduction

**Authors / issuer:** Monica Lam

**Publisher / venue:** Stanford University

**Date:** Fall 2026

**Type:** University lecture slides, supplied by the presenter

**Full source URL:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**Publication:** [https://web.stanford.edu/class/cs224v/](https://web.stanford.edu/class/cs224v/)

## [ST02] WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia

**Authors / issuer:** Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam

**Publisher / venue:** Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413

**Date:** December 2023

**Type:** Peer-reviewed dialogue research

**Full source URL:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**Full paper PDF:** [https://aclanthology.org/2023.findings-emnlp.157.pdf](https://aclanthology.org/2023.findings-emnlp.157.pdf)

**Source code:** [https://github.com/stanford-oval/WikiChat](https://github.com/stanford-oval/WikiChat)

## [OT01] Guide to Operational Technology (OT) Security

**Authors / issuer:** Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson

**Publisher / venue:** National Institute of Standards and Technology, NIST SP 800-82 Revision 3

**Date:** September 2023 (final)

**Type:** Published OT security guidance

**Full source URL:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**Full paper PDF:** [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)

**Publication:** [https://csrc.nist.gov/pubs/sp/800/82/r3/final](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

## [H03] Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H04] Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H05] Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H06] Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

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

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [LRR] Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 27 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json)

## [H08] Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

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

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [LRC] Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 21 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json)

## [H10] Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [ST03] Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets

**Authors / issuer:** Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam

**Publisher / venue:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308

**Date:** July 2025

**Type:** Peer-reviewed task-oriented dialogue framework

**Full source URL:** [https://aclanthology.org/2025.acl-long.1323/](https://aclanthology.org/2025.acl-long.1323/)

**Full paper PDF:** [https://aclanthology.org/2025.acl-long.1323.pdf](https://aclanthology.org/2025.acl-long.1323.pdf)

**Source code:** [https://github.com/stanford-oval/genie-worksheets](https://github.com/stanford-oval/genie-worksheets)

## [H12] Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [EVAL01] Artificial Intelligence Risk Management Framework (AI RMF 1.0)

**Authors / issuer:** National Institute of Standards and Technology

**Publisher / venue:** NIST AI 100-1

**Date:** 26 January 2023

**Type:** Voluntary risk-management guidance

**Full source URL:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

**Full paper PDF:** [https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

## Visual credit: hands_on_L1_binding.png

**Caption:** Reference L1 output: only the unchanged request and command match the evidence.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 10. Run L1: does the evidence still match?

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L1 output: only the unchanged request and command match the evidence.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L1_binding.png](research/evidence/replots/hands_on_L1_binding.png)

## Visual credit: feeder.png

**Caption:** Synthetic SMART-DS teaching feeder; not an operating utility circuit.

**Credit:** Existing GridGuard workshop numerical figure

**Used on:** 11. Voltage: open L2

**Asset type:** Synthetic feeder visualization

**Transformation:** Unchanged original plot.

**Evidence limit:** Synthetic SMART-DS teaching feeder; not an operating utility circuit.

**Original source / page:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

**Original figure / image URL:** [research/evidence/replots/feeder.png](research/evidence/replots/feeder.png)

## Visual credit: hands_on_L2_plot.png

**Caption:** Reference L2 plots; rerun L2 to calculate plots for your inputs.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 16. Read the voltage and current plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L2 plots; rerun L2 to calculate plots for your inputs.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_plot.png](research/evidence/replots/hands_on_L2_plot.png)

## Visual credit: hands_on_L2_table.png

**Caption:** Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 17. Check limits before comparing scores

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_table.png](research/evidence/replots/hands_on_L2_table.png)

## Visual credit: hands_on_L4_checks.png

**Caption:** Reference L4 output: old selector choices, new numerical checks of the original case.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 26. Separate the old choice from the new check

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L4 output: old selector choices, new numerical checks of the original case.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L4_checks.png](research/evidence/replots/hands_on_L4_checks.png)

## Visual credit: hands_on_L5_scope.png

**Caption:** Reference L5 output: a medium-voltage check with OpenDSS disabled.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 28. A PASS covers only the model checked

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L5 output: a medium-voltage check with OpenDSS disabled.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L5_scope.png](research/evidence/replots/hands_on_L5_scope.png)

## Visual credit: llama_voltage_1.png

**Caption:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 29. Voltage: Llama asks to check the saved controller

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_1.png](research/evidence/replots/llama_voltage_1.png)

## Visual credit: llama_voltage_2.png

**Caption:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 30. Voltage: Llama chooses the existing fallback plan

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_2.png](research/evidence/replots/llama_voltage_2.png)

## Visual credit: llama_voltage_3.png

**Caption:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 31. Voltage: the checks pass and human review remains

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved voltage example; separate from this case’s fresh calculation. Replay it in L10B later.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_3.png](research/evidence/replots/llama_voltage_3.png)

## Visual credit: hands_on_L6_plot.png

**Caption:** Reference L6 plots; rerun L6 to compare your chosen tie capacities.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 36. Read both service plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L6 plots; rerun L6 to compare your chosen tie capacities.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_plot.png](research/evidence/replots/hands_on_L6_plot.png)

## Visual credit: hands_on_L6_table.png

**Caption:** Reference L6 results at a 40 kW tie limit: compare total and critical load served.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 37. The tradeoff at a 40 kW tie limit

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L6 results at a 40 kW tie limit: compare total and critical load served.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_table.png](research/evidence/replots/hands_on_L6_table.png)

## Visual credit: hands_on_L7_binding.png

**Caption:** Reference L7 output: changed request, unchanged evidence, so a new check is needed.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 42. Read the evidence-match test

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L7 output: changed request, unchanged evidence, so a new check is needed.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L7_binding.png](research/evidence/replots/hands_on_L7_binding.png)

## Visual credit: llama_restoration_14.png

**Caption:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 46. Restoration: Llama chooses a useful new trial

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_14.png](research/evidence/replots/llama_restoration_14.png)

## Visual credit: llama_restoration_15.png

**Caption:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 47. Restoration: the next trial crosses the current limit

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_15.png](research/evidence/replots/llama_restoration_15.png)

## Visual credit: llama_restoration_16.png

**Caption:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 48. Restoration: catch Llama’s wrong ranking

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved restoration example; separate from this case’s fresh calculation. Replay it in L10B later.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_16.png](research/evidence/replots/llama_restoration_16.png)

## Visual credit: hands_on_L8_plot.png

**Caption:** Reference L8 plots; rerun L8 to calculate results for your chosen attack scales.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 53. Read both cyber plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L8 plots; rerun L8 to calculate results for your chosen attack scales.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L8_plot.png](research/evidence/replots/hands_on_L8_plot.png)

## Visual credit: hands_on_L9_trust.png

**Caption:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 61. Read the two decision states

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L9_trust.png](research/evidence/replots/hands_on_L9_trust.png)

## Visual credit: llama_cyber_7.png

**Caption:** Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 65. Cyber: Llama selects the tool already allowed

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_cyber_7.png](research/evidence/replots/llama_cyber_7.png)

## Visual credit: llama_cyber_8.png

**Caption:** Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 66. Cyber: a passing calculation still needs review

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved cyber example; separate from this case’s fresh calculation. Replay it in L10B later.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_cyber_8.png](research/evidence/replots/llama_cyber_8.png)

## Visual credit: stanford_wikichat_steps.png

**Caption:** Monica Lam, Stanford CS224V, Lecture 1, Fall 2026, p.19. Original excerpt; full reference in the guide.

**Credit:** Monica Lam, Stanford University, CS224V Lecture 1: Introduction, Fall 2026.

**Used on:** 70. Stanford example: check before you write

**Asset type:** Original lecture figure excerpt

**Transformation:** Cropped vector excerpt from the user-supplied lecture PDF, p.19; selected content unchanged. PNG derived with Poppler. Full provenance: research/stanford_80/excerpt_manifest.json.

**Provenance note:** Cropped from the supplied Stanford lecture PDF. Original author and page retained in the caption and full source guide.

**Evidence limit:** Monica Lam, Stanford CS224V, Lecture 1, Fall 2026, p.19. Original excerpt; full reference in the guide.

**Original source / page:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=19](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=19)

**Original figure / image URL:** [research/evidence/replots/stanford_wikichat_steps.png](research/evidence/replots/stanford_wikichat_steps.png)

## Visual credit: stanford_genie_specification.png

**Caption:** Monica Lam, Stanford CS224V, Lecture 1, Fall 2026, p.40. Original excerpt; full reference in the guide.

**Credit:** Monica Lam, Stanford University, CS224V Lecture 1: Introduction, Fall 2026.

**Used on:** 71. Stanford example: tools need clear rules

**Asset type:** Original lecture figure excerpt

**Transformation:** Cropped vector excerpt from the user-supplied lecture PDF, p.40; selected content unchanged. PNG derived with Poppler. Full provenance: research/stanford_80/excerpt_manifest.json.

**Provenance note:** Cropped from the supplied Stanford lecture PDF. Original author and page retained in the caption and full source guide.

**Evidence limit:** Monica Lam, Stanford CS224V, Lecture 1, Fall 2026, p.40. Original excerpt; full reference in the guide.

**Original source / page:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=40](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=40)

**Original figure / image URL:** [research/evidence/replots/stanford_genie_specification.png](research/evidence/replots/stanford_genie_specification.png)

## Visual credit: hands_on_L12_packet.png

**Caption:** Reference L12 output. Run L12 here, after the three cases and the L10B replay.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 74. Read the two readback outcomes

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L12 output. Run L12 here, after the three cases and the L10B replay.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L12_packet.png](research/evidence/replots/hands_on_L12_packet.png)
