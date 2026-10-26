# Presenter script: three operator cases

**Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.**

One notebook, 69 slides, 90 minutes. Use the spoken explanation in your own voice. The run cue says exactly when to open, run, edit, reset or inspect a cell. Run the complete cell identified by its L heading and stable ID.

Python calculates new numerical results. L3, L10 and L10B show separately labeled saved model records. One Llama model fills two roles in the saved five-role Python workflow. L12 is a simulated readback; equipment_dispatch stays False.

## Session route

- Agent concepts and Colab setup: slides 1-13, 00:00-13:30
- Voltage support: slides 14-34, 13:30-38:30
- Service restoration: slides 35-47, 38:30-54:30
- Cyber response: slides 48-62, 54:30-72:00
- Agent workflow and operator review: slides 63-69, 72:00-90:00

## Colab run sheet

### Slide 10: setup / RUN

Connect a CPU. Run the whole setup cell once and wait for Ready.

Exact cells: colab-setup.

Expected: Ready appears; the support files and CPU packages are available.

### Slide 12: L0 / RUN

Run L0 with RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False.

Exact cells: classroom-002.

Expected: The data assertion passes. Both optional live-tool paths remain off.

### Slide 13: L1 / RUN

Run the whole L1 cell after L0.

Exact cells: classroom-004.

Expected: binding_pass is True, False, False in row order.

### Slide 19: L2 / RUN

Run the full L2 cell at LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

Exact cells: classroom-007.

Expected: Both default proposals pass; current use is about 73.62% for MPC and 51.68% for SAC.

### Slide 22: L2 / EDIT AND RERUN

Change only RATING_FRACTION to 0.75. Predict, then rerun all of L2. Give this exercise four minutes.

Exact cells: classroom-007.

Expected: MPC current use is about 78.53%; SAC about 54.85%; both pass this MV test.

### Slide 25: L2 / RESET AND RERUN

Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80; rerun the complete L2 cell.

Exact cells: classroom-007.

Expected: The default output returns. L3-L5 will use their separate original test_01 case.

### Slide 27: L3 / RUN

Run L3. Keep the default test_01 case.

Exact cells: classroom-010.

Expected: Three saved model replies and recorded times appear; no new model request occurs.

### Slide 29: L4 / RUN

Run L4 after L3 without changing the case ID.

Exact cells: classroom-013.

Expected: Both selectors choose RELAX_Q_10_PERCENT. Both new electrical checks pass.

### Slide 30: L5 / RUN

Run L5 with RUN_OPENDSS still False.

Exact cells: classroom-016.

Expected: The linear-model check is shown; the optional full-model path is disabled.

### Slide 37: L6 / RUN

Run L6 with CAPACITIES_KW=(40.,60.,80.,100.,120.).

Exact cells: classroom-018.

Expected: The priority MILP agrees with exhaustive enumeration. At 40 kW, compare 130/90 with 140/30 kW total/critical.

### Slide 40: L6 / EDIT AND RERUN

Append 180. to CAPACITIES_KW, keeping 40. first. Rerun all of L6. Give this exercise four minutes.

Exact cells: classroom-018.

Expected: At 180 kW, both goals serve 250 kW total and 90 kW critical.

### Slide 42: L6, L7 / RESET, THEN RUN

Restore the original capacity list and rerun L6. Then run the whole L7 cell.

Exact cells: classroom-018, classroom-021.

Expected: Original contract: True. Changed rating with old evidence: False. HOLD requests a fresh solve.

### Slide 51: L8 / RUN

Run L8 with ATTACK_SCALES=(0.,.25,.5,1.,1.5).

Exact cells: classroom-023.

Expected: A coordinated Hc attack preserves a small residual while offline state error grows.

### Slide 54: L8 / EDIT AND RERUN

Add .10 to ATTACK_SCALES. Rerun all of L8 and inspect the isolated-bias row. Give this exercise four minutes.

Exact cells: classroom-023.

Expected: At isolated scale 0.10, J is about 10.14, below the 15.09 threshold; no alarm is not proof of truth.

### Slide 56: L8 / RESET AND RERUN

Restore ATTACK_SCALES=(0.,.25,.5,1.,1.5) and rerun all of L8.

Exact cells: classroom-023.

Expected: The default sweep returns. L9 remains a separate fixed recovery fixture.

### Slide 58: L9 / RUN

Run all of L9 after resetting L8.

Exact cells: classroom-026.

Expected: No trusted replacement readings: HOLD. With assumed trusted readings: PROPOSE, u about 0.121694 p.u., zero offline violations.

### Slide 63: L10 / RUN

Run all of L10 after L9. Read the case and stage columns in the saved trace.

Exact cells: classroom-028.

Expected: Five stage names appear. Planning and optimizer rows contain actual saved Llama replies; other stages contain Python results.

### Slide 64: L10B / REPLAY THREE TIMES

After L10, run the whole L10B cell for SCENARIO="voltage", then "restoration", then "cyber". Change only that string between runs.

Exact cells: classroom-llama-walkthrough.

Expected: Input, exact model choice and public reason, saved tool result and next step appear. No new LLM call or electrical solve runs.

### Slide 65: L11, L12 / SKIP LIVE CALL, THEN RUN

Keep RUN_LOCAL_LLAMA=False. Run L11 and expect SKIPPED. Then run all of L12.

Exact cells: classroom-030, classroom-033.

Expected: The table shows HOLD for full MV/LV and an acknowledged MV teaching request. The assertions confirm wrong-ID rejection; equipment_dispatch remains False.


<a id="module-opening"></a>
## Agent concepts and Colab setup

### Slide 1. Hands-on: Three Operator Cases

00:00-01:00 / 1 minute

**Say:** Help an operator compare options, check results and decide the next step. One notebook / 90 minutes / three short exercises

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1)

### Slide 2. An agent chooses what to try next

01:00-02:00 / 1 minute

**Say:** Give the agent a goal. It requests a tool, reads the result and chooses the next step. The agent coordinates the work. The numerical tool supplies the engineering result. An error can also guide the next request.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** Who calculates the electrical result?

**Answer:** The numerical tool. The agent coordinates the requests and reads the returned evidence.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/2)

### Slide 3. The agent asks; the tool calculates

02:00-02:30 / 0.5 minutes

**Say:** A tool does one job. An agent can connect several jobs using their results. A solver can answer a well-defined study request. The agent’s job is deciding which permitted request should come next.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** What does the agent add to one tool call?

**Answer:** It can choose and connect permitted next steps using the returned results.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/3)

### Slide 4. Solar settings: which option should we try?

02:30-03:00 / 0.5 minutes

**Say:** Compare possible settings, then check voltage and line current. The agent can organize these trials and report the checked options. Think of several possible solar settings on the operator’s desk. Each candidate needs the same limit checks before comparison.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 19; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/4)

### Slide 5. Give the agent a goal and clear limits

03:00-04:00 / 1 minute

**Say:** State the goal, allowed tools and stopping rules. Keep the operator’s review step explicit. These rules belong to the application and operating process. A persuasive model response cannot change them.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** Who sets the limits and allowed actions?

**Answer:** The application and operating process, with the operator’s stated task and authority.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/5)

### Slide 6. Restoration: who should get power first?

04:00-04:30 / 0.5 minutes

**Say:** The operator sets the service priority. That priority changes what we ask the restoration tool to do. For example, serving more total power can differ from serving more critical demand. The operator must state the intended goal.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY.** Show the slide only. Run L6 later on slide 37; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/6)

### Slide 7. Keep three jobs clear

04:30-05:00 / 0.5 minutes

**Say:** The agent requests a study. The tool calculates. The operator reviews the result. Keep the three responsibilities separate when reading the examples. A fluent explanation is not a substitute for the calculation.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** Which job belongs to the operator?

**Answer:** Reviewing the evidence and deciding the next authorized step.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/7)

### Slide 8. Wrong readings can still fit a model

05:00-05:30 / 0.5 minutes

**Say:** A good fit alone does not prove the readings are true. The agent can organize checks and flag missing evidence. Later we will change readings in a small model and compare the alarm with the resulting estimation error.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY.** Show the slide only. Run L8 later on slide 51; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/8)

### Slide 9. Use one notebook for all three cases

05:30-06:30 / 1 minute

**Say:** Open Classroom Labs and save your own copy. We will use it throughout the workshop. Other notebooks on the website are supporting resources. Classroom Labs is the one required notebook for this session.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN.** Open Classroom Labs and save a copy. Run setup on slide 10, not the later lesson cells.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/9)

### Slide 10. Start Colab in three steps

06:30-09:00 / 2.5 minutes

**Say:** Save a copy, connect a CPU and run setup. Wait for Ready, then run L0 and L1. Colab gives you a temporary computer. After a runtime reset, rerun setup and the earlier cells to recreate their variables.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: RUN.** Connect a CPU. Run the whole setup cell once and wait for Ready.

Exact cells: colab-setup. Run the whole cell.

**Expected:** Ready appears; the support files and CPU packages are available.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/10)

### Slide 11. Run a cell, then read its output

09:00-09:30 / 0.5 minutes

**Say:** Find the L heading and run the whole cell. After changing an input, run that cell again. The play button runs the cell. The output below it belongs to the last completed run, so an edit alone changes nothing.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 19; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/11)

### Slide 12. Python runs the default lab

09:30-11:00 / 1.5 minutes

**Say:** In Colab, run L0 with both switches False. Python runs the calculations. The Llama examples use saved replies. No live model is needed.

**Show:** Locate L0 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN.** Run L0 with RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False.

Exact cells: classroom-002. Run the whole cell.

**Expected:** The data assertion passes. Both optional live-tool paths remain off.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/12)

### Slide 13. Does the saved result still match?

11:00-13:30 / 2.5 minutes

**Say:** Run L1. Only the unchanged request should match its saved result. Changed inputs or actions need a new check.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: RUN.** Run the whole L1 cell after L0.

Exact cells: classroom-004. Run the whole cell.

**Expected:** binding_pass is True, False, False in row order.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/13)


<a id="module-voltage"></a>
## Voltage support

### Slide 14. Case 1: which solar settings should we use?

13:30-14:00 / 0.5 minutes

**Say:** Imagine an operator comparing possible settings for solar units. Each choice changes power flows. The job is to find an acceptable option while respecting voltage, line-current and unit limits. An agent can organize the requests and responses, while the tool calculates the electrical effects. We first learn those tools in Colab, then inspect saved agent decisions.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 19; keep the notebook in order.

**Expected:** No new notebook output on this slide.

**Ask:** What must a proposed solar setting respect?

**Answer:** The checked voltage, line-current and solar-unit limits for the stated model.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/14)

### Slide 15. Two tools suggest different settings

14:00-15:00 / 1 minute

**Say:** MPC plans with a model. SAC uses a previously trained controller. Treat both outputs as proposals that need the same electrical checks. MPC means model predictive control. SAC means soft actor-critic, a learned controller. You do not need their algorithms to follow this lab: both simply supply settings for the same check.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/15)

### Slide 16. How the agent helps with solar settings

15:00-16:30 / 1.5 minutes

**Say:** Follow the arrows from the operator’s goal to the returned result. If a check fails, the agent can request another permitted trial. If evidence is missing, it can stop and ask. The useful behavior is the choice made after reading the tool result. The tool still performs the electrical calculation.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** What can happen after a failed trial?

**Answer:** Request another permitted trial, ask for missing evidence or stop for review.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/16)

### Slide 17. The study changes two solar settings

16:30-17:30 / 1 minute

**Say:** a sets active-power output. b sets voltage-support output. The tool checks voltage, line current and the solar unit’s capacity. Active power supplies energy. Reactive power supports voltage. The inverter’s shared capacity means these settings cannot be chosen independently without checking.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 19; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/17)

### Slide 18. A Python function can be a tool

17:30-18:00 / 0.5 minutes

**Say:** It receives inputs, runs calculations and returns results. L2 calls this function directly. The saved agent example shows who requests it. A tool does not have to be another AI model. Here it is ordinary Python code that calls the numerical study and returns structured results.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY.** Show the slide only. Run L2 later on slide 19; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/18)

### Slide 19. Two solar proposals, one set of checks

18:00-22:00 / 4 minutes

**Say:** Run L2 with the default settings. Look for pass/fail, current used and score J. Lower J is better after checks pass. Look for feasible, max_allowed_current_pct and current_step_J in the notebook. These mean the checked limits pass, current used and the comparison score.

**Show:** Locate L2 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN.** Run the full L2 cell at LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

Exact cells: classroom-007. Run the whole cell.

**Expected:** Both default proposals pass; current use is about 73.62% for MPC and 51.68% for SAC.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/19)

### Slide 20. Read the voltage and current checks

22:00-23:00 / 1 minute

**Say:** Left: voltages should stay in the allowed band. Right: current should stay below 100% of the allowance. A value below the current line does not replace the voltage check. The same candidate must satisfy every required check.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/20)

### Slide 21. Both pass; MPC has the lower score

23:00-24:00 / 1 minute

**Say:** MPC: 73.62% current use; score J about 0.03110. Saved SAC: 51.68% current use; score J about 0.43643. SAC uses less current, but MPC has the lower cost score. This is why we must name the goal instead of selecting the smallest number in any column.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/21)

### Slide 22. Exercise 1: lower the current allowance

24:00-28:00 / 4 minutes

**Say:** In L2, change RATING_FRACTION from 0.80 to 0.75. Predict, then rerun. Compare pass/fail, current use and score J for both methods. Does this check cover the whole medium- and low-voltage network?

**Show:** Show the question for three minutes: predict for one, then edit and run for two. Advance once for the worked answer.

**Colab: EDIT AND RERUN.** Change only RATING_FRACTION to 0.75. Predict, then rerun all of L2. Give this exercise four minutes.

Exact cells: classroom-007. Run the whole cell.

**Expected:** MPC current use is about 78.53%; SAC about 54.85%; both pass this MV test.

**Ask:** In L2, change RATING_FRACTION from 0.80 to 0.75. Predict, then rerun. Compare pass/fail, current use and score J for both methods. Does this check cover the whole medium- and low-voltage network?

**Answer:** MPC has the lower score; SAC uses less current. The score considers more than current alone. This check covers the medium-voltage model. The wider network needs a wider study. At the exercise settings, MPC uses 78.53% of the allowance and SAC uses 54.85%. Both pass. Their current-step scores are about 0.03110 and 0.43246.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/22)

### Slide 23. Exercise 1 answer: both options still pass

28:00-29:00 / 1 minute

**Say:** MPC has the lower score; SAC uses less current. The score considers more than current alone. This check covers the medium-voltage model. The wider network needs a wider study. At the exercise settings, MPC uses 78.53% of the allowance and SAC uses 54.85%. Both pass. Their current-step scores are about 0.03110 and 0.43246.

**Show:** Advance from the exercise only after learners try it. Read the verified values, explain why the outcome occurs and answer every part of the question.

**Colab: INSPECT / RESET.** Use the output already produced for the exercise. Restore RATING_FRACTION=0.80 and rerun all of L2 before continuing.

**Expected:** MPC has the lower score J. The saved SAC actor uses less current; current use alone is not the objective. Both checks cover the default MV model. They do not establish full MV/LV or dynamic performance.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/23)

### Slide 24. Less current does not mean the best option

29:00-30:00 / 1 minute

**Say:** Here SAC also uses less solar output. The goal values generation as well as limits. Compare the score after checks pass. The active-power setting is about 0.9603 for MPC and 0.3431 for SAC in this exercise. Lower solar output can reduce current but also increase the stated cost.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/24)

### Slide 25. Back to the starting values

30:00-30:30 / 0.5 minutes

**Say:** Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Rerun L2. The next cells use a separate saved case. Resetting keeps the class together. The following saved case has its own original inputs; your changed L2 settings do not rewrite it.

**Show:** Locate L2 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RESET AND RERUN.** Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80; rerun the complete L2 cell.

Exact cells: classroom-007. Run the whole cell.

**Expected:** The default output returns. L3-L5 will use their separate original test_01 case.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/25)

### Slide 26. Separate a new calculation from a replay

30:30-31:00 / 0.5 minutes

**Say:** Your inputs produce new numerical results. Saved replies show past model decisions; editing L2 does not change them. A fresh calculation answers the inputs you just supplied. A replay shows what happened previously. Both are useful, but they answer different questions.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/26)

### Slide 27. What did the saved models choose?

31:00-32:00 / 1 minute

**Say:** Run L3 to see what the models requested for the saved case. This displays old replies; it makes no new model call. Read the request, reason and recorded time as a historical record. The model is not responding to your new L2 input.

**Show:** Locate L3 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN.** Run L3. Keep the default test_01 case.

Exact cells: classroom-010. Run the whole cell.

**Expected:** Three saved model replies and recorded times appear; no new model request occurs.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/27)

### Slide 28. Different replies can request the same action

32:00-32:30 / 0.5 minutes

**Say:** Group requests that describe the same settings. A vote chooses what to test next. The electrical check still has to run. Wording alone should not create extra votes for the same physical operation. The numerical check still determines whether the selected setting passes.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/28)

### Slide 29. A fresh check of the chosen proposal

32:30-33:30 / 1 minute

**Say:** Run L4 to check the chosen proposal again in its original case. Both selectors choose the same action here, and the fresh electrical checks pass. The selection score and the engineering check do different jobs. A selected action must still be checked.

**Show:** Locate L4 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN.** Run L4 after L3 without changing the case ID.

Exact cells: classroom-013. Run the whole cell.

**Expected:** Both selectors choose RELAX_Q_10_PERCENT. Both new electrical checks pass.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/29)

### Slide 30. Which part of the grid was checked?

33:30-35:00 / 1.5 minutes

**Say:** Run L5 with the default settings. It checks the medium-voltage (MV) part of the saved case. The wider OpenDSS study is disabled by default. This cell therefore supports a medium-voltage claim only.

**Show:** Locate L5 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN.** Run L5 with RUN_OPENDSS still False.

Exact cells: classroom-016. Run the whole cell.

**Expected:** The linear-model check is shown; the optional full-model path is disabled.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/30)

### Slide 31. A PASS covers only what was checked

35:00-35:30 / 0.5 minutes

**Say:** A limited model cannot answer a wider grid question. Request the missing study or return HOLD. A checked part of a network does not stand for every device or every operating limit. Ask for the check needed by the actual decision.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/31)

### Slide 32. Recorded example: the first option fails

35:30-36:30 / 1 minute

**Say:** This saved study is different from your L2 run. Llama asks for a SAC check. The tool reports too much current. This is a preview of a different saved study, not a continuation of the passing L2 results. The recorded tool result reports a current-limit failure. The next agent choice follows that evidence.

**Show:** Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/32)

### Slide 33. Recorded example: request another option

36:30-37:30 / 1 minute

**Say:** Llama asks the tool to check the existing MPC fallback. The returned electrical checks pass for this saved case. The agent requests a plan that already exists rather than inventing its electrical outcome. The tool calculates the check and returns the evidence.

**Show:** Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/33)

### Slide 34. Recorded example: return to the operator

37:30-38:30 / 1 minute

**Say:** The agent returns the checked proposal and its conditions. Human review is still pending. No equipment command is sent. The result is a recommendation for review. The record still shows human acknowledgement pending and equipment dispatch disabled.

**Show:** Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/34)


<a id="module-restoration"></a>
## Service restoration

### Slide 35. Case 2: who gets power after a fault?

38:30-39:00 / 0.5 minutes

**Say:** A fault removes one normal supply path. Alternative paths have limited capacity, so the operator must choose what to restore. Serving critical demand first can differ from maximizing the total power served. The agent can carry that priority into a study request, collect the result and request a new study when the situation changes.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY.** Show the slide only. Run L6 later on slide 37; keep the notebook in order.

**Expected:** No new notebook output on this slide.

**Ask:** Could most total power and most critical service differ?

**Answer:** Yes. Limited capacity can force a trade-off, so the goal must be stated.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/35)

### Slide 36. How the agent helps restore service

39:00-40:00 / 1 minute

**Say:** The operator supplies the goal. The numerical solver chooses loads under the network rules. An agent could manage the study request and read its result, but it should not invent the service priority. L6 runs the tools directly; the recorded agent example comes later.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY.** Show the slide only. Run L6 later on slide 37; keep the notebook in order.

**Expected:** No new notebook output on this slide.

**Ask:** Who chooses the service priority?

**Answer:** The operator supplies the priority; the solver and agent must preserve it.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/36)

### Slide 37. Two goals for restoring power

40:00-43:00 / 3 minutes

**Say:** Run L6 to choose which loads receive power under each goal. MILP chooses whole loads; a separate calculation checks its result. MILP is a solver for choices such as whether an entire load is restored. The independent search checks the small teaching model’s objective result.

**Show:** Locate L6 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN.** Run L6 with CAPACITIES_KW=(40.,60.,80.,100.,120.).

Exact cells: classroom-018. Run the whole cell.

**Expected:** The priority MILP agrees with exhaustive enumeration. At 40 kW, compare 130/90 with 140/30 kW total/critical.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/37)

### Slide 38. Read total and critical service

43:00-44:00 / 1 minute

**Say:** Critical-first goal: 130 kW total, including 90 kW for critical loads. Most-total-power goal: 140 kW total, including 30 kW for critical loads. Read the 40 kW tie setting first. The left chart shows total service and the right shows critical service. The network is the same; the service goal changes the result.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/38)

### Slide 39. Check the restoration plan

44:00-44:30 / 0.5 minutes

**Say:** Keep the faulted branch out of service. Check supply paths and capacity. Voltage, protection and field switching need separate studies. This small exercise uses an active-power service model. The agent can request and compare its results, while the operator must review the remaining work.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/39)

### Slide 40. Exercise 2: increase tie capacity

44:30-48:30 / 4 minutes

**Say:** Add 180. to CAPACITIES_KW. Keep 40. first. Predict, then rerun L6. Compare total and critical power at 40 and 180 kW. At which tested capacity do the two goals first give the same result?

**Show:** Show the question for three minutes: predict for one, then edit and run for two. Advance once for the worked answer.

**Colab: EDIT AND RERUN.** Append 180. to CAPACITIES_KW, keeping 40. first. Rerun all of L6. Give this exercise four minutes.

Exact cells: classroom-018. Run the whole cell.

**Expected:** At 180 kW, both goals serve 250 kW total and 90 kW critical.

**Ask:** Add 180. to CAPACITIES_KW. Keep 40. first. Predict, then rerun L6. Compare total and critical power at 40 and 180 kW. At which tested capacity do the two goals first give the same result?

**Answer:** At 40 kW, the priority goal serves 90 kW critical instead of 30 kW, with less total service. The goals first match at the tested 80 kW. At 180 kW, both serve 250 kW total and 90 kW critical. The goals first match at 80 kW among the tested capacities. At 180 kW both restore 250 kW total, including 90 kW critical. This discrete sweep does not identify an exact continuous crossover.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/40)

### Slide 41. Exercise 2 answer: capacity changes the trade-off

48:30-49:30 / 1 minute

**Say:** At 40 kW, the priority goal serves 90 kW critical instead of 30 kW, with less total service. The goals first match at the tested 80 kW. At 180 kW, both serve 250 kW total and 90 kW critical. The goals first match at 80 kW among the tested capacities. At 180 kW both restore 250 kW total, including 90 kW critical. This discrete sweep does not identify an exact continuous crossover.

**Show:** Advance from the exercise only after learners try it. Read the verified values, explain why the outcome occurs and answer every part of the question.

**Colab: INSPECT / RESET.** Use the exercise output. Keep 40 first; restore the original list and rerun L6 before L7.

**Expected:** At 40 kW, priorities give more critical service: 90 kW instead of 30 kW, with less total service. The goals match from 80 kW in the tested list. At 180 kW, both serve 250 kW total, including 90 kW critical.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/41)

### Slide 42. A changed request needs a new check

49:30-51:00 / 1.5 minutes

**Say:** Restore the original capacity list and rerun L6. Run L7: the requested capacity changes from 40 kW to 20 kW. Run the complete L7 cell after restoring L6. It compares an old checked result with a request that now has a smaller capacity.

**Show:** Locate L7 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RESET, THEN RUN.** Restore the original capacity list and rerun L6. Then run the whole L7 cell.

Exact cells: classroom-018, classroom-021. Run the whole cell.

**Expected:** Original contract: True. Changed rating with old evidence: False. HOLD requests a fresh solve.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/42)

### Slide 43. A new limit needs a new study

51:00-51:30 / 0.5 minutes

**Say:** The original request matches the old result. The changed request does not. Hold the old proposal, calculate again and check the new result. The two L7 match tests return True and False. This tests whether evidence belongs to the request; it does not prove that a new plan is physically feasible.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/43)

### Slide 44. The agent keeps the operator’s goal

51:30-52:00 / 0.5 minutes

**Say:** The operator sets priorities. The solver selects loads. The agent can request the solve and explain the returned service trade-off. Keeping the goal fixed matters when many studies are requested. The agent should return the achieved total and critical service with each result.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: PREVIEW ONLY.** Show the slide only. Run L6 later on slide 37; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/44)

### Slide 45. Recorded example: try more service

52:00-53:00 / 1 minute

**Say:** This saved feeder study is different from L6. Llama requests another plan. The tool reports more service and passing checks. The saved feeder example is larger than the L6 exercise and has different numbers. Watch the request, returned check and next choice rather than comparing its total kW with L6.

**Show:** Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/45)

### Slide 46. Recorded example: the tool rejects a trial

53:00-53:30 / 0.5 minutes

**Say:** The next trial carries too much current. It cannot replace the previous passing option. The numerical guard excludes the overloaded trial. Restoring more load is useful only when the required checks also pass.

**Show:** Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/46)

### Slide 47. Recorded example: correct a wrong ranking

53:30-54:30 / 1 minute

**Say:** Llama puts two passing plans in the wrong order. Python keeps the lower-cost plan and checks it again. Here the lower costs are negative: about minus 6109 is lower than minus 5509. The model’s order is wrong, so Python corrects it and rechecks the retained plan.

**Show:** Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/47)


<a id="module-cyber"></a>
## Cyber response

### Slide 48. Case 3: can we trust these readings?

54:30-55:00 / 0.5 minutes

**Say:** The operator sees measurements, not the true system state. Several altered readings can agree with each other and still lead to a wrong estimate. An agent can request tests and organize the evidence, but it cannot create a trusted measurement source. The lab uses known simulated changes so that we can compare fit with actual estimation error.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY.** Show the slide only. Run L8 later on slide 51; keep the notebook in order.

**Expected:** No new notebook output on this slide.

**Ask:** Does a good fit prove a reading is true?

**Answer:** No. Coordinated wrong readings can fit the model while giving a wrong estimated state.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/48)

### Slide 49. How the agent helps with suspicious readings

55:00-55:30 / 0.5 minutes

**Say:** Follow the information from the readings to the proposed correction. Without the required trusted data, the workflow returns HOLD. With that assumption, the tool can calculate a candidate. The agent can request these steps and explain missing checks; the operator must still assess the premise and decide the authorized next step.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/49)

### Slide 50. Mismatch is only one check

55:30-56:30 / 1 minute

**Say:** Mismatch J measures how well the model fits the readings. The simulation lets us measure how wrong the estimate is (state error). In the cyber lab, J is a mismatch statistic, not the control cost used in the voltage lab. A low mismatch says the model fits the readings; it does not authenticate them.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY.** Show the slide only. Run L8 later on slide 51; keep the notebook in order.

**Expected:** No new notebook output on this slide.

**Ask:** What does a low mismatch tell us?

**Answer:** That the model fits the supplied readings, not that the readings are authentic.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/50)

### Slide 51. Two ways readings can be misleading

56:30-59:30 / 3 minutes

**Say:** Run L8 with the default settings. Compare one biased reading with a coordinated change across several readings. The isolated pattern changes one reading. The coordinated pattern changes several together. We compare the same two questions: did the alarm trigger, and how wrong was the estimated state?

**Show:** Locate L8 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN.** Run L8 with ATTACK_SCALES=(0.,.25,.5,1.,1.5).

Exact cells: classroom-023. Run the whole cell.

**Expected:** A coordinated Hc attack preserves a small residual while offline state error grows.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/51)

### Slide 52. Read the alarm and the estimation error

59:30-60:30 / 1 minute

**Say:** Left: mismatch and its alarm threshold. Right: error against the simulation’s known truth. A quiet alarm can appear alongside a growing error. The right plot uses truth known inside the simulation. A real operator usually cannot read that error directly from a live system.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/52)

### Slide 53. A coordinated change can escape the alarm

60:30-61:30 / 1 minute

**Say:** At scale 1, one biased reading gives mismatch J=277.50 and an alarm. A coordinated change gives J=3.92, no alarm, and 0.02678 rad of state error. The coordinated changes preserve a small mismatch even as the estimate moves away from the known state. This is the reason a quiet alarm is incomplete evidence.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/53)

### Slide 54. Exercise 3: test a small bias

61:30-65:30 / 4 minutes

**Say:** Add .10 to ATTACK_SCALES. Predict, then rerun L8. At scale 0.10, compare mismatch J, the alarm and state error. Does no alarm prove that the readings are correct?

**Show:** Show the question for three minutes: predict for one, then edit and run for two. Advance once for the worked answer.

**Colab: EDIT AND RERUN.** Add .10 to ATTACK_SCALES. Rerun all of L8 and inspect the isolated-bias row. Give this exercise four minutes.

Exact cells: classroom-023. Run the whole cell.

**Expected:** At isolated scale 0.10, J is about 10.14, below the 15.09 threshold; no alarm is not proof of truth.

**Ask:** Add .10 to ATTACK_SCALES. Predict, then rerun L8. At scale 0.10, compare mismatch J, the alarm and state error. Does no alarm prove that the readings are correct?

**Answer:** Both alarms are False at scale 0.10, but both estimates still have error. No alarm means the mismatch is below this threshold. It does not establish data trust. At scale 0.10, the isolated mismatch is about 10.143 and the coordinated mismatch is about 3.920. Both are below 15.086, while their state errors are nonzero.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/54)

### Slide 55. Exercise 3 answer: no alarm can hide an error

65:30-66:30 / 1 minute

**Say:** Both alarms are False at scale 0.10, but both estimates still have error. No alarm means the mismatch is below this threshold. It does not establish data trust. At scale 0.10, the isolated mismatch is about 10.143 and the coordinated mismatch is about 3.920. Both are below 15.086, while their state errors are nonzero.

**Show:** Advance from the exercise only after learners try it. Read the verified values, explain why the outcome occurs and answer every part of the question.

**Colab: INSPECT / RESET.** Use the output already produced for the exercise. Restore the original ATTACK_SCALES and rerun L8 before the separate fixed L9 recovery case.

**Expected:** At scale 0.10, both alarms are False. Both state estimates still have error; the coordinated shift has the larger error here. No alarm means J is below this threshold. It does not prove correct data or trusted sensors.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/55)

### Slide 56. Back to the original data-bias settings

66:30-67:00 / 0.5 minutes

**Say:** Restore the original attack scales and rerun L8. L9 uses a separate fixed recovery case. L9 is deliberately a fixed recovery example. Your L8 sweep is a separate experiment and does not select the L9 correction.

**Show:** Locate L8 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RESET AND RERUN.** Restore ATTACK_SCALES=(0.,.25,.5,1.,1.5) and rerun all of L8.

Exact cells: classroom-023. Run the whole cell.

**Expected:** The default sweep returns. L9 remains a separate fixed recovery fixture.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/56)

### Slide 57. Trusted readings must come from somewhere

67:00-67:30 / 0.5 minutes

**Say:** This example assumes extra trustworthy readings are available. Neither the fitting tool nor Llama proves that these readings are authentic. The lesson supplies a trust assumption so that the numerical task can be studied. The calculation is not a method for proving sensor identity or integrity.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: PREVIEW ONLY.** Show the slide only. Run L9 later on slide 58; keep the notebook in order.

**Expected:** No new notebook output on this slide.

**Ask:** Does Llama authenticate the extra readings?

**Answer:** No. Their trustworthiness is an explicit assumption of this example.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/57)

### Slide 58. Does the result say HOLD or PROPOSE?

67:30-69:00 / 1.5 minutes

**Say:** Run L9 and read the status before the proposed adjustment. Then check the model’s returned limits and remaining assumptions. HOLD means a required condition is absent. PROPOSE means the tool can offer a model-based correction for review, not permission to operate equipment.

**Show:** Locate L9 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: RUN.** Run all of L9 after resetting L8.

Exact cells: classroom-026. Run the whole cell.

**Expected:** No trusted replacement readings: HOLD. With assumed trusted readings: PROPOSE, u about 0.121694 p.u., zero offline violations.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/58)

### Slide 59. Missing trust means HOLD

69:00-70:00 / 1 minute

**Say:** Without trusted replacement readings: HOLD. With the trust assumption: PROPOSE a 0.121694 p.u. adjustment; the offline model checks pass. The passing result depends on the declared trust premise and the simplified model. Zero offline violations is a model result, not a field guarantee.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/59)

### Slide 60. The tool calculates a small correction

70:00-70:30 / 0.5 minutes

**Say:** The solver finds the smallest allowed adjustment that meets the checked branch limits. Predicted flow: 0.17000 p.u. Offline check: 0.17046 p.u. Limit: 0.18000 p.u. Per unit, written p.u., expresses a value relative to a chosen model base. Compare the predicted and offline checked flow with the same 0.18 limit.

**Show:** Read the visual from the input to the result. Name the operator’s goal, the agent’s request and the fact supplied by the tool. Explain the decision in the two slide sentences.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/60)

### Slide 61. Recorded example: request the recovery tool

70:30-71:00 / 0.5 minutes

**Say:** Llama requests the supplied recovery tool. Python calculates a correction using the assumed trusted readings. The permitted tool is already supplied in this example. Llama chooses to request it; Python performs the estimation and correction calculation.

**Show:** Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/61)

### Slide 62. Recorded example: keep human review

71:00-72:00 / 1 minute

**Say:** The model checks pass; human review is still pending. Data trust and operating permission still need review. A model check, human review and permission to operate equipment are separate steps. The record has not completed the latter two.

**Show:** Preview the actual saved Llama request and returned tool evidence. Do not ask learners to run ahead. L10B will replay these records after the three labs.

**Colab: PREVIEW ONLY.** Show the slide only. Run L10B later on slide 64; keep the notebook in order.

**Expected:** No new notebook output on this slide.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/62)


<a id="module-closing"></a>
## Agent workflow and operator review

### Slide 63. The saved agent workflow

72:00-74:30 / 2.5 minutes

**Say:** Run L10 to inspect the recorded planning, calculation and checking stages. Llama chooses and refines trials. Python calculates and checks them. The framework summary near the end shows all five roles together. This cell replays saved stages and makes no new model call.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: RUN.** Run all of L10 after L9. Read the case and stage columns in the saved trace.

Exact cells: classroom-028. Run the whole cell.

**Expected:** Five stage names appear. Planning and optimizer rows contain actual saved Llama replies; other stages contain Python results.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/63)

### Slide 64. How Llama chooses the next tool

74:30-81:00 / 6.5 minutes

**Say:** Set SCENARIO to voltage, restoration or cyber, then rerun this cell. Read the model’s request and the tool’s response. This is a saved replay. Run this full cell once for each scenario. The displayed words and tool evidence were recorded earlier; this default demonstration makes no fresh Llama call.

**Show:** Locate L10B in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: REPLAY THREE TIMES.** After L10, run the whole L10B cell for SCENARIO="voltage", then "restoration", then "cyber". Change only that string between runs.

Exact cells: classroom-llama-walkthrough. Run the whole cell.

**Expected:** Input, exact model choice and public reason, saved tool result and next step appear. No new LLM call or electrical solve runs.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/64)

### Slide 65. The operator checks the recommendation ID

81:00-83:00 / 2 minutes

**Say:** Leave L11 disabled, then run L12. Compare the wrong ID with the matching ID. Equipment control stays off. Readback means acknowledging the specific recommendation being reviewed. The wrong identifier must not acknowledge a different recommendation.

**Show:** Locate L12 in Classroom Labs. Show the highlighted source lines, then run the whole cell when the Colab cue says to run. Read the returned result in plain words.

**Colab: SKIP LIVE CALL, THEN RUN.** Keep RUN_LOCAL_LLAMA=False. Run L11 and expect SKIPPED. Then run all of L12.

Exact cells: classroom-030, classroom-033. Run the whole cell.

**Expected:** The table shows HOLD for full MV/LV and an acknowledged MV teaching request. The assertions confirm wrong-ID rejection; equipment_dispatch remains False.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/65)

### Slide 66. Approval must match the checked study

83:00-84:00 / 1 minute

**Say:** The wider-grid request returns HOLD. The limited teaching request permits a simulated readback. A wrong ID fails. This practice sends no equipment commands. The wider request requires checks the default study does not supply. The narrower teaching packet supports only a simulated acknowledgement, with equipment dispatch remaining False.

**Show:** Use the actual source image. Point to the returned status or number that supports the slide’s statement. State whether it is a fresh calculation or a saved example.

**Colab: NO NEW RUN.** Read the output from the previous run. Compare it with the reference figure; no new cell is needed.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/66)

### Slide 67. The operator chooses the next step

84:00-85:00 / 1 minute

**Say:** Review the case, tool results, checked limits and missing work. Request another study, reject the proposal or take the next authorized step. Ask whether the evidence belongs to this case, whether all needed checks are present and what remains unresolved. Those questions support the next human decision.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** What should happen when a required check is missing?

**Answer:** Return the unresolved condition and request the missing study or review before proceeding.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/67)

### Slide 68. Multi-agent framework used in this workshop

85:00-87:30 / 2.5 minutes

**Say:** This is the framework implemented for the saved study. Awareness reads the case facts. Planning prepares options and uses Llama to select an allowed study. Simulation calculates the result. Verification checks the limits and whether the result matches the case. The Llama optimizer can request a small change or rank passing options. A changed trial loops back through calculation and checking. Python guards the final choice, then the operator reviews it. One Llama model fills two roles. The same framework connects different numerical tools for solar settings, restoration and suspicious readings. L10 displays its saved trace; the default Colab does not launch a live agent team.

**Show:** Trace the five named roles, then the feedback loop. Ask learners to name the numerical tool used in each case. Finish at the final Python check and operator review.

**Colab: NO NEW RUN.** Explain the figure or discuss the output already produced. Do not run ahead.

**Ask:** Which roles use Llama, and what happens after a trial changes?

**Answer:** Planning and the optimizer use the same Llama model. A changed trial needs fresh simulation and verification; Python checks the final choice before operator review.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/68)

### Slide 69. Try one change and explain the result

87:30-90:00 / 2.5 minutes

**Say:** Choose one case. Change one input, rerun and save the result. Explain the problem, agent choice, tool result and operator decision. Use one case to explain the complete story. State the problem, the agent’s choice, the tool’s returned fact and the operator’s remaining decision.

**Show:** Use the two short slide statements to explain the idea. Link it to the operator’s next decision or to the named Colab cell.

**Colab: NO NEW RUN.** No required new run. Learners may repeat one case afterward and save their changed inputs and outputs.

**Ask:** What are the four parts of your explanation?

**Answer:** Problem, agent choice, tool result and operator decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/69)

## Agent roles in the three recorded cases

### Voltage: L10 MV archive

- **Awareness: read the case / Python:** Read the load, forecast, current allowance and MV model scope.
- **Planning: choose a trial / numerical tools and Llama:** Prepare MPC and saved-SAC candidates. Llama can request the declared initial studies or return review.
- **Simulation: calculate / Python:** Calculate the effects of each candidate using the declared three-phase linear model.
- **Verification: check / Python:** Check case matching, voltage, current and inverter limits. Only passing candidates receive eligible scores.
- **LLM optimizer: refine / Llama, with a Python guard:** Request less reactive power, then more PV output. Recalculate and check every changed setting. Python selects by verified cost and performs a final recheck.

Selected final current use: about 50.75% of the allowance. This is the L10 MV archive, not the L2 experiment or P3 OpenDSS replay. The operator still reviews scope and missing checks.

### Restoration: L10 feeder catalog

- **Awareness: read the case / Python:** Keep the fault, available ties, critical loads, service goal and model scope in the shared case record.
- **Planning: choose a trial / numerical tools and Llama:** Prepare the stated restoration catalog options; request the initial evaluations or review.
- **Simulation: calculate / Python:** Calculate total and critical service and the current used by each option.
- **Verification: check / Python:** Reject the SHED_065 trial at about 111.01% of allowed current. Keep the passing SHED_075 trial eligible.
- **LLM optimizer: refine / Llama, with a Python guard:** Request bounded catalog changes and rank passing IDs. Python corrects the wrong cost order and rechecks the chosen plan.

Selected final service: about 1,843.61 kW total and 474.04 kW critical, at 91.87% current use. This is not L6's six-node MILP. Physical switching order and operating permissions remain outside the result.

### Cyber: L10 four-bus DC archive

- **Awareness: read the case / Python:** Read the measurements, alarm context and declared availability of assumed trusted channels.
- **Planning: choose a trial / numerical tools and Llama:** Prepare the permitted response candidates. Llama can request the initial evaluations or review.
- **Simulation: calculate / Python:** Estimate state and calculate each candidate's branch flows and correction.
- **Verification: check / Python:** Test the trust condition, stated branch limits, bounds, evidence match and DC model scope.
- **LLM optimizer: refine / Llama, with a Python guard:** Request bounded trials including TRUSTED_QP. Python ranks only passing candidates and rechecks the selected correction.

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
- [H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023. https://doi.org/10.6028/NIST.AI.100-1
- [WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. Implementation inspected 25 October 2026; records dated 27 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py
