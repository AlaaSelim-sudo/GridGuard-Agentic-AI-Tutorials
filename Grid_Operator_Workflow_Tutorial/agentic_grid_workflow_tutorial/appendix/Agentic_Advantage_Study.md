# Where Llama can add value: request interpretation and recovery

This study asks whether a local language model can turn varied operator wording into a correct, usable control request with fewer manual handoffs than a documented rule-based interface. MPC, DRL, restoration search, and the fresh OpenDSS verifier remain the numerical and engineering tools.

A second experiment asks whether a bounded repair loop recovers from a failed tool or rejected proposal. It includes an adaptive deterministic supervisor so that the value of repair is not automatically attributed to Llama.

These are authored teaching pilots on the same synthetic Greensboro feeder. They are not evaluations of a deployed control room or evidence that language models improve the optimality of the underlying controllers.

## 1. Request-intake question

> With the same downstream controllers and checks, which interface correctly interprets the operator's request and obtains a verified recommendation without requesting manual structuring?

The input is authorized operator language. It may restrict permitted operations; it cannot redefine the trusted physical state. Trusted telemetry, actual topology, fault quarantine, device capability, and forecasts are supplied separately.

The experiment reads [operator_requests.json](../data/operator_requests.json) and executes [request_study.py](../src/request_study.py). There are 24 authored requests: 20 with a clear supported interpretation and four that require clarification or refusal to proceed. The clear requests include canonical phrasing and paraphrases; the others cover unspecified limits, conflicting values, forbidden fault reclosure or bypassed checks, and unknown permissions.

The set was authored for the tutorial and is **not held out from its design process**. Freezing its files before the final run preserves a defined experiment; it does not make the set an independent generalization benchmark.

## 2. Shared interpretation schema and trust boundary

Each interpreter produces READY or CLARIFY, a brief reason, and the same four fields:

| Field | Meaning | Implemented values |
|---|---|---|
| rating_fraction | Additional fraction of nominal line-current allowance | 0.8 or 1.0 |
| short_limit_amps | Additional operating ceiling on the short restoration bypass | 100, 150, or 400 A |
| allow_long_tie | Permission to use an already available long route | true or false |
| allow_pv | Permission to use already available PV | true or false |

A current fraction is not a PV cap. The controller still computes the PV candidate. “Reduce current by 20%” and “allow 20% current” therefore have different meanings; the latter is outside this lesson's supported fraction catalog.

The runtime combines restrictions with trusted capability:

\[
\rho_{\mathrm{effective}}
=\min(\rho_{\mathrm{trusted}},\rho_{\mathrm{request}}),
\qquad
I_{\mathrm{short,effective}}
=\min(I_{\mathrm{short,trusted}},I_{\mathrm{request}}),
\]

\[
b_{\mathrm{effective}}=b_{\mathrm{trusted}}\land b_{\mathrm{permission}}.
\]

A permission cannot make unavailable equipment available, and a larger requested ceiling cannot raise the trusted rating. The request cannot overwrite the forecast, source topology, fault status, or mandatory verifier. Trusted information is still a simulation fixture, not implemented field authentication.

The trusted context and shared documentation identify the short route as 0.25 km and the long route as 2.0 km. Interpreting “the quarter-kilometre route” therefore uses public route information, not a fact available only in the evaluator's labels.

## 3. Compared interfaces

| Interface | What happens |
|---|---|
| Rule parser | Apply the documented finite grammar; request a form or clarification outside its supported interpretation. |
| Llama once | Make one actual local-model call using the common schema and trusted context. |
| Llama plus critic | Give a second role the original request, policy, and first interpretation; use its checked interpretation. |
| Llama self-review | Give the interpreter a second opportunity with the same original request, policy, and first interpretation. |
| Structured reference | Supply the authored correct structure directly to the downstream workflow for clear requests. |

The rule parser is an inspectable conventional baseline. It supports numeric expressions, common number words and fractions, relevant synonyms, reduction-by and reserve expressions, and several negation patterns. It hands off outside its documented grammar rather than assuming a permissive default. Its limitations are the limitations of this specified parser, not of every conventional interface or commercial system.

The structured reference represents the result obtainable after correct manual form entry. It is not a measured human trial: no operator completion time or workload is assigned to it. Its zero intake computation cost does not imply zero human effort.

The critic and self-review conditions each allow two logical model calls, while the once condition allows one. Both second calls are fresh requests to the same model backbone and receive the same original request, policy, and initial interpretation. The difference is the role instruction. This tests the incremental value of another pass and of the critic framing. It does not establish independent evidence or independent model errors, despite the role name used in the critic prompt.

The initial model response is shared across these paired conditions, so the study does not contain three independent first-call trials. Count unique actual calls separately from the logical calls charged to each method. Retain service and schema failures; a fail-closed handoff is an appropriate disposition but is not evidence that the model correctly understood the ambiguity.

## 4. Identical downstream workflow

Every READY interpretation is converted into a restricted Case and passed to the **same fixed downstream supervisor**, with the same controller tools, two-tool-call budget, and fresh OpenDSS verifier. CLARIFY stops before a control candidate is requested.

Using a fixed downstream workflow isolates the effect of request interpretation. Any advantage here is evidence for language-assisted intake within the framework. It is not proof that multiple control agents are necessary.

The offline evaluator does not repair an incorrect interpretation before running it. It observes what the produced structure actually causes. Only afterward does it compare the structure and candidate with the authored reference.

## 5. Ground truth and success metrics

Gold labels, request groups, and expected answers are offline evaluation inputs. They are not supplied to Llama or used by the runtime to select an answer.

For each clear request, count **correct automatic completion** only when:

1. the interpretation is READY and all four semantic fields equal the authored reference;
2. the shared runtime produces a recommendation; and
3. the actual recommended candidate passes a fresh evaluation under the reference restrictions.

Thus a schema-valid but semantically wrong interpretation fails, even if it produces some electrically feasible action. Conversely, a good explanation does not compensate for the wrong current limit or permission.

Report separate counts for:

- exact interpretation on the 20 clear requests;
- correct automatic completion on those same requests;
- unnecessary intake handoffs on clear requests;
- appropriate clarification/abstention dispositions on the four non-actionable requests;
- incorrect READY interpretations;
- service/schema failures and their fail-closed dispositions;
- actual/logical model calls and machine latency.

The raw scorer's correct_clarification field records the abstention disposition. The report must additionally exclude service/schema failures when identifying successful semantic clarification, using the retained call errors. The short natural-language reason is retained for inspection; its factual accuracy is not separately scored. A handoff is a counted interface event, not a measured number of operator minutes. Clarification cases should not be treated as failed control completions when clarification was the intended outcome.

The downstream workflow's own escalation is also distinct from an intake handoff. Report both if either occurs. Use denominators explicitly rather than combining clear requests and intentionally non-actionable requests into one misleading completion rate.

## 6. Recovery experiment

[recovery_study.py](../src/recovery_study.py) compares three supervisors with a common forced first tool:

| Supervisor | Behavior after a failed first attempt |
|---|---|
| Single pass | Stop without a recommendation. |
| Adaptive rules | Remove the failed tool and select an available alternative. |
| Agent loop | Ask the actual Llama critic and planner to select a remaining tool using the failure evidence. |

The three cases comprise an injected MPC service-unavailable response, an injected DQN checkpoint-access failure, and an actual trained-DQN proposal rejected under an 80% line-current allowance.

The two availability failures are declared adapter injections with a 20 ms delay. No real service is stopped and no checkpoint is deleted. The electrical-rejection case uses the saved trained policy and a fresh OpenDSS solve.

All routes share the first attempt and verifier. The two recovery routes can make a second tool call. A proven infeasible MPC horizon ends the attempt rather than authorizing a myopic substitute.

The single-pass condition is a repair-loop ablation. It is not the strongest conventional-practice baseline. The adaptive-rules condition supplies that counterfactual for these known failure types.

Measure verified completion, no-action outcomes, failed-tool responses, gate rejections, tool calls, fresh solves, model calls, and elapsed time. If both recovery methods succeed, the finding is that repair helped and that a deterministic supervisor handled these known cases too. Do not assume that the critic improves success or that Llama's additional cost is justified.

## 7. Recorded results and their interpretation

The tables below come from [advantage_summary.json](../results/advantage_summary.json) and [confirmation.json](../results/confirmation.json). A correct completion requires both exact requested fields and a recommendation freshly checked under the offline reference restrictions. An incorrect READY counts a committed semantic error, including an answer to a request that should have required clarification.

### Authored pilot: 20 clear requests and four clarification cases

| Interface | Correct completions / 20 | Incorrect READY / 24 | Clear-request handoffs / 20 | Correct clarifications / 4 | Median machine time, s |
|---|---:|---:|---:|---:|---:|
| Rule parser | 14 | 0 | 6 | 4 | 0.30 |
| Llama once | 16 | 4 | 0 | 4 | 3.84 |
| Llama plus critic | 9 | 5 | 7 | 3 | 6.42 |
| Llama self-review | 10 | 7 | 4 | 3 | 6.54 |
| Correct structured reference | 20 | 0 | 0 | Not evaluated | 1.10 |

Llama once correctly completes two more clear requests than the parser, but it also commits four wrong READY interpretations. Its absence of handoffs therefore includes mistakes. The pilot shows increased interpretation coverage with errors, rather than an unconditional improvement. The structured reference shows that correct intake lets the same downstream tools complete all 20 clear cases. Human form-entry time was not measured. Its timing covers only the 20 clear cases; other rows include all 24, so their medians do not constitute matched human-interface timing comparisons.

The critic corrects no initial mistakes and introduces eight paired regressions; self-review corrects none and introduces seven. These regression counts include clarification outcomes as well as control completion. Extra roles and extra passes did not help in this run. There were 72 unique actual model calls, because the initial answer is shared by the once, critic, and self-review conditions. No model service/schema errors occurred in this final request run. The timings describe one local session with a fixed evaluation order and model caching.

**Follow q09 from language to a verified recommendation.** The request is: “Bring back demand with at most one hundred amperes through the nearby bypass. Keep the farther route open and leave solar generation out of the plan.” The parser requests manual structuring. Llama once correctly supplies rating fraction 1.0, short-route limit 100 A, long-route permission false, and PV permission false. The unchanged restoration search chooses the short route, zero PV, and a 0.75 noncritical-load shedding fraction. Fresh verification accepts **1,843.61 kW of nominal connected demand**. Llama's contribution is interpreting the request; the numerical search and OpenDSS produce and verify the restoration result.

### Exploratory hybrid and prospective confirmation

After examining the pilot, a hybrid was selected: keep a parser READY output; otherwise call the original Llama interpreter once. Applying this policy to the saved pilot responses gives 19/20 correct completions, one wrong READY, no clear-request handoffs, and 4/4 correct clarifications. This is **post-hoc exploratory analysis**, not a prespecified pilot arm or a separate validation run; it makes no new model calls.

A distinct set of 12 requests was then authored without inspecting the pilot's numerical results or testing the new requests against the parser/model. It contains eight clear requests and four clarification cases. Its labels, unchanged parser/interpreter, and hybrid policy were frozen before confirmation inference. The hybrid itself had been selected after the pilot, so this is a **prospective authored confirmation of that selected policy**, not a field sample or a large generalization benchmark. The fixture hash is `3cc87e17b2de96f368bdb1cac8c459131bf1604b3e25fcf4586c758811975893`; the full freeze and model digest are retained in [confirmation_freeze.json](../results/confirmation_freeze.json).

| Interface | Correct completions / 8 | Incorrect READY / 12 | Clear-request handoffs / 8 | Correct clarifications / 4 | Accepted candidates outside gold limits | Actual Llama calls | Median machine time, s |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rule parser | 5 | 1 | 2 | 4 | 1 | 0 | 0.13 |
| Parser-first hybrid | 7 | 2 | 0 | 3 | 1 | 6 | 2.16 |

The hybrid correctly automates two additional clear requests, h06 and h07. It inherits the parser's mistake on h05 and introduces another wrong READY on h09. Both mistakes matter:

- **h05: an intended restriction is lost.** “Keep a one-fifth margin below nominal ampacity” requires rating fraction 0.8. The parser produces 1.0, and the hybrid accepts that READY without calling Llama. The 30% DQN cap passes the operational gate at 87.60% of nominal rating, but the offline check under the intended 0.8 restriction finds 109.50% utilization and five overloaded lines. A fresh electrical check cannot recover an omitted semantic constraint by itself.
- **h09: an unsupported value is silently changed.** The request specifies 90% of nominal current, outside this lesson's 0.8/1.0 catalog. The parser correctly requests clarification. Llama instead emits READY with 0.8 and an unrequested 150 A short-route limit. The resulting MPC recommendation passes the interpreted case's checks, but it is not a correct response to the request. Choosing a more restrictive supported value does not authorize silently rewriting an unsupported request.

The confirmation therefore supports a narrow benefit in language coverage while showing that the hybrid can carry forward parser errors and add new ones. It does not establish field safety, measured operator workload reduction, or a uniformly preferable interface. Operator readback and validation of interpreted restrictions would be needed before relying on such a design for field recommendations; that human process is not implemented or measured here. A future separately evaluated design could distinguish unfamiliar wording from prohibited or unsupported intent before allowing a model fallback. These frozen results have not been retroactively repaired.

### Recovery: the value of another permitted attempt

| Supervisor | Verified completions / 3 | No-action outcomes / 3 | Numerical tool calls | Fresh AC solves | Actual Llama calls | Total machine time, s |
|---|---:|---:|---:|---:|---:|---:|
| Single pass | 0 | 3 | 3 | 4 | 0 | 0.58 |
| Adaptive rules | 3 | 0 | 6 | 7 | 0 | 1.14 |
| Agent loop | 3 | 0 | 6 | 7 | 6 | 17.66 |

Repair helps relative to stopping after the forced failed first attempt. The competent adaptive supervisor and the agent both recover all three cases, and the agent is slower. These observations show no unique Llama completion advantage for the known failure types. They are descriptive totals from one session, not statistical latency estimates.

## 8. Fifteen-minute classroom narrative

| Minutes | Activity |
|---|---|
| 0–3 | Read a canonical request and a paraphrase; predict the four semantic fields. |
| 3–7 | Compare parser and Llama outputs, then run their structures through the shared controls and checks. |
| 7–10 | Inspect h05 and h09: distinguish a passing interpreted case from the intended request. |
| 10–13 | Read the pilot and prospective confirmation tables; keep coverage, errors, and handoffs separate. |
| 13–15 | Compare once, critic, and self-review; state why the extra roles did not help here. |

A useful discussion prompt is: “If the expert-structured reference reaches the same electrical result, what did the language model add?” The intended distinction is automatic interpretation and workflow access, with an associated accuracy/cost trade-off.

A supported claim is: “On these small authored sets, language-assisted intake correctly automated additional requests, while also producing wrong READY interpretations. Shared engineering checks evaluated the interpreted constraints and did not guarantee fidelity to the operator's meaning.”

## 9. Reproduction and claim limits

From the tutorial environment:

~~~text
python -m src.request_study
python -m src.recovery_study
python -m src.hybrid_study
~~~

Preserve existing outputs before regeneration. Request-study metadata record the fixture and implementation hashes, policy, schema, model, seed, and temperature before calls. Recovery metadata record the protocol, injected faults, source/checkpoint provenance, and method budgets.

Inspect request_freeze.json, request_calls.json, request_study.json, recovery_protocol.json, recovery_calls.json, recovery.json, confirmation_freeze.json, confirmation_calls.json, confirmation.json, and advantage_summary.json in the results folder. Preserve all failures and development revisions rather than retaining only successful wording. The confirmation freeze prevents silently changing its fixture or implementation while reusing the same study version; create a separately identified experiment for changes.

Request-study machine time includes intake and the shared runtime. The extra gold verification belongs to offline scoring and is not an operational decision step. Training and reusable AC-table preparation are separate shared costs. Timings from this authored pilot are descriptive, not a statistical speedup result.

The study cannot establish operator workload reduction, deployment safety, broad language robustness, or superiority over all conventional interfaces. It also cannot show that several roles are necessary merely because a model-assisted interface improves over a finite grammar. That is why the second-pass and adaptive-rule counterfactuals are included.

## Primary scientific references

1. **T. Schick et al. (2023), Toolformer: Language Models Can Teach Themselves to Use Tools.** [Paper](https://arxiv.org/abs/2302.04761). Supports separating language-model tool/argument selection from specialist computation. Its trained API-use results are not evidence of the performance of this prompted model or feeder.
2. **S. Yao et al. (2023), ReAct: Synergizing Reasoning and Acting in Language Models, ICLR.** [Paper](https://arxiv.org/abs/2210.03629). Motivates using observations from tools to guide subsequent actions. It does not establish superiority over a well-designed deterministic grid supervisor.
3. **S. G. Patil, H. Mao, F. Yan, C. C.-J. Ji, V. Suresh, I. Stoica, and J. E. Gonzalez (2025), The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models, ICML.** [Proceedings](https://proceedings.mlr.press/v267/patil25a.html). Motivates separate evaluation of function/argument correctness, abstention, and multi-step execution. Correct syntax alone does not establish the intended outcome or electrical feasibility.
