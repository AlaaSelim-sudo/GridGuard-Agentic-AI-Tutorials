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

**Say:** Today we will use one notebook for three operator studies. We will connect Stanford ideas to the cases, run calculations, change inputs, inspect saved Llama choices and explain what a person must still review.

**Do / discuss:** Have slides, Classroom Labs and the Participant Lab Guide ready. Pair participants. Allow breaks outside the 180 teaching minutes.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/1)

### Slide 2. What is agentic AI?

00:00:30-00:01:30 / 1 minutes

**Say:** An LLM agent works toward a goal by choosing a permitted tool, reading its result and choosing the next step. The application keeps the tool rules fixed. The numerical tool supplies the physical evidence.

**Do / discuss:** Ask which part supplies a physical result. Expected: the numerical tool. Ordinary programs can also contain loops.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/2) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/2)

### Slide 3. Stanford: tool calls become a workflow

00:01:30-00:02:30 / 1 minutes

**Say:** These original Stanford panels distinguish a model-selected function call from a workflow connecting several steps. We will inspect the requests and returned results, so the coordinating role is visible.

**Do / discuss:** Point to the original function-calling and workflow panels. Follow the source link for lecture p.2.

[Read the Stanford lecture, p.2](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=2)

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/3) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/3)

### Slide 4. Stanford example: check before you write

00:02:30-00:03:45 / 1.25 minutes

**Say:** WikiChat separates retrieval, claim checking and writing. We borrow the checking habit for grid studies: the summary should follow the evidence returned by a tool.

**Do / discuss:** Point to fact checking before Draft. Ask what numerical evidence a grid proposal would need.

[Read the Stanford lecture, p.19](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=19)

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/4) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/4)

### Slide 5. Voltage: a proposal needs a numerical check

00:03:45-00:05:15 / 1.5 minutes

**Say:** In L2, Python calculates a proposal and checks it. This reference plan uses about 73.62 percent of allowed current. Also review voltage and model coverage. A separate saved Llama episode later shows tool selection.

**Do / discuss:** Preview L2 now; run it after setup, L0 and L1. The bar is a reference result, separate from the P3 replay.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/5) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/5)

### Slide 6. Stanford example: tools need clear rules

00:05:15-00:06:30 / 1.25 minutes

**Say:** Genie Worksheets emphasizes a complete task description, beyond listing functions. Our Python rules state the inputs, limits and stop conditions. A model explanation cannot silently change them.

**Do / discuss:** Ask which task rules must remain fixed when comparing restoration plans.

[Read the Stanford lecture, p.40](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=40)

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/6) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/6)

### Slide 7. Restoration: the service goal shapes the plan

00:06:30-00:08:00 / 1.5 minutes

**Say:** The service goal changes the preferred restoration plan. Priority weighting gives 130 total kW with 90 critical kW. Maximizing total gives 140 total kW with only 30 critical kW. The network and capacities stay the same.

**Do / discuss:** Compare the cyan critical-service segments. The varied tie is 40 kW, another tie stays at 100 kW, and totals include upstream load.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/7) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/7)

### Slide 8. Stanford: language and decision checks

00:08:00-00:09:15 / 1.25 minutes

**Say:** Stanford separates language understanding from a solver that checks a formal decision model. Our grid adaptation separates Llama coordination, Python numerical checks and operator review. The clinical-source example supplies an analogy.

**Do / discuss:** Explain SMT briefly as logical constraints and MaxSAT as supporting decision-changing conditions. Our lab uses numerical checks and no SMT guarantee.

[Read the Stanford lecture, p.53](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=53)

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/8) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/8)

### Slide 9. Cyber: a clear answer still needs evidence

00:09:15-00:10:45 / 1.5 minutes

**Say:** L8 asks whether readings fit the model. A small mismatch can hide a wrong estimate. L9 asks a separate recovery question that requires an explicit trust premise and passing numerical checks.

**Do / discuss:** Ask why a clear explanation cannot establish sensor trust.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/9) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/9)

### Slide 10. Ask four questions about a study result

00:10:45-00:12:00 / 1.25 minutes

**Say:** Use four review questions: which result supports the claim, which assumptions were used, were the rules kept, and what happens next? These questions apply to all three labs.

**Do / discuss:** Collect one example of a missing check, then start Colab setup.

[Read the Stanford lecture, p.52](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=52)

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/10) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/10)

### Slide 11. One notebook covers all three cases

00:12:00-00:13:00 / 1 minutes

**Say:** Only Classroom Labs is required today. Keep that notebook beside the slides. It contains all three cases and the L10B replay; the graph and trace notebooks are companion resources.

**Do / discuss:** Open Classroom Labs and save a copy. Keep the same notebook open for all three cases.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/11) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/11)

### Slide 12. Get ready in four small steps

00:13:00-00:14:30 / 1.5 minutes

**Say:** Colab supplies a temporary computer. Save your copy, connect a CPU runtime and run setup until Ready. The default route needs no GPU, API key or model download.

**Do / discuss:** Connect a CPU runtime and run the first setup cell. Wait for Ready. After a reset, rerun setup and the required earlier cells.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/12) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/12)

### Slide 13. Run a cell, then read what it returns

00:14:30-00:16:00 / 1.5 minutes

**Say:** Find the input, play button and returned output. Editing a number does not change an old output until the whole cell runs again. Follow the named L lesson cells in order.

**Do / discuss:** Locate input, play button and output. Run the complete named L cell; slide code is often an excerpt.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/13) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/13)

### Slide 14. Run L0: choose the classroom route

00:16:00-00:17:00 / 1 minutes

**Say:** L0 selects the classroom route. Keep both switches False. Numerical calculations run now, the controller uses saved weights, and the model replies are recorded. The data-file assertion checks the working folder.

**Do / discuss:** Run L0 with RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. If the data check fails, rerun setup.

Notebook: Run the full L0 cell. Stable ID: classroom-002; slide excerpt: source lines 11-14.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/14) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/14)

### Slide 15. Run L1: does the evidence still match?

00:17:00-00:19:00 / 2 minutes

**Say:** The unchanged request and command match the evidence. Changing either breaks that match. A fresh study is needed for the new request; stale evidence alone does not prove the changed case infeasible.

**Do / discuss:** Run L1. Read binding_pass as True, False, False. Ask what changed in each row.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/15) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/15)

<a id="module-voltage"></a>

## 2. Voltage support

### Slide 16. Voltage: open L2

00:19:00-00:21:00 / 2 minutes

**Say:** This synthetic feeder is our voltage teaching network. We will compare two control proposals, check modeled voltage and current limits, then compare their penalty scores. The default model has limited coverage.

**Do / discuss:** Locate L2 and identify this synthetic teaching feeder.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/16) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/16)

### Slide 17. MPC plans; SAC proposes

00:21:00-00:22:30 / 1.5 minutes

**Say:** MPC plans from a model and a short forecast. SAC proposes settings using saved learned weights. Both are tools inside the wider workflow, and the same numerical checks must test their proposals.

**Do / discuss:** Define MPC as model predictive control and SAC as Soft Actor–Critic. SAC uses saved weights without training again.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/17) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/17)

### Slide 18. A real agent changes its next step

00:22:30-00:24:00 / 1.5 minutes

**Say:** This separate saved P3 example makes the agentic sequence visible. A SAC check fails at about 111.97 percent of the allowance. Llama requests the MPC fallback, whose current check passes at about 99.60 percent. Human review remains pending.

**Do / discuss:** Point to the failed check between Llama choices. This is the saved P3 MV/LV study; the fixed comparator reaches the same numerical outcome.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/18) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/18)

### Slide 19. Control settings and limits

00:24:00-00:26:00 / 2 minutes

**Say:** Active and reactive settings share the inverter power limit. Network voltage and current must also pass. Here, 100 percent current means the configured allowance, which is a fraction of nominal rating.

**Do / discuss:** Explain per unit as a value divided by its base. At RATING_FRACTION=0.80, 100% current denotes the reduced allowance.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/19) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/19)

### Slide 20. A tool is a Python function in this lab

00:26:00-00:27:30 / 1.5 minutes

**Say:** A tool has defined inputs and returned evidence. Your L2 cell calls the voltage function directly. In the separate agent study, Python validates Llama’s named choice before calling an allowed function.

**Do / discuss:** Locate lab.voltage_lab on the next slide. Distinguish a direct Python call from a model-selected request.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/20) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/20)

### Slide 21. Run L2 with the default inputs

00:27:30-00:29:30 / 2 minutes

**Say:** Run L2 at the defaults. It calculates an MPC plan and a proposal from the saved SAC policy, then checks both. Read feasibility and allowed-current use before comparing the current-step penalty.

**Do / discuss:** Set LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Run all of L2; read feasible, max_allowed_current_pct and current_step_J.

Notebook: Run the full L2 cell. Stable ID: classroom-007; slide excerpt: source lines 1-4.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/21) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/21)

### Slide 22. Read the voltage and current plots

00:29:30-00:32:30 / 3 minutes

**Say:** Read both plots together. The voltage curves are sorted separately, so equal ranks need not be the same location. Compare current use against the 100 percent line, using the output from the current run.

**Do / discuss:** Ask a pair to describe one voltage check and one current check. Use the current run’s outputs.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/22) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/22)

### Slide 23. Check limits before comparing scores

00:32:30-00:34:30 / 2 minutes

**Say:** Both reference proposals pass. MPC uses about 73.62 percent of the current allowance; SAC uses about 51.68 percent. MPC has the lower penalty here. This single case does not establish a universal controller advantage.

**Do / discuss:** Read feasibility before penalty. Reference J: MPC about 0.03110, SAC about 0.43643.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/23) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/23)

### Slide 24. A rule and a tool result answer different questions

00:34:30-00:36:00 / 1.5 minutes

**Say:** A document can state a current limit, while a numerical tool calculates a proposal’s current. Keep the rule, result and remaining checks together. This displayed P3 number is separate from your fresh L2 result.

**Do / discuss:** Keep the P3 value separate from the fresh L2 exercise. Ask which remaining checks the operator must review.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/24) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/24)

### Slide 25. Exercise 1: tighten the current allowance

00:36:00-00:40:00 / 4 minutes

**Say:** Predict the effect of tightening the current allowance. Change only that input, rerun L2 and report each method’s feasibility, percentage and penalty. Explain what the default model covers.

**Do / discuss:** FOUR MINUTES: predict for 1 minute, edit/run for 2, report for 1. Change only RATING_FRACTION to 0.75; keep LOAD_SCALE=1.0.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/25) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/25)

### Slide 26. Change one number and explain the difference

00:40:00-00:44:30 / 4.5 minutes

**Say:** The same current becomes a larger share of a smaller allowance, so the percentage rises. Both proposals still pass this particular exercise. Explain the returned result and its scope rather than expecting a rejection.

**Do / discuss:** Debrief: reference current use becomes 78.527895% for MPC and 54.854158% for SAC. Both pass; default coverage is MV only.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/26) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/26)

### Slide 27. Reset L2 before reading old model choices

00:44:30-00:46:30 / 2 minutes

**Say:** Restore the defaults before the saved-response lessons. L3 through L5 use the original test_01 archive. Your edited L2 run does not rewrite that historical case.

**Do / discuss:** Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80, then rerun L2.

Notebook: Run the full L2 cell. Stable ID: classroom-007; slide excerpt: source lines 1-2.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/27) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/27)

### Slide 28. What runs now and what was recorded

00:46:30-00:48:30 / 2 minutes

**Say:** A fresh calculation runs now. A replay displays an old reply with its original inputs. The closing control-room pilot is a teaching proposal. Keep those evidence labels visible.

**Do / discuss:** Ask which evidence mode applies to L2 and to the coming L3 replies.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/28) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/28)

### Slide 29. L3 opens a separate recorded case

00:48:30-00:50:30 / 2 minutes

**Say:** L3 opens saved responses for test_01. Read the requested operation, public reason and recorded time. Displaying these records makes no new language-model call.

**Do / discuss:** Run L3. Read the original test_01 identifier, requested operation and exact public reason.

Notebook: Run the full L3 cell. Stable ID: classroom-010; slide excerpt: source lines 1-2.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/29) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/29)

### Slide 30. What did the models choose?

00:50:30-00:52:30 / 2 minutes

**Say:** Different wording can request the same numerical trial. Two recorded replies agree on reactive-power relaxation. Agreement selects a trial; a numerical check still has to evaluate it.

**Do / discuss:** Ask what evidence is required before accepting the selected trial for review.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/30) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/30)

### Slide 31. Run L4: check the old choice again

00:52:30-00:54:30 / 2 minutes

**Say:** L4 checks the selected archived trial again. It compares majority selection with a saved LinUCB selector. The engineering result comes from the new check, while the selection models remain fixed.

**Do / discuss:** Run L4 after L3. Read the table and separate the fixed selection methods from new numerical checks.

Notebook: Run the full L4 cell. Stable ID: classroom-013; slide excerpt: source lines 5-9.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/31) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/31)

### Slide 32. Separate the old choice from the new check

00:54:30-00:56:30 / 2 minutes

**Say:** Both selectors choose the same relaxation trial in this reference case, and its fresh check passes. A learned selection score and physical feasibility answer different questions.

**Do / discuss:** Read operation, new_check_passes and current_step_J. Reference penalty is about 0.031082.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/32) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/32)

### Slide 33. Run L5: check what the model covers

00:56:30-00:58:30 / 2 minutes

**Say:** L5 asks what the original plan’s model covers. It audits the archived test_01 MV-MPC plan, rather than L4’s selected relaxation trial. Keep OpenDSS disabled on the default route.

**Do / discuss:** Keep RUN_OPENDSS=False. Run L5, read optional_mode and the checked model scope.

Notebook: Run the full L5 cell. Stable ID: classroom-016; slide excerpt: source lines 1-4.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/33) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/33)

### Slide 34. A PASS covers only the model checked

00:58:30-01:00:30 / 2 minutes

**Say:** A passing result applies to the checked model and limits. An MV-only pass leaves missing evidence for a request requiring both MV and LV. Obtain the wider check or keep HOLD for that request.

**Do / discuss:** Ask which missing coverage prevents an MV-only pass from supporting a full MV/LV request.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/34) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/34)

### Slide 35. Voltage: Llama asks to check the saved controller

01:00:30-01:03:00 / 2.5 minutes

**Say:** Return to the separate saved P3 study. Llama requests the missing SAC check. OpenDSS reports two current violations and about 111.97 percent of allowed current. That tool result supports considering another permitted step.

**Do / discuss:** Identify VERIFY_SAC_FIRST and the recorded numerical failure. Replay the full source later in L10B.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/35) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/35)

### Slide 36. Voltage: Llama chooses the existing fallback plan

01:03:00-01:05:30 / 2.5 minutes

**Say:** An MPC fallback already exists in the saved case. Llama selects it for a check; Python and OpenDSS supply the passing result. The language model coordinates the request rather than solving the power flow.

**Do / discuss:** Identify USE_MPC_PLAN. Contrast Llama’s requested step with the returned numerical evidence.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/36) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/36)

### Slide 37. Voltage: the checks pass and human review remains

01:05:30-01:08:00 / 2.5 minutes

**Say:** The numerical checks pass, while acknowledgment remains pending. The fixed workflow reached the same numerical result. Describe the coordination role and the missing human decision without claiming a numerical benefit from the model.

**Do / discuss:** Partner recap: one fresh calculation, one saved model choice and one unresolved operator review. Next, restoration.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/37) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/37)

<a id="module-restoration"></a>

## 3. Service restoration

### Slide 38. Restoration: open L6

01:08:00-01:09:00 / 1 minutes

**Say:** Restoration uses a separate six-node teaching graph. Keep the faulted branch unavailable. We will compare service goals, vary the tie capacity and inspect whether the evidence still matches its request.

**Do / discuss:** Locate L6 and keep the faulted branch unavailable.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/38) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/38)

### Slide 39. Choose the service goal before the plan

01:09:00-01:11:00 / 2 minutes

**Say:** The two plans follow different service goals under the same constraints. More total kW can come with less critical service. State the requested goal before deciding which plan is preferable.

**Do / discuss:** Ask pairs to state the service goal before choosing the preferred plan.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/39) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/39)

### Slide 40. Run L6: change the tie capacity

01:11:00-01:13:00 / 2 minutes

**Say:** L6 sweeps the tie capacity. The mixed-integer solver chooses whole loads under the graph rules. A separate exhaustive search checks the priority score on this small case.

**Do / discuss:** Run L6 with original capacities 40, 60, 80, 100 and 120 kW. Read served_kw, critical_kw and MILP_matches_exhaustive_check.

Notebook: Run the full L6 cell. Stable ID: classroom-018; slide excerpt: source lines 1-5.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/40) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/40)

### Slide 41. Read both service plots

01:13:00-01:16:00 / 3 minutes

**Say:** Read total service on the left and critical service on the right. Coincident points mean the goals give the same result at that capacity. Compare both measures before explaining the tradeoff.

**Do / discuss:** Compare both plots at the same capacity. Ask where the service goals differ.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/41) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/41)

### Slide 42. The tradeoff at a 40 kW tie limit

01:16:00-01:18:00 / 2 minutes

**Say:** At the 40 kW varied-tie limit, priority weighting gives 130 total kW and 90 critical kW. The maximum-kW goal gives 140 total kW and 30 critical kW. Both use the same network and rules.

**Do / discuss:** Compare 130 total/90 critical with 140 total/30 critical kW. The goals share the same capacities and rules.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/42) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/42)

### Slide 43. How Python checks the plan

01:18:00-01:20:00 / 2 minutes

**Say:** Python checks source connection, capacities, power balance, the excluded fault and energized loops. Exhaustive enumeration checks the priority score. These graph checks leave AC physics and field switching order open.

**Do / discuss:** Ask which AC, protection and switching-order checks remain outside this formulation.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/43) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/43)

### Slide 44. Exercise 2: add more tie capacity

01:20:00-01:24:00 / 4 minutes

**Say:** Predict whether more tie capacity removes the tradeoff. Append 180 kW, keep 40 kW first and rerun L6. Compare total and critical service at those two capacities.

**Do / discuss:** FOUR MINUTES: predict for 1 minute, edit/run for 2, report for 1. Append 180. to CAPACITIES_KW and keep 40. first.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/44) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/44)

### Slide 45. Debrief: the tradeoff disappears here

01:24:00-01:27:00 / 3 minutes

**Say:** At 180 kW both goals give 250 total kW and 90 critical kW in this example. Priority weighting matters when constraints create a tradeoff; it does not improve every instance.

**Do / discuss:** Debrief: at 180 kW both methods serve 250 total and 90 critical kW. Explain why the constrained-case tradeoff disappears.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/45) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/45)

### Slide 46. Reset the capacity list, then run L7

01:27:00-01:29:00 / 2 minutes

**Say:** Restore the original capacity list before L7. The next cell binds the first 40 kW result to its request, then changes that request while keeping the old evidence.

**Do / discuss:** Restore the original capacity list and rerun L6. Run L7; it binds the first 40 kW record.

Notebook: Run the full L7 cell. Stable ID: classroom-021; slide excerpt: source lines 1-3.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/46) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/46)

### Slide 47. Read the evidence-match test

01:29:00-01:31:00 / 2 minutes

**Say:** The original request matches. The changed request no longer matches the old evidence. The required next step is a fresh constrained study, rather than reusing an unsupported recommendation.

**Do / discuss:** Read original contract True and changed rating False. Request a fresh constrained solve.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/47) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/47)

### Slide 48. Changed inputs need a new check

01:31:00-01:33:00 / 2 minutes

**Say:** When inputs change, update the request, solve and check again, then bind the new evidence. An old correct calculation can still be irrelevant to a changed case.

**Do / discuss:** Ask which request fields and evidence must be refreshed after a change.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/48) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/48)

### Slide 49. Proposed agent role: keep the service goal

01:33:00-01:35:00 / 2 minutes

**Say:** The present cell runs Python: the operator supplies the service goal, and the optimizer chooses loads. A coordinating agent would request that study and explain the returned tradeoff while preserving the goal.

**Do / discuss:** Identify the current Python calculation and the proposed coordinating-agent responsibility.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/49) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/49)

### Slide 50. What this model does not check

01:35:00-01:36:00 / 1 minutes

**Say:** This transport model does not check AC voltage, reactive power or protection. An energized graph also does not supply a safe field switching sequence. Keep those missing checks explicit.

**Do / discuss:** Name a further study needed before a real operating decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/50) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/50)

### Slide 51. Restoration: Llama chooses a useful new trial

01:36:00-01:38:30 / 2.5 minutes

**Say:** In this separate recorded feeder study, Llama requests SHED_075. The tool returns about 1843.614 total kW and 474.040 critical kW, with a passing current check. The result establishes what that trial achieved.

**Do / discuss:** Read SHED_075, served/critical kW and the passing current check. This archive uses a separate feeder catalog; the fraction selects load objects, not percent kW.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/51) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/51)

### Slide 52. Restoration: the next trial crosses the current limit

01:38:30-01:41:00 / 2.5 minutes

**Say:** Llama requests SHED_065 next. The returned tie loading is about 111.009 percent, so the check rejects the trial. More served load cannot override a required current limit.

**Do / discuss:** Keep the previously passed candidate when SHED_065 fails its current check.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/52) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/52)

### Slide 53. Restoration: catch Llama’s wrong ranking

01:41:00-01:43:30 / 2.5 minutes

**Say:** The final language ranking is wrong. Python compares the numerical costs, retains the lower-cost passed candidate E03 and rechecks it. A fluent explanation needs a guard grounded in the actual results.

**Do / discuss:** Find the wrong language order and numerical guard retaining E03. Contrast this saved feeder case with L6, then move to cyber.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/53) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/53)

<a id="module-cyber"></a>

## 4. Cyber response

### Slide 54. Cyber: open L8

01:43:30-01:44:30 / 1 minutes

**Say:** The cyber lab uses a separate four-bus DC fixture. We compare model fit with error against known simulation truth. That teaching truth is an offline comparison, not an extra authenticated operator measurement.

**Do / discuss:** Locate L8. Explain that the known truth is available for offline teaching comparison.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/54) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/54)

### Slide 55. Best fit and true state are different

01:44:30-01:46:30 / 2 minutes

**Say:** Weighted least squares finds the state that best fits the readings, weighting more precise measurements more strongly. A small residual measures consistency with the model; it does not establish authentic readings.

**Do / discuss:** Define WLS as weighted least squares. Ask what small residual establishes and what it leaves open.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/55) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/55)

### Slide 56. Run L8: compare two data attacks

01:46:30-01:48:30 / 2 minutes

**Say:** L8 compares an isolated biased reading with a coordinated shift fitting a different modeled state. This declared defensive fixture makes a detector limitation visible under stated model and access assumptions.

**Do / discuss:** Run the full default L8 cell. The defensive Hc example assumes knowledge of H and access to modeled unprotected channels.

Notebook: Run the full L8 cell. Stable ID: classroom-023; slide excerpt: source lines 1-5.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/56) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/56)

### Slide 57. Read both cyber plots

01:48:30-01:51:30 / 3 minutes

**Say:** Follow each curve across both plots. Residual is on the left, while error against known teaching truth is on the right. The residual alarm can remain quiet while estimation error grows.

**Do / discuss:** Follow the same curve across residual and state-error plots.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/57) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/57)

### Slide 58. At scale 1, the alarm misses a state error

01:51:30-01:53:30 / 2 minutes

**Say:** The coordinated shift changes the estimated state while preserving the residual pattern of this linear fixture. At scale one the residual stays about 3.92 without an alarm, while state error is nonzero.

**Do / discuss:** Compare no residual alarm with nonzero state error at scale one.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/58) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/58)

### Slide 59. Exercise 3: add a small isolated bias

01:53:30-01:57:30 / 4 minutes

**Say:** Predict whether a small isolated bias triggers the alarm. Add scale 0.10, rerun L8, and read the alarm alongside the state error. Use both results to explain what no alarm means.

**Do / discuss:** FOUR MINUTES: predict for 1 minute, edit/run for 2, report for 1. Add .10 to ATTACK_SCALES and rerun L8.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/59) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/59)

### Slide 60. Debrief: no alarm does not prove truth

01:57:30-02:00:30 / 3 minutes

**Say:** The small isolated bias also stays below the chosen threshold. A quiet alarm alone cannot establish truth. Keep the claim tied to this fixture and its stated assumptions.

**Do / discuss:** Debrief: isolated-bias J about 10.143237 is below the 15.086272 threshold. Alarm=False despite nonzero error; coordinated J stays about 3.920222.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/60) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/60)

### Slide 61. Reset L8 before the recovery example

02:00:30-02:01:30 / 1 minutes

**Say:** Restore the default scale list and rerun L8. L9 uses a separate fixed recovery fixture; its correction does not follow the scale you just added.

**Do / discuss:** Restore the original ATTACK_SCALES tuple and rerun L8.

Notebook: Run the full L8 cell. Stable ID: classroom-023; slide excerpt: source lines 1-3.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/61) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/61)

### Slide 62. L9 uses a fixed recovery case

02:01:30-02:03:30 / 2 minutes

**Say:** L9 compares a fixed recovery case with and without additional readings assumed trustworthy. We will separate that premise from the returned numerical result.

**Do / discuss:** Locate L9 and note that its fixed fixture does not follow the changed L8 sweep.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/62) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/62)

### Slide 63. Trusted readings are an assumption

02:03:30-02:05:30 / 2 minutes

**Say:** The three trusted angle readings are explicitly assumed. They supply three independent measurements for the three-angle model, with no residual redundancy left. This numerical calculation does not authenticate them.

**Do / discuss:** Ask who or what would establish the trusted-data premise outside this calculation.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/63) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/63)

### Slide 64. Run L9: compare HOLD and PROPOSE

02:05:30-02:07:30 / 2 minutes

**Say:** Run both L9 calls. Without trusted replacement data the result is HOLD. With the set assumed trusted and numerical checks passing, the result is PROPOSE. A proposal still needs review.

**Do / discuss:** Run all of L9, including its assertions. Read status, u_pu and offline_actual_violations.

Notebook: Run the full L9 cell. Stable ID: classroom-026; slide excerpt: source lines 1-2.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/64) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/64)

### Slide 65. Read the two decision states

02:07:30-02:09:30 / 2 minutes

**Say:** The reference proposed injection is about 0.121694 per unit, with zero recorded offline model violations. This depends on the fixture and trust premise and does not authorize equipment dispatch.

**Do / discuss:** Read HOLD without trusted data and PROPOSE with the assumed trusted set. Reference u is about 0.121694 p.u.; offline toy violations are zero.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/65) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/65)

### Slide 66. Check the numerical correction

02:09:30-02:11:30 / 2 minutes

**Say:** The optimizer seeks the least-effort modeled correction under branch limits and a margin. Predicted flow12 is 0.17000 per unit; the offline truth check gives about 0.17046, below the 0.18000 rating.

**Do / discuss:** Compare predicted and offline flow checks. These use fixed DC sensitivities, rather than a full AC or dynamic model.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/66) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/66)

### Slide 67. What makes the recovery possible?

02:11:30-02:13:30 / 2 minutes

**Say:** The recovery depends on assumed trusted information and a constrained correction. Preserve both in the evidence packet so the operator can review the conditions supporting the proposal.

**Do / discuss:** Ask what must happen if the trust premise cannot be established. Retain HOLD.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/67) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/67)

### Slide 68. Cyber: Llama selects the tool already allowed

02:13:30-02:16:00 / 2.5 minutes

**Say:** In this separate saved cyber episode, the task already permits WLS_TRUSTED_REDISPATCH. Llama selects it and Python computes the correction. The model has not discovered or authenticated trusted sensors.

**Do / discuss:** Separate what the task already permits from what Llama chooses and Python computes.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/68) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/68)

### Slide 69. Cyber: a passing calculation still needs review

02:16:00-02:18:30 / 2.5 minutes

**Say:** The numerical calculation passes, while the overall result remains REVIEW and acknowledgment remains pending. Keep the trust premise and missing operating checks visible. The fixed comparison reaches the same numerical outcome.

**Do / discuss:** Partner recap: why are PASS and PROPOSE different from approved action? Then inspect the complete replays.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/69) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/69)

<a id="module-closing"></a>

## 5. Llama replay and operator review

### Slide 70. Run L10 before the Llama walkthrough

02:18:30-02:21:30 / 3 minutes

**Say:** L10 opens a separate archived five-stage study. Read it for context, then continue to L10B for the readable saved Llama episodes. These records differ from your current classroom edits.

**Do / discuss:** Run L10 to inspect the separate archive. The later L11 switch stays False.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/70) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/70)

### Slide 71. Run L10B: watch Llama choose a tool

02:21:30-02:28:00 / 6.5 minutes

**Say:** Inspect the three saved episodes yourselves. Identify the supplied facts, allowed choice, exact public reason, returned tool result and next step. The replay makes no new model request or electrical solve.

**Do / discuss:** Run L10B for SCENARIO="voltage", then "restoration", then "cyber". Allow about 2 minutes per episode and swap runner/checker roles. Afterward run L11 with RUN_LOCAL_LLAMA=False.

Notebook: Run the full L10B cell. Stable ID: classroom-llama-walkthrough; slide excerpt: source lines 1-5.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/71) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/71)

### Slide 72. Finish L12: practice the readback

02:28:00-02:33:00 / 5 minutes

**Say:** L12 practices repeating the same recommendation ID and conditions. A wrong ID is rejected. The correct simulated acknowledgment still grants no equipment authority and does not resolve a scope gap.

**Do / discuss:** After L10B and L11, run all of L12. It returns to L4’s selected test_01 voltage trial. Check wrong-ID rejection, simulated acknowledgment and equipment_dispatch=False.

Notebook: Run the full L12 cell. Stable ID: classroom-033; slide excerpt: source lines 9-10.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/72) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/72)

### Slide 73. Read the two readback outcomes

02:33:00-02:36:00 / 3 minutes

**Say:** The full MV/LV request remains HOLD because its evidence lacks full coverage. An explicit MV teaching request can reach simulated readback. Each result stays tied to its actual request and recommendation ID.

**Do / discuss:** Explain the full-scope HOLD and the MV-only simulated readback. These do not complete the pending review of a separate old record.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/73) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/73)

### Slide 74. Llama chooses; tools calculate; people decide

02:36:00-02:37:00 / 1 minutes

**Say:** Llama chooses and explains permitted steps. Numerical software calculates and checks. The operator reviews the evidence and retains authority. These responsibilities shape the proposed advisory pilot.

**Do / discuss:** Assign one task to Llama, numerical software and the operator. Start the proposed advisory-pilot discussion.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/74) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/74)

### Slide 75. Start a control-room pilot with a clear study request

02:37:00-02:41:00 / 4 minutes

**Say:** Begin with a clear study request and an approved read-only snapshot containing time, topology version and limits. A stale topology copy needs refreshing before the study can support a current decision.

**Do / discuss:** Ask which snapshot fields must be refreshed after the illustrated topology mismatch. This is a teaching pilot, not a deployed integration.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/75) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/75)

### Slide 76. Give the assistant a small, controlled tool list

02:41:00-02:45:00 / 4 minutes

**Say:** Use a small approved tool list and a gateway that validates requests and logs results. Equipment commands remain in the utility’s authorized operating process.

**Do / discuss:** Discuss one approved read-only function and one input-validation rule.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/76) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/76)

### Slide 77. Check three things before returning a proposal

02:45:00-02:49:00 / 4 minutes

**Say:** Before returning a proposal, check the evidence matches, all required limits pass and the requested scope is covered. A single PASS field cannot answer all three questions.

**Do / discuss:** Ask which of the three checks caught each workshop failure mode.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/77) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/77)

### Slide 78. Give the operator a short evidence packet

02:49:00-02:53:00 / 4 minutes

**Say:** Give the operator a concise evidence packet containing inputs, results, margins, rejected trials, scope and missing checks. The reviewer can request more study, reject the proposal or accept the study for the next review step.

**Do / discuss:** Ask pairs to draft a two-sentence handover for one case. Accepting a study packet does not operate equipment.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/78) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/78)

### Slide 79. Adopt it in stages and measure the benefit

02:53:00-02:57:00 / 4 minutes

**Say:** Adopt an assistant in stages, beginning with historical replay and read-only shadow studies. Measure correct work, missed checks, time and reviewer changes against a fixed workflow using the same tools.

**Do / discuss:** Choose one measurement that could demonstrate useful benefit against the fixed-workflow baseline.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/79) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/79)

### Slide 80. Save a workshop record others can repeat

02:57:00-03:00:00 / 3 minutes

**Say:** Save enough for another person to repeat the study. Explain the input, tool call, returned result, supporting checks and next operator decision. Mark each result as fresh, recorded or simulated.

**Do / discuss:** Collect an exit ticket: input, tool, result, checks and operator decision. Save the notebook and its changed inputs.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/80) · [Presenter view](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/presenter/80)

## Reading and source credits

Original source figures and our grid adaptations remain labeled on the slides. The lab uses custom Python, not the Stanford frameworks. Complete numerical sources, figure credits and evidence limits are in the [Teaching and Source Guide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/Full_Reading_Guide.html).

- Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026. [Read full source](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf).
- Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023. [Read full source](https://aclanthology.org/2023.findings-emnlp.157/).
- Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025. [Read full source](https://aclanthology.org/2025.acl-long.1323/).
- Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19. [Read full source](https://www.anthropic.com/research/building-effective-agents).
