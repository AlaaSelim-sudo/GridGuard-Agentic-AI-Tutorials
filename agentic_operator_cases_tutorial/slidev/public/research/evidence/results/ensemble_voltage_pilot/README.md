# Voltage response-selection pilot: how to read the evidence

This is a new, bounded teaching experiment. It does not replace or relabel the
archived five-stage proposal runs. The protocol fixes 24 training, 8 validation
and 12 test contexts on one supplied feeder before collecting outcomes. The
actual completed counts and file hashes are in `collection_manifest.json`.

## Roles and authority

1. Three forecast load multipliers, a current allowance and a previous control
   define an immutable synthetic operating context.
2. A fresh three-step local sensitivity MPC plan and the previously trained SAC
   actor each provide a continuous first-action proposal. Neither is an LLM.
3. Each first action receives a fresh numerical simulation and reconstructed
   voltage, current, inverter and dispatch-tracking checks. The feasible
   current-step minimum becomes the incumbent. A conservative `[0.25, 0]`
   fallback is tested only if both initial actions fail.
4. Three actual local LLMs receive the same compact initial evidence and bounded
   operation menu. They request PV increase, Q relaxation, PV decrease or KEEP.
   Their short public reasons are explanations, not private reasoning traces.
5. A selector may spend one response-action evaluation, then retain the feasible
   numerical minimum of that action and the incumbent. A separate fresh final
   solve is recorded for every possible canonical response choice.

Voting and the learned selector choose a **numerical instruction from an LLM
response**. They never grant electrical feasibility, change engineering limits,
issue an equipment command or acknowledge for an operator. The canonical
operation and context are available to the selector; this is not a trained
semantic evaluator of the explanation prose or a learned ranking of model
identity. Several models may produce the exact same instruction.

## Planning horizon versus first-action checks

The existing MPC routine records fresh checks over its three-step forecast
horizon. Its complete plan and `planning_failures` remain in `numerical/`.
The initial candidate gate and response objective in this experiment are
**first-action/current-step** checks. The compact response context does not
contain the separate plan-failure list. A passing first action must not be
described as proving robust horizon feasibility, recursive feasibility,
stability, protection coordination or global AC optimality.

The objective is
`J=(1-a)^2+0.05*b^2+10*mean((V-1.01)^2)+0.05*||[a,b]-previous||^2`.
MPC's discounted horizon objective is different from this current-step ranking
objective. A local refinement of the first step is not a demonstrated
improvement in the full MPC trajectory.

## Keep decision inputs separate from audit outcomes

- `protocol.json`: frozen cases, split, source hashes, model tags/digests and settings.
- `contexts.json`: initial checked evidence, immutable public context, catalog,
  and pretrial selector features. No response trial outcome belongs here.
- `responses.json`: actual model choice, public reason, wall time and raw-journal link.
- `llm_calls/`: complete payloads, raw local responses, token counts and server clocks.
- `counterfactuals/`: all four canonical operations independently simulated.
- `counterfactual_outcomes.json`: response-linked outcomes. Duplicate operations
  deliberately share exactly the same numerical evidence.
- `initial_model_audits.json`: first MPC/SAC actions under the planning and common audit models.
- `final_rechecks.json`: distinct final selected-model solves after retaining the
  numerical minimum, with exact-action links to the separate common AC audit.

The counterfactual table is **full-information simulator data**, not logged
deployment bandit data. A training replay must reveal only the selected
candidate's feedback at each update. The test split must remain frozen; the
validation split is separate. Full-information best-of-N evaluation is a useful
oracle/reference with a larger evaluation budget, not an equal-cost selector.

## Two model scopes and the separate AC transfer

The main experiment uses MV three-phase LinDistFlow with ideal LV aggregation.
Every initial and response action also receives a separate full-feeder OpenDSS
audit. The AC audit is kept out of MV acceptance, LLM inputs and selector reward.
An MV PASS and an AC failure can coexist because the models cover different
constraints; such an action must remain held from broader-scope operator release.

`opendss_planning/` contains independent OpenDSS MPC plans for the twelve test
contexts. `ac_transfer/` reuses those exact plans and the same saved SAC proposals,
checks both first actions afresh, collects three new actual LLM responses per
context, simulates every canonical operation and performs distinct final checks.
Its planning time is marked **reused**, not presented as newly executed in that
phase. A selector transferred from MV must remain frozen during AC evaluation.
This is a model-scope transfer comparison, not an accuracy-only experiment.

## Latency and limits

Requests are collected in batches by model to reduce local residency churn.
Each call's elapsed time is real, including any cold-load cost. Summing three
calls gives a serial response-pool cost estimate; it is not a measured contiguous
three-model end-to-end online transaction. All three model calls must be billed
for every pool-based method. Numerical collection evaluates all counterfactuals;
a one-budget selector uses only its chosen action's recorded evaluation time,
plus its distinct final recheck. Training time, MPC setup and common initial
checks should be reported separately.

The SAC actor was reward-trained on an OpenDSS response surface at nominal
current allowance. The present derated cases are a transfer test with no SAC
retraining. Forty-four MV contexts and twelve AC transfer contexts, one feeder,
one scenario seed and one selector training order do not establish statistical
or field superiority of an agentic framework, a particular model or RL routing.
