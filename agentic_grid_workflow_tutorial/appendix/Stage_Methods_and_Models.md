# Stage methods, two electrical models, and operator readback

**Scope of this record:** the equations and results below document the original restricted workflow. For the general three-use-case OPF/MILP/WLS formulations, see [General Optimization Formulations](General_Optimization_Formulations.md). The separate [standard-method notebook](../Standard_Formulations.ipynb) runs continuous P/Q optimization and compact MILP/WLS experiments. Those additions do not relabel or overwrite the frozen studies.


This extension makes every stage inspectable: **input → named method → actual response → check → next step**. It compares complete workflows using two electrical prediction models on the same synthetic Greensboro feeder. MPC and DQN remain numerical tools, while Llama supplies bounded orchestration and short, recorded explanations.

This note describes the implemented stages in [stage_workflow.py](../src/stage_workflow.py), the independent electrical model, and operator readback. The frozen request, recovery, and confirmation studies remain separate experiments and retain their original results. The new stage-run findings below are identified separately.

## One stage record, with a clear source for every response

Display the same small card for every stage: stage name; named method; relevant inputs; numerical or structured result; status and failure reason; model scope; and a reference to the underlying record. Show elapsed time where recorded, without inventing stage timings from the total. Label the response source as **numerical result**, **deterministic rule**, **actual Llama output**, **local failure fallback**, **recorded replay**, or **operator input**.

Show a concise Llama rationale as the model's stated reason. It is not an independent proof of the calculation or a faithful account of hidden reasoning. A formatted sentence assembled from metrics is a deterministic summary, even when the card is called “Explanation.” A skipped Llama call must be shown as skipped, not replaced by model-like text.

The implemented live calls occur in **Planning**, **Recovery when needed**, and **Explanation**. Awareness, numerical proposal, simulation, and verification are deterministic responsibilities with visible responses. Calling them workflow stages does not mean that each secretly invokes a language model.

| Stage | Named numerical or deterministic method | Llama's bounded contribution | Response the audience should see |
|---|---|---|---|
| Awareness | Required-field, finite-value, timestamp, and topology checks; aggregate minimum/maximum-voltage residual test | No separate Llama call; the validated evidence feeds subsequent stages | Reported/reference voltage extrema, residual and threshold, evidence age, topology match, and PASS or REVIEW |
| Planning | Three-step finite-action MPC solved by dynamic programming, or bounded restoration enumeration | Choose DRL_THEN_MPC, MPC_ONLY, or REVIEW for voltage; RESTORATION_PLAN or REVIEW for restoration; state a brief reason | Forecast, constraints, numerical plan/candidate, objective, route choice, and response source |
| Execution proposal | Greedy DQN action-value maximization using the supplied checkpoint, or extraction of the numerical plan's candidate | No separate Llama call; the earlier planner chooses the route | All action scores or the MPC first move, proposed cap, checkpoint identity, and “proposal only” status |
| Simulation | Fresh selected-backend solve: nonlinear OpenDSS or the independent three-phase LinDistFlow MV solver | No separate Llama call; returned values cannot be replaced by narrative | Model voltage range, line utilization, convergence/validity diagnostics, and model coverage |
| Verification | Action-scope checks, selected-model electrical constraints, feasible MPC horizon continuation, and objective-gap tolerance | No separate Llama call; a later critic cannot waive a rejection or change its threshold | Failure list, objective gap, model coverage warning, and final gate verdict; continuation values and optimum remain in the numerical plan |
| Recovery | Finite-state fallback with bounded attempts: rejected DQN proposal → MPC first move, otherwise stop as specified | Optional actual critic response consumes the failure evidence; it cannot authorize bypassing checks | Rejection reason, remaining attempt budget, permitted next tool, new candidate, and its new verification result |
| Explanation | Deterministic metric card linked to the immutable recommendation and its full trace | Actual operator-focus category and short reason, displayed separately from computed metrics | Proposed action, scope, constraints, rejected attempts, unresolved limitations, and the recorded Llama wording |
| Operator acknowledgment | Local form validation and a readback record bound to the recommendation hash | No model-generated acknowledgment | Operator name, interpreted-limit/model-scope readback checkboxes, recommendation identity, and acknowledgment status |

The DQN does not operate equipment. “Execution” means producing and evaluating a proposed action in this tutorial. A recommendation becomes acknowledged only through the local operator interaction, and acknowledgment still does not send a command to physical equipment.

## Awareness: evidence screening is not state estimation

The implemented awareness fixture takes the selected model's minimum and maximum bus-voltage magnitudes, synthesizes the corresponding reported values, and compares these two aggregate sensors with their reference. It also checks evidence age and topology identity. This is not a per-phase sensor array. The bias case subtracts 0.03 p.u. from both reported extrema; the stale case sets age to 180 seconds. The normal age is two seconds.

A residual such as

\[
r_\infty=\max_{k\in\{\min,\max\}}
\left|V^{\mathrm{reported}}_{k}-V^{\mathrm{reference}}_{k}\right|
\]

is the implemented numerical consistency statistic. A residual greater than 0.01 p.u. is rejected, as is age greater than 60 seconds, topology mismatch, or malformed/nonfinite evidence. Zero residual against the same model-derived fixture provides no independent measurement-validation evidence. The two model routes generate their own awareness references, so this comparison does not use one common field-sensor dataset. Do not claim a calibrated false-alarm probability or per-phase attack-detection rate.

This is **evidence screening**, not weighted least-squares distribution-state estimation. A genuine estimator would require a measurement function, sensor uncertainty model, observability assumptions, and an implemented estimation problem, for example \(\min_x(z-h(x))^T R^{-1}(z-h(x))\). A solved power flow using known synthetic inputs does not become a state estimator merely because it produces voltages. Schweppe and Wildes' foundational state-estimation formulation supplies the distinction. [Schweppe and Wildes, 1970](https://ieeexplore.ieee.org/abstract/document/4074022).

Residual tests also do not detect every malicious measurement. Coordinated false-data attacks can evade conventional bad-data tests under their assumed models; the tutorial's visible attack cases demonstrate specific checks, not universal intrusion detection. [Liu, Ning, and Reiter, 2009](https://cse.usf.edu/~yliu21/webresources/?n=pdf%2Fccs09-PowerGrids.pdf).

## Planning and proposal: MPC evaluates, DQN proposes

Use the same three-step forecast, action catalog, previous action, normalized PV benefit, movement penalty, and discount factor for both prediction models. The finite-action dynamic program computes an optimum for that stated discrete problem. It does not solve a continuous AC OPF or establish feasibility beyond the supplied forecast. Each stage case demonstrates the planned first move; it does not run a dynamical closed-loop plant. Replanning after applying the first move is the broader MPC mechanism. [Rawlings, Mayne, and Diehl, 2022 printing](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-4th-printing.pdf).

For restoration, the extension enumerates the same stated bypass/shedding catalog in each model and maximizes served nominal kW plus nine times critical served nominal kW. Equal objectives retain the first catalog entry; the extension does not use losses with different physical coverage to break cross-model ties. This differs from the earlier frozen restoration tool's loss tie-break and is declared here rather than retroactively changing that study.

The DQN proposes

\[
a_{\mathrm{DQN}}=\arg\max_{a\in\mathcal A}Q_\theta(o,a).
\]

Its scores are learned predictions, not measured electrical feasibility. Reuse the original pretrained checkpoint across both model workflows to avoid changing the learning algorithm and electrical model at once. Identify its original training environment; reusing it with the linear model is not evidence of retraining or of broad model-transfer capability. The original DQN paper supports the algorithm, not a grid-safety guarantee. [Mnih et al., 2015](https://www.nature.com/articles/nature14236).

The additional MPC consistency check asks whether a proposed first move admits a feasible continuation over the same horizon. Let \(J^*\) be the model's optimal horizon value and \(J(a)\) the best feasible continuation with first action fixed to \(a\). Require a finite \(J(a)\) and

\[
J^*-J(a)\leq 0.02.
\]

The tolerance is in the tutorial's normalized objective units. It is a stated acceptance preference, not a 2% physical margin or a formal safety bound. Show electrical rejection and objective-gap rejection separately. A DQN action may be electrically feasible yet fail the planning-quality check.

Call this a **deterministic proposal gate with MPC fallback**. The word “shielded” describes the implemented rejection mechanism, not a guarantee that the DQN itself is safe. Formal predictive safety-filter results depend on assumptions and constructions beyond these simulated checks. [Wabersich and Zeilinger, 2021](https://arxiv.org/abs/1812.05506).

## Two complete workflows with different physical coverage

| Property | OpenDSS workflow | Three-phase LinDistFlow workflow |
|---|---|---|
| Network source | Included synthetic Greensboro feeder | Same feeder's exported MV phase network |
| Electrical calculation | Nonlinear multiphase circuit solution | Independent linear calculation after static export |
| Phase structure | Original modeled phase/device connections | Actual 1- and 3-phase MV lines in this export, retaining mutual impedance terms |
| LV and service transformers | Retained in the supplied electrical model | LV load/PV powers aggregated to mapped transformer-primary phases; service transformers treated as ideal and lossless |
| Voltage claim | Evaluated full-feeder bus/phase voltages | MV bus/phase voltages only |
| Line-current claim | Evaluated currents on modeled lines | Approximate currents on retained MV lines |
| Completion label | Recommendation under the evaluated OpenDSS model and checks | Provisional recommendation under the stated MV approximation and checks |
| OpenDSS audit of a linear recommendation | Applicable reference calculation | Separate full-feeder audit when OpenDSS is available; never silently implied by a linear-only run |

Both routes cover awareness through acknowledgment. “Complete workflow” describes the process; it does not mean the reduced model predicts every device in the original circuit. A linear-only run must remain visibly provisional with respect to omitted LV voltages, service-transformer effects, and unimplemented constraints.

OpenDSS normally solves the unbalanced circuit using iterative current injection. Numerical convergence and compliance with the tutorial's constraints are separate outcomes. OpenDSS is the higher-detail simulation reference here, not ground truth about a real feeder. [EPRI power flow](https://opendss.epri.com/PowerFlow.html), [solution techniques](https://opendss.epri.com/OpenDSSSolutionTechniques.html).

The linear model is genuinely multiphase when it retains phase-specific complex powers and the off-diagonal terms of the line impedance matrix. One physical-unit form of the squared-voltage approximation is

\[
|V_{j\phi}|^2\approx |V_{i\phi}|^2
-2\Re\!\left[
\overline{V^0_\phi}\sum_{\psi\in\Phi_{ij}}
Z_{ij,\phi\psi}\,
\overline{\frac{S_{ij,\psi}}{V^0_\psi}}
\right].
\]

Here \(S_{ij,\psi}=P_{ij,\psi}+jQ_{ij,\psi}\) is downstream phase power; \(Z_{ij}\) includes mutual impedances; and \(V^0\) contains fixed nominal phase phasors. A backward sweep accumulates downstream powers, and a forward sweep propagates squared voltages. Use volts, watts, vars, and ohms consistently. The simplified branch-current estimate uses the same nominal phasors. Loss terms and voltage-dependent changes in those phasors are neglected. This differs from three independent scalar voltage-drop calculations. Multiphase linear-approximation literature motivates the approach but does not transfer its reported accuracy to this feeder or reduction. [Gan and Low, 2014](https://arxiv.org/abs/1406.3054).

The implementation must expose phase mapping, disconnected components, unsupported topology, and invalid squared voltages as diagnostics. An ambiguous primary-phase mapping or unsupported topology should not be replaced by an unexplained numerical result. Losses omitted by the approximation must not be presented as measured zero physical losses.

The supplied export contains 453 baseline energized MV buses, 599 MV bus/phase values, and 452 original MV branches (380 one-phase and 72 three-phase), plus the two optional teaching ties. The aggregation maps 2,173 loads, 930 PV systems, and 436 idle storage devices through 258 ideal service-transformer interfaces. The independent solver retains declared PV power factors and inverter kvar/kVA clipping, nominal storage standby consumption, the fixed capacitor, and nominal-voltage line shunts. It uses a balanced 1.03 p.u. source reference for approximate branch currents. These retained details improve fidelity within the chosen model; they do not restore the omitted LV circuit or transformer losses. The static export contains equipment parameters, not fitted AC sensitivities or cached AC operating-point solutions.

## Compare models and orchestrators separately

Use a 2 × 2 design: electrical backend **OpenDSS / LinDistFlow MV**, and supervisor **adaptive fixed rules / actual Llama**. Pair the operating-case definitions and hold forecasts, action catalog, objective, checkpoint, tolerances, and attempt budget fixed. Each backend generates its own synthetic awareness extrema, as disclosed above. Record any extra model calls or reference audits separately. If the DQN is rejected in both routes, both supervisors must have the same permitted MPC fallback.

For model accuracy, compare matched **MV bus/phase pairs** and aligned MV lines under the same candidate, injections, source assumptions, and topology. Report phase-voltage MAE and maximum absolute error in p.u.; current error in amperes or percentage points of the same rating; and disagreement in the gate verdict. Do not compare full-feeder minimum voltage to MV-only minimum voltage as though they covered the same nodes.

For workflow performance, report proposed/accepted caps, service metric where relevant, task status, rejections, recovery attempts, model/tool calls, and elapsed time. Separate model construction, reusable prediction-table preparation, live inference, fresh solves, and optional AC audits. One hardware run gives descriptive timings, not statistical speedup evidence.

Inspect both kinds of disagreement: a linear pass followed by an AC failure, and a linear rejection of an AC-feasible candidate. First distinguish **coverage differences** from **approximation error**. A full-feeder AC failure caused solely by an LV limit that the MV model omits is a scope limitation; it does not demonstrate poor linear accuracy on their common MV network. Differences at the same modeled bus/phase or line can instead reveal approximation error or differing model assumptions. If a margin is later tuned using these results, declare it as tuning and evaluate it on separate cases.

Llama's interleaved use of tool observations follows the general motivation of ReAct; it does not establish that more roles outperform the matched adaptive supervisor. The earlier frozen studies already show why that distinction matters. [Yao et al., 2023](https://arxiv.org/abs/2210.03629).

## Recorded stage-run finding: repair can be declined

The completed [model_workflow.json](../results/model_workflow.json) contains 32 runs: eight cases × two electrical models × two supervisors, with 26 actual Llama calls. In V2, the common starting DQN proposes a 30% cap. The OpenDSS gate rejects it for thermal limits and lack of a feasible horizon continuation. The MV-only gate rejects it for an MPC value gap. A feasible MPC plan is already supplied in both contexts.

The fixed supervisor proceeds to the MPC first move: 20% with OpenDSS and 100% within the MV model. The actual Llama Recovery response chooses REVIEW in both contexts, so the agentic route makes no recommendation. This is unnecessary escalation relative to the available plan and the matched fixed rule. It demonstrates the numerical gate and a limitation of model-mediated recovery; it is not successful agentic repair.

Both supervisors complete R1 and R2 with the same respective actions: short bypass with 20% PV and no shedding for R1; short bypass with zero PV and a 0.75 noncritical shedding fraction for R2. These are nominal service results under the stated synthetic restoration catalog. Model agreement does not establish field switching feasibility.

The earlier three-case recovery experiment reported 3/3 completion for both adaptive rules and its agent loop. That experiment uses a different prompt, protocol, and failure set. Preserve both findings; do not combine them into a single recovery rate or substitute one protocol's favorable result for the new V2 outcome.

## Final model comparison and separate AC audit

The following tables are derived from [model_comparison.json](../results/model_comparison.json) and [model_workflow_reviewed.json](../results/model_workflow_reviewed.json). Each workflow is evaluated on the same eight named cases. A recommendation count is not a task-success rate: C1 and C2 appropriately stop for stale or biased evidence, and the OpenDSS V3 problem has no feasible plan in the stated catalog.

| Prediction model and supervisor | Recommendations in model scope / 8 | Separate full-feeder AC passes / recommendations | Actual Llama calls | Total workflow time, s |
|---|---:|---:|---:|---:|
| OpenDSS, adaptive fixed | 5 | 5/5 | 0 | 4.04 |
| OpenDSS, agentic | 4 | 4/4 | 13 | 47.95 |
| LinDistFlow MV, adaptive fixed | 6 | 2/6 | 0 | 1.42 |
| LinDistFlow MV, agentic | 5 | 2/5 | 13 | 38.42 |

The 80 prediction-table setup solves are separate: 40 OpenDSS solves took 5.63 seconds and 40 linear solves took 1.73 seconds on the preparation machine. Workflow times above exclude these setup costs and the offline AC audits. These are descriptive totals from one fixed-order local run, not hardware-independent timings or statistical speedup estimates.

Every rejected linear recommendation is classified **LV_ONLY** by the separate AC audit: its voltage/current violations occur on the secondary network excluded from the linear model. The audit does not repair these recommendations; it labels them for review. The model-limited route can run without OpenDSS, but without a separately run audit it cannot claim these full-feeder checks.

The common-domain comparison matches 599 energized MV bus/phase voltage magnitudes and 452 energized MV lines per evaluated candidate. The current statistic is the maximum terminal/conductor current for each matched line; it is not a phase-by-phase current-error measure. The table shows the distinct sampled linear recommendations, using fixed-supervisor rows where needed; the other supervisor's matching candidates are duplicate operating points rather than independent repetitions.

| Linear recommendation | Cap | Maximum absolute MV voltage error, p.u. | Mean absolute MV voltage error, p.u. | Maximum absolute aligned-line current error, A | Full-feeder AC result |
|---|---:|---:|---:|---:|---|
| V1, V2, C3 nominal-load candidate | 100% | 0.001728 | 0.000608 | 7.381 | LV-only failures; review |
| V3 first move at 0.3 demand | 40% | 0.000501 | 0.000187 | 4.393 | LV-only failures; review |
| R1 short bypass, no shedding | 20% | 0.000796 | 0.000683 | 5.626 | Passes implemented AC checks |
| R2 short bypass, 0.75 noncritical shedding | 0% | 0.000420 | 0.000303 | 3.688 | Passes implemented AC checks |

For example, the 100% PV candidate has predicted MV maximum voltage 1.04735 p.u., while the full-feeder AC maximum is 1.10748 p.u. Those maxima have different coverage and are not the model-error metric. The aligned MV maximum error is 0.001728 p.u.; the much larger full-feeder maximum comes from the omitted LV network. Rating fractions still differ between V1/V2, so their current-utilization percentages should not be treated as identical even though physical currents and the shared candidate coincide.

R1 connects 4,747.47 kW of nominal demand and R2 connects 1,843.61 kW, under both supervisors and both models. Their matching actions pass the separate AC checks. These are nominal connected-demand figures, not energy or measured delivered power. The sampled maximum voltage-error range, 0.000420–0.001728 p.u., is not a general accuracy guarantee; it applies to these aligned operating points and modeling assumptions.

## Dashboard acknowledgment is a readback, not a control command

The dashboard should first show the interpreted request, proposal, selected model and its coverage, verification details, repair history, and any separate AC-audit result. Display deterministic metrics independently from the actual Llama focus and reason fields. Distinguish “reference audit not run” from “reference audit passed.”

The local acknowledgment form records the operator's name and explicit readback of the interpreted restrictions and model scope. Bind this record to an immutable recommendation hash. Changing the request, model, candidate, or constraints requires a new acknowledgment; an old checked box cannot acknowledge a different result. Retain the original recommendation status after acknowledgment: a provisional MV-only result remains provisional.

This demonstrates a review interaction and traceable local record. It does not authenticate a field operator, prove comprehension, measure workload, satisfy a utility switching procedure, or authorize physical operation. A future human study would need predefined comprehension/error measures. NIST AI RMF supports defining responsibilities and oversight in human–AI configurations; it does not validate this checkbox interface as a safety mechanism. [Tabassi, 2023, AI RMF 1.0, Appendix C](https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/).

## Stage worksheet

Complete one row per stage for a single voltage case, then repeat with the other model. Copy evidence from the visible record before writing an interpretation.

| Stage | Record from the experiment | Explain in one sentence |
|---|---|---|
| Awareness | Age, aggregate extrema residual, topology result, threshold | Why can the workflow continue or why must it stop? |
| Planning | Forecast, MPC caps/value, Llama route and reason source | Which calculation sets the control objective? |
| Proposal | DQN Q-values/selected cap or MPC first move | Why is a proposal not yet an accepted action? |
| Simulation | Model scope, phase-voltage range, maximum line loading | Which physical quantities does this model omit? |
| Verification | Each verdict, horizon continuation, value gap | Which specific check accepted or rejected the proposal? |
| Recovery | Failed attempt, next allowed tool, final verdict | Could the supplied adaptive rule perform the same recovery? |
| Explanation | Metric card and actual Llama qualitative response | Which facts are calculated and which words are model-generated? |
| Acknowledgment | Recommendation identity and completed readback | What has the operator acknowledged, and what has not been authorized? |

**Expected distinctions:** awareness screens supplied evidence; MPC computes the stated horizon plan; DQN supplies a learned proposal; simulation predicts within a model's scope; verification applies explicit checks; recovery can be deterministic or Llama-coordinated; explanation must preserve result provenance; acknowledgment records readback of one unchanged simulation recommendation.

## Instructor plan: preserve the 180-minute workshop

Use this as a suggested revision of the existing route; it does not add a second three-hour class. Run one representative dual-model case live, then use recorded results for repeated comparisons. Keep derivation details and regeneration of the complete experiment set in preparation or the appendix.

| Clock | Minutes | Activity |
|---|---:|---|
| 00:00–00:15 | 15 | Setup, objectives, live/replay labels, and scope of the dashboard |
| 00:15–00:35 | 20 | Same feeder, two model scopes; phase network and aggregate residual illustration |
| 00:35–01:05 | 30 | MPC and DQN; trace one case through both models and fill the worksheet |
| 01:05–01:35 | 30 | Stage responses and recovery, retaining the 15-minute language-intake value experiment |
| 01:35–01:45 | 10 | Break |
| 01:45–02:15 | 30 | Two restoration variants and shared-scope model comparisons |
| 02:15–02:45 | 30 | Evidence/cyber cases; distinguish numerical rejection from semantic misunderstanding |
| 02:45–03:00 | 15 | Five minutes for paired results, five for dashboard readback, five for the closing claim exercise |

For the closing exercise, ask participants to complete: “On these cases, method ___ changed ___, while the common numerical tool/check provided ___. The result remains limited by ___.” A defensible answer may report equal outcomes, slower Llama coordination, approximation error, or added language coverage with mistakes. The tutorial should make those findings understandable rather than requiring an agentic advantage in every stage.

## Regression checks versus experimental evidence

Run `python appendix/test_stages.py` to check the stage contracts without live model calls or OpenDSS. The tests compare dynamic programming with exhaustive horizon enumeration, verify conditional first-action values and future infeasibility, compare the transferred DQN's outputs with its original forward implementation, and exercise evidence, schema, scope, objective-gap, and fallback failures. Explicit numerical/model test doubles make these software checks deterministic; they are not empirical Llama-quality, power-flow-accuracy, or safety results.
