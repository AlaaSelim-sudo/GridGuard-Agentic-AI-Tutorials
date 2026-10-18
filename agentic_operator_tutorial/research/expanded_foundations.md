# Foundational agent mechanisms: verified teaching evidence

Reviewed 17 October 2026. The five fixed-paper experiments below are separate studies. Their tasks, models, samples, metrics and budgets differ; they must not become a cross-paper ranking or an estimate of utility reliability. `expanded_foundations.json` preserves raw chart rows, methods, limitations and slide suggestions. `expanded_foundations_sources.json` is ready to merge into the source registry.

## F01 — ReAct: an evidence-dependent interaction loop

The paper interleaves planning text, environment calls and returned observations. The frozen model can change its next call after seeing evidence; this is a prompting architecture rather than an SDK. Its [original repository](https://github.com/ysymyth/ReAct) contains GPT-3 notebooks, whereas the main result uses PaLM-540B.

The strongest compact controlled result is WebShop success rate: Act-only 30.1%, ReAct 40.0% on 500 test instructions, a calculated 9.9-percentage-point difference. Reproduce Table 4, PDF p.8, from [the fixed v3 paper](https://arxiv.org/pdf/2210.03629v3). These are reported rounded rates, not reconstructed integer counts. ReAct does not dominate every method on every task: Table 1 has HotpotQA exact match 27.4% versus CoT 29.4%.

Suggested pair: a short action/observation trace with an unexpected search return, then the two-bar result. Optional third slide: show why a useful observation loop still depends on retrieval and correct interpretation. Original Figure 1, PDF p.2, supplies example trajectories. A utility transfer is a proposed advisory workflow with independent unit, snapshot and engineering checks.

## F02 — Toolformer: learn the value of calls offline

The training pipeline samples calls in a text corpus, executes them, retains responses that reduce subsequent token-prediction loss, and fine-tunes on the augmented corpus. At runtime, generation pauses for a call and resumes with its response. This changes model weights; merely adding a function schema to an SDK does not reproduce the method.

For MAWPS, the same trained model scores 15.0% with API calls disabled and 44.0% enabled: a calculated 29-point difference. The metric scores the first generated number, with an equation exception, rather than exact-string match. The evaluated sample count is not disclosed beside the reported setup; do not substitute a nominal external dataset size. Only one call per input is allowed. Use Table 3, PDF p.6, in [the NeurIPS paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf); the arXiv v1 numbers have different table numbering.

Suggested extension pair: original Figure 2, PDF p.2, then the calls-disabled/enabled chart. An optional third slide contrasts the loss filter with an engineering acceptance contract. No official implementation link was identified in the checked primary publication links; third-party repositories should not be attributed to the authors.

## F03 — Reflexion: feedback and memory without a weight update

An actor attempts the task, an evaluator supplies feedback, and a reflection model records a repair lesson for the next attempt. Original Figure 2 and Algorithm 1 are on PDF p.4. The [paper-linked repository](https://github.com/noahshinn/reflexion) preserves experiment code and logs; its dependencies and model names are historical.

Use the explicit-denominator ablation rather than the headline alone: on the 50 hardest HumanEval Rust problems, GPT-4 base scores 60%, reflection without generated tests 52%, generated tests without reflection 60%, and full Reflexion 68%. Reproduce Table 3, PDF p.8, in [the NeurIPS paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf). The result teaches that ungrounded self-critique can harm. The reported pass@1 procedure can perform internal tests and revisions before returning its selected program; it is not one model call or an equal-compute comparison.

Suggested core pair: failed checker output → retained repair note → new candidate, then the four-ablation chart. Optional third slide: internal test acceptance can be false, as illustrated by the paper's MBPP counterexample. A utility adaptation should preserve the actual checker evidence independently from the generated lesson.

## F04 — LATS: search alternative trajectories inside one task

LATS adds selection, expansion, evaluation, simulation, backpropagation and reflection to task execution. Original Figure 2 is on PDF p.5; Algorithm 1 is on p.15. It assumes an environment can be reset to earlier states. That supports sandbox or simulator exploration; it does not imply that a live physical action is reversible.

Table 6, PDF p.8, reports WebShop task score 64.2 for Reflexion and 75.9 for LATS using GPT-3.5, 50 instructions and a 30-trajectory limit. The calculated difference is 11.7 score points. Task score is 100 times mean reward, distinct from fully successful-task rate. The common trajectory cap does not equalize calls or tokens. Use [v3](https://arxiv.org/pdf/2310.04406v3), [the ICML publication](https://proceedings.mlr.press/v235/zhou24r.html) and [the original implementation](https://github.com/andyz245/LanguageAgentTreeSearch).

Suggested pair: a small branching action tree, then the task-score chart with the replay/budget condition. The original ReAct WebShop experiment used a different model and 500 instructions; its values must remain on a separate result slide.

## F05 — AFlow: search for a reusable procedure offline

An AFlow search node is a whole executable workflow. The optimizer edits prompts and code connections, evaluates candidates, and preserves successful edits. This differs from LATS's nodes representing intermediate states inside one task. Original Figure 3, PDF p.5, and Algorithm 1, p.7, explain the search. Appendix B.1, p.22, shows an MBPP procedure: generate three candidates, ensemble-select, test, and repair on failure.

Table 1, PDF p.8, reports MBPP pass@1 of 73.6% for the best tested manual baselines and 83.4% for AFlow, with GPT-4o-mini as executor and three test runs averaged. The calculated gain is 9.8 points. Exact MBPP test count is undisclosed; the paper describes a 20/80 validation/test split. Do not substitute the standard benchmark test count or treat an average of unlike benchmark metrics as a reliability probability. See [v4](https://arxiv.org/pdf/2410.10762v4) and [the author repository](https://github.com/FoundationAgents/AFlow).

Suggested pair: offline workflow optimization versus subsequent task execution, then the MBPP chart. Optional third slide: the discovered test/repair branch makes the mechanism concrete. Search cost, validation design and independent held-out evaluation remain necessary.

## Route and visual guidance

Use ReAct and Reflexion as core examples; distinguish LATS from AFlow before discussing their scores. Toolformer fits a training-focused extension. Concept/result pairs give ten useful slides; optional failure or code-workflow examples can add depth without a framework-name list.

All five new charts reproduce reported values. Their deltas are recalculated by the tutorial. No confidence intervals are invented, no raw counts are inferred from rounded percentages, and each chart retains its own metric and setup. Original paper figures need their source credit and a legible crop; a redraw must be labeled as a teaching adaptation.
