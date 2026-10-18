# Framework evidence for the introductory tutorial

**Reviewed October 17, 2026.** Use about eight to nine minutes for frameworks within a 45–50 minute introduction. Keep three detailed utility use cases in the separate practical tutorial.

## Main recommendation

Use **ToolUniverse** as the main Harvard example. It is a scientific-tool platform led by the Zitnik Lab at Harvard Medical School with collaborators, with an official Harvard explanation, public code and current documentation. Follow it with a compact **TxAgent + POPPER** research-pattern slide. This distinguishes a reusable tool platform, a domain agent, and a hypothesis-testing method.

## Harvard candidate 1: ToolUniverse

The August 7, 2026 paper revision lists Harvard Medical School, Harvard College, Kempner, HDSI, Broad, MIT and MIT Lincoln Laboratory affiliations. Gao is at HMS; corresponding author Zitnik has HMS/Kempner/Broad/HDSI affiliations. The system registers, finds, calls and composes scientific tools using typed interfaces. The manuscript describes open-source release v1.3.1. The cited paper is a preprint; no cited source establishes a utility deployment. [Paper](https://arxiv.org/abs/2509.23426v3), [affiliation PDF](https://arxiv.org/pdf/2509.23426v3), [code](https://github.com/mims-harvard/ToolUniverse), [official docs](https://zitniklab.hms.harvard.edu/ToolUniverse/en/).

Suggested slide title: **Harvard example: ToolUniverse**. Use an original static schematic: goal → tool finder → typed caller → scientific resources, with structured results returning to the agent. Add manager/composer as small supporting blocks. The utility analogy is an approved catalog of historian, procedure and simulation tools; label that analogy as a teaching proposal.

Avoid counts on the main slide. The [October 9, 2025 Harvard article](https://kempnerinstitute.harvard.edu/research/deeper-learning/from-models-to-scientists-building-ai-agents-for-scientific-discovery/) says 600+ tools; paper v3 says 2,700+ as of July 2026; live docs contain both 1000+ and 2700+ wording. Any count must carry its source and date.

## Harvard candidate 2: TxAgent

The March 14, 2025 paper and official project page explicitly identify a Harvard Medical School-led team with MIT Lincoln Laboratory collaboration. TxAgent combines a domain-specialized model, tool retrieval and ToolUniverse to obtain evidence and answer biomedical reasoning tasks over multiple steps. It is a research agent with public code, demos and author-reported benchmark results, rather than a general application orchestration runtime. Its original 211-tool experiment does not describe today's ToolUniverse size. [Paper](https://arxiv.org/abs/2503.10970), [project and affiliations](https://zitniklab.hms.harvard.edu/TxAgent/), [code](https://github.com/mims-harvard/TxAgent).

Teach the pattern **request → relevant tools → evidence-based response**. Use it to motivate domain tools and source checking. Do not convert benchmark results into claims of clinical outcomes or utility performance.

## Harvard candidate 3: POPPER

POPPER is a **Stanford–Harvard collaboration**, published at ICML 2025. Its first page gives co-first author Ying Jin's affiliation as Harvard Data Science Initiative and Department of Health Care Policy; the other listed department affiliations are Stanford. An experiment-design agent proposes falsification tests, an execution agent performs analyses, and sequential evidence aggregation supports the decision. The stated false-positive control depends on statistical and logical assumptions. [PMLR paper](https://proceedings.mlr.press/v267/huang25n.html), [PDF with affiliations and assumptions](https://cs.stanford.edu/~jure/pubs/auto-hypothesis-validation-icml25.pdf), [code](https://github.com/snap-stanford/POPPER).

Teach **hypothesis → designed test → executed analysis → evidence decision**. The transferable lesson is that an explanation needs a test. This research does not validate feeder control or transmission dispatch.

## Established development frameworks

One comparison slide is enough in the introductory session. These roles are supported by official docs; their utility connections are proposed instructional applications.

| Framework / maintainer | Role to explain | Visual |
|---|---|---|
| [LangGraph / LangChain](https://docs.langchain.com/oss/python/langgraph/overview) | Stateful graphs, deterministic and agentic steps, persistence, human oversight | Graph with bounded retry and review node |
| [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) | Agents, graphs, middleware, [resumable checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) | Workflow plus checkpoint store |
| [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk) | Application-hosted tools, handoffs, guardrails, review and tracing | Coordinator, three typed tools, visible action trace |
| [Google ADK](https://adk.dev/2.0/) | Agent/graph workflows, human input and [evaluation](https://github.com/google/adk-docs/blob/main/docs/evaluate/criteria.md) | Input validation → agent/tools → evaluator |

Do not label these frameworks Harvard-developed merely because Harvard lists them. The [Kempner computing handbook](https://handbook.eng.kempnerinstitute.harvard.edu/s5b_agentic_ai_workflows/agentic_ai_tools.html), updated October 11, 2026, lists common external frameworks and separately identifies ToolUniverse as a Zitnik Lab at HMS project.

## Suggested two main Harvard slides

1. **Harvard example: ToolUniverse** — a large original tool-interface diagram; four short claims: Harvard-led team; common tool interfaces; discovery/calling/composition; research platform with its own validation scope.
2. **Specialize the tools, test the claim** — two horizontal lanes for TxAgent and POPPER. Keep attribution and maturity visible beneath each. Finish with one takeaway: domain tools provide evidence, while separate checks determine what the evidence establishes.

Use static diagrams and at most one reveal per diagram. Provide full paper titles, authors, dates, official docs and code URLs in the reading list. The structured companion framework_motivation.json includes exact H01–H12 sources, slide suggestions and attribution details. Existing T IDs refer to the prior research registry.

