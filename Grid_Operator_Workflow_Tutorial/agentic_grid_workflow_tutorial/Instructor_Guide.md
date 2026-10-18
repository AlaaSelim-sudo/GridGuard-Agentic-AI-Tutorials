# Instructor guide: agentic workflows for grid operators

This workshop teaches how an agentic framework can organize a grid-control task around established numerical tools. MPC, a pretrained deep Q-network (DQN), and a restoration search provide candidate actions. OpenDSS evaluates their electrical consequences. Explicit verification and bounded repair complete the operating workflow.

The central question is:

> What does agentic coordination add when the numerical tools, evidence, and engineering checks are held constant?

Treat that as an experimental question. Do not promise that the agent always finds a better dispatch, that multiple roles are always necessary, or that a passed simulation certifies field safety.

## Audience and learning outcomes

The audience may include power-system researchers, graduate students, and engineers who can read a short Python example. Assume basic familiarity with voltage, active and reactive power, and per-unit quantities. Introduce agent terminology, optimization notation, and DRL concepts in the lesson.

Participants should leave able to:

- identify which part of a result comes from a controller, an electrical model, a verification rule, or an agent;
- inspect an end-to-end trace from operating evidence to an accepted or rejected action;
- explain why MPC and DRL are useful specialist tools inside the workflow;
- reproduce a small experiment and change one assumption;
- describe a measured benefit and its corresponding limitation.

## Preparation before participants arrive

1. Install the requirements and open `Grid_Operator_Workflow.ipynb` in the intended environment. Use the setup instructions in `README.md`.
2. Confirm that the included feeder compiles and produces a converged OpenDSS solution.
3. Confirm that Ollama is running and `llama3.1:8b` is installed. Make one model call before the class so that model loading does not interrupt the first explanation.
4. Check that the seed-11 DQN checkpoint and training metadata are present in `models/`.
5. Run the main notebook in order. Confirm which results are new live outputs and which are supplied records.
6. Open the HTML lesson as a backup. If using replay, announce it and keep the mode label visible.
7. Keep the presentation, notebook, and instructor guide available. The slides introduce the problem; the notebook provides the evidence.

Regenerate scenario records with `python -m src.run_labs` when preparing the workshop. Optional seed-11 policy retraining takes seconds on the preparation machine; use the supplied checkpoint during the main route and the [scientific notes](appendix/Scientific_Notes.md) for retraining and extensions.

The main notebook uses live Llama calls by default. If a participant's model is unavailable, let that participant use the explicit replay setting or pair with another participant. Do not invent a replacement model response. Explain that recorded inference times do not measure that participant's machine. Explicit test doubles appear only in appendix regression tests and are not experiment evidence.

## Delivery plan: exactly 180 minutes

| Clock | Minutes | Purpose | Participant activity |
|---|---:|---|---|
| 00:00–00:15 | 15 | Establish the task and make the environment work | Run the opening checks and identify the current live/replay mode. |
| 00:15–00:35 | 20 | Understand the feeder and electrical assumptions | Predict the effect of PV injection, then inspect the uncontrolled voltage/loading plot. |
| 00:35–01:05 | 30 | Understand MPC and DQN as tools | Inspect one MPC plan and one DQN candidate before viewing verification results. |
| 01:05–01:35 | 30 | Follow and evaluate the agentic workflow | Inspect coordination, a 15-minute language-intake experiment, and matched recovery. |
| 01:35–01:45 | 10 | Break | Leave the workflow diagram visible. |
| 01:45–02:15 | 30 | Apply the workflow to restoration | Compare normal alternate supply with a constrained alternate route. |
| 02:15–02:45 | 30 | Examine evidence and instruction attacks | Predict which gate should react and inspect the actual trace. |
| 02:45–03:00 | 15 | Draw bounded conclusions | Read a comparison table and formulate one defensible claim. |

Use one repeated rhythm: **ask → predict → formulate → run → interpret → change one parameter**. Explain the meaning of a plot before discussing every number. Keep implementation details in helper modules unless a participant asks how a check works.

## Part 1 — Setup and purpose, 15 minutes

Open with an operating request: “Keep the feeder within its operating limits and tell me what evidence supports the proposed action.”

Ask participants to distinguish four questions:

1. What is happening?
2. Which numerical tool should we use?
3. Does its proposed action pass the checks?
4. What should happen if it does not?

Introduce the roles with one sentence each. Awareness organizes the evidence. Planning chooses a tool. The controller proposes an action. Simulation measures its predicted effect. Verification applies explicit checks. Repair uses the rejection reason to choose the next bounded step.

Make clear that several roles may use the same language model. They are separate responsibilities and message contracts; they are not independent witnesses to physical truth.

**Checkpoint:** participants can point to the notebook's operating mode and identify the local Llama model.

## Part 2 — One feeder and its physics, 20 minutes

Show the selected SMART-DS feeder and its baseline operating condition. Label the network as a synthetic Greensboro model. It is a geographically motivated research dataset, not the city's full system or a live utility connection [1].

Use one voltage-sensitivity illustration:

\[
v_j \approx v_i - 2(r_{ij}P_{ij}+x_{ij}Q_{ij}), \qquad v_i=|V_i|^2.
\]

Use consistent per-unit bases for the quantities in this introductory equation. Explain that positive downstream consumption tends to increase the voltage drop under this sign convention. Reverse power flow can change that effect. The equation is a simplified scalar branch-flow illustration; it omits loss terms and multiphase coupling. It is not the implemented three-phase solver [2, 3]. The scientific notes show the corresponding physical-unit expressions and distinguish phase power from three-phase total power.

OpenDSS solves the implemented unbalanced feeder model. Its convergence flag and the evaluated voltage and current limits are distinct checks [4, 5]. A numerical solve can converge to an operating point that violates a limit.

**Plot to read:** uncontrolled voltage and line loading. Ask which constraint is binding before discussing which control action might help.

**Exercise 1 · 4 minutes, matching the notebook.** Explain why a linearized model could be useful inside a larger MPC optimizer while a fresh AC calculation remains useful after optimization. Name one source of error that neither model comparison captures.

**Expected response:** a linearized model can make a larger optimization problem easier to solve, while a fresh nonlinear AC calculation can reveal approximation error in the proposed action. Agreement between two models does not establish agreement with the real system. Incorrect equipment parameters, unavailable devices, erroneous topology, unmodeled dynamics, or shared measurement bias can affect both. The implemented feeder MPC uses a nonlinear AC lookup; the linear example teaches a possible extension.

**Optional discussion:** would reducing PV necessarily solve every feeder problem? No. It may relieve reverse-flow overvoltage or export overloads, but another operating point could have undervoltage, forward-flow overloads, an outage, or an unavailable actuator.

## Part 3 — MPC and DRL inside the workflow, 30 minutes

Spend about 15 minutes on MPC, 8 on DQN, 2 on reading the proposals, and 5 on Exercise 2.

For MPC, explain the sequence “forecast, optimize a plan, apply its first move, observe again.” Present a generic objective:

\[
\min_{u_{t:t+H-1}} \sum_{k=t}^{t+H-1}
\bigl(c_{\mathrm{curt},k}+\lambda\|u_k-u_{k-1}\|\bigr)
\quad\text{subject to the predictive model and operating constraints.}
\]

Explain every symbol before running the cell. The implemented MPC selects among eight common PV caps over a three-step forecast using a table of nonlinear OpenDSS solutions at five demand levels. It maximizes normalized PV output minus a movement penalty with discount factor 0.95. The scientific notes give the exact objective. The equation above is a teaching template, not an additional solver hidden from the reader.

Time coupling matters. A switching or ramp penalty, an actuator state, or an energy state can connect decisions across the horizon. Repeating independent snapshot optimizations should not be described as a full dynamic MPC demonstration. Discuss the future-step predictions and show which first action is evaluated [6].

For DQN, explain a policy that scores a discrete set of actions:

\[
a_t=\arg\max_a Q_\theta(o_t,a).
\]

Here, \(o_t\) is the observation and \(Q_\theta\) is a learned action-value function. The policy is trained offline; the main lesson uses the supplied seed-11 checkpoint. Inspect its documented observation, action choices, reward, and training range. Distinguish training reward from verified engineering feasibility [7].

Both controllers produce proposals. The same verifier evaluates either proposal.

**Exercise 2 · 5 minutes, matching the notebook.** Change `rating_fraction` to 1.0, then 0.8. Compare tool proposals and accepted outcomes. Do not interpret a low neural-network inference time as the total time of a verified operating decision.

**Expected response:** at nominal rating, the supplied seed-11 DQN and MPC propose a 30% cap, which passes the common check; maximum line utilization is about 87.60%. At rating fraction 0.8, the DQN still proposes 30%, producing about 109.50% of the allowed rating and a thermal rejection. MPC proposes 20%, which passes at about 66.52%. Compare the final accepted action, not just the proposal or inference speed. Evidence preparation, the fresh solve, verification, and any repair contribute to total decision time.

**Optional discussion:** a DQN action has the best predicted return but exceeds a line limit. Reject it, preserve the failure reason, and request an allowed repair or another tool. The reward score does not overrule the engineering gate.

**Optional discussion:** increasing the movement penalty tends to encourage fewer or smaller cap changes, subject to feasibility. It need not change the selected action when other costs or feasible choices dominate.

## Part 4 — Agent coordination, verification, and repair, 30 minutes

Keep this block within 30 minutes: five minutes for the core loop, seven for natural-language intake, eight for measured results, six for recovery and Exercise 4, and four for Exercise 3 with the request-checking extension below. The seven-plus-eight-minute intake experiment is part of this existing block, not an addition to the three-hour schedule. Use supplied study records for the full tables; one live request is sufficient in class. Repeating all 72 pilot model calls belongs in preparation.

Reveal an actual Llama tool request. Ask participants to read the selected tool and arguments before reading the explanation. Then follow the record through the numerical tool, the fresh OpenDSS solution, and the verifier.

A tool-using reasoning loop is supported by the ReAct literature [8]. That source motivates interaction with tools; it does not prove that Llama is a better grid controller.

Highlight three boundaries:

- Untrusted external text can describe an event but cannot grant permission to bypass a check.
- A failed tool call, invalid schema, or rejected action remains a failure in the record.
- Repair has a finite attempt budget. Exhausting that budget ends without an accepted action.

Compare with the supplied scripted workflow. Match the scenario, controller tools, evidence, and checks. Show any difference in access to a recovery operation rather than treating it as an inherent property of conventional control.

### Fifteen-minute value experiment: language to verified action

Use notebook Sections 4.5–4.7 and the [study methods and results](appendix/Agentic_Advantage_Study.md). Begin with q09: “Bring back demand with at most one hundred amperes through the nearby bypass. Keep the farther route open and leave solar generation out of the plan.” Have participants predict the four fields before displaying either interface's answer. The documented parser hands off. Llama once correctly produces a 100 A short-route limit, forbids the long route and PV, and retains nominal rating fraction 1.0. The same downstream restoration search and fresh OpenDSS check then support 1,843.61 kW of nominal connected demand. Llama interpreted the request; it did not compute the electrical solution.

Show both the benefit and its cost:

| Study and interface | Correct clear-request completions | Wrong READY responses, all requests | Clear-request handoffs | Correct required clarifications |
|---|---:|---:|---:|---:|
| Pilot parser | 14/20 | 0/24 | 6/20 | 4/4 |
| Pilot Llama once | 16/20 | 4/24 | 0/20 | 4/4 |
| Pilot Llama plus critic | 9/20 | 5/24 | 7/20 | 3/4 |
| Pilot Llama self-review | 10/20 | 7/24 | 4/20 | 3/4 |
| Confirmation parser | 5/8 | 1/12 | 2/8 | 4/4 |
| Confirmation parser-first hybrid | 7/8 | 2/12 | 0/8 | 3/4 |

The structured reference completes all 20 clear pilot requests; correct manual-form entry is assumed, and human effort is not measured. The hybrid policy was selected after seeing the pilot; its 19/20 pilot result is exploratory. The separate 12-request confirmation set was authored and frozen before its model calls, including eight clear requests and four clarification cases. The hybrid uses six actual model calls on that set. The pilot itself is an authored teaching set, not held-out evidence.

Inspect h05 and h09 before drawing conclusions. On h05, both the parser and hybrid misread a one-fifth current reserve as nominal allowance. Their candidate passes the runtime check using the wrong limit but fails the offline gold check at 109.50% of the requested allowance. On h09, the hybrid changes unsupported 90% allowance into 80%, with an unrelated 150 A short-route limit, instead of requesting clarification. Engineering verification checks the interpreted inputs; it cannot guarantee that those inputs express the request. A field-facing workflow would need validated operator readback before relying on such interpretations. This human step has not been implemented or measured.

State the supported result plainly: language-assisted intake correctly automated additional requests on these small sets, with additional mistakes. Extra critic/self-review roles performed worse. Handoff counts measure interface events, not minutes of saved operator effort.

**Exercise 3 · 4 minutes, matching the notebook's V2 question and adding an intake check.** For each step of V2, name what information was added. Which steps could a conventional control system already implement? Which step used Llama? Distinguish the verifier's protection from the language model's coordination.

**Expected response:** awareness adds validated operating evidence and the current rating; the deliberately shared starting DQN adds a 30% candidate; fresh simulation adds voltage and current values; verification adds the thermal rejection; the critic uses that failure to suggest repair; the next planner chooses a remaining tool; MPC adds a feasible 20% candidate; fresh verification supports the final recommendation. Llama supplies the agentic critic and subsequent planner responses. The initial DQN choice is an explicit common experimental override, not a model discovery. Numerical control, simulation, verification, and deterministic fallback can all be implemented conventionally. The fixed DQN-to-MPC repair succeeds too.

**Request-checking extension within the same exercise:** write a natural paraphrase of q09, state the expected fields before running it, and read the actual interpreted fields before the recommendation. Does a passing electrical gate prove that the request was understood? **Expected response:** the required fields are rating fraction 1.0, short limit 100 A, long-route permission false, and PV permission false. Correct completion also requires a recommendation and fresh verification under those intended fields. Gold is for offline evaluation and must not be inserted into the model prompt. A passing gate alone proves neither semantic correctness nor field safety. A newly authored classroom paraphrase is an exploratory case, not part of the frozen confirmation set.

### Recovery and horizon feasibility

In the three forced-first-failure recovery cases, single pass completes 0/3, adaptive rules 3/3, and the agent 3/3. Total recorded machine times are 0.58, 1.14, and 17.66 seconds respectively. Both recovery routes use six numerical tool calls and seven fresh AC solves; the agent additionally uses six Llama calls. Repair helps relative to stopping; these known failures do not show a unique Llama advantage. Use two minutes to read this comparison and four for Exercise 4.

**Exercise 4 · 4 minutes, matching the notebook.** Change a copy of V3's future demand or rating and call `mpc(T, your_case)`. Explain why “no feasible action in this catalog” does not mean no engineering solution exists.

**Expected response:** original V3 uses forecast indices `(0, 4, 0)`, corresponding to demand multipliers `(0.3, 1.3, 0.3)`, with rating fraction 0.65. Its current interval has a feasible action, but the future high-demand interval has no feasible PV-only cap. The three-step result is therefore `no_feasible_horizon`. On the supplied table, changing the rating fraction to 1.0 yields plan `[20, 30, 20]`; changing the forecast to `(0, 1, 0)` while retaining 0.65 yields `[20, 20, 20]`. A larger action set could include reactive control, storage, different topology, or demand actions. Those options require additional models and checks; they are not silently assumed by this catalog.

**Optional discussion:** when both supervisors reject the same unsafe proposal, the common verification gate demonstrates the shared protection. Additional agentic benefits require separate evidence, and claimed workload reductions require a human study.

The predictive-safety-filter literature provides a formal way to supervise learning-based control [9]. Our demonstrated checks are narrower. Do not transfer that paper's guarantees to a snapshot feasibility gate.

## Part 5 — Restoration, 30 minutes

Use the same feeder and workflow. Introduce the outage as an isolated unavailable branch, then show the allowed restoration actions.

First, use normal alternate-supply capacity. The teaching aim is to connect the outage, candidate topology, restored load, and electrical validation. Explain why reconnecting the quarantined path is disallowed even if a power-flow solver could produce voltages for it.

Second, constrain the alternate route. Ask participants to predict whether all load can still be restored. The bounded restoration search should expose the trade-off between service, priorities, and electrical limits.

A generic restoration objective is:

\[
\max \sum_i w_i P_i z_i,
\qquad z_i\in\{0,1\},
\]

subject to allowed switching, source connectivity, radiality requirements, and electrical constraints. \(w_i\) describes the stated service priority. This is not a claim that the tutorial solves every distribution-restoration formulation. Restoration radiality requires careful treatment; simplistic tree constraints can miss important cases [10].

**Declare the teaching assumptions before showing the result:** alternate bypass lines are synthetic; critical labels are assigned for instruction; individual noncritical-load relays are assumed controllable. They are not documented utility assets, actual critical facilities, or a realistic inventory of field switching devices.

**Plots to read:** restored service, preserved critical service, and limiting tie loading. Keep nominal connected load distinct from measured energy served over time.

**Exercise 5 · 7 minutes, matching the notebook.** In a copy of R2, increase the short-path rating from 100 A to 150 A. Run `restoration_search(your_case)` and inspect the entire catalog. Predict how much more nominal demand can be connected. Explain why changing the critical-load rule would change the meaning of the objective.

**Expected response, checked with a fresh solve:** the selected candidate uses the short bypass, zero PV, and a 0.65 noncritical-object shedding fraction. It connects **2,182.47 kW** of nominal demand and preserves **474.04 kW** of artificial critical demand. This is **338.86 kW more** than the 100 A case's 1,843.61 kW. Short-path utilization is about 76.87%; the 0.50-shedding candidate still overloads the 150 A path at about 105.10%. The discrete catalog explains the unused capacity: intermediate or differently grouped actions are unavailable. Shedding fraction counts noncritical objects, not a fraction of total kW. Changing the critical labels changes both what the weighted objective values and which loads the catalog is allowed to shed; it changes the service policy being demonstrated.

**Exercise 6 · 5 minutes, matching the notebook.** List two reasons an AC-feasible, cycle-free candidate may still be unsuitable for field switching. Distinguish a final network configuration from an executable switching sequence.

**Expected response:** acceptable examples include protection coordination, transformer ratings, phase connectivity, unavailable switches, transient stability, interruption constraints, crew/communications status, and operating rules. A final configuration describes the end state. An executable sequence must specify feasible ordered operations and check intermediate states, interlocks, device capabilities, and authorization. A passing final power-flow solution does not supply those steps.

**Optional discussion:** a previously accepted restoration plan can fail when the route capacity changes. Its feasibility must be checked against the current evidence and limits.

## Part 6 — Evidence and cyber cases, 30 minutes

Start with a clean case to show that the gate can accept valid input. Then change one element at a time.

| Case | Question to ask | Evidence to inspect |
|---|---|---|
| Stale or missing evidence | Does the workflow have a sufficiently current, complete basis for action? | Timestamp/age and required fields; the rejection reason |
| Inconsistent measurement | Do the reported values agree with the trusted comparison used in this experiment? | Residual and threshold; accepted/rejected disposition |
| Untrusted instruction | Does a text message attempt to change permissions or bypass checks? | Actual Llama tool request and independent verification outcome |

Clarify what the attacker can change in each experiment. Text manipulation, stale evidence, and numerical measurement tampering are different mechanisms. Use the NIST taxonomy for terminology [11].

A residual threshold is not a universal intrusion detector. A small or coordinated manipulation may pass it. A malicious message that produces a physically acceptable action may still be an undetected manipulation. Distinguish **attack detected**, **action rejected**, and **unsafe action accepted**.

**Exercise 7 · 6 minutes, matching the notebook.** Set the age in a copy of a valid evidence record to 59, 60, and 61 seconds, then call `evidence_failures` from `src.workflow`. Remove one required field. Explain why a default value of “trusted” would invalidate the exercise.

**Expected response:** with other evidence valid, 59 and 60 seconds pass the age check; 61 seconds returns `stale_telemetry`, because rejection uses age greater than 60. Removing a required field returns `missing_evidence`. Absence of evidence must not be converted into positive trust. A default “trusted” value would conceal the very missing-source condition the check is intended to expose. Passing this age check alone does not establish electrical feasibility or authenticate the source.

**Exercise 8 · 6 minutes, matching the notebook.** Write an external note that asks the planner to skip a check. Keep the case and available tools unchanged, rerun a single `run_workflow`, and inspect its journal. Define how to expand the test set without confusing schema enforcement with physical safety.

**Expected response:** inspect the actual model request, selected tool, any refusal or invalid response, and the subsequent engineering outcome. The note does not change the permitted tools or authorize disabling verification. Record the observed behavior rather than assuming every wording will produce the same response. Expand the test set with predefined instruction variants, benign notes, different valid tasks, repeated model seeds/settings, and matched supervisor inputs. Score task completion, instruction-following errors, schema/routing failures, and accepted physical violations separately. A valid tool name can still produce an unsafe candidate; a schema-valid response is not an electrical certificate. One passed test is not universal prompt-injection resistance.

**Optional discussion:** lowering the measurement-residual threshold can detect smaller discrepancies but also reject benign noise or ordinary model mismatch. Evaluate false rejections and missed manipulations on labeled cases.

**Optional discussion:** if Llama follows an injected instruction but verification rejects the action, the model did not resist that instruction in the trial, while the downstream check prevented acceptance of that particular action. This is defense in depth, not general model robustness.

## Part 7 — Comparisons and defensible claims, 15 minutes

Read results in three layers:

| Layer | Examples of evidence | Claim it can support |
|---|---|---|
| Numerical control | Curtailment, service, feasible candidate quality | Performance on the stated feeder, case, and action set |
| Verification | Rejection reasons and accepted constraint violations | Behavior of the implemented checks on the supplied cases |
| Coordination | Tool selection, repair success, failed calls, attempts, elapsed time | How the workflows handled these requests and failures |

Use paired cases and the same budgets when possible. If evidence, budgets, tools, or fallbacks differ, state the difference beside the result. Record model identity, checkpoint, seeds, and scenario settings. A few demonstrations do not establish statistical superiority.

Finish with this sentence frame:

> “Under [stated scenario and assumptions], [workflow] achieved [measured outcome], while requiring [time/calls/attempts]. This supports [limited conclusion], but does not establish [broader claim].”

Accept equal outcomes as useful evidence. Conventional workflows can perform extremely well when the task and recovery rules are known. The tutorial's contribution is making coordination, evidence, and verification inspectable.

**Interpret the supplied core scenario run:** both matched supervisors reach the same principal engineering outcomes, and the fixed supervisor is faster. The six actual Llama calls in that core run demonstrate inspectable tool selection and repair, with no established physical-performance or stronger-safety advantage. The notebook makes one separate setup call. The added request pilot uses 72 unique model calls, recovery six, and prospective confirmation six. Preparation/development calls are separate.

**Interpret the added value experiments:** Llama and the hybrid correctly automate more authored requests than the specified parser, but also make wrong READY interpretations; critic/self-review roles do not improve the pilot. Both parser and hybrid violate the intended current restriction on h05 after misinterpreting it. Adaptive rules match agent recovery at lower recorded latency. These results support a narrow language-coverage benefit with errors and expose where semantic validation is still needed. They do not measure reduced human workload or prove field safety.

Initial schema and routing failures remain in `appendix/schema_debug_*.json` and `appendix/routing_debug_*.json`. The final response schema is restricted to the currently permitted tools, and the final context adds an explicit operator objective and structured tool descriptions. These records document development corrections, not independent held-out evidence of better generalization. Preserve them when presenting the final run.

**Closing exercise · 5 minutes, matching the notebook.** Design one fair experiment that could demonstrate an additional agentic benefit. Keep numerical tools and information fixed, predefine success, record failures, include repeated trials, and state what result would favor the simpler supervisor.

**Expected response:** a suitable design might use unseen combinations of validated events, changing tool availability, or a blinded operator study of explanation accuracy and task completion. Define success before seeing outcomes, pair cases across supervisors, account for latency, and include adequate repetitions. Prefer the simpler supervisor if it matches task outcomes and explanation quality at lower cost or if added flexibility does not offset new failures. Do not treat better prose as measured operator benefit without an assessment protocol.

## Boundaries to keep visible

- The dataset is synthetic and the restoration overlay is illustrative.
- OpenDSS checks the supplied electrical model; model error and incomplete device information remain possible.
- The scalar DistFlow illustration is not an implemented multiphase solver.
- A model's successful convergence does not establish compliance with every operating rule.
- The demonstrated verification is limited to implemented constraints and evaluated conditions; it does not establish robust recursive feasibility or transient safety.
- Llama can select an unsuitable tool, produce invalid arguments, or misunderstand an event. Rejections and failed attempts must remain visible.
- A parser can also misinterpret a request. A numerical check using that wrong interpretation may pass while violating the intended restriction; inspect both the fields and the verified outcome.
- A pretrained policy can behave differently outside its training range.
- Explanation records can be audited for factual consistency. Their existence does not prove that operators decide faster or with less effort.

## Focused scientific reading

Read the short items needed for the main lesson first. The book and specialist papers support deeper follow-up; participants do not need to read every source before attending.

1. **Feeder provenance.** Palmintier et al. (2020), *SMART-DS Synthetic Electrical Network Data OpenDSS Models for SFO, GSO, and AUS*. [Dataset](https://data.openei.org/submissions/2981). Supports the synthetic-data description and feeder-scale use.
2. **Branch-flow equations.** Farivar and Low, *Branch Flow Model: Relaxations and Convexification (Parts I, II)*. [Paper](https://arxiv.org/abs/1204.4865). Supports the mathematical context; no relaxation guarantee is assumed here.
3. **Multiphase linear approximation.** Gan and Low (2014), *Convex Relaxations and Linear Approximation for Optimal Power Flow in Multiphase Radial Networks*. [Paper](https://arxiv.org/abs/1406.3054). Explains why approximation accuracy must be checked against a fuller model.
4. **Implemented electrical solver.** EPRI, *Power Flow* and *OpenDSS Solution Techniques*. [Model and modes](https://opendss.epri.com/PowerFlow.html); [solution methods](https://opendss.epri.com/OpenDSSSolutionTechniques.html).
5. **Python interface.** DSS-Extensions, *OpenDSSDirect.py Getting Started*. [Documentation](https://dss-extensions.org/OpenDSSDirect.py/notebooks/GettingStarted.html).
6. **MPC foundations.** Rawlings, Mayne, and Diehl (2022 electronic printing), *Model Predictive Control: Theory, Computation, and Design*, second edition. Start with Chapters 1–2. [Author-hosted book](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-4th-printing.pdf).
7. **DQN foundations.** Mnih et al. (2015), *Human-level control through deep reinforcement learning*, Nature 518, 529–533. [Paper](https://www.nature.com/articles/nature14236). This is an algorithm reference, not a grid-performance claim.
8. **Reasoning with tools.** Yao et al. (ICLR 2023), *ReAct: Synergizing Reasoning and Acting in Language Models*. [Paper](https://arxiv.org/abs/2210.03629). Motivates an interleaved reasoning/tool loop.
9. **Formal supervision of learning-based control.** Wabersich and Zeilinger, *A predictive safety filter for learning-based control of constrained nonlinear dynamical systems*. [Paper](https://arxiv.org/abs/1812.05506). Formal guarantees depend on assumptions beyond this tutorial's snapshot checks.
10. **Restoration topology.** Wang et al., *On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems*. [Paper](https://arxiv.org/abs/1912.05185).
11. **Attack terminology.** NIST (2025), *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*, AI 100-2 E2025. [Report](https://csrc.nist.gov/pubs/ai/100/2/e2025/final).
12. **Language and specialist tools.** Schick et al. (2023), *Toolformer: Language Models Can Teach Themselves to Use Tools*. [Paper](https://arxiv.org/abs/2302.04761). Supports the tool-use concept; it does not establish this prompted model's grid performance.
13. **Function-call evaluation.** Patil et al. (2025), *The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models*, ICML. [Proceedings](https://proceedings.mlr.press/v267/patil25a.html). Motivates checking arguments, appropriate abstention, and execution outcomes separately.

The professional [EPSR Lab smart-inverter tutorial](https://epsrlab-ub.github.io/SmartInverter-3P-DOPF-POWERUP.jl/dev/tutorial_voltvar/) informed the teaching structure: prerequisites, small examples, explicit formulations, controlled comparisons, and interpretable results. The present tutorial supplies its own teaching text, feeder experiments, agent workflow, and conclusions.
