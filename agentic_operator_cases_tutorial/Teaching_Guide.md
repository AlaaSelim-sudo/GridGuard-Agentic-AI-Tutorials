# Teaching and Source Guide

Hands-on: Three Operator Cases — notebook-aligned tutorial. Evidence reviewed 24 October 2026. The full reading guide is separate from the timed main talk. Corporate issuers are listed when no individual author is recorded. Original figures, page locations and image-source credits are included. Attribution alone is not a blanket reuse license.

## Using the lab and source guide

**Format:** 80 slides, one notebook and three operator cases. Follow along during the session or finish the experiments afterward.

**Prerequisite:** Use the foundations tutorial first. This session follows the current Classroom Labs notebook through voltage support, service restoration and cyber response.

**Evidence modes:** Run the selected numerical cells to calculate results for your inputs. Archived model-response pools and historical evaluation records remain separately labeled. Editing L2 does not change the archived test_01 used by L3–L5, and editing the L8 sweep does not change the fixed L9 recovery fixture. No default cell calls an LLM or operates equipment.

**Setup:** Open Classroom Labs, save a copy in Drive and connect a CPU. Run setup, wait for Ready, then run L0 and L1. Keep both switches False. No API key, LLM download or GPU is needed.

**Lab order:** Voltage L2-L5, restoration L6-L7, cyber L8-L9, then saved agent records L10-L10B and simulated readback L12. Leave L11 disabled.

**Source figures:** Monica Lam, CS224V Agentic AI, Lecture 1: Introduction, Stanford University, Fall 2026, pp.2, 19, 40 and 53. Original excerpts keep their source credits. Grid diagrams are teaching adaptations. This notebook does not run WikiChat, Genie Worksheets or a theorem prover.

**Five-role workflow:** Slides 74-77 map the custom Python workflow to all three recorded L10 cases. One Llama model fills the planning and optimizer roles. Python runs awareness, simulation and verification. The notebook replays these saved stages; it does not launch five independent LLM agents.

## 1. Hands-on: Three Operator Cases

**Timing:** 00:00–01:00 (1 minutes)

**Slide content:** One notebook. Three operator problems.
90 minutes / three short exercises

**Teaching notes:** One Classroom Labs notebook covers all three cases. Follow the L labels in order, keep both optional-tool switches False and use the saved Llama examples after the numerical cases. Learners can follow along during the 90-minute lecture and finish the experiments afterward. Presenters and affiliations are supplied by the presenters.

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[B01] IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.:** [https://www.comsoc.org/about/brand-experience/resources](https://www.comsoc.org/about/brand-experience/resources)

## 2. What is agentic AI?

**Timing:** 01:00–02:00 (1 minutes)

**Slide content:** An AI agent chooses a tool, reads its result and chooses the next step toward a goal.

**Teaching notes:** Use the architectural definition in Anthropic, Building effective agents: an agent lets the LLM direct its process and tool use. Agentic AI is a broad term; here it means a system organized around this bounded loop. An AI agent is the component that chooses and follows steps. A tool is a permitted software function that returns a result. Point to the goal, model choice, executable tool, returned evidence and feedback arrow. The application stores case facts and prior results as the context supplied at the next model request. If a required check is missing, the outcome remains HOLD. Stop or return a proposal only under the fixed workflow rules. Do not imply that feedback alone establishes agency: conventional programs can also branch and loop. Our default notebook calculates engineering results now but replays the actual old Llama choices. No live model service is needed. Stanford source: Monica Lam, CS224V Agentic AI, Lecture 1: Introduction, Fall 2026, p.2 describes function calling and agentic workflows. The goal-and-feedback drawing is our grid teaching adaptation, supported by the separate bounded-agent architecture citation. This is not an original Stanford power-system diagram.

**Figure scope:** Teaching diagram. Llama choices are saved; Python calculations can run now.

**Editable figure:** diagrams/agent_goal_loop.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 3. A tool call and an agent workflow

**Timing:** 02:00–02:30 (0.5 minutes)

**Slide content:** A tool call does one job. An agent links jobs using the returned results.

**Teaching notes:** Show the two original capability panels from Monica Lam’s Stanford CS224V introduction, p.2. The left panel introduces model-selected function calling. The right panel describes multi-step planning, tool use and self-correction. Our plain-language sentence connects the panels to the preceding bounded-loop teaching drawing. The following source-and-lab pairs show why tool results, explicit goals and checked evidence matter in each case. In that example Llama requests a named action and Python validates the JSON choice before calling an existing function; it does not use a native tool_calls protocol. Conventional software can also loop, and a chatbot may itself contain an agent. Here we identify the agentic feature by the model’s permitted next-step choice based on returned evidence. The class replays those old model choices while numerical cells calculate current results. Source lecture figure is shown unchanged within the documented crop.

**Figure scope:** Source figure, p.2. Function calling and a multi-step workflow.

**Figure asset:** images/stanford_agentic_capabilities.png

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 4. Evidence before an answer

**Timing:** 02:30–03:00 (0.5 minutes)

**Slide content:** WikiChat checks claims before writing. Our lab checks numbers before reporting a result.

**Teaching notes:** The displayed figure is an original excerpt from Monica Lam’s Stanford CS224V introduction, p.19. Follow its retrieval, claim checking and writing steps. The WikiChat paper is fully cited in the reading guide. Our application to grid studies is a teaching analogy: read the stated limits, run the appropriate numerical check and summarize the actual returned result. Ask which lab step would detect a current violation. The classroom notebook does not run WikiChat; its dialogue factuality measurements are not electrical performance results. This source figure is now in the opening. Spend about one minute on the check-before-writing idea. The next slide maps it to L2; do not run a cell yet.

**Figure scope:** Source figure, p.19. WikiChat checks claims before writing.

**Figure asset:** images/stanford_wikichat_steps.png

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.19.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 5. Voltage: propose, then check

**Timing:** 03:00–03:30 (0.5 minutes)

**Slide content:** L2 calculates and checks proposals. L10B shows saved Llama tool choices.

**Teaching notes:** Connect the preceding original WikiChat figure to a grid claim. A text answer might say that a proposed plan fits the limits; a numerical tool must calculate the supporting result. The reference bar is the default L2 MPC result: maximum allowed-current utilization 73.619901%, rounded to 73.62%, at LOAD_SCALE=1.0 and RATING_FRACTION=0.80. It passes this current allowance; modeled voltage and required model coverage must also be checked. The default medium-voltage calculation is not proof for the full MV/LV system. This visual previews the lab; do not run L2 before setup, L0 and L1. L2 calls numerical functions directly. The separate P3 L10B archive later shows Llama requesting a check, reading a failed result and selecting a fallback. Our application is an analogy to evidence checking, not a claim that the notebook runs WikiChat.

**Figure scope:** Teaching adaptation. L2 runs Python; L10B replays saved model choices.

**Editable figure:** diagrams/stanford_colab_voltage.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.19; Classroom Labs L2.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 6. Clear rules for tool use

**Timing:** 03:30–04:30 (1 minutes)

**Slide content:** Set the inputs, allowed tools, limits and stop rules.
Python keeps these rules fixed when Llama chooses a step.

**Teaching notes:** Stanford connection: Lam p.40 and the published Genie Worksheets paper emphasize developer-defined workflows and knowledge sources. The published framework uses an algorithmic runtime to enforce a supplied policy, with LLMs used for language understanding and response generation. Our lab uses custom Python functions, not Genie Worksheets. The application analogy is to specify the task and prevent a language reply from silently changing its limits or filling missing required inputs. A passed calculation does not prove that the task description was correct. The figure shown here is an actual excerpt from the supplied Stanford lecture. Ask the audience to point to the claim-checking or policy step, then identify the corresponding Python check in our lab. We borrow the design habit; the notebook does not run WikiChat or Genie. Their non-grid benchmarks are not electrical performance results.

**Figure scope:** Source figure, p.40. Task rules define permitted tool use.

**Figure asset:** images/stanford_genie_specification.png

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST03] Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.:** [https://aclanthology.org/2025.acl-long.1323/](https://aclanthology.org/2025.acl-long.1323/)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 7. Restoration: define the service goal

**Timing:** 04:30–05:00 (0.5 minutes)

**Slide content:** The goal changes which loads the solver restores. L6 compares two goals.

**Teaching notes:** The preceding Genie excerpt motivates writing down the task and its rules before calling a function. In L6 the goal is part of the optimization problem: priority weighting serves 130 total kW, including 90 critical kW; maximizing total service gives 140 total kW, including 30 critical kW. The 40 kW limit belongs to one varied tie, while another tie stays fixed at 100 kW. Totals also include the 40 kW load at node 1 upstream of those ties. A 40 kW varied-tie limit is not a cap on total system service. Each stacked bar uses the same scale. Critical service is cyan; other service is blue. Ask which goal better matches an illustrative request to prioritize a hospital. The numerical model uses abstract critical loads, not an actual hospital dataset. Later learners run both goals and change the tie capacity. L6 is a direct Python calculation, not a live LLM agent. An agent coordinating such a study must preserve the requested goal and explain the returned tradeoff. The separate L10B feeder-catalog archive supplies actual saved Llama choices; it differs from this six-node L6 model. Our notebook does not implement Genie Worksheets.

**Figure scope:** L6: same network and limits, different service goals.

**Editable figure:** diagrams/stanford_colab_restoration.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40; Classroom Labs L6.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST03] Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.:** [https://aclanthology.org/2025.acl-long.1323/](https://aclanthology.org/2025.acl-long.1323/)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 8. Language and decision checks

**Timing:** 05:00–05:30 (0.5 minutes)

**Slide content:** The source example turns written facts into constraints for a solver.
In our lab, Llama requests a study. Python checks it. A person reviews it.

**Teaching notes:** This original diagram selection comes from the function row on p.53 of Monica Lam’s introduction. It shows a clinical-trial example, not a power-system experiment. The language model translates written facts into an SMT representation; a separate solver derives a decision from those constraints. SMT means satisfiability modulo theories, a way to express and solve logical constraints. MaxSAT supports the lecture’s search for conditions that change a decision. The lecture also states that the formalization may not be completely faithful, so correctness remains relative to the represented constraints. Our application is an analogy: Llama requests the permitted estimate or control tool and Python checks numerical limits. An operator must still confirm the trust assumption and review the proposed action. Our notebook does not run an SMT/MaxSAT solver or prove formal electrical safety. Preview the HOLD/PROPOSE distinction now; participants will calculate the L9 outcomes later with their stated model and trusted-data assumption.

**Figure scope:** Source figure, p.53. Clinical example using logical constraints, not a power-system model.

**Figure asset:** images/stanford_language_decision.png

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 9. Cyber: good fit can hide bad data

**Timing:** 05:30–06:00 (0.5 minutes)

**Slide content:** L8 tests misleading readings. L9 shows when to return HOLD or a proposal.

**Teaching notes:** Relate the original Stanford clinical example to this lab without importing a formal guarantee. L8 fits readings to a four-bus DC model using WLS, weighted least squares. Its small residual is a measure of fit, not proof of sensor truth; the known simulation truth is used only for teaching error comparisons. L9 is a separate fixed recovery fixture. Without trusted replacement data it returns HOLD. With three additional readings assumed trusted and a successful modeled recovery check, it returns PROPOSE. The yes branch depicts this fixed example with passing numerical checks; a real study also needs every required check to pass. The calculation does not authenticate the extra readings. Later learners run L8, vary the attack scale, then reset before the independent L9 example. Python performs these calculations now. A coordinating agent should request evidence and retain HOLD when a required premise is missing; saved L10B replies show a separate recorded cyber case. Our code uses numerical checks, not the Stanford SMT/MaxSAT runtime.

**Figure scope:** L8 checks fit. L9 requires a trust assumption before proposing recovery.

**Editable figure:** diagrams/stanford_colab_cyber.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53; Classroom Labs L8–L9.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 10. Four questions about any result

**Timing:** 06:00–07:00 (1 minutes)

**Slide content:** Which tool ran? What did it assume? Which limits passed? What should the operator do next?

**Teaching notes:** Lam’s pp.52–53 distinguish verifiable rationale, explicit assumptions, policy consistency and actionable next conditions. Translate these into four plain questions: which tool supports this claim, which inputs and model were used, were the same limits and service priorities kept, and what must the operator review next? Our power-flow, optimization and evidence-binding checks are numerical/software checks. They do not inherit the lecture’s SMT correctness claims. Ask pairs to apply the questions to one L10B explanation and to the full-scope HOLD at L12. We show only the actual public returned reasons, not hidden chain-of-thought. This closes the twelve-minute opening concept block. Point out that all three labs will use these questions; participants do not need to memorize a framework or run ahead.

**Figure scope:** Teaching adaptation of the cited lecture. The lab uses custom Python.

**Editable figure:** diagrams/lab_review_questions.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, pp.52–53.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 11. One notebook for all three cases

**Timing:** 07:00–08:00 (1 minutes)

**Slide content:** Open Classroom Labs and save a copy in Drive. Use it throughout.

**Teaching notes:** Open https://alaaselim-sudo.github.io/GridGuard-Agentic-AI-Tutorials/#notebooks and choose the first notebook, Classroom Labs. The LangGraph and trace notebooks are separate companions. Keep the slides in one tab and Classroom Labs in another.

**Figure scope:** Classroom Labs is the only required notebook.

**Editable figure:** diagrams/lab_one_notebook.tex

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

## 12. Colab setup

**Timing:** 08:00–10:30 (2.5 minutes)

**Slide content:** Save a copy, connect a CPU and run setup.
Wait for Ready, then run L0 and L1.

**Teaching notes:** For a paced workshop, run the setup cell first, then run each named lesson cell when prompted. Runtime > Run all also works, but it reveals later outputs before the prediction questions. The default route needs no GPU, API key or LLM download. If setup stops, reconnect the runtime and rerun setup before starting L0.

**Figure scope:** Setup first, then L0 and L1.

**Editable figure:** diagrams/lab_ready.tex

**Notebook / source locator:** Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[COL01] Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

## 13. Input, run, output

**Timing:** 10:30–11:00 (0.5 minutes)

**Slide content:** Find the L heading and run its whole code cell.
Read the output below it. After any edit, rerun the cell.

**Teaching notes:** Point to the three parts: editable input, run control and returned output. The illustrated input lines are the first two lines of the actual L2 cell, not a complete standalone program. The full cell calls the voltage helper and draws two plots. The runtime remembers variables from earlier cells, which is why we run the lesson in order. If NameError reports a missing variable, return to setup/L0 and rerun the required earlier cells. Do not treat a previously displayed output as the result of a number just edited until you rerun its cell. Use the L labels instead of numerical cell indexes. Later cells need earlier variables.

**Figure scope:** Illustration of a code cell. Run the full L2 cell.

**Editable figure:** diagrams/lab_cell_loop.tex

**Notebook / source locator:** Google Colab FAQ; Classroom Labs L2, cell classroom-007.

**[COL01] Google Colaboratory. Frequently Asked Questions: Using Colab, notebook storage and execution state. Google Research. Reviewed 24 October 2026.:** [https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 14. L0: keep the default settings

**Timing:** 11:00–12:30 (1.5 minutes)

**Slide content:** Leave both switches False. Python calculates new results; Llama replies come from saved records.
If data are missing, rerun setup.

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

## 15. L1: does the result match the request?

**Timing:** 12:30–15:00 (2.5 minutes)

**Slide content:** Read binding_pass. Expect True, False, False.
Changed inputs or commands need a new check.

**Teaching notes:** Evidence binding means matching a checked record to the exact inputs, proposed command and returned result, using content hashes. Treat L1 as a same-content check, not a test that a physical action passes its limits. The first row keeps the request and command unchanged. The next two rows change a request field or command field, so binding_pass is True, False, False. A failed match calls for new evidence; it does not prove the changed action fails its limits. A matching hash also does not authenticate a sensor.

**Figure scope:** Reference L1 output. Only the unchanged request and command match.

**Figure asset:** images/hands_on_L1_binding.png

**Notebook / source locator:** Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 16. Case 1: voltage support

**Timing:** 15:00–15:30 (0.5 minutes)

**Slide content:** MPC plans ahead. SAC uses a saved learned policy.
Check limits first. Among passing options, a smaller score J is better.

**Teaching notes:** The feeder is a synthetic SMART-DS Greensboro-area example, not a measured utility circuit. The command sets active- and reactive-power participation for an inverter fleet. MPC, model predictive control, uses a system model and a short forecast to calculate a plan under limits; here the proposed command is the first step of that plan. SAC, Soft Actor–Critic, is a saved controller learned from rewards. It produces a proposal from old weights without training again. The default calculation covers medium-voltage (MV) phases and MV line currents, with simplified low-voltage (LV) aggregation. Feasible means the proposal passes the limits represented by that model. Compare the penalty score J only after checking those limits; smaller J is preferred for this stated objective. Run L0 and L1 first.

**Figure scope:** Synthetic SMART-DS feeder used for teaching.

**Figure asset:** images/feeder.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VCASE] Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

## 17. Two ways to propose settings

**Timing:** 15:30–16:30 (1 minutes)

**Slide content:** MPC plans with a model. SAC proposes from learned weights. Both need the same electrical checks.

**Teaching notes:** MPC uses a model and a short forecast to optimize a plan; this lab applies its first action. SAC is a saved policy learned through reinforcement learning; it produces a new control proposal using old weights, without training again. Neither is the coordinating LLM. The outer agent can choose which permitted study to request. L2 calls both tools directly and displays their checks; this cell alone is not a live LLM agent. Later recorded P3 figures illustrate Llama coordinating the existing tools. Define per unit when the control-limit slide introduces the voltage scale: 1.0 p.u. is the stated base value. Explain MILP and WLS only in their respective cases.

**Figure scope:** MPC = model predictive control. SAC = Soft Actor-Critic.

**Editable figure:** diagrams/agent_mpc_sac.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

**[VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

## 18. A tool result changes the next step

**Timing:** 16:30–18:00 (1.5 minutes)

**Slide content:** The first trial fails. Llama requests the fallback. A passing result goes to human review.

**Teaching notes:** This is an actual saved Llama 3.1:8b voltage episode, not a fabricated interactive exchange. Call 1 selects VERIFY_SAC_FIRST; the numerical check returns 111.966607 percent of allowed current and two current violations. Call 2 selects USE_MPC_PLAN; its numerical check returns 99.604410 percent of allowed current and no recorded violations. The SAC and MPC tools already exist; Llama does not invent or solve the power flow. The arrows show tool-request, result, next-request, result. Call 3 selects REVIEW_EVIDENCE. Human acknowledgment remains PENDING and equipment_dispatch is False. This separate P3 MV/LV OpenDSS archive differs from the fresh L2 exercise and from L3 test_01. Later voltage slides display the exact public returned reasons; learners can replay the source in L10B after completing the three cases. The fixed comparator reaches the same numerical outcome, so the trace illustrates coordination rather than a proven performance improvement. This recorded example now follows the MPC/SAC definition slide in the voltage case, after Colab setup. It remains a preview; run the complete episode in L10B later.

**Figure scope:** Saved P3 OpenDSS example, separate from L2. Values rounded.

**Editable figure:** diagrams/agent_recorded_trace.tex

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 19. Two control settings

**Timing:** 18:00–19:00 (1 minutes)

**Slide content:** a controls active power. b controls reactive power.
Check inverter capacity, voltage and line current.

**Teaching notes:** Active power delivers net energy; reactive power supports the AC voltage and current balance. The command uses P_i = a S_i and Q_i = b S_i. Its bounds are 0 <= a <= 1, |b| <= 0.44 and a^2 + b^2 <= 1. Modeled voltages must be between 0.95 and 1.05 per unit (p.u.), where values are divided by a stated base. RATING_FRACTION=0.80 sets allowed current to 80% of the nominal rating. The displayed current percentage uses this reduced allowance as its denominator. Passing the inverter bounds alone does not show that network limits pass.

**Figure scope:** Active and reactive power share the inverter capacity.

**Editable figure:** diagrams/voltage_capability.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 20. A tool is a callable function

**Timing:** 19:00–19:30 (0.5 minutes)

**Slide content:** Inputs go in. Calculations run. Results come back. L2 calls this Python function directly.

**Teaching notes:** Find the actual function call on the next slide. The first two cell lines set the load scale and current allowance; the helper returns numerical proposals, checks and a table for plotting. A tool can be an optimizer, simulator, estimator, lookup or evidence checker. It is not the LLM itself. The student initiates this direct function call with the play button. In the separate recorded workflow Llama selects a named action, the Python application validates that action and its inputs, then invokes a permitted numerical function. Do not claim that the L2 helper uses a live agent gateway. Saving a notebook is separate from keeping a runtime: after a reset, rerun setup and earlier cells.

**Figure scope:** L2 calls lab.voltage_lab directly. Agent coordination is shown in the saved study.

**Editable figure:** diagrams/agent_python_tool.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 21. L2: run the default case

**Timing:** 19:30–22:30 (3 minutes)

**Slide content:** Run all of L2. It checks the MPC plan and the saved SAC policy.
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

## 22. L2: voltage and current plots

**Timing:** 22:30–23:30 (1 minutes)

**Slide content:** Left: voltages should stay inside the allowed band.
Right: current use should stay below 100% of the allowance.

**Teaching notes:** The left panel sorts each voltage curve separately. The same horizontal position means the same rank, not necessarily the same physical bus. The right panel reports current relative to the reduced allowance. Use the output table for exact extrema and feasibility; do not decide acceptance from a plot alone.

**Figure scope:** Reference L2 plots. Rerun for your inputs.

**Figure asset:** images/hands_on_L2_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 23. L2: both default proposals pass

**Timing:** 23:30–24:30 (1 minutes)

**Slide content:** MPC: 73.62% current use, score J about 0.03110.
Saved SAC: 51.68% current use, score J about 0.43643.

**Teaching notes:** In the reference execution, MPC returns a=0.960307 and b=-0.111114, with Vmin=1.023874 and Vmax=1.038709 p.u. SAC returns a=0.340066 and b=0.014024, with Vmin=1.013243 and Vmax=1.030000 p.u. Values may vary slightly with the solver or dependency version. Lower current use need not mean lower J, because the objective also includes service and control terms. Check feasibility before comparing J. Both voltage extrema are within the stated 0.95–1.05 p.u. band for this represented MV model.

**Figure scope:** Reference L2: load scale 1.0, current allowance 0.80.

**Figure asset:** images/hands_on_L2_table.png

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 24. The limit and the calculated result

**Timing:** 24:30–25:00 (0.5 minutes)

**Slide content:** A rule states the limit. A tool checks the proposal against it.
Keep both with the result so the operator can review it.

**Teaching notes:** Stanford connection: the lecture’s WikiChat discussion, pp.17–25, separates finding material from checking factual claims. Apply the habit to a grid study: retrieving a current limit is different from calculating current for a candidate. The displayed 99.604410% value belongs to the separate archived P3 OpenDSS replay, not to the learner’s fresh L2 result. This example supports only that current check under its recorded model. A sentence, retrieved document or citation does not establish full-network feasibility. Treat the input limits as the task policy. A text source describes the rule; the solver evaluates the particular proposal.

**Figure scope:** Example uses the separate saved P3 case.

**Editable figure:** diagrams/lab_claim_evidence.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, pp.17–25; recorded P3 current check.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

## 25. Exercise 1: lower the current allowance

**Timing:** 25:00–29:00 (4 minutes)

**Slide content:** In L2, change RATING_FRACTION from 0.80 to 0.75. Predict, then rerun.
Compare feasible, current use and score J for both methods.
Does this check cover the whole MV/LV network?

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. Keep LOAD_SCALE=1.0. Reference allowed-current use is 78.527895% for MPC and 54.854158% for SAC; both remain feasible. Do not ask learners to find a rejection that this edit does not produce. The default model still covers MV only.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 26. Exercise 1: both still pass

**Timing:** 29:00–30:00 (1 minutes)

**Slide content:** A smaller allowance makes the same current a larger percentage.
At 0.75: MPC uses 78.53%, SAC 54.85%. Both pass this test.

**Teaching notes:** Use this visual immediately after the first exercise debrief. It shows the measured reference MPC outputs, rounded to two decimal places, for RATING_FRACTION 0.80 and 0.75. The SAC result is also computed in the notebook but is not drawn here. Both proposals pass this particular tighter test. The result is not a general guarantee for other loads or limits. Ask pairs to explain the denominator in the percentage. Restore the default before moving to L3’s independent archived case. This combines the original numerical debrief with the visual explanation. Compare both methods before restoring RATING_FRACTION=0.80.

**Figure scope:** Reference L2 experiment. Both proposals pass at 0.75.

**Editable figure:** diagrams/lab_try_observe.tex

**Notebook / source locator:** Classroom Labs L2, cell classroom-007; verified default and exercise outputs.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 27. L2: reset before continuing

**Timing:** 30:00–30:30 (0.5 minutes)

**Slide content:** Restore LOAD_SCALE=1.0 and RATING_FRACTION=0.80. Rerun L2.
L3-L5 use a separate saved case called test_01.

**Teaching notes:** Make the experiment boundary explicit. L3 loads a separate preserved context into pool. It does not inherit the fresh L2 case or the participant's edits. Do not pair an edited L2 result with the test_01 model explanation as though the model had seen those new inputs.

**Exact source excerpt:** Classroom_Labs.ipynb L2 (classroom-007), source lines 1–2.
LOAD_SCALE = 1.0
RATING_FRACTION = 0.80

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 28. New calculations and saved replies

**Timing:** 30:30–31:00 (0.5 minutes)

**Slide content:** Python calculates new results. A saved Llama reply keeps its original inputs.
Your changed lab input does not change the saved reply.

**Teaching notes:** Point to these evidence modes throughout the session. Default classroom cells calculate fresh results without a live language-model call. L10B displays verified historical Llama choices, original reasons and associated recorded results. Changing your L2 or L6 input does not change those old replies. The final control-room diagrams are a proposed teaching design, not evidence of a deployed utility platform. No new equipment operation occurs in any of these modes. FRESH means calculated during the current execution. SAVED POLICY means old weights used for new inference. ARCHIVED ACTUAL LLM means an old reply with its original inputs and timing. This slide comes just before L3 so the distinction is applied immediately.

**Figure scope:** New calculation, saved reply and proposed pilot are different evidence types.

**Editable figure:** diagrams/bridge_modes.tex

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

## 29. L3: inspect saved model choices

**Timing:** 31:00–32:00 (1 minutes)

**Slide content:** Run L3. Read the case ID, chosen operations and recorded times.
This cell displays old replies. It makes no new model call.

**Teaching notes:** The output contains three actual replies from the frozen response-selection study. Ask learners to identify the operation and numerical parameters requested by each reply. The reported seconds measure the original model calls, not today's display cell. Keep this archived context separate from the fresh L2 comparison.

**Exact source excerpt:** Classroom_Labs.ipynb L3 (classroom-010), source lines 1–2.
pool = lab.saved_pool('test_01')
display(pd.DataFrame(pool['responses'])[['model_id', 'operation_id', 'reason', 'seconds', 'source']])

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 30. Different words can request the same trial

**Timing:** 32:00–32:30 (0.5 minutes)

**Slide content:** The notebook groups identical tool requests and settings.
A vote chooses what to test next. It does not prove that limits pass.

**Teaching notes:** The three old replies reduce to two distinct operations after matching their tool names and numerical parameters. The vote keeps one contribution per model. In test_01, two models vote for the Q-relaxation trial, which relaxes a reactive-power restriction in that declared test. This diagram shows the old input and choices; it is not a new vote after a learner edits L2. Grouping matching trials avoids counting different wording as different physical proposals.

**Figure scope:** Three saved replies request two different trials.

**Editable figure:** diagrams/voltage_canonical_trial.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H03] Classroom Labs notebook. Classroom_Labs.ipynb, L3; cell classroom-010; archived test_01 context. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 31. L4: check the selected trial

**Timing:** 32:30–33:30 (1 minutes)

**Slide content:** Run L4 after L3. Python checks the selected trial for its original case.
Compare majority voting with the saved LinUCB selector, which learns which trial to test.

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

## 32. L4: read the new check

**Timing:** 33:30–34:00 (0.5 minutes)

**Slide content:** Both selectors choose the same trial and pass the new MV check.
new_check_passes is the electrical check. Predicted reward is a learned score.

**Teaching notes:** The reference J is about 0.031082 for both selectors. The predicted reward is around -0.0075. It is a learned score, not a feasibility flag. Read new_check_passes for the engineering result. This one case does not show that learned selection is better than voting.

**Figure scope:** Saved choices, new checks of the original test_01 case.

**Figure asset:** images/hands_on_L4_checks.png

**Notebook / source locator:** Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H04] Classroom Labs notebook. Classroom_Labs.ipynb, L4; cell classroom-013; fresh checks of archived choices. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 33. L5: check model coverage

**Timing:** 34:00–35:30 (1.5 minutes)

**Slide content:** Leave RUN_OPENDSS=False. Run L5 and read the table.
The default checks the test_01 MPC plan with the MV model.

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

## 34. A PASS has a scope

**Timing:** 35:30–36:00 (0.5 minutes)

**Slide content:** This result covers medium-voltage (MV) phases and currents.
A full medium- and low-voltage (MV/LV) request needs the wider check or a HOLD.

**Teaching notes:** Ask a participant to read the explicit scope message aloud. A PASS is conditional on the model and action that were checked. The default model does not cover every LV constraint. A more confident explanation cannot supply the missing model coverage.

**Figure scope:** Default L5 checks MV only. OpenDSS is off.

**Figure asset:** images/hands_on_L5_scope.png

**Notebook / source locator:** Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 35. Saved voltage case: check SAC first

**Timing:** 36:00–37:00 (1 minutes)

**Slide content:** Llama asks to check SAC. The tool finds a current-limit failure.

**Teaching notes:** Read the exact reason. The model was offered VERIFY_SAC_FIRST or REVIEW. The application then checks the saved SAC action in OpenDSS. 111.966607% refers to the allowed current, which was 80% of nominal, so this exceeds the configured allowance. The numerical result records two current violations. This P3 full supplied MV/LV study is separate from L2 and L3 test_01. Ask the audience to predict the next allowed step before advancing. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved P3 case, separate from L2. Replay in L10B.

**Figure asset:** images/llama_voltage_1.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 1; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 36. Saved voltage case: try the MPC fallback

**Timing:** 37:00–38:00 (1 minutes)

**Slide content:** Llama requests the existing MPC plan. The electrical tool checks it.

**Teaching notes:** The model selects USE_MPC_PLAN from two allowed choices, the other being REVIEW. It does not invent or solve MPC. The recorded context already supplies a plan and its eligibility. The application performs a fresh numerical check at that historical time. The result is just below the allowed current threshold. No operating permission follows from this check alone. Ask which evidence, rather than wording, makes the fallback eligible for review. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved P3 case, separate from L2. Replay in L10B.

**Figure asset:** images/llama_voltage_2.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 2; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 37. Saved voltage case: return for review

**Timing:** 38:00–39:00 (1 minutes)

**Slide content:** The checks pass. Human review is still pending. A fixed script gets the same final result.

**Teaching notes:** Read the exact REVIEW_EVIDENCE choice and distinguish it from the overall status. The proposed controls are 2387.157 kW and +325.738 kvar. The supplied full MV/LV feeder check returned voltage 1.001783–1.035026 p.u. and zero listed violations. The fixed supervisor used the same SAC-to-MPC sequence with identical numerical output. Recorded workflow intervals were 0.346053 s fixed and 3.110454 s agentic, excluding precomputed MPC/SAC preparation. These are single recorded timings, not performance distributions or a measured reduction in operator workload. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation. End-of-case partner check: L2 makes new proposals; L3 shows old replies; L4–L5 run new checks on test_01. Report the inputs, proposal, model coverage and result before naming the next step. Give pairs 30 seconds to describe the sequence without calling every step an AI decision. L2 calculates an MPC plan and a saved-policy proposal for the current classroom inputs. L3 displays old model replies. L4 runs new checks of the selected trials; L5 checks the original archived plan and its model coverage. Numerical tools provide the physical evidence. The old model choices select a permitted trial; they do not replace these checks. The operator receives an advisory record whose stated coverage must match the request. The three P3 previews are an additional separate archive. Contrast their saved Llama decisions with your current direct function calls.

**Figure scope:** Saved P3 case, separate from L2. Replay in L10B.

**Figure asset:** images/llama_voltage_3.png

**Notebook / source locator:** Classroom Labs L10B: voltage replay, recorded call 3; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 38. Case 2: restoring service

**Timing:** 39:00–39:30 (0.5 minutes)

**Slide content:** Use the six-node teaching network with one faulted branch.
Compare total service with service to critical loads.

**Teaching notes:** This six-node graph is separate from the voltage feeder. It represents active-power transport, not AC power flow or a time-ordered field switching procedure. Loads are picked up as whole blocks. A tie is an alternative connection that can supply load; CAPACITIES_KW sets its transfer limit in kilowatts.

**Figure scope:** Six-node active-power model. One branch is unavailable.

**Editable figure:** diagrams/restoration_fault_map.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 39. Two service goals

**Timing:** 39:30–40:30 (1 minutes)

**Slide content:** One goal gives extra weight to critical loads.
The other restores the most total kW. Both use the same network rules.

**Teaching notes:** Critical demand totals 90 kW: 60 kW at node 2 and 30 kW at node 5. The objective is the service goal encoded as a score. The priority score gives more weight to these critical loads, while the comparison score maximizes total kW. The difference in selected service comes from that goal. Both numerical methods use the same graph, capacities and whole-load pickup rules. Neither needs a language model to solve this declared problem.

**Figure scope:** Different goals can select different loads.

**Editable figure:** diagrams/restoration_priority.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 40. L6: solve the restoration problem

**Timing:** 40:30–42:30 (2 minutes)

**Slide content:** Run L6. MILP selects whole loads. A separate search checks its priority score.
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

## 41. L6: read both service plots

**Timing:** 42:30–43:30 (1 minutes)

**Slide content:** Left: total kW served. Right: critical kW served.
Overlapping markers mean the two goals give the same result.

**Teaching notes:** The markers show sampled capacities rather than a continuous ramp between whole-load pickup plans. A higher capacity may still be too small to add another complete load block. Read both total and critical service before choosing the policy that matches the request.

**Figure scope:** Reference L6 plots. Overlapping markers show equal outcomes.

**Figure asset:** images/hands_on_L6_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 42. L6: the tradeoff at 40 kW

**Timing:** 43:30–44:30 (1 minutes)

**Slide content:** Priority goal: 130 kW total, including 90 kW critical.
Most-total-kW goal: 140 kW total, including 30 kW critical.

**Teaching notes:** Compare the first two output rows, where tie_capacity_kw=40. The priority plan serves 10 kW less total demand while preserving 60 kW more critical demand. These results compare two service objectives, not AI with no AI.

**Figure scope:** Reference L6: 40 kW varied tie, 100 kW fixed tie.

**Figure asset:** images/hands_on_L6_table.png

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 43. Restoration checks

**Timing:** 44:30–45:00 (0.5 minutes)

**Slide content:** Check source paths, branch capacity, power balance and the fault.
A separate search checks the priority score.

**Teaching notes:** Numerical checks and same-content evidence matching answer different questions. A record can match the inputs exactly while still omitting AC voltage, reactive-power or protection limits. Comparing the MILP score with every permitted plan is an independent check of this small stated problem. Minimizing energized branches does not calculate the number or order of physical switching steps.

**Figure scope:** Checks cover this graph model, not AC operation or field switching.

**Editable figure:** diagrams/restoration_verify.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[RSTL01] Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.:** [https://arxiv.org/abs/1912.05185v3](https://arxiv.org/abs/1912.05185v3)

**[RSTL02] Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.:** [https://doi.org/10.1109/TPWRS.2017.2720122](https://doi.org/10.1109/TPWRS.2017.2720122)

## 44. Exercise 2: increase tie capacity

**Timing:** 45:00–49:00 (4 minutes)

**Slide content:** Add 180. to CAPACITIES_KW. Keep 40. first. Predict, then rerun L6.
Compare total and critical kW at 40 and 180 kW.
At which capacity do the two goals give the same result?

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. At 180 kW, both methods serve 250 kW total and 90 kW critical demand. Keep 40 kW first in the list because L7 binds the first result to the first capacity. Do not reorder the list for this exercise.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 45. Exercise 2: enough capacity removes this tradeoff

**Timing:** 49:00–50:00 (1 minutes)

**Slide content:** At 180 kW, both goals serve 250 kW total and 90 kW critical.
The priority goal helps at some limits. It does not improve every case.

**Teaching notes:** Compare the 180 kW result with the 40 kW case before generalizing. Equal service at 180 kW follows from this small graph and its demands; it is not a universal threshold. A single success percentage would hide the service-policy question.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 46. L7: test an old result after a change

**Timing:** 50:00–51:30 (1.5 minutes)

**Slide content:** Restore the original capacity list and rerun L6.
Run L7. It changes the first request from 40 kW to 20 kW.

**Teaching notes:** Keeping 40 kW first already preserves the L7 example. Resetting the list also makes the saved notebook easy to compare with the default. L7 changes the request capacity and revision without solving a new case. It tests whether the old evidence can still be used.

**Exact source excerpt:** Classroom_Labs.ipynb L7 (classroom-021), source lines 1–3.
rest_record = restoration['records'][0]['weighted']
rest_request = {'task': 'restoration', 'capacity_kw': CAPACITIES_KW[0],
                'critical_nodes': [2, 5], 'model': 'six_node_active_transport', 'revision': 1}

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 47. L7: the old evidence no longer matches

**Timing:** 51:30–52:00 (0.5 minutes)

**Slide content:** Original request: True. Changed request: False.
HOLD the old recommendation and request a new solve.

**Teaching notes:** This output reports evidence binding, not physical infeasibility. A separate fresh solve at 20 kW still gives the 130 kW total and 90 kW critical priority outcome on this graph. L7 itself does not run that solve. Replace the stale evidence because it belongs to a different request, even when the old plan might remain feasible.

**Figure scope:** Reference L7. New inputs require new evidence.

**Figure asset:** images/hands_on_L7_binding.png

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 48. New inputs need new evidence

**Timing:** 52:00–52:30 (0.5 minutes)

**Slide content:** An outdated check does not tell us whether the new plan works.
Solve again, check again and attach the new result to the new request.

**Teaching notes:** Evidence binding asks whether a record matches the exact request, proposed plan and returned result. The diagram’s extra topology labels are teaching illustrations. The runnable L7 example changes only the request capacity and revision; students do not change topology in that cell. Old evidence is unusable for a changed request even if the old plan might still pass its limits. Ask which new numerical check would establish that for the changed request.

**Figure scope:** L7 changes capacity and revision, then tests the old evidence.

**Editable figure:** diagrams/restoration_stale.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 49. The agent keeps the service goal

**Timing:** 52:30–53:00 (0.5 minutes)

**Slide content:** L6 runs Python directly. The operator sets priorities; MILP selects loads.
An agent could request the solve and explain its returned tradeoff.

**Teaching notes:** This is a proposed role for an agent, not a new model decision in the default notebook. The current supervisor is ordinary Python. A future language-model agent could request the allowed solve and explain the returned tradeoff. It must preserve the operator’s service goal and limits, rather than quietly changing weights or making up load values. A different service goal requires an explicit new request and solve. The numerical difference here comes from the optimization objective.

**Figure scope:** Proposed agent use. L6 itself runs Python.

**Editable figure:** diagrams/restoration_plan.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 50. Restoration model limits

**Timing:** 53:00–53:30 (0.5 minutes)

**Slide content:** This graph checks active power, not AC voltage or protection.
Selected branches do not specify the order of field switching.

**Teaching notes:** State this boundary clearly and briefly. The result is useful within its declared transport formulation. Actual restoration requires the utility's engineering checks, operating procedure and separate authority.

**Notebook / source locator:** Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 51. Saved restoration case: try another plan

**Timing:** 53:30–54:30 (1 minutes)

**Slide content:** Llama requests a trial that restores more load and passes the current check.

**Teaching notes:** Switch L10B to restoration. This is the separate L10 feeder-catalog restoration study, not the L6 six-node MILP. The recorded protocol requires a first refinement but Llama chooses between the offered fractions. SHED_075 disconnects 75% of the ordered noncritical load objects, not 75% of load kW. The exact reason calls improvement a possibility. Python evaluates the trial and finds improved service while the tie loading remains 91.867215% of its allowance. A useful hypothesis becomes evidence only after that check. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Figure asset:** images/llama_restoration_14.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 14; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 52. Saved restoration case: reject a failed trial

**Timing:** 54:30–55:00 (0.5 minutes)

**Slide content:** The next trial exceeds the current limit. Keep the previous passing plan.

**Teaching notes:** Keep the actual returned reason visible. It refers to a target in the objective, but its claim should not be accepted as a proved fact. In this record the next trial is numerically rejected for a thermal failure. Restoring more load does not make a failed current check acceptable. Ask participants to explain why the previous passed candidate must remain in the case record. The model’s trial budget is bounded. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Figure asset:** images/llama_restoration_15.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 15; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 53. Saved restoration case: correct the ranking

**Timing:** 55:00–56:00 (1 minutes)

**Slide content:** Python corrects the ranking and rechecks the lowest-cost passing plan.

**Teaching notes:** Let pairs answer before discussing the result. Smaller cost is better, so E03 must rank before E02. Llama returns [E02,E03] while its explanation claims lowest score first. The recorded language_order_agrees_with_cost field is False. A deterministic guard retains E03 and rechecks it as E05, with no recorded failures. Human acknowledgment and dispatch remain False. The paired fixed workflow reaches the same final action and cost. This example motivates verification rather than an unsupported superiority claim. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation. End-of-case partner check: At 40 kW, explain 130 total / 90 critical versus 140 total / 30 critical, all in kW. For a changed request, keep HOLD until evidence for the current request is available. Ask each pair to give one number and one condition. They should distinguish three decisions: selecting a service policy, checking current evidence and authorizing a physical switching operation. Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.

**Figure scope:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Figure asset:** images/llama_restoration_16.png

**Notebook / source locator:** Classroom Labs L10B: restoration replay, recorded call 16; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 54. Case 3: suspicious readings

**Timing:** 56:00–56:30 (0.5 minutes)

**Slide content:** Use the separate four-bus DC teaching model.
Compare the fit to readings with error against known simulation truth.

**Teaching notes:** The separate four-bus linear DC model has three unknown voltage angles, measured relative to a reference bus, and eight readings. This DC approximation is not a full AC estimator, malware detector or sensor-authentication system. Synthetic truth is known for the offline classroom comparison only. A residual checks how well the estimate fits the supplied readings; state error checks how far the estimate is from the known teaching truth.

**Figure scope:** Four-bus DC model. Simulation truth is used only for offline comparison.

**Editable figure:** diagrams/cyber_network.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 55. What the residual measures

**Timing:** 56:30–57:30 (1 minutes)

**Slide content:** Weighted least squares (WLS) fits the readings. Residual J measures the mismatch.
The true state is known in this simulation, not in a live control room.

**Teaching notes:** WLS means weighted least squares: find the state that best fits the readings, giving more influence to readings with smaller stated uncertainty. That weighting does not authenticate a reading. Here J is the residual mismatch statistic, not the voltage case’s penalty score. Its chi-square alarm threshold is about 15.086272 for five residual degrees of freedom at a 1% significance level. This calibration depends on the stated linear model and noise assumptions. An operator does not have the synthetic truth used to calculate the plotted state error. A small J does not establish that the readings are authentic.

**Figure scope:** A good fit does not authenticate the readings.

**Editable figure:** diagrams/cyber_residual.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY01] Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.:** [https://doi.org/10.1109/TPAS.1970.292678](https://doi.org/10.1109/TPAS.1970.292678)

## 56. L8: run two data attacks

**Timing:** 57:30–59:30 (2 minutes)

**Slide content:** Run L8 with the default scales.
Compare one biased reading with a coordinated change across readings.

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

## 57. L8: read both cyber plots

**Timing:** 59:30–60:30 (1 minutes)

**Slide content:** Left: mismatch J and the alarm threshold. Right: error against simulation truth.
A quiet alarm can appear alongside a growing state error.

**Teaching notes:** The left plot uses a symmetric-log scale. The right plot compares the estimate with known synthetic truth. As the coordinated shift grows, the residual stays unchanged while the state error increases. These plots answer different questions; they do not express the same quantity in different units.

**Figure scope:** Reference L8 plots. State error uses known simulation truth.

**Figure asset:** images/hands_on_L8_plot.png

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 58. L8: a coordinated attack escapes the alarm

**Timing:** 60:30–61:30 (1 minutes)

**Slide content:** At scale 1, one biased reading gives J=277.50 and an alarm.
The coordinated attack gives J=3.92, no alarm, and 0.02678 rad of state error.

**Teaching notes:** The diagram is a simple scalar illustration of coordinated consistency, not the numerical eight-measurement system. Read the numerical values from L8. A larger false-data shift need not increase the residual when the shift lies in the modeled measurement subspace. The state error is measured in radians; it is available here because this is an offline test with known synthetic truth.

**Figure scope:** Values from the eight-reading L8 model.

**Editable figure:** diagrams/cyber_stealth.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY02] Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.:** [https://doi.org/10.1145/1952982.1952995](https://doi.org/10.1145/1952982.1952995)

## 59. Exercise 3: test a small bias

**Timing:** 61:30–65:30 (4 minutes)

**Slide content:** Add .10 to ATTACK_SCALES. Predict, then rerun L8.
At scale 0.10, compare J, the alarm flag and state error.
Does no alarm mean the data are correct?

**Teaching notes:** Allow one minute to predict, two minutes to edit and run, and one minute to report. For isolated bias at scale 0.10, J is about 10.143237, below the 15.086272 threshold. The alarm is False despite nonzero state error. The coordinated residual stays about 3.920222. This added scale remains within the notebook's plot limits.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 60. Exercise 3: a small bias can miss the threshold

**Timing:** 65:30–66:30 (1 minutes)

**Slide content:** At scale 0.10, J is about 10.14, below the 15.09 alarm threshold.
A quiet alarm alone cannot prove that readings are true.

**Teaching notes:** Separate the two mechanisms. A small isolated bias can stay below a statistical threshold. A coordinated Hc shift can preserve residual consistency by construction. Neither result establishes trusted telemetry. The state-error curve uses offline synthetic truth, not an input available to an online detector.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 61. L8: reset before recovery

**Timing:** 66:30–67:00 (0.5 minutes)

**Slide content:** Restore the original attack scales and rerun L8.
L9 uses a separate fixed recovery case.

**Teaching notes:** Explain the boundary before comparing the recovery output. Changing ATTACK_SCALES changes the residual and state-error sweep. It does not change the fixed recovery scenario held inside the demo object.

**Exact source excerpt:** Classroom_Labs.ipynb L8 (classroom-023), source lines 1–3.
ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 62. L9: one fixed recovery case

**Timing:** 67:00–67:30 (0.5 minutes)

**Slide content:** Compare the same case with and without readings assumed to be trusted.
Your L8 scale change does not change this case.

**Teaching notes:** The helper uses the fixed run_wls_demo recovery fixture. The cyber object holds both the sweep results and this shared fixed demo. The comparison tests the trust premise under controlled conditions; it is not a controller reacting continuously to each plotted scale.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 63. Data trust is an assumption

**Timing:** 67:30–68:00 (0.5 minutes)

**Slide content:** This example assumes three extra angle readings are trustworthy.
Neither WLS nor Llama authenticates them.

**Teaching notes:** The example assumes three protected angle readings determine the three unknown angles, leaving zero residual degrees of freedom. Independent trusted information must come from a justified source outside this numerical calculation. A zero residual in this exactly determined system adds no detection guarantee. Neither a good model fit nor a language-model explanation establishes authenticity.

**Figure scope:** Three extra angle readings are assumed trustworthy.

**Editable figure:** diagrams/cyber_trusted.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 64. L9: HOLD or PROPOSE

**Timing:** 68:00–69:30 (1.5 minutes)

**Slide content:** Run all of L9. Read status first.
Then read the proposed injection and the offline violation count.

**Teaching notes:** The two calls use the same fixed fixture and change only protected_available. Without the trusted channels, the result is HOLD. With the assumed trusted set, it is PROPOSE. A proposal is neither an acknowledgment nor a dispatch command.

**Exact source excerpt:** Classroom_Labs.ipynb L9 (classroom-026), source lines 1–2.
without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 65. L9: two outcomes

**Timing:** 69:30–70:30 (1 minutes)

**Slide content:** Without trusted replacement readings: HOLD.
With assumed trusted readings: PROPOSE, u about 0.121694 p.u., zero offline model violations.

**Teaching notes:** Read the condition column together with the returned state. The PROPOSE outcome depends on the supplied trust assumption and fixed model. The recovery record keeps dispatch=False. It does not use the equipment_dispatch field from the separate L12 readback example.

**Figure scope:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Figure asset:** images/hands_on_L9_trust.png

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 66. L9: check the correction

**Timing:** 70:30–71:00 (0.5 minutes)

**Slide content:** A quadratic-program (QP) solver finds the smallest allowed injection that meets the branch limits.
One flow: predicted 0.17000 p.u., offline actual 0.17046 p.u., limit 0.18000 p.u.

**Teaching notes:** QP means quadratic programming: this numerical solver minimizes a quadratic effort score while enforcing the declared branch limits and a 0.01 p.u. margin. The flexible injection is u=0.1216936673 p.u., balanced by the reference bus. Predicted flow12 is 0.17000 p.u.; the offline actual flow is about 0.17046 p.u., below the 0.18000 p.u. rating. The actual-flow comparison uses synthetic truth for this fixed case. It does not guarantee AC behavior omitted by the model or trustworthy field telemetry.

**Figure scope:** Fixed L9 correction: compare the predicted branch flow with the offline truth check.

**Editable figure:** diagrams/cyber_qp.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 67. A proposal depends on its assumptions

**Timing:** 71:00–71:30 (0.5 minutes)

**Slide content:** Assumed trusted data support the estimate. The solver calculates a correction.
The operator still reviews data trust, model coverage and missing checks.

**Teaching notes:** Do not attribute recovered information or numerical feasibility to confident prose. The workflow can coordinate the estimator, constrained correction and evidence checks. It cannot invent an independent trusted measurement source.

**Figure scope:** A numerical proposal still needs human review.

**Editable figure:** diagrams/cyber_handoff.tex

**Notebook / source locator:** Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 68. Saved cyber case: request the allowed tool

**Timing:** 71:30–72:00 (0.5 minutes)

**Slide content:** Llama selects the supplied recovery tool. Python calculates the correction.

**Teaching notes:** Switch L10B to cyber. This standard four-bus DC record is separate from L10’s proposal-complete cyber record, and matches the Agent Trace notebook T6 archive. The route is narrow: the prompt already authorizes the tool and supplies the trusted-sensor assumption. The three angle readings give full rank but zero residual redundancy, so a good fit is not an independent trust test. u is the flexible injection correction in per unit. Offline synthetic-truth flow is available to the experimenter, not guaranteed available to a real operator. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation.

**Figure scope:** Saved four-bus study. Replay in L10B.

**Figure asset:** images/llama_cyber_7.png

**Notebook / source locator:** Classroom Labs L10B: cyber replay, recorded call 7; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 69. Saved cyber case: keep human review

**Timing:** 72:00–73:00 (1 minutes)

**Slide content:** The model check passes. The operator must still review trust and missing checks.

**Teaching notes:** Read the actual reply, including the REVIEW choice. Numerical verification is PASS, but the overall result remains REVIEW and human acknowledgment is PENDING. The fixed comparator obtains the same numerical state estimate and correction without Llama. This replay demonstrates permitted tool routing and a report decision. It does not demonstrate better estimation, authenticated measurements, AC network security or operating authority. Run L11 with the default False setting, then proceed to L12. This slide is a recorded preview beside the matching case. Do not run ahead to L10B yet. Keep the named L2–L9 cells in order; after L10, use L10B to inspect all three complete episodes. The source label locates the replay rather than the current classroom calculation. End-of-case partner check: Report the trust assumption, model, proposed u and the checks that passed or failed. Without independent trusted information, keep HOLD and name what is missing. Ask pairs to state the outcome and its condition in the same sentence. For example: 'The fixture proposes u when the supplied trusted channels are available.' Do not say: 'The AI proved that the telemetry is safe.' Ask which step was chosen by Llama in the recorded example, which returned result came from software, and what the operator must review. These previews use a separate archived case; L10B later displays the full source.

**Figure scope:** Saved four-bus study. Replay in L10B.

**Figure asset:** images/llama_cyber_8.png

**Notebook / source locator:** Classroom Labs L10B: cyber replay, recorded call 8; full record in source guide.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 70. L10: inspect the five-role workflow

**Timing:** 73:00–74:30 (1.5 minutes)

**Slide content:** Run L10 to see every recorded stage and result.
The stages share case facts, proposals and check results. The next slides explain their jobs.

**Teaching notes:** L10 reads the archived proposal_complete_workflow study. It includes feeder-catalog restoration and is separate from the L6 six-node MILP and your edited classroom inputs. L10B, inserted immediately after L10, then gives readable verified replay episodes for all three cases. Run L11 after those replays; the default False setting skips a new local model request.

**Notebook / source locator:** Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 71. L10B: replay the three Llama examples

**Timing:** 74:30–79:00 (4.5 minutes)

**Slide content:** Set SCENARIO to voltage, restoration and cyber. Rerun for each.
These are saved replies and tool results. No new Llama call runs here.

**Teaching notes:** Run L10 first. In the new L10B cell the helper validates the original JSON reply against the parsed journal and trace, then displays the recorded episode. Change only SCENARIO to inspect the other two episodes. Earlier case slides previewed selected fields from these replays. Now inspect the full episodes in the same notebook. This cell makes no model request and performs no new electrical solve. At the end, run L11 at its default False setting before L12. Llama reasons are historical public returned text. Their correctness must be judged against the input and tool results. SCENARIO can be voltage, restoration or cyber. The full cell is shown. Allow about a minute and a half per scenario: one partner identifies the model choice, the other finds its tool result and the unresolved operator decision. These additional minutes replace removed checkpoint slides and the longer source explanations.

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

## 72. L12: practice operator readback

**Timing:** 79:00–81:00 (2 minutes)

**Slide content:** Leave L11 disabled, then run L12.
Check the wrong ID, the matching ID and equipment_dispatch=False.

**Teaching notes:** This cell returns to the original test_01 voltage result through selected_trials. It does not use the restoration or cyber sweeps. Read both scope outcomes and explain why the full MV/LV request remains HOLD. The new simulated acknowledgment grants no physical operating authority and does not complete the review of an old record. Readback means repeating the recommendation ID and conditions so the acknowledgment can be matched to the same proposal. In this exercise it is simulated. Check the wrong-ID rejection, the correct simulated acknowledgment and equipment_dispatch=False.

**Exact source excerpt:** Classroom_Labs.ipynb L12 (classroom-033), source lines 9–10.
wrong_id = lab.acknowledge(mv_scope, 'wrong-id', 'Student operator')
readback = lab.acknowledge(mv_scope, mv_scope['recommendation_id'], 'Student operator')

**Source alignment:** This excerpt is selected by stable cell ID from the canonical sibling notebook, not the preserved historical notebook. research/code_manifest.json records the notebook SHA-256, cell ID, current index and inclusive source-line range. research/code/ contains the unchanged selected lines.

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 73. L12: approval must match the checked scope

**Timing:** 81:00–82:00 (1 minutes)

**Slide content:** Full MV/LV request: HOLD. The MV teaching request allows a simulated readback.
A wrong ID fails. This exercise never sends equipment commands.

**Teaching notes:** After running the complete L12 cell, compare these reference outputs with your own. The full MV/LV request remains HOLD because the checked model covers only MV phases. An explicit MV teaching request can pass the simulated readback after the recommendation ID matches. The wrong-ID attempt is rejected. Acknowledgment records a classroom review step and does not operate equipment.

**Figure scope:** Reference L12 output. Readback is simulated.

**Figure asset:** images/hands_on_L12_packet.png

**Notebook / source locator:** Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only.

**Open the notebook:** [https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 74. Our multi-agent design: five roles

**Timing:** 82:00–83:30 (1.5 minutes)

**Slide content:** The roles pass structured results to each other. Llama handles planning and refinement; Python runs the other stages.

**Teaching notes:** This is a custom, role-based Python workflow. It is not five independent LLMs. One Llama 3.1:8b model is called with the Planning Agent and LLM Optimizer roles. Awareness, simulation and verification run Python. The default notebook displays saved role traces in L10 and saved selected episodes in L10B; it does not execute a new multi-agent LLM run. The handoff is structured case facts, candidate IDs, tool results and checks, not an invented agent conversation. src/proposal_workflow.py defines CORE_STAGES, run_proposal_case, evaluate and the ranking guard. A final independent recheck precedes MODEL_RECOMMEND. Human acknowledgment remains separate and pending. Hash checks detect changed records but do not authenticate telemetry.

**Figure scope:** Custom Python workflow, one Llama model in two roles. L10 displays its saved trace.

**Editable figure:** diagrams/multi_agent_roles.tex

**Notebook / source locator:** Five-role implementation: src/proposal_workflow.py; recorded results: proposal_complete_workflow.json.

**[WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

## 75. Five roles in the voltage case

**Timing:** 83:30–84:30 (1 minutes)

**Slide content:** Llama asks for less reactive power, then more solar output. Python checks each new trial.

**Teaching notes:** This is a custom, role-based Python workflow. It is not five independent LLMs. One Llama 3.1:8b model is called with the Planning Agent and LLM Optimizer roles. Awareness, simulation and verification run Python. The default notebook displays saved role traces in L10 and saved selected episodes in L10B; it does not execute a new multi-agent LLM run. The handoff is structured case facts, candidate IDs, tool results and checks, not an invented agent conversation. src/proposal_workflow.py defines CORE_STAGES, run_proposal_case, evaluate and the ranking guard. A final independent recheck precedes MODEL_RECOMMEND. Human acknowledgment remains separate and pending. Hash checks detect changed records but do not authenticate telemetry. In this L10 lindistflow3 record, the optimizer asks for RELAX_Q_10_PERCENT then INCREASE_PV_0025. Python recalculates each proposal and the verification stage checks it. The selected final recheck uses a=0.3394386941 and b=0.0276310594, with 50.75344954 percent allowed-current use and no recorded violations. The scope is MV phases only with ideal LV aggregation. Do not substitute the P3 99.604410 percent result or L2 MPC score. These are different experiments.

**Figure scope:** L10 MV voltage archive, separate from L2 and the P3 replay in L10B.

**Editable figure:** diagrams/multi_agent_voltage.tex

**Notebook / source locator:** Five-role implementation: src/proposal_workflow.py; recorded results: proposal_complete_workflow.json.

**[WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 76. Five roles in the restoration case

**Timing:** 84:30–85:30 (1 minutes)

**Slide content:** The goal stays fixed. A failed trial cannot enter the final ranking, and Python corrects a wrong cost order.

**Teaching notes:** This is a custom, role-based Python workflow. It is not five independent LLMs. One Llama 3.1:8b model is called with the Planning Agent and LLM Optimizer roles. Awareness, simulation and verification run Python. The default notebook displays saved role traces in L10 and saved selected episodes in L10B; it does not execute a new multi-agent LLM run. The handoff is structured case facts, candidate IDs, tool results and checks, not an invented agent conversation. src/proposal_workflow.py defines CORE_STAGES, run_proposal_case, evaluate and the ranking guard. A final independent recheck precedes MODEL_RECOMMEND. Human acknowledgment remains separate and pending. Hash checks detect changed records but do not authenticate telemetry. The L10 lindistflow3 restoration record uses a feeder bypass catalog. SHED_075 returns 1843.61355 kW served and 474.03975 critical kW at 91.86721465 percent allowed-current use. SHED_065 then fails at 111.009413 percent. Llama ranks E02 before E03 even though E03 has the smaller cost. The numerical guard selects E03, then records the final recheck as E05. Switching sequence and broader physical operation are not established.

**Figure scope:** L10 feeder catalog, separate from the six-node L6 exercise.

**Editable figure:** diagrams/multi_agent_restoration.tex

**Notebook / source locator:** Five-role implementation: src/proposal_workflow.py; recorded results: proposal_complete_workflow.json.

**[WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

## 77. Five roles in the cyber case

**Timing:** 85:30–86:30 (1 minutes)

**Slide content:** The workflow keeps the trust assumption visible. It cannot create trusted data from a convincing answer.

**Teaching notes:** This is a custom, role-based Python workflow. It is not five independent LLMs. One Llama 3.1:8b model is called with the Planning Agent and LLM Optimizer roles. Awareness, simulation and verification run Python. The default notebook displays saved role traces in L10 and saved selected episodes in L10B; it does not execute a new multi-agent LLM run. The handoff is structured case facts, candidate IDs, tool results and checks, not an invented agent conversation. src/proposal_workflow.py defines CORE_STAGES, run_proposal_case, evaluate and the ranking guard. A final independent recheck precedes MODEL_RECOMMEND. Human acknowledgment remains separate and pending. Hash checks detect changed records but do not authenticate telemetry. Awareness preserves the declared measurement-trust condition. Planning requests the initial candidates; Python runs the estimator and constrained-response tools. The optimizer requests EXTRA_MARGIN_001 and TRUSTED_QP. The selected final recheck uses TRUSTED_QP with u=0.1216936673 per unit and predicted flow12=0.17 per unit against a 0.18 limit. The model checks a four-bus DC fixture with three protected angles assumed trustworthy. No stage authenticates those channels, and offline truth is not fed to Llama.

**Figure scope:** L10 four-bus DC cyber_stealth archive. Trusted channels are assumed.

**Editable figure:** diagrams/multi_agent_cyber.tex

**Notebook / source locator:** Five-role implementation: src/proposal_workflow.py; recorded results: proposal_complete_workflow.json.

**[WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 78. The operator reviews one evidence packet

**Timing:** 86:30–87:30 (1 minutes)

**Slide content:** Review the inputs, proposal, worst margins and missing checks.
Request another study, reject the proposal or accept it for the next authorized step.

**Teaching notes:** Proposed control-room use. The operator reviews the case snapshot, data quality, limits, selected proposal and missing studies. Ask for another study, reject it or accept it for a defined next step. L12 practices ID-bound readback only and never operates equipment.

**Figure scope:** Proposed control-room use. Study review does not operate equipment.

**Editable figure:** diagrams/ops_review.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**[EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

## 79. What the evidence shows

**Timing:** 87:30–88:30 (1 minutes)

**Slide content:** In L10, five paired final costs tied; one Llama route was worse.
Start with past cases and read-only use. Measure benefit against the same tools in a fixed script.

**Teaching notes:** The six matched fixed-versus-Llama runs in proposal_complete_workflow.json have five tied final costs and one worse Llama voltage result. Recorded model calls add elapsed time. This demonstrates traceable coordination, not better power-flow solvers or general efficiency. Test any proposed benefit against the same tools and budgets. A control-room pilot starts with archived cases, then read-only shadow studies and a limited reviewed scope.

**Figure scope:** L10 comparison: same tools and trial budgets. No general performance gain is established.

**Editable figure:** diagrams/ops_pilot.tex

**Notebook / source locator:** Teaching proposal informed by NIST OT guidance and the cited notebook checks.

**[WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

## 80. Questions and your next lab run

**Timing:** 88:30–90:00 (1.5 minutes)

**Slide content:** Choose one case. Change one input, rerun and save the result.
Explain the agent choice, tool result, check and operator decision.

**Teaching notes:** Close by connecting the full loop: a goal, an allowed agent choice, a tool result, a check and a human decision. Ask each learner to name one case and one changed input they can repeat after the session. Save the notebook. Use the source guide for complete references, not as another required activity.

**Figure scope:** Keep the saved replies separate from your new experiment.

**Editable figure:** diagrams/lab_one_notebook.tex

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

## [ST01] CS224V Agentic AI, Lecture 1: Introduction

**Authors / issuer:** Monica Lam

**Publisher / venue:** Stanford University

**Date:** Fall 2026

**Type:** University lecture slides, supplied by the presenter

**Full source URL:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**Publication:** [https://web.stanford.edu/class/cs224v/](https://web.stanford.edu/class/cs224v/)

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

## [H06] Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [H09] Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture

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

## [LRV] Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 27 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/workshop_run_opendss.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/workshop_run_opendss.json)

## [OT01] Guide to Operational Technology (OT) Security

**Authors / issuer:** Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson

**Publisher / venue:** National Institute of Standards and Technology, NIST SP 800-82 Revision 3

**Date:** September 2023 (final)

**Type:** Published OT security guidance

**Full source URL:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**Full paper PDF:** [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)

**Publication:** [https://csrc.nist.gov/pubs/sp/800/82/r3/final](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

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

## [LRR] Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 27 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json)

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

## [LRC] Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8

**Authors / issuer:** Workshop recorded model replies and numerical study records

**Publisher / venue:** Public teaching archive

**Date:** 21 September 2026

**Type:** Recorded Llama reply and engineering result

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_agent_workflow.json)

## [H10] Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## [OLL1] Structured Outputs: generating structured JSON with a schema

**Authors / issuer:** Ollama documentation maintainers

**Publisher / venue:** Official Ollama documentation

**Date:** Reviewed 24 October 2026

**Type:** Official API documentation

**Full source URL:** [https://docs.ollama.com/capabilities/structured-outputs](https://docs.ollama.com/capabilities/structured-outputs)

## [WF01] Five-role operator study workflow: implementation and recorded cases

**Authors / issuer:** Alaa Selim and Mohamed Chehada

**Publisher / venue:** GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive

**Date:** Implementation inspected 25 October 2026; records dated 27 September 2026

**Type:** Executable teaching implementation and recorded evidence

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_case_tools.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_case_tools.py)

**Publication:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json)

## [EVAL01] Artificial Intelligence Risk Management Framework (AI RMF 1.0)

**Authors / issuer:** National Institute of Standards and Technology

**Publisher / venue:** NIST AI 100-1

**Date:** 26 January 2023

**Type:** Voluntary risk-management guidance

**Full source URL:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

**Full paper PDF:** [https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

## Visual credit: stanford_agentic_capabilities.png

**Caption:** Source figure, p.2. Function calling and a multi-step workflow.

**Credit:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.

**Used on:** 3. A tool call and an agent workflow

**Asset type:** Original Stanford lecture figure excerpt

**Transformation:** Unchanged vector selection from the presenter-supplied Stanford lecture, p.2; Poppler PNG rendering. Exact crop and source/image hashes: research/stanford_sources/excerpt_manifest.json.

**Provenance note:** Cropped from the supplied Stanford lecture PDF. Original author and page retained in the caption and full source guide.

**Evidence limit:** Source figure, p.2. Function calling and a multi-step workflow.

**Original source / page:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=2](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=2)

**Original figure / image URL:** [research/evidence/replots/stanford_agentic_capabilities.png](research/evidence/replots/stanford_agentic_capabilities.png)

## Visual credit: stanford_wikichat_steps.png

**Caption:** Source figure, p.19. WikiChat checks claims before writing.

**Credit:** Monica Lam, Stanford University, CS224V Lecture 1: Introduction, Fall 2026.

**Used on:** 4. Evidence before an answer

**Asset type:** Original lecture figure excerpt

**Transformation:** Cropped vector excerpt from the user-supplied lecture PDF, p.19; selected content unchanged. PNG derived with Poppler. Full provenance: research/stanford_80/excerpt_manifest.json.

**Provenance note:** Cropped from the supplied Stanford lecture PDF. Original author and page retained in the caption and full source guide.

**Evidence limit:** Source figure, p.19. WikiChat checks claims before writing.

**Original source / page:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=19](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=19)

**Original figure / image URL:** [research/evidence/replots/stanford_wikichat_steps.png](research/evidence/replots/stanford_wikichat_steps.png)

## Visual credit: stanford_genie_specification.png

**Caption:** Source figure, p.40. Task rules define permitted tool use.

**Credit:** Monica Lam, Stanford University, CS224V Lecture 1: Introduction, Fall 2026.

**Used on:** 6. Clear rules for tool use

**Asset type:** Original lecture figure excerpt

**Transformation:** Cropped vector excerpt from the user-supplied lecture PDF, p.40; selected content unchanged. PNG derived with Poppler. Full provenance: research/stanford_80/excerpt_manifest.json.

**Provenance note:** Cropped from the supplied Stanford lecture PDF. Original author and page retained in the caption and full source guide.

**Evidence limit:** Source figure, p.40. Task rules define permitted tool use.

**Original source / page:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=40](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=40)

**Original figure / image URL:** [research/evidence/replots/stanford_genie_specification.png](research/evidence/replots/stanford_genie_specification.png)

## Visual credit: stanford_language_decision.png

**Caption:** Source figure, p.53. Clinical example using logical constraints, not a power-system model.

**Credit:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53.

**Used on:** 8. Language and decision checks

**Asset type:** Original Stanford lecture figure excerpt

**Transformation:** Unchanged vector selection from the presenter-supplied Stanford lecture, p.53; Poppler PNG rendering. Exact crop and source/image hashes: research/stanford_sources/excerpt_manifest.json.

**Provenance note:** Cropped from the supplied Stanford lecture PDF. Original author and page retained in the caption and full source guide.

**Evidence limit:** Source figure, p.53. Clinical example using logical constraints, not a power-system model.

**Original source / page:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=53](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=53)

**Original figure / image URL:** [research/evidence/replots/stanford_language_decision.png](research/evidence/replots/stanford_language_decision.png)

## Visual credit: hands_on_L1_binding.png

**Caption:** Reference L1 output. Only the unchanged request and command match.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 15. L1: does the result match the request?

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L1 output. Only the unchanged request and command match.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L1_binding.png](research/evidence/replots/hands_on_L1_binding.png)

## Visual credit: feeder.png

**Caption:** Synthetic SMART-DS feeder used for teaching.

**Credit:** Existing GridGuard workshop numerical figure

**Used on:** 16. Case 1: voltage support

**Asset type:** Synthetic feeder visualization

**Transformation:** Unchanged original plot.

**Evidence limit:** Synthetic SMART-DS feeder used for teaching.

**Original source / page:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

**Original figure / image URL:** [research/evidence/replots/feeder.png](research/evidence/replots/feeder.png)

## Visual credit: hands_on_L2_plot.png

**Caption:** Reference L2 plots. Rerun for your inputs.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 22. L2: voltage and current plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L2 plots. Rerun for your inputs.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_plot.png](research/evidence/replots/hands_on_L2_plot.png)

## Visual credit: hands_on_L2_table.png

**Caption:** Reference L2: load scale 1.0, current allowance 0.80.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 23. L2: both default proposals pass

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L2: load scale 1.0, current allowance 0.80.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_table.png](research/evidence/replots/hands_on_L2_table.png)

## Visual credit: hands_on_L4_checks.png

**Caption:** Saved choices, new checks of the original test_01 case.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 32. L4: read the new check

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Saved choices, new checks of the original test_01 case.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L4_checks.png](research/evidence/replots/hands_on_L4_checks.png)

## Visual credit: hands_on_L5_scope.png

**Caption:** Default L5 checks MV only. OpenDSS is off.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 34. A PASS has a scope

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Default L5 checks MV only. OpenDSS is off.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L5_scope.png](research/evidence/replots/hands_on_L5_scope.png)

## Visual credit: llama_voltage_1.png

**Caption:** Saved P3 case, separate from L2. Replay in L10B.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 35. Saved voltage case: check SAC first

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved P3 case, separate from L2. Replay in L10B.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_1.png](research/evidence/replots/llama_voltage_1.png)

## Visual credit: llama_voltage_2.png

**Caption:** Saved P3 case, separate from L2. Replay in L10B.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 36. Saved voltage case: try the MPC fallback

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved P3 case, separate from L2. Replay in L10B.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_2.png](research/evidence/replots/llama_voltage_2.png)

## Visual credit: llama_voltage_3.png

**Caption:** Saved P3 case, separate from L2. Replay in L10B.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 37. Saved voltage case: return for review

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved P3 case, separate from L2. Replay in L10B.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_3.png](research/evidence/replots/llama_voltage_3.png)

## Visual credit: hands_on_L6_plot.png

**Caption:** Reference L6 plots. Overlapping markers show equal outcomes.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 41. L6: read both service plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L6 plots. Overlapping markers show equal outcomes.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_plot.png](research/evidence/replots/hands_on_L6_plot.png)

## Visual credit: hands_on_L6_table.png

**Caption:** Reference L6: 40 kW varied tie, 100 kW fixed tie.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 42. L6: the tradeoff at 40 kW

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L6: 40 kW varied tie, 100 kW fixed tie.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_table.png](research/evidence/replots/hands_on_L6_table.png)

## Visual credit: hands_on_L7_binding.png

**Caption:** Reference L7. New inputs require new evidence.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 47. L7: the old evidence no longer matches

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L7. New inputs require new evidence.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L7_binding.png](research/evidence/replots/hands_on_L7_binding.png)

## Visual credit: llama_restoration_14.png

**Caption:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 51. Saved restoration case: try another plan

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_14.png](research/evidence/replots/llama_restoration_14.png)

## Visual credit: llama_restoration_15.png

**Caption:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 52. Saved restoration case: reject a failed trial

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_15.png](research/evidence/replots/llama_restoration_15.png)

## Visual credit: llama_restoration_16.png

**Caption:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 53. Saved restoration case: correct the ranking

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved feeder-catalog study, separate from L6. Replay in L10B.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_16.png](research/evidence/replots/llama_restoration_16.png)

## Visual credit: hands_on_L8_plot.png

**Caption:** Reference L8 plots. State error uses known simulation truth.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 57. L8: read both cyber plots

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L8 plots. State error uses known simulation truth.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L8_plot.png](research/evidence/replots/hands_on_L8_plot.png)

## Visual credit: hands_on_L9_trust.png

**Caption:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 65. L9: two outcomes

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L9 output for the fixed recovery case, not the edited L8 scale.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L9_trust.png](research/evidence/replots/hands_on_L9_trust.png)

## Visual credit: llama_cyber_7.png

**Caption:** Saved four-bus study. Replay in L10B.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 68. Saved cyber case: request the allowed tool

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved four-bus study. Replay in L10B.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_cyber_7.png](research/evidence/replots/llama_cyber_7.png)

## Visual credit: llama_cyber_8.png

**Caption:** Saved four-bus study. Replay in L10B.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 69. Saved cyber case: keep human review

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Saved four-bus study. Replay in L10B.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_cyber_8.png](research/evidence/replots/llama_cyber_8.png)

## Visual credit: hands_on_L12_packet.png

**Caption:** Reference L12 output. Readback is simulated.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 73. L12: approval must match the checked scope

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Reference L12 output. Readback is simulated.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L12_packet.png](research/evidence/replots/hands_on_L12_packet.png)
