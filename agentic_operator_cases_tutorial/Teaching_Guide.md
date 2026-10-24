# Teaching and Source Guide

Hands-on: Three Operator Cases — notebook-aligned tutorial. Evidence reviewed 24 October 2026. The full reading guide is separate from the timed main talk. Corporate issuers are listed when no individual author is recorded. Original figures, page locations and image-source credits are included. Attribution alone is not a blanket reuse license.

## How to teach this hands-on session

**Format:** 86 static slides / 180.0 minutes. Getting started and agent basics: 21 slides / 30.0 minutes; Voltage support: 18 slides / 37.5 minutes; Service restoration: 14 slides / 28 minutes; Cyber response: 16 slides / 32 minutes; Llama walkthrough and operator practice: 17 slides / 52.5 minutes.

**Prerequisite:** Use the foundations tutorial first. This session follows the current Classroom Labs notebook through voltage support, service restoration and cyber response.

**Evidence modes:** Run the selected numerical cells to calculate results for your inputs. Archived model-response pools and historical evaluation records remain separately labeled. Editing L2 does not change the archived test_01 used by L3–L5, and editing the L8 sweep does not change the fixed L9 recovery fixture. No default cell calls an LLM or operates equipment.

**Preparation:** Give participants Participant_Lab_Guide.pdf. Open the one required notebook in Google Colab, sign in and use a standard CPU runtime. Run setup, wait for Ready, then follow the L labels in order. Keep both model switches at the stated defaults. The default route needs no API key, LLM download or GPU.

**Stanford teaching bridge:** Original grid teaching diagrams adapt task decomposition, evidence checking and explicit workflow specification from Monica Lam’s CS224V Lecture 1, with full lecture and paper references below. This notebook does not run WikiChat, Genie Worksheets or a theorem prover.

**Facilitation:** Follow each slide’s lab label and stable cell ID. Read the code, predict the result, run it, change the stated parameter and explain what changed. Each exercise has its own timed prompt; answers belong in the teacher notes and following debrief.

## 1. Hands-on: Three Operator Cases

**Timing:** 00:00–00:30 (0.5 minutes)

**Slide content:** Run one notebook to understand three operator studies.
180 minutes / three short exercises / no coding experience required

**Teaching notes:** Open Classroom Labs before the workshop. Participants will run fresh numerical calculations and inspect clearly labeled archived model replies. Use the same notebook for all three cases. If devices are limited, work in pairs: one person runs the cells while the other checks the evidence. The deck uses the IEEE ComSoc theme. The classroom cycle is run, change, check and explain. This expanded edition includes a new L10B replay and a proposed control-room advisory pilot. The scheduled teaching time is 180 minutes; allow breaks outside that total. The presenter affiliations are supplied by the presenters. The new Stanford teaching bridge is an adaptation of general reliability ideas, not a claim that the lab implements those Stanford frameworks. Use the six-page Participant Lab Guide for the exact activity steps.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[B01] IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.:** [https://www.comsoc.org/about/brand-experience/resources](https://www.comsoc.org/about/brand-experience/resources)

## 2. What would an operator ask an assistant to do?

**Timing:** 00:30–02:00 (1.5 minutes)

**Slide content:** Ask for a study: compare allowed options and show the checks needed for a decision.
The assistant returns a reviewable proposal linked to the input data and tool results.

**Teaching notes:** Start with the operator’s job, not the model name. Read the illustrative request aloud. Ask participants to name the information they would need before making the study. This is a teaching design for an advisory assistant. The classroom notebook provides numerical counterparts for selected steps, not a live control-room connection.

**Figure scope:** Illustrative study request and review path. The operator retains the decision.

**Editable figure:** diagrams/bridge_request.tex

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 3. What makes this an LLM agent?

**Timing:** 02:00–03:30 (1.5 minutes)

**Slide content:** A fixed script follows choices written in code. An LLM agent can choose a permitted next tool.
Both can branch and use the same solvers. We must test whether model choice adds value.

**Teaching notes:** Use Anthropic’s attributed architectural distinction. A conventional program can contain feedback, branches, rules and sophisticated optimization. Those alone do not demonstrate an LLM agent. A generative model can also just write an explanation. In these records Llama makes bounded choices from an allowed list, receives tool evidence and may select another step. This is narrow agency, not unrestricted autonomy. The default class replays those choices.

**Figure scope:** Same engineering tools, different source of the next-step choice. Both paths require checks.

**Editable figure:** diagrams/bridge_script_agent.tex

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 4. Llama, Python and the operator have different jobs

**Timing:** 03:30–05:00 (1.5 minutes)

**Slide content:** Llama chooses and explains. Python calculates, checks limits and rejects failed proposals.
The operator reviews the evidence and decides whether another study or review is needed.

**Teaching notes:** Llama is the language model, Ollama is the local service used to run it, and the application controls which tools can execute. Our recorded wrappers return schema-constrained JSON choices. They do not use Ollama’s native tool_calls protocol. Python validates and interprets the choice before calling numerical functions. Good JSON formatting does not make a claim physically correct. No classroom cell sends an equipment command.

**Figure scope:** Roles in the recorded teaching workflow. The classroom route shows saved Llama choices.

**Editable figure:** diagrams/bridge_llama_tools.tex

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[OLL1] Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

## 5. An agent needs a goal, tools and a place to stop

**Timing:** 05:00–06:30 (1.5 minutes)

**Slide content:** Give the agent approved data, a small tool list and a saved record of what has been tried.
After each result, let it choose the next permitted step within explicit check and stop rules.

**Teaching notes:** Walk around the loop once. State means the saved case record: input snapshot, selected candidate, tool outcomes and remaining study budget. A tool is an application function, such as running a power-flow check or solving a restoration problem. The engineering model, allowed actions, limits and stop conditions belong to the application. A model can request REVIEW when the permitted route cannot resolve a problem. In the original P3 record only two candidate checks are allowed.

**Figure scope:** Teaching model of a bounded agent. Each result updates the case record before the next choice.

**Editable figure:** diagrams/bridge_agent_parts.tex

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

## 6. Break one big request into small jobs

**Timing:** 06:30–08:00 (1.5 minutes)

**Slide content:** Ask for one clear result at each step. Save it so the next step can use it.
In our lab, Python calculates and checks. L10B shows how Llama selected a next step.

**Teaching notes:** Stanford connection: Lam’s CS224V introduction, pp.19–20, uses WikiChat to illustrate splitting a response into retrieval, claim checking and writing. Our diagram is an original power-system teaching adaptation. Follow the voltage path: read the current allowance, choose a permitted candidate, calculate its result, check limits and explain the outcome. This is an analogy across domains, not evidence that WikiChat is a power-system controller. Ask pairs to name which step would detect a current violation.

**Figure scope:** Original teaching adaptation of the task-decomposition idea. The notebook does not run WikiChat.

**Editable figure:** diagrams/lab_stanford_steps.tex

**Notebook / source locator:** Monica Lam, CS224V Lecture 1, pp.19–20; Semnani et al., WikiChat (2023).

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 7. Find the rule, then test the result

**Timing:** 08:00–09:30 (1.5 minutes)

**Slide content:** A document can tell us the limit. A numerical tool tells us how the proposal compares with it.
Keep the source, the measured or calculated value, and the remaining checks together.

**Teaching notes:** Stanford connection: the lecture’s WikiChat discussion, pp.17–25, separates finding material from checking factual claims. Apply the habit to a grid study: retrieving a current limit is different from calculating current for a candidate. The displayed 99.604410% value belongs to the separate archived P3 OpenDSS replay, not to the learner’s fresh L2 result. This example supports only that current check under its recorded model. A sentence, retrieved document or citation does not establish full-network feasibility.

**Figure scope:** Teaching analogy. The number shown comes from the recorded P3 replay, which is separate from L2.

**Editable figure:** diagrams/lab_claim_evidence.tex

**Notebook / source locator:** Monica Lam, CS224V Lecture 1, pp.17–25; recorded P3 current check.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

## 8. Tell the agent what is allowed

**Timing:** 09:30–11:00 (1.5 minutes)

**Slide content:** Write down the goal, required inputs, permitted tools and stop rules before the study.
If something required is missing, report what is missing and keep the proposal on HOLD.

**Teaching notes:** Stanford connection: Lam p.40 and the published Genie Worksheets paper emphasize developer-defined workflows and knowledge sources. The published framework uses an algorithmic runtime to enforce a supplied policy, with LLMs used for language understanding and response generation. Our lab uses custom Python functions, not Genie Worksheets. The application analogy is to specify the task and prevent a language reply from silently changing its limits or filling missing required inputs. A passed calculation does not prove that the task description was correct.

**Figure scope:** Original teaching analogy to Genie Worksheets. This lab uses Python and does not implement Genie.

**Editable figure:** diagrams/lab_workflow_spec.tex

**Notebook / source locator:** Monica Lam, CS224V Lecture 1, p.40; Joshi et al., Genie Worksheets (ACL 2025).

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST03] Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.:** [https://aclanthology.org/2025.acl-long.1323/](https://aclanthology.org/2025.acl-long.1323/)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 9. A useful explanation makes a claim we can check

**Timing:** 11:00–12:30 (1.5 minutes)

**Slide content:** Read the returned reason. Identify its evidence and the tool result that could support it.
A clear explanation can still be wrong. Keep the numerical check and the original reply.

**Teaching notes:** We show only the public reasons returned in the recorded JSON. We do not expose or infer private internal reasoning. Ask whether the statement matches the input, respects the allowed choices and survives the numerical check. Later the restoration reply says it sorted costs correctly while returning the wrong order. That specific error is an opportunity to inspect the application’s guard.

**Figure scope:** Check the explanation against the recorded facts and tool output.

**Editable figure:** diagrams/bridge_reason_check.tex

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

## 10. Six terms we will use in the notebook

**Timing:** 12:30–14:00 (1.5 minutes)

**Slide content:** Each term describes one job. The language model chooses among tools that do these jobs.
A passing result applies only to the inputs, limits and parts of the network that were checked.

**Teaching notes:** MPC plans controls using a forecast. SAC supplies a proposal from a previously trained controller. MILP chooses whole loads while respecting the stated constraints. WLS finds the state that best fits the weighted readings. Evidence binding checks that inputs and command still match a stored result. Model scope means which network parts and physical effects were included. Also define p.u. as a value divided by its stated base: 1.0 p.u. is that base value. A thermal limit here is a current or flow limit. The objective or cost is the numerical score to optimize after required checks pass.

**Figure scope:** Plain-language meanings. The detailed equations stay in the notebooks and source guide.

**Editable figure:** diagrams/bridge_words.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 11. Know what is running and what is being replayed

**Timing:** 14:00–15:30 (1.5 minutes)

**Slide content:** Green: run a numerical calculation now. Amber: read an actual saved Llama reply in L10B.
Blue: discuss a proposed advisory pilot for a control room after the hands-on work.

**Teaching notes:** Point to these evidence modes throughout the session. Default classroom cells calculate fresh results without a live language-model call. L10B displays verified historical Llama choices, original reasons and associated recorded results. Changing your L2 or L6 input does not change those old replies. The final control-room diagrams are a proposed teaching design, not evidence of a deployed utility platform. No new equipment operation occurs in any of these modes.

**Figure scope:** Three explicitly labeled teaching modes used throughout this workshop.

**Editable figure:** diagrams/bridge_modes.tex

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

## 12. Colab is a workbook with a computer attached

**Timing:** 15:30–17:00 (1.5 minutes)

**Slide content:** The notebook holds instructions, code and outputs. A temporary computer runs the code.
Save your notebook copy. After a runtime reset, rerun setup and the earlier cells.

**Teaching notes:** Explain the picture before using any interface terms. An .ipynb file is the workbook. The runtime is a temporary computer supplied by Colab. Variables and files in its temporary storage are separate from the notebook file. Saving a copy in Drive or downloading the notebook keeps its text, code and saved outputs; it does not keep the whole temporary computer. There is no need to mount the user’s Drive for this lab. The setup cell retrieves the required source and records. We use a CPU runtime and no live language-model service.

**Figure scope:** Notebook file and temporary runtime are different. Google Colab FAQ; original illustration.

**Editable figure:** diagrams/lab_colab_workbook.tex

**Notebook / source locator:** Google Colab FAQ: notebook storage, execution state and temporary virtual machines.

**[COL01] Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 13. One notebook covers all three cases

**Timing:** 17:00–18:30 (1.5 minutes)

**Slide content:** Save a copy in Drive. Keep this same notebook open for all three cases.

**Teaching notes:** Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.

**Figure scope:** Only Classroom Labs is required. The graph and trace notebooks are companion material.

**Editable figure:** diagrams/lab_one_notebook.tex

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 14. Get ready in four small steps

**Timing:** 18:30–20:30 (2 minutes)

**Slide content:** Open the notebook, save your copy, connect a CPU and run setup.
Wait for Ready. Then run L0 and L1 before starting the three cases.

**Teaching notes:** For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or LLM download. If setup stops, reconnect the runtime and rerun setup before starting L0.

**Figure scope:** Setup prepares the runtime. Then follow each named lesson cell with the slides.

**Editable figure:** diagrams/lab_ready.tex

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[COL01] Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

## 15. Find each task by its L label

**Timing:** 20:30–21:30 (1 minutes)

**Slide content:** Use the headings L0 through L12 to find each task.
Run the whole cell with its play button or Shift+Enter. Later cells need earlier results.

**Teaching notes:** The added Colab setup cells changed the numerical cell positions. Use the L headings and stable cell IDs to find the same source in Colab, Jupyter and these slides. A slide shows only the relevant code fragment. Students should run the complete matching notebook cell.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 16. Run a cell, then read what it returns

**Timing:** 21:30–23:00 (1.5 minutes)

**Slide content:** Use the play button beside a code cell. Wait until that cell finishes.
Read the table or plot underneath it. A slide shows a fragment; run the whole matching cell.

**Teaching notes:** Point to the three parts: editable input, run control and returned output. The illustrated input lines are the first two lines of the actual L2 cell, not a complete standalone program. The full cell calls the voltage helper and draws two plots. The runtime remembers variables from earlier cells, which is why we run the lesson in order. If NameError reports a missing variable, return to setup/L0 and rerun the required earlier cells. Do not treat a previously displayed output as the result of a number just edited until you rerun its cell.

**Figure scope:** Teaching illustration, not a Colab screenshot. Input lines match L2; run the full L2 cell.

**Editable figure:** diagrams/lab_cell_loop.tex

**Notebook / source locator:** Google Colab FAQ; Classroom Labs L2, cell classroom-007.

**[COL01] Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 17. Run L0: choose the classroom route

**Timing:** 23:00–25:00 (2 minutes)

**Slide content:** Keep both switches False: new numerical checks, saved controller and archived model replies.
If the data check fails, rerun setup before continuing.

**Teaching notes:** Run all of L0 to import the helpers, configure the plots and initialize the timing record. Keep RUN_OPENDSS=False and RUN_LOCAL_LLAMA=False. These settings skip the optional full-feeder OpenDSS route and local model service. They do not make the calculations prerecorded: L2 and L4 through L9 run fresh numerical calculations or checks, while L12 checks the evidence binding and simulated readback.

**Exact source excerpt:** Classroom_Labs.ipynb L0 (classroom-002), source lines 11–14.
RUN_OPENDSS = False       # True: fresh full-model audit + separate AC MPC solve in L5
RUN_LOCAL_LLAMA = False   # True: one optional local call in L11
ROOT = Path.cwd()
assert (ROOT / 'data/lindistflow3_network.json').exists(), 'Start Jupyter in the tutorial folder'

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 18. New results, saved controller, old replies

**Timing:** 25:00–26:30 (1.5 minutes)

**Slide content:** FRESH means calculated now. SAVED POLICY uses old weights to make a new control proposal.
ARCHIVED ACTUAL LLM means an old model reply, shown with its original input and timing.

**Teaching notes:** A script follows rules written in code. An LLM agent can choose the next allowed tool from a task and the returned results. The diagram shows proposed responsibilities, not a live agent run in this notebook. Ordinary Python functions do the engineering calculations here; the notebook does not run through LangGraph. A saved policy uses learned weights to calculate a new proposal without retraining. Displaying an old language-model reply does not make a new model call. A language model does not replace the power-flow calculation, load-selection solver or state estimator.

**Figure scope:** Proposed roles in an advisory workflow; the default notebook uses Python and saved records.

**Editable figure:** diagrams/common_operator_loop.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 19. Run L1: does the evidence still match?

**Timing:** 26:30–28:00 (1.5 minutes)

**Slide content:** Read binding_pass: does the record match the same inputs and command?
Expect True, False, False. Changing the load or command breaks that match.

**Teaching notes:** Evidence binding means matching a checked record to the exact inputs, proposed command and returned result, using content hashes. Treat L1 as a same-content check, not a test that a physical action passes its limits. The first row keeps the request and command unchanged. The next two rows change a request field or command field, so binding_pass is True, False, False. A failed match calls for new evidence; it does not prove the changed action fails its limits. A matching hash also does not authenticate a sensor.

**Figure scope:** Reference L1 output: only the unchanged request and command match the evidence.

**Figure asset:** images/hands_on_L1_binding.png

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 20. Use the same experiment cycle

**Timing:** 28:00–29:00 (1 minutes)

**Slide content:** Predict, run the default, read the result, change one input and rerun.
Name the next allowed step and the evidence for it.

**Teaching notes:** Pause before showing each output. Ask pairs to write one sentence predicting the change, then compare it with the calculated result. Keep the input values and evidence together. Change only one parameter in the first experiment.

**Figure scope:** Keep the request, proposed command and checked result together.

**Editable figure:** diagrams/common_evidence_binding.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 21. Work in pairs and explain one result

**Timing:** 29:00–30:00 (1 minutes)

**Slide content:** One person runs the cell while the other checks the result. Swap roles in the next case.
Save enough information for another pair to repeat your experiment.

**Teaching notes:** Participants can add a text cell below an output or use paper notes; no extra software is needed. Each pair should finish with one changed-input experiment that another person can repeat. Explain the result and one limit on the claim. The three cases use different networks and do not form a single utility deployment study. Model scope means which parts of the network, quantities and physical effects the calculation covers.

**Figure scope:** Record one changed input, one result, the check outcome and the next decision.

**Editable figure:** diagrams/lab_record.tex

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 22. Voltage: open L2

**Timing:** 30:00–32:00 (2 minutes)

**Slide content:** MPC makes a forecast-based plan. SAC is a saved learned controller.
Check limits first. Then compare penalty score J; smaller is preferred after the checks pass.

**Teaching notes:** The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The command sets active- and reactive-power participation for an inverter fleet. MPC, model predictive control, uses a system model and a short forecast to calculate a plan under limits; here the proposed command is the first step of that plan. SAC, Soft Actor–Critic, is a saved controller learned from rewards. It produces a proposal from old weights without training again. The default calculation covers medium-voltage (MV) phases and MV line currents, with simplified low-voltage (LV) aggregation. Feasible means the proposal passes the limits represented by that model. Compare the penalty score J only after checking those limits; smaller J is preferred for this stated objective. Run L0 and L1 first.

**Figure scope:** Synthetic SMART-DS teaching feeder; not an operating utility circuit.

**Figure asset:** images/feeder.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VCASE] Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

## 23. Control settings and limits

**Timing:** 32:00–34:00 (2 minutes)

**Slide content:** a sets active-power participation; b sets reactive-power participation.
Check the inverter limits, modeled voltages and allowed line current.

**Teaching notes:** Active power delivers net energy; reactive power supports the AC voltage and current balance. The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltages must be between 0.95 and 1.05 per unit (p.u.), where values are divided by a stated base. RATING_FRACTION=0.80 sets allowed current to 80% of the nominal rating. The displayed current percentage uses this reduced allowance as its denominator. Passing the inverter bounds alone does not show that network limits pass.

**Figure scope:** Active and reactive settings share the inverter’s power limit.

**Editable figure:** diagrams/voltage_capability.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 24. Run L2 with the default inputs

**Timing:** 34:00–36:00 (2 minutes)

**Slide content:** Run all of L2 to calculate the MPC plan and check the saved SAC controller’s proposal.
Read feasible, current_step_J and max_allowed_current_pct.

**Teaching notes:** Start with LOAD_SCALE=1.0 and RATING_FRACTION=0.80. The saved SAC actor produces a new proposal by inference; it is not trained in this cell. Both proposals pass the default classroom checks. MPC has the lower current-step J for this case and objective. This single result does not establish a universal control advantage. The output field feasible reports whether the modeled limits pass; current_step_J is this step’s penalty score, and max_allowed_current_pct is maximum current as a percentage of the reduced allowance.

**Exact source excerpt:** Classroom_Labs.ipynb L2 (classroom-007), source lines 1–4.
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

**[VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

## 25. Read the voltage and current plots

**Timing:** 36:00–38:00 (2 minutes)

**Slide content:** Left: compare the sorted modeled voltages with the allowed band.
Right: compare line current with the 100% allowed-current limit.

**Teaching notes:** The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.

**Figure scope:** Reference L2 plots; rerun L2 to calculate plots for your inputs.

**Figure asset:** images/hands_on_L2_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 26. Check limits before comparing scores

**Timing:** 38:00–40:00 (2 minutes)

**Slide content:** Default MPC passes: current use 73.62%, penalty score J about 0.03110.
Default saved SAC passes: current use 51.68%, J about 0.43643.

**Teaching notes:** In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J. Both voltage extrema are within the stated 0.95–1.05 p.u. band for this represented MV model.

**Figure scope:** Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

**Figure asset:** images/hands_on_L2_table.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 27. Exercise 1: tighten the current allowance

**Timing:** 40:00–44:00 (4 minutes)

**Slide content:** In L2, change only RATING_FRACTION from 0.80 to 0.75. Predict, then rerun.
For each method, report feasible, allowed-current use and current_step_J.
Does a PASS cover the full medium- and low-voltage network? Explain.

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 28. Debrief: both proposals still pass

**Timing:** 44:00–46:00 (2 minutes)

**Slide content:** At 0.75, both pass: MPC uses about 78.53% of the allowance; SAC uses about 54.85%.
The tighter allowance raises current use as a percentage, but does not cause failure here.

**Teaching notes:** An incorrect prediction is useful evidence, not a failed exercise. Compare the hypothesis with the actual output. Both candidates retain enough headroom in this case. An optimizer may change its command when a constraint changes, so a simple fixed-ratio argument does not apply to every scenario. The model scope has not expanded.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 29. Change one number and explain the difference

**Timing:** 46:00–47:30 (1.5 minutes)

**Slide content:** A smaller current allowance makes the same current a larger percentage of that allowance.
Record the new percentage and check whether it still stays below 100%.

**Teaching notes:** Use this visual immediately after the first exercise debrief. It shows the measured reference MPC outputs, rounded to two decimal places, for RATING_FRACTION 0.80 and 0.75. The SAC result is also computed in the notebook but is not drawn here. Both proposals pass this particular tighter test. The result is not a general guarantee for other loads or limits. Ask pairs to explain the denominator in the percentage. Restore the default before moving to L3’s independent archived case.

**Figure scope:** Reference L2 exercise: MPC uses 73.62% of the default allowance and 78.53% after the change.

**Editable figure:** diagrams/lab_try_observe.tex

**Notebook / source locator:** Classroom Labs L2, cell classroom-007; verified default and exercise outputs.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 30. Reset L2 before reading old model choices

**Timing:** 47:30–49:30 (2 minutes)

**Slide content:** Restore the default values and rerun L2.
L3–L5 use the original test_01 case, separate from your changed L2 experiment.

**Teaching notes:** Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.

**Exact source excerpt:** Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 31. L3 opens a separate recorded case

**Timing:** 49:30–51:30 (2 minutes)

**Slide content:** Run L3. Read the original case ID, requested operations and recorded seconds.
These reasons are old model replies. Displaying them makes no new model call.

**Teaching notes:** The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.

**Exact source excerpt:** Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.
pool = lab.saved_pool('test_01')
display(pd.DataFrame(pool['responses'])[['model_id', 'operation_id', 'reason', 'seconds', 'source']])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 32. What did the models choose?

**Timing:** 51:30–53:30 (2 minutes)

**Slide content:** Different wording can request the same tool and numbers.
The notebook groups matching trials. An explanation alone does not show that limits pass.

**Teaching notes:** The three old replies reduce to two distinct operations after matching their tool names and numerical parameters. The vote keeps one contribution per model. In test_01, two models vote for the Q-relaxation trial, which relaxes a reactive-power restriction in that declared test. This diagram shows the old input and choices; it is not a new vote after a learner edits L2. Grouping matching trials avoids counting different wording as different physical proposals.

**Figure scope:** Three old replies request two distinct operations; two votes select reactive-power relaxation.

**Editable figure:** diagrams/voltage_canonical_trial.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 33. Run L4: check the old choice again

**Timing:** 53:30–55:30 (2 minutes)

**Slide content:** After L3, run L4. Python checks the selected proposal again for its original case.
Compare majority vote with the saved LinUCB selector on that same case.

**Teaching notes:** The selector is frozen and makes no training updates in this lesson. L4 applies the archived selected operation to its original test context and runs a fresh numerical check. This is a replay with new verification, not a new language-model decision or an online learning experiment. LinUCB is a learned selector that scores the available choices from context; its saved settings stay fixed here.

**Exact source excerpt:** Classroom_Labs.ipynb L4 (classroom-013), source lines 5–9.
started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings['L4 new verification of archived choices'] = time.perf_counter() - started
display(selected_trials['table'])
assert pool['frozen'] and pool['training_updates'] == 24

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H04] Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 34. Separate the old choice from the new check

**Timing:** 55:30–57:30 (2 minutes)

**Slide content:** Both selectors choose the same reactive-power relaxation trial and pass the new MV check.
Predicted reward is a learned score. Read new_check_passes for the engineering check.

**Teaching notes:** The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.

**Figure scope:** Reference L4 output: old selector choices, new numerical checks of the original case.

**Figure asset:** images/hands_on_L4_checks.png

**Notebook / source locator:** Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H04] Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 35. Run L5: check what the model covers

**Timing:** 57:30–59:30 (2 minutes)

**Slide content:** Keep RUN_OPENDSS=False. Run L5 and read the table and optional_mode message.
L5 checks the original test_01 MV-MPC plan. OpenDSS is disabled.

**Teaching notes:** L5 rebuilds the original test_01 case and runs a new check on its original MV-MPC incumbent, meaning the baseline plan saved with that case. This is not the reactive-power-relaxation candidate checked in L4. With RUN_OPENDSS=False, L5 checks only the reduced model and reports that OpenDSS is disabled. This CPU route performs no new full-feeder AC check. A wider-model study saved earlier is not a result calculated today. Model scope means the network parts and physical effects that a check represents.

**Exact source excerpt:** Classroom_Labs.ipynb L5 (classroom-016), source lines 1–4.
started = time.perf_counter()
scope_audit = lab.backend_audit(pool, run_opendss=RUN_OPENDSS)
timings['L5 selected model scope checks'] = time.perf_counter() - started
display(scope_audit['table'])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 36. A PASS covers only the model checked

**Timing:** 59:30–61:30 (2 minutes)

**Slide content:** This check covers medium-voltage (MV) phases and currents, not all low-voltage (LV) equipment.
For a full MV/LV request, get the wider check or HOLD.

**Teaching notes:** Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.

**Figure scope:** Reference L5 output: a medium-voltage check with OpenDSS disabled.

**Figure asset:** images/hands_on_L5_scope.png

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 37. Preview the L12 handover

**Timing:** 61:30–63:30 (2 minutes)

**Slide content:** L12 uses selected_trials from L4, not the new L2 comparison.
Finish L6–L11 first. Run L12 at the end, in notebook order.

**Teaching notes:** Preview the purpose of the final handoff without asking participants to jump ahead. L12 will use selected_trials from L4, not the fresh L2 comparison. It contrasts a full MV/LV request with an explicit MV-only teaching request. Continue to L6 after the voltage checkpoint, finish L6–L11, and run L12 once in the closing section. The readback is a simulated teaching event with no equipment dispatch.

**Figure scope:** Preview only: L12 checks model coverage before a simulated readback.

**Editable figure:** diagrams/voltage_operator_packet.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 38. Preview the two handover outcomes

**Timing:** 63:30–65:30 (2 minutes)

**Slide content:** Full MV/LV request: HOLD. An explicit MV teaching request can pass a simulated readback.
A wrong recommendation ID is rejected. equipment_dispatch stays False.

**Teaching notes:** This screenshot previews the executed default L12 result; students have not run L12 yet. At the final step they will check the returned state and acknowledgment fields. The full-coverage request remains HOLD; the explicit MV teaching scope allows a simulated readback. The simulation does not complete human approval of an archived study and does not dispatch equipment.

**Figure scope:** Reference L12 output; run this cell at the end of the workshop.

**Figure asset:** images/hands_on_L12_packet.png

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 39. Voltage checkpoint: say what ran

**Timing:** 65:30–67:30 (2 minutes)

**Slide content:** L2 makes new proposals; L3 shows old replies; L4–L5 run new checks on test_01.
Report the inputs, proposal, model coverage and result before naming the next step.

**Teaching notes:** Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates an MPC plan and a saved-policy proposal for the current classroom inputs. L3 displays old model replies. L4 runs new checks of the selected trials; L5 checks the original archived plan and its model coverage. Numerical tools provide the physical evidence. The old model choices select a permitted trial; they do not replace these checks. The operator receives an advisory record whose stated coverage must match the request.

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 40. Restoration: open L6

**Timing:** 67:30–68:30 (1 minutes)

**Slide content:** Use the six-node teaching graph. Keep the faulted branch unavailable.
Compare total restored load with restored critical load.

**Teaching notes:** This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks. A tie is an alternative connection that can supply load; CAPACITIES_KW sets its transfer limit in kilowatts.

**Figure scope:** Six-node active-power teaching graph with whole-load pickup and one unavailable branch.

**Editable figure:** diagrams/restoration_fault_map.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 41. Choose the service goal before the plan

**Timing:** 68:30–70:30 (2 minutes)

**Slide content:** The priority goal gives more weight to two critical loads.
The comparison goal serves the most total kW, using the same network and pickup rules.

**Teaching notes:** Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective is the service goal encoded as a score. The priority score gives more weight to these critical loads, while the comparison score maximizes total kW. The difference in selected service comes from that goal. Both numerical methods use the same graph, capacities and whole-load pickup rules. Neither needs a language model to solve this declared problem.

**Figure scope:** Different service goals can select different loads on the same network.

**Editable figure:** diagrams/restoration_priority.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 42. Run L6: change the tie capacity

**Timing:** 70:30–72:30 (2 minutes)

**Slide content:** Run all of L6. MILP chooses whole loads; an exhaustive search checks its priority score.
Read served_kw, critical_kw and MILP_matches_exhaustive_check.

**Teaching notes:** MILP means mixed-integer linear programming. Here it is a whole-load chooser: on/off choices decide which load blocks are served, while linear constraints enforce the stated network rules. Start with tie capacities of 40, 60, 80, 100 and 120 kW. The solver enforces active-power balance, capacity limits, connection to a source, no loops in the energized graph, and exclusion of the faulted branch. An independent exhaustive search checks the priority score on this small graph. Agreement supports this formulation; it does not check the AC physics left out of the model.

**Exact source excerpt:** Classroom_Labs.ipynb L6 (classroom-018), source lines 1–5.
CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings['L6 fresh MILP sweep + independent enumeration'] = time.perf_counter() - started
display(restoration['table'].drop(columns='pickup'))

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 43. Read both service plots

**Timing:** 72:30–74:30 (2 minutes)

**Slide content:** Left: total load served in kW. Right: critical load served in kW.
Overlapping markers mean the two plans give the same result at that tested capacity.

**Teaching notes:** The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.

**Figure scope:** Reference L6 plots; rerun L6 to compare your chosen tie capacities.

**Figure asset:** images/hands_on_L6_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 44. The tradeoff at a 40 kW tie limit

**Timing:** 74:30–76:30 (2 minutes)

**Slide content:** Priority goal: 130 kW total, including 90 kW of critical load.
Most-total-kW goal: 140 kW total, including 30 kW of critical load.

**Teaching notes:** Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.

**Figure scope:** Reference L6 results at a 40 kW tie limit: compare total and critical load served.

**Figure asset:** images/hands_on_L6_table.png

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 45. How Python checks the plan

**Timing:** 76:30–78:30 (2 minutes)

**Slide content:** Check paths to a source, capacity limits, power balance and the faulted branch.
Then compare the MILP service score with the independent exhaustive search.

**Teaching notes:** Numerical checks and same-content evidence matching answer different questions. A record can match the inputs exactly while still omitting AC voltage, reactive-power or protection limits. Comparing the MILP score with every permitted plan is an independent check of this small stated problem. Minimizing energized branches does not calculate the number or order of physical switching steps.

**Figure scope:** Python checks the stated graph constraints, then compares the priority score independently.

**Editable figure:** diagrams/restoration_verify.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[RSTL01] Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.:** [https://arxiv.org/abs/1912.05185v3](https://arxiv.org/abs/1912.05185v3)

**[RSTL02] Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.:** [https://doi.org/10.1109/TPWRS.2017.2720122](https://doi.org/10.1109/TPWRS.2017.2720122)

## 46. Exercise 2: add more tie capacity

**Timing:** 78:30–82:30 (4 minutes)

**Slide content:** Add 180. to CAPACITIES_KW, keeping 40. first. Predict, then rerun L6.
Compare total and critical load served at 40 and 180 kW.
At which of these two capacities do the service goals give the same result?

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 47. Debrief: the tradeoff disappears here

**Timing:** 82:30–84:30 (2 minutes)

**Slide content:** At 180 kW, both methods serve 250 kW total and 90 kW of critical load.
Priority helps in the constrained case. It does not improve every case.

**Teaching notes:** Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 48. Reset the capacity list, then run L7

**Timing:** 84:30–86:30 (2 minutes)

**Slide content:** Restore the original CAPACITIES_KW list and rerun L6.
L7 checks the first 40 kW record, then changes the request to 20 kW.

**Teaching notes:** Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.

**Exact source excerpt:** Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.
rest_record = restoration['records'][0]['weighted']
rest_request = {'task': 'restoration', 'capacity_kw': CAPACITIES_KW[0],
                'critical_nodes': [2, 5], 'model': 'six_node_active_transport', 'revision': 1}

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 49. Read the evidence-match test

**Timing:** 86:30–88:30 (2 minutes)

**Slide content:** Original request: True. Changed rating with the old evidence: False.
HOLD the old recommendation and request a new solve.

**Teaching notes:** This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.

**Figure scope:** Reference L7 output: changed request, unchanged evidence, so a new check is needed.

**Figure asset:** images/hands_on_L7_binding.png

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 50. Changed inputs need a new check

**Timing:** 88:30–90:30 (2 minutes)

**Slide content:** “The evidence is old” does not mean “the changed plan fails its limits.”
Update the request, solve and check it, then match the new evidence to that request.

**Teaching notes:** Evidence binding asks whether a record matches the exact request, proposed plan and returned result. The diagram’s extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision; students do not change topology in that cell. Old evidence is unusable for a changed request even if the old plan might still pass its limits. Ask which new numerical check would establish that for the changed request.

**Figure scope:** L7 changes capacity and revision; extra topology labels are teaching examples.

**Editable figure:** diagrams/restoration_stale.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 51. Proposed agent role: keep the service goal

**Timing:** 90:30–92:30 (2 minutes)

**Slide content:** This cell runs Python: the operator sets the goal and limits; MILP chooses the whole loads.
A proposed agent would request that solve and explain the returned tradeoff.

**Teaching notes:** This is a proposed role for an agent, not a new model decision in the default notebook. The current supervisor is ordinary Python. A future language-model agent could request the allowed solve and explain the returned tradeoff. It must preserve the operator’s service goal and limits, rather than quietly changing weights or making up load values. A different service goal requires an explicit new request and solve. The numerical difference here comes from the optimization objective.

**Figure scope:** Proposed agent responsibilities; the current notebook cell runs Python.

**Editable figure:** diagrams/restoration_plan.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 52. What this model does not check

**Timing:** 92:30–93:30 (1 minutes)

**Slide content:** This active-power graph does not check AC voltage, reactive power or protection.
The energized branches do not give the order of field switching steps.

**Teaching notes:** State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 53. Restoration checkpoint: name the next step

**Timing:** 93:30–95:30 (2 minutes)

**Slide content:** At 40 kW, explain 130 total / 90 critical versus 140 total / 30 critical, all in kW.
For a changed request, keep HOLD until evidence for the current request is available.

**Teaching notes:** Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation.

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 54. Cyber: open L8

**Timing:** 95:30–96:30 (1 minutes)

**Slide content:** Use the separate four-bus DC model and its supplied readings.
Compare a residual alarm, which checks fit, with error against the known teaching truth.

**Teaching notes:** The separate four-bus linear DC model has three unknown voltage angles, measured relative to a reference bus, and eight readings. This DC approximation is not a full AC estimator, malware detector or sensor-authentication system. Synthetic truth is known for the offline classroom comparison only. A residual checks how well the estimate fits the supplied readings; state error checks how far the estimate is from the known teaching truth.

**Figure scope:** Four-bus linear DC teaching model; known synthetic truth is used only for offline comparison.

**Editable figure:** diagrams/cyber_network.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 55. Best fit and true state are different

**Timing:** 96:30–98:30 (2 minutes)

**Slide content:** WLS finds the best fit to readings, giving more weight to lower stated uncertainty.
Residual J measures fit mismatch. State error uses teaching truth unavailable to an operator.

**Teaching notes:** WLS means weighted least squares: find the state that best fits the readings, giving more influence to readings with smaller stated uncertainty. That weighting does not authenticate a reading. Here J is the residual mismatch statistic, not the voltage case’s penalty score. Its chi-square alarm threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. An operator does not have the synthetic truth used to calculate the plotted state error. A small J does not establish that the readings are authentic.

**Figure scope:** A good fit to readings does not show that those readings are authentic.

**Editable figure:** diagrams/cyber_residual.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY01] Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.:** [https://doi.org/10.1109/TPAS.1970.292678](https://doi.org/10.1109/TPAS.1970.292678)

## 56. Run L8: compare two data attacks

**Timing:** 98:30–100:30 (2 minutes)

**Slide content:** Run all of L8 with its default scale list.
Compare one biased reading with the coordinated Hc shift in the table and plots.

**Teaching notes:** L8 runs new WLS calculations. An isolated bias changes one reading. The coordinated Hc shift changes readings in a pattern consistent with a different modeled state. This counterexample assumes knowledge of the linear measurement matrix H and access to the modeled unprotected channels. It is a declared defensive teaching model, not evidence of an incident at a utility.

**Exact source excerpt:** Classroom_Labs.ipynb L8 (classroom-023), source lines 1–5.
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings['L8 fresh WLS attack sweep'] = time.perf_counter() - started
display(cyber['table'])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 57. Read both cyber plots

**Timing:** 100:30–102:30 (2 minutes)

**Slide content:** Left: residual J and its alarm threshold. Right: error against the known teaching truth.
Follow the coordinated curve across both plots before calling a quiet alarm reassuring.

**Teaching notes:** The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.

**Figure scope:** Reference L8 plots; rerun L8 to calculate results for your chosen attack scales.

**Figure asset:** images/hands_on_L8_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 58. At scale 1, the alarm misses a state error

**Timing:** 102:30–104:30 (2 minutes)

**Slide content:** One biased reading: J about 277.50, so the residual alarm is True.
Coordinated Hc: J about 3.92, no alarm, but state error is about 0.02678 rad.

**Teaching notes:** The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace. The state error is measured in radians; it is available here because this is an offline test with known synthetic truth.

**Figure scope:** Simple consistency illustration; the numerical values come from the eight-reading L8 model.

**Editable figure:** diagrams/cyber_stealth.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY02] Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.:** [https://doi.org/10.1145/1952982.1952995](https://doi.org/10.1145/1952982.1952995)

## 59. Exercise 3: add a small isolated bias

**Timing:** 104:30–108:30 (4 minutes)

**Slide content:** Add .10 to ATTACK_SCALES. Predict, then rerun L8.
At scale 0.10, read J, the alarm flag and the error against known teaching truth.
Does “no alarm” mean the reading is correct? Use both plots to explain.

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 60. Debrief: no alarm does not prove truth

**Timing:** 108:30–110:30 (2 minutes)

**Slide content:** At scale 0.10, the isolated-bias J is about 10.14, below the 15.09 threshold.
A small bias can miss the threshold. A coordinated shift can preserve the fit.

**Teaching notes:** Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 61. Reset L8 before the recovery example

**Timing:** 110:30–111:30 (1 minutes)

**Slide content:** Restore the original ATTACK_SCALES list and rerun L8.
L9 uses a fixed recovery case, separate from the scale you changed.

**Teaching notes:** Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.

**Exact source excerpt:** Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 62. L9 uses a fixed recovery case

**Timing:** 111:30–113:30 (2 minutes)

**Slide content:** Check the same case with and without replacement readings assumed to be trusted.
Its control value does not follow your L8 scale change.

**Teaching notes:** The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 63. Trusted readings are an assumption

**Timing:** 113:30–115:30 (2 minutes)

**Slide content:** The example assumes three independent angle readings are trustworthy.
The residual check and a model’s explanation cannot authenticate those readings.

**Teaching notes:** The example assumes three protected angle readings determine the three unknown angles, leaving zero residual degrees of freedom. Independent trusted information must come from a justified source outside this numerical calculation. A zero residual in this exactly determined system adds no detection guarantee. Neither a good model fit nor a language-model explanation establishes authenticity.

**Figure scope:** Three trusted angle readings are assumed, not authenticated by this calculation.

**Editable figure:** diagrams/cyber_trusted.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 64. Run L9: compare HOLD and PROPOSE

**Timing:** 115:30–117:30 (2 minutes)

**Slide content:** Run the whole L9 cell, including its assertions.
Read status first, then the proposed injection and the offline limit-violation count.

**Teaching notes:** The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.

**Exact source excerpt:** Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.
without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 65. Read the two decision states

**Timing:** 117:30–119:30 (2 minutes)

**Slide content:** No trusted replacement readings: HOLD, with no proposed injection.
Trusted readings assumed: PROPOSE; u ≈ 0.121694 p.u.; zero offline toy-model violations.

**Teaching notes:** Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.

**Figure scope:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Figure asset:** images/hands_on_L9_trust.png

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 66. Check the numerical correction

**Timing:** 119:30–121:30 (2 minutes)

**Slide content:** The QP solver minimizes effort, subject to branch limits and a 0.01 p.u. margin.
Predicted flow12: 0.17000; offline actual: about 0.17046, below the 0.18000 rating.

**Teaching notes:** QP means quadratic programming: this numerical solver minimizes a quadratic effort score while enforcing the declared branch limits and a 0.01 p.u. margin. The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. Predicted flow12 is 0.17000 p.u.; the offline actual flow is about 0.17046 p.u., below the 0.18000 p.u. rating. The actual-flow comparison uses synthetic truth for this fixed case. It does not guarantee AC behavior omitted by the model or trustworthy field telemetry.

**Figure scope:** Fixed L9 correction: compare the predicted branch flow with the offline truth check.

**Editable figure:** diagrams/cyber_qp.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 67. What makes the recovery possible?

**Timing:** 121:30–123:30 (2 minutes)

**Slide content:** Assumed trusted readings support the estimate. The solver calculates a limited correction.
The explanation must keep those conditions clear and leave the proposal for review.

**Teaching notes:** Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.

**Figure scope:** Trusted information and numerical checks have separate roles.

**Editable figure:** diagrams/cyber_handoff.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 68. Proposed agent role: request and explain

**Timing:** 123:30–125:30 (2 minutes)

**Slide content:** This cell runs Python. A proposed agent would request the approved estimate and control check.
The operator must confirm the trust basis and review the returned proposal.

**Teaching notes:** The default classroom calls are ordinary deterministic Python functions, so this cell makes no new language-model decision. The slide states a proposed agent responsibility: request the allowed estimator and control tool, then explain the exact conditions returned. The operator must establish the basis for trusting the replacement readings and review the limited proposal through the authorized process. The old model explanations in L10 come from a separate historical study and are not replies to this participant’s changed inputs.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 69. Cyber checkpoint: explain why PROPOSE is allowed

**Timing:** 125:30–127:30 (2 minutes)

**Slide content:** Report the trust assumption, model, proposed u and the checks that passed or failed.
Without independent trusted information, keep HOLD and name what is missing.

**Teaching notes:** Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.'

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 70. Run L10 before the Llama walkthrough

**Timing:** 127:30–130:30 (3 minutes)

**Slide content:** Run L10 to inspect its separate archived five-stage study.
Continue to L10B for the recorded Llama choices, then run L11 with its default False setting.

**Teaching notes:** L10 reads the archived proposal_complete_workflow study. It includes feeder-catalog restoration and is separate from the L6 six-node MILP and your edited classroom inputs. L10B, inserted immediately after L10, then gives readable verified replay episodes for all three cases. Run L11 after those replays; the default False setting skips a new local model request.

**Notebook / source locator:** Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 71. Run L10B: watch Llama choose a tool

**Timing:** 130:30–133:00 (2.5 minutes)

**Slide content:** Run the whole L10B cell. Change SCENARIO to inspect each saved episode.

**Teaching notes:** Run L10 first. In the new L10B cell the helper validates the original JSON reply against the parsed journal and trace, then displays the recorded episode. Change only SCENARIO to inspect the other two episodes. The following slides show selected fields from the same replay. This cell makes no model request and performs no new electrical solve. At the end, run L11 at its default False setting before L12. Llama reasons are historical public returned text. Their correctness must be judged against the input and tool results. SCENARIO can be voltage, restoration or cyber. The full cell is shown.

**Exact source excerpt:** Classroom_Labs.ipynb L10B (classroom-llama-walkthrough), source lines 1–5.
SCENARIO = "voltage"  # Change to "restoration" or "cyber", then rerun this cell.
from IPython.display import HTML, display
from src.llama_walkthrough import load_episodes, render_episode_html
replay_episodes = load_episodes(ROOT)
display(HTML(render_episode_html(replay_episodes[SCENARIO])))

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L10B; cell classroom-llama-walkthrough; src/llama_walkthrough.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[OLL1] Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

## 72. Voltage: Llama asks to check the saved controller

**Timing:** 133:00–135:30 (2.5 minutes)

**Slide content:** Llama identifies the missing check. The current failure forces a new trial.

**Teaching notes:** Read the exact reason. The model was offered VERIFY_SAC_FIRST or REVIEW. The application then checks the saved SAC action in OpenDSS. 111.966607% refers to the allowed current, which was 80% of nominal, so this exceeds the configured allowance. The numerical result records two current violations. This P3 full supplied MV/LV study is separate from L2 and L3 test_01. Ask the audience to predict the next allowed step before advancing.

**Figure scope:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Figure asset:** images/llama_voltage_1.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 1; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 73. Voltage: Llama chooses the existing fallback plan

**Timing:** 135:30–138:00 (2.5 minutes)

**Slide content:** Llama chooses an existing MPC plan. Python checks whether the result passes.

**Teaching notes:** The model selects USE_MPC_PLAN from two allowed choices, the other being REVIEW. It does not invent or solve MPC. The recorded context already supplies a plan and its eligibility. The application performs a fresh numerical check at that historical time. The result is just below the allowed current threshold. No operating permission follows from this check alone. Ask which evidence, rather than wording, makes the fallback eligible for review.

**Figure scope:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Figure asset:** images/llama_voltage_2.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 2; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 74. Voltage: the checks pass and human review remains

**Timing:** 138:00–140:30 (2.5 minutes)

**Slide content:** Human review remains pending. The fixed script returned the same numerical result.

**Teaching notes:** Read the exact REVIEW_EVIDENCE choice and distinguish it from the overall status. The proposed controls are 2387.157 kW and +325.738 kvar. The supplied full MV/LV feeder check returned voltage 1.001783–1.035026 p.u. and zero listed violations. The fixed supervisor used the same SAC-to-MPC sequence with identical numerical output. Recorded workflow intervals were 0.346053 s fixed and 3.110454 s agentic, excluding precomputed MPC/SAC preparation. These are single recorded timings, not performance distributions or a measured reduction in operator workload.

**Figure scope:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Figure asset:** images/llama_voltage_3.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 3; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 75. Restoration: Llama chooses a useful new trial

**Timing:** 140:30–143:00 (2.5 minutes)

**Slide content:** The new trial serves more load, keeps critical service and passes the current check.

**Teaching notes:** Switch L10B to restoration. This is the separate L10 feeder-catalog restoration study, not the L6 six-node MILP. The recorded protocol requires a first refinement but Llama chooses between the offered fractions. SHED_075 disconnects 75% of the ordered noncritical load objects, not 75% of load kW. The exact reason calls improvement a possibility. Python evaluates the trial and finds improved service while the tie loading remains 91.867215% of its allowance. A useful hypothesis becomes evidence only after that check.

**Figure scope:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Figure asset:** images/llama_restoration_14.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 14; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 76. Restoration: the next trial crosses the current limit

**Timing:** 143:00–145:30 (2.5 minutes)

**Slide content:** The next trial fails the current limit. Keep the previous passed candidate.

**Teaching notes:** Keep the actual returned reason visible. It refers to a target in the objective, but its claim should not be accepted as a proved fact. In this record the next trial is numerically rejected for a thermal failure. Restoring more load does not make a failed current check acceptable. Ask participants to explain why the previous passed candidate must remain in the case record. The model’s trial budget is bounded.

**Figure scope:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Figure asset:** images/llama_restoration_15.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 15; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 77. Restoration: catch Llama’s wrong ranking

**Timing:** 145:30–148:00 (2.5 minutes)

**Slide content:** The returned order is wrong. Python chooses the smaller cost and rechecks the plan.

**Teaching notes:** Let pairs answer before discussing the result. Smaller cost is better, so E03 must rank before E02. Llama returns [E02,E03] while its explanation claims lowest score first. The recorded language_order_agrees_with_cost field is False. A deterministic guard retains E03 and rechecks it as E05, with no recorded failures. Human acknowledgment and dispatch remain False. The paired fixed workflow reaches the same final action and cost. This example motivates verification rather than an unsupported superiority claim.

**Figure scope:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Figure asset:** images/llama_restoration_16.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 16; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 78. Cyber: Llama selects the tool already allowed

**Timing:** 148:00–150:30 (2.5 minutes)

**Slide content:** The task supplies the tool and trust assumption. Python computes the correction.

**Teaching notes:** Switch L10B to cyber. This standard four-bus DC record is separate from L10’s proposal-complete cyber record, and matches the Agent Trace notebook T6 archive. The route is narrow: the prompt already authorizes the tool and supplies the trusted-sensor assumption. The three angle readings give full rank but zero residual redundancy, so a good fit is not an independent trust test. u is the flexible injection correction in per unit. Offline synthetic-truth flow is available to the experimenter, not guaranteed available to a real operator.

**Figure scope:** L10B recorded cyber episode. Selected fields; full record and sources in the guide.

**Figure asset:** images/llama_cyber_7.png

**Notebook / source locator:** Classroom Labs L10B: cyber replay, recorded call 7; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 79. Cyber: a passing calculation still needs review

**Timing:** 150:30–153:00 (2.5 minutes)

**Slide content:** Keep REVIEW visible. The operator must resolve the trust assumption and missing checks.

**Teaching notes:** Read the actual reply, including the REVIEW choice. Numerical verification is PASS, but the overall result remains REVIEW and human acknowledgment is PENDING. The fixed comparator obtains the same numerical state estimate and correction without Llama. This replay demonstrates permitted tool routing and a report decision. It does not demonstrate better estimation, authenticated measurements, AC network security or operating authority. Run L11 with the default False setting, then proceed to L12.

**Figure scope:** L10B recorded cyber episode. Selected fields; full record and sources in the guide.

**Figure asset:** images/llama_cyber_8.png

**Notebook / source locator:** Classroom Labs L10B: cyber replay, recorded call 8; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 80. Finish L12: practice the readback

**Timing:** 153:00–157:00 (4 minutes)

**Slide content:** Run all of L12 after completing L0–L11 in notebook order.
Check wrong-ID rejection, simulated acknowledgment and equipment_dispatch=False.

**Teaching notes:** This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record. Readback means repeating the recommendation ID and conditions so the acknowledgment can be matched to the same proposal. In this exercise it is simulated. Check the wrong-ID rejection, the correct simulated acknowledgment and equipment_dispatch=False.

**Exact source excerpt:** Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.
wrong_id = lab.acknowledge(mv_scope, 'wrong-id', 'Student operator')
readback = lab.acknowledge(mv_scope, mv_scope['recommendation_id'], 'Student operator')

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 81. Start a control-room pilot with a clear study request

**Timing:** 157:00–161:00 (4 minutes)

**Slide content:** Use an approved copy of the network data with a time stamp, topology version and limits.
If required data are missing or too old, return HOLD and name the missing information.

**Teaching notes:** Proposed advisory pilot, not a deployment claim. F12 is an illustrative teaching feeder name. Read the study request aloud: compare the allowed voltage-support options, keep the stated current and voltage limits, show the worst margins and missing checks, and return a recommendation for review. The data owner defines acceptable age, source and quality rules. L1 and L7 illustrate matching inputs to results, but hashes alone do not authenticate those sources.

**Figure scope:** Proposed advisory pilot — teaching design. F12 is an illustrative identifier.

**Editable figure:** diagrams/ops_request_snapshot.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 82. Give the assistant a small, controlled tool list

**Timing:** 161:00–165:00 (4 minutes)

**Slide content:** An approved interface supplies read-only data and study tools. Log every request and result.
Keep equipment commands in the utility’s separate authorized operating process.

**Teaching notes:** Proposed advisory pilot. Walk through the lanes: operator, assistant, application-controlled tool gateway and engineering tools. Llama requests one permitted function; the application checks the request and executes the tool. A snapshot identifier binds the result to the input. The workshop Python functions are teaching counterparts, not SCADA adapters. NIST OT guidance supports controlled information flows, least privilege and logging. The exact pilot architecture is our teaching recommendation, not a NIST-certified design.

**Figure scope:** Proposed advisory pilot — teaching design. Classroom functions are not live control-room interfaces.

**Editable figure:** diagrams/ops_tool_boundary.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**[OLL1] Ollama documentation maintainers. Structured Outputs: generating structured JSON with a schema. Official Ollama documentation. Reviewed 24 October 2026.:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 83. Check three things before returning a proposal

**Timing:** 165:00–169:00 (4 minutes)

**Slide content:** Check that the inputs match, the required limits pass and the required network parts were modeled.
Example: an MV-only PASS stays on HOLD when the request requires the full MV/LV network.

**Teaching notes:** Proposed advisory pilot. Current data and a matching evidence packet are the first gate. The second gate checks stated engineering limits with approved tools. The third asks whether the calculations cover the request, including excluded low-voltage parts or required protection and dynamic studies. This is not a universal complete security checklist. It illustrates why L12 can produce a passing local calculation and still HOLD a broader request. Make missing evidence visible instead of allowing fluent text to fill the gap.

**Figure scope:** Proposed advisory pilot — teaching design. A PASS is limited to its tested model and inputs.

**Editable figure:** diagrams/ops_three_gates.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

## 84. Give the operator a short evidence packet

**Timing:** 169:00–173:00 (4 minutes)

**Slide content:** Show the input snapshot, selected option, worst margins, rejected trials and missing checks.
The reviewer can ask for another study, reject the proposal or accept it for the next review step.

**Teaching notes:** Proposed advisory pilot. Use three review questions: Does this match the current equipment, inputs and model? Did the required checks pass, with missing checks clear? What exactly am I approving, who owns the next step, and where is the record? Record the reviewer, reason, case snapshot and tool versions. Accepting a study result does not itself issue an equipment command. Authorized operating procedures and roles determine any later physical action. L12 practices only a simulated ID-bound readback.

**Figure scope:** Proposed advisory pilot — teaching design. Review of a study is distinct from operating equipment.

**Editable figure:** diagrams/ops_review.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**[EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

## 85. Adopt it in stages and measure the benefit

**Timing:** 173:00–177:00 (4 minutes)

**Slide content:** Begin with past cases, then read-only shadow work, then a limited pilot with named reviewers.
Compare against the same tools in a fixed script: correct studies, missed checks, time and rework.

**Teaching notes:** Proposed advisory pilot. Historical replay lets engineers define expected outcomes and failure cases. Shadow use compares recommendations alongside the existing process without relying on them for equipment control. A limited pilot needs a named owner, training, an agreed scope and a way to stop use. Measure end-to-end elapsed time including review, correct completed studies, missed or stale inputs, overlooked limits and reviewer changes. Compare the same engineering tools with and without Llama. Our paired records show identical final numerical results, so there is no basis yet to promise higher accuracy, less operator workload or faster decisions. NIST AI RMF supports human roles, evaluation under realistic conditions and deactivation; these particular pilot metrics are our recommendation.

**Figure scope:** Proposed advisory pilot — teaching design. Benefits must be measured against an appropriate baseline.

**Editable figure:** diagrams/ops_pilot.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

## 86. Save a workshop record others can repeat

**Timing:** 177:00–180:00 (3 minutes)

**Slide content:** Save your changed inputs and results, labeled new, archived or simulated.
Explain the request, tool call, result, checks and next decision.

**Teaching notes:** Use the final three minutes for pair reports and saving. Each pair names one changed parameter, compares its predicted and observed result, and states one evidence limit. Another person should be able to repeat the experiment from the saved notebook. The reading guide supplies the full source links, stable cell map and debrief answers.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## [H00] Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## [B01] IEEE Communications Society: official resources and network presentation template

**Authors / issuer:** IEEE Communications Society

**Publisher / venue:** IEEE Communications Society

**Date:** Reviewed 17 October 2026

**Theme assets:** comsoc-lockup.png and image7.png; independent educational adaptation

**Full source URL:** [https://www.comsoc.org/about/brand-experience/resources](https://www.comsoc.org/about/brand-experience/resources)

## [DEF03] Building effective agents

**Authors / issuer:** Erik S., Barry Zhang

**Publisher / venue:** Anthropic Engineering

**Date:** 2024-12-19

**Type:** Official practitioner architecture account by the system maintainers

**Location:** What are agents?; Agents; Workflow: Routing; Workflow: Orchestrator-workers; Workflow: Evaluator-optimizer

**Version note:** The live page now warns that tooling has changed since the original publication. Use its conceptual distinction, not its present SDK list as a claim about the 2024 implementation.

**Full source URL:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

## [LR0] L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py

**Authors / issuer:** Classroom Labs notebook and Python helper

**Publisher / venue:** Public reproducible teaching material

**Date:** 24 October 2026

**Type:** Verified historical reply replay

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [OLL1] Structured Outputs: generating structured JSON with a schema

**Authors / issuer:** Ollama documentation maintainers

**Publisher / venue:** Official Ollama documentation

**Date:** Reviewed 24 October 2026

**Type:** Official API documentation

**Full source URL:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

## [LRV] Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 27 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/workshop_run_opendss.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/workshop_run_opendss.json)

## [ST01] CS224V Agentic AI, Lecture 1: Introduction

**Authors / issuer:** Monica Lam

**Publisher / venue:** Stanford University

**Date:** Fall 2026

**Type:** University lecture slides, supplied by the presenter

**Full source URL:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**Publication:** [https://web.stanford.edu/class/cs224v/](https://web.stanford.edu/class/cs224v/)

## [ST02] WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia

**Authors / issuer:** Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam

**Publisher / venue:** Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413

**Date:** December 2023

**Type:** Peer-reviewed dialogue research

**Full source URL:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**Full paper PDF:** [https://aclanthology.org/2023.findings-emnlp.157.pdf](https://aclanthology.org/2023.findings-emnlp.157.pdf)

**Source code:** [https://github.com/stanford-oval/WikiChat](https://github.com/stanford-oval/WikiChat)

## [H02] Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [ST03] Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets

**Authors / issuer:** Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam

**Publisher / venue:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308

**Date:** July 2025

**Type:** Peer-reviewed task-oriented dialogue framework

**Full source URL:** [https://aclanthology.org/2025.acl-long.1323/](https://aclanthology.org/2025.acl-long.1323/)

**Full paper PDF:** [https://aclanthology.org/2025.acl-long.1323.pdf](https://aclanthology.org/2025.acl-long.1323.pdf)

**Source code:** [https://github.com/stanford-oval/genie-worksheets](https://github.com/stanford-oval/genie-worksheets)

## [H01] Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [LRR] Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 27 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json)

## [H06] Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H08] Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H12] Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [OT01] Guide to Operational Technology (OT) Security

**Authors / issuer:** Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson

**Publisher / venue:** National Institute of Standards and Technology, NIST SP 800-82 Revision 3

**Date:** September 2023 (final)

**Type:** Published OT security guidance

**Full source URL:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**Full paper PDF:** [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)

**Publication:** [https://csrc.nist.gov/pubs/sp/800/82/r3/final](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

## [COL01] Frequently Asked Questions: Using Colab, notebook storage and execution state

**Authors / issuer:** Google Colaboratory

**Publisher / venue:** Google Research

**Date:** Reviewed 24 October 2026

**Type:** Official product documentation

**Full source URL:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

## [VCASE] Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope

**Authors / issuer:** Existing GridGuard workshop / SMART-DS synthetic-feeder extraction

**Publisher / venue:** data.openei.org

**Date:** Existing teaching snapshot reviewed 18 October 2026

**Type:** Existing local scientific model figure; external URL is the dataset reference retained by the original workshop

**Full source URL:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

## [VMPC] Model Predictive Control: Theory, Computation, and Design, second edition

**Authors / issuer:** James B. Rawlings; David Q. Mayne; Moritz M. Diehl

**Publisher / venue:** Nob Hill Publishing

**Date:** 2017

**Type:** Primary author-hosted textbook

**Full source URL:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

## [VSAC] Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

**Authors / issuer:** Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine

**Publisher / venue:** Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870

**Date:** 2018

**Type:** Primary research paper

**Full source URL:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

## [H03] Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H04] Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H05] Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [RSTL01] On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems

**Authors / issuer:** Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang

**Publisher / venue:** Author preprint, arXiv:1912.05185v3

**Date:** 15 March2020(v3); first submitted11 December2019

**Full source URL:** [https://arxiv.org/abs/1912.05185v3](https://arxiv.org/abs/1912.05185v3)

**Full paper PDF:** [https://arxiv.org/pdf/1912.05185v3](https://arxiv.org/pdf/1912.05185v3)

## [RSTL02] Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids

**Authors / issuer:** Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry

**Publisher / venue:** IEEE Transactions on Power Systems33(2),1507–1520

**Date:** March2018

**Full source URL:** [https://doi.org/10.1109/TPWRS.2017.2720122](https://doi.org/10.1109/TPWRS.2017.2720122)

## [H07] Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [CY01] Power System Static-State Estimation, Part I: Exact Model

**Authors / issuer:** Fred C. Schweppe, J. Wildes

**Publisher / venue:** IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125

**Date:** January 1970

**Full source URL:** [https://doi.org/10.1109/TPAS.1970.292678](https://doi.org/10.1109/TPAS.1970.292678)

## [CY02] False Data Injection Attacks against State Estimation in Electric Power Grids

**Authors / issuer:** Yao Liu, Peng Ning, Michael K. Reiter

**Publisher / venue:** ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages

**Date:** May 2011

**Full source URL:** [https://doi.org/10.1145/1952982.1952995](https://doi.org/10.1145/1952982.1952995)

**Full paper PDF:** [https://reitermk.github.io/papers/2011/TISSEC2.pdf](https://reitermk.github.io/papers/2011/TISSEC2.pdf)

## [H09] Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H10] Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [LRC] Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 21 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json)

## [EVAL01] Artificial Intelligence Risk Management Framework (AI RMF 1.0)

**Authors / issuer:** National Institute of Standards and Technology

**Publisher / venue:** NIST AI 100-1

**Date:** 26 January 2023

**Type:** Voluntary risk-management guidance

**Full source URL:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

**Full paper PDF:** [https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

## Visual credit: hands_on_L1_binding.png

**Caption:** Reference L1 output: only the unchanged request and command match the evidence.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 19. Run L1: does the evidence still match?

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L1 output: only the unchanged request and command match the evidence.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L1_binding.png](research/evidence/replots/hands_on_L1_binding.png)

## Visual credit: feeder.png

**Caption:** Synthetic SMART-DS teaching feeder; not an operating utility circuit.

**Credit:** Existing GridGuard workshop numerical figure

**Used on:** 22. Voltage: open L2

**Asset type:** Synthetic feeder visualization

**Transformation:** Unchanged original plot.

**Evidence limit:** Synthetic SMART-DS teaching feeder; not an operating utility circuit.

**Original source / page:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

**Original figure / image URL:** [research/evidence/replots/feeder.png](research/evidence/replots/feeder.png)

## Visual credit: hands_on_L2_plot.png

**Caption:** Reference L2 plots; rerun L2 to calculate plots for your inputs.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 25. Read the voltage and current plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L2 plots; rerun L2 to calculate plots for your inputs.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_plot.png](research/evidence/replots/hands_on_L2_plot.png)

## Visual credit: hands_on_L2_table.png

**Caption:** Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 26. Check limits before comparing scores

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L2 output with LOAD_SCALE=1.0 and RATING_FRACTION=0.80.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_table.png](research/evidence/replots/hands_on_L2_table.png)

## Visual credit: hands_on_L4_checks.png

**Caption:** Reference L4 output: old selector choices, new numerical checks of the original case.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 34. Separate the old choice from the new check

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L4 output: old selector choices, new numerical checks of the original case.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L4_checks.png](research/evidence/replots/hands_on_L4_checks.png)

## Visual credit: hands_on_L5_scope.png

**Caption:** Reference L5 output: a medium-voltage check with OpenDSS disabled.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 36. A PASS covers only the model checked

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L5 output: a medium-voltage check with OpenDSS disabled.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L5_scope.png](research/evidence/replots/hands_on_L5_scope.png)

## Visual credit: hands_on_L12_packet.png

**Caption:** Reference L12 output; run this cell at the end of the workshop.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 38. Preview the two handover outcomes

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L12 output; run this cell at the end of the workshop.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L12_packet.png](research/evidence/replots/hands_on_L12_packet.png)

## Visual credit: hands_on_L6_plot.png

**Caption:** Reference L6 plots; rerun L6 to compare your chosen tie capacities.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 43. Read both service plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L6 plots; rerun L6 to compare your chosen tie capacities.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_plot.png](research/evidence/replots/hands_on_L6_plot.png)

## Visual credit: hands_on_L6_table.png

**Caption:** Reference L6 results at a 40 kW tie limit: compare total and critical load served.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 44. The tradeoff at a 40 kW tie limit

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L6 results at a 40 kW tie limit: compare total and critical load served.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_table.png](research/evidence/replots/hands_on_L6_table.png)

## Visual credit: hands_on_L7_binding.png

**Caption:** Reference L7 output: changed request, unchanged evidence, so a new check is needed.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 49. Read the evidence-match test

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L7 output: changed request, unchanged evidence, so a new check is needed.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L7_binding.png](research/evidence/replots/hands_on_L7_binding.png)

## Visual credit: hands_on_L8_plot.png

**Caption:** Reference L8 plots; rerun L8 to calculate results for your chosen attack scales.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 57. Read both cyber plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L8 plots; rerun L8 to calculate results for your chosen attack scales.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L8_plot.png](research/evidence/replots/hands_on_L8_plot.png)

## Visual credit: hands_on_L9_trust.png

**Caption:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 65. Read the two decision states

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L9_trust.png](research/evidence/replots/hands_on_L9_trust.png)

## Visual credit: llama_voltage_1.png

**Caption:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 72. Voltage: Llama asks to check the saved controller

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_1.png](research/evidence/replots/llama_voltage_1.png)

## Visual credit: llama_voltage_2.png

**Caption:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 73. Voltage: Llama chooses the existing fallback plan

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_2.png](research/evidence/replots/llama_voltage_2.png)

## Visual credit: llama_voltage_3.png

**Caption:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 74. Voltage: the checks pass and human review remains

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** L10B recorded voltage episode. Selected fields; full record and sources in the guide.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_3.png](research/evidence/replots/llama_voltage_3.png)

## Visual credit: llama_restoration_14.png

**Caption:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 75. Restoration: Llama chooses a useful new trial

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_14.png](research/evidence/replots/llama_restoration_14.png)

## Visual credit: llama_restoration_15.png

**Caption:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 76. Restoration: the next trial crosses the current limit

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_15.png](research/evidence/replots/llama_restoration_15.png)

## Visual credit: llama_restoration_16.png

**Caption:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 77. Restoration: catch Llama’s wrong ranking

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** L10B recorded restoration episode. Selected fields; full record and sources in the guide.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_16.png](research/evidence/replots/llama_restoration_16.png)

## Visual credit: llama_cyber_7.png

**Caption:** L10B recorded cyber episode. Selected fields; full record and sources in the guide.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 78. Cyber: Llama selects the tool already allowed

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** L10B recorded cyber episode. Selected fields; full record and sources in the guide.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_cyber_7.png](research/evidence/replots/llama_cyber_7.png)

## Visual credit: llama_cyber_8.png

**Caption:** L10B recorded cyber episode. Selected fields; full record and sources in the guide.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 79. Cyber: a passing calculation still needs review

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** L10B recorded cyber episode. Selected fields; full record and sources in the guide.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_cyber_8.png](research/evidence/replots/llama_cyber_8.png)
