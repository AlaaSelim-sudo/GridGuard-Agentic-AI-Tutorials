# Instructor Guide: Hands-on Three Operator Cases

59 static slides / 120.0 minutes. Opening: 9 slides / 12.0 minutes; Voltage support: 17 slides / 36 minutes; Service restoration: 14 slides / 28 minutes; Cyber response: 16 slides / 32 minutes; Closing: 3 slides / 12 minutes. Follow the L labels and stable notebook cell IDs; predict, run, edit and interpret each result. The three exercises have separate teacher notes and debriefs. Numerical calculations and archived model replies remain distinct. No tables, transitions or click reveals.

## 1. Hands-on: Three Operator Cases

00:00–00:30 / 0.5 minutes.

Open Classroom Labs before the workshop. Participants will run fresh numerical calculations and inspect clearly labeled archived model replies. Use the same notebook for all three cases. If devices are limited, work in pairs: one person runs the cells while the other checks the evidence.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources

## 2. Open one notebook for all three cases

00:30–02:00 / 1.5 minutes.

Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

## 3. Connect a CPU and run the setup cell

02:00–04:00 / 2 minutes.

For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or model download. If setup stops, reconnect the runtime and rerun setup before starting L0.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

## 4. Find cells by L label, not by cell number

04:00–05:00 / 1 minutes.

The added Colab setup cells changed the numerical cell positions. Use the L headings and stable cell IDs to find the same source in Colab, Jupyter and these slides. A slide shows only the relevant code fragment. Students should run the complete matching notebook cell.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

## 5. Run L0: choose the classroom route

05:00–07:00 / 2 minutes.

Run all of L0 to import the helpers, configure the plots and initialize the timing record. Keep RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. These settings skip the optional full-feeder OpenDSS route and local model service. They do not make the calculations prerecorded: L2 and L4 through L9 run fresh numerical calculations or checks, while L12 checks the evidence binding and simulated readback.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L0 (classroom-002), source lines 11–14.):

```python
RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / 'data/lindistflow3_network.json').exists(), 'Start Jupyter in the tutorial folder'
```

## 6. Know which evidence you are reading

07:00–08:30 / 1.5 minutes.

The diagram shows responsibilities. Ordinary Python functions perform the engineering calculations; this notebook does not run through LangGraph. A model reply remains an archived event when displayed today. A language model does not replace the power-flow solver, MILP or state estimator.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 7. Run L1: does old evidence still match?

08:30–10:00 / 1.5 minutes.

Treat this first check as a content-consistency test, not a physical feasibility test. The first row keeps the request and command unchanged. The next two rows change a request field or command field. A failed binding requires fresh evidence, but does not prove the changed action is infeasible. A matching hash does not authenticate a sensor.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 8. Use the same cycle in every case

10:00–11:00 / 1 minutes.

Pause before showing each output. Ask pairs to write one sentence predicting the change, then compare it with the calculated result. Keep the input values and evidence together. Change only one parameter in the first experiment.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 9. Keep a short experiment record

11:00–12:00 / 1 minutes.

Participants can add a text cell below an output or use paper notes; no extra software is needed. Each pair should finish with one changed-input experiment that another person can repeat. Explain the result and one limit on the claim. The three cases use different networks and do not form a single utility deployment study.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

## 10. Voltage: start with L2

12:00–14:00 / 2 minutes.

The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The default backend models MV phases and MV line currents, with idealized LV aggregation. Run L0 and L1 before this cell.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.
Full source: https://data.openei.org/submissions/2981

## 11. Read the control and limits

14:00–16:00 / 2 minutes.

The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltage bounds are 0.95 to 1.05 p.u. RATING_FRACTION=0.80 sets the allowed current to 80% of the nominal rating. The displayed current percentage uses that reduced allowance as its denominator. Passing the inverter bounds alone does not establish network feasibility.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 12. Run L2 with the default inputs

16:00–18:00 / 2 minutes.

Start with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. The saved SAC actor produces a new proposal by inference; it is not trained in this cell. Both proposals pass the default classroom checks. MPC has the lower current-step J for this case and objective. This single result does not establish a universal control advantage.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
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

## 13. Read your voltage plots

18:00–20:00 / 2 minutes.

The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 14. Read feasibility before cost

20:00–22:00 / 2 minutes.

In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 15. Exercise 1: tighten the current allowance

22:00–26:00 / 4 minutes.

Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 16. Debrief: a tighter allowance can still pass

26:00–28:00 / 2 minutes.

An incorrect prediction is useful evidence, not a failed exercise. Compare the hypothesis with the actual output. Both candidates retain enough headroom in this case. An optimizer may change its command when a constraint changes, so a simple fixed-ratio argument does not apply to every scenario. The model scope has not expanded.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 17. Reset L2 before the recorded-choice lesson

28:00–30:00 / 2 minutes.

Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.):

```python
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
```

## 18. L3 starts a separate recorded context

30:00–32:00 / 2 minutes.

The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.):

```python
pool = lab.saved_pool('test_01')
display(pd.DataFrame(pool['responses'])[['model_id', 'operation_id', 'reason', 'seconds', 'source']])
```

## 19. What did the language models choose?

32:00–34:00 / 2 minutes.

The three recorded replies reduce to two distinct canonical operations. The vote retains one contribution per model identity. In test_01, the Q-relaxation trial receives two votes. This diagram represents the archived input; it is not a new vote after a learner edits L2.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 20. Run L4: check the recorded choice again

34:00–36:00 / 2 minutes.

The selector is frozen and makes no training updates in this lesson. L4 applies the archived selected operation to its original test context and runs a fresh numerical check. This is a replay with new verification, not a new language-model decision or an online learning experiment.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.):

```python
started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings['L4 new verification of archived choices'] = time.perf_counter() - started
display(selected_trials['table'])
assert pool['frozen'] and pool['training_updates'] == 24
```

## 21. Separate the old choice from the new check

36:00–38:00 / 2 minutes.

The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 22. Run L5: identify the model scope

38:00–40:00 / 2 minutes.

L5 reconstructs the original test_01 context and freshly checks its archived MV-MPC incumbent. This is not the Q-relaxation candidate checked in L4. With RUN_OPENDSS=False, it checks only the reduced model and reports that OpenDSS is disabled. It produces no fresh full-feeder audit in this CPU route. A separate recorded broader-model study is not a result calculated today.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.):

```python
started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings['L5 selected model scope checks'] = time.perf_counter() - started
display(scope_audit['table'])
```

## 23. A PASS belongs to the model that produced it

40:00–42:00 / 2 minutes.

Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 24. Preview the handoff you will build at L12

42:00–44:00 / 2 minutes.

Preview the purpose of the final handoff without asking participants to jump ahead. L12 will use selected_trials from L4, not the fresh L2 comparison. It contrasts a full MV/LV request with an explicit MV-only teaching request. Continue to L6 after the voltage checkpoint, finish L6–L11, and run L12 once in the closing section. The readback is a simulated teaching event with no equipment dispatch.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 25. Preview: the two handoff outcomes

44:00–46:00 / 2 minutes.

This screenshot previews the executed default L12 result; students have not run L12 yet. At the final step they will check the returned state and acknowledgment fields. The full-coverage request remains HOLD; the explicit MV teaching scope allows a simulated readback. The simulation does not complete human approval of an archived study and does not dispatch equipment.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 26. Voltage checkpoint: state exactly what ran

46:00–48:00 / 2 minutes.

Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates proposals for the current classroom inputs. L3 displays archived replies, L4 rechecks selected trials, and L5 checks the archived incumbent's model scope. Numerical tools provide the physical evidence; the bounded model choice selects a permitted trial. The operator receives a scoped advisory record.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 27. Restoration: open L6

48:00–49:00 / 1 minutes.

This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 28. Read the objective before choosing a plan

49:00–51:00 / 2 minutes.

Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective expresses a service policy. The difference between the plans comes from that objective. Neither numerical optimizer needs a language model to solve this declared problem.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 29. Run L6: sweep the tie capacity

51:00–53:00 / 2 minutes.

Start with capacities of 40, 60, 80, 100 and 120 kW. The solver enforces active-power balance, capacity limits, source connectivity, radiality and fault exclusion. Independent enumeration checks the priority objective on this small graph. Agreement supports this formulation; it does not check omitted AC physics.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.):

```python
CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings['L6 fresh MILP sweep + independent enumeration'] = time.perf_counter() - started
display(restoration['table'].drop(columns='pickup'))
```

## 30. Read the two service plots together

53:00–55:00 / 2 minutes.

The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 31. Explain the 40 kW tradeoff

55:00–57:00 / 2 minutes.

Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 32. How Python checks the plan

57:00–59:00 / 2 minutes.

Numerical verification and evidence binding answer different questions. A correctly bound record may still omit AC voltage, reactive-power or protection constraints. Minimizing energized branches does not calculate the number or order of physical switching operations.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.
Full source: https://arxiv.org/abs/1912.05185v3
Full paper: https://arxiv.org/pdf/1912.05185v3

Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.
Full source: https://doi.org/10.1109/TPWRS.2017.2720122

## 33. Exercise 2: add more tie capacity

59:00–63:00 / 4 minutes.

Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 34. Debrief: enough capacity removes this tradeoff

63:00–65:00 / 2 minutes.

Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 35. Reset the sweep; then run L7

65:00–67:00 / 2 minutes.

Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.):

```python
rest_record = restoration['records'][0]['weighted']
rest_request = {'task': 'restoration', 'capacity_kw': CAPACITIES_KW[0],
                'critical_nodes': [2, 5], 'model': 'six_node_active_transport', 'revision': 1}
```

## 36. Read the changed-evidence test

67:00–69:00 / 2 minutes.

This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 37. A failed binding asks for a new check

69:00–71:00 / 2 minutes.

The diagram's extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision. Do not say that participants changed topology in the notebook. Ask which numerical step would establish feasibility for the changed request.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 38. The agent must preserve the service policy

71:00–73:00 / 2 minutes.

A language model must not silently change priority weights or invent pickup values. A different service policy needs an explicit request and a new solve. This classroom supervisor uses ordinary Python. The numerical difference comes from the optimization objective.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 39. State what the model leaves out

73:00–74:00 / 1 minutes.

State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 40. Restoration checkpoint: name the next action

74:00–76:00 / 2 minutes.

Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 41. Cyber: open L8

76:00–77:00 / 1 minutes.

The four-bus model has three non-slack voltage angles and eight measurements. It is not an AC estimator, malware detector or sensor-authentication system. Synthetic truth is available only for the offline classroom comparison.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 42. Read residual and state error separately

77:00–79:00 / 2 minutes.

The chi-square threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. A small J does not establish that the measurements are authentic.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678

## 43. Run L8: compare two attack patterns

79:00–81:00 / 2 minutes.

This cell runs fresh weighted-least-squares calculations. The coordinated counterexample assumes knowledge of the linear measurement matrix and access to the modeled unprotected channels. It is a declared defensive teaching model, not evidence of an incident at a utility.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.):

```python
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings['L8 fresh WLS attack sweep'] = time.perf_counter() - started
display(cyber['table'])
```

## 44. Read your two plots together

81:00–83:00 / 2 minutes.

The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 45. At scale 1, what does the alarm miss?

83:00–85:00 / 2 minutes.

The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.
Full source: https://doi.org/10.1145/1952982.1952995
Full paper: https://reitermk.github.io/papers/2011/TISSEC2.pdf

## 46. Exercise 3: add a small isolated bias

85:00–89:00 / 4 minutes.

Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 47. Debrief: a quiet alarm is not proof of truth

89:00–91:00 / 2 minutes.

Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 48. Reset the sweep before recovery

91:00–92:00 / 1 minutes.

Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.):

```python
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
```

## 49. L9 is a fixed recovery example

92:00–94:00 / 2 minutes.

The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 50. Where do the trusted readings come from?

94:00–96:00 / 2 minutes.

Three protected angle readings determine three unknown angles, leaving zero residual degrees of freedom. A zero residual in this exactly determined system provides no new detection guarantee. The trust premise must be justified outside this numerical example.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 51. Run L9: compare HOLD with PROPOSE

96:00–98:00 / 2 minutes.

The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.):

```python
without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)
```

## 52. Read the two decision states

98:00–100:00 / 2 minutes.

Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 53. Check the numerical correction

100:00–102:00 / 2 minutes.

The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. The offline actual flow is an audit against synthetic truth for this fixed case. It does not guarantee unmodeled AC behavior or trustworthy field telemetry.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 54. Trace what caused the improvement

102:00–104:00 / 2 minutes.

Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 55. Agent request, tool result, operator decision

104:00–106:00 / 2 minutes.

The default classroom calls are deterministic Python functions. The archived model explanations shown in L10 belong to a separate historical study. A real agent implementation would need to bind an allowed request to these tools. This default route makes no new language-model decisions.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 56. Cyber checkpoint: state the condition behind PROPOSE

106:00–108:00 / 2 minutes.

Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.'

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 57. Run L10–L11 with the evidence labels visible

108:00–111:00 / 3 minutes.

L10 reads the archived proposal_complete_workflow study, which has its own models and includes feeder-catalog restoration. It is not the L6 six-node MILP. Use L10 to inspect returned stage evidence and original timings, not as the result of a learner's edited L2, L6 or L8 inputs. In this CPU workshop, L11 explicitly skips the optional model call. This route generates no new LLM reply.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 58. Finish L12: practice the operator readback

111:00–115:00 / 4 minutes.

This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Exact displayed excerpt (Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.):

```python
wrong_id = lab.acknowledge(mv_scope, 'wrong-id', 'Student operator')
readback = lab.acknowledge(mv_scope, mv_scope['recommendation_id'], 'Student operator')
```

## 59. Save a reproducible workshop record

115:00–120:00 / 5 minutes.

Use the final five minutes for pair reports and saving. Each pair names one changed parameter, compares its predicted and observed result, and states one evidence limit. Another person should be able to repeat the experiment from the saved notebook. The reading guide supplies the full source links, stable cell map and debrief answers.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; notebook cells checked against revision 4fa0e70.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

