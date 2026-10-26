# Presenter script: three operator cases

**Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.**

80 slides / 180 teaching minutes / one required notebook / three four-minute exercises.

Use Say for the spoken explanation and Do / discuss for demonstrations and audience prompts. Timings include code execution, pair work and discussion; add breaks outside the 180-minute teaching schedule.

Start with the twelve-minute Stanford concept block, then seven minutes of Colab setup. Follow one Classroom Labs notebook in order through L0-L12, including L10B after L10. Leave both live-tool switches False for the standard route.

Python calculates fresh numerical results. L10B replays saved Llama replies and their original tool results. The recorded studies are separate from learner edits. L12 is a simulated readback and equipment_dispatch remains False.

[Slides](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/1) · [Classroom Labs](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb) · [Full sources](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Full_Reading_Guide.html)

## Session route

- [1. Stanford concepts and Colab setup](#module-opening): slides 1-15, 00:00:00-00:19:00.
- [2. Voltage support](#module-voltage): slides 16-37, 00:19:00-01:08:00.
- [3. Service restoration](#module-restoration): slides 38-53, 01:08:00-01:43:30.
- [4. Cyber response](#module-cyber): slides 54-69, 01:43:30-02:18:30.
- [5. Llama replay and operator review](#module-closing): slides 70-80, 02:18:30-03:00:00.

Exercises: slides 25, 44 and 59. Run one four-minute timer for each. Reset the changed input before continuing.

<a id="module-opening"></a>

## 1. Stanford concepts and Colab setup

### Slide 1. Hands-on: Three Operator Cases

00:00:00-00:00:30 / 0.5 minutes

**Say:** One notebook. Three operator problems. 90 minutes / three short exercises

**Do / discuss:** Have slides, Classroom Labs and the Participant Lab Guide ready. Pair participants. Allow breaks outside the 180 teaching minutes.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/1)

### Slide 2. What is agentic AI?

00:00:30-00:01:30 / 1 minutes

**Say:** An AI agent chooses a tool, reads its result and chooses the next step toward a goal.

**Do / discuss:** Ask which part supplies a physical result. Expected: the numerical tool. Ordinary programs can also contain loops.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/2) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/2)

### Slide 3. A tool call and an agent workflow

00:01:30-00:02:30 / 1 minutes

**Say:** A tool call does one job. An agent links jobs using the returned results.

**Do / discuss:** Point to the original function-calling and workflow panels. Follow the source link for lecture p.2.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/3) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/3)

### Slide 4. Evidence before an answer

00:02:30-00:03:45 / 1.25 minutes

**Say:** WikiChat checks claims before writing. Our lab checks numbers before reporting a result.

**Do / discuss:** Point to fact checking before Draft. Ask what numerical evidence a grid proposal would need.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/4) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/4)

### Slide 5. Voltage: propose, then check

00:03:45-00:05:15 / 1.5 minutes

**Say:** L2 calculates and checks proposals. L10B shows saved Llama tool choices.

**Do / discuss:** Preview L2 now; run it after setup, L0 and L1. The bar is a reference result, separate from the P3 replay.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/5) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/5)

### Slide 6. Clear rules for tool use

00:05:15-00:06:30 / 1.25 minutes

**Say:** Set the inputs, allowed tools, limits and stop rules. Python keeps these rules fixed when Llama chooses a step.

**Do / discuss:** Ask which task rules must remain fixed when comparing restoration plans.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/6) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/6)

### Slide 7. Restoration: define the service goal

00:06:30-00:08:00 / 1.5 minutes

**Say:** The goal changes which loads the solver restores. L6 compares two goals.

**Do / discuss:** Compare the cyan critical-service segments. The varied tie is 40 kW, another tie stays at 100 kW, and totals include upstream load.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/7) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/7)

### Slide 8. Language and decision checks

00:08:00-00:09:15 / 1.25 minutes

**Say:** The source example turns written facts into constraints for a solver. In our lab, Llama requests a study. Python checks it. A person reviews it.

**Do / discuss:** Explain SMT briefly as logical constraints and MaxSAT as supporting decision-changing conditions. Our lab uses numerical checks and no SMT guarantee.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/8) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/8)

### Slide 9. Cyber: good fit can hide bad data

00:09:15-00:10:45 / 1.5 minutes

**Say:** L8 tests misleading readings. L9 shows when to return HOLD or a proposal.

**Do / discuss:** Ask why a clear explanation cannot establish sensor trust.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/9) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/9)

### Slide 10. Four questions about any result

00:10:45-00:12:00 / 1.25 minutes

**Say:** Which tool ran? What did it assume? Which limits passed? What should the operator do next?

**Do / discuss:** Collect one example of a missing check, then start Colab setup.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/10) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/10)

### Slide 11. One notebook for all three cases

00:12:00-00:13:00 / 1 minutes

**Say:** Open Classroom Labs and save a copy in Drive. Use it throughout.

**Do / discuss:** Open Classroom Labs and save a copy. Keep the same notebook open for all three cases.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/11) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/11)

### Slide 12. Colab setup

00:13:00-00:14:30 / 1.5 minutes

**Say:** Save a copy, connect a CPU and run setup. Wait for Ready, then run L0 and L1.

**Do / discuss:** Connect a CPU runtime and run the first setup cell. Wait for Ready. After a reset, rerun setup and the required earlier cells.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/12) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/12)

### Slide 13. Input, run, output

00:14:30-00:16:00 / 1.5 minutes

**Say:** Find the L heading and run its whole code cell. Read the output below it. After any edit, rerun the cell.

**Do / discuss:** Locate input, play button and output. Run the complete named L cell; slide code is often an excerpt.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/13) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/13)

### Slide 14. L0: keep the default settings

00:16:00-00:17:00 / 1 minutes

**Say:** Leave both switches False. Python calculates new results; Llama replies come from saved records. If data are missing, rerun setup.

**Do / discuss:** Run L0 with RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. If the data check fails, rerun setup.

Notebook: Run the full L0 cell. Stable ID: classroom-002; slide excerpt: source lines 11-14.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/14) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/14)

### Slide 15. L1: does the result match the request?

00:17:00-00:19:00 / 2 minutes

**Say:** Read binding_pass. Expect True, False, False. Changed inputs or commands need a new check.

**Do / discuss:** Run L1. Read binding_pass as True, False, False. Ask what changed in each row.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/15) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/15)

<a id="module-voltage"></a>

## 2. Voltage support

### Slide 16. Case 1: voltage support

00:19:00-00:21:00 / 2 minutes

**Say:** MPC plans ahead. SAC uses a saved learned policy. Check limits first. Among passing options, a smaller score J is better.

**Do / discuss:** Locate L2 and identify this synthetic teaching feeder.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/16) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/16)

### Slide 17. Two ways to propose settings

00:21:00-00:22:30 / 1.5 minutes

**Say:** MPC plans with a model. SAC proposes from learned weights. Both need the same electrical checks.

**Do / discuss:** Define MPC as model predictive control and SAC as Soft Actor–Critic. SAC uses saved weights without training again.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/17) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/17)

### Slide 18. A tool result changes the next step

00:22:30-00:24:00 / 1.5 minutes

**Say:** The first trial fails. Llama requests the fallback. A passing result goes to human review.

**Do / discuss:** Point to the failed check between Llama choices. This is the saved P3 MV/LV study; the fixed comparator reaches the same numerical outcome.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/18) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/18)

### Slide 19. Two control settings

00:24:00-00:26:00 / 2 minutes

**Say:** a controls active power. b controls reactive power. Check inverter capacity, voltage and line current.

**Do / discuss:** Explain per unit as a value divided by its base. At RATING_FRACTION=0.80, 100% current denotes the reduced allowance.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/19) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/19)

### Slide 20. A tool is a callable function

00:26:00-00:27:30 / 1.5 minutes

**Say:** Inputs go in. Calculations run. Results come back. L2 calls this Python function directly.

**Do / discuss:** Locate lab.voltage_lab on the next slide. Distinguish a direct Python call from a model-selected request.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/20) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/20)

### Slide 21. L2: run the default case

00:27:30-00:29:30 / 2 minutes

**Say:** Run all of L2. It checks the MPC plan and the saved SAC policy. Read feasible, current_step_J and max_allowed_current_pct.

**Do / discuss:** Set LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Run all of L2; read feasible, max_allowed_current_pct and current_step_J.

Notebook: Run the full L2 cell. Stable ID: classroom-007; slide excerpt: source lines 1-4.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/21) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/21)

### Slide 22. L2: voltage and current plots

00:29:30-00:32:30 / 3 minutes

**Say:** Left: voltages should stay inside the allowed band. Right: current use should stay below 100% of the allowance.

**Do / discuss:** Ask a pair to describe one voltage check and one current check. Use the current run’s outputs.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/22) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/22)

### Slide 23. L2: both default proposals pass

00:32:30-00:34:30 / 2 minutes

**Say:** MPC: 73.62% current use, score J about 0.03110. Saved SAC: 51.68% current use, score J about 0.43643.

**Do / discuss:** Read feasibility before penalty. Reference J: MPC about 0.03110, SAC about 0.43643.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/23) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/23)

### Slide 24. The limit and the calculated result

00:34:30-00:36:00 / 1.5 minutes

**Say:** A rule states the limit. A tool checks the proposal against it. Keep both with the result so the operator can review it.

**Do / discuss:** Keep the P3 value separate from the fresh L2 exercise. Ask which remaining checks the operator must review.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/24) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/24)

### Slide 25. Exercise 1: lower the current allowance

00:36:00-00:40:00 / 4 minutes

**Say:** In L2, change RATING_FRACTION from 0.80 to 0.75. Predict, then rerun. Compare feasible, current use and score J for both methods. Does this check cover the whole MV/LV network?

**Do / discuss:** FOUR MINUTES: predict for 1 minute, edit/run for 2, report for 1. Change only RATING_FRACTION to 0.75; keep LOAD_SCALE=1.0.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/25) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/25)

### Slide 26. Exercise 1: both still pass

00:40:00-00:44:30 / 4.5 minutes

**Say:** A smaller allowance makes the same current a larger percentage. At 0.75: MPC uses 78.53%, SAC 54.85%. Both pass this test.

**Do / discuss:** Debrief: reference current use becomes 78.527895% for MPC and 54.854158% for SAC. Both pass; default coverage is MV only.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/26) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/26)

### Slide 27. L2: reset before continuing

00:44:30-00:46:30 / 2 minutes

**Say:** Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Rerun L2. L3-L5 use a separate saved case called test_01.

**Do / discuss:** Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80, then rerun L2.

Notebook: Run the full L2 cell. Stable ID: classroom-007; slide excerpt: source lines 1-2.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/27) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/27)

### Slide 28. New calculations and saved replies

00:46:30-00:48:30 / 2 minutes

**Say:** Python calculates new results. A saved Llama reply keeps its original inputs. Your changed lab input does not change the saved reply.

**Do / discuss:** Ask which evidence mode applies to L2 and to the coming L3 replies.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/28) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/28)

### Slide 29. L3: inspect saved model choices

00:48:30-00:50:30 / 2 minutes

**Say:** Run L3. Read the case ID, chosen operations and recorded times. This cell displays old replies. It makes no new model call.

**Do / discuss:** Run L3. Read the original test_01 identifier, requested operation and exact public reason.

Notebook: Run the full L3 cell. Stable ID: classroom-010; slide excerpt: source lines 1-2.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/29) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/29)

### Slide 30. Different words can request the same trial

00:50:30-00:52:30 / 2 minutes

**Say:** The notebook groups identical tool requests and settings. A vote chooses what to test next. It does not prove that limits pass.

**Do / discuss:** Ask what evidence is required before accepting the selected trial for review.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/30) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/30)

### Slide 31. L4: check the selected trial

00:52:30-00:54:30 / 2 minutes

**Say:** Run L4 after L3. Python checks the selected trial for its original case. Compare majority voting with the saved LinUCB selector, which learns which trial to test.

**Do / discuss:** Run L4 after L3. Read the table and separate the fixed selection methods from new numerical checks.

Notebook: Run the full L4 cell. Stable ID: classroom-013; slide excerpt: source lines 5-9.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/31) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/31)

### Slide 32. L4: read the new check

00:54:30-00:56:30 / 2 minutes

**Say:** Both selectors choose the same trial and pass the new MV check. new_check_passes is the electrical check. Predicted reward is a learned score.

**Do / discuss:** Read operation, new_check_passes and current_step_J. Reference penalty is about 0.031082.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/32) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/32)

### Slide 33. L5: check model coverage

00:56:30-00:58:30 / 2 minutes

**Say:** Leave RUN_OPENDSS=False. Run L5 and read the table. The default checks the test_01 MPC plan with the MV model.

**Do / discuss:** Keep RUN_OPENDSS=False. Run L5, read optional_mode and the checked model scope.

Notebook: Run the full L5 cell. Stable ID: classroom-016; slide excerpt: source lines 1-4.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/33) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/33)

### Slide 34. A PASS has a scope

00:58:30-01:00:30 / 2 minutes

**Say:** This result covers medium-voltage (MV) phases and currents. A full medium- and low-voltage (MV/LV) request needs the wider check or a HOLD.

**Do / discuss:** Ask which missing coverage prevents an MV-only pass from supporting a full MV/LV request.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/34) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/34)

### Slide 35. Saved voltage case: check SAC first

01:00:30-01:03:00 / 2.5 minutes

**Say:** Llama asks to check SAC. The tool finds a current-limit failure.

**Do / discuss:** Identify VERIFY_SAC_FIRST and the recorded numerical failure. Replay the full source later in L10B.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/35) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/35)

### Slide 36. Saved voltage case: try the MPC fallback

01:03:00-01:05:30 / 2.5 minutes

**Say:** Llama requests the existing MPC plan. The electrical tool checks it.

**Do / discuss:** Identify USE_MPC_PLAN. Contrast Llama’s requested step with the returned numerical evidence.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/36) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/36)

### Slide 37. Saved voltage case: return for review

01:05:30-01:08:00 / 2.5 minutes

**Say:** The checks pass. Human review is still pending. A fixed script gets the same final result.

**Do / discuss:** Partner recap: one fresh calculation, one saved model choice and one unresolved operator review. Next, restoration.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/37) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/37)

<a id="module-restoration"></a>

## 3. Service restoration

### Slide 38. Case 2: restoring service

01:08:00-01:09:00 / 1 minutes

**Say:** Use the six-node teaching network with one faulted branch. Compare total service with service to critical loads.

**Do / discuss:** Locate L6 and keep the faulted branch unavailable.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/38) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/38)

### Slide 39. Two service goals

01:09:00-01:11:00 / 2 minutes

**Say:** One goal gives extra weight to critical loads. The other restores the most total kW. Both use the same network rules.

**Do / discuss:** Ask pairs to state the service goal before choosing the preferred plan.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/39) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/39)

### Slide 40. L6: solve the restoration problem

01:11:00-01:13:00 / 2 minutes

**Say:** Run L6. MILP selects whole loads. A separate search checks its priority score. Read served_kw, critical_kw and MILP_matches_exhaustive_check.

**Do / discuss:** Run L6 with original capacities 40, 60, 80, 100 and 120 kW. Read served_kw, critical_kw and MILP_matches_exhaustive_check.

Notebook: Run the full L6 cell. Stable ID: classroom-018; slide excerpt: source lines 1-5.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/40) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/40)

### Slide 41. L6: read both service plots

01:13:00-01:16:00 / 3 minutes

**Say:** Left: total kW served. Right: critical kW served. Overlapping markers mean the two goals give the same result.

**Do / discuss:** Compare both plots at the same capacity. Ask where the service goals differ.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/41) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/41)

### Slide 42. L6: the tradeoff at 40 kW

01:16:00-01:18:00 / 2 minutes

**Say:** Priority goal: 130 kW total, including 90 kW critical. Most-total-kW goal: 140 kW total, including 30 kW critical.

**Do / discuss:** Compare 130 total/90 critical with 140 total/30 critical kW. The goals share the same capacities and rules.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/42) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/42)

### Slide 43. Restoration checks

01:18:00-01:20:00 / 2 minutes

**Say:** Check source paths, branch capacity, power balance and the fault. A separate search checks the priority score.

**Do / discuss:** Ask which AC, protection and switching-order checks remain outside this formulation.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/43) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/43)

### Slide 44. Exercise 2: increase tie capacity

01:20:00-01:24:00 / 4 minutes

**Say:** Add 180. to CAPACITIES_KW. Keep 40. first. Predict, then rerun L6. Compare total and critical kW at 40 and 180 kW. At which capacity do the two goals give the same result?

**Do / discuss:** FOUR MINUTES: predict for 1 minute, edit/run for 2, report for 1. Append 180. to CAPACITIES_KW and keep 40. first.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/44) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/44)

### Slide 45. Exercise 2: enough capacity removes this tradeoff

01:24:00-01:27:00 / 3 minutes

**Say:** At 180 kW, both goals serve 250 kW total and 90 kW critical. The priority goal helps at some limits. It does not improve every case.

**Do / discuss:** Debrief: at 180 kW both methods serve 250 total and 90 critical kW. Explain why the constrained-case tradeoff disappears.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/45) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/45)

### Slide 46. L7: test an old result after a change

01:27:00-01:29:00 / 2 minutes

**Say:** Restore the original capacity list and rerun L6. Run L7. It changes the first request from 40 kW to 20 kW.

**Do / discuss:** Restore the original capacity list and rerun L6. Run L7; it binds the first 40 kW record.

Notebook: Run the full L7 cell. Stable ID: classroom-021; slide excerpt: source lines 1-3.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/46) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/46)

### Slide 47. L7: the old evidence no longer matches

01:29:00-01:31:00 / 2 minutes

**Say:** Original request: True. Changed request: False. HOLD the old recommendation and request a new solve.

**Do / discuss:** Read original contract True and changed rating False. Request a fresh constrained solve.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/47) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/47)

### Slide 48. New inputs need new evidence

01:31:00-01:33:00 / 2 minutes

**Say:** An outdated check does not tell us whether the new plan works. Solve again, check again and attach the new result to the new request.

**Do / discuss:** Ask which request fields and evidence must be refreshed after a change.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/48) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/48)

### Slide 49. The agent keeps the service goal

01:33:00-01:35:00 / 2 minutes

**Say:** L6 runs Python directly. The operator sets priorities; MILP selects loads. An agent could request the solve and explain its returned tradeoff.

**Do / discuss:** Identify the current Python calculation and the proposed coordinating-agent responsibility.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/49) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/49)

### Slide 50. Restoration model limits

01:35:00-01:36:00 / 1 minutes

**Say:** This graph checks active power, not AC voltage or protection. Selected branches do not specify the order of field switching.

**Do / discuss:** Name a further study needed before a real operating decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/50) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/50)

### Slide 51. Saved restoration case: try another plan

01:36:00-01:38:30 / 2.5 minutes

**Say:** Llama requests a trial that restores more load and passes the current check.

**Do / discuss:** Read SHED_075, served/critical kW and the passing current check. This archive uses a separate feeder catalog; the fraction selects load objects, not percent kW.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/51) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/51)

### Slide 52. Saved restoration case: reject a failed trial

01:38:30-01:41:00 / 2.5 minutes

**Say:** The next trial exceeds the current limit. Keep the previous passing plan.

**Do / discuss:** Keep the previously passed candidate when SHED_065 fails its current check.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/52) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/52)

### Slide 53. Saved restoration case: correct the ranking

01:41:00-01:43:30 / 2.5 minutes

**Say:** Python corrects the ranking and rechecks the lowest-cost passing plan.

**Do / discuss:** Find the wrong language order and numerical guard retaining E03. Contrast this saved feeder case with L6, then move to cyber.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/53) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/53)

<a id="module-cyber"></a>

## 4. Cyber response

### Slide 54. Case 3: suspicious readings

01:43:30-01:44:30 / 1 minutes

**Say:** Use the separate four-bus DC teaching model. Compare the fit to readings with error against known simulation truth.

**Do / discuss:** Locate L8. Explain that the known truth is available for offline teaching comparison.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/54) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/54)

### Slide 55. What the residual measures

01:44:30-01:46:30 / 2 minutes

**Say:** Weighted least squares (WLS) fits the readings. Residual J measures the mismatch. The true state is known in this simulation, not in a live control room.

**Do / discuss:** Define WLS as weighted least squares. Ask what small residual establishes and what it leaves open.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/55) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/55)

### Slide 56. L8: run two data attacks

01:46:30-01:48:30 / 2 minutes

**Say:** Run L8 with the default scales. Compare one biased reading with a coordinated change across readings.

**Do / discuss:** Run the full default L8 cell. The defensive Hc example assumes knowledge of H and access to modeled unprotected channels.

Notebook: Run the full L8 cell. Stable ID: classroom-023; slide excerpt: source lines 1-5.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/56) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/56)

### Slide 57. L8: read both cyber plots

01:48:30-01:51:30 / 3 minutes

**Say:** Left: mismatch J and the alarm threshold. Right: error against simulation truth. A quiet alarm can appear alongside a growing state error.

**Do / discuss:** Follow the same curve across residual and state-error plots.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/57) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/57)

### Slide 58. L8: a coordinated attack escapes the alarm

01:51:30-01:53:30 / 2 minutes

**Say:** At scale 1, one biased reading gives J=277.50 and an alarm. The coordinated attack gives J=3.92, no alarm, and 0.02678 rad of state error.

**Do / discuss:** Compare no residual alarm with nonzero state error at scale one.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/58) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/58)

### Slide 59. Exercise 3: test a small bias

01:53:30-01:57:30 / 4 minutes

**Say:** Add .10 to ATTACK_SCALES. Predict, then rerun L8. At scale 0.10, compare J, the alarm flag and state error. Does no alarm mean the data are correct?

**Do / discuss:** FOUR MINUTES: predict for 1 minute, edit/run for 2, report for 1. Add .10 to ATTACK_SCALES and rerun L8.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/59) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/59)

### Slide 60. Exercise 3: a small bias can miss the threshold

01:57:30-02:00:30 / 3 minutes

**Say:** At scale 0.10, J is about 10.14, below the 15.09 alarm threshold. A quiet alarm alone cannot prove that readings are true.

**Do / discuss:** Debrief: isolated-bias J about 10.143237 is below the 15.086272 threshold. Alarm=False despite nonzero error; coordinated J stays about 3.920222.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/60) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/60)

### Slide 61. L8: reset before recovery

02:00:30-02:01:30 / 1 minutes

**Say:** Restore the original attack scales and rerun L8. L9 uses a separate fixed recovery case.

**Do / discuss:** Restore the original ATTACK_SCALES tuple and rerun L8.

Notebook: Run the full L8 cell. Stable ID: classroom-023; slide excerpt: source lines 1-3.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/61) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/61)

### Slide 62. L9: one fixed recovery case

02:01:30-02:03:30 / 2 minutes

**Say:** Compare the same case with and without readings assumed to be trusted. Your L8 scale change does not change this case.

**Do / discuss:** Locate L9 and note that its fixed fixture does not follow the changed L8 sweep.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/62) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/62)

### Slide 63. Data trust is an assumption

02:03:30-02:05:30 / 2 minutes

**Say:** This example assumes three extra angle readings are trustworthy. Neither WLS nor Llama authenticates them.

**Do / discuss:** Ask who or what would establish the trusted-data premise outside this calculation.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/63) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/63)

### Slide 64. L9: HOLD or PROPOSE

02:05:30-02:07:30 / 2 minutes

**Say:** Run all of L9. Read status first. Then read the proposed injection and the offline violation count.

**Do / discuss:** Run all of L9, including its assertions. Read status, u_pu and offline_actual_violations.

Notebook: Run the full L9 cell. Stable ID: classroom-026; slide excerpt: source lines 1-2.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/64) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/64)

### Slide 65. L9: two outcomes

02:07:30-02:09:30 / 2 minutes

**Say:** Without trusted replacement readings: HOLD. With assumed trusted readings: PROPOSE, u about 0.121694 p.u., zero offline model violations.

**Do / discuss:** Read HOLD without trusted data and PROPOSE with the assumed trusted set. Reference u is about 0.121694 p.u.; offline toy violations are zero.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/65) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/65)

### Slide 66. L9: check the correction

02:09:30-02:11:30 / 2 minutes

**Say:** A quadratic-program (QP) solver finds the smallest allowed injection that meets the branch limits. One flow: predicted 0.17000 p.u., offline actual 0.17046 p.u., limit 0.18000 p.u.

**Do / discuss:** Compare predicted and offline flow checks. These use fixed DC sensitivities, rather than a full AC or dynamic model.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/66) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/66)

### Slide 67. A proposal depends on its assumptions

02:11:30-02:13:30 / 2 minutes

**Say:** Assumed trusted data support the estimate. The solver calculates a correction. The operator still reviews data trust, model coverage and missing checks.

**Do / discuss:** Ask what must happen if the trust premise cannot be established. Retain HOLD.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/67) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/67)

### Slide 68. Saved cyber case: request the allowed tool

02:13:30-02:16:00 / 2.5 minutes

**Say:** Llama selects the supplied recovery tool. Python calculates the correction.

**Do / discuss:** Separate what the task already permits from what Llama chooses and Python computes.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/68) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/68)

### Slide 69. Saved cyber case: keep human review

02:16:00-02:18:30 / 2.5 minutes

**Say:** The model check passes. The operator must still review trust and missing checks.

**Do / discuss:** Partner recap: why are PASS and PROPOSE different from approved action? Then inspect the complete replays.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/69) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/69)

<a id="module-closing"></a>

## 5. Llama replay and operator review

### Slide 70. L10: inspect the five-role workflow

02:18:30-02:21:30 / 3 minutes

**Say:** Run L10 to see every recorded stage and result. The stages share case facts, proposals and check results. The next slides explain their jobs.

**Do / discuss:** Run L10 to inspect the separate archive. The later L11 switch stays False.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/70) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/70)

### Slide 71. L10B: replay the three Llama examples

02:21:30-02:28:00 / 6.5 minutes

**Say:** Set SCENARIO to voltage, restoration and cyber. Rerun for each. These are saved replies and tool results. No new Llama call runs here.

**Do / discuss:** Run L10B for SCENARIO="voltage", then "restoration", then "cyber". Allow about 2 minutes per episode and swap runner/checker roles. Afterward run L11 with RUN_LOCAL_LLAMA=False.

Notebook: Run the full L10B cell. Stable ID: classroom-llama-walkthrough; slide excerpt: source lines 1-5.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/71) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/71)

### Slide 72. L12: practice operator readback

02:28:00-02:33:00 / 5 minutes

**Say:** Leave L11 disabled, then run L12. Check the wrong ID, the matching ID and equipment_dispatch=False.

**Do / discuss:** After L10B and L11, run all of L12. It returns to L4’s selected test_01 voltage trial. Check wrong-ID rejection, simulated acknowledgment and equipment_dispatch=False.

Notebook: Run the full L12 cell. Stable ID: classroom-033; slide excerpt: source lines 9-10.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/72) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/72)

### Slide 73. L12: approval must match the checked scope

02:33:00-02:36:00 / 3 minutes

**Say:** Full MV/LV request: HOLD. The MV teaching request allows a simulated readback. A wrong ID fails. This exercise never sends equipment commands.

**Do / discuss:** Explain the full-scope HOLD and the MV-only simulated readback. These do not complete the pending review of a separate old record.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/73) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/73)

### Slide 74. Our multi-agent design: five roles

02:36:00-02:37:00 / 1 minutes

**Say:** The roles pass structured results to each other. Llama handles planning and refinement; Python runs the other stages. This is a custom, role-based Python workflow. It is not five independent LLMs. One Llama 3.1:8b model is called with the Planning Agent and LLM Optimizer roles. Awareness, simulation and verification run Python. The default notebook displays saved role traces in L10 and saved selected episodes in L10B; it does not execute a new multi-agent LLM run. The handoff is structured case facts, candidate IDs, tool results and checks, not an invented agent conversation. src/proposal_workflow.py defines CORE_STAGES, run_proposal_case, evaluate and the ranking guard. A final independent recheck precedes MODEL_RECOMMEND. Human acknowledgment remains separate and pending. Hash checks detect changed records but do not authenticate telemetry.

**Do / discuss:** Follow the diagram, then identify the tool result and remaining operator decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/74) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/74)

### Slide 75. Five roles in the voltage case

02:37:00-02:41:00 / 4 minutes

**Say:** Llama asks for less reactive power, then more solar output. Python checks each new trial. This is a custom, role-based Python workflow. It is not five independent LLMs. One Llama 3.1:8b model is called with the Planning Agent and LLM Optimizer roles. Awareness, simulation and verification run Python. The default notebook displays saved role traces in L10 and saved selected episodes in L10B; it does not execute a new multi-agent LLM run. The handoff is structured case facts, candidate IDs, tool results and checks, not an invented agent conversation. src/proposal_workflow.py defines CORE_STAGES, run_proposal_case, evaluate and the ranking guard. A final independent recheck precedes MODEL_RECOMMEND. Human acknowledgment remains separate and pending. Hash checks detect changed records but do not authenticate telemetry. In this L10 lindistflow3 record, the optimizer asks for RELAX_Q_10_PERCENT then INCREASE_PV_0025. Python recalculates each proposal and the verification stage checks it. The selected final recheck uses a=0.3394386941 and b=0.0276310594, with 50.75344954 percent allowed-current use and no recorded violations. The scope is MV phases only with ideal LV aggregation. Do not substitute the P3 99.604410 percent result or L2 MPC score. These are different experiments.

**Do / discuss:** Follow the diagram, then identify the tool result and remaining operator decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/75) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/75)

### Slide 76. Five roles in the restoration case

02:41:00-02:45:00 / 4 minutes

**Say:** The goal stays fixed. A failed trial cannot enter the final ranking, and Python corrects a wrong cost order. This is a custom, role-based Python workflow. It is not five independent LLMs. One Llama 3.1:8b model is called with the Planning Agent and LLM Optimizer roles. Awareness, simulation and verification run Python. The default notebook displays saved role traces in L10 and saved selected episodes in L10B; it does not execute a new multi-agent LLM run. The handoff is structured case facts, candidate IDs, tool results and checks, not an invented agent conversation. src/proposal_workflow.py defines CORE_STAGES, run_proposal_case, evaluate and the ranking guard. A final independent recheck precedes MODEL_RECOMMEND. Human acknowledgment remains separate and pending. Hash checks detect changed records but do not authenticate telemetry. The L10 lindistflow3 restoration record uses a feeder bypass catalog. SHED_075 returns 1843.61355 kW served and 474.03975 critical kW at 91.86721465 percent allowed-current use. SHED_065 then fails at 111.009413 percent. Llama ranks E02 before E03 even though E03 has the smaller cost. The numerical guard selects E03, then records the final recheck as E05. Switching sequence and broader physical operation are not established.

**Do / discuss:** Follow the diagram, then identify the tool result and remaining operator decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/76) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/76)

### Slide 77. Five roles in the cyber case

02:45:00-02:49:00 / 4 minutes

**Say:** The workflow keeps the trust assumption visible. It cannot create trusted data from a convincing answer. This is a custom, role-based Python workflow. It is not five independent LLMs. One Llama 3.1:8b model is called with the Planning Agent and LLM Optimizer roles. Awareness, simulation and verification run Python. The default notebook displays saved role traces in L10 and saved selected episodes in L10B; it does not execute a new multi-agent LLM run. The handoff is structured case facts, candidate IDs, tool results and checks, not an invented agent conversation. src/proposal_workflow.py defines CORE_STAGES, run_proposal_case, evaluate and the ranking guard. A final independent recheck precedes MODEL_RECOMMEND. Human acknowledgment remains separate and pending. Hash checks detect changed records but do not authenticate telemetry. Awareness preserves the declared measurement-trust condition. Planning requests the initial candidates; Python runs the estimator and constrained-response tools. The optimizer requests EXTRA_MARGIN_001 and TRUSTED_QP. The selected final recheck uses TRUSTED_QP with u=0.1216936673 per unit and predicted flow12=0.17 per unit against a 0.18 limit. The model checks a four-bus DC fixture with three protected angles assumed trustworthy. No stage authenticates those channels, and offline truth is not fed to Llama.

**Do / discuss:** Follow the diagram, then identify the tool result and remaining operator decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/77) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/77)

### Slide 78. The operator reviews one evidence packet

02:49:00-02:53:00 / 4 minutes

**Say:** Review the inputs, proposal, worst margins and missing checks. Request another study, reject the proposal or accept it for the next authorized step. Proposed control-room use. The operator reviews the case snapshot, data quality, limits, selected proposal and missing studies. Ask for another study, reject it or accept it for a defined next step. L12 practices ID-bound readback only and never operates equipment.

**Do / discuss:** Follow the diagram, then identify the tool result and remaining operator decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/78) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/78)

### Slide 79. What the evidence shows

02:53:00-02:57:00 / 4 minutes

**Say:** In L10, five paired final costs tied; one Llama route was worse. Start with past cases and read-only use. Measure benefit against the same tools in a fixed script. The six matched fixed-versus-Llama runs in proposal_complete_workflow.json have five tied final costs and one worse Llama voltage result. Recorded model calls add elapsed time. This demonstrates traceable coordination, not better power-flow solvers or general efficiency. Test any proposed benefit against the same tools and budgets. A control-room pilot starts with archived cases, then read-only shadow studies and a limited reviewed scope.

**Do / discuss:** Follow the diagram, then identify the tool result and remaining operator decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/79) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/79)

### Slide 80. Questions and your next lab run

02:57:00-03:00:00 / 3 minutes

**Say:** Choose one case. Change one input, rerun and save the result. Explain the agent choice, tool result, check and operator decision. Close by connecting the full loop: a goal, an allowed agent choice, a tool result, a check and a human decision. Ask each learner to name one case and one changed input they can repeat after the session. Save the notebook. Use the source guide for complete references, not as another required activity.

**Do / discuss:** Invite questions. Ask learners to save one changed input, result and next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/80) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/80)

## Reading and source credits

Original source figures and our grid adaptations remain labeled on the slides. The lab uses custom Python, not the Stanford frameworks. Complete numerical sources, figure credits and evidence limits are in the [Teaching and Source Guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Full_Reading_Guide.html).

- Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026. [Read full source](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf).
- Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023. [Read full source](https://aclanthology.org/2023.findings-emnlp.157/).
- Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025. [Read full source](https://aclanthology.org/2025.acl-long.1323/).
- Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19. [Read full source](https://www.anthropic.com/research/building-effective-agents).
