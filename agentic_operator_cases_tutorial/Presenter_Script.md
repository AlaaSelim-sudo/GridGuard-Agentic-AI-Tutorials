# Presenter script: three operator cases

**Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.**

One notebook, 83 slides, 90 minutes. Use the spoken explanation in your own voice. The run cue says exactly when to open, run, edit, reset or inspect a cell. Run the complete cell identified by its L heading and stable ID.

Python calculates new numerical results. L3, L10 and L10B show separately labeled saved model records. One Llama model fills two roles in the saved five-role Python workflow. L12 is a simulated readback; equipment_dispatch stays False.

## Session route

- Agent concepts and Colab setup: slides 1-15, 00:00-15:00
- Voltage support: slides 16-38, 15:00-39:00
- Service restoration: slides 39-55, 39:00-56:00
- Cyber response: slides 56-72, 56:00-73:00
- Agent workflow and operator review: slides 73-83, 73:00-90:00

## Colab run sheet

### Slide 12: setup / RUN

Connect a CPU. Run the whole setup cell once and wait for Ready.

Exact cells: colab-setup.

Expected: Ready appears; the support files and CPU packages are available.

### Slide 14: L0 / RUN

Run L0 with RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False.

Exact cells: classroom-002.

Expected: The data assertion passes. Both optional live-tool paths remain off.

### Slide 15: L1 / RUN

Run the whole L1 cell after L0.

Exact cells: classroom-004.

Expected: binding_pass is True, False, False in row order.

### Slide 21: L2 / RUN

Run the full L2 cell at LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

Exact cells: classroom-007.

Expected: Both default proposals pass; current use is about 73.62% for MPC and 51.68% for SAC.

### Slide 25: L2 / EDIT AND RERUN

Change only RATING_FRACTION to 0.75. Predict, then rerun all of L2. Give this exercise four minutes.

Exact cells: classroom-007.

Expected: MPC current use is about 78.53%; SAC about 54.85%; both pass this MV test.

### Slide 28: L2 / RESET AND RERUN

Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80; rerun the complete L2 cell.

Exact cells: classroom-007.

Expected: The default output returns. L3-L5 will use their separate original test_01 case.

### Slide 30: L3 / RUN

Run L3. Keep the default test_01 case.

Exact cells: classroom-010.

Expected: Three saved model replies and recorded times appear; no new model request occurs.

### Slide 32: L4 / RUN

Run L4 after L3 without changing the case ID.

Exact cells: classroom-013.

Expected: Both selectors choose RELAX_Q_10_PERCENT; new_check_passes is True for both.

### Slide 34: L5 / RUN

Run L5 with RUN_OPENDSS still False.

Exact cells: classroom-016.

Expected: The linear-model check is shown; the optional full-model path is disabled.

### Slide 41: L6 / RUN

Run L6 with CAPACITIES_KW=(40.,60.,80.,100.,120.).

Exact cells: classroom-018.

Expected: The priority MILP agrees with exhaustive enumeration. At 40 kW, compare 130/90 with 140/30 kW total/critical.

### Slide 45: L6 / EDIT AND RERUN

Append 180. to CAPACITIES_KW, keeping 40. first. Rerun all of L6. Give this exercise four minutes.

Exact cells: classroom-018.

Expected: At 180 kW, both goals serve 250 kW total and 90 kW critical.

### Slide 48: L6, L7 / RESET, THEN RUN

Restore the original capacity list and rerun L6. Then run the whole L7 cell.

Exact cells: classroom-018, classroom-021.

Expected: Original contract: True. Changed rating with old evidence: False. HOLD requests a fresh solve.

### Slide 58: L8 / RUN

Run L8 with ATTACK_SCALES=(0.,.25,.5,1.,1.5).

Exact cells: classroom-023.

Expected: A coordinated Hc attack preserves a small residual while offline state error grows.

### Slide 61: L8 / EDIT AND RERUN

Add .10 to ATTACK_SCALES. Rerun all of L8 and inspect the isolated-bias row. Give this exercise four minutes.

Exact cells: classroom-023.

Expected: At isolated scale 0.10, J is about 10.14, below the 15.09 threshold; no alarm is not proof of truth.

### Slide 64: L8 / RESET AND RERUN

Restore ATTACK_SCALES=(0.,.25,.5,1.,1.5) and rerun all of L8.

Exact cells: classroom-023.

Expected: The default sweep returns. L9 remains a separate fixed recovery fixture.

### Slide 67: L9 / RUN

Run all of L9 after resetting L8.

Exact cells: classroom-026.

Expected: No trusted replacement readings: HOLD. With assumed trusted readings: PROPOSE, u about 0.121694 p.u., zero offline violations.

### Slide 73: L10 / RUN

Run all of L10 after L9. Read the case and stage columns in the saved trace.

Exact cells: classroom-028.

Expected: Five stage names appear. Planning and optimizer rows contain actual saved Llama replies; other stages contain Python results.

### Slide 74: L10B / REPLAY THREE TIMES

After L10, run the whole L10B cell for SCENARIO="voltage", then "restoration", then "cyber". Change only that string between runs.

Exact cells: classroom-llama-walkthrough.

Expected: Input, exact model choice and public reason, saved tool result and next step appear. No new LLM call or electrical solve runs.

### Slide 75: L11, L12 / SKIP LIVE CALL, THEN RUN

Keep RUN_LOCAL_LLAMA=False. Run L11 and expect SKIPPED. Then run all of L12.

Exact cells: classroom-030, classroom-033.

Expected: The table shows HOLD for full MV/LV and an acknowledged MV teaching request. The assertions confirm wrong-ID rejection; equipment_dispatch remains False.


<a id="module-opening"></a>
## Agent concepts and Colab setup

### Slide 1. Hands-on: Three Operator Cases

00:00-01:00 / 1 minute

**Say:** We will use one notebook to study three operator problems: voltage support, restoring service and suspicious measurements. For each case, we will look at the input, run a tool, read the result and decide what still needs review. You can follow along now or finish the experiments later. The notebook does not control equipment.

**Show:** Point to the three case names and the one-notebook route.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1)

### Slide 2. What is agentic AI?

01:00-02:00 / 1 minute

**Say:** Here, agentic AI means a model can choose a permitted next step using a tool's returned result. The important part is that the result can change the next choice. The model still works within limits set by the application. In our default lab, Python runs now while the Llama choices come from saved recordings.

**Show:** Trace goal, model choice, tool result and feedback arrow.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** Which component supplies the electrical numbers?

**Answer:** The numerical tool; the model selects an allowed next step.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/2)

### Slide 3. A tool call and an agent workflow

02:00-02:30 / 0.5 minutes

**Say:** A tool call is one job, such as calculating a power flow. A workflow connects several jobs. In an agentic step, the model helps choose what happens next. A fixed program can also contain loops and checks, so a loop alone does not make a system agentic. Look for the actual model decision.

**Show:** Point to the single-call panel, then the multi-step panel.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/3)

### Slide 4. Evidence before an answer

02:30-03:00 / 0.5 minutes

**Say:** This source example is about checking claims before writing an answer. We use the same design habit in a grid study: calculate first, then explain the returned numbers. We are borrowing the idea, not running WikiChat in this notebook. A fluent report should never replace an electrical check.

**Show:** Follow checking before drafting in the source figure.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/4)

### Slide 5. Voltage: propose, then check

03:00-03:30 / 0.5 minutes

**Say:** For voltage, a controller proposes settings and an electrical model checks their effects. L2 lets us run those calculations ourselves. Later, L10B shows a saved Llama choice about which existing tool to use. Keep those two activities separate: a new calculation is different from replaying an old model reply.

**Show:** Point to the proposal, electrical check and returned current value.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/5)

### Slide 6. Clear rules for tool use

03:30-04:30 / 1 minute

**Say:** A useful tool needs a clear contract: required inputs, allowed operations, fixed limits and a stop condition. The language model cannot quietly change those rules to make an answer look better. In this lab, Python owns the rules. If a required input or check is missing, the workflow must stop or request review.

**Show:** Point to the explicit task-rule specification.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/6)

### Slide 7. Restoration: define the service goal

04:30-05:00 / 0.5 minutes

**Say:** Before asking for a restoration plan, define what good service means. Serving the most total power can give a different answer from protecting critical loads. The solver follows the objective we give it. The agent's job is to preserve that goal when requesting a tool and explaining its result.

**Show:** Compare the critical-service segments, then the total kW.

**Colab: PREVIEW ONLY.** Show the slide only. Run L6 later on slide 40; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/7)

### Slide 8. Language and decision checks

05:00-05:30 / 0.5 minutes

**Say:** The source figure separates language processing from a solver that checks a decision. Our grid example uses a similar separation: Llama requests a permitted study, Python calculates and checks it, and a person reviews the proposal. Our electrical models are not the logical solvers in this source example and do not inherit their guarantees.

**Show:** Follow language input into a separate checked decision.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/8)

### Slide 9. Cyber: good fit can hide bad data

05:30-06:00 / 0.5 minutes

**Say:** Suspicious readings can fit a model and still be wrong. L8 makes that problem visible by comparing a mismatch alarm with known simulation truth. L9 asks a different question: can we propose a correction if extra readings are assumed trustworthy? The trust condition remains an assumption that the operator must review.

**Show:** Point to the quiet residual and the trust-dependent recovery gate.

**Colab: PREVIEW ONLY.** Show the slide only. Run L8 later on slide 56; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/9)

### Slide 10. Four questions about any result

06:00-07:00 / 1 minute

**Say:** Use these four questions throughout the session. Which tool produced this result? What did the tool assume? Which limits did it actually check? What should the operator do next? These questions help us assess both an ordinary software result and a model-generated explanation. Missing evidence stays missing even when the wording sounds confident.

**Show:** Use the four questions to assess one statement from the opening.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** What evidence is missing from a confident answer with no tool result?

**Answer:** The actual calculated or measured result and its assumptions.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/10)

### Slide 11. One notebook for all three cases

07:00-08:00 / 1 minute

**Say:** Classroom Labs is the only required notebook. Save a copy in Drive so you can keep your changes. The voltage, restoration and cyber sections are in this same file. The other notebooks on the website are companions, so you do not need to open several Colabs to follow this workshop.

**Show:** Open the canonical Classroom Labs link and save a Drive copy.

**Colab: NO NEW RUN.** Open Classroom Labs and save a copy. Run setup on slide 12, not the later lesson cells.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/11)

### Slide 12. Colab setup

08:00-10:30 / 2.5 minutes

**Say:** Colab gives us a temporary computer called a runtime. Connect a CPU runtime and run the setup cell once. Wait for Ready before continuing. Saving a notebook keeps the text and saved outputs, not the temporary variables. After a runtime reset, rerun setup and the earlier cells. If setup is still running, follow the reference figures and catch up afterward.

**Show:** Show the CPU connection control and setup-cell play button.

**Colab: RUN.** Connect a CPU. Run the whole setup cell once and wait for Ready.

Exact cells: colab-setup. Run the whole cell.

**Expected:** Ready appears; the support files and CPU packages are available.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/12)

### Slide 13. Input, run, output

10:30-11:00 / 0.5 minutes

**Say:** A notebook cell has input code and an output below it. The slide shows selected lines, but we always run the whole matching code cell. First predict the result, then run it and read what appears. Changing a number does not update an old plot until you rerun the cell.

**Show:** Identify the input, run button and output region.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/13)

### Slide 14. L0: keep the default settings

11:00-12:30 / 1.5 minutes

**Say:** Leave both switches False. OpenDSS is off, so the default voltage calculation uses the three-phase linear model. The local Llama call is also off, so there is no new language-model request. Python still makes new numerical calculations, and the saved SAC policy still proposes a new action from its stored weights.

**Show:** Point to both False settings.

**Colab: RUN.** Run L0 with RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False.

Exact cells: classroom-002. Run the whole cell.

**Expected:** The data assertion passes. Both optional live-tool paths remain off.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/14)

### Slide 15. L1: does the result match the request?

12:30-15:00 / 2.5 minutes

**Say:** This small test asks whether the result still belongs to the same request and command. The first row should be True. Changing the load or command gives False. That match is necessary before using an old result. The hash detects a changed record; it does not authenticate a sensor or prove that the physical action is safe.

**Show:** Read the three binding_pass results.

**Colab: RUN.** Run the whole L1 cell after L0.

Exact cells: classroom-004. Run the whole cell.

**Expected:** binding_pass is True, False, False in row order.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/15)


<a id="module-voltage"></a>
## Voltage support

### Slide 16. Case 1: voltage support

15:00-15:30 / 0.5 minutes

**Say:** Our first case compares two ways to propose voltage-support settings. MPC plans using a model and a short forecast. SAC uses a policy learned earlier. We send both proposals through the same electrical check. Only after a proposal passes should we compare its penalty score J. These are teaching results on a synthetic feeder.

**Show:** Locate the voltage case on the synthetic feeder figure.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/16)

### Slide 17. Two ways to propose settings

15:30-16:30 / 1 minute

**Say:** MPC calculates settings from the model when we run it. The saved SAC policy quickly maps the current conditions to settings. Neither proposal is automatically acceptable. A separate model checks voltage, current and inverter limits. These numerical controllers are tools inside the workflow; they do not become language agents just because a model can call them.

**Show:** Follow both proposal methods into the same checker.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/17)

### Slide 18. A tool result changes the next step

16:30-18:00 / 1.5 minutes

**Say:** This is a saved P3 example, not the new L2 experiment. Llama first asks to check SAC. The tool returns about 111.97 percent of allowed current, so that trial fails. Llama then requests the existing MPC fallback, which returns about 99.60 percent and passes the recorded checks. Human review still remains pending.

**Show:** Follow the two saved current results in order.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** Why can the fallback enter review?

**Answer:** Its stated numerical checks pass; human acknowledgment is still separate.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/18)

### Slide 19. Two control settings

18:00-19:00 / 1 minute

**Say:** There are two control settings. The active-power setting changes how much real power the inverter supplies. The reactive-power setting changes reactive support. They share the inverter's capacity, so changing one affects the room available for the other. The numerical checker tests that capacity together with voltage and line-current limits.

**Show:** Point to active and reactive settings and their shared capacity.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/19)

### Slide 20. A tool is a callable function

19:00-19:30 / 0.5 minutes

**Say:** In the lab, a tool is an ordinary Python function with defined inputs and returned results. L2 calls voltage_lab directly with load scale and current allowance. That lets us inspect what the tool does without a live LLM. In the saved agent workflow, the application validates a model choice before calling an allowed function.

**Show:** Match function inputs to its returned fields.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 21; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/20)

### Slide 21. L2: run the default case

19:30-22:30 / 3 minutes

**Say:** Run the whole L2 cell with load scale 1.0 and current allowance 0.80. The cell makes an MPC plan, runs the saved SAC actor and checks both proposals. Read feasible first. Then inspect maximum allowed-current use and the score J. The plots and table below the cell are new calculations for these inputs.

**Show:** Show the input lines, then the resulting L2 table.

**Colab: RUN.** Run the full L2 cell at LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

Exact cells: classroom-007. Run the whole cell.

**Expected:** Both default proposals pass; current use is about 73.62% for MPC and 51.68% for SAC.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/21)

### Slide 22. L2: voltage and current plots

22:30-23:30 / 1 minute

**Say:** Read both plots before choosing a method. The voltage plot shows sorted modeled voltages, not the physical order of buses along a feeder. Check that they remain inside the band. The current plot shows the largest use of the allowed current. Its 100 percent line is a limit, not a performance target.

**Show:** Read the voltage band and current allowance line.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/22)

### Slide 23. L2: both default proposals pass

23:30-24:30 / 1 minute

**Say:** Both default proposals pass this model. MPC uses about 73.62 percent of the allowed current and has J about 0.03110. SAC uses less current, about 51.68 percent, but has a higher penalty score. Lower current alone does not mean a better overall objective. Compare scores only among proposals that pass the stated checks.

**Show:** Compare feasibility first, then current use and score.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

**Ask:** Does less current always mean a smaller objective?

**Answer:** No. J also includes curtailment, reactive effort and other declared penalties.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/23)

### Slide 24. The limit and the calculated result

24:30-25:00 / 0.5 minutes

**Say:** A rule tells us what is allowed. A numerical tool tells us whether a particular proposal meets that rule in a particular model. We need both. When reporting a result, keep the input case, the limit and the calculated value together. The number in this illustration comes from the separate saved P3 example.

**Show:** Point separately to the rule and returned value.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/24)

### Slide 25. Exercise 1: lower the current allowance

25:00-28:00 / 3 minutes

**Say:** Change only RATING_FRACTION from 0.80 to 0.75 in L2. Before running it, predict how the percentage of allowed current will change. Run the whole cell and compare both methods. Record the pass flag, current percentage and score. Then decide whether this model covers a full medium- and low-voltage request.

**Show:** Keep the question visible for three minutes: predict for one minute, then edit and run for two. Advance to the next slide for the one-minute worked answer.

**Colab: EDIT AND RERUN.** Change only RATING_FRACTION to 0.75. Predict, then rerun all of L2. Give this exercise four minutes.

Exact cells: classroom-007. Run the whole cell.

**Expected:** MPC current use is about 78.53%; SAC about 54.85%; both pass this MV test.

**Ask:** Does this PASS cover the whole MV/LV network?

**Answer:** No. The default covers MV phases and currents with ideal LV aggregation.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/25)

### Slide 26. Exercise 1 answer: both options still pass

28:00-29:00 / 1 minute

**Say:** At LOAD_SCALE=1.0 and RATING_FRACTION=0.75, MPC is feasible with 78.527895% current use and J=0.0311038194. Saved SAC is feasible with 54.854158% current use and J=0.4324637539. Lower J is preferred only among feasible candidates. These are fresh three-phase linear MV checks, not a full MV/LV study. Restore RATING_FRACTION=0.80 and rerun all of L2 before continuing.

**Show:** Advance from the question only after learners have made a prediction and run the cell. Read every chart label, compare the results and explain the model’s scope.

**Colab: INSPECT / RESET.** Use the output already produced for the exercise. Restore RATING_FRACTION=0.80 and rerun all of L2 before continuing.

**Expected:** MPC has the lower score J. The saved SAC actor uses less current; current use alone is not the objective. Both checks cover the default MV model. They do not establish full MV/LV or dynamic performance.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/26)

### Slide 27. Exercise 1: both still pass

29:00-30:00 / 1 minute

**Say:** A smaller allowance makes the same physical current a larger percentage of the allowance. In this example, MPC reaches about 78.53 percent and SAC about 54.85 percent. Both still pass. This particular experiment does not show a rejection, and the MV-only model still does not establish full MV/LV coverage. Compare with your own output before generalizing.

**Show:** Compare the default and changed allowance.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/27)

### Slide 28. L2: reset before continuing

30:00-30:30 / 0.5 minutes

**Say:** Restore load scale 1.0 and current allowance 0.80, then rerun L2. This gives everyone the same starting point again. L3 through L5 use a separate archived case called test_01. Your earlier parameter edit does not rewrite that archive, so we must not attach its old Llama explanation to a different new experiment.

**Show:** Show the restored two default inputs.

**Colab: RESET AND RERUN.** Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80; rerun the complete L2 cell.

Exact cells: classroom-007. Run the whole cell.

**Expected:** The default output returns. L3-L5 will use their separate original test_01 case.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/28)

### Slide 29. New calculations and saved replies

30:30-31:00 / 0.5 minutes

**Say:** We now have two kinds of evidence. A new calculation uses the inputs we just supplied. A saved model reply records what the model said for its original case. Both can be useful, but they answer different questions. A proposed control-room pilot is a third category: a design to evaluate, not evidence of a deployment.

**Show:** Point to new calculation, saved reply and proposed pilot labels.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/29)

### Slide 30. L3: inspect saved model choices

31:00-32:00 / 1 minute

**Say:** Run L3 and read the original case ID, each requested operation and its recorded call time. These are actual earlier replies. Displaying them does not call those models again. Different explanations may request exactly the same tool and settings, so the next step groups those matching requests before counting votes.

**Show:** Locate case ID, operation and recorded seconds.

**Colab: RUN.** Run L3. Keep the default test_01 case.

Exact cells: classroom-010. Run the whole cell.

**Expected:** Three saved model replies and recorded times appear; no new model request occurs.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/30)

### Slide 31. Different words can request the same trial

32:00-32:30 / 0.5 minutes

**Say:** Three replies do not necessarily produce three different physical trials. Here, two replies request the same reactive-power change, so there are two distinct operations. The vote chooses what to test next. It does not certify the choice. A numerical tool must still check the selected settings, regardless of how many models supported them.

**Show:** Count unique tool/settings records rather than sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** How many distinct trials do these three replies request?

**Answer:** Two, because two replies have identical tool/settings records.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/31)

### Slide 32. L4: check the selected trial

32:30-33:30 / 1 minute

**Say:** Run L4 after L3. We compare majority voting with a saved LinUCB selector that learned which trial to test. All earlier model calls have already happened. This selection step allocates a numerical trial; it does not decide which model to call or whether the grid limits pass. Python checks the selected original-case proposal now.

**Show:** Locate the two selectors and fresh check calls.

**Colab: RUN.** Run L4 after L3 without changing the case ID.

Exact cells: classroom-013. Run the whole cell.

**Expected:** Both selectors choose RELAX_Q_10_PERCENT; new_check_passes is True for both.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/32)

### Slide 33. L4: read the new check

33:30-34:00 / 0.5 minutes

**Say:** Both selectors choose the same trial in this example and the new MV check passes. Read new_check_passes for that result. Predicted reward is the selector's learned estimate, not an electrical margin. The saved twelve-case comparison tied voting, so this example does not show that learned selection is generally better than a simple rule.

**Show:** Point to new_check_passes and distinguish predicted reward.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/33)

### Slide 34. L5: check model coverage

34:00-35:30 / 1.5 minutes

**Say:** Run L5 with OpenDSS still off. This cell checks the original test_01 MPC plan with the MV model and reports its scope. Read the model, command and pass columns together. An optional OpenDSS route can add a wider AC audit, but we are not running it in the default classroom route.

**Show:** Read model, command, pass and scope information together.

**Colab: RUN.** Run L5 with RUN_OPENDSS still False.

Exact cells: classroom-016. Run the whole cell.

**Expected:** The linear-model check is shown; the optional full-model path is disabled.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/34)

### Slide 35. A PASS has a scope

35:30-36:00 / 0.5 minutes

**Say:** A PASS describes only what the model checked. Here that means MV phases and line currents, with ideal aggregation of LV load. If the actual request needs the full MV/LV circuit, this result is insufficient. The correct response is to obtain the wider study or keep the request on HOLD, not relabel the result.

**Show:** Point to MV coverage and the missing wider check.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/35)

### Slide 36. Saved voltage case: check SAC first

36:00-37:00 / 1 minute

**Say:** We return to a saved P3 episode. Llama asks to verify the saved SAC proposal because that check is missing. The electrical tool then finds a current-limit failure. The useful behavior is recognizing which check to request. The failure comes from the numerical tool, not from the confidence of the language explanation.

**Show:** Point to Llama choice, exact public reason and failed result.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/36)

### Slide 37. Saved voltage case: try the MPC fallback

37:00-38:00 / 1 minute

**Say:** After the failure, Llama requests the MPC plan that already exists. It does not calculate the power flow or invent a new controller. Python and OpenDSS evaluate the fallback and return its voltage and current results. We will inspect the complete saved exchange in L10B after the three numerical cases.

**Show:** Point to the MPC fallback choice and returned checks.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/37)

### Slide 38. Saved voltage case: return for review

38:00-39:00 / 1 minute

**Say:** The recorded checks pass for the MPC fallback, but the human acknowledgment is still pending. The model's review message is not the operator's approval. A fixed script reaches the same final numerical outcome in this comparison. This episode demonstrates a traceable tool-selection loop, not a measured improvement in the electrical solver.

**Show:** Point to pending acknowledgment and dispatch=False.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/38)


<a id="module-restoration"></a>
## Service restoration

### Slide 39. Case 2: restoring service

39:00-39:30 / 0.5 minutes

**Say:** The restoration exercise uses a separate six-node graph. One branch is faulted and unavailable. The tool selects whole loads under the stated capacities. We will compare total served power with power served to critical loads. This smaller example makes the objective easy to inspect; it is not the feeder catalog shown in the saved Llama episode.

**Show:** Identify the source, faulted branch, two ties and critical loads.

**Colab: PREVIEW ONLY.** Show the slide only. Run L6 later on slide 40; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/39)

### Slide 40. Two service goals

39:30-40:30 / 1 minute

**Say:** The two methods use the same graph, fault and capacity rules. One maximizes total kW. The other gives extra weight to two critical loads. The different result therefore comes from the service goal. Before an agent requests a restoration solve, the operator must state which goal the tool should follow.

**Show:** Compare the two goals on the same network.

**Colab: PREVIEW ONLY.** Show the slide only. Run L6 later on slide 40; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/40)

### Slide 41. L6: solve the restoration problem

40:30-42:30 / 2 minutes

**Say:** Run L6 with the original capacity list. A mixed-integer linear program chooses which whole loads to serve. A separate exhaustive search checks the priority score on this small graph. Read total kW, critical kW and the agreement flag. Agreement supports this formulation's result; it does not add AC voltage or protection checks.

**Show:** Read total service, critical service and enumeration agreement.

**Colab: RUN.** Run L6 with CAPACITIES_KW=(40.,60.,80.,100.,120.).

Exact cells: classroom-018. Run the whole cell.

**Expected:** The priority MILP agrees with exhaustive enumeration. At 40 kW, compare 130/90 with 140/30 kW total/critical.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/41)

### Slide 42. L6: read both service plots

42:30-43:30 / 1 minute

**Say:** Read the two service plots together. The left reports total kW and the right reports critical kW. At some capacities the markers overlap because the objectives give the same outcome. Avoid assuming that a priority objective must improve every operating point. Identify where there is a real service tradeoff before explaining a benefit.

**Show:** Compare the two plotted service measures.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/42)

### Slide 43. L6: the tradeoff at 40 kW

43:30-44:30 / 1 minute

**Say:** At a 40 kW varied tie limit, the priority goal serves 130 kW total, including 90 kW critical. The maximum-total goal serves 140 kW total, including only 30 kW critical. A separate fixed tie remains at 100 kW, so the varied tie rating is not the total served load. The priorities explain this tradeoff.

**Show:** Point to 130/90 versus 140/30, all in kW.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

**Ask:** Which goal would you choose if critical service is the stated priority?

**Answer:** The priority-weighted goal, with the explicit total-service tradeoff.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/43)

### Slide 44. Restoration checks

44:30-45:00 / 0.5 minutes

**Say:** The graph checks include source connection, power balance, branch capacity and keeping the faulted branch unavailable. The separate enumeration checks the priority objective. Those checks give evidence for this active-power model. They do not establish a field switching order, protection coordination or the voltage behavior of an AC network.

**Show:** Trace connection, balance, capacity and independent score checks.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/44)

### Slide 45. Exercise 2: increase tie capacity

45:00-48:00 / 3 minutes

**Say:** Append 180. to the capacity list and keep 40. first. Predict whether the two service goals will still disagree, then rerun the full L6 cell. Compare total and critical kW at 40 and 180 kW. Keeping the first entry unchanged matters because L7 later uses the first record in this list.

**Show:** Keep the question visible for three minutes: predict for one minute, then edit and run for two. Advance to the next slide for the one-minute worked answer.

**Colab: EDIT AND RERUN.** Append 180. to CAPACITIES_KW, keeping 40. first. Rerun all of L6. Give this exercise four minutes.

Exact cells: classroom-018. Run the whole cell.

**Expected:** At 180 kW, both goals serve 250 kW total and 90 kW critical.

**Ask:** At which tested capacity do these two goals agree?

**Answer:** They agree at 180 kW in this exercise.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/45)

### Slide 46. Exercise 2 answer: capacity changes the trade-off

48:00-49:00 / 1 minute

**Say:** At 40 kW tie capacity, priority-weighted MILP serves 130 kW total and 90 kW critical. The unweighted maximum-kW policy serves 140 kW total and 30 kW critical. In the sampled list, outcomes first match at 80 kW; they also match at 100, 120 and 180 kW. At 180 kW, both serve 250 total and 90 critical kW. Do not infer the exact continuous crossover from this discrete sweep. Keep 40 first, restore the original list and rerun L6 before L7.

**Show:** Advance from the question only after learners have made a prediction and run the cell. Read every chart label, compare the results and explain the model’s scope.

**Colab: INSPECT / RESET.** Use the exercise output. Keep 40 first; restore the original list and rerun L6 before L7.

**Expected:** At 40 kW, priorities give more critical service: 90 kW instead of 30 kW, with less total service. The goals match from 80 kW in the tested list. At 180 kW, both serve 250 kW total, including 90 kW critical.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/46)

### Slide 47. Exercise 2: enough capacity removes this tradeoff

49:00-50:00 / 1 minute

**Say:** At 180 kW, both goals serve all 250 kW of load and all 90 kW of critical load in this graph. The earlier tradeoff has disappeared. That is why a good explanation states where a method helps rather than claiming an improvement everywhere. These numbers come from conventional optimization, not from Llama.

**Show:** Compare the equal total and critical service at 180 kW.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/47)

### Slide 48. L7: test an old result after a change

50:00-51:30 / 1.5 minutes

**Say:** First restore the original capacity list and rerun L6. Then run the whole L7 cell. It matches the first restoration result to its 40 kW request, then changes the request to 20 kW without recomputing the plan. We are testing whether old evidence still matches, not solving the changed problem in this cell.

**Show:** Show the reset list, then the L7 changed request.

**Colab: RESET, THEN RUN.** Restore the original capacity list and rerun L6. Then run the whole L7 cell.

Exact cells: classroom-018, classroom-021. Run the whole cell.

**Expected:** Original contract: True. Changed rating with old evidence: False. HOLD requests a fresh solve.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/48)

### Slide 49. L7: the old evidence no longer matches

51:30-52:00 / 0.5 minutes

**Say:** The original request matches and returns True. The changed request returns False because the old evidence describes another set of inputs. Keep the old recommendation on HOLD and request a new solve. This result does not prove that every new plan at 20 kW must fail; it says the old check cannot support the changed request.

**Show:** Read original True and changed-request False.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

**Ask:** Does False prove the new physical plan is infeasible?

**Answer:** No. It detects that the old evidence does not match the changed request.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/49)

### Slide 50. New inputs need new evidence

52:00-52:30 / 0.5 minutes

**Say:** There are two different problems: an electrical limit violation and an outdated result. A mismatch test detects the second. After changing the request, we need a new solve and a new check attached to the new inputs. A confident natural-language explanation cannot turn an old calculation into current evidence.

**Show:** Distinguish an old-evidence mismatch from physical infeasibility.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/50)

### Slide 51. The agent keeps the service goal

52:30-53:00 / 0.5 minutes

**Say:** L6 itself runs Python directly: the operator supplies priorities and limits, and MILP selects loads. An agent could request that existing tool and explain the returned tradeoff while keeping the goal fixed. We should not describe that possible role as a live LLM action in L6. The saved multi-role restoration workflow is a separate study.

**Show:** Point to the operator goal and numerical load selection.

**Colab: PREVIEW ONLY.** Show the slide only. Run L6 later on slide 40; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/51)

### Slide 52. Restoration model limits

53:00-53:30 / 0.5 minutes

**Say:** The six-node model is deliberately small. It handles active-power transport and whole-load pickup. It does not check AC voltage, reactive power, protection or a safe order of field operations. A selected set of energized branches is therefore a study result to review, not a complete switching instruction.

**Show:** Name one omitted physical check.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/52)

### Slide 53. Saved restoration case: try another plan

53:30-54:30 / 1 minute

**Say:** In the separate saved feeder-catalog case, Llama requests SHED_075. The tool reports more served load than the previous passing plan, while preserving critical service and passing the current check. The operation name describes a setting in this catalog. It is not the capacity edit or MILP result from our six-node exercise.

**Show:** Read the saved SHED_075 result and current percentage.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/53)

### Slide 54. Saved restoration case: reject a failed trial

54:30-55:00 / 0.5 minutes

**Say:** Llama next requests SHED_065. That restores more ordinary load but reaches about 111 percent of allowed current, so the verifier rejects it. A larger service number cannot compensate for a failed hard limit. Keep the earlier passing candidate available, record the failure and prevent the rejected trial from entering the final ranking.

**Show:** Point to the failed current check for SHED_065.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/54)

### Slide 55. Saved restoration case: correct the ranking

55:00-56:00 / 1 minute

**Say:** Llama then puts the passing candidates in the wrong cost order. Python checks the numerical costs, keeps the lower-cost passing plan and rechecks it. This is a concrete reason to keep a deterministic ranking guard. A valid JSON answer can still contain a bad decision, so checking the output format is only the first step.

**Show:** Compare Llama order with the numerical cost order.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected:** No new notebook output on this slide.

**Ask:** Can schema-valid JSON still give the wrong ranking?

**Answer:** Yes. The numerical order must also be checked.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/55)


<a id="module-cyber"></a>
## Cyber response

### Slide 56. Case 3: suspicious readings

56:00-56:30 / 0.5 minutes

**Say:** The cyber exercise uses a separate four-bus DC model. We can compare an alarm against the true simulated state because this is an offline teaching experiment. A real control-room estimator does not receive that truth for comparison. Keep the alarm's measured consistency separate from our offline measurement of estimation error.

**Show:** Identify the separate four-bus model.

**Colab: PREVIEW ONLY.** Show the slide only. Run L8 later on slide 56; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/56)

### Slide 57. What the residual measures

56:30-57:30 / 1 minute

**Say:** Weighted least squares finds a state that fits the supplied readings, with more weight on readings declared less uncertain. Residual J measures the remaining mismatch. It does not establish where the data came from. The state-error plot is possible here because the simulation supplies a known truth, which remains outside the estimator and Llama inputs.

**Show:** Distinguish measured residual from offline truth error.

**Colab: PREVIEW ONLY.** Show the slide only. Run L8 later on slide 56; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/57)

### Slide 58. L8: run two data attacks

57:30-59:30 / 2 minutes

**Say:** Run the default L8 cell. One attack biases a single reading. The other coordinates changes so that they remain consistent with the modeled measurement relationships. Compare both the residual and state-error plots. Before looking at the curves, predict whether a larger data attack must always create a larger residual alarm.

**Show:** Show the two attack types and default scale list.

**Colab: RUN.** Run L8 with ATTACK_SCALES=(0.,.25,.5,1.,1.5).

Exact cells: classroom-023. Run the whole cell.

**Expected:** A coordinated Hc attack preserves a small residual while offline state error grows.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/58)

### Slide 59. L8: read both cyber plots

59:30-60:30 / 1 minute

**Say:** The coordinated curve is the important one to follow across both panels. Its state error can grow while the residual stays small. The left panel therefore tells us about fit to the model, not the truth of the data. Read the threshold and the offline error together before calling a quiet alarm reassuring.

**Show:** Follow one coordinated curve across both panels.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/59)

### Slide 60. L8: a coordinated attack escapes the alarm

60:30-61:30 / 1 minute

**Say:** At scale one, the isolated bias gives J about 277.50 and triggers the alarm. The coordinated attack gives J about 3.92, below the threshold, while the state error is about 0.02678 radians. This attack assumes knowledge of the model and control of the modeled unprotected channels. It is a defined teaching threat, not every possible attack.

**Show:** Compare alarm, residual and state error at scale 1.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/60)

### Slide 61. Exercise 3: test a small bias

61:30-64:30 / 3 minutes

**Say:** Add .10 to the attack-scale list and rerun L8. Focus on the isolated-bias row at that scale. Read J, the alarm flag and state error. Use the two plots to answer whether no alarm means the reading is correct. Change only the scale list so the comparison stays clear.

**Show:** Keep the question visible for three minutes: predict for one minute, then edit and run for two. Advance to the next slide for the one-minute worked answer.

**Colab: EDIT AND RERUN.** Add .10 to ATTACK_SCALES. Rerun all of L8 and inspect the isolated-bias row. Give this exercise four minutes.

Exact cells: classroom-023. Run the whole cell.

**Expected:** At isolated scale 0.10, J is about 10.14, below the 15.09 threshold; no alarm is not proof of truth.

**Ask:** Does no alarm mean the reading is true?

**Answer:** No. The threshold can miss a small bias, and coordinated changes can preserve the fit.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/61)

### Slide 62. Exercise 3 answer: no alarm can hide an error

64:30-65:30 / 1 minute

**Say:** At scale 0.10, isolated bias gives residual J=10.143237 and state error 0.0008057145 rad. Coordinated Hc gives J=3.920222 and state error 0.0025529499 rad. Both are below the 15.086272 alarm threshold, so both alarm flags are False. This J is a residual statistic, unlike the voltage-control objective J. State error is available here because simulation truth is known. Restore the original ATTACK_SCALES and rerun L8 before the separate fixed L9 recovery case.

**Show:** Advance from the question only after learners have made a prediction and run the cell. Read every chart label, compare the results and explain the model’s scope.

**Colab: INSPECT / RESET.** Use the output already produced for the exercise. Restore the original ATTACK_SCALES and rerun L8 before the separate fixed L9 recovery case.

**Expected:** At scale 0.10, both alarms are False. Both state estimates still have error; the coordinated shift has the larger error here. No alarm means J is below this threshold. It does not prove correct data or trusted sensors.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/62)

### Slide 63. Exercise 3: a small bias can miss the threshold

65:30-66:30 / 1 minute

**Say:** At isolated scale 0.10, J is about 10.14, below the 15.09 alarm threshold. A small inconsistent bias can therefore miss the threshold. The coordinated attack illustrates a different problem: it can preserve the fit by design. These examples show why a residual alarm alone cannot establish measurement authenticity.

**Show:** Point to 10.14 below 15.09.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/63)

### Slide 64. L8: reset before recovery

66:30-67:00 / 0.5 minutes

**Say:** Restore the original attack-scale list and rerun L8. This resets the shared notebook state before continuing. L9 uses a fixed recovery case rather than the last point from your scale sweep. Changing a plotted scale in L8 therefore does not automatically change the correction calculated in L9.

**Show:** Show the original scale list restored.

**Colab: RESET AND RERUN.** Restore ATTACK_SCALES=(0.,.25,.5,1.,1.5) and rerun all of L8.

Exact cells: classroom-023. Run the whole cell.

**Expected:** The default sweep returns. L9 remains a separate fixed recovery fixture.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/64)

### Slide 65. L9: one fixed recovery case

67:00-67:30 / 0.5 minutes

**Say:** We will compare the same recovery case under two information conditions. In one, the extra trusted readings are unavailable. In the other, three angle readings are assumed trustworthy. The numerical fixture stays fixed. We are testing the effect of that information assumption, not making the solver recover from every attack scale we just plotted.

**Show:** Keep the same fixed recovery case while changing data availability.

**Colab: PREVIEW ONLY.** Show the slide only. Run L9 later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/65)

### Slide 66. Data trust is an assumption

67:30-68:00 / 0.5 minutes

**Say:** The word trusted has a specific meaning here: the example assumes three independent angle readings are trustworthy. No authentication system is implemented. Neither a small residual nor a good Llama explanation can create that trust. In an actual operator study, the source and protection of those readings would need independent evidence.

**Show:** Point to the assumed trusted angle channels.

**Colab: PREVIEW ONLY.** Show the slide only. Run L9 later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

**Ask:** Which tool authenticates these three readings?

**Answer:** None in this fixture; their trust is an external assumption.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/66)

### Slide 67. L9: HOLD or PROPOSE

68:00-69:30 / 1.5 minutes

**Say:** Run all of L9. First read the status for each condition. Without the assumed trusted replacement readings, the result is HOLD and no correction is proposed. With them, a quadratic-program solver calculates a constrained correction and returns PROPOSE. The offline check uses simulation truth to assess the outcome afterward.

**Show:** Read status before looking at the correction.

**Colab: RUN.** Run all of L9 after resetting L8.

Exact cells: classroom-026. Run the whole cell.

**Expected:** No trusted replacement readings: HOLD. With assumed trusted readings: PROPOSE, u about 0.121694 p.u., zero offline violations.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/67)

### Slide 68. L9: two outcomes

69:30-70:30 / 1 minute

**Say:** With the trust assumption, the proposed flexible injection is about 0.121694 per unit and the offline model reports zero violations. Per unit means a value relative to the model's stated base, not a direct MW command. PROPOSE is a study outcome for review. It does not say that the sensors have been authenticated or that equipment may operate.

**Show:** Compare HOLD, PROPOSE and the offline violation count.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/68)

### Slide 69. L9: check the correction

70:30-71:00 / 0.5 minutes

**Say:** The solver looks for the smallest permitted correction that meets the modeled branch limits with a margin. One predicted flow is 0.17000 per unit. The offline actual value is about 0.17046, below the 0.18000 limit. Those are model-specific results. They do not add protection, dynamic or equipment-permission checks.

**Show:** Locate predicted flow, offline actual flow and the limit.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/69)

### Slide 70. A proposal depends on its assumptions

71:00-71:30 / 0.5 minutes

**Say:** The recovery proposal depends on assumed trusted data, the four-bus model and the stated limits. The numerical tool supplies the correction and its checks. The operator must still review those assumptions and any missing studies. If the required information is unavailable, the useful assistant response is a clear HOLD with the missing requirement identified.

**Show:** Point to assumptions, checks and the operator-review step.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/70)

### Slide 71. Saved cyber case: request the allowed tool

71:30-72:00 / 0.5 minutes

**Say:** This saved standard cyber episode already supplies the allowed recovery tool and the trust assumption. Llama selects that tool, and Python calculates the correction. The model does not discover a trusted sensor source. This recording is separate from the five-role cyber archive in L10, even though both use related four-bus teaching methods.

**Show:** Read the supplied tool choice and trust condition.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/71)

### Slide 72. Saved cyber case: keep human review

72:00-73:00 / 1 minute

**Say:** The recorded numerical check passes, but the language result still asks for review. The operator's acknowledgment is pending. This is the right distinction to keep visible: a passed calculation, a model's review message and a person's decision are different events. The fixed comparator gives the same numerical outcome in this saved episode.

**Show:** Read PASS, REVIEW and pending human acknowledgment separately.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 71; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/72)


<a id="module-closing"></a>
## Agent workflow and operator review

### Slide 73. L10: inspect the five-role workflow

73:00-74:30 / 1.5 minutes

**Say:** Run L10 to inspect every stage in the saved five-role workflow. Read a case, role, returned choice and result rather than only the model's explanation. One Llama model fills the planning and optimizer roles; Python performs the other stages. This cell reads the saved trace. It does not launch five new agents or call a model.

**Show:** Expand the saved trace and find all five distinct stage names.

**Colab: RUN.** Run all of L10 after L9. Read the case and stage columns in the saved trace.

Exact cells: classroom-028. Run the whole cell.

**Expected:** Five stage names appear. Planning and optimizer rows contain actual saved Llama replies; other stages contain Python results.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/73)

### Slide 74. L10B: replay the three Llama examples

74:30-79:00 / 4.5 minutes

**Say:** Run the full L10B cell for voltage, then change SCENARIO to restoration and cyber, rerunning each time. Follow input facts, allowed choice, exact public reason, tool result and next step. Find the failed voltage trial or wrong restoration ranking. These are saved, source-checked episodes; replaying them performs no new Llama call or electrical solve.

**Show:** Follow one full replay from facts to next decision.

**Colab: REPLAY THREE TIMES.** After L10, run the whole L10B cell for SCENARIO="voltage", then "restoration", then "cyber". Change only that string between runs.

Exact cells: classroom-llama-walkthrough. Run the whole cell.

**Expected:** Input, exact model choice and public reason, saved tool result and next step appear. No new LLM call or electrical solve runs.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/74)

### Slide 75. L12: practice operator readback

79:00-81:00 / 2 minutes

**Say:** Leave the live-model switch False and run L11; SKIPPED is expected. Then run L12. It returns to the original voltage test_01 result, not the restoration or cyber sweeps. Compare a full MV/LV request with an explicit MV teaching request, then inspect the wrong-ID and correct-ID readback tests. This remains a simulation.

**Show:** Locate the wrong-ID assertion, the matching readback and equipment_dispatch.

**Colab: SKIP LIVE CALL, THEN RUN.** Keep RUN_LOCAL_LLAMA=False. Run L11 and expect SKIPPED. Then run all of L12.

Exact cells: classroom-030, classroom-033. Run the whole cell.

**Expected:** The table shows HOLD for full MV/LV and an acknowledged MV teaching request. The assertions confirm wrong-ID rejection; equipment_dispatch remains False.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/75)

### Slide 76. L12: approval must match the checked scope

81:00-82:00 / 1 minute

**Say:** The full MV/LV request stays on HOLD because the evidence only covers MV. The narrower teaching request can accept a simulated readback when the recommendation ID matches. A wrong ID fails. Check that equipment_dispatch remains False. Human acknowledgment records which study was reviewed; it cannot repair a missing engineering check or authorize field switching here.

**Show:** Compare scope matching before acknowledgment.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

**Ask:** Can a correct recommendation ID repair missing LV coverage?

**Answer:** No. Scope must match before a readback can be accepted.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/76)

### Slide 77. Our multi-agent design: five roles

82:00-83:30 / 1.5 minutes

**Say:** The multi-agent design here means five named responsibilities in one Python workflow. Awareness reads the case. Planning prepares candidates and asks Llama whether to proceed. Simulation calculates their effects. Verification applies fixed checks. The optimizer asks Llama for an allowed new trial or ranking. Changed trials return for calculation and checking, and the selected option gets a final recheck before human review.

**Show:** Follow the five roles and the return path for a changed trial.

**Colab: NO NEW RUN.** Use the saved L10 trace already displayed. Map the five roles without making a new model call.

**Ask:** Are these five separate LLMs?

**Answer:** No. One Llama model fills two roles; Python runs awareness, simulation and verification.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/77)

### Slide 78. Five roles in the voltage case

83:30-84:30 / 1 minute

**Say:** For the saved L10 voltage case, awareness keeps the load and limits. Numerical planning tools supply MPC and SAC candidates. Simulation calculates voltage and current, and verification tests the limits. Llama requests less reactive power and then more solar output. Python rechecks each change. The final current use is about 50.75 percent in the MV-only model; operator review is still separate.

**Show:** Map each role to the saved voltage inputs, calculations and final result.

**Colab: NO NEW RUN.** Use the saved L10 trace already displayed. Map the five roles without making a new model call.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/78)

### Slide 79. Five roles in the restoration case

84:30-85:30 / 1 minute

**Say:** For L10 restoration, awareness records the fault, available ties and critical loads. Planning supplies catalog options. Simulation measures service and current. Verification rejects the SHED_065 trial that exceeds the current limit. Llama's optimizer also ranks passing plans incorrectly. Python corrects the cost order and rechecks the chosen plan: about 1,843.61 kW total and 474.04 kW critical, with 91.87 percent current use.

**Show:** Map each role to the saved catalog trial, failure and corrected ranking.

**Colab: NO NEW RUN.** Use the saved L10 trace already displayed. Map the five roles without making a new model call.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/79)

### Slide 80. Five roles in the cyber case

85:30-86:30 / 1 minute

**Say:** For L10 cyber response, awareness preserves the readings and declared trust assumption. Planning supplies allowed response candidates. Simulation estimates the state and calculates corrections. Verification tests the trust condition, flows and model scope. Llama requests bounded refinements, including the trusted-data QP. The final selected injection is about 0.121694 per unit. None of these roles authenticates the sensors or replaces human review.

**Show:** Map each role to data trust, the QP correction and flow checks.

**Colab: NO NEW RUN.** Use the saved L10 trace already displayed. Map the five roles without making a new model call.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/80)

### Slide 81. The operator reviews one evidence packet

86:30-87:30 / 1 minute

**Say:** An operator needs a short evidence packet: which case and data were used, which proposal was selected, the worst margins and the missing checks. The person can request another study, reject the proposal or accept it for a defined next step. Reviewing a study is different from issuing an equipment command through an authorized operating process.

**Show:** Point to the study packet and the three review choices.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/81)

### Slide 82. What the evidence shows

87:30-88:30 / 1 minute

**Say:** We should measure useful benefit rather than assume it. In L10's six paired comparisons, five final costs tied and one Llama route was worse. Model calls also added time. Start with past cases and read-only studies. Compare completed work, missed checks, time and review effort against a fixed script using the same numerical tools and budgets.

**Show:** Keep the paired study result separate from a proposed pilot benefit.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** What useful benefit should a new pilot measure?

**Answer:** Completed correct studies, missed checks, elapsed time and reviewer effort against a fixed-script baseline.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/82)

### Slide 83. Questions and your next lab run

88:30-90:00 / 1.5 minutes

**Say:** Choose one case you can repeat after the session. Change one input, run the relevant cell and save the result. Explain the model's choice where a saved episode is used, the numerical tool result, the check and the operator's remaining decision. Keep your new experiment separate from the saved reply's original inputs. We can now use questions to revisit any part of that loop.

**Show:** Point to the Colab link and invite one repeatable experiment.

**Colab: NO NEW RUN.** No required new run. Learners may repeat one case afterward and save their changed inputs and outputs.

**Ask:** Can you explain one case using input, tool, result, check and operator decision?

**Answer:** Accept an answer only when it distinguishes new calculations from saved model replies and states a remaining limit.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/83)

## Agent roles in the three recorded cases

### Voltage: L10 MV archive

- **Awareness / Python:** Read the load, forecast, current allowance and MV model scope.
- **Planning / numerical tools and Llama:** Prepare MPC and saved-SAC candidates. Llama can request the declared initial studies or return review.
- **Simulation / Python:** Calculate the effects of each candidate using the declared three-phase linear model.
- **Verification / Python:** Check case matching, voltage, current and inverter limits. Only passing candidates receive eligible scores.
- **Optimizer / Llama, with a Python guard:** Request less reactive power, then more PV output. Recalculate and check every changed setting. Python selects by verified cost and performs a final recheck.

Selected final current use: about 50.75% of the allowance. This is the L10 MV archive, not the L2 experiment or P3 OpenDSS replay. The operator still reviews scope and missing checks.

### Restoration: L10 feeder catalog

- **Awareness / Python:** Keep the fault, available ties, critical loads, service goal and model scope in the shared case record.
- **Planning / numerical tools and Llama:** Prepare the stated restoration catalog options; request the initial evaluations or review.
- **Simulation / Python:** Calculate total and critical service and the current used by each option.
- **Verification / Python:** Reject the SHED_065 trial at about 111.01% of allowed current. Keep the passing SHED_075 trial eligible.
- **Optimizer / Llama, with a Python guard:** Request bounded catalog changes and rank passing IDs. Python corrects the wrong cost order and rechecks the chosen plan.

Selected final service: about 1,843.61 kW total and 474.04 kW critical, at 91.87% current use. This is not L6's six-node MILP. Physical switching order and operating permissions remain outside the result.

### Cyber: L10 four-bus DC archive

- **Awareness / Python:** Read the measurements, alarm context and declared availability of assumed trusted channels.
- **Planning / numerical tools and Llama:** Prepare the permitted response candidates. Llama can request the initial evaluations or review.
- **Simulation / Python:** Estimate state and calculate each candidate's branch flows and correction.
- **Verification / Python:** Test the trust condition, stated branch limits, bounds, evidence match and DC model scope.
- **Optimizer / Llama, with a Python guard:** Request bounded trials including TRUSTED_QP. Python ranks only passing candidates and rechecks the selected correction.

Selected correction: about 0.121694 p.u., with predicted flow 0.17000 p.u. against the 0.18000 p.u. limit. The trusted readings are assumed, not authenticated. Human review is still separate from equipment dispatch.

## Full sources

- [H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md
- [B01] . IEEE Communications Society: official resources and network presentation template. IEEE Communications Society. Reviewed 17 October 2026. https://www.comsoc.org/about/brand-experience/resources
- [ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026. https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
- [DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19. https://www.anthropic.com/research/building-effective-agents
- [LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py
- [ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023. https://aclanthology.org/2023.findings-emnlp.157/
- [H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [ST03] Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025. https://aclanthology.org/2025.acl-long.1323/
- [H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [COL01] Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026. https://research.google.com/colaboratory/faq.html
- [VCASE] Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. . Existing teaching snapshot reviewed 18 October 2026. https://data.openei.org/submissions/2981
- [VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017. https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf
- [VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018. https://proceedings.mlr.press/v80/haarnoja18b.html
- [LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json
- [OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final). https://doi.org/10.6028/NIST.SP.800-82r3
- [H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [H04] Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [RSTL01] Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019. https://arxiv.org/abs/1912.05185v3
- [RSTL02] Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018. https://doi.org/10.1109/TPWRS.2017.2720122
- [H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json
- [CY01] Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970. https://doi.org/10.1109/TPAS.1970.292678
- [CY02] Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011. https://doi.org/10.1145/1952982.1952995
- [LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json
- [H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [OLL1] Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026. https://docs.ollama.com/capabilities/structured-outputs
- [WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. Implementation inspected 25 October 2026; records dated 27 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py
- [EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023. https://doi.org/10.6028/NIST.AI.100-1
