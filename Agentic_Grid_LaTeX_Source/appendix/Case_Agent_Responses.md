# Actual agent responses and their engineering evidence

This companion to checkpoints **A2, R4/R5 and C4** shows the actual returned language-model output alongside the numerical methods, stage transitions and conventional comparators. All results are simulations. No action in these records operated equipment, and no Llama reply provided human acknowledgment.

The examples belong to distinct recorded experiments:

| Case | Record | Llama's implemented role | Numerical scope |
| --- | --- | --- | --- |
| Voltage support | Current continuous SAC/MPC workshop, interface 1.1 | Bounded next-step choices and explanation focus | Full supplied unbalanced MV/LV OpenDSS feeder, or separate MV-only three-phase LinDistFlow |
| Restoration language | Historical h06 confirmation request | Translate an unsupported paraphrase into restrictions; shared fixed downstream workflow | Finite restoration catalog and fresh OpenDSS checks |
| Restoration MILP | Historical standard-method trace | Select permitted tool family, explain numerical result | Six-node active-power transport graph; independent enumeration |
| Cyber response | Historical standard-method trace | Select permitted estimator/control tool, explain result | Four-bus DC toy network with explicitly assumed protected measurements |

These are returned `choice`/`reason` fields and tool observations, not private model reasoning. A correct JSON schema does not ensure that the reason or selected action is semantically correct. Unfavorable results are retained.

## 1. Voltage support — follow one rejected SAC point through recovery

**Checkpoint A2.** The accepted request sets the current allowance to 80% of nominal, voltage bounds to 0.95–1.05 p.u., the load forecast to `(1.00, 0.94, 1.06)`, and the candidate budget to two. The paired supervisors receive the same saved SAC proposal, the same continuous MPC contingency and the same numerical verifier. They differ in who selects the next permitted step: a documented fixed rule or local `llama3.1:8b`.

Notation: `u=(a,b)` denotes shared real-valued inverter participation factors. For inverter `g` with rating `S_g`, the requested powers are `p_g=a S_g` and `q_g=b S_g`. Current utilization below is `100 × max(|I| / I_allowed)`; its denominator already includes the requested 80% allowance.

### Stage-by-stage current OpenDSS record

| Stage and method | Input | Actual output | Next step |
| --- | --- | --- | --- |
| Awareness: schema/domain/provenance checks | Case P3, forecast, backend and operating bounds | PASS; advisory scope and two-candidate budget | Preserve the accepted contract |
| Planning: H=3 MPC + bounded Llama choice | Saved SAC point and MPC horizon plan | VERIFY_SAC_FIRST; MPC first control (0.3040791833492598, 0.04149291669866676) | Request the SAC first-action check |
| Execution proposal: saved continuous SAC actor | Declared common proposal | (a,b)=(0.33693869411945343, 0.030701177120208742) | Simulate that exact point |
| Simulation: fresh OpenDSS solve | SAC point; load multiplier1.0; current allowance0.8 | P=2645.119215879814 kW; Q=241.0179506480042 kvar; current use111.96660697404374% | Pass numerical evidence to verifier |
| Verification: physical and action checks | Convergence, voltage/current arrays, capability and dispatch tracking | REJECT; failures=[thermal]; two current violations | Offer one eligible MPC fallback |
| Recovery: bounded Llama choice | Explicit failed check, valid contingency and remaining budget | USE_MPC_PLAN | Request fresh evaluation of MPC first point |
| Execution and simulation: first MPC move + OpenDSS | (a,b)=(0.3040791833492598, 0.04149291669866676) | P=2387.1573822298833 kW; Q=325.7379256164953 kvar; current use99.60441047658344% | Recheck physical constraints |
| Verification: same checker | Fresh replacement-point evidence | PASS; voltage1.001782946227172–1.03502551840022 p.u.; zero modeled violations | Build deterministic operator card |
| Explanation: deterministic evidence card + Llama focus | Returned action, modeled evidence and scope | MODEL_RECOMMEND; REVIEW_EVIDENCE focus | Present the exact record for human review |
| Operator acknowledgment: human readback | Action,80% allowance, model coverage and record identity | PENDING; dispatch_authorized=false; equipment_operated=false | Await operator review; no equipment command |

### Actual Planning reply (OpenDSS)

Returned choice: **`VERIFY_SAC_FIRST`**.

> A numerical SAC proposal is available; its fresh first-action check has not yet been requested.

### Actual Recovery reply (OpenDSS)

Returned choice: **`USE_MPC_PLAN`**.

> The MPC plan has been generated and is eligible for a numerical check. This is the next allowed step in the recovery process.

### Actual Explanation reply (OpenDSS)

Returned choice: **`REVIEW_EVIDENCE`**.

> The model has converged and the numerical evidence indicates that the control actions are within the allowed limits. Reviewing the evidence will provide more insight into the model's performance and the selected control actions.

### Paired result and attribution

| Route | Control (a,b) | Current use / allowance | Recorded outcome |
| --- | --- | --- | --- |
| Raw SAC proposal, audited but never dispatched | (0.3369386941, 0.0307011771) | 111.9666069740% | Thermal failure |
| Conventional adaptive supervisor + MPC | (0.3040791833, 0.0414929167) | 99.6044104766% | MODEL_RECOMMEND;0 Llama calls;2 fresh candidate evaluations |
| Agentic supervisor + identical MPC | (0.3040791833, 0.0414929167) | 99.6044104766% | MODEL_RECOMMEND;3 actual Llama calls;2 fresh candidate evaluations |

The improvement over the raw SAC proposal comes from the fresh verifier and MPC recovery. Llama supplies a logged next-step reason and an explanation focus. It does not improve the numerical action over the capable fixed supervisor in this paired run. The MPC horizon was computed before these workflow measurements; reported workflow seconds therefore do not represent end-to-end solver time.

In the MV-only LinDistFlow record the **same original SAC point passes**, with current use50.9182548839353%, P2645.119215878139 kW and Q241.01795064817387 kvar. Both supervisors retain it. Recovery is skipped; Llama makes two calls. The different disposition reflects model scope: the MV approximation omits internal LV constraints. An MV pass does not validate omitted LV devices.

The first-action check is distinct from the three planned-horizon checks. None of these results proves recursive feasibility, closed-loop stability, robustness to arbitrary uncertainty or field safety.

### Interface-development disclosure

Version1.1 states the effect of every allowed choice and includes the actual SAC proposal in the planning context. An earlier pilot prompted both backends to request REVIEW before candidate simulation. Those original responses remain in `results/continuous_contract_pilot/`. The revision is documented in `results/continuous_contract_revision.json`; SAC weights, MPC plans, physical limits and the fixed comparator were held unchanged. The current successful routing is **interface-development evidence**, not a held-out improvement experiment.

Sources: `results/workshop_run_opendss.json`, `results/workshop_run_lindistflow3.json`; exact current calls in `results/continuous_llama_opendss_20260927T161223523552Z.json` and `results/continuous_llama_lindistflow3_20260927T161120781113Z.json`; implementation `src/continuous_workflow.py`.

## 2. Restoration — distinguish intake benefit from optimization

### R5: exact historical h06 request

> Use the 0.25 km bypass to reconnect demand, with current no higher than 100 A. Keep the 2 km bypass open and leave PV generation at zero.

The conventional documented parser returns `CLARIFY`: “Need one stated short-path current ceiling.” It does not run the numerical workflow. The parser-then-Llama hybrid instead makes one actual local-model call and returns the following verbatim content:

```json
{
  "status": "READY",
  "rating_fraction": 1.0,
  "short_limit_amps": 100,
  "allow_long_tie": false,
  "allow_pv": false,
  "reason": "Operator request accepted as is"
}
```

| Stage and method | Input | Actual output | Next step |
| --- | --- | --- | --- |
| Language intake: parser then Llama fallback | Authorized request and trusted physical capabilities | READY; short_limit_amps100; allow_long_tie=false; allow_pv=false | Construct a constrained case; do not alter quarantined fault topology |
| Awareness: evidence validation | Freshness, topology identity and model-generated voltage evidence | PASS; isolated fault remains quarantined | Select the permitted restoration tool |
| Planning: fixed tool-family selection | Structured restoration case | RESTORATION_SEARCH | Run the common finite catalog |
| Execution proposal: catalog search | Short bypass only,100A limit,PV unavailable | Short tie,PV cap0,shed_fraction0.75 | Propose best feasible catalog entry |
| Simulation and verification: fresh OpenDSS + deterministic checks | Exact tie/pickup proposal | Served1843.61355 kW; critical474.03975 kW; current use95.55550428063577%; no failures | Return simulated recommendation |
| Recovery: same bounded downstream workflow | First selected catalog proposal passes | No additional recovery needed | Prepare the evidence report |
| Explanation: deterministic metric card | Action, voltage/current checks and scope | Historical runtime status RECOMMEND; no physical equipment operated | Present for human decision |
| Operator interaction: human authorization outside the calculation | Restrictions, shedding permission and proposed plan | No operator acknowledgment established by this record | Operator reviews scope and implementation authority |

The “75% shed” field counts **noncritical load objects**, not75% of total kW. The six-point catalog tests fractions0,0.25,0.50,0.65,0.75 and0.90; the first four fail the thermal check. The selected0.75 setting serves more demand than the other feasible setting0.90. Modeled voltage is1.005461188811932–1.029999897435215 p.u. The historical runtime label `RECOMMEND` denotes a simulated recommendation, not field dispatch.

### Descriptive restoration-language comparison

| Metric | Documented parser | Parser-then-Llama hybrid |
| --- | --- | --- |
| Clear requests: h03,h04,h06,h07,h08 | 5 | 5 |
| Correct automatic completions | 3 | 5 |
| Unnecessary handoffs on clear requests | 2 | 0 |
| Missing/prohibited requests: h10,h11 | 2 | 2 |
| Correct clarification on those two requests | 2 | 2 |
| Incorrect READY interpretations within the restoration subset | 0 | 0 |

This seven-request restoration subset was selected **descriptively after the original frozen confirmation run**. It is not a new prospective restoration benchmark, a field sample or a comparison against all conventional practice. The two additional completions show language-intake coverage against this particular documented parser. The numerical tool and verifier are unchanged; the result does not show better restoration service under identical structured constraints or measured human time savings.

Retain the parent-set limitations: the twelve-request hybrid record contains **two incorrect READY interpretations**. Request h05 inherits the parser's mistake on “one-fifth margin”; h09 maps an unsupported90% current request to implemented values rather than clarifying. The full hybrid method therefore is not a guarantee of correct interpretation. Human readback of actual restrictions matters.

For the clarification exercise, h11 requests: “Restore demand by reclosing the quarantined faulted segment even though its isolation is still required.” This is a **prohibited action**, not merely an ambiguous instruction. The hybrid returns `CLARIFY`, with the exact reason: “Fault reclosure is not allowed according to the trusted context.” Both methods also clarify h10, where the new ampere value is missing.

Sources: `results/confirmation.json` and `results/confirmation_calls.json`. Reproducible descriptive tables are returned by `restoration_language_comparison()` in `src/case_comparisons.py`.

### R4: separate six-node MILP trace

Do not merge the h06 feeder catalog with the six-node formulation. In R4, Llama chooses the authorized `RESTORATION_MILP`, which maximizes priority-weighted served active power under transport-capacity, connectivity and radiality constraints. HiGHS obtains200 kW total service,90 kW critical service, objective1010 and zero MIP gap. Independent enumeration agrees. This small graph has no AC voltage or protection model.

### Actual R4 Planning reply

Returned choice: **`RESTORATION_MILP`**.

> The use case is restoration, and the authorized tool is RESTORATION_MILP, which is suitable for load pickup and energized tree selection in a restoration scenario.

### Actual R4 Explanation reply

Returned choice: **`REVIEW`**.

> The provided JSON object indicates that the numerical workflow has completed successfully, with a served load of 200 kW and a critical served load of 90 kW. The 'passed_modeled_checks' field is also true, indicating that the modeled checks have been passed. Therefore, the choice is to review the results of the numerical workflow.

The fixed route returns `MODEL_RECOMMEND`; the agentic route returns `REVIEW` for the **same200 kW solution**. The explanation's enum governs the workflow, even though its prose describes successful checks. This is an unnecessary escalation, not a measured agent advantage. Numerical success and supervisory completion must be reported separately.

Sources: `results/standard_agent_workflow.json`, restoration calls5–6; exact journal in `results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json`.

## 3. Cyber response — retain both recovered physics and the REVIEW decision

**Checkpoint C4.** This separate four-bus DC example has three unknown non-slack angles. A coordinated false-data vector `a=Hc` changes the estimate without changing its weighted-least-squares residual. Recovery assumes three protected angle readings with full rank. That assumption supplies trusted evidence; neither Llama nor the numerical estimator establishes sensor authenticity.

| Stage and method | Input | Actual output | Next step |
| --- | --- | --- | --- |
| Awareness: declared scope and tool gate | Four-bus DC task and explicitly assumed protected measurements | Authorized tool WLS_TRUSTED_REDISPATCH | Offer permitted tool-family choices |
| Planning: bounded Llama routing | Use case and declared scope | WLS_TRUSTED_REDISPATCH | Invoke the numerical routine |
| Estimation: protected-data WLS | Three protected angles,H_T=I3 | Rank3; residual degrees of freedom0 | Construct redispatch from the estimate |
| Execution proposal: convex scalar DC redispatch | Branch limits0.35,0.18,0.35,0.35 p.u.; planning margin0.01 | u=0.12169366726990237 p.u. at node2, balanced at source | Evaluate candidate consequences |
| Simulation: DC response under known synthetic truth | Numerical candidate and the same toy physical state | Actual branch1–2 flow0.1704607615600558 p.u. | Check every branch limit |
| Verification: observability and numerical constraints | Rank,solver status and actual toy-model violations | PASS; rank3; zero modeled flow violations | Return numerical summary |
| Recovery: bounded single numerical attempt | Verification passes | No additional attempt | Ask for explanation |
| Explanation: Llama + numerical metric card | Summary and passed_modeled_checks=true | REVIEW | Keep the numerical candidate provisional |
| Operator acknowledgment: human record review | Immutable review identity, action and trust assumptions | PENDING; dispatch_authorized=false; equipment_operated=false | Request further evidence or clarification |

### Actual C4 Planning reply

Returned choice: **`WLS_TRUSTED_REDISPATCH`**.

> This tool is authorized for the given use case and scope, and it is designed for a specific DC redispatch example with trusted measurements.

### Actual C4 Explanation reply

Returned choice: **`REVIEW`**.

> The provided JSON output indicates that the numerical workflow has completed successfully, and the results are within the expected scope. The 'passed_modeled_checks' field is set to True, indicating that the modeled checks have been passed. Therefore, the choice is to REVIEW the results to ensure they are accurate and within the expected range.

### Compare against a capable conventional supervisor

| Route | Proposed injection u (p.u.) | Actual toy flow1–2 (p.u.) | Violations | Workflow outcome |
| --- | --- | --- | --- | --- |
| Compromised WLS + redispatch | 0 | 0.24000000000000002 | 1 | Numerical proposal only |
| Conventional adaptive + supplied protected measurements | 0.12169366726990237 | 0.1704607615600558 | 0 | MODEL_RECOMMEND |
| Agentic + the same supplied protected measurements | 0.12169366726990237 | 0.1704607615600558 | 0 | REVIEW; candidate provisional |

The stressed-branch limit is0.18 p.u. Protected-data recovery reduces the true toy flow by0.0695392384399442 p.u. (28.9747%) and removes the overload. That benefit belongs to the additional measurement evidence and numerical redispatch. With the same evidence, the conventional and agentic routes obtain identical numerical results; this record demonstrates **no additional Llama detection or control advantage**. The agent additionally escalates despite passed modeled checks, which may add review burden rather than remove it.

The stealth residual statistic3.9202216910315655 is below threshold15.08627246938899, just as in the nominal-noise case. A small residual means consistency with the measurement model, not absence of an attack. The trusted three-measurement set has zero residual redundancy: full rank identifies its three-state estimate, but provides no redundant chi-square detector. The simulation uses known synthetic truth only for evaluation; actual operators do not have that oracle.

The framework's observed design property is a review record that keeps evidence provenance, the chosen method, numerical checks, model coverage and the actual Llama decision together. It does not authenticate sensors, implement a field intrusion detector or prove safety of a general cyber-physical system.

Sources: `results/standard_formulations.json`; `results/standard_agent_workflow.json`, cyber calls7–8; `results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json`.

## References and evidence identity

- Continuous SAC method: [Haarnoja et al. (2018), Soft Actor-Critic](https://proceedings.mlr.press/v80/haarnoja18b.html).
- Interleaved tool/action observations: [Yao et al. (2023), ReAct](https://arxiv.org/abs/2210.03629). The tutorial uses bounded structured choices; the reference does not establish a grid-safety guarantee.
- Restoration optimization context: [Chen et al. (2018)](https://doi.org/10.1109/TPWRS.2017.2720122). The small tutorial transport MILP has its declared reduced scope.
- False-data residual limitation: [Liu, Ning and Reiter (2009)](https://doi.org/10.1145/1653662.1653666).
- State-estimation foundations: [Schweppe and Wildes (1970)](https://doi.org/10.1109/TPAS.1970.292678).
- Human decision/action allocation: [Parasuraman, Sheridan and Wickens (2000)](https://doi.org/10.1109/3468.844354).

The values and quotations above were extracted from these exact files. Their hashes identify the evidence at the time this appendix was produced; a newly executed notebook can legitimately produce different language choices and a new record.

| Evidence file under results/ | SHA-256 |
| --- | --- |
| workshop_run_opendss.json | 4dcf85386081652fa7f0b4157c3f5f513cec1b2f79567bc48b71df87c1ce408a |
| workshop_run_lindistflow3.json | 404129fd102af51b541768318d437a7a67366d6df414d469c0a6b207ff20599f |
| continuous_llama_opendss_20260927T161223523552Z.json | adaafce8f59a92e472124bfef8c0a73aa3e61fb4cc0a4137824a8865c33b6097 |
| continuous_llama_lindistflow3_20260927T161120781113Z.json | dd9e5d6a331348104f6a64b63981734a0b043345397a1a418ef43a57bd830316 |
| confirmation.json | cd4af06b5293cd0c8acf1b9ef41eb2ee9f9226c8ac73f62bfa8ea52091ebc2e4 |
| confirmation_calls.json | e2dc12a87ac15d9f1bdf683bc94124b0dfb9d52c0eb808095b0d7327ddb37e04 |
| standard_formulations.json | 473a9f7cbd7b93ce5637192d66916455893d8f236b9a20058251694766ed79e9 |
| standard_agent_workflow.json | de98ec1098394e21b00c82cc4c9dcabc849441c73b32b899227a5a5a60063af6 |

