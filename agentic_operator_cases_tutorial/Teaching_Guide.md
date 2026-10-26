# Teaching and Source Guide

Hands-on: Three Operator Cases — notebook-aligned tutorial. Evidence reviewed 24 October 2026. The full reading guide is separate from the timed main talk. Corporate issuers are listed when no individual author is recorded. Original figures, page locations and image-source credits are included. Attribution alone is not a blanket reuse license.

## Using the case and source guide

**Format:** 50 self-contained concept slides and three what-if discussions. No software or account is required.

**Learning route:** Understand the problem, change one condition, follow the agent request and numerical result, then identify the operator decision.

**Evidence:** Numerical figures are prepared results. Recorded language-model replies retain their own case inputs and scope. A different recorded study is explicitly labeled. These examples do not demonstrate field deployment or general performance gains.

**Practice afterward:** The participant lab guide and notebooks are separate optional practice material. Their setup and cell labels are not needed to understand this presentation.

**Credits:** External Stanford material retains its credits. Full source and calculation provenance are collected here; the authors’ own case slides have no source footer.

## 1. Agentic AI: Three Operator Cases

**Timing:** 00:00–01:00 (1 minutes)

**Slide content:** Understand the problem, follow the agent and review the evidence.
90 minutes / three what-if discussions

**Teaching notes:** The examples are self-contained. No computer or software setup is needed. We will follow a goal, the agent’s requests, numerical evidence and a human decision. The results come from reduced or synthetic studies; they are examples for learning.

**[H00] Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md)

**[B01] IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.:** [https://www.comsoc.org/about/brand-experience/resources](https://www.comsoc.org/about/brand-experience/resources)

## 2. An agent chooses what to try next

**Timing:** 01:00–02:00 (1 minutes)

**Slide content:** Give the agent a goal. It requests a tool, reads the result and chooses the next step.

**Teaching notes:** The agent does not calculate the electrical result by writing a confident answer. It chooses a permitted tool, reads the result and decides whether another request or human review is needed. Trace the feedback arrow once with the audience.

**Figure scope:** Teaching diagram: the model requests a tool and uses the returned evidence.

**Editable figure:** diagrams/plain_agent_loop.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 3. The agent asks; the tool calculates

**Timing:** 02:00–02:30 (0.5 minutes)

**Slide content:** A tool does one job. An agent can connect several jobs using their results.

**Teaching notes:** The Stanford figure distinguishes one function call from a longer agentic workflow. A function can perform one calculation. An agentic workflow connects requests and uses returned results to decide what comes next.

**Figure scope:** Original Stanford figure: one function call and a multi-step workflow.

**Figure asset:** images/stanford_agentic_capabilities.png

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[DEF03] Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.:** [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 4. Solar settings: which option should we try?

**Timing:** 02:30–03:00 (0.5 minutes)

**Slide content:** Compare possible settings, then check voltage and line current.
The agent can organize these trials and report the checked options.

**Teaching notes:** Suppose an operator needs new solar settings. Different settings affect voltage, current and useful solar output. The agent organizes a bounded study; the numerical tool supplies the engineering evidence.

**Figure scope:** The tool calculates; the agent coordinates the next request.

**Editable figure:** diagrams/stanford_colab_voltage.tex

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST02] Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.:** [https://aclanthology.org/2023.findings-emnlp.157/](https://aclanthology.org/2023.findings-emnlp.157/)

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 5. Give the agent a goal and clear limits

**Timing:** 03:00–04:00 (1 minutes)

**Slide content:** State the goal, allowed tools and stopping rules.
Keep the operator’s review step explicit.

**Teaching notes:** A useful request states the operating goal, available tools and stopping conditions. The agent needs to know when it must ask for review rather than continue trying options. The operator defines these boundaries.

**Figure scope:** Grid teaching adaptation of Stanford’s task-specification concept.

**Editable figure:** diagrams/plain_rules.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.40.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST03] Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.:** [https://aclanthology.org/2025.acl-long.1323/](https://aclanthology.org/2025.acl-long.1323/)

**[H01] Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 6. Restoration: who should get power first?

**Timing:** 04:00–04:30 (0.5 minutes)

**Slide content:** The operator sets the service priority.
That priority changes the study the agent requests.

**Teaching notes:** When supply is limited, restoring the greatest total power can differ from protecting essential services. The operator chooses that priority. The agent must preserve it when requesting and comparing studies.

**Figure scope:** Same network and limits, different service goals.

**Editable figure:** diagrams/stanford_colab_restoration.tex

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[ST03] Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.:** [https://aclanthology.org/2025.acl-long.1323/](https://aclanthology.org/2025.acl-long.1323/)

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 7. Keep three jobs clear

**Timing:** 04:30–05:00 (0.5 minutes)

**Slide content:** The agent requests a study. The tool calculates. The operator reviews the result.

**Teaching notes:** Keep the jobs separate. The agent coordinates requests. The numerical tool calculates. The operator reviews the evidence and decides the next authorized step. A tool passing its checks is not operating permission.

**Figure scope:** Adapted principle: language, calculation and human review have different jobs.

**Editable figure:** diagrams/plain_three_jobs.tex

**Notebook / source locator:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.53.

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 8. Wrong readings can still fit a model

**Timing:** 05:00–05:30 (0.5 minutes)

**Slide content:** A good fit alone does not prove that the readings are true.
The agent can organize checks and flag missing evidence.

**Teaching notes:** Readings may fit a model and still be wrong. An alarm test measures one kind of mismatch. The agent can request additional checks and identify missing information, but its explanation cannot make a data source trustworthy.

**Figure scope:** Model fit and trusted information answer different questions.

**Editable figure:** diagrams/stanford_colab_cyber.tex

**[ST01] Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf)

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 9. Case 1: which solar settings should we use?

**Timing:** 05:30–07:30 (2.0 minutes)

**Slide content:** Use solar generation while keeping voltage and line current within the allowed range.
An agent can organize the trials and return checked options.

**Teaching notes:** Start with the physical problem: choose solar controls that respect voltage, current and equipment capacity while serving the stated generation goal. The agent can organize trials and return a checked option. It does not replace the solver or the operator.

**Figure scope:** Concept sketch: choose settings, then calculate their effects.

**Editable figure:** diagrams/plain_voltage_problem.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VCASE] Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.:** [https://data.openei.org/submissions/2981](https://data.openei.org/submissions/2981)

## 10. Two tools suggest different settings

**Timing:** 07:30–08:30 (1 minutes)

**Slide content:** MPC plans with a model. SAC uses a previously trained controller.
Treat both outputs as proposals that need the same electrical checks.

**Teaching notes:** MPC means model predictive control: it plans with a model. SAC means soft actor-critic: it uses a previously trained policy. Both produce proposals. Apply the same electrical checks to each before comparing cost or usefulness.

**Figure scope:** MPC: model predictive control. SAC: soft actor-critic. Both proposals need the same checks.

**Editable figure:** diagrams/plain_two_proposals.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

**[VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

## 11. How the agent helps with solar settings

**Timing:** 08:30–11:30 (3.0 minutes)

**Slide content:** The agent requests a study and reads the returned checks.
It can try another allowed option or ask the operator for help.

**Teaching notes:** Read the loop from left to right. The operator supplies a goal. The agent requests an allowed trial. The tool calculates voltage and current. The checks decide whether it can be compared. A failed trial can lead to another permitted request or a request for help.

**Figure scope:** The agent uses returned checks to choose the next permitted step.

**Editable figure:** diagrams/plain_voltage_agent.tex

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 12. Two solar settings change the result

**Timing:** 11:30–12:30 (1 minutes)

**Slide content:** One setting controls solar power output. The other provides voltage support.
The tool checks voltage, line current and the solar unit’s capacity.

**Teaching notes:** The two controls are active-power output and voltage support. The source model represents them as a and b. They share inverter capacity, so reducing one effect can change another. Use the tool to calculate those effects rather than infer safety from the control names.

**Figure scope:** Active power and voltage support share equipment capacity.

**Editable figure:** diagrams/plain_solar_controls.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 13. Both proposals face the same checks

**Timing:** 12:30–16:30 (4 minutes)

**Slide content:** The tool calculates the effect of each proposal.
Compare their scores only after voltage, current and capacity checks pass.

**Teaching notes:** The same checks apply to both candidates. Check voltage, line current and inverter capacity first. Only a passing proposal is eligible for cost comparison. The agent’s next request should be based on the returned checks.

**Figure scope:** Both proposals need the same voltage, current and capacity checks.

**Editable figure:** diagrams/concept_solar_checks.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[VMPC] James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.:** [https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf](https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf)

**[VSAC] Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.:** [https://proceedings.mlr.press/v80/haarnoja18b.html](https://proceedings.mlr.press/v80/haarnoja18b.html)

## 14. Read the voltage and current checks

**Timing:** 16:30–17:30 (1 minutes)

**Slide content:** Left: voltages should stay in the allowed band.
Right: current should stay below 100% of the allowance.

**Teaching notes:** The left plot shows the voltage distribution. The right compares current use with the allowed current. Both pass this model’s checks. The curves on the left are sorted separately, so their horizontal rank is not a matched physical location.

**Figure scope:** Calculated example at the original current allowance.

**Figure asset:** images/hands_on_L2_plot.png

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 15. Both pass, but the trade-off is different

**Timing:** 17:30–18:30 (1 minutes)

**Slide content:** MPC uses 73.62% of the current allowance; SAC uses 51.68%.
MPC has the lower overall score because current is only one part of the goal.

**Teaching notes:** The current-use values are 73.62% for MPC and 51.68% for saved SAC. Their scores are approximately 0.03110 and 0.43643. Lower score is preferred after all checks pass. SAC uses less current here partly because it also uses less active power.

**Figure scope:** Calculated example: both electrical checks pass.

**Editable figure:** diagrams/concept_solar_result.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 16. What if we allow less current?

**Timing:** 18:30–24:30 (6 minutes)

**Slide content:** Reduce the allowance from 80% to 75% of nominal current.
Which proposal might fail? Which would you choose if both pass?
What must the agent ask the tool to check again?

**Teaching notes:** Ask people to predict without doing any calculation. Make the rule change explicit: allowed current decreases from 80% to 75% of nominal. Give pairs time to explain what must be checked again and why the lowest current is not automatically the best proposal. Advance only after the discussion.

**Figure scope:** Discuss the scenario, then advance to the calculated result.

**Editable figure:** diagrams/concept_current_change.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 17. Both proposals pass the new current check

**Timing:** 24:30–26:30 (2 minutes)

**Slide content:** MPC has the lower score. SAC uses less current and less solar output.
These results cover the medium-voltage model. A wider grid needs a wider study.

**Teaching notes:** The numerical study has already been calculated for this changed allowance. MPC uses about 78.53% of the new allowance and SAC about 54.85%; both pass. Their scores are about 0.03110 and 0.43246. MPC has the lower score. These checks cover the medium-voltage model, not the entire distribution system.

**Figure scope:** Same load; the allowed current has been reduced to 75% of nominal.

**Editable figure:** diagrams/exercise_voltage_solution.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 18. Less current does not mean the best option

**Timing:** 26:30–27:30 (1 minutes)

**Slide content:** Here SAC also uses less solar output.
The operator’s goal values solar generation as well as operating limits.

**Teaching notes:** In the changed-allowance example, the active-power setting is about 96% of inverter rating for MPC and 34% for SAC. These percentages use inverter rating as the base. Less current comes with a generation trade-off, so the operator’s objective matters.

**Figure scope:** Active-power settings use inverter rating as their base.

**Editable figure:** diagrams/plain_voltage_tradeoff.tex

**[H02] Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 19. A PASS covers only the checked model

**Timing:** 27:30–28:00 (0.5 minutes)

**Slide content:** A study of the medium-voltage network cannot confirm a whole-grid claim.
The agent should request the missing study or return HOLD.

**Teaching notes:** The model’s scope travels with its result. A passing medium-voltage study does not establish low-voltage or whole-feeder safety. When the request is wider than the evidence, the useful response is a missing-study request or HOLD.

**Figure scope:** A passing result applies to the model and conditions actually checked.

**Editable figure:** diagrams/concept_scope.tex

**[H05] Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 20. Recorded example: the first option fails

**Timing:** 28:00–30:00 (2 minutes)

**Slide content:** Llama requests a check of the saved SAC proposal.
The numerical tool reports too much current and rejects it.

**Teaching notes:** This is a separate recorded full-feeder study, with different inputs from the earlier numerical comparison. Read the actual Llama request and returned tool result. The SAC trial reaches about 111.97% of allowed current, so it fails. The tool result determines eligibility.

**Figure scope:** Recorded full-feeder study; different inputs from the earlier comparison.

**Figure asset:** images/llama_voltage_1.png

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 21. Recorded example: another option is checked

**Timing:** 30:00–32:00 (2 minutes)

**Slide content:** Llama requests a check of the existing MPC fallback.
The returned electrical checks pass for this recorded case.

**Teaching notes:** The agent requests a check of an existing MPC fallback. It does not invent or solve MPC. The historical electrical check returns about 99.60% of allowed current and no listed violations. That makes the option eligible for review within this study’s stated scope.

**Figure scope:** Recorded full-feeder study: the requested fallback passes the checks.

**Figure asset:** images/llama_voltage_2.png

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 22. Recorded example: the operator receives a proposal

**Timing:** 32:00–34:00 (2 minutes)

**Slide content:** The agent returns the checked proposal and its conditions.
The operator still reviews it before any authorized action.

**Teaching notes:** The recorded workflow returns the checked proposal, while human acknowledgement remains pending and no equipment command is sent. Ask what evidence the operator receives and what remains outside the study, including permissions and protection checks.

**Figure scope:** Recorded workflow result; human review remains pending.

**Figure asset:** images/llama_voltage_3.png

**[LRV] Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 23. Case 2: who gets power after a fault?

**Timing:** 34:00–36:00 (2.0 minutes)

**Slide content:** A fault removes a supply path. Available capacity limits what can be restored.
The operator sets priorities; the agent can request and check restoration options.

**Teaching notes:** A fault removes one supply path in the six-node network. The available backup capacity limits which loads can be restored. Cyan marks the critical loads. The operator defines priorities, while the agent can request alternative restoration studies.

**Figure scope:** Six-node example. Cyan marks critical loads; dashed links are backup paths.

**Editable figure:** diagrams/plain_restoration_problem.tex

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 24. How the agent helps restore service

**Timing:** 36:00–39:00 (3 minutes)

**Slide content:** Choose the goal: critical loads first, or the most total power.
The agent can request a study, read the trade-off and ask for a new study when limits change.

**Teaching notes:** The goal changes the requested optimization. The agent should keep the operator’s priority, ask the tool for a plan, read service and capacity checks, and request a new study when inputs change. The solver decides which whole loads fit the network constraints.

**Figure scope:** The operator sets the priority. The agent requests the matching study.

**Editable figure:** diagrams/plain_restoration_agent.tex

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 25. The service goal changes the study request

**Timing:** 39:00–42:00 (3 minutes)

**Slide content:** Critical-first gives more weight to essential service.
Most-total-power aims to restore the largest amount of power.

**Teaching notes:** Critical-first assigns more value to essential service. Most-total-power maximizes total restored kW. Both still need the same network constraints. The agent translates the selected goal into the appropriate permitted study request; the solver performs the optimization.

**Figure scope:** Two possible operator goals for the same fault and available network.

**Editable figure:** diagrams/concept_service_request.tex

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 26. The goal changes who receives power

**Timing:** 42:00–43:00 (1 minutes)

**Slide content:** Critical-first: 130 kW total, including 90 kW for critical loads.
Most-total-power: 140 kW total, including 30 kW for critical loads.

**Teaching notes:** At a 40 kW backup tie, the critical-first result restores 130 kW total, including 90 kW critical. The total-power result restores 140 kW, including only 30 kW critical. Neither objective removes the need to explain the service trade-off. In the plots, overlapping markers indicate equal outcomes.

**Figure scope:** Calculated restoration results for the same network and limits.

**Figure asset:** images/hands_on_L6_plot.png

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 27. Check the restoration plan

**Timing:** 43:00–43:30 (0.5 minutes)

**Slide content:** Keep the faulted branch out of service. Check supply paths and capacity.
Voltage, protection and field switching need separate studies.

**Teaching notes:** Check that the fault stays isolated, supply paths connect and capacities are respected. This teaching exercise uses an active-power service model. AC voltages, protection coordination and the order of physical switching require separate studies and procedures.

**Figure scope:** Active-power model checks. Voltage, protection and field switching require separate work.

**Editable figure:** diagrams/plain_restoration_checks.tex

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[RSTL01] Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.:** [https://arxiv.org/abs/1912.05185v3](https://arxiv.org/abs/1912.05185v3)

**[RSTL02] Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.:** [https://doi.org/10.1109/TPWRS.2017.2720122](https://doi.org/10.1109/TPWRS.2017.2720122)

## 28. What if the backup path can carry more power?

**Timing:** 43:30–49:30 (6 minutes)

**Slide content:** Increase its capacity from 40 kW to 180 kW. Keep the fault and loads the same.
Would the two service goals still give different results?
What should the agent recalculate before reporting the new plan?

**Teaching notes:** Change only backup capacity in the scenario, from 40 to 180 kW. Ask whether the two service goals must always disagree. Invite participants to explain what the agent should recalculate before presenting a new plan. No software is needed to make the prediction.

**Figure scope:** Discuss the scenario, then advance to the calculated result.

**Editable figure:** diagrams/concept_capacity_change.tex

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 29. More capacity removes this service trade-off

**Timing:** 49:30–51:30 (2 minutes)

**Slide content:** At 40 kW, critical-first serves 90 kW of critical load instead of 30 kW.
At 180 kW, both goals serve 250 kW total, including all 90 kW of critical load.

**Teaching notes:** At 180 kW the two goals both restore 250 kW total, including 90 kW critical. Among the sampled capacities, the first agreement is at 80 kW. That discrete sweep does not establish an exact continuous crossover. More capacity removes the trade-off in this example.

**Figure scope:** Calculated results with the same fault, loads and service goals.

**Editable figure:** diagrams/exercise_restoration_solution.tex

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 30. A new limit needs a new study

**Timing:** 51:30–52:00 (0.5 minutes)

**Slide content:** Now reduce the allowed backup capacity from 40 kW to 20 kW.
The old result no longer supports the request. The agent must request a new study.

**Teaching notes:** Now imagine a stricter request: the backup capacity falls from 40 to 20 kW. Evidence calculated for the old capacity no longer matches the request. The agent should hold the old proposal and obtain a new constrained study. A failed evidence match does not itself prove that every new plan will fail.

**Figure scope:** A changed limit requires evidence calculated for the new request.

**Editable figure:** diagrams/plain_stale_result.tex

**[H07] Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 31. The agent keeps the operator’s goal

**Timing:** 52:00–52:30 (0.5 minutes)

**Slide content:** The operator sets priorities. The solver selects loads.
The agent can request the solve and explain the returned service trade-off.

**Teaching notes:** In the illustrated priority plan, loads 1, 2 and 5 receive service: 130 kW total and 90 kW critical. The operator sets the goal. The numerical solver selects loads. The agent can request the solve and explain the returned trade-off without changing the goal.

**Figure scope:** The operator’s priority stays fixed while the tool selects a feasible plan.

**Editable figure:** diagrams/restoration_plan.tex

**[H06] Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 32. Recorded example: another plan restores more service

**Timing:** 52:30–54:30 (2 minutes)

**Slide content:** In this separate larger-feeder study, Llama requests another plan.
The tool reports more service and passing electrical checks.

**Teaching notes:** This recorded larger-feeder example is separate from the six-node illustration. Llama requests another catalog option. The tool returns about 1,843.61 kW total and 474.04 kW critical service, with current at about 91.87% of its allowance. A proposed improvement becomes evidence only after the check.

**Figure scope:** Recorded larger-feeder example, separate from the six-node network.

**Figure asset:** images/llama_restoration_14.png

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 33. Recorded example: the tool rejects a trial

**Timing:** 54:30–56:00 (1.5 minutes)

**Slide content:** The next trial carries too much current.
It cannot replace the previous passing option.

**Teaching notes:** The next recorded trial restores more load but reaches about 111.01% of allowed current. It is rejected. The agent must keep the earlier passing option eligible rather than replace it with an overloaded plan.

**Figure scope:** Recorded larger-feeder example: the overloaded trial is rejected.

**Figure asset:** images/llama_restoration_15.png

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 34. Recorded example: a wrong ranking is corrected

**Timing:** 56:00–58:00 (2 minutes)

**Slide content:** Llama puts two passing plans in the wrong cost order.
Python keeps the lower-cost plan and checks it again.

**Teaching notes:** The model ranks two passing plans in the wrong cost order. Since smaller cost is preferred, negative 6109 is lower than negative 5509. Python keeps the lower-cost passing plan and rechecks it. This example shows why the workflow needs a numerical guard.

**Figure scope:** Recorded larger-feeder example. Lower cost is preferred, including negative costs.

**Figure asset:** images/llama_restoration_16.png

**[LRR] Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 35. Case 3: can we trust these readings?

**Timing:** 58:00–60:00 (2.0 minutes)

**Slide content:** Wrong readings can still look consistent with the model.
The agent can request checks, but action still needs a trusted basis.

**Teaching notes:** Wrong measurements can look consistent with a grid model. The operating question is whether the evidence supports a correction, not whether the agent can write a convincing explanation. Data trust and model coverage remain explicit conditions.

**Figure scope:** Concept sketch using a small four-bus model.

**Editable figure:** diagrams/plain_cyber_problem.tex

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 36. How the agent helps with suspicious readings

**Timing:** 60:00–63:00 (3.0 minutes)

**Slide content:** The agent can request the checks and keep missing evidence visible.
The operator reviews trust, model coverage and the proposed correction.

**Teaching notes:** The agent can request the permitted checks, read the results and report missing evidence. A required missing trust condition should lead to HOLD. The operator reviews the data basis, model scope and proposed adjustment.

**Figure scope:** The agent requests checks and preserves missing evidence.

**Editable figure:** diagrams/plain_cyber_agent.tex

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 37. Mismatch is only one check

**Timing:** 63:00–64:00 (1 minutes)

**Slide content:** Mismatch J measures how well the model fits the readings.
The simulation lets us measure how wrong the estimate is (state error).

**Teaching notes:** Mismatch J measures how well the model fits the readings. It is different from the control-cost score used in the solar case. The simulation also supplies a known true state, allowing an estimation error to be measured. That true state is not normally available to a real operator.

**Figure scope:** Mismatch measures model fit; state error measures estimation accuracy.

**Editable figure:** diagrams/plain_mismatch.tex

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY01] Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.:** [https://doi.org/10.1109/TPAS.1970.292678](https://doi.org/10.1109/TPAS.1970.292678)

## 38. Two patterns of wrong readings

**Timing:** 64:00–67:00 (3 minutes)

**Slide content:** One wrong reading may conflict with the other readings.
Coordinated changes may still look consistent with the model.

**Teaching notes:** One biased reading can disagree with the remaining data. Coordinated changes can agree with one another and still move the estimated state away from truth. This is a conceptual illustration of the two tested patterns; it is not an instruction for creating an attack.

**Figure scope:** Concept illustration of two patterns used in the numerical comparison.

**Editable figure:** diagrams/concept_bad_readings.tex

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 39. Read the alarm and the estimation error

**Timing:** 67:00–68:00 (1 minutes)

**Slide content:** Left: mismatch and its alarm threshold. Right: error against the simulation’s known truth.
A quiet alarm can appear alongside a growing error.

**Teaching notes:** The left plot compares mismatch with the alarm threshold. The right compares the state estimate with known simulation truth. A quiet alarm can coexist with a growing error. The agent should preserve this distinction when summarizing results.

**Figure scope:** Calculated model-fit and state-error results.

**Figure asset:** images/hands_on_L8_plot.png

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 40. A coordinated change can escape the alarm

**Timing:** 68:00–69:00 (1 minutes)

**Slide content:** At scale 1, one biased reading gives mismatch J=277.50 and an alarm.
A coordinated change gives J=3.92, no alarm, and 0.02678 rad of state error.

**Teaching notes:** At the reference change size, an isolated bias gives mismatch about 277.50 and triggers the alarm. A coordinated change gives about 3.92, no alarm, and about 0.02678 radians of state error. A low mismatch is incomplete evidence about data trust.

**Figure scope:** The known state is available inside the simulation for this comparison.

**Editable figure:** diagrams/plain_hidden_error.tex

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[CY02] Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.:** [https://doi.org/10.1145/1952982.1952995](https://doi.org/10.1145/1952982.1952995)

## 41. What if the data change is small?

**Timing:** 69:00–75:00 (6 minutes)

**Slide content:** Reduce the change to one tenth of the reference size.
Will the alarm always detect the error?
What else would the operator need before trusting the readings?

**Teaching notes:** Ask pairs to predict what a smaller error does to the alarm. Use one tenth of the reference change size. The question is whether a quiet alarm proves correct readings and what independent information an operator would need. Reveal the calculated example on the next slide.

**Figure scope:** Discuss the scenario, then advance to the calculated result.

**Editable figure:** diagrams/concept_bias_change.tex

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 42. A quiet alarm can still hide an error

**Timing:** 75:00–77:00 (2 minutes)

**Slide content:** Neither example triggers this alarm at one tenth of the reference size.
Both estimates still contain error. No alarm alone does not establish data trust.

**Teaching notes:** For the smaller change, mismatch is about 10.14 for isolated bias and 3.92 for the coordinated pattern. Both are below the threshold of about 15.09. Both estimates still contain error. No alarm means this test has not crossed its threshold; it does not authenticate the readings.

**Figure scope:** Calculated results at one tenth of the reference change size.

**Editable figure:** diagrams/exercise_cyber_solution.tex

**[H08] Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 43. Trusted information is needed before recovery

**Timing:** 77:00–77:30 (0.5 minutes)

**Slide content:** Without the required trusted readings, the response is HOLD.
With readings assumed trustworthy, the tool can calculate a proposal for review.

**Teaching notes:** The recovery example assumes additional trustworthy readings are available. Without that required condition the result is HOLD. With the assumption, the tool can calculate a bounded proposal. Neither the fitting algorithm nor Llama authenticates those channels.

**Figure scope:** Additional trustworthy readings are assumed in this example.

**Editable figure:** diagrams/plain_trust_choice.tex

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 44. The tool calculates a small correction

**Timing:** 77:30–78:00 (0.5 minutes)

**Slide content:** The solver finds the smallest allowed adjustment that meets the checked branch limits.
Predicted flow: 0.17000 p.u. Offline check: 0.17046 p.u. Limit: 0.18000 p.u.

**Teaching notes:** The fixed recovery example proposes an adjustment of about 0.121694 per unit. The model predicts a monitored flow of 0.17000, while the offline synthetic-truth check gives 0.17046; both are below the 0.18000 limit. Per unit expresses values relative to a common model base. The offline truth check is an experimental aid, not guaranteed field information.

**Figure scope:** Per-unit values share the same model base.

**Editable figure:** diagrams/plain_correction.tex

**[H09] Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 45. Recorded example: request the recovery tool

**Timing:** 78:00–79:30 (1.5 minutes)

**Slide content:** Llama requests the supplied recovery tool.
Python calculates a correction using the assumed trusted readings.

**Teaching notes:** Read the actual recorded Llama request. The task already supplies a permitted recovery tool and the trusted-reading assumption. Python estimates the state and calculates the correction. The language model routes the request; it does not provide the numerical estimate.

**Figure scope:** Recorded recovery request and numerical tool result.

**Figure asset:** images/llama_cyber_7.png

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 46. Recorded example: keep human review

**Timing:** 79:30–81:30 (2 minutes)

**Slide content:** The model checks pass; human review is still pending.
Data trust and operating permission still need review.

**Teaching notes:** The recorded model checks pass, but the overall result remains REVIEW and human acknowledgement is pending. The operator still needs a trusted data basis and operating authority. The fixed workflow obtains the same numerical correction, so this is not evidence that Llama improves estimation.

**Figure scope:** Recorded workflow result; human review remains pending.

**Figure asset:** images/llama_cyber_8.png

**[LRC] Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json)

**[LR0] Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py)

## 47. Review must refer to the same proposal

**Timing:** 81:30–82:30 (1 minutes)

**Slide content:** The proposal ID and model scope must match the checked study.
A different proposal or wider scope needs a new review.

**Teaching notes:** A reviewer must refer to the same proposal and scope that were checked. A changed proposal ID or a wider request cannot inherit an earlier passing result. In the teaching example, readback is simulated and sends no equipment command.

**Figure scope:** Illustrative proposal IDs. Review is separate from equipment operation.

**Editable figure:** diagrams/concept_review_match.tex

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 48. The operator chooses the next step

**Timing:** 82:30–83:30 (1 minutes)

**Slide content:** Review the case, tool results, checked limits and missing work.
Request another study, reject the proposal or take the next authorized step.

**Teaching notes:** The operator can request more evidence, reject the proposal or continue with a defined authorized step. Review the case, returned limits, model coverage and missing studies. Acceptance of a study is separate from issuing a field command.

**Figure scope:** The operator reviews the study and chooses the next authorized step.

**Editable figure:** diagrams/ops_review.tex

**[H12] Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

**[OT01] Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).:** [https://doi.org/10.6028/NIST.SP.800-82r3](https://doi.org/10.6028/NIST.SP.800-82r3)

**[EVAL01] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

## 49. Multi-agent framework used in these cases

**Timing:** 83:30–87:30 (4.0 minutes)

**Slide content:** The five roles share the same case facts and checked results.
One Llama model handles planning and refinement. Python calculates and checks.

**Teaching notes:** Awareness reads the shared case. Planning prepares permitted options and uses Llama to choose a study. Simulation calculates. Verification checks limits and case identity. The Llama optimizer requests a bounded change or ranks passing options. Every changed trial returns for simulation and verification. Python guards the final choice before operator review. One Llama model fills two roles; this is not five independent language models. The implementation uses case-specific numerical tools behind the same stages.

**Figure scope:** Implemented five-role workflow with a case-specific numerical tool.

**Editable figure:** diagrams/workshop_multi_agent.tex

**[WF01] Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py)

**[H10] Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## 50. Explain one case in your own words

**Timing:** 87:30–90:00 (2.5 minutes)

**Slide content:** What is the operator’s problem, and what should the agent request next?
Which tool result supports the proposal, and what must the operator still decide?

**Teaching notes:** Ask participants to choose one case and explain the complete loop in their own words. They should name the problem, an agent request, a returned numerical fact and a remaining human decision. Optional practice materials can be used after the concept tutorial, but no account or code is needed for this discussion.

**Figure scope:** Explain the idea first. Practice material is available separately.

**Editable figure:** diagrams/concept_case_summary.tex

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

## [EVAL01] Artificial Intelligence Risk Management Framework (AI RMF 1.0)

**Authors / issuer:** National Institute of Standards and Technology

**Publisher / venue:** NIST AI 100-1

**Date:** 26 January 2023

**Type:** Voluntary risk-management guidance

**Full source URL:** [https://doi.org/10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)

**Full paper PDF:** [https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

## [WF01] Five-role operator study workflow: implementation and recorded cases

**Authors / issuer:** Alaa Selim and Mohamed Chehada

**Publisher / venue:** GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive

**Date:** Implementation inspected 25 October 2026; records dated 27 September 2026

**Type:** Executable teaching implementation and recorded evidence

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py)

**Source code:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_case_tools.py](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_case_tools.py)

**Publication:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json)

## [H10] Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030

**Authors / issuer:** Classroom Labs notebook

**Publisher / venue:** Public notebook and Python source

**Date:** 24 October 2026; stable notebook cell IDs checked

**Type:** Executable teaching material

**Full source URL:** [https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb](https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb)

## Visual credit: stanford_agentic_capabilities.png

**Caption:** Original Stanford figure: one function call and a multi-step workflow.

**Credit:** Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University, Fall 2026, p.2.

**Used on:** 3. The agent asks; the tool calculates

**Asset type:** Original Stanford lecture figure excerpt

**Transformation:** Unchanged vector selection from the presenter-supplied Stanford lecture, p.2; Poppler PNG rendering. Exact crop and source/image hashes: research/stanford_sources/excerpt_manifest.json.

**Provenance note:** Cropped from the supplied Stanford lecture PDF. Original author and page retained in the caption and full source guide.

**Evidence limit:** Original Stanford figure: one function call and a multi-step workflow.

**Original source / page:** [https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=2](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf#page=2)

**Original figure / image URL:** [research/evidence/replots/stanford_agentic_capabilities.png](research/evidence/replots/stanford_agentic_capabilities.png)

## Visual credit: hands_on_L2_plot.png

**Caption:** Calculated example at the original current allowance.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 14. Read the voltage and current checks

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Calculated example at the original current allowance.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L2_plot.png](research/evidence/replots/hands_on_L2_plot.png)

## Visual credit: llama_voltage_1.png

**Caption:** Recorded full-feeder study; different inputs from the earlier comparison.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 20. Recorded example: the first option fails

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Recorded full-feeder study; different inputs from the earlier comparison.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_1.png](research/evidence/replots/llama_voltage_1.png)

## Visual credit: llama_voltage_2.png

**Caption:** Recorded full-feeder study: the requested fallback passes the checks.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 21. Recorded example: another option is checked

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Recorded full-feeder study: the requested fallback passes the checks.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_2.png](research/evidence/replots/llama_voltage_2.png)

## Visual credit: llama_voltage_3.png

**Caption:** Recorded workflow result; human review remains pending.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 22. Recorded example: the operator receives a proposal

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Recorded workflow result; human review remains pending.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_voltage_3.png](research/evidence/replots/llama_voltage_3.png)

## Visual credit: hands_on_L6_plot.png

**Caption:** Calculated restoration results for the same network and limits.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 26. The goal changes who receives power

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Calculated restoration results for the same network and limits.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L6_plot.png](research/evidence/replots/hands_on_L6_plot.png)

## Visual credit: llama_restoration_14.png

**Caption:** Recorded larger-feeder example, separate from the six-node network.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 32. Recorded example: another plan restores more service

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Recorded larger-feeder example, separate from the six-node network.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_14.png](research/evidence/replots/llama_restoration_14.png)

## Visual credit: llama_restoration_15.png

**Caption:** Recorded larger-feeder example: the overloaded trial is rejected.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 33. Recorded example: the tool rejects a trial

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Recorded larger-feeder example: the overloaded trial is rejected.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_15.png](research/evidence/replots/llama_restoration_15.png)

## Visual credit: llama_restoration_16.png

**Caption:** Recorded larger-feeder example. Lower cost is preferred, including negative costs.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 34. Recorded example: a wrong ranking is corrected

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Recorded larger-feeder example. Lower cost is preferred, including negative costs.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_restoration_16.png](research/evidence/replots/llama_restoration_16.png)

## Visual credit: hands_on_L8_plot.png

**Caption:** Calculated model-fit and state-error results.

**Credit:** Classroom Labs: actual executed notebook output, Python 3.12

**Used on:** 39. Read the alarm and the estimation error

**Asset type:** Executed notebook plot or browser capture

**Transformation:** Exact PNG output or documented HTML output selection; see research/hands_on/hands_on_manifest.json.

**Evidence limit:** Calculated model-fit and state-error results.

**Original source / page:** [research/hands_on/index.html](research/hands_on/index.html)

**Original figure / image URL:** [research/evidence/replots/hands_on_L8_plot.png](research/evidence/replots/hands_on_L8_plot.png)

## Visual credit: llama_cyber_7.png

**Caption:** Recorded recovery request and numerical tool result.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 45. Recorded example: request the recovery tool

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Recorded recovery request and numerical tool result.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_cyber_7.png](research/evidence/replots/llama_cyber_7.png)

## Visual credit: llama_cyber_8.png

**Caption:** Recorded workflow result; human review remains pending.

**Credit:** Recorded Llama 3.1:8b replies and numerical study records; exact public reasons preserved

**Used on:** 46. Recorded example: keep human review

**Asset type:** Browser-rendered selection of verified recorded fields

**Transformation:** Presentation selection of verified recorded fields. Exact returned reason is unchanged. Full data, hashes and source paths: research/llama_replay/episodes.json.

**Provenance note:** Raw JSON, parsed response and historical trace cross-checked by src/llama_walkthrough.py. Selected fields are not a screenshot of a deployed product. capture_manifest.json records source and image SHA-256 values.

**Evidence limit:** Recorded workflow result; human review remains pending.

**Original source / page:** [research/llama_replay/index.html](research/llama_replay/index.html)

**Original figure / image URL:** [research/evidence/replots/llama_cyber_8.png](research/evidence/replots/llama_cyber_8.png)
