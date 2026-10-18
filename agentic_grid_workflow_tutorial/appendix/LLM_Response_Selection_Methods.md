# MPC, SAC and learned selection of LLM proposals

This extension answers a specific question: **given a feasible numerical incumbent and a pool of LLM-proposed refinements, which proposal deserves one additional simulator trial?** It preserves the previous P1–P8 experiment as a separate reference. The new lesson is `LLM_Response_Selection.ipynb` (E1–E8).

## What each component does

1. Awareness fixes the operating scenario, forecast, limits, model coverage and permitted control space.
2. MPC solves a three-step plan. A frozen SAC policy supplies another first-action proposal. Both are evaluated explicitly, so the LLM cannot omit the MPC candidate as it did in the earlier reference example.
3. Fresh electrical simulation returns each action's consequences. Numerical checks reject violations. The best admissible action under the declared current-step objective becomes the incumbent. A conservative fallback is tested only when both proposals fail.
4. Llama 3.1 8B, Llama 3.2 3B and Qwen 2.5 7B receive the same public context and bounded operation menu. Actual raw replies, public reasons, model digests, errors and durations are retained. A reason is an output statement, not access to hidden internal reasoning.
5. The optimizer canonicalizes the structured replies, counts duplicate votes and chooses one operation for a trial. Majority voting is a baseline. A contextual bandit learns a context-dependent preference from reward.
6. The selected operation receives a numerical evaluation and the same constraints. An infeasible or worse trial cannot replace the verified incumbent. A distinct final check precedes the operator record.

SAC is a controller, not the verifier. Its previously trained weights map observations to continuous active/reactive settings. The new bandit selects a **canonical operation proposed by an LLM**. It does not fine-tune an LLM, analyze the semantic quality of its prose, or decide which one model to call. All three responses have already been generated, so their entire inference cost belongs in the shared-pool comparison.

## Objective and model coverage

For common-fleet control \(u=(a,b)\), the comparison minimizes

\[
J(u)=(1-a)^2+0.05b^2+10\operatorname{mean}[(V(u)-1.01)^2]
       +0.05\lVert u-u_{\mathrm{previous}}\rVert_2^2.
\]

Here \(a\) is the active-power participation fraction, \(b\) the reactive-power fraction, \(V\) the modeled voltage magnitudes in per unit and \(u_{\mathrm{previous}}\) the preceding control. The terms penalize curtailment, reactive effort, voltage deviation and movement. This is a declared dimensionless teaching objective. MPC optimizes a separate discounted three-step objective and supplies its first action. A better current-step result is not evidence of a better full-horizon plan or closed-loop stability.

The Python three-phase LinDistFlow model covers retained MV phases with ideal LV aggregation. OpenDSS includes the supplied MV/LV circuit. A fresh full-feeder AC audit is reported separately from the MV acceptance decision. It does not leak into the MV selector's features or reward. For an operator requiring full-feeder acceptance, an MV-only PASS remains insufficient if that audit fails.

The same twelve test scenarios also receive OpenDSS-based MPC and the response-selection workflow. The policy trained on MV contexts stays frozen for this **model-transfer** evaluation. This is different from an independent in-domain training experiment for each model.

## Learning and voting

Let \(s_t\) contain only context available before a new trial, and let \(a\) index a canonical proposed operation. The shared linear contextual-action model uses

\[
\widehat r(s_t,a)=\widehat\theta^\top\varphi(s_t,a),\qquad
a_t=\arg\max_a\{\widehat r(s_t,a)+\beta\sqrt{\varphi^\top A^{-1}\varphi}\}.
\]

\(\varphi\) contains declared context features, operation indicators and vote share. \(A\) is a regularized feature-information matrix, \(\widehat\theta\) the learned coefficients and \(\beta\) the training exploration weight. After observing only the chosen reward \(r_t\):

\[
A\leftarrow A+\varphi_t\varphi_t^\top,\quad
b\leftarrow b+r_t\varphi_t,\quad \widehat\theta=A^{-1}b.
\]

The vector \(b\) in this update is a reward accumulator, distinct from the reactive-control scalar above. Frozen evaluation removes the exploration bonus and rejects updates. This is one-step reinforcement learning. A sequential PPO optimizer would require multiple dependent routing actions, episode transitions and a separately trained policy.

Majority voting selects the operation with the most valid model votes, with a published deterministic tie rule. Different textual explanations of an identical physical command produce one candidate. Invalid responses remain visible. If all models agree, the selector has no alternative in that context; report this rather than manufacture diversity.

## Frozen pilot and interpretation

The numerical protocol fixes **24 training, 8 validation and 12 test scenarios** before collection, with seed 270926. Complete scenarios stay in one split. Load multipliers range from 0.9 to 1.1, current-allowance fractions from 0.78 to 0.88, and previous active fractions from 0.2 to 0.3. These are authored sampling ranges on one supplied feeder. The existing SAC actor was trained under a different nominal current-allowance setting; its performance here is a transfer result.

The learning protocol records feature scales, reward, hyperparameters and training orders separately. No test reward updates the policy. The validation split is a separate diagnostic unless the frozen analysis protocol explicitly declares its use for choosing a parameter. With only 24 training scenarios and a regularized linear model, this is a small teaching experiment, not evidence of broad generalization.

The prepared dataset contains simulator outcomes for all permitted operations in a separate audit file. During training, the policy update reads only its selected operation's outcome. This is **simulated partial-feedback replay over a full-information outcome table**, not logged deployment bandit data or an off-policy causal estimate. Test comparisons use the same scenarios and response pools. Actual live generation time and cached replay time remain separate.

Baselines include the verified numerical incumbent, one fixed numerical refinement, fixed-model responses, uniform selection, majority vote and the frozen learned selector. Best-of-all unique responses has a larger trial budget and serves only as an upper reference. Report candidate rejection, retained-incumbent behavior, final cost, final audit, model-call time and trial count separately. A reward penalty never substitutes for the hard numerical gate.

Restoration and cyber retain their existing case-specific catalog/MILP and WLS/redispatch lessons. The shared architectural pattern applies, but this extension does not claim trained selectors, SAC controllers or temporal MPC models for those cases.

## Primary references

- Rawlings, Mayne and Diehl, [Model Predictive Control: Theory, Computation, and Design](https://sites.engineering.ucsb.edu/~jbraw/mpc/).
- Haarnoja et al., [Soft Actor-Critic](https://proceedings.mlr.press/v80/haarnoja18b.html), ICML 2018.
- Li et al., [A Contextual-Bandit Approach to Personalized News Article Recommendation](https://arxiv.org/abs/1003.0146), WWW 2010.
- Poon et al., [Online Multi-LLM Selection via Contextual Bandits under Unstructured Context Evolution](https://arxiv.org/abs/2506.17670), 2025 preprint.
- Wei et al., [Learning to Route LLMs from Bandit Feedback: One Policy, Many Trade-offs](https://arxiv.org/abs/2510.07429), 2025.
- Ong et al., [RouteLLM: Learning to Route LLMs from Preference Data](https://arxiv.org/abs/2406.18665), ICLR 2025. Preference-trained routing and reward-based bandit selection are distinct methods.
- Gan and Low, [Convex Relaxations and Linear Approximation for Optimal Power Flow in Multiphase Radial Networks](https://arxiv.org/abs/1406.3054), 2014; [EPRI OpenDSS](https://opendss.epri.com/PowerFlow.html).

Related power-system agent mechanisms and qualified capability marks appear in [Power_Frameworks_Comparison.md](Power_Frameworks_Comparison.md).
