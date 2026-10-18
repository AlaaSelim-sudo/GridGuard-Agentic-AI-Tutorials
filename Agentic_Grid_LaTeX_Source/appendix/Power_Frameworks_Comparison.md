# Power-system agent frameworks: mechanisms and evidence

Primary sources refreshed on **17 October 2026**. This comparison supports the current foundation slides in `sections/classroom_foundations.tex` and the detailed literature appendix in `sections/power_frameworks.tex`. It distinguishes inspected literature from the executed P1–P8 reference tutorial and E1–E8 selector extension. The authors' software benchmarks were not rerun here. Results from different papers are not a common performance ranking.

For the wider 2026 teaching update—including uncertainty-aware orchestration, reusable skills, governance and agent evaluation—see [Agentic_AI_Research_2026.md](Agentic_AI_Research_2026.md). This page retains the five closest comparison works; it is not an exhaustive review.

## Exact works

| Work | Citation and primary source | Distinctive mechanism |
|---|---|---|
| PowerAgent | Qian Zhang and Le Xie, *PowerAgent: A Road Map Toward Agentic Intelligence in Power Systems: Foundation Model, Model Context Protocol, and Workflow*, IEEE Power and Energy Magazine 23(5), 93–101, 2025. [DOI](https://doi.org/10.1109/MPE.2025.3579718), [official ecosystem](https://poweragent.seas.harvard.edu/). | Domain models, standardized tool interfaces and reusable workflows. |
| PowerDAG | Emmanuel O. Badmus and Amritanshu Pandey, *PowerDAG: Reliable Agentic AI System for Automating Distribution Grid Analysis*, [arXiv:2603.17418v1](https://arxiv.org/html/2603.17418v1), 2026. | Adaptive exemplar retrieval and deterministic tool-prerequisite supervision. |
| Grid-Agent | Yan Zhang, Ahmad Mohammad Saber, Amr Youssef and Deepa Kundur, *Grid-Agent: An LLM-Powered Multi-Agent System for Power Grid Control*, [arXiv:2508.05702v3](https://arxiv.org/html/2508.05702v3), revised 8 September 2025. | Five agents, sandbox simulation, validation and rollback. |
| X-GridAgent | Yihan (Logon) Wen and Xin Chen, *X-GridAgent: An LLM-Powered Agentic AI System for Assisting Power Grid Analysis*, [arXiv:2512.20789v1](https://arxiv.org/html/2512.20789v1), 2025. | Planning–coordination–action hierarchy, structured retrieval and prompt refinement. |
| PowerAgentBench-SS | Costas Mylonas, Magda Foti, Andrea Pomarico, Matheus Duarte, Qian Zhang and Emmanouel Varvarigos, *PowerAgentBench-SS: A Benchmark for Agentic AI in Power System Steady-State Studies*, [arXiv:2606.18789v1](https://arxiv.org/html/2606.18789v1), 2026. | Equal tool/budget access and hidden physical revalidation of submitted claims. |

PowerAgent is the verified name matching the likely intended “powerc agent”; no separate PowerC-Agent is asserted. The PowerAgent roadmap citation is confirmed by its authors' site, while capability descriptions here use the official ecosystem and repositories. Its publisher PDF was unavailable in this research session. The other four cited works were inspected as author preprints; these links do not imply peer-reviewed publication.

## Scope matrix

**✓** documented; **△** qualified scope; **NR** not reported in the inspected source; **—** absent from the named tutorial reference implementation.

| Work | Plans/tools | Simulation feedback | Electrical checks | RL response selection | Multi-LLM vote | Human review |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| PowerAgent ecosystem | ✓ | ✓ | △ | NR | NR | ✓ |
| PowerDAG | ✓ | ✓ | △ | NR | NR | NR |
| Grid-Agent | ✓ | ✓ | ✓ | NR | NR | △ |
| X-GridAgent | ✓ | ✓ | △ | NR | NR | △ |
| PowerAgentBench-SS | ✓ | ✓ | ✓ | NR | NR | △ |
| Executed P1–P8 tutorial reference | ✓ | ✓ | ✓ | — | — | ✓ |

The reference tutorial's six Llama cases and separate Qwen portability example are not multi-model voting or RL-based response selection. The new selector extension must report its own implementation and results separately.

## Evidence and limits behind the marks

**PowerAgent.** Its official site describes PowerFM, PowerMCP, PowerWF and PowerSkills. Demonstrations cover grid-impact studies, contingency evaluation, load growth and a market assistant with human review. Tool capabilities differ across workflows: an ecosystem-wide immutable physical acceptance gate is not established by these pages. [PowerMCP](https://github.com/Power-Agent/PowerMCP) includes engineering-software interfaces, including OpenDSS; [PowerWF](https://github.com/Power-Agent/PowerWF) hosts modular workflows. An RL LLM-response selector and multi-model vote were not reported in the inspected sources. This is evidence for interoperability and workflow reuse, not a single control-system safety claim.

**PowerDAG.** Sections IV–V describe retrieval plus a just-in-time supervisor that checks required earlier tool writes. It prevents specified stale-state and dependency errors; rules cover a subset of tools. Electrical constraint tools and expert numerical-result evaluation are reported, but the state guard is not a universal electrical-feasibility certificate. The study has 30 unseen queries, 50 expert exemplars and 82 tools. It tests unbalanced power flow, hosting capacity, infeasibility and data analysis using anonymized real feeder data. Different LLMs are evaluated separately. Do not equate this with voting or compare its benchmark success percentages directly with our case outcomes. [Primary paper](https://arxiv.org/html/2603.17418v1).

**Grid-Agent.** The inspected v3 identifies Topology, Planner, Executor, Validator and Summarizer roles, sandbox power-flow checking and rollback after unsuccessful changes. IEEE 30/69 and CIGRE MV cases use different LLMs in separate runs. Human oversight is recommended for deployment rather than evaluated as per-action operator approval. A trained RL response selector or multi-model vote is not demonstrated in the inspected methods. Its architecture closely precedes our proposal: this tutorial cannot reasonably claim the first five-agent grid workflow or first use of numerical verification. [Primary paper, v3](https://arxiv.org/html/2508.05702v3). Version note: v3 no longer contains v2's numbered VI-D RL subsection; the prior VI-B/VI-C/VI-D references have therefore been removed. Removing those references does not itself prove that a capability is absent.

**X-GridAgent.** Sections II–IV describe three layers and eight pandapower-backed MCP servers. Solver tools assess physical constraints; reflection checks task completion. Judge/edit agents and human experts refine prompts against reference answers. This does not establish a separate immutable physical gate or per-action operator approval. The reported experiment uses 11 representative queries repeated 30 times, with GPT-5 at temperature zero; systems include IEEE cases and Texas 2k. The reported success applies to that query set, not arbitrary grid control. RL response selection and model voting are not demonstrated. [Primary paper](https://arxiv.org/html/2512.20789v1).

**PowerAgentBench-SS.** Sections II–IV define common public tools and budgets, evidence logs and hidden revalidation. The pilot covers eight IEEE-39 operating points, 1,035 possible N-2 contingencies and a budget of 80 validations. Its electrical scope is DC thermal screening with islanding penalties, excluding AC voltage/reactive constraints. The protocol supports approval logging, while the reported pilot compares scripted and LLM agents. It motivates separate measures of evidence support, physical outcomes, action cost and tool use. It is a benchmark rather than a controller, and its authors do not present the pilot as a final LLM ranking. [Primary paper](https://arxiv.org/html/2606.18789v1).

## The proposed selection extension

Use MPC for model-based candidate planning and SAC for a model-free control proposal. The power-flow simulator executes candidates on a model; a common deterministic verifier checks declared electrical and policy limits. A DRL proposal is an alternative controller, not the physical safety certificate.

Several LLMs can return allowed candidate choices and concise explanations. The response selector chooses the next simulation trial before its electrical outcome is known; the selected response is not already physically verified. Voting is one selection baseline. A learned selector is another: for a one-step decision, a contextual bandit is a transparent RL specialization. Its action is selecting a model response, distinct from the continuous physical action produced by SAC. Calling a fixed numerical ranking or ordinary language critique “RL” would be inaccurate.

Before claiming advantage, disclose training/test separation, learned parameters, reward, candidate and model-call budgets, rejected outputs, objective quality, constraint outcomes and measured latency. Include fixed selection, individual LLMs and voting. Recheck the selected action, preserve the declared model scope, and record operator acknowledgment separately from dispatch. The learned selector cannot make an electrically rejected candidate acceptable.

The reference P1–P8 study has five cost ties and one worse Llama result against matched fixed search; it therefore motivates a new experiment rather than proving the proposed extension works. The extension's results belong in a separate record, including null or worse outcomes.


## Executed E1–E8 extension

The separate voltage pilot now executes MPC and SAC first-action candidates, actual three-model response pools, canonical operation voting and a trained linear contextual-bandit selector. It records 168 actual calls: 44 MV scenarios and the same 12 held-out scenarios with full-feeder OpenDSS planning. Five training orders each use 24 selected-feedback updates. Validation and testing keep the learned weights fixed. The operator output is an advisory report; the P dashboard remains the separate local-acknowledgment interface.

Learned selection ties majority voting on all 12 MV test and 12 AC-transfer cases. Every retained MV test control fails the separately reported broader AC audit, while all 12 AC-transfer final controls pass their modeled checks. The AC learned selector has a worse mean objective than fixed numerical selection. These results demonstrate the mechanism and its limits, not superiority to the cited frameworks, voting, or conventional optimization. Full evidence appears in `results/ensemble_voltage_pilot/selector_analysis.json` and the E notebook.
