# From the proposal to an executable five-stage workflow

This coverage audit uses the supplied **Tutorial Proposal for IEEE SmartGridComm 2026**, especially the five-module table and feedback diagram on page 2. The proposal is the design reference. Its descriptions of intended capabilities are not evidence that those capabilities have already been executed.

The original main notebooks and their saved studies remain useful numerical lessons. They expose eight responsibilities: Awareness, Planning, Execution proposal, Simulation, Verification, Recovery, Explanation, and Operator acknowledgment. However, their bounded Recovery role primarily selects an already computed fallback. Their Explanation role chooses a review focus. Those mechanisms alone do **not** implement the proposal's fifth module: an LLM optimizer that consumes simulation and verification feedback, generates or revises candidates, and compares their quality.

The new `Proposal_Complete_Workflow.ipynb` uses the proposal's five stages as the visible execution contract. The additional engineering responsibilities fit inside or after those stages; they are not replacements for the optimizer.

## Five stages, with an observable handoff

| Proposal stage | Existing foundation | Required executable evidence in the complete workflow | Boundary to retain |
|---|---|---|---|
| **1. Awareness** | Structured request and provenance checks; synthetic case definitions; separate WLS/residual lessons | A case record with the objective, model scope, topology, availability, limits, evidence trust, and supported actions | A model-generated state is not independently validated telemetry. A consistency test is not general attack detection. |
| **2. Planning** | Continuous SAC proposal and numerical MPC; restoration MILP and catalog; constrained DC redispatch | One or more bounded candidate actions with a named generating method and a stable identity | A candidate is a proposal. Choosing a tool, producing a control, and accepting that control are different operations. |
| **3. Simulation** | Fresh OpenDSS and Python three-phase LinDistFlow; compact DC examples | A fresh model result tied to the candidate, case, and backend, including convergence and relevant electrical quantities | A simulator predicts within its modeled scope; it does not certify field behavior. |
| **4. Verification** | Deterministic constraints, authorized-action checks, failure lists, model warnings | Explicit checks against unchanged request limits, device bounds, topology/policy restrictions, and simulation validity | Llama cannot waive a failed check, redefine the request, or substitute its own claim for numerical evidence. |
| **5. LLM optimizer** | Previously only a bounded fallback choice and explanation focus | Actual model feedback and revised/selected candidate proposals; repeated simulation and verification; feasible-candidate comparison; recorded stop reason | Verifier-guided refinement is a bounded search. It need not beat a conventional optimizer, and it has no global-optimum guarantee. |

**Operator handoff follows these stages.** The operator sees the selected candidate, alternatives, rejected attempts, modeled limits, actual returned Llama explanations, cost/latency, and unresolved scope. Acknowledgment records readback of this particular recommendation; it does not dispatch equipment.

Use the same five labels in the diagrams, notebook traces, and result tables. A helpful slide shows one input card, five numbered boxes, a feedback arrow from verification to the optimizer, a return arrow to simulation, and a final human-review card. The numerical methods belong inside the boxes rather than replacing the stage names.

## Teach method families before algorithm names

| Family | How it proposes a decision | Tutorial instance | Essential limitation |
|---|---|---|---|
| **Model-based control or optimization** | Uses an explicit predictive/constraint model to compare candidate actions | Receding-horizon MPC for inverter P/Q; MILP or enumerated restoration actions; constrained redispatch using an estimate | Model mismatch, omitted equipment, forecast errors, and solver limitations remain. A feasible plan is not an unconditional safety proof. |
| **Model-free policy learning** | Learns a policy or action values from experience; the deployed policy maps its observation to an action | Continuous SAC actor for voltage support; PPO is a discussed alternative, not an executed controller in these records | Training cost and distribution shift matter. A policy proposal has no automatic constraint guarantee. |
| **Agentic coordination and refinement** | Uses task context and returned tool evidence to organize a bounded search and communicate the result | Local Llama proposes allowed refinements and returns a short reason; tools simulate and gate each candidate | More coordination can add latency and errors. Benefit must be measured against the same available numerical tools and budget. |

Model-free does **not** mean that no simulator was used during training. An SAC policy can learn from a simulated environment and still be model-free in the reinforcement-learning sense: its policy update and online action do not solve a learned or explicit transition model. Conversely, training a neural network does not by itself make a controller model-free. State explicitly whether the online decision uses a predictor or optimizer. The tutorial's fitted training surrogate is an environment for generating SAC experience, not an MPC label source. [Haarnoja et al., SAC, ICML 2018](https://proceedings.mlr.press/v80/haarnoja18b.html).

MPC predicts over a horizon, solves a constrained problem, and proposes the first move; a deployed receding-horizon controller repeats that procedure after new observations. A single first-action notebook experiment demonstrates the optimization step and gate, not a closed-loop stability result. [Rawlings, Mayne, and Diehl, author-hosted MPC textbook](https://sites.engineering.ucsb.edu/~jbraw/mpc/).

SAC is an off-policy maximum-entropy actor-critic method used here for continuous actions. PPO is an on-policy policy-gradient alternative with a surrogate objective; an audience can discuss its trade-offs without implying that this tutorial trained or compared a PPO policy. [SAC paper](https://proceedings.mlr.press/v80/haarnoja18b.html), [Schulman et al., PPO, 2017](https://arxiv.org/abs/1707.06347).

## What the optimizer literature contributes

These primary sources were checked on **2026-09-27**. Their mechanisms motivate the tutorial; their benchmark scores are not evidence about this feeder.

| Method | Transferable mechanism | What the tutorial must show before using the label |
|---|---|---|
| **ReAct** | Interleave permitted actions with returned observations so later decisions can use external evidence | A model call actually receives earlier tool results and chooses a subsequent allowed operation. [Yao et al., ICLR 2023](https://arxiv.org/abs/2210.03629). |
| **Self-Refine** | Generate an output, produce feedback, and revise iteratively without retraining the base model | A revision step is visible. Here the physical verifier supplies external evidence, so call the adaptation *verifier-guided refinement* rather than claiming a reproduction of pure self-feedback. [Madaan et al., NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html). |
| **OPRO** | Supply previously proposed solutions and their evaluated values to the next proposal step | A bounded action search actually conditions on evaluated candidates. If candidate values are computed by numerical tools, label those tools as the source of the scores. This is an OPRO-inspired pattern, not a reproduction of its prompt-optimization benchmark. [Yang et al., 2023 preprint](https://arxiv.org/abs/2309.03409). |
| **Reflexion** | Retain feedback in textual memory for subsequent trials without updating model weights | Persistent cross-trial reflective memory would need to be implemented to claim Reflexion itself. A one-run critique log is only a related feedback mechanism. [Shinn et al., 2023](https://arxiv.org/abs/2303.11366). |
| **Best-of-N and simulation-informed ranking** | Compare several proposals using an explicit evaluator and select an acceptable candidate | Declare N, candidate sources, retry budget, constraint handling, score direction, and ties. Llama's proposed order and the deterministic numerical ranking must remain distinguishable. The generator–verifier pattern has a primary example in [Cobbe et al., 2021](https://arxiv.org/abs/2110.14168); that work trains a learned math verifier, whereas this tutorial uses explicit electrical checks. |

Returned `reason` or critique text is the model's **stated explanation**. It is not an independent mathematical proof, and it should not be presented as hidden internal reasoning. Multiple prompted roles using one local Llama model are a sequential role-based architecture, not evidence of independent expert consensus.

## Fair comparisons and claims

Use short tick tables for mechanism coverage: proposed candidates, physical simulation, constraint gate, feedback refinement, alternative ranking, and human readback. A tick means that a mechanism executed or is available in the named route. It does not mean superior accuracy or utility readiness.

Keep capability and performance comparisons separate. A conventional numerical optimizer also searches, ranks alternatives, checks constraints, and can expose diagnostics. Comparing an unchecked first guess with a fully verified agent loop demonstrates the value of checking, but does not isolate the value of Llama. Include a deterministic route with the same candidate tools, bounds, observations, model, and search budget whenever making an agent-specific claim.

Report case completion, all rejected attempts, objective values, remaining violations, model solves, actual Llama calls, and elapsed time separately. Declare whether model preparation, training, MPC preparation, audit solves, and operator interaction are inside the timing interval. One local run is descriptive evidence, not a latency distribution or a hardware-independent benchmark. Do not hide ties or a worse agentic outcome.

Cross-model comparisons require matched coverage. The Python three-phase LinDistFlow model retains MV phases and aggregates the downstream LV system. OpenDSS contains more of the feeder. Different full-feeder and MV-only extrema are not an aligned model-error statistic. Show common-MV discrepancies separately from failures on omitted LV equipment. A passing MV-only result remains provisional with respect to omitted constraints.

The older four-bus WLS cyber lesson, restoration MILP, feeder restoration catalog, continuous SAC/MPC records, and language-confirmation set use different protocols. Keep their numerical findings and timings identified separately from the new five-stage experiments.

## Proposal scope that must remain explicit

| Proposal item | Honest implementation boundary |
|---|---|
| Five-stage propose–simulate–verify–refine loop | Executed in the new complete-workflow lesson: six paired settings and one additional Qwen portability example; see the audited results below. |
| Open-weight Llama and Qwen examples | Actual `llama3.1:8b` calls run all six settings. Actual `qwen2.5:7b-instruct` calls run one MV-voltage portability example. This is not a multi-model benchmark. |
| Cloud/GPU-backed environment | Local Jupyter and Ollama execution is available. It is not evidence of a deployed cloud teaching service or GPU benchmark. |
| Telemetry fusion and forecasts | Synthetic operating conditions and declared forecasts are provided; no live SCADA/ADMS connection or calibrated field forecasting system is established. |
| Battery actions | Network data may contain storage devices, but active battery scheduling, state-of-charge trajectories, and storage-control learning are outside the demonstrated controller. |
| Restoration switching sequences | Catalog/MILP topology decisions and any explicit intermediate-state checks must be distinguished from a utility switching procedure. Protection, synchronization, crews, and switching transients are not implied. |
| Attack-aware safety | The implemented attacks and trust assumptions define the claim. Passing a residual test cannot establish that all readings are authentic. |
| Operator deployment | A local advisory review/readback interface is demonstrated. Authentication, utility change control, command execution, and an operator usability study are outside this evidence. |

The proposal's detailed eight-part outline totals 180 minutes. A larger slide library should preserve a clearly marked three-hour route, with optional mathematical and code detail outside that route. The new optimizer stage should be taught before the three use cases, then revisited with case-specific inputs, methods, outputs, and returned explanations.

## Validation checklist for the completed extension

1. Each executed case contains all five named stage records, including an actual Llama optimizer call or an explicitly labeled failure; absent calls must not be filled with fabricated model responses.
2. Candidate identity, case, backend, immutable limits, simulation result, and gate result stay bound together. A stale passing result cannot validate a changed candidate.
3. Unknown actions/IDs, extra fields, nonfinite numbers, malformed replies, unsupported limits, and unauthorized topology changes fail closed. Boolean values are not silently accepted as numerical controls.
4. Each revised candidate receives a fresh required simulation and verification. Invalid output, no feasible candidate, or exhausted search budget produces a defined REVIEW/STOP state.
5. Ranking excludes rejected candidates, uses the declared objective and tie rule, and retains a verified incumbent when later proposals are worse. A language preference cannot override the gate.
6. Reference and agentic routes use their declared common tools and budgets. Every extra numerical solve and Llama call appears in the recorded cost.
7. Cases cover a rejected first proposal, successful repair if produced, no-improvement/tie, invalid model output, and inability to find a feasible repair. Software test doubles are clearly separate from empirical Llama results.
8. Any handoff stays advisory and binds human readback to the selected immutable recommendation. No model response acknowledges for the operator.

## Execution audit status

At initial audit, the original 137-frame deck and the two 23-cell main notebooks were inspected, together with the nine-cell trace companion and underlying stage-method documentation. The new orchestration and numerical-adapter source were then reviewed independently. Thirteen orchestration checks using **explicit synthetic test doubles** pass after correction of two evidence-binding issues. They check the candidate budget, a retained incumbent, final rejection, invalid or duplicate ranking IDs, numerical ranking despite a reversed language ordering, nonfinite/Boolean scores, candidate/evidence/contract mutation, and exclusion of the offline truth audit from model contexts. These tests establish behavior of the tested software paths; they are not electrical accuracy or Llama-quality experiments.

The new voltage optimizer minimizes a **current-step** objective, while its MPC tool supplies a first action from an H=3 plan. A local refinement that lowers current-step cost is not therefore a better horizon optimum, and it does not inherit the MPC plan's future-step checks. The final gate is explicitly a first-action check. Restoration uses a finite feeder catalog, while the earlier six-node MILP remains its own formulation lesson. The cyber extension retains the four-bus DC problem with additional protected angle channels; it does not claim two feeder-specific AC/MV cyber solvers.

The isolated-corruption cyber example's unprotected zero-control seed is a deliberately unchecked proposal. A conventional chi-square-aware WLS controller would already hold on its residual alarm. The matched deterministic **verified** workflow is the conventional comparator; the unchecked seed illustrates a rejection mechanism. For the stealth case, a residual-only controller can miss the injected shift.

The numerical cyber gate uses the protected estimate. The known synthetic truth is retained only for separately identified offline audit, and is removed from Llama's refinement and ranking context. Protected-channel authenticity is assumed, not implemented. The consistency threshold is a declared teaching threshold; no general attack-detection probability is inferred.

### Completed five-stage execution

The canonical [recorded suite](../results/proposal_complete_workflow.json), protocol **1.1**, was executed on 2026-09-27. It contains six matched settings × two supervisors, plus one separate Qwen portability example. Every run executes all five proposal stages, evaluates **two initial candidates and two refinement candidates**, then performs **one fresh final recheck**. A Llama-guided run makes four real language-model calls: planning, two critique/refinement choices, and feasible ranking. Awareness, electrical calculation, numerical candidate construction, and engineering verification remain numerical responsibilities.

An independent record audit confirms the following for all 13 runs: the saved implementation hashes match the executed current source; contract, candidate, and evidence hashes remain bound; the returned final action matches the minimum-cost verified search candidate; all final checks pass within the stated model scope; and the best recorded search cost never increases. Every actual model response and client duration matches its source journal. The actual Llama and Qwen input contexts exclude the offline truth oracle. Original operator-acknowledgment and dispatch fields remain false.

| Setting | Fixed final cost | Llama final cost | Fixed / Llama elapsed seconds | Observed outcome |
|---|---:|---:|---:|---|
| Voltage, OpenDSS | 0.484842 | 0.484842 | 11.299 / 20.587 | Same final cost; different refinement order |
| Voltage, three-phase LinDistFlow MV | 0.032600 | 0.437605 | 3.489 / 8.866 | Llama selects weaker search operations and returns a higher cost |
| Restoration, OpenDSS | −6109.971300 | −6109.971300 | 0.947 / 5.720 | Same restored demand; numerical guard corrects Llama's ordering |
| Restoration, three-phase LinDistFlow MV | −6109.971300 | −6109.971300 | 0.306 / 5.232 | Same restored demand; numerical guard corrects Llama's ordering |
| Cyber, isolated corruption, DC | 0.007405 | 0.007405 | 0.004933 / 5.782 | Same protected-estimate constrained response |
| Cyber, stealth Hc, DC | 0.007405 | 0.007405 | 0.003814 / 5.203 | Same protected-estimate constrained response |

Smaller cost is better. Cost units and model coverage differ across use cases and backends; the table supports comparisons **within each row**. Timing includes awareness, candidate preparation, simulation, verification, refinement, and language calls. It excludes adapter construction/imports, prior policy training, and human review. These are single recorded local intervals, with fixed execution before Llama; they are not latency distributions or causal overhead estimates.

The numerical findings support the value of a complete **bounded search plus independent checks**, not superiority of the language model. The final numerical cost ties the fixed route in five of six settings and is worse in the MV-voltage setting. In that setting, Llama spends its two trials reducing reactive participation and slightly increasing PV rather than testing the available MPC first action. The same final gate correctly accepts the selected action in MV scope, but feasibility does not imply good optimization quality.

The restoration case exposes a separate error. Both models give the two feasible search candidates costs approximately −5509.13524 and −6109.97130. Llama orders the former first, despite the instruction to minimize cost. The deterministic ranking guard retains the latter, which connects **1843.61355 kW** of nominal demand, including **474.03975 kW** of critical demand. The recorded `language_order_agrees_with_cost` flag is false for both restoration runs. This is concrete evidence for retaining numerical authority over ranking; it is not successful Llama arithmetic.

The single Qwen MV-voltage example also executes all five stages and the 2+2+1 candidate budget, makes four real calls, and returns cost **0.43760548** in **12.598 seconds**. Its order of local trials differs, and some returned explanations contain inaccurate numerical comparisons. A successful interface call is not a quality or speed advantage. The model-family references describe the underlying models; our journal, rather than those papers, establishes the locally executed tags. [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783), [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115).

### Disclosed interface development

The first complete [pilot suite](../results/proposal_contract_pilot.json) is retained with its original call journals. Llama produced a final recommendation in **one of six** settings and requested REVIEW in the other five. Those unfavorable outputs are part of the evidence.

The [single documented revision](../results/proposal_contract_revision.json) then supplied compact PASS/REJECT and cost feedback, an explicit lowest-cost incumbent, and clearer operation effects. Version 1.1 also requires **one bounded refinement trial whenever valid operations exist**; the second trial may use `KEEP_INCUMBENT`. Model/schema/tool failures still stop for review, and planning retains a REVIEW choice. The first healthy optimizer menu therefore expresses the tutorial's required trial policy rather than allowing a free decision to stop immediately. Both fixed and language-guided routes use the same required minimum and maximum search budget. The interface does not force Llama to choose the best tool or waive a constraint.

The same authored settings were rerun once after this revision. The change from one to six completed Llama settings demonstrates interface development on these cases. It is **not a held-out completion-rate improvement**, and it cannot isolate better prompting from the changed minimum-trial policy. The weaker MV optimization and incorrect restoration ordering remain visible in the final results.

### Operator handoff

The [proposal operator dashboard](../Proposal_Operator_Dashboard.html) displays all six paired settings, five-stage execution marks, actual returned explanations and timings, candidate failures, numerical and language orderings, and model limits. It explicitly identifies the initial pilot and revised protocol.

The human-readback button requires a final independently verified `MODEL_RECOMMEND` record, a name, the exact recommendation ID, and explicit action/scope/authority readback. It creates a separate browser-local record; it does not alter the original experiment or send a physical command. Changing the selected case or supervisor clears the visible acknowledgment and all readback fields. The interaction illustrates an auditable review boundary, not identity authentication or measured operator comprehension.
