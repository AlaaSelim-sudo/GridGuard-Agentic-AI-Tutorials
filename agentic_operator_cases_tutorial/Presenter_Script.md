# Presenter script: three operator cases

**Alaa Selim, MIT/Dartmouth; Mohamed Chehada, UT Austin.**

50 concept slides, 90 minutes and three what-if discussions. Explain each operator problem before following the agent request, tool result and human decision. No software or account is needed.

The numerical results and model replies are prepared examples. Separate recorded studies retain their own inputs and scope. One Llama model fills two roles in the implemented five-role Python workflow. No teaching example operates equipment.

## Session route

- Agent concepts and three operator problems: slides 1-8, 00:00-05:30
- Voltage support: slides 9-22, 05:30-34:00
- Service restoration: slides 23-34, 34:00-58:00
- Cyber response: slides 35-46, 58:00-81:30
- Agent workflow and operator review: slides 47-50, 81:30-90:00

<a id="module-opening"></a>
## Agent concepts and three operator problems

### Slide 1. Agentic AI: Three Operator Cases

00:00-01:00 / 1 minute

**Say:** Understand the problem, follow the agent and review the evidence. 90 minutes / three what-if discussions The examples are self-contained. No computer or software setup is needed. We will follow a goal, the agent’s requests, numerical evidence and a human decision. The results come from reduced or synthetic studies; they are examples for learning.

**Show:** Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/1)

### Slide 2. An agent chooses what to try next

01:00-02:00 / 1 minute

**Say:** Give the agent a goal. It requests a tool, reads the result and chooses the next step. The agent does not calculate the electrical result by writing a confident answer. It chooses a permitted tool, reads the result and decides whether another request or human review is needed. Trace the feedback arrow once with the audience.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/2)

### Slide 3. The agent asks; the tool calculates

02:00-02:30 / 0.5 minutes

**Say:** A tool does one job. An agent can connect several jobs using their results. The Stanford figure distinguishes one function call from a longer agentic workflow. A function can perform one calculation. An agentic workflow connects requests and uses returned results to decide what comes next.

**Show:** Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/3)

### Slide 4. Solar settings: which option should we try?

02:30-03:00 / 0.5 minutes

**Say:** Compare possible settings, then check voltage and line current. The agent can organize these trials and report the checked options. Suppose an operator needs new solar settings. Different settings affect voltage, current and useful solar output. The agent organizes a bounded study; the numerical tool supplies the engineering evidence.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/4)

### Slide 5. Give the agent a goal and clear limits

03:00-04:00 / 1 minute

**Say:** State the goal, allowed tools and stopping rules. Keep the operator’s review step explicit. A useful request states the operating goal, available tools and stopping conditions. The agent needs to know when it must ask for review rather than continue trying options. The operator defines these boundaries.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/5)

### Slide 6. Restoration: who should get power first?

04:00-04:30 / 0.5 minutes

**Say:** The operator sets the service priority. That priority changes the study the agent requests. When supply is limited, restoring the greatest total power can differ from protecting essential services. The operator chooses that priority. The agent must preserve it when requesting and comparing studies.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/6)

### Slide 7. Keep three jobs clear

04:30-05:00 / 0.5 minutes

**Say:** The agent requests a study. The tool calculates. The operator reviews the result. Keep the jobs separate. The agent coordinates requests. The numerical tool calculates. The operator reviews the evidence and decides the next authorized step. A tool passing its checks is not operating permission.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/7)

### Slide 8. Wrong readings can still fit a model

05:00-05:30 / 0.5 minutes

**Say:** A good fit alone does not prove that the readings are true. The agent can organize checks and flag missing evidence. Readings may fit a model and still be wrong. An alarm test measures one kind of mismatch. The agent can request additional checks and identify missing information, but its explanation cannot make a data source trustworthy.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/8)


<a id="module-voltage"></a>
## Voltage support

### Slide 9. Case 1: which solar settings should we use?

05:30-07:30 / 2 minutes

**Say:** Choose settings that keep voltage and line current within the allowed range. An agent can organize the trials and return checked options. Start with the physical problem: choose solar controls that respect voltage, current and equipment capacity while serving the stated generation goal. The agent can organize trials and return a checked option. It does not replace the solver or the operator.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/9)

### Slide 10. Two tools suggest different settings

07:30-08:30 / 1 minute

**Say:** MPC plans with a model. SAC uses a previously trained controller. Treat both outputs as proposals that need the same electrical checks. MPC means model predictive control: it plans with a model. SAC means soft actor-critic: it uses a previously trained policy. Both produce proposals. Apply the same electrical checks to each before comparing cost or usefulness.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/10)

### Slide 11. How the agent helps with solar settings

08:30-11:30 / 3 minutes

**Say:** The agent requests a study and reads the returned checks. It can try another allowed option or ask the operator for help. Read the loop from left to right. The operator supplies a goal. The agent requests an allowed trial. The tool calculates voltage and current. The checks decide whether it can be compared. A failed trial can lead to another permitted request or a request for help.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/11)

### Slide 12. Two solar settings change the result

11:30-12:30 / 1 minute

**Say:** One setting controls solar power output. The other provides voltage support. The tool checks voltage, line current and the solar unit’s capacity. The two controls are active-power output and voltage support. The source model represents them as a and b. They share inverter capacity, so reducing one effect can change another. Use the tool to calculate those effects rather than infer safety from the control names.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/12)

### Slide 13. Both proposals face the same checks

12:30-16:30 / 4 minutes

**Say:** The tool calculates the effect of each proposal. Compare their scores only after voltage, current and capacity checks pass. The same checks apply to both candidates. Check voltage, line current and inverter capacity first. Only a passing proposal is eligible for cost comparison. The agent’s next request should be based on the returned checks.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/13)

### Slide 14. Read the voltage and current checks

16:30-17:30 / 1 minute

**Say:** Left: voltages should stay in the allowed band. Right: current should stay below 100% of the allowance. The left plot shows the voltage distribution. The right compares current use with the allowed current. Both pass this model’s checks. The curves on the left are sorted separately, so their horizontal rank is not a matched physical location.

**Show:** Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/14)

### Slide 15. Both pass, but the trade-off is different

17:30-18:30 / 1 minute

**Say:** MPC uses 73.62% of the current allowance; SAC uses 51.68%. MPC has the lower overall score because current is only one part of the goal. The current-use values are 73.62% for MPC and 51.68% for saved SAC. Their scores are approximately 0.03110 and 0.43643. Lower score is preferred after all checks pass. SAC uses less current here partly because it also uses less active power.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/15)

### Slide 16. What if we allow less current?

18:30-24:30 / 6 minutes

**Say:** Reduce the allowance from 80% to 75% of nominal current. Which proposal might fail? Which would you choose if both pass? What must the agent ask the tool to check again? Ask people to predict without doing any calculation. Make the rule change explicit: allowed current decreases from 80% to 75% of nominal. Give pairs time to explain what must be checked again and why the lowest current is not automatically the best proposal. Advance only after the discussion.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: DISCUSS.** Invite a prediction and one reason. Advance only after the discussion.

**Ask:** Reduce the allowance from 80% to 75% of nominal current. Which proposal might fail? Which would you choose if both pass? What must the agent ask the tool to check again?

**Answer:** MPC has the lower score. SAC uses less current and less solar output. These results cover the medium-voltage model. A wider grid needs a wider study.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/16)

### Slide 17. Both proposals pass the new current check

24:30-26:30 / 2 minutes

**Say:** MPC has the lower score. SAC uses less current and less solar output. These results cover the medium-voltage model. A wider grid needs a wider study. The numerical study has already been calculated for this changed allowance. MPC uses about 78.53% of the new allowance and SAC about 54.85%; both pass. Their scores are about 0.03110 and 0.43246. MPC has the lower score. These checks cover the medium-voltage model, not the entire distribution system.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: REVEAL.** Use the prepared result to explain the answer and its limits.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/17)

### Slide 18. Less current does not mean the best option

26:30-27:30 / 1 minute

**Say:** Here SAC also uses less solar output. The operator’s goal values solar generation as well as operating limits. In the changed-allowance example, the active-power setting is about 96% of inverter rating for MPC and 34% for SAC. These percentages use inverter rating as the base. Less current comes with a generation trade-off, so the operator’s objective matters.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/18)

### Slide 19. A PASS covers only the checked model

27:30-28:00 / 0.5 minutes

**Say:** A study of the medium-voltage network cannot confirm a whole-grid claim. The agent should request the missing study or return HOLD. The model’s scope travels with its result. A passing medium-voltage study does not establish low-voltage or whole-feeder safety. When the request is wider than the evidence, the useful response is a missing-study request or HOLD.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/19)

### Slide 20. Recorded example: the first option fails

28:00-30:00 / 2 minutes

**Say:** Llama requests a check of the saved SAC proposal. The numerical tool reports too much current and rejects it. This is a separate recorded full-feeder study, with different inputs from the earlier numerical comparison. Read the actual Llama request and returned tool result. The SAC trial reaches about 111.97% of allowed current, so it fails. The tool result determines eligibility.

**Show:** Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/20)

### Slide 21. Recorded example: another option is checked

30:00-32:00 / 2 minutes

**Say:** Llama requests a check of the existing MPC fallback. The returned electrical checks pass for this recorded case. The agent requests a check of an existing MPC fallback. It does not invent or solve MPC. The historical electrical check returns about 99.60% of allowed current and no listed violations. That makes the option eligible for review within this study’s stated scope.

**Show:** Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/21)

### Slide 22. Recorded example: the operator receives a proposal

32:00-34:00 / 2 minutes

**Say:** The agent returns the checked proposal and its conditions. The operator still reviews it before any authorized action. The recorded workflow returns the checked proposal, while human acknowledgement remains pending and no equipment command is sent. Ask what evidence the operator receives and what remains outside the study, including permissions and protection checks.

**Show:** Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/22)


<a id="module-restoration"></a>
## Service restoration

### Slide 23. Case 2: who gets power after a fault?

34:00-36:00 / 2 minutes

**Say:** A fault removes a supply path. Available capacity limits what can be restored. The operator sets priorities; the agent can request and check restoration options. A fault removes one supply path in the six-node network. The available backup capacity limits which loads can be restored. Cyan marks the critical loads. The operator defines priorities, while the agent can request alternative restoration studies.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/23)

### Slide 24. How the agent helps restore service

36:00-39:00 / 3 minutes

**Say:** Choose the goal: critical loads first, or the most total power. The agent can request a study, read the trade-off and ask for a new study when limits change. The goal changes the requested optimization. The agent should keep the operator’s priority, ask the tool for a plan, read service and capacity checks, and request a new study when inputs change. The solver decides which whole loads fit the network constraints.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/24)

### Slide 25. The service goal changes the study request

39:00-42:00 / 3 minutes

**Say:** Critical-first gives more weight to essential service. Most-total-power aims to restore the largest amount of power. Critical-first assigns more value to essential service. Most-total-power maximizes total restored kW. Both still need the same network constraints. The agent translates the selected goal into the appropriate permitted study request; the solver performs the optimization.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/25)

### Slide 26. The goal changes who receives power

42:00-43:00 / 1 minute

**Say:** Critical-first: 130 kW total, including 90 kW for critical loads. Most-total-power: 140 kW total, including 30 kW for critical loads. At a 40 kW backup tie, the critical-first result restores 130 kW total, including 90 kW critical. The total-power result restores 140 kW, including only 30 kW critical. Neither objective removes the need to explain the service trade-off. In the plots, overlapping markers indicate equal outcomes.

**Show:** Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/26)

### Slide 27. Check the restoration plan

43:00-43:30 / 0.5 minutes

**Say:** Keep the faulted branch out of service. Check supply paths and capacity. Voltage, protection and field switching need separate studies. Check that the fault stays isolated, supply paths connect and capacities are respected. This teaching exercise uses an active-power service model. AC voltages, protection coordination and the order of physical switching require separate studies and procedures.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/27)

### Slide 28. What if the backup path can carry more power?

43:30-49:30 / 6 minutes

**Say:** Increase its capacity from 40 kW to 180 kW. Keep the fault and loads the same. Would the two service goals still give different results? What should the agent recalculate before reporting the new plan? Change only backup capacity in the scenario, from 40 to 180 kW. Ask whether the two service goals must always disagree. Invite participants to explain what the agent should recalculate before presenting a new plan. No software is needed to make the prediction.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: DISCUSS.** Invite a prediction and one reason. Advance only after the discussion.

**Ask:** Increase its capacity from 40 kW to 180 kW. Keep the fault and loads the same. Would the two service goals still give different results? What should the agent recalculate before reporting the new plan?

**Answer:** At 40 kW, critical-first serves 90 kW of critical load instead of 30 kW. At 180 kW, both goals serve 250 kW total, including all 90 kW of critical load.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/28)

### Slide 29. More capacity removes this service trade-off

49:30-51:30 / 2 minutes

**Say:** At 40 kW, critical-first serves 90 kW of critical load instead of 30 kW. At 180 kW, both goals serve 250 kW total, including all 90 kW of critical load. At 180 kW the two goals both restore 250 kW total, including 90 kW critical. Among the sampled capacities, the first agreement is at 80 kW. That discrete sweep does not establish an exact continuous crossover. More capacity removes the trade-off in this example.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: REVEAL.** Use the prepared result to explain the answer and its limits.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/29)

### Slide 30. A new limit needs a new study

51:30-52:00 / 0.5 minutes

**Say:** Now reduce the allowed backup capacity from 40 kW to 20 kW. The old result no longer supports the request. The agent must request a new study. Now imagine a stricter request: the backup capacity falls from 40 to 20 kW. Evidence calculated for the old capacity no longer matches the request. The agent should hold the old proposal and obtain a new constrained study. A failed evidence match does not itself prove that every new plan will fail.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/30)

### Slide 31. The agent keeps the operator’s goal

52:00-52:30 / 0.5 minutes

**Say:** The operator sets priorities. The solver selects loads. The agent can request the solve and explain the returned service trade-off. In the illustrated priority plan, loads 1, 2 and 5 receive service: 130 kW total and 90 kW critical. The operator sets the goal. The numerical solver selects loads. The agent can request the solve and explain the returned trade-off without changing the goal.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/31)

### Slide 32. Recorded example: another plan restores more service

52:30-54:30 / 2 minutes

**Say:** In this separate larger-feeder study, Llama requests another plan. The tool reports more service and passing electrical checks. This recorded larger-feeder example is separate from the six-node illustration. Llama requests another catalog option. The tool returns about 1,843.61 kW total and 474.04 kW critical service, with current at about 91.87% of its allowance. A proposed improvement becomes evidence only after the check.

**Show:** Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/32)

### Slide 33. Recorded example: the tool rejects a trial

54:30-56:00 / 1.5 minutes

**Say:** The next trial carries too much current. It cannot replace the previous passing option. The next recorded trial restores more load but reaches about 111.01% of allowed current. It is rejected. The agent must keep the earlier passing option eligible rather than replace it with an overloaded plan.

**Show:** Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/33)

### Slide 34. Recorded example: a wrong ranking is corrected

56:00-58:00 / 2 minutes

**Say:** Llama puts two passing plans in the wrong cost order. Python keeps the lower-cost plan and checks it again. The model ranks two passing plans in the wrong cost order. Since smaller cost is preferred, negative 6109 is lower than negative 5509. Python keeps the lower-cost passing plan and rechecks it. This example shows why the workflow needs a numerical guard.

**Show:** Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/34)


<a id="module-cyber"></a>
## Cyber response

### Slide 35. Case 3: can we trust these readings?

58:00-60:00 / 2 minutes

**Say:** Wrong readings can still look consistent with the model. The agent can request checks, but action still needs a trusted basis. Wrong measurements can look consistent with a grid model. The operating question is whether the evidence supports a correction, not whether the agent can write a convincing explanation. Data trust and model coverage remain explicit conditions.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/35)

### Slide 36. How the agent helps with suspicious readings

60:00-63:00 / 3 minutes

**Say:** The agent can request the checks and keep missing evidence visible. The operator reviews trust, model coverage and the proposed correction. The agent can request the permitted checks, read the results and report missing evidence. A required missing trust condition should lead to HOLD. The operator reviews the data basis, model scope and proposed adjustment.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/36)

### Slide 37. Mismatch is only one check

63:00-64:00 / 1 minute

**Say:** Mismatch J measures how well the model fits the readings. The simulation lets us measure how wrong the estimate is (state error). Mismatch J measures how well the model fits the readings. It is different from the control-cost score used in the solar case. The simulation also supplies a known true state, allowing an estimation error to be measured. That true state is not normally available to a real operator.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/37)

### Slide 38. Two patterns of wrong readings

64:00-67:00 / 3 minutes

**Say:** One wrong reading may conflict with the other readings. Coordinated changes may still look consistent with the model. One biased reading can disagree with the remaining data. Coordinated changes can agree with one another and still move the estimated state away from truth. This is a conceptual illustration of the two tested patterns; it is not an instruction for creating an attack.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/38)

### Slide 39. Read the alarm and the estimation error

67:00-68:00 / 1 minute

**Say:** Left: mismatch and its alarm threshold. Right: error against the simulation’s known truth. A quiet alarm can appear alongside a growing error. The left plot compares mismatch with the alarm threshold. The right compares the state estimate with known simulation truth. A quiet alarm can coexist with a growing error. The agent should preserve this distinction when summarizing results.

**Show:** Explain the plotted quantities and connect them to the operator’s decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/39)

### Slide 40. A coordinated change can escape the alarm

68:00-69:00 / 1 minute

**Say:** At scale 1, one biased reading gives mismatch J=277.50 and an alarm. A coordinated change gives J=3.92, no alarm, and 0.02678 rad of state error. At the reference change size, an isolated bias gives mismatch about 277.50 and triggers the alarm. A coordinated change gives about 3.92, no alarm, and about 0.02678 radians of state error. A low mismatch is incomplete evidence about data trust.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/40)

### Slide 41. What if the data change is small?

69:00-75:00 / 6 minutes

**Say:** Reduce the change to one tenth of the reference size. Will the alarm always detect the error? What else would the operator need before trusting the readings? Ask pairs to predict what a smaller error does to the alarm. Use one tenth of the reference change size. The question is whether a quiet alarm proves correct readings and what independent information an operator would need. Reveal the calculated example on the next slide.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: DISCUSS.** Invite a prediction and one reason. Advance only after the discussion.

**Ask:** Reduce the change to one tenth of the reference size. Will the alarm always detect the error? What else would the operator need before trusting the readings?

**Answer:** Neither example triggers this alarm at one tenth of the reference size. Both estimates still contain error. No alarm alone does not establish data trust.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/41)

### Slide 42. A quiet alarm can still hide an error

75:00-77:00 / 2 minutes

**Say:** Neither example triggers this alarm at one tenth of the reference size. Both estimates still contain error. No alarm alone does not establish data trust. For the smaller change, mismatch is about 10.14 for isolated bias and 3.92 for the coordinated pattern. Both are below the threshold of about 15.09. Both estimates still contain error. No alarm means this test has not crossed its threshold; it does not authenticate the readings.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: REVEAL.** Use the prepared result to explain the answer and its limits.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/42)

### Slide 43. Trusted information is needed before recovery

77:00-77:30 / 0.5 minutes

**Say:** Without the required trusted readings, the response is HOLD. With readings assumed trustworthy, the tool can calculate a proposal for review. The recovery example assumes additional trustworthy readings are available. Without that required condition the result is HOLD. With the assumption, the tool can calculate a bounded proposal. Neither the fitting algorithm nor Llama authenticates those channels.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/43)

### Slide 44. The tool calculates a small correction

77:30-78:00 / 0.5 minutes

**Say:** The solver finds the smallest allowed adjustment that meets the checked branch limits. Predicted flow: 0.17000 p.u. Offline check: 0.17046 p.u. Limit: 0.18000 p.u. The fixed recovery example proposes an adjustment of about 0.121694 per unit. The model predicts a monitored flow of 0.17000, while the offline synthetic-truth check gives 0.17046; both are below the 0.18000 limit. Per unit expresses values relative to a common model base. The offline truth check is an experimental aid, not guaranteed field information.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/44)

### Slide 45. Recorded example: request the recovery tool

78:00-79:30 / 1.5 minutes

**Say:** Llama requests the supplied recovery tool. Python calculates a correction using the assumed trusted readings. Read the actual recorded Llama request. The task already supplies a permitted recovery tool and the trusted-reading assumption. Python estimates the state and calculates the correction. The language model routes the request; it does not provide the numerical estimate.

**Show:** Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/45)

### Slide 46. Recorded example: keep human review

79:30-81:30 / 2 minutes

**Say:** The model checks pass; human review is still pending. Data trust and operating permission still need review. The recorded model checks pass, but the overall result remains REVIEW and human acknowledgement is pending. The operator still needs a trusted data basis and operating authority. The fixed workflow obtains the same numerical correction, so this is not evidence that Llama improves estimation.

**Show:** Point to the recorded request and the returned numerical result. Distinguish the model’s words from the engineering evidence.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/46)


<a id="module-closing"></a>
## Agent workflow and operator review

### Slide 47. Review must refer to the same proposal

81:30-82:30 / 1 minute

**Say:** The proposal ID and model scope must match the checked study. A different proposal or wider scope needs a new review. A reviewer must refer to the same proposal and scope that were checked. A changed proposal ID or a wider request cannot inherit an earlier passing result. In the teaching example, readback is simulated and sends no equipment command.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/47)

### Slide 48. The operator chooses the next step

82:30-83:30 / 1 minute

**Say:** Review the case, tool results, checked limits and missing work. Request another study, reject the proposal or take the next authorized step. The operator can request more evidence, reject the proposal or continue with a defined authorized step. Review the case, returned limits, model coverage and missing studies. Acceptance of a study is separate from issuing a field command.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/48)

### Slide 49. Multi-agent framework used in these cases

83:30-87:30 / 4 minutes

**Say:** The five roles share the same case facts and checked results. One Llama model handles planning and refinement. Python calculates and checks. Awareness reads the shared case. Planning prepares permitted options and uses Llama to choose a study. Simulation calculates. Verification checks limits and case identity. The Llama optimizer requests a bounded change or ranks passing options. Every changed trial returns for simulation and verification. Python guards the final choice before operator review. One Llama model fills two roles; this is not five independent language models. The implementation uses case-specific numerical tools behind the same stages.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

**Ask:** Which roles use Llama, and who checks a revised proposal?

**Answer:** Planning and the optimizer use one Llama model. Python performs fresh simulation, verification and a final guarded check before operator review.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/49)

### Slide 50. Explain one case in your own words

87:30-90:00 / 2.5 minutes

**Say:** What is the operator’s problem, and what should the agent request next? Which tool result supports the proposal, and what must the operator still decide? Ask participants to choose one case and explain the complete loop in their own words. They should name the problem, an agent request, a returned numerical fact and a remaining human decision. Optional practice materials can be used after the concept tutorial, but no account or code is needed for this discussion.

**Show:** Trace the visual from the operator’s problem to the returned evidence and the next decision.

**Teaching cue: EXPLAIN.** Connect the visual to the operator’s next decision.

[Open slide](https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/operator-cases/#/50)

## Agent roles in the three recorded cases

### Solar settings: recorded medium-voltage study

- **Awareness: read the case / Python:** Read the load, forecast, current allowance and MV model scope.
- **Planning: choose a trial / numerical tools and Llama:** Prepare MPC and saved-SAC candidates. Llama can request the declared initial studies or return review.
- **Simulation: calculate / Python:** Calculate the effects of each candidate using the declared three-phase linear model.
- **Verification: check / Python:** Check case matching, voltage, current and inverter limits. Only passing candidates receive eligible scores.
- **LLM optimizer: refine / Llama, with a Python guard:** Request less reactive power, then more PV output. Recalculate and check every changed setting. Python selects by verified cost and performs a final recheck.

Selected final current use: about 50.75% of the allowance. This recorded medium-voltage study has its own inputs and scope. The operator still reviews scope and missing checks.

### Restoration: recorded feeder-catalog study

- **Awareness: read the case / Python:** Keep the fault, available ties, critical loads, service goal and model scope in the shared case record.
- **Planning: choose a trial / numerical tools and Llama:** Prepare the stated restoration catalog options; request the initial evaluations or review.
- **Simulation: calculate / Python:** Calculate total and critical service and the current used by each option.
- **Verification: check / Python:** Reject the SHED_065 trial at about 111.01% of allowed current. Keep the passing SHED_075 trial eligible.
- **LLM optimizer: refine / Llama, with a Python guard:** Request bounded catalog changes and rank passing IDs. Python corrects the wrong cost order and rechecks the chosen plan.

Selected final service: about 1,843.61 kW total and 474.04 kW critical, at 91.87% current use. This recorded feeder study is separate from the six-node example. Physical switching order and operating permissions remain outside the result.

### Suspicious readings: recorded four-bus study

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
- [VCASE] Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. . Existing teaching snapshot reviewed 18 October 2026. https://data.openei.org/submissions/2981
- [VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017. https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf
- [VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018. https://proceedings.mlr.press/v80/haarnoja18b.html
- [LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json
- [H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [RSTL01] Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019. https://arxiv.org/abs/1912.05185v3
- [RSTL02] Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018. https://doi.org/10.1109/TPWRS.2017.2720122
- [H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json
- [CY01] Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970. https://doi.org/10.1109/TPAS.1970.292678
- [CY02] Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011. https://doi.org/10.1145/1952982.1952995
- [LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json
- [H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
- [OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final). https://doi.org/10.6028/NIST.SP.800-82r3
- [EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023. https://doi.org/10.6028/NIST.AI.100-1
- [WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. Implementation inspected 25 October 2026; records dated 27 September 2026. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py
- [H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked. https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb
