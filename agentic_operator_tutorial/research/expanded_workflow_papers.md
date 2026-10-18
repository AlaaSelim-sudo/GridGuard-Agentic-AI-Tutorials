# Expanded workflow-paper research

Exact numeric rows, source locators, historical settings and source-inspected execution instructions are in `expanded_workflow_papers.json` in this directory. No experiment was executed.

For the tutorial, use two adjacent diagrams: a procedure-improvement loop across held-out tasks and a decision-search tree within one task. This makes the search target visible before naming either algorithm. Present an SDK as an implementation layer beneath those choices. The source code's current defaults and dependencies are separate from the historical experiment.

Recommended chart sources are [AFlow Table 1](https://arxiv.org/pdf/2410.10762v4#page=8) and [LATS Table 6](https://arxiv.org/pdf/2310.04406v3#page=8). Use the per-paper rows in JSON, with their own axes and captions. They measure different tasks and metrics and cannot support a cross-paper ranking.

Metadata and publication context: [AFlow arXiv history](https://arxiv.org/abs/2410.10762), [LATS arXiv history](https://arxiv.org/abs/2310.04406), [LATS ICML proceedings](https://proceedings.mlr.press/v235/zhou24r.html).

Implementation references: [AFlow official repository](https://github.com/FoundationAgents/AFlow), [AFlow executable entry point](https://github.com/FoundationAgents/AFlow/blob/main/run.py), [LATS official repository](https://github.com/andyz245/LanguageAgentTreeSearch), [LATS WebShop experiment script](https://github.com/andyz245/LanguageAgentTreeSearch/blob/main/webshop/lats.sh).
