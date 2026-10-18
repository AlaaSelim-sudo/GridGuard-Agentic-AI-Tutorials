# Agentic AI toolkit and research evidence

Reviewed as of **October 17, 2026**. This is a selected primary-source review, not an exhaustive newest-release ranking. All proposed utility uses below are educational designs, not claims of deployment by named utilities.

## Eight entries for the tutorial

| Toolkit | What to teach | Operator example | Limit | Sources |
|---|---|---|---|---|
| LangGraph | Durable stateful graphs, deterministic steps mixed with agent reasoning, human oversight | Alarm → evidence → diagnosis → validation → approval | Application authors still implement policy and connectors | [T01](https://docs.langchain.com/oss/python/langgraph/overview) |
| Microsoft Agent Framework | Agents plus graphs, middleware, MCP, checkpoints and resume | Resume an investigation after a shift change | In-memory checkpoints do not survive restart; persistent state needs protection | [T02](https://learn.microsoft.com/en-us/agent-framework/overview/), [T03](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) |
| OpenAI Agents SDK | Python/TypeScript tools, handoffs, guardrails, review and tracing | Approved historian functions and draft work orders | Teach current SDK capabilities and check component lifecycles | [T04](https://developers.openai.com/api/docs/guides/agents/sdk) |
| Google ADK 2.0 | Graph workflows, human input, structured routing and evaluation | Require valid asset identity before reasoning | Feature parity and migration vary by language | [T06](https://adk.dev/2.0/), [T07](https://github.com/google/adk-docs/blob/main/docs/evaluate/criteria.md) |
| MCP | Discover and call standardized tools and context sources | Governed gateway to historian, GIS, manuals and registry | Authentication, scope and trust remain application responsibilities | [T08](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture), [T09](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) |
| A2A | Agent Cards and tasks/messages/artifacts across independent agents | Delegate bounded work to an asset-health agent | Interoperability does not verify engineering conclusions | [T10](https://a2a-protocol.org/latest/specification/) |
| AIOpsLab | Fault injection, workloads, telemetry and agent evaluation in cloud testbeds | Rehearse diagnosis and recovery in utility IT/communications | Cloud research does not demonstrate autonomous grid switching | [T11](https://www.microsoft.com/en-us/research/publication/aiopslab-a-holistic-framework-for-evaluating-ai-agents-for-enabling-autonomous-cloud/) |
| Evaluation toolkit | tau²-bench coordination, AgentDojo security, ADK Arena framework comparison | Local replay cases with operator actions and adversarial documents | Benchmark success is a proxy; pin harness, tasks and versions | [T12](https://arxiv.org/abs/2506.07982), [T13](https://github.com/sierra-research/tau2-bench), [T14](https://arxiv.org/abs/2406.13352), [T15](https://arxiv.org/abs/2606.05548) |

## Date and lifecycle details

- Google documents Python 2.0 GA on May 19, 2026; Go 2.0 GA on June 30; TypeScript 2.0 GA on August 21. Its 2.0 workflow runtime evaluates agents, tools and functions as graph nodes. [T06](https://adk.dev/2.0/)
- Microsoft overview was updated August 25, 2026; checkpoints documentation September 16. Go has documented preview gaps. Checkpoint resumption requires compatible workflow structure and identities. [T02](https://learn.microsoft.com/en-us/agent-framework/overview/), [T03](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints)
- MCP sources are pinned to the July 28, 2026 documentation revision. A2A's current spec documents v1.0 migration changes. Do not silently mix old and new protocol examples. [T08](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture), [T10](https://a2a-protocol.org/latest/specification/)
- OpenAI **Agent Builder is deprecated**, with shutdown scheduled November 30, 2026; ChatKit remains available. The separate Evals platform is scheduled to become read-only October 31 and shut down November 30. Use the SDK and an actively supported evaluation path for new instructional implementation. Do not portray the older AgentKit bundle as a fixed current product stack. [T05](https://developers.openai.com/api/docs/guides/agent-builder), [T16](https://developers.openai.com/api/docs/deprecations)
- Sierra's live repository documents a July 2026 grading fix: banking-knowledge scores below version 1.0.1 cannot be compared with later versions; other domains are unaffected by that fix. [T13](https://github.com/sierra-research/tau2-bench)

## Three research lessons

1. **Grade coordinated action.** tau²-bench (June 2025) puts agent and simulated user in a shared telecom environment with tools. Tutorial inference: measure whether the assistant gathers the required evidence, guides the human correctly and reaches an allowed final state; repeat cases instead of reporting one successful run. [T12](https://arxiv.org/abs/2506.07982)
2. **Keep data and authority separate.** AgentDojo (2024, revised November) evaluates prompt injection in tool-returned content. Tutorial inference: a maintenance document or vendor message cannot authorize a tool action; authorization and argument checks belong outside the model. [T14](https://arxiv.org/abs/2406.13352)
3. **Choose the whole system through local evaluation.** ADK Arena (June 2026, explicitly work in progress) compares 51 Python frameworks with a fixed LLM developer and finds no universal winner across its tested benchmarks. Tutorial inference: compare maintainability, evidence quality, policy behavior, latency and cost on your own operator tasks. [T15](https://arxiv.org/abs/2606.05548)

## Suggested teaching architecture

**Status: proposed architecture, not a claim about a named company.** Use a transformer cooling alarm that results in a draft maintenance work order.

1. An event bus receives asset ID, alarm ID and timestamp from a read-only operational-data mirror; validate mapping and freshness.
2. Scoped tools retrieve trends, approved procedures, asset metadata and maintenance history, retaining sources and timestamps.
3. A durable workflow routes retrieval and bounded diagnosis. Start with one agent; add specialists only when their ownership has a clear purpose.
4. Deterministic checks enforce units, required signals, procedure revision, action allowlists and argument validation. Approved calculators/simulators perform numerical checks.
5. The operator reviews evidence, uncertainty and the proposed action; missing or conflicting evidence triggers escalation.
6. After authenticated approval, a separate service creates the draft work item, uses an idempotency key, re-reads the record and records the outcome.

Keep control-plane credentials outside the reasoning service. Existing protection and real-time control remain in deterministic systems. Protect checkpoint storage and log evidence, versions, decisions, tool outcomes and recovery paths. Rehearse with replay/shadow operation, then use site-approved criteria for a bounded pilot. These are tutorial design inferences informed by orchestration, protocol-security and testbed literature. [T01](https://docs.langchain.com/oss/python/langgraph/overview), [T03](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints), [T09](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices), [T11](https://www.microsoft.com/en-us/research/publication/aiopslab-a-holistic-framework-for-evaluating-ai-agents-for-enabling-autonomous-cloud/)

Suggested metrics: allowed final-state success, unauthorized-action rate, evidence correctness, repeated-trial reliability, operator intervention, recovery success, latency and cost. No cited benchmark certifies electrical operating safety.

Exact references, dates, claims and structured architecture are in tools.json (T01–T16).

