# Guide to agent traces, returned explanations and measured latency

Use [Agent_Trace_and_Latency.ipynb](../Agent_Trace_and_Latency.ipynb) to inspect actual saved responses and measured intervals without contacting Ollama, invoking OpenDSS, running an optimizer or retraining a policy. Its analysis-cell execution time is different from the historical durations displayed in its tables.

The expanded presentation has **137 distinct frames: 80 core teaching frames, 48 optional code/detail frames and 9 mathematical/reference frames**. The 80-frame core retains the three-hour route. Select detail frames to replace the corresponding discussion time, support questions or extend a lab. Progressive PDF pages can exceed the number of distinct frames. Follow the [slide/notebook map](../latex_slides/Slide_Notebook_Map.md) for exact checkpoint alignment.

## Start with the evidence boundary

The companion selects **10 actual local Llama calls and 8 containing workflow intervals** from three distinct protocols. These are the records selected for this lesson; they are not the total calls ever made in the project.

| Protocol | Selected calls | Scope of its measured time | Result to retain |
| --- | --- | --- | --- |
| Current continuous voltage | 3 OpenDSS calls and 2 MV LinDistFlow calls | Supervisor, fresh candidate checks and language calls; MPC plans and SAC proposals were precomputed | Fixed and agentic supervision return the same backend-specific action |
| Historical standard methods | 2 restoration MILP calls and 2 cyber DC calls | Complete small-model workflow, including its numerical method | Same numerical result as fixed supervision; actual Llama explanation escalates to REVIEW |
| Historical h06 restoration intake | 1 interpretation call | Raw language call inside intake; intake plus downstream runtime is reported separately | Hybrid completes this request; documented parser asks for clarification |

The first two protocols supply four fixed/agentic pairs, hence eight workflow intervals. The h06 record supplies its own two intake/runtime rows; it is not inserted into those eight intervals. The older standard-method voltage calls and other language-confirmation requests remain in their source files but are outside this selected ten-call table.

## Run T1–T9 in order

Open Jupyter in the tutorial folder, using the tutorial environment with pandas and matplotlib. The companion imports a read-only evidence reader. Ollama, OpenDSS and PyTorch need not be active.

| Checkpoint | What to inspect | Question to answer |
| --- | --- | --- |
| T1 | Exact reply/journal matches, source hashes and selected counts | Are these the actual records used by the displayed results? |
| T2 | Current voltage stages, returned choices/reasons and pending operator card | Which numerical check caused the transition to recovery? |
| T3 | Five current voltage calls, request options and token metadata | What did each Llama role actually return, and what interval was timed? |
| T4 | Six-node MILP fixed/agentic traces and numerical summary | Why is a solved 200 kW plan still marked REVIEW by the language route? |
| T5 | h06 request, interpretation, intake and downstream runtime | Which added completion comes from language coverage rather than a better optimizer? |
| T6 | Four-bus DC cyber traces and actual REVIEW explanation | Which evidence is explicitly assumed trusted, and which state does the enum select? |
| T7 | Ten per-call client/server/token rows and paired bars | Which quantities are nested, and which are generation-only? |
| T8 | Four paired workflow panels and excluded numerical preparation | What work is inside each interval, and are the scopes comparable? |
| T9 | Exact source fingerprints and final consistency checks | Which claimed benefit is supported, and what needs another experiment? |

Main-notebook counterparts are **V4/V5/A1/A2** for voltage, **R4/R5** for the two restoration protocols, and **C4** for cyber. The main notebooks execute the electrical demonstrations; this companion reads their records and journals.

The underlying trace retains each complete stage response, including numerical evidence. Long pandas cells can truncate a display. To inspect one complete response, select it from the loaded record, for example:

```python
run = evidence['voltage']['opendss']['agentic']
for stage in run['trace']:
    if stage['stage'] == 'Verification':
        print(json.dumps(stage['response'], indent=2))
```

This prints both actual verification attempts from the saved record. It does not rerun either check. [Case_Agent_Responses.md](Case_Agent_Responses.md) provides the corresponding stage-by-stage teaching narrative and full returned reasons.

## What the numbers measure

`client_s` comes from the tutorial client's elapsed-time timer around a model request and response handling. In these clients the per-call timer is recorded before the journal file is written. The enclosing workflow interval also contains other orchestration, numerical evaluation and recording work. A difference between client time and Ollama time does not isolate network delay, hardware scheduling or Python overhead.

The official [Ollama chat API](https://docs.ollama.com/api/chat), checked **27 September 2026**, defines server duration fields in **nanoseconds**. This notebook converts them to seconds by dividing by `1e9`. `total_duration` is the server's total; `load_duration`, `prompt_eval_duration` and `eval_duration` describe loading, uncached prompt evaluation and output generation. Prompt, cached-prompt and generated-token counts are retained as reported metadata. They are not measured dollar or energy costs.

For a call with positive generation duration:

\[
T_{\mathrm{server}}=\frac{\texttt{total\_duration}}{10^9},\qquad
\text{generation rate}=\frac{\texttt{eval\_count}}{\texttt{eval\_duration}/10^9}.
\]

The rate measures generated tokens per second during generation. It excludes prompt evaluation, request handling, tool computation and operator review. Client and server durations are two views of the same call: do not add their bars. Server sub-durations need not sum exactly to the returned total.

### The ten selected actual calls

Times are seconds, rounded here to six decimal places. The notebook and journals retain the original values. All selected calls used `llama3.1:8b`.

| Record | Role | Returned choice | Client s | Server s | Output tokens | Generation tokens/s |
| --- | --- | --- | --- | --- | --- | --- |
| Voltage / OpenDSS | Planner | VERIFY_SAC_FIRST | 0.987997 | 0.954963 | 36 | 74.32 |
| Voltage / OpenDSS | Recovery | USE_MPC_PLAN | 0.846633 | 0.832109 | 43 | 75.26 |
| Voltage / OpenDSS | Explanation | REVIEW_EVIDENCE | 0.985395 | 0.960166 | 57 | 74.93 |
| Voltage / MV | Planner | VERIFY_SAC_FIRST | 3.809483 | 3.788563 | 36 | 74.56 |
| Voltage / MV | Explanation | REVIEW_EVIDENCE | 1.010360 | 0.984771 | 56 | 75.06 |
| Restoration MILP | Planning | RESTORATION_MILP | 2.883081 | 0.804366 | 51 | 69.39 |
| Restoration MILP | Explanation | REVIEW | 3.207768 | 1.130471 | 79 | 74.14 |
| Cyber DC | Planning | WLS_TRUSTED_REDISPATCH | 2.699153 | 0.646972 | 46 | 77.14 |
| Cyber DC | Explanation | REVIEW | 3.230637 | 1.158535 | 77 | 74.83 |
| h06 intake | Interpreter | READY | 3.160396 | 1.123916 | 59 | 71.74 |

The MV Planner's recorded server loading component is 2.972156 s; its total client call is 3.809483 s. This helps describe this particular observation. It does not establish that the MV electrical model inherently needs slower language reasoning. Prompt cache state, loading and service conditions were not randomized or repeated as a hardware benchmark.

The historical MILP, cyber and h06 client intervals are roughly two seconds longer than their server intervals. The saved data do not decompose that difference into measured causes, so the tutorial does not assign it to networking, safety checking or any particular stage.

### Paired workflow intervals

The remainder is `workflow seconds − sum(included client call seconds)`. It is aggregate work inside that interval, **not isolated solver time**. A blank per-stage Llama duration means no isolated language call was recorded for that stage; it does not mean the numerical work took zero time.

| Protocol/model | Route | Final status | Workflow s | Included client calls s | Other in interval s |
| --- | --- | --- | --- | --- | --- |
| Current / OpenDSS | fixed | MODEL_RECOMMEND | 0.346053 | 0.000000 | 0.346053 |
| Current / OpenDSS | agentic | MODEL_RECOMMEND | 3.110454 | 2.820025 | 0.290429 |
| Current / MV LinDistFlow | fixed | MODEL_RECOMMEND | 0.134196 | 0.000000 | 0.134196 |
| Current / MV LinDistFlow | agentic | MODEL_RECOMMEND | 4.911368 | 4.819843 | 0.091525 |
| Historical / restoration | fixed | MODEL_RECOMMEND | 0.009859 | 0.000000 | 0.009859 |
| Historical / restoration | agentic | REVIEW | 6.101782 | 6.090849 | 0.010933 |
| Historical / cyber | fixed | MODEL_RECOMMEND | 0.002146 | 0.000000 | 0.002146 |
| Historical / cyber | agentic | REVIEW | 5.934650 | 5.929790 | 0.004860 |

For current OpenDSS voltage, the actual language-call sum is 2.8200252000096953 s, within the 3.1104542999964906 s workflow. The remainder is 0.29042909998679534 s. For MV LinDistFlow the corresponding values are 4.81984339999326 s, 4.911368000000948 s and 0.0915246000076877 s. These calculations use intervals from the same containing run.

Do not pool a precomputed-MPC voltage interval with a historical small-model interval that includes its solver. T8 displays preparation times separately. Adding independently measured pieces after the fact does not create an experimentally measured end-to-end latency distribution.

### h06 has a different timing boundary

| Route | Intake s | Downstream runtime s | Machine sum s | Disposition |
| --- | --- | --- | --- | --- |
| rule_parser | 0.000027900 | 0.000000100 | 0.000028000 | Clarification; no restoration solve |
| hybrid | 3.160423900 | 1.125596200 | 4.286020100 | Verified simulation recommendation |

The hybrid's raw model call is 3.1603959999993094 s inside the 3.160423899993475 s intake. Its downstream runtime is 1.1255961999995634 s, giving 4.2860200999930385 s of recorded machine work. That sum excludes offline gold-label verification and human handling. The parser's tiny interval ends at clarification; it does not measure completion of the same restoration task.

## Returned reasons, status and physical proof have different roles

The named agents share a local model and execute sequential roles. They are not independent expert votes. The displayed text is the actual returned `reason`, not a private reasoning trace or a physical correctness certificate. The `choice` field selects a permitted transition; numerical methods calculate the action and deterministic checks evaluate the declared model.

- **Voltage:** Planner requests the common SAC check; OpenDSS rejects current use 111.97% of allowance; Recovery requests the shared MPC point, which passes at 99.60%. Fixed supervision reaches the same accepted control. Llama adds visible reasoning text and measured machine latency, with no additional numerical improvement in this pair.
- **Restoration MILP:** the numerical tool returns 200 kW service and 90 kW critical service for both routes. Actual Llama Explanation returns `REVIEW` despite describing passed checks. Retain that escalation.
- **Restoration h06:** the parser cannot complete the request; hybrid intake correctly extracts the 100 A ceiling, no long tie and no PV, and the shared downstream workflow completes it. The post-hoc five-clear-request restoration subset is 3/5 versus 5/5, while the full 12-request parent study still contains 1/12 versus 2/12 incorrect READY interpretations.
- **Cyber:** the explicitly supplied protected-data branch and conventional redispatch reduce the actual toy stressed-line flow from 0.24000 to 0.17046 p.u. Fixed and agentic numerical results agree. The language route's final `REVIEW` leaves its numerical candidate provisional. Llama does not authenticate the additional protected measurements.

The earlier current-voltage interface pilot also remains available: both agentic runs initially escalated before a candidate evaluation. Interface 1.1 clarified the tool effects and included the supplied SAC proposal. Its later successful routing is disclosed development evidence, not a held-out estimate of language-model reliability.

## What T1 and T9 verify

The loader checks that each selected voltage reply has one matching journal by call ID, returned choice/reason and client duration. Historical standard-method replies match their declared journal. h06 matches its exact operator request and complete interpreted response. Parsed journal responses must equal the actual JSON response text.

Selected duration/count fields must be recorded, finite and nonnegative; counts must be integers. Missing timing metadata is rejected rather than reported as zero. Declared voltage call counts must match the matched journal. Included client calls must fit their containing workflows; h06's call must fit its intake, and its machine duration must equal intake plus runtime. SHA-256 values identify every source file read. Those hashes are consistency fingerprints, not signatures authenticating a device or evidence of electrical safety.

The analysis was checked against the unchanged golden records and **15 deliberately corrupted temporary fixtures** covering reply/ID/duration mismatches, raw/parsed disagreement, interval nesting, inconsistent call count, missing metrics, nonfinite/negative durations and fractional token counts. Each fixture was rejected. All nine notebook code cells passed syntax compilation. These are tests of the analysis contract; they do not establish field-model or sensor correctness.

## Claims this evidence can support

Report the observed action, its modeled constraints, the actual returned language decision, the task's completion/escalation outcome and the exact scope of the timed interval. The data support transparent case-specific comparisons and a small recorded language-intake coverage result.

They do not measure repeated-run latency distributions, p50/p95 response time, a hardware-normalized speed ranking, monetary price, energy use, operator workload or field reliability. A faster stop for review is not a faster completed task. A passed first-action check is not closed-loop stability or a future-horizon guarantee.

For the next controlled study, freeze cases/prompts and scoring rules; pair identical scenarios; randomize route order; record model version, hardware and load/cache state; repeat runs; retain failures and timeouts; report completion and incorrect recommendations alongside elapsed-time quantiles. Measure human comprehension/readback separately. These are proposed experiments, not results already demonstrated by this tutorial.

## Source records

- `results/workshop_run_opendss.json`
- `results/continuous_llama_opendss_20260927T161223523552Z.json`
- `results/workshop_run_lindistflow3.json`
- `results/continuous_llama_lindistflow3_20260927T161120781113Z.json`
- `results/standard_agent_workflow.json`
- `results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json`
- `results/confirmation.json`
- `results/confirmation_calls.json`

Reader implementation: [`src/trace_latency.py`](../src/trace_latency.py). Full responses: [Case_Agent_Responses.md](Case_Agent_Responses.md). The notebook displays the exact source hashes in T9.
