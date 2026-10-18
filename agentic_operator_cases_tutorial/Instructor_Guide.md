# Instructor Guide: Three Operator Cases

59 static slides / 120 minutes. Each case includes a five-step recorded walkthrough, a four-minute exercise and its debrief. No tables, transitions, click reveals or What to notice labels. All numerical evidence is from the labeled local teaching records.

## 1. Agentic AI: Three Operator Cases

00:00–00:30 / 0.5 minutes.

This is the follow-on to the agentic-AI foundations tutorial. We apply the ideas to three engineering decisions, rather than repeating the literature survey. The numerical examples come from the existing GridGuard teaching studies. Their models and assumptions differ: a synthetic distribution feeder, a six-node restoration transport graph, and a four-bus DC estimation fixture. None is a live utility deployment or a permission to operate equipment. All slides belong to the session. The three exercises require discussion and a decision, not software installation.

Full sources:

IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources

GridGuard project teaching materials. Classroom Labs: voltage support, six-node restoration and four-bus cyber response. Existing local GridGuard workshop; recorded numerical examples and source code. 2026; inspected 18 October 2026.
Full source: research/workshop_evidence.md

## 2. Three cases test three different kinds of evidence

00:30–02:00 / 1.5 minutes.

Ask participants to predict which evidence can fail in each case. Voltage has a model-coverage problem: a candidate can pass a reduced model and fail a broader AC audit. Restoration has an explicit objective and topology problem: maximum total load and priority service can legitimately produce different plans. Cyber has an information-trust problem: a small residual can coexist with a wrong estimated state. These are not interchangeable failure modes, so one universal success percentage is inappropriate. Keep the cases separate while reusing the habit of specifying inputs, tools, tests and the human decision.

Full sources:

GridGuard project teaching materials. Classroom Labs: voltage support, six-node restoration and four-bus cyber response. Existing local GridGuard workshop; recorded numerical examples and source code. 2026; inspected 18 October 2026.
Full source: research/workshop_evidence.md

## 3. An operator request becomes a checked study

02:00–03:30 / 1.5 minutes.

Read the workflow as responsibilities, not a claim that each box is a separate LLM. Awareness fixes the study state. Planning proposes an allowed action. Simulation produces numerical evidence. Verification tests the request, limits and evidence identity. The optimizer or repair step may suggest a new candidate within a fixed budget. A person receives the resulting advisory packet. This structure is a teaching synthesis informed by the existing classroom implementation. The engineering notebooks use a custom Python supervisor. Their shared responsibilities do not establish that they execute in LangGraph; the separate graph lab demonstrates that runtime independently. A numerical solver or fixed script may perform most of the work. The added walkthroughs expose the actual recorded choices, code calls, output values and pending human decisions. The voltage P3 workflow and the standard restoration/cyber workflow are separate dated studies. Each uses its original custom Python supervisor. The present GridGuard app has a separate LangGraph implementation; these archived records do not test that newer runtime.

Full sources:

GridGuard project teaching materials. Classroom Labs: voltage support, six-node restoration and four-bus cyber response. Existing local GridGuard workshop; recorded numerical examples and source code. 2026; inspected 18 October 2026.
Full source: research/workshop_evidence.md

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/engineering/building-effective-agents

## 4. Every result must stay attached to its inputs

03:30–05:00 / 1.5 minutes.

Use a concrete example: a voltage result at load multiplier 1.00 cannot support a changed request at 1.10 without checking applicability. Likewise, a restoration capacity change or a different measurement-trust set changes the evidence context. The classroom binding routine hashes canonicalized request, candidate and result contents. That establishes local content consistency only. It is not a digital signature, sensor authentication, or a proof of physical feasibility. The operator should be able to see the relevant identity and limits directly in the report. Do not transfer all details into a cryptographic-looking identifier that nobody can inspect.

Full sources:

GridGuard project teaching materials. Classroom Labs: voltage support, six-node restoration and four-bus cyber response. Existing local GridGuard workshop; recorded numerical examples and source code. 2026; inspected 18 October 2026.
Full source: research/workshop_evidence.md

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## 5. The three exercises end with a specific next step

05:00–06:00 / 1 minutes.

Explain the active-learning format before the first case. Give pairs one minute to read, two minutes to decide and one minute to prepare a short justification. The debrief follows as a separate slide, so the answer is not hidden behind a click or given away on the exercise slide. The choices concern progression through an advisory study, not field dispatch. Encourage participants to name the next responsible tool or human role. A valid hold decision should specify what evidence would allow progress.

Full sources:

GridGuard project teaching materials. Classroom Labs: voltage support, six-node restoration and four-bus cyber response. Existing local GridGuard workshop; recorded numerical examples and source code. 2026; inspected 18 October 2026.
Full source: research/workshop_evidence.md

## 6. Voltage support: return a command with evidence

06:00–07:30 / 1.5 minutes.

Start with the operator’s work request, not a model brand. The supplied case is one synthetic SMART-DS Greensboro feeder, uhs20_1247–udt8894. The purpose is to propose fleet inverter settings while checking the declared voltage, current and capability constraints. The command is advisory and does not reach a distribution-management system. The map establishes the study model; it does not establish field accuracy, protection coordination or operational approval. Ask learners to identify the needed inputs: load forecast, previous command, device ratings, available active power assumption, topology/model revision and requested MV/LV coverage. The controller implementation scales inverter ratings, so “available solar” is a declared modeling assumption rather than an irradiance forecast validated here. The twelve-slide path follows request → frozen contract → proposals → numerical validation → bounded repair → scope audit → human review. Evidence: voltage chapter frame V01 and Classroom_Labs.ipynb cells 2, 4 and 33; source plot figures/feeder.png.

Full sources:

Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.
Full source: https://data.openei.org/submissions/2981

GridGuard teaching materials. Instructor guide: a coherent 180-minute teaching session. Existing local workshop snapshot, reviewed 18 October 2026.
Full source: research/source_VGUIDE.html

## 7. Freeze what the two control numbers mean

07:30–09:30 / 2 minutes.

Define S_i as each inverter’s kVA rating. The implementation requests p_i=a S_i kW and q_i=b S_i kvar using one dimensionless fleet command. Negative b means reactive absorption under the injection convention. The action validator requires 0≤a≤1, |b|≤0.44 and a²+b²≤1. These are implemented teaching bounds, not universal utility settings. Network checks separately require modeled voltage magnitudes in [0.95,1.05] p.u. and current no greater than the scenario’s rating_fraction times nominal current allowance. “100% allowed-current use” means the derated allowance is fully used, not necessarily 100% nameplate current. Freeze the backend, forecast, rating fraction, previous action and model/request revision before interpreting a result. A small negative b may help high voltage in this case, but its direction and feasibility still need a model solve. The illustrated capability region is clipped to the implemented reactive band. The marker uses rounded MPC coordinates and does not prove network feasibility. Evidence: continuous_control.py _control, map_action, ContinuousPlant.solve and verify_control; Classroom_Labs.ipynb L1 cell 4.

Full sources:

GridGuard teaching materials. Continuous fleet P/Q control and classroom validation/readback helpers. Local source reviewed 18 October 2026.
Full source: research/source_VCTRL.html

GridGuard teaching materials. Agentic AI for grid operators — Classroom Labs. Executed 17 October 2026.
Full source: research/source_VNOTE.html

## 8. Numerical tools propose; the language model selects a trial

09:30–11:30 / 2 minutes.

MPC means model predictive control. Here it is a local sensitivity optimizer over H=3 quasi-static power-flow snapshots, linked by a command-movement penalty and discount 0.98. Only its first action enters the response-selection experiment. This is not a certified global optimum, dynamic stability study or robust recursive-feasibility proof. SAC means soft actor-critic: a model-free RL method. The supplied actor was trained previously using rewards from a declared OpenDSS response-surface approximation at nominal current allowance. Classroom inference uses saved weights without retraining; current derating is a transfer condition. Both tools produce candidate numerical commands. A fresh simulation and fail-closed checks decide whether a candidate can become the incumbent. Only then do actual local language models request a bounded refinement from the allowed menu. They do not solve the power flow, relax limits or grant approval. Cite the local implementation for every measured result; the MPC book and SAC paper explain the algorithm families, not performance of this feeder. Evidence: continuous_control.py optimize_mpc/sac_proposal, pilot README Roles and authority and Planning horizon versus first-action checks.

Full sources:

GridGuard teaching materials. Continuous fleet P/Q control and classroom validation/readback helpers. Local source reviewed 18 October 2026.
Full source: research/source_VCTRL.html

James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.
Full source: https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.
Full source: https://proceedings.mlr.press/v80/haarnoja18b.html

GridGuard teaching materials. Voltage response-selection pilot: how to read the evidence. Protocol frozen 27 September 2026; reviewed 18 October 2026.
Full source: research/source_VPILOT.html

## 9. Compare two freshly checked proposals

11:30–13:30 / 2 minutes.

Use the executed default L2 output in Classroom_Labs.ipynb cell 7, ID classroom-007, with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Its forecast multipliers derive from the saved base context; LOAD_SCALE=1.0 does not mean every forecast equals one. MPC returns a=0.960307,b=−0.111114 with vmin=1.023874,vmax=1.038709 and maximum allowed-current utilization 73.619901%. Saved SAC returns a=0.340066,b=+0.014024 with vmin=1.013243,vmax=1.030000 and utilization 51.679336%. Both pass the reduced MV contract. Their current-step teaching costs are 0.031104 and 0.436428, respectively. The lower-cost proposal is preferred only after constraints are checked. The cost is dimensionless J=(1−a)²+0.05b²+10 mean[(V−1.01)²]+0.05||u−u_previous||². It is not dollars or a field reliability score. A controller cost gap does not measure agent-orchestration benefit. The crop selects only the coherent current panel; the full original plot also has separately sorted voltage curves, whose equal horizontal ranks are not identical buses. L2’s timer encloses planning, saved-actor inference and checks, not isolated SAC inference.

Full sources:

GridGuard teaching materials. Agentic AI for grid operators — Classroom Labs. Executed 17 October 2026.
Full source: research/source_VNOTE.html

GridGuard teaching materials. Continuous fleet P/Q control and classroom validation/readback helpers. Local source reviewed 18 October 2026.
Full source: research/source_VCTRL.html

## 10. Turn three replies into two physical trial choices

13:30–15:30 / 2 minutes.

Deliberately switch from fresh L2 to archived original test_01, whose rating_fraction is 0.7995473229563319 rather than L2’s 0.80. The load forecast is [1.0112062191802391,1.005224985779734,1.0006905741130825], and previous command [0.2696261713643143,0]. This context has MPC incumbent [0.9603066164910677,−0.11111388575888505]. Llama3.1:8b requests INCREASE_PV_0025, giving [0.9628066164910677,−0.11111388575888505]. Llama3.2:3b and qwen2.5:7b-instruct both request RELAX_Q_10_PERCENT, giving [0.9603066164910677,−0.10000249718299654]. Group requests by physical tool and parameters before counting them: three public replies form two candidates. The two-vote candidate gets one simulator trial. Neither a majority nor a bandit score is a probability of electrical safety. The actual recorded reasons include unsupported links from Q reduction to curtailment and a “voltage stability” claim; steady-state first-action checks do not establish stability. Printing these stored replies makes no new LLM call. Evidence: contexts.json record id=test_01, catalog and case; responses.json context_id=test_01; Classroom_Labs.ipynb cell 10.

Full sources:

GridGuard teaching materials. Archived immutable voltage contexts and actual local Llama/Qwen response records. Recorded September 2026; reviewed 18 October 2026.
Full source: research/source_VARCH.html

GridGuard teaching materials. Agentic AI for grid operators — Classroom Labs. Executed 17 October 2026.
Full source: research/source_VNOTE.html

## 11. Validate the changed command and bind its evidence

15:30–17:30 / 2 minutes.

The final_rechecks.json record context_id=test_01, operation_id=RELAX_Q_10_PERCENT reports control [0.9603066164910677,−0.10000249718299654], score 0.031082078060572192, vmin 1.0244175701973093, vmax 1.039431162620944 and maximum allowed-current utilization 72.92980992911413%. All recorded voltage, line-current, inverter-capability and dispatch-tracking violation counts are zero. This is a newly checked MV first action in its archived original context. Do not subtract its score from a learner-edited L2 case. The physical verifier reconstructs findings from identified finite voltage/current arrays, freshness/convergence, scenario parameters and actual-versus-requested dispatch. The result still needs a separate request/scope check before readback. Bind the exact request, candidate and result so changed load, command or model revision invalidates old evidence. Hash matching demonstrates local identity/consistency; it is not sensor authentication or a guarantee that evidence is trustworthy. A rejected trial does not replace a valid incumbent. Recompute after every repair; a better public explanation changes no electrical evidence. Evidence: exact final_rechecks record; classroom_labs.py trial_saved_selection, bind_evidence and bound_to; notebook L4 cell 13.

Full sources:

GridGuard teaching materials. Distinct final first-action numerical rechecks after bounded response selection. Recorded September 2026.
Full source: research/source_VRECHECK.html

GridGuard teaching materials. Continuous fleet P/Q control and classroom validation/readback helpers. Local source reviewed 18 October 2026.
Full source: research/source_VCTRL.html

GridGuard teaching materials. Agentic AI for grid operators — Classroom Labs. Executed 17 October 2026.
Full source: research/source_VNOTE.html

## 12. 1. Inputs: the recorded OpenDSS case

17:30–19:30 / 2 minutes.

Explicitly start a separate, internally coherent recorded walkthrough. Do not carry over test_01 controls, costs or response-selection results. The source is workshop_run_opendss.json, agentic, case P3_current_reserve, recorded 2026-09-27T16:12:29.530248+00:00. Forecast multipliers are [1.00,0.94,1.06], previous command [0.25,0], rating_fraction=0.80, and modeled voltage bounds [0.95,1.05] p.u. The workflow receives a saved SAC proposal and a previously calculated three-snapshot MPC plan; it independently solves and checks the selected first actions during this recorded workflow. The structured contract labels the data as synthetic scenario/model-generated evidence, with no live SCADA. Both fixed and agentic supervisors have the same numerical proposals and permit at most two candidate evaluations: SAC first and one eligible MPC fallback. The language model's role is to request a permitted next numerical check. The engineering runtime is a custom Python supervisor; it is not the current GridGuard desktop LangGraph implementation. Reading the saved dashboard or notebook now makes no new LLM call or physical command.

Full sources:

GridGuard teaching materials. Recorded OpenDSS voltage workflow: P3 case, actual Llama replies, dashboard and Python source. Local executed tutorial and preserved model-call journals. 27 September 2026.
Full source: research/source_TRACE_VOLT.html

## 13. 2. Agent: request the MPC fallback

19:30–21:30 / 2 minutes.

All three replies are genuine records in continuous_llama_opendss_20260927T161223523552Z.json and are matched to this workflow. Planner, call 1 at 16:12:23.523552 UTC, returns VERIFY_SAC_FIRST: 'A numerical SAC proposal is available; its fresh first-action check has not yet been requested.' Its context contains the immutable contract, numerical MPC plan, SAC proposal, current stage, protocol and permitted actions. After numerical thermal rejection, Recovery, call 2 at 16:12:24.665244 UTC, receives failed_candidate, failed_checks=['thermal'], replacement_plan and the same contract. It returns USE_MPC_PLAN: 'The MPC plan has been generated and is eligible for a numerical check. This is the next allowed step in the recovery process.' Explanation, call 3 at 16:12:25.646676 UTC, returns REVIEW_EVIDENCE after the MPC check passes. The client times are 0.9879972, 0.8466333 and 0.9853947 seconds. These replies select bounded transitions; they do not produce the setpoints, prove feasibility, alter the 80% limit or acknowledge for an operator. The resulting fixed and agentic final controls are the same in this recorded pair. No general performance improvement is demonstrated by adding these calls.

Full sources:

GridGuard teaching materials. Recorded OpenDSS voltage workflow: P3 case, actual Llama replies, dashboard and Python source. Local executed tutorial and preserved model-call journals. 27 September 2026.
Full source: research/source_TRACE_VOLT.html

## 14. 3. Code: check the chosen command

21:30–23:30 / 2 minutes.

This excerpt displays the two original statements from src/continuous_workflow.py lines231–232. Long arguments are wrapped for readability; the builder verifies the same Python syntax tree. plant.solve receives the exact candidate control, first forecast load and current allowance. verify_control then checks the result. The following original lines233–234 also enforce backend/control identity. Earlier in this same recorded run, Llama selected VERIFY_SAC_FIRST, the fresh SAC check failed thermal limits, and Recovery selected USE_MPC_PLAN. The bounded loop then checked the existing numerical MPC candidate. The model neither writes setpoints nor changes limits. The statement excerpt is part of a function, not a standalone program. Full original source and the source/call journals are linked under TRACE_VOLT.

Full sources:

GridGuard teaching materials. Recorded OpenDSS voltage workflow: P3 case, actual Llama replies, dashboard and Python source. Local executed tutorial and preserved model-call journals. 27 September 2026.
Full source: research/source_TRACE_VOLT.html

Exact displayed excerpt (src/continuous_workflow.py, lines 231–232. Source statements; line breaks added for readability.):

```python
point = plant.solve(
    candidate['control'],
    load_mult=case.forecast_loads[0],
    rating_fraction=case.rating_fraction,
)
failures = verify_control(point, case)
```

## 15. 4. Result: SAC fails; MPC passes

23:30–25:30 / 2 minutes.

The saved SAC action is [0.33693869411945343,0.030701177120208742]. OpenDSS converges, voltage is 1.0025570904–1.0375340016 p.u., but current use is 111.9666069740% of the allowed current, with two line-current findings. It is rejected for thermal limits. The MPC fallback is [0.3040791833492598,0.04149291669866676]. A new selected-first-action solve gives P=2387.1573822298833 kW, Q=325.7379256164953 kvar, Vmin=1.001782946227172 and Vmax=1.03502551840022 p.u., current use=99.60441047658344% of the allowed current, and zero voltage/current/inverter/dispatch-tracking findings. Nominal-current utilization is 79.68352838126675%, which becomes 99.6044% when divided by the 80% allowance. Keep these denominators explicit. The workflow contains two fresh candidate evaluations and one rejection. Its recorded interval is 3.1104543 seconds, excluding the supplied precomputed controllers/training. The paired fixed workflow reaches the same final MPC control. These results establish what the numerical tools checked in one synthetic full-feeder snapshot, not a benefit caused by LLM routing, dynamic stability or protection adequacy.

Full sources:

GridGuard teaching materials. Recorded OpenDSS voltage workflow: P3 case, actual Llama replies, dashboard and Python source. Local executed tutorial and preserved model-call journals. 27 September 2026.
Full source: research/source_TRACE_VOLT.html

## 16. 5. Operator: review the exact recommendation

25:30–27:30 / 2 minutes.

The recorded final status is MODEL_RECOMMEND. Its last trace event is Operator acknowledgment, PENDING: acknowledged=False, dispatch_authorized=False and equipment_operated=False. The recommendation identity is 63408d6a0cdca791ff902746f97ef2a2d1c27d1f9456846b74ccfcacd6f97fb1. That binds the displayed case, action, modeled results and contract; it is not authenticated identity or proof that sensors are correct. The original Workshop_Operator_Dashboard.html offers a local P/Q readback, requested-current-allowance readback, scope/assumption confirmations and reviewer label. A record may be acknowledged only if its stored numerical evidence is internally consistent and the readback matches. For this result the displayed P/Q is 2387.16 kW and 325.74 kvar, with an 80% nominal-current allowance. Viewing this screenshot does not acknowledge anything. The screenshot must retain the pending state and blank readback controls. Any later dashboard acknowledgment would be a new unauthenticated local teaching record, not part of the archived experiment or permission to operate equipment. The model still omits protection, switching transients and operational authorization.

Full sources:

GridGuard teaching materials. Recorded OpenDSS voltage workflow: P3 case, actual Llama replies, dashboard and Python source. Local executed tutorial and preserved model-call journals. 27 September 2026.
Full source: research/source_TRACE_VOLT.html

## 17. Exercise: is this packet ready for the requested scope?

27:30–31:30 / 4 minutes.

Keep the answer hidden until the following debrief slide. Give pairs four minutes: one person argues for a disposition and the other audits the evidence. The figure contains the exact archived test_01 Q-reduction result, rounded for display. The full MV/LV request is a hypothetical operator requirement used to examine scope matching, not a claim that the archived experiment dispatched a full-feeder action. Ask learners to distinguish three questions: are the displayed MV numbers within the teaching bounds, does that cover the requested network, and is any equipment action authorized? Answer for the teacher: the MV physical checks pass, but the packet remains HOLD for the requested full MV/LV scope because the evidence covers only MV phases with ideal LV aggregation. A same-action full-feeder OpenDSS audit is needed. If that action fails, use an allowed numerical replan/repair and obtain new checks; do not reuse old evidence or ask the language model to declare approval. Acknowledgment cannot fill a missing scope check. No additional simulation has been run for this exercise. Accept any answer that clearly separates physical pass, scope adequacy and human authority. Evidence: recorded metrics in final_rechecks.json; operator_packet scope equality rule; Classroom_Labs.ipynb cell 33.

Full sources:

GridGuard teaching materials. Distinct final first-action numerical rechecks after bounded response selection. Recorded September 2026.
Full source: research/source_VRECHECK.html

GridGuard teaching materials. Agentic AI for grid operators — Classroom Labs. Executed 17 October 2026.
Full source: research/source_VNOTE.html

## 18. Debrief: passing one model is not enough

31:30–33:30 / 2 minutes.

Reveal the answer after pairs have reported. First acknowledge that the displayed MV voltage and current checks pass: this avoids teaching that an unfavorable decision means the calculations were wrong. The mismatch is coverage. A request for full supplied MV/LV needs evidence from that scope. A same-action broader-model audit asks whether this exact command survives changed equations and constraint coverage. A separate AC MPC solve asks what a controller using that broader model would recommend; it changes the action and therefore needs a new final check. Do not call that change an LLM improvement. Keep the failed trial and scope limitation in the final packet. In the actual classroom L12 code, the full-scope packet has evidence_matches=True and engineering_pass=True but scope_matches=False, so it remains HOLD and cannot be acknowledged. For an explicitly MV-scoped teaching request, the same bound result can be READY_FOR_READBACK. Wrong recommendation ID or missing operator name rejects readback. A valid local acknowledgment still has equipment_dispatch=False. This is a semantic guard in a teaching implementation, not a certified live control-room permission system. Evidence: Classroom_Labs.ipynb cell 33 stored output and src/classroom_labs.py operator_packet/acknowledge.

Full sources:

GridGuard teaching materials. Agentic AI for grid operators — Classroom Labs. Executed 17 October 2026.
Full source: research/source_VNOTE.html

GridGuard teaching materials. Continuous fleet P/Q control and classroom validation/readback helpers. Local source reviewed 18 October 2026.
Full source: research/source_VCTRL.html

## 19. Check the same actions against broader model coverage

33:30–35:30 / 2 minutes.

Use the historical twelve-context comparison, not the default L5 notebook cell as evidence for all twelve outcomes. The primary frozen learned selector and majority both have final_model_passes=12 and final_ac_passes=0 on the MV test split in selector_analysis.json. The exact retained actions were independently audited in full-feeder OpenDSS. AC audit outcomes were excluded from MV LLM inputs, acceptance and selector reward; do not imply that the MV selector anticipated them. The broad model changes both equations and covered network/constraints, so this is not an isolated numerical-accuracy test. For a concrete initial-action example, test_01’s original MV-MPC command has MV vmax=1.0387087638 and allowed-current utilization=73.6615825%, yet its same-action AC audit reports vmax=1.0898278087, allowed-current utilization=347.2530224%, seventeen high-voltage findings and eleven line-current findings. That example is the INITIAL_MPC audit, not the later Q-reduction record. Independent AC MPC replanning gives first actions passing 12/12 AC checks in these recorded contexts. Neither result is a field safety certificate or a claim of global AC optimality. Evidence: selector_analysis test summaries and ac_transfer summaries; initial_model_audits test_01/INITIAL_MPC; heldout_model_comparison.json.

Full sources:

GridGuard teaching materials. Frozen response-selector comparison: held-out MV test and paired full-feeder AC transfer. Protocol frozen 27 September 2026.
Full source: research/source_VANAL.html

GridGuard teaching materials. Paired same-action full-feeder audit and independent OpenDSS MPC first-action plans. Recorded September 2026.
Full source: research/source_VAC.html

GridGuard teaching materials. Voltage response-selection pilot: how to read the evidence. Protocol frozen 27 September 2026; reviewed 18 October 2026.
Full source: research/source_VPILOT.html

## 20. The historical selector ties a simpler voting rule

35:30–37:30 / 2 minutes.

LinUCB is a linear contextual bandit: it scores which permitted operation to test from context and canonical-action features. It does not train the LLMs or evaluate private reasoning. There are 24 training contexts, 8 validation contexts and 12 held-out tests. The primary selector has 24 selected-feedback updates and remains frozen during validation/test. The actual test summaries give majority_vote and learned_selector identical mean final objective 0.0339847924178626. paired_test_comparison against majority_vote reports learned_better=0, ties=12 and learned_worse=0. The predeclared fixed numerical refinement is INCREASE_PV_0025, with mean 0.0340065598125857. A posthoc fixed Q-reduction rule reproduces the vote/learner choices without LLM calls; label that rule diagnostic, not a predeclared baseline. The tiny cost improvement over one fixed action does not establish a general learned or language-model benefit. All common-pool selectors incur three response calls. Reconstructed serial mean time is 8.119085 seconds for the learned selector versus 3.326839 for the fixed numerical method; these are sums of recorded components, not a measured online control-room transaction. Five training orders reuse the same contexts and do not create five independent datasets. Evidence: selector_analysis.json protocol, test.summaries and paired_test_comparison; README Latency and limits.

Full sources:

GridGuard teaching materials. Frozen response-selector comparison: held-out MV test and paired full-feeder AC transfer. Protocol frozen 27 September 2026.
Full source: research/source_VANAL.html

GridGuard teaching materials. Archived immutable voltage contexts and actual local Llama/Qwen response records. Recorded September 2026; reviewed 18 October 2026.
Full source: research/source_VARCH.html

## 21. Replan with the model that covers the request

37:30–39:30 / 2 minutes.

This single-panel original plot is figures/selector_E6.png. It compares the active component a of the original MV LinDistFlow incumbent with an independent full-feeder OpenDSS MPC first action for each of the same twelve contexts. It is not a percent-error plot or an LLM-selector comparison. For archived test_01, heldout_model_comparison.json gives AC first action [0.3060522326419636,+0.027696908967886763], vmin=1.0005276166702253, vmax=1.0330024384102277 and maximum allowed-current utilization=99.87273873689041%; the check passes with no recorded violations. All twelve independently AC-planned first actions pass their snapshot gate. Raw saved SAC passes only one of the twelve full AC checks. The AC transfer reuses already computed MPC plans and marks the planning time as reused; it does not retrain or tune the selector. Its final mean J remains 0.4713848786592687 for both majority and learner, compared with fixed numerical 0.47112137693022893 and uniform response 0.47110513098466494. Thus the learned selector does not beat those simpler comparators here. Do not directly rank MV and AC objective means: the voltage sets and covered constraints differ. A passing first action proves neither full-horizon feasibility nor stability. Evidence: heldout_model_comparison array test_01 opendss_mpc; selector_analysis ac_transfer.summaries mpc_only/raw_sac and comparators.

Full sources:

GridGuard teaching materials. Paired same-action full-feeder audit and independent OpenDSS MPC first-action plans. Recorded September 2026.
Full source: research/source_VAC.html

GridGuard teaching materials. Frozen response-selector comparison: held-out MV test and paired full-feeder AC transfer. Protocol frozen 27 September 2026.
Full source: research/source_VANAL.html

## 22. Return one scoped packet for human review

39:30–42:00 / 2.5 minutes.

Ask a learner to narrate the complete operator path: state the request; freeze case and allowed actions; obtain MPC/SAC proposals; calculate fresh evidence; verify every physical bound; test any permitted refinement; audit the requested model scope; and return the exact evidence packet. The packet must preserve the original command, source/model identity, failed trials, current/voltage margins, limitations and a recommendation identifier. A human reviews the specific packet and reads back that identifier with an operator name. In the implementation, valid acknowledgment changes only the local advisory record. It cannot invoke a live DMS, change a setpoint or overrule a failed scope check. The actual L12 output shows a full MV/LV request remaining HOLD despite engineering_pass=True under MV scope, while an explicitly MV teaching request can be acknowledged. A wrong ID is rejected; a correct readback still leaves equipment_dispatch=False. Hashes establish consistency of the local request/candidate/result binding, not external authenticity. End with the measured lesson: numerical tools supplied settings; language supplied bounded trial instructions; the MV learner tied voting; a broader model changed admissibility. No general advantage of more LLMs, a learned selector or this teaching architecture has been demonstrated. Evidence: notebook cell 33 and source operator_packet/acknowledge.

Full sources:

GridGuard teaching materials. Agentic AI for grid operators — Classroom Labs. Executed 17 October 2026.
Full source: research/source_VNOTE.html

GridGuard teaching materials. Continuous fleet P/Q control and classroom validation/readback helpers. Local source reviewed 18 October 2026.
Full source: research/source_VCTRL.html

GridGuard teaching materials. Instructor guide: a coherent 180-minute teaching session. Existing local workshop snapshot, reviewed 18 October 2026.
Full source: research/source_VGUIDE.html

## 23. Restoration starts with a specific operator request

42:00–44:00 / 2 minutes.

Read the operator request before naming a solver: “Restore eligible load after fault 1–2. Keep the fault isolated. Use the declared ratings and priorities; return a proposal for review.” The explicit request is a teaching contract, not an actual dispatch instruction. T1 is a tutorial snapshot label added for this follow-on module. The tools may select a plan, calculate and report evidence; they have no physical switching authority. The six-node transport example is separate from the archived Greensboro feeder and its ampere-based bypass catalog. Spend two minutes identifying the goal, constraints and expected output.

Full sources:

GridGuard teaching materials. Agentic AI for Grid Operators: restoration teaching chapter, frames R01–R18. Local existing workshop teaching edition. 17 October 2026 edition.
Full source: research/source_RST01.html

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

## 24. Lock the fault, topology and load priorities

44:00–46:00 / 2 minutes.

Demand is [0,40,60,70,50,30] kW at nodes 0–5. Priority weights are [0,1,10,1,1,10]. Healthy source edge 0–1 has 300 kW capacity; faulted edge 1–2 is unavailable even though its nominal capacity is 250 kW. Sections 2–3, 3–4 and 2–5 each have 250 kW capacity. Tie 1–5 is 100 kW; tie 0–4 is the capacity varied in the experiment. This map fixes a transparent classroom topology; it is not an extracted Greensboro switching diagram. Ask learners to identify the isolated edge and the two critical loads. Fault isolation is an assumed input to this study, not a protection diagnosis performed by the agent.

Full sources:

GridGuard teaching materials. Agentic AI for Grid Operators: restoration teaching chapter, frames R01–R18. Local existing workshop teaching edition. 17 October 2026 edition.
Full source: research/source_RST01.html

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

## 25. Trace the routes before choosing a pickup plan

46:00–48:00 / 2 minutes.

Trace the source-to-critical-node path. The 100 kW tie must carry downstream load assigned behind it; node 1’s 40 kW is upstream of that bottleneck. The 40 kW tie alone cannot serve the indivisible 50 kW load at node 4. Local load pickup is all-or-nothing. A bus can be energized for transit while its local load remains disconnected; energized and served are different decisions. The optional arrows illustrate static paths only. They neither tell a crew which device to operate first nor establish interlocks, dead-line checks, protection coordination or equipment status.

Full sources:

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

## 26. More restored kW can mean less critical service

48:00–50:00 / 2 minutes.

Behind tie 1–5, critical loads 2 and 5 require 60+30=90 kW. Add 40 kW at node 1 upstream: 130 total and 90 critical. The unweighted choice serves loads 3 and 5 behind that tie: 70+30=100 kW, plus the same upstream 40, giving 140 total but 30 critical. Weights 10 for nodes 2 and 5 produce scores 940 versus 410 weighted kW; these are priority scores, not actual power. A finite weight of ten is not universal lexicographic critical-first service. The comparison changes the objective, so it does not measure an LLM benefit. Both methods are conventional exact optimizers on this fixture.

Full sources:

GridGuard teaching materials. Agentic AI for Grid Operators: restoration teaching chapter, frames R01–R18. Local existing workshop teaching edition. 17 October 2026 edition.
Full source: research/source_RST01.html

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

## 27. Ask the solver for a plan tied to this case

50:00–52:00 / 2 minutes.

The highlighted plan uses source_healthy, tie_15 and section_25. Flow is 130 kW on 0–1, 90 on 1–5 and 60 from 5 to 2. The source-file orientation of section_25 is 2→5, so its signed flow is −60 kW. Negative flow is a direction convention, not a violation. Nodes 3 and 4 remain unenergized in this particular minimal-edge plan. The MILP first maximizes priority-weighted pickup, then preserves that optimum while minimizing energized branch count with a small index tie-breaker. This second solve is not a minimum switching-operation sequence. Different feasible or optimal edge sets can exist; the figure states an explicit checked plan rather than claiming uniqueness.

Full sources:

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

## 28. Check capacity, source paths and the objective

52:00–54:00 / 2 minutes.

The model uses separate binary variables for energized nodes, picked-up loads and closed edges. Pickup requires an energized node; a selected edge requires energized endpoints. Fictitious commodity flow establishes source connectivity, and the edge count then enforces a tree. Counting edges alone is insufficient. The fictitious flow is not electrical kW. Electrical transport balance and signed capacity inequalities are checked separately. The actual independent routine enumerates pickup and edge choices, verifies source reachability/tree structure and branch demand, and compares the weighted optimum. This is tractable because the fixture is tiny. Agreement validates the finite transport calculation, not the coverage of AC voltage, reactive power, losses, protection or switching dynamics. Wang et al. sections III–IV explain why reachability and edge count are distinct requirements.

Full sources:

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.
Full source: https://arxiv.org/abs/1912.05185v3
Full paper: https://arxiv.org/pdf/1912.05185v3

## 29. A higher tie rating does not always restore another load

54:00–56:00 / 2 minutes.

Inspect both panels and the discrete markers. The saved executed L6 cell reports weighted total/critical service 130/90,180/90,200/90,200/90,250/90 at tie capacities 40,60,80,100,120 kW. The unweighted totals/critical values are 140/30,190/30,200/90,200/90,250/90. Fresh exhaustive enumeration of the same source functions reconfirmed those values for this module. The saved notebook’s MILP agrees with exhaustive checks; no fresh SciPy MILP is claimed here. At 80/100, one feasible plan supplies nodes 2 and 5 through the 100 kW tie (90 kW), node 3 through tie 0–4 and edge 4–3 (70 kW), and node 1 upstream (40 kW); node 4 is energized for transit but its own 50 kW load is shed. These static paths explain the plateau and are not a switching sequence.

Full sources:

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

GridGuard teaching materials. Classroom restoration capacity sweep: total and critical service. Original computed local scientific figure. 17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST05.html

## 30. 1. Inputs: the six-node restoration task

56:00–58:00 / 2 minutes.

Spend the first minute identifying what is supplied rather than inferred. The original Awareness response contains use_case=restoration, authorized_tool=RESTORATION_MILP, the six-node active-power transport scope, backend=separate_reduced_teaching_model, and approved transparent simulation fixtures. It does not contain live utility measurements or a free-text operator request. The tie rating is fixed by numerical_tool at solve_restoration_milp(100.), not selected by Llama. This is the same graph family as our classroom example, with tie 0–4 now at 100 kW rather than the initial 40 kW. Tie 1–5 remains 100 kW; fault 1–2 remains unavailable. Full evidence: C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json, runs[5], case=restoration, supervisor=agentic, trace[0]. Recorded 21 September 2026. Matching executed display: Standard_Formulations.ipynb, zero-based cell 19, id e3659785, execution_count 8. Actual model journal: results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json, call 5 context. The screenshot is a crop of this saved notebook output, not a fresh execution or a utility control-room deployment.

Full sources:

GridGuard teaching materials. Recorded six-node restoration workflow: actual Llama routing, MILP evidence and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_REST.html

## 31. 2. Agent: choose the authorized MILP

58:00–60:00 / 2 minutes.

Read the exact choice before the explanation. Journal call 5 has role Planning and model llama3.1:8b. Its supplied schema allows VOLTVAR_OPF, RESTORATION_MILP, WLS_TRUSTED_REDISPATCH or REVIEW. The returned choice is RESTORATION_MILP; the returned reason says the authorized tool is suitable for load pickup and energized-tree selection. Because the authorized tool is already included in the input, this demonstrates bounded routing, not independent tool discovery. The actual provider response is schema-constrained JSON in an Ollama chat message. It is not a native provider tool_calls message. Python compares the choice with TOOLS[case]; a different family would stop this route before numerical execution. The wrapper, not the language model, fixes the tie capacity and calls the optimizer. Exact evidence: C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json, runs[5].trace[1].response.routing; original journal results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json, call_id 5, zero-based index 4. Matching notebook: Standard_Formulations.ipynb, cell 19, Planning — SOLVED details. Current src/standard_agent_workflow.py has the same SHA-256 recorded in the run metadata.

Full sources:

GridGuard teaching materials. Recorded six-node restoration workflow: actual Llama routing, MILP evidence and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_REST.html

## 32. 3. Code: solve and check the pickup plan

60:00–62:00 / 2 minutes.

The display selects the original statements at src/standard_agent_workflow.py lines80 and83. The intervening summary extraction is omitted and disclosed by the noncontiguous line citation. Only line breaks and indentation change; the builder verifies equivalent Python syntax trees. solve_restoration_milp(100.) fixes tie0–4 capacity at100 kW in the same six-node graph taught here. accepted requires both MILP success and independent enumeration agreement. This is a graph/transport check, with no AC voltage, protection or temporal switching certificate. Llama only routes the structured input to its already authorized tool. Both fixed and agentic supervisors run the same numerical calculation. Full original function and result/journal are linked under TRACE_REST.

Full sources:

GridGuard teaching materials. Recorded six-node restoration workflow: actual Llama routing, MILP evidence and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_REST.html

Exact displayed excerpt (src/standard_agent_workflow.py, lines 80, 83. Source statements; line breaks added for readability.):

```python
result = solve_restoration_milp(100.)
accepted = bool(
    result['milp']['success']
    and result['agreement']
)
```

## 33. 4. Result: 200 kW total, 90 kW critical

62:00–64:00 / 2 minutes.

Connect the pickup vector [0,1,1,1,0,1] to nodes 1,2,3,5 and their demands 40+60+70+30=200 kW. Critical nodes 2 and 5 contribute 60+30=90 kW. The weighted objective is 1010 weighted kW, a priority score rather than physical power. Selected edges are source_healthy, section_34, section_25, tie_04 and tie_15; the reported MILP gap is 0. Solver success and independent_enumeration_agreement are both true. Node 4 can be energized for transit while its own 50 kW load is not picked up. The fixed comparator uses identical numerical parameters and returns the same summary: no numerical advantage from Llama is established. Exact evidence: C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json, runs[5].summary and trace[4] for the agentic case; runs[4] for the fixed comparator. Matching executed output: Standard_Formulations.ipynb, cell 19, Planning/Execution proposal and Verification details. Recovery is NOT_NEEDED with additional_attempts=0; do not claim agent repair. The evidence covers discrete pickup, source connectivity, radial graph flow and stated capacities. It does not verify AC voltage, protection, field isolation or a switching sequence.

Full sources:

GridGuard teaching materials. Recorded six-node restoration workflow: actual Llama routing, MILP evidence and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_REST.html

## 34. 5. Operator: the record requires review

64:00–66:00 / 2 minutes.

Read the enum and the returned prose separately. Actual journal call 6 returns choice=REVIEW. Its reason describes successful modeled checks, 200 kW served and 90 kW critical service, then says the results should be reviewed. The wrapper deliberately treats this choice as a hold on its recommendation: src/standard_agent_workflow.py lines 134–141 sets accepted=False when report.choice is REVIEW. Final status is REVIEW. This does not prove the numerical plan is infeasible. The same fixed numerical route ends MODEL_RECOMMEND, which also requires human review and is not dispatch. Exact record: C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json, runs[5].trace[6], trace[7] and status. Actual reply: results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json, call_id 6, zero-based index 5. The final recorded human stage says PENDING, acknowledged=false, dispatch_authorized=false and equipment_operated=false. No actual human acceptance or rejection is recorded. The second bullet is a proposed operator response for discussion, not a historical human decision. Request whatever current AC, equipment-status, protection and procedural evidence the intended operation requires; approval of a classroom calculation grants no switching authority. This recorded case demonstrates integration and an explanation-interface limitation, not numerical improvement, successful repair or measured operator-time savings.

Full sources:

GridGuard teaching materials. Recorded six-node restoration workflow: actual Llama routing, MILP evidence and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_REST.html

## 35. A changed topology or rating makes old evidence stale

66:00–68:00 / 2 minutes.

Actual L7 binds request, candidate and result using SHA-256 digests, then changes capacity from 40 to 20 kW and revision from 1 to 2; bound_to returns True then False. This module additionally executes the same unmodified binding functions on a request containing the full graph snapshot and topology_revision. It removes unused section_23 and changes T1/revision1 to T2/revision2; old evidence returns False. The previous plan did not use that branch, illustrating why identity failure does not itself establish physical infeasibility. The explicit graph snapshot is essential: a hash can only bind fields that are included. Hashes do not authenticate the data source, prove measurement freshness or grant operational authority. HOLD the old recommendation and obtain fresh checks under the changed request.

Full sources:

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Evidence digest, binding and contract matching functions. Local classroom implementation. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST04.html

GridGuard teaching materials. Fresh restoration enumeration and explicit topology-binding teaching check. Local reproducible teaching evidence. 18 October2026.
Full source: research/source_RST06.html

## 36. Give the operator a packet that can be checked and read back

68:00–70:00 / 2 minutes.

An example readback is: “For topology T1, fault 1–2 isolated, tie 1–5 at 100 kW and tie 0–4 at 40 kW, I understand this proposes serving nodes 1,2,5:130 kW total and 90 critical. Transport and enumeration checks match this candidate. AC/security and switching authorization are outside this packet.” The packet also records shed loads, limitations and any unsuccessful checks. A readback is a tutorial communication step, not proof that a field procedure has been completed. Acceptance of the calculation must remain separate from switching authorization. Missing status, failed binding, failed checks or conflicting instructions produce HOLD rather than an action request.

Full sources:

GridGuard teaching materials. Agentic AI for Grid Operators: restoration teaching chapter, frames R01–R18. Local existing workshop teaching edition. 17 October 2026 edition.
Full source: research/source_RST01.html

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Evidence digest, binding and contract matching functions. Local classroom implementation. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST04.html

## 37. Exercise: choose the service policy and handle a changed case

70:00–74:00 / 4 minutes.

Allow the complete four minutes. First minute: identify demands and which loads are critical. Second minute: calculate both service outcomes and explain the preferred policy. Third minute: check a feasible source path and the 100 kW bottleneck. Fourth minute: decide what a topology change does to the evidence. Answers: 2+5 gives90 kW through the tie, plus upstream40 =130 total/90 critical. 3+5 gives100 through the tie, plus40 =140 total/30 critical. The declared priority-weighted policy chooses the first outcome. Fault1–2 cannot be reclosed. A topology change requires HOLD of the old bound packet and a new check; it does not by itself prove the old candidate infeasible. No participant should invent a field switching order from the static map. Keep answers off this exercise slide.

Full sources:

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

GridGuard teaching materials. Evidence digest, binding and contract matching functions. Local classroom implementation. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST04.html

## 38. Debrief: keep the priority and the evidence current

74:00–76:00 / 2 minutes.

Spend the first minute asking one pair to explain the arithmetic and the 100 kW tie budget. Use the second minute to explain the stale-evidence response. The difference between130 and140 kW is not a solver error: objectives differ. The original critical weighting yields940 versus410 weighted kW in these example plans. It is not a measured benefit of an LLM. A correct numerical answer from the old request is not current evidence after the request changes. If a learner says “the old plan is definitely infeasible,” correct that: changed identity requires rechecking; only fresh engineering evaluation answers feasibility. A finite priority weight does not guarantee universal strict priority.

Full sources:

GridGuard teaching materials. Classroom Labs: L6 restoration sweep and L7 changed-contract binding. Local executed Jupyter notebook. 17 October 2026 teaching edition; inspected18 October2026.
Full source: research/source_RST02.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

GridGuard teaching materials. Evidence digest, binding and contract matching functions. Local classroom implementation. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST04.html

GridGuard teaching materials. Fresh restoration enumeration and explicit topology-binding teaching check. Local reproducible teaching evidence. 18 October2026.
Full source: research/source_RST06.html

## 39. Stop at the boundary of the model and the operator’s authority

76:00–78:00 / 2 minutes.

Conclude with a scope readback. The agent can preserve the requested priorities, select allowed tools, assemble evidence, detect a stale binding and ask for review. The conventional optimizer chooses a transport plan; no field improvement is established by this case. A larger real restoration model may need three-phase AC checks, cold-load pickup, DER availability, dynamic limits, protection coordination and a time-ordered procedure. Chen et al. is a background reference on sequential restoration, not the source of these six-node numbers. Do not import the separate archived feeder’s ampere ratings, served-kW figures or Llama latencies into this module. The next case can ask what happens when the measurements feeding a correct optimizer are wrong.

Full sources:

GridGuard teaching materials. Agentic AI for Grid Operators: restoration teaching chapter, frames R01–R18. Local existing workshop teaching edition. 17 October 2026 edition.
Full source: research/source_RST01.html

GridGuard teaching materials. Six-node restoration graph, MILP and exhaustive enumeration implementation. Local Python source and saved numerical evidence. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST03.html

GridGuard teaching materials. Evidence digest, binding and contract matching functions. Local classroom implementation. Existing17 October2026 teaching edition; inspected18 October2026.
Full source: research/source_RST04.html

Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.
Full source: https://doi.org/10.1109/TPWRS.2017.2720122

## 40. Freeze the assessment before changing control

78:00–79:30 / 1.5 minutes.

Set the operator problem: a network estimate suggests that no corrective action is needed, but the provenance of some measurements is unresolved. Before asking for a new control, record the reading set, its time, trust flags, topology, model H, noise scales, operating limits and proposed action. A repeated calculation on changed inputs is a new assessment. The three horizontal tracks make this shared context visible; they do not claim that a hash, an LLM or the workshop code authenticates sensors. In the laboratory, trusted_response returns HOLD and dispatch=false when an independent trusted state is unavailable. A residual alarm may reflect a bad reading, topology or model error, or an adversarial change. It alone identifies none of these causes. The upcoming Hc example is a defensive negative control on synthetic data, not a live-system test.

Full sources:

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

GridGuard teaching materials. Workshop Instructor Guide and Cyber Teaching Chapter: evidence scope and operator interpretation. Local instructor material. Reviewed 18 October 2026.
Full source: research/source_CY07.html

## 41. Eight readings describe three unknown angles

79:30–81:30 / 2 minutes.

Bus 0 is the reference, with angle zero. The unknown vector is x=(theta1,theta2,theta3). The four line susceptance coefficients are 10, 8, 10 and 5 for reference branches 01, 12, 23 and 03. The linear measurement matrix stacks four flow rows F, three injection rows B, and an angle-1 row. Its rank is three. Thus m=8 measurements minus rank(H)=3 gives five residual degrees of freedom. The arrows define algebraic reference directions; actual flow can be negative. In this fixed DC approximation, active flow is linear in angle differences. It omits voltage magnitude, reactive power, losses, protection behavior and AC constraints. Do not transfer this result to the distribution-feeder model used in the voltage case. Ask participants which extra measurements provide consistency information beyond the minimum needed to solve for the angles.

Full sources:

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678

## 42. WLS finds the best common explanation

81:30–84:00 / 2.5 minutes.

Start with the scalar picture. Two equally precise readings of one quantity are 9 and 11. Choosing 10 leaves residuals -1 and +1; moving the estimate toward either reading increases the total squared mismatch. WLS extends this idea to the network predictions Hx. It minimizes the sum over readings of ((z_j-(Hx)_j)/sigma_j)^2. Here z is the reading vector, H maps angles to expected readings, and sigma_j is the assumed standard deviation of the reading noise. A smaller sigma creates a larger penalty for the same raw mismatch. It expresses the estimator's stated precision model, not a cybersecurity trust judgment. The supplied code solves the full-rank weighted problem numerically using least squares. Flow noise scales are 0.004 p.u., injection noise scales 0.006 p.u., and the angle-1 noise scale is 0.0005 rad. Do not interpret unequal weights as proof that a channel is authentic.

Full sources:

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678

## 43. A residual alarm checks consistency

84:00–86:00 / 2 minutes.

The statistic is J=r^T R^-1 r, where r=z-Hxhat and R is the diagonal matrix of the assumed noise variances. Under the stated linear Gaussian model, correct H and covariance, and full column rank, the minimized statistic has m-rank(H)=5 degrees of freedom. The 99th percentile is 15.0862724694; use 15.0863 on the slide. Nominal J is 3.9202216910. Alpha=0.01 is a nominal upper-tail false-alarm probability under those assumptions. It is not a 99% chance that the data are safe, nor the probability that an attacker is present. An isolated +0.08 p.u. change on flow12 produces J=277.4974469045 and an alarm in this seeded run. That is evidence of inconsistency, not an identification of the cause or a guarantee that all coordinated errors will be detected.

Full sources:

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

NIST/SEMATECH. e-Handbook of Statistical Methods, Section 1.3.6.7.4: Critical Values of the Chi-Square Distribution. National Institute of Standards and Technology. Accessed 18 October 2026.
Full source: https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm

## 44. Coordinated changes can leave the residual unchanged

86:00–88:00 / 2 minutes.

Return to the scalar illustration: shifting both readings by three moves their best common estimate by three, while the two residuals remain -1 and +1. The linear network identity is z'=z+Hc, xhat'=xhat+c and r'=r when the same full-rank H and weights are used. Here c is a shift in the inferred angle state; Hc is the corresponding change in model predictions. Liu, Ning and Reiter establish this limitation of residual-based bad-data detection. Their result has specific access and model assumptions; it is not a claim that any attacker can alter every utility state estimate. Protected measurements restrict which changes are possible. The synthetic workshop deliberately supplies a matching coordinated perturbation as a negative control, so it can test whether a residual-only workflow mistakes consistency for trust. We do not discuss targeting real measurement channels. The operator lesson is to seek independent evidence when the trust premise is unresolved, even if the residual test is quiet.

Full sources:

Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.
Full source: https://doi.org/10.1145/1952982.1952995
Full paper: https://reitermk.github.io/papers/2011/TISSEC2.pdf

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

## 45. A quiet residual can hide a wrong inferred state

88:00–90:00 / 2 minutes.

Read the panels together. At scale zero both cases start from the same seeded noisy readings. Increasing one isolated flow bias raises the weighted residual and eventually crosses the threshold. The coordinated Hc changes leave J essentially unchanged while their state-error norm grows. At scale one the nominal and coordinated statistics are both 3.92022 to displayed precision, but the coordinated state error is 0.0267799957 rad, versus 0.0002374314 rad for nominal noise. The left panel's symmetric-log scale accommodates small and large statistics. The right panel compares the estimate with the known state supplied by the synthetic experiment. A real operator does not have that exact ground truth as an online test input. This is a negative-control demonstration of a detector limitation, not a statistical field evaluation, attack prevalence estimate or measurement of an LLM's detection capability.

Full sources:

GridGuard teaching materials. Classroom Labs L8–L9: cyber consistency sweep and trusted response gate. Local workshop notebook and companion lab functions. Reviewed 18 October 2026.
Full source: research/source_CY05.html

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.
Full source: https://doi.org/10.1145/1952982.1952995
Full paper: https://reitermk.github.io/papers/2011/TISSEC2.pdf

## 46. Independent trusted readings change the evidence

90:00–92:00 / 2 minutes.

The protected recovery uses H_T=I_3 with three angle readings. Each has assumed noise standard deviation 0.00005 rad and a separate seeded noise realization. Because the measurement count and rank are both three, the fit is exactly determined: residual degrees of freedom are zero, the residual is zero up to numerical precision, and the code supplies no chi-square threshold or alarm. The trust argument comes from an external assumption about these channels, not their zero residual. The workshop does not implement sensor authentication, prove channel independence operationally, or ask an LLM to decide authenticity. The trusted_response wrapper returns HOLD when the protected set is unavailable. With the set available, it can return a numerical proposal, still with dispatch=false. In an operational design, the utility would need to justify provenance, independence, time alignment and applicability before using a replacement evidence set.

Full sources:

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

GridGuard teaching materials. Classroom Labs L8–L9: cyber consistency sweep and trusted response gate. Local workshop notebook and companion lab functions. Reviewed 18 October 2026.
Full source: research/source_CY05.html

## 47. A small QP proposes a limited correction

92:00–94:30 / 2.5 minutes.

The optimizer chooses one nonnegative flexible injection u at bus 2, balanced by bus 0. The objective 0.5u^2 favors a smaller action. It is a quadratic program because this objective is quadratic while the flow constraints and action bounds are linear. Bounds are 0<=u<=0.5 p.u. Every predicted branch flow must lie between minus and plus its rating less a 0.01 p.u. planning margin. Ratings are [0.35,0.18,0.35,0.35] p.u. for branches 01,12,23,03. Flow changes use g=F B^-1 e2, with g12=-4/7, so increasing u reduces the positive 1-to-2 flow. For this protected noisy estimate the binding constraint is predicted flow12=0.17, producing u=0.1216936673 and objective 0.0074046743. This differs from the 0.1225 noiseless arithmetic example in the longer chapter. The code solves the small QP with SLSQP and independently rechecks finite values, action bounds and all predicted constraints. A failed solve or check produces HOLD.

Full sources:

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

## 48. Check the consequences on every branch

94:30–96:30 / 2 minutes.

Both sets of bars are evaluated using the known synthetic state after their respective actions, not the measurement estimates themselves. The action based on the coordinated corrupt estimate is u=0, leaving actual flow12 at 0.24, above its 0.18 rating. The trusted set selects u=0.1216936673. Its predicted flow12 is 0.170000; the independent offline physical audit gives actual flow12=0.1704607616. All four actual branch flows satisfy their physical ratings in this fixed toy network. The 0.01 planning margin accommodates the small protected-noise difference in this run; it is not a general robust uncertainty guarantee. Online, the code checks predicted constraints and finite values. Exact actual-state values are retained for experimental evaluation, not assumed to be an available online measurement or an operational authorization gate. The result demonstrates the value of better evidence plus a constrained solver, without establishing a benefit from an LLM.

Full sources:

GridGuard teaching materials. Trusted control comparison: all-branch actual-flow audit for two four-bus DC decisions. Local workshop computed figure. Reviewed 18 October 2026.
Full source: research/source_CY06.html

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

## 49. 1. Inputs: a declared four-bus DC task

96:30–98:30 / 2 minutes.

Use one coherent archived run throughout these five slides. Source: C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json, runs entry with case='cyber' and supervisor='agentic', review_id=4a10da2aa66efaa3c1f39dae3b67372c384dbf66a297de9ed01841f6ba9c4fd9. Exact raw model journal: results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json, call_id=7, context (file lines 394–401). The context contains use_case='cyber', authorized_tool='WLS_TRUSTED_REDISPATCH', scope='Four-bus DC measurement/control example with explicitly assumed trusted sensors', backend='separate_reduced_teaching_model', and approved_inputs='Supplied transparent simulation fixtures; no live utility measurements'. It is a structured specification, not a recorded natural-language request. The tool authorization is already supplied, so this run does not test discovery of the right engineering method from an ambiguous request. The second bullet explains the associated numerical fixture rather than adding fields to the model's recorded input: run_wls_demo supplies three protected angle channels, assumes their trust, and uses known synthetic truth to audit consequences. The historical standard-stage wrapper also uses that offline violation count in its teaching verification; it is not an operational truth oracle. Preserve this distinction when presenting the screenshot. The four-bus DC case omits AC voltage magnitudes, reactive power, protection, authentication and live actuation. An illustrative operator question may be spoken separately, but must not be presented as an archived prompt.

Full sources:

GridGuard teaching materials. Recorded four-bus cyber workflow: actual Llama routing, trusted-state correction and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_CYBER.html

## 50. 2. Agent: choose the authorized estimator

98:30–100:30 / 2 minutes.

Exact source: C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json, call_id=7 (Planning), raw_response.message.content at line 432 and parsed response at lines 444–449. Exact reply: {"choice":"WLS_TRUSTED_REDISPATCH","reason":"This tool is authorized for the given use case and scope, and it is designed for a specific DC redispatch example with trusted measurements."}. The model is llama3.1:8b; the record contains the raw local Ollama response, with no error. This is an actual recorded LLM call from 21 September 2026, not a newly generated reply and not an LLM invocation when the notebook is read. The request uses http://localhost:11434/api/chat, a constrained JSON response schema, temperature 0 and seed 11; implementation is src/standard_agent_workflow.py lines 31–67. The choices are VOLTVAR_OPF, RESTORATION_MILP, WLS_TRUSTED_REDISPATCH and REVIEW. Application code requires the selected choice to equal TOOLS[case] (lines 113–120); an incompatible choice records REVIEW and leaves subsequent numerical stages NOT_RUN. Do not describe the JSON choice as a native SDK function-call event: the wrapper reads the choice and calls Python. Nor does this routing choice authenticate sensors, select which measurements to trust, set constraints or calculate an injection. In this experiment those premises and numerical parameters are fixed. The useful visible role is bounded tool routing with a preserved reply and an explicit scope gate.

Full sources:

GridGuard teaching materials. Recorded four-bus cyber workflow: actual Llama routing, trusted-state correction and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_CYBER.html

## 51. 3. Code: calculate the provisional correction

100:30–102:30 / 2 minutes.

The three displayed statements are src/standard_agent_workflow.py lines87–89 with leading indentation removed. The builder verifies the same Python syntax tree. run_wls_demo computes WLS estimates, the protected-state correction and the offline known-state audit. The next two statements extract its trusted_recovery and control records. The original lines93–96 check rank3, PROPOSE and zero known-state toy-model violations; this historical offline check is not an online truth oracle. Protected-channel trust is assumed rather than authenticated. Both supervisors call the same method and obtain the same numerical correction. In this actual agentic run, Llama subsequently returns REVIEW and the human step remains pending. Full original function and result/journal are linked under TRACE_CYBER.

Full sources:

GridGuard teaching materials. Recorded four-bus cyber workflow: actual Llama routing, trusted-state correction and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_CYBER.html

Exact displayed excerpt (src/standard_agent_workflow.py, lines 87–89. Source statements; line breaks added for readability.):

```python
result = run_wls_demo()
recovery = result['trusted_recovery']
control = recovery['control']
```

## 52. 4. Result: a bounded correction with evidence

102:30–104:30 / 2 minutes.

Source: C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json, cyber/agentic entry, summary.control and trace Planning/Execution proposal/Simulation/Verification. Exact proposed injection is 0.12169366726990237 p.u. at bus 2, balanced at reference bus 0. The objective is 0.5u^2, giving 0.007404674326798854, with 0<=u<=0.5. Predicted flows in branch order [01,12,23,03] are [0.13028137485605382,0.16999999999999998,-0.046197066897314544,0.14829215397936965] p.u. Physical ratings are [0.35,0.18,0.35,0.35] p.u.; predicted constraints reserve 0.01 p.u. The independent known-state toy audit gives [0.1304607615600558,0.1704607615600558,-0.047845571170041824,0.14784557117004185] p.u. and actual_violation_count=0. The wrapper's modeled checks pass. Its protected estimate is [-0.019982061329599805,-0.04992446613459283,-0.04008931656186556] rad, rank three, residual degrees of freedom zero. The three protected angles are externally assumed trustworthy; their zero residual cannot supply a redundant detection test. The compromised-estimate baseline chooses u=0 and has known-state flow12=0.24 p.u., above 0.18. This improvement comes from the supplied trusted evidence and numerical redispatch. The matched fixed supervisor computes the exact same protected numerical result and returns MODEL_RECOMMEND; the agentic run will instead end at REVIEW. Do not attribute a better optimum, attack-detection advantage, sensor authentication or field safety to the LLM. The displayed correction remains a provisional tool result.

Full sources:

GridGuard teaching materials. Recorded four-bus cyber workflow: actual Llama routing, trusted-state correction and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_CYBER.html

## 53. 5. Operator: resolve trust before proceeding

104:30–106:30 / 2 minutes.

Exact source: C:/Users/f00863x/OPRO/output/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json, call_id=8 (Explanation), context numerical_summary and passed_modeled_checks=true, raw_response.message.content, and parsed response through line 538. The actual reply is choice='REVIEW'; its reason says the numerical workflow completed successfully and passed its modeled checks, then asks to review the results. Preserve this apparently cautious or ambiguous reply rather than replacing it with an invented confident approval. In src/standard_agent_workflow.py lines 134–141, the allowed explanation choices are REPORT_LIMITS and REVIEW; REVIEW sets accepted=False. Therefore this run's final status is REVIEW even though its numerical Verification stage is PASS. This is a workflow/response-label outcome, not proof that the numerical plan is infeasible. Operator acknowledgment (lines 150–151) is PENDING with acknowledged=false, dispatch_authorized=false and equipment_operated=false. The review_id is 4a10da2aa66efaa3c1f39dae3b67372c384dbf66a297de9ed01841f6ba9c4fd9. No recorded human decision follows it. The second bullet is a proposed next human step, not an event asserted to have happened. Suggested review questions: who established the protected-channel premise, whether topology and limits are current, and what AC/protection/permission checks a real application would still require. This archived run makes two actual model calls, numbered 7 and 8 within the eight-call suite; simply viewing its executed notebook makes zero new LLM calls. The numerical method and parameters match the fixed comparator, so the record establishes no superior agentic control result or reduced operator workload.

Full sources:

GridGuard teaching materials. Recorded four-bus cyber workflow: actual Llama routing, trusted-state correction and pending human review. Local executed tutorial and preserved model-call journals. 21 September 2026.
Full source: research/source_TRACE_CYBER.html

## 54. Exercise: HOLD or propose for operator review?

106:30–110:30 / 4 minutes.

Give participants one minute to read, two minutes to compare decisions with a partner, and one minute to prepare a reason and a next evidence request. Correct answers: A is HOLD in the stated stealth-capable trust scenario; low J alone does not resolve provenance. B is HOLD and investigate the inconsistency; the statistic does not identify an attacker or authorize removal of a channel. C may be PROPOSE for operator review within this fixed DC fixture, because the trust premise is supplied externally and the current-model QP and post-solve checks pass. It is not EXECUTE. For C, all four predicted branch constraints, action bounds and finite checks matter. Expected follow-up questions include whether data are current and aligned, who established trust, whether topology or limits changed, and what operational checks the DC fixture omits. Do not reveal the answers while pairs are discussing.

Full sources:

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

GridGuard teaching materials. Classroom Labs L8–L9: cyber consistency sweep and trusted response gate. Local workshop notebook and companion lab functions. Reviewed 18 October 2026.
Full source: research/source_CY05.html

## 55. Debrief: consistency, trust and permission differ

110:30–112:30 / 2 minutes.

Ask one pair to justify each packet. A passes a residual consistency test but has an unresolved trust premise, so the trusted_response policy holds. B fails the residual test, also without a trustworthy replacement, and holds while the discrepancy is investigated. C can progress to a human review packet after the stated current-model checks. The independent trust premise still needs a real operational justification outside this demonstration. Reinforce three separate questions: do the data fit the model; why should the channels be believed; and who is permitted to act? The three trusted angles have no residual redundancy, so their zero residual supplies no extra authenticity evidence. The comparison does not isolate an LLM detection benefit or prove operational cyber resilience. A useful agent can organize the assessment and report what a numerical tool actually checked, while failing closed when necessary evidence is absent.

Full sources:

GridGuard teaching materials. Standard formulation companion: four-bus DC weighted least squares, residual tests and constrained redispatch. Local reproducible teaching fixture. 21 September 2026.
Full source: research/source_CY04.html

GridGuard teaching materials. Classroom Labs L8–L9: cyber consistency sweep and trusted response gate. Local workshop notebook and companion lab functions. Reviewed 18 October 2026.
Full source: research/source_CY05.html

Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.
Full source: https://doi.org/10.1145/1952982.1952995
Full paper: https://reitermk.github.io/papers/2011/TISSEC2.pdf

## 56. Give the operator an evidence packet

112:30–114:00 / 1.5 minutes.

The final packet should let the operator trace a recommendation back to its evidence, rather than accept a confident explanation. Include the current reading and topology versions, who established the trusted-channel premise, the fixed DC scope, u=0.121694, predicted flow12=0.170000, all other predicted branch checks, physical ratings, 0.01 planning margin and any failed or omitted checks. State that the offline 0.170461 actual-flow audit used synthetic truth and is not an online truth oracle. The local trusted_response function sets dispatch=false whether it holds or proposes. Any real deployment would require the utility's authorization, operating procedures and applicable additional engineering checks; these are outside this module. The agent's useful role here is to assemble the correct tool calls, preserve the evidence context, flag missing premises and explain verified results. It must not convert low residuals into trust or numerical feasibility into permission.

Full sources:

GridGuard teaching materials. Classroom Labs L8–L9: cyber consistency sweep and trusted response gate. Local workshop notebook and companion lab functions. Reviewed 18 October 2026.
Full source: research/source_CY05.html

GridGuard teaching materials. Workshop Instructor Guide and Cyber Teaching Chapter: evidence scope and operator interpretation. Local instructor material. Reviewed 18 October 2026.
Full source: research/source_CY07.html

## 57. Each failure points to a different repair

114:00–116:00 / 2 minutes.

Return to the opening comparison. A broader AC violation requires a candidate change, broader model study, or both. A changed network or rating invalidates restoration evidence until the affected study is repeated. A stealth measurement change requires an independent trust argument or escalation; a quiet residual does not supply it. Each repair is a concrete engineering step. The LLM can help interpret a request, assemble the right tool arguments and explain verified results, but it cannot substitute wording for missing evidence. Ask for one example from each case without adding another timed exercise.

Full sources:

GridGuard project teaching materials. Classroom Labs: voltage support, six-node restoration and four-bus cyber response. Existing local GridGuard workshop; recorded numerical examples and source code. 2026; inspected 18 October 2026.
Full source: research/workshop_evidence.md

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## 58. An operator reviews one complete recommendation packet

116:00–118:00 / 2 minutes.

A useful packet lets an operator inspect why a candidate is eligible for review. It includes what the solver actually checked and what remains outside the model. Voltage should show model scope and margins. Restoration should identify the served and unserved demand and the need for operational isolation/protection work. Cyber should identify the trusted evidence assumption and the response audit. The classroom acknowledgment checks a packet identity and operator name. That local interaction has no connection to live SCADA or DMS control. In deployment, the utility’s operating procedures, role permissions, interlocks and field coordination remain separate engineering requirements.

Full sources:

GridGuard project teaching materials. Classroom Labs: voltage support, six-node restoration and four-bus cyber response. Existing local GridGuard workshop; recorded numerical examples and source code. 2026; inspected 18 October 2026.
Full source: research/workshop_evidence.md

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## 59. A useful pilot measures completed work and its errors

118:00–120:00 / 2 minutes.

Close with a testable motivation for agentic assistance: reducing specific workflow errors or handling varied requests without weakening numerical checks. The recorded voltage selector tied voting, so the tutorial makes no blanket claim that a learned selector improves every task. The restoration improvement in critical service came from objective weights, and the cyber recovery benefit came from protected measurements. A pilot should isolate what the agent adds under matched conditions. If the question concerns human workload, use a human study instead of inferring workload from solver seconds. The teaching guide contains all three exercise debriefs, full primary references, numerical provenance and local evidence paths.

Full sources:

GridGuard project teaching materials. Classroom Labs: voltage support, six-node restoration and four-bus cyber response. Existing local GridGuard workshop; recorded numerical examples and source code. 2026; inspected 18 October 2026.
Full source: research/workshop_evidence.md

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.
Full source: https://doi.org/10.6028/NIST.AI.100-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

