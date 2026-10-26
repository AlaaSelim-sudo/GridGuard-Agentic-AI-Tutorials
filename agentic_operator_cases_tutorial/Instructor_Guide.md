# Instructor Guide: Three Operator Cases

50 concept slides / 90 minutes. Agent concepts and Colab setup: 8 slides / 5.5 minutes; Voltage support: 14 slides / 28.5 minutes; Service restoration: 12 slides / 24.0 minutes; Cyber response: 12 slides / 23.5 minutes; Llama walkthrough and operator practice: 4 slides / 8.5 minutes. Explain the problem, follow the agent request and numerical result, and discuss the operator decision. No audience software steps are required.

## 1. Agentic AI: Three Operator Cases

00:00–01:00 / 1 minutes.

The examples are self-contained. No computer or software setup is needed. We will follow a goal, the agent’s requests, numerical evidence and a human decision. The results come from reduced or synthetic studies; they are examples for learning.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

IEEE Communications Society. IEEE Communications Society: official resources and network presentation template. Reviewed 17 October 2026.
Full source: https://www.comsoc.org/about/brand-experience/resources

## 2. An agent chooses what to try next

01:00–02:00 / 1 minutes.

The agent does not calculate the electrical result by writing a confident answer. It chooses a permitted tool, reads the result and decides whether another request or human review is needed. Trace the feedback arrow once with the audience.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 3. The agent asks; the tool calculates

02:00–02:30 / 0.5 minutes.

The Stanford figure distinguishes one function call from a longer agentic workflow. A function can perform one calculation. An agentic workflow connects requests and uses returned results to decide what comes next.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Erik S., Barry Zhang. Building effective agents. Anthropic Engineering. 2024-12-19.
Full source: https://www.anthropic.com/research/building-effective-agents

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 4. Solar settings: which option should we try?

02:30–03:00 / 0.5 minutes.

Suppose an operator needs new solar settings. Different settings affect voltage, current and useful solar output. The agent organizes a bounded study; the numerical tool supplies the engineering evidence.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Sina J. Semnani, Violet Z. Yao, Heidi C. Zhang, Monica S. Lam. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia. Findings of the Association for Computational Linguistics: EMNLP 2023, pp.2387–2413. December 2023.
Full source: https://aclanthology.org/2023.findings-emnlp.157/
Full paper: https://aclanthology.org/2023.findings-emnlp.157.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 5. Give the agent a goal and clear limits

03:00–04:00 / 1 minutes.

A useful request states the operating goal, available tools and stopping conditions. The agent needs to know when it must ask for review rather than continue trying options. The operator defines these boundaries.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.
Full source: https://aclanthology.org/2025.acl-long.1323/
Full paper: https://aclanthology.org/2025.acl-long.1323.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L0–L1; cells classroom-002 and classroom-004. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 6. Restoration: who should get power first?

04:00–04:30 / 0.5 minutes.

When supply is limited, restoring the greatest total power can differ from protecting essential services. The operator chooses that priority. The agent must preserve it when requesting and comparing studies.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Harshit Joshi, Shicheng Liu, James Chen, Larsen Weigle, Monica Lam. Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp.27264–27308. July 2025.
Full source: https://aclanthology.org/2025.acl-long.1323/
Full paper: https://aclanthology.org/2025.acl-long.1323.pdf

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 7. Keep three jobs clear

04:30–05:00 / 0.5 minutes.

Keep the jobs separate. The agent coordinates requests. The numerical tool calculates. The operator reviews the evidence and decides the next authorized step. A tool passing its checks is not operating permission.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 8. Wrong readings can still fit a model

05:00–05:30 / 0.5 minutes.

Readings may fit a model and still be wrong. An alarm test measures one kind of mismatch. The agent can request additional checks and identify missing information, but its explanation cannot make a data source trustworthy.

Full sources:

Monica Lam. CS224V Agentic AI, Lecture 1: Introduction. Stanford University. Fall 2026.
Full source: https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf
Publication: https://web.stanford.edu/class/cs224v/

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 9. Case 1: which solar settings should we use?

05:30–07:30 / 2.0 minutes.

Start with the physical problem: choose solar controls that respect voltage, current and equipment capacity while serving the stated generation goal. The agent can organize trials and return a checked option. It does not replace the solver or the operator.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Existing GridGuard workshop / SMART-DS synthetic-feeder extraction. Synthetic Greensboro feeder uhs20_1247–udt8894: model map and declared study scope. Existing teaching snapshot reviewed 18 October 2026.
Full source: https://data.openei.org/submissions/2981

## 10. Two tools suggest different settings

07:30–08:30 / 1 minutes.

MPC means model predictive control: it plans with a model. SAC means soft actor-critic: it uses a previously trained policy. Both produce proposals. Apply the same electrical checks to each before comparing cost or usefulness.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.
Full source: https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.
Full source: https://proceedings.mlr.press/v80/haarnoja18b.html

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

## 11. How the agent helps with solar settings

08:30–11:30 / 3.0 minutes.

Read the loop from left to right. The operator supplies a goal. The agent requests an allowed trial. The tool calculates voltage and current. The checks decide whether it can be compared. A failed trial can lead to another permitted request or a request for help.

Full sources:

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 12. Two solar settings change the result

11:30–12:30 / 1 minutes.

The two controls are active-power output and voltage support. The source model represents them as a and b. They share inverter capacity, so reducing one effect can change another. Use the tool to calculate those effects rather than infer safety from the control names.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 13. Both proposals face the same checks

12:30–16:30 / 4 minutes.

The same checks apply to both candidates. Check voltage, line current and inverter capacity first. Only a passing proposal is eligible for cost comparison. The agent’s next request should be based on the returned checks.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

James B. Rawlings; David Q. Mayne; Moritz M. Diehl. Model Predictive Control: Theory, Computation, and Design, second edition. Nob Hill Publishing. 2017.
Full source: https://sites.engineering.ucsb.edu/~jbraw/mpc/MPC-book-2nd-edition-1st-printing.pdf

Tuomas Haarnoja; Aurick Zhou; Pieter Abbeel; Sergey Levine. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. Proceedings of the 35th International Conference on Machine Learning, PMLR 80, pp. 1861–1870. 2018.
Full source: https://proceedings.mlr.press/v80/haarnoja18b.html

## 14. Read the voltage and current checks

16:30–17:30 / 1 minutes.

The left plot shows the voltage distribution. The right compares current use with the allowed current. Both pass this model’s checks. The curves on the left are sorted separately, so their horizontal rank is not a matched physical location.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 15. Both pass, but the trade-off is different

17:30–18:30 / 1 minutes.

The current-use values are 73.62% for MPC and 51.68% for saved SAC. Their scores are approximately 0.03110 and 0.43643. Lower score is preferred after all checks pass. SAC uses less current here partly because it also uses less active power.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 16. What if we allow less current?

18:30–24:30 / 6 minutes.

Ask people to predict without doing any calculation. Make the rule change explicit: allowed current decreases from 80% to 75% of nominal. Give pairs time to explain what must be checked again and why the lowest current is not automatically the best proposal. Advance only after the discussion.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 17. Both proposals pass the new current check

24:30–26:30 / 2 minutes.

The numerical study has already been calculated for this changed allowance. MPC uses about 78.53% of the new allowance and SAC about 54.85%; both pass. Their scores are about 0.03110 and 0.43246. MPC has the lower score. These checks cover the medium-voltage model, not the entire distribution system.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 18. Less current does not mean the best option

26:30–27:30 / 1 minutes.

In the changed-allowance example, the active-power setting is about 96% of inverter rating for MPC and 34% for SAC. These percentages use inverter rating as the base. Less current comes with a generation trade-off, so the operator’s objective matters.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L2; cell classroom-007; src/continuous_control.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 19. A PASS covers only the checked model

27:30–28:00 / 0.5 minutes.

The model’s scope travels with its result. A passing medium-voltage study does not establish low-voltage or whole-feeder safety. When the request is wider than the evidence, the useful response is a missing-study request or HOLD.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L5; cell classroom-016; MV-only default model. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 20. Recorded example: the first option fails

28:00–30:00 / 2 minutes.

This is a separate recorded full-feeder study, with different inputs from the earlier numerical comparison. Read the actual Llama request and returned tool result. The SAC trial reaches about 111.97% of allowed current, so it fails. The tool result determines eligibility.

Full sources:

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 21. Recorded example: another option is checked

30:00–32:00 / 2 minutes.

The agent requests a check of an existing MPC fallback. It does not invent or solve MPC. The historical electrical check returns about 99.60% of allowed current and no listed violations. That makes the option eligible for review within this study’s stated scope.

Full sources:

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 22. Recorded example: the operator receives a proposal

32:00–34:00 / 2 minutes.

The recorded workflow returns the checked proposal, while human acknowledgement remains pending and no equipment command is sent. Ask what evidence the operator receives and what remains outside the study, including permissions and protection checks.

Full sources:

Workshop recorded model replies and numerical study records. Voltage P3_current_reserve: Llama 3.1:8b planner, recovery and review calls 1–3. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/continuous_llama_opendss_20260927T161223523552Z.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 23. Case 2: who gets power after a fault?

34:00–36:00 / 2.0 minutes.

A fault removes one supply path in the six-node network. The available backup capacity limits which loads can be restored. Cyan marks the critical loads. The operator defines priorities, while the agent can request alternative restoration studies.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 24. How the agent helps restore service

36:00–39:00 / 3 minutes.

The goal changes the requested optimization. The agent should keep the operator’s priority, ask the tool for a plan, read service and capacity checks, and request a new study when inputs change. The solver decides which whole loads fit the network constraints.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 25. The service goal changes the study request

39:00–42:00 / 3 minutes.

Critical-first assigns more value to essential service. Most-total-power maximizes total restored kW. Both still need the same network constraints. The agent translates the selected goal into the appropriate permitted study request; the solver performs the optimization.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 26. The goal changes who receives power

42:00–43:00 / 1 minutes.

At a 40 kW backup tie, the critical-first result restores 130 kW total, including 90 kW critical. The total-power result restores 140 kW, including only 30 kW critical. Neither objective removes the need to explain the service trade-off. In the plots, overlapping markers indicate equal outcomes.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 27. Check the restoration plan

43:00–43:30 / 0.5 minutes.

Check that the fault stays isolated, supply paths connect and capacities are respected. This teaching exercise uses an active-power service model. AC voltages, protection coordination and the order of physical switching require separate studies and procedures.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Ying Wang, Yin Xu, Jiaxu Li, Jinghan He, Xiaojun Wang. On the Radiality Constraints for Distribution System Restoration and Reconfiguration Problems. Author preprint, arXiv:1912.05185v3. 15 March2020(v3); first submitted11 December2019.
Full source: https://arxiv.org/abs/1912.05185v3
Full paper: https://arxiv.org/pdf/1912.05185v3

Bo Chen, Chen Chen, Jianhui Wang, Karen L. Butler-Purry. Sequential Service Restoration for Unbalanced Distribution Systems and Microgrids. IEEE Transactions on Power Systems33(2),1507–1520. March2018.
Full source: https://doi.org/10.1109/TPWRS.2017.2720122

## 28. What if the backup path can carry more power?

43:30–49:30 / 6 minutes.

Change only backup capacity in the scenario, from 40 to 180 kW. Ask whether the two service goals must always disagree. Invite participants to explain what the agent should recalculate before presenting a new plan. No software is needed to make the prediction.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 29. More capacity removes this service trade-off

49:30–51:30 / 2 minutes.

At 180 kW the two goals both restore 250 kW total, including 90 kW critical. Among the sampled capacities, the first agreement is at 80 kW. That discrete sweep does not establish an exact continuous crossover. More capacity removes the trade-off in this example.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 30. A new limit needs a new study

51:30–52:00 / 0.5 minutes.

Now imagine a stricter request: the backup capacity falls from 40 to 20 kW. Evidence calculated for the old capacity no longer matches the request. The agent should hold the old proposal and obtain a new constrained study. A failed evidence match does not itself prove that every new plan will fail.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L7; cell classroom-021; request/evidence binding. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 31. The agent keeps the operator’s goal

52:00–52:30 / 0.5 minutes.

In the illustrated priority plan, loads 1, 2 and 5 receive service: 130 kW total and 90 kW critical. The operator sets the goal. The numerical solver selects loads. The agent can request the solve and explain the returned trade-off without changing the goal.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L6; cell classroom-018; src/standard_formulations.py. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 32. Recorded example: another plan restores more service

52:30–54:30 / 2 minutes.

This recorded larger-feeder example is separate from the six-node illustration. Llama requests another catalog option. The tool returns about 1,843.61 kW total and 474.04 kW critical service, with current at about 91.87% of its allowance. A proposed improvement becomes evidence only after the check.

Full sources:

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 33. Recorded example: the tool rejects a trial

54:30–56:00 / 1.5 minutes.

The next recorded trial restores more load but reaches about 111.01% of allowed current. It is rejected. The agent must keep the earlier passing option eligible rather than replace it with an overloaded plan.

Full sources:

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 34. Recorded example: a wrong ranking is corrected

56:00–58:00 / 2 minutes.

The model ranks two passing plans in the wrong cost order. Since smaller cost is preferred, negative 6109 is lower than negative 5509. Python keeps the lower-cost passing plan and rechecks it. This example shows why the workflow needs a numerical guard.

Full sources:

Workshop recorded model replies and numerical study records. Feeder-catalog restoration: Llama 3.1:8b refinement and ranking calls 14–16. Public teaching archive. 27 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_run_20260927T184402Z_53e0cf/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 35. Case 3: can we trust these readings?

58:00–60:00 / 2.0 minutes.

Wrong measurements can look consistent with a grid model. The operating question is whether the evidence supports a correction, not whether the agent can write a convincing explanation. Data trust and model coverage remain explicit conditions.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 36. How the agent helps with suspicious readings

60:00–63:00 / 3.0 minutes.

The agent can request the permitted checks, read the results and report missing evidence. A required missing trust condition should lead to HOLD. The operator reviews the data basis, model scope and proposed adjustment.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 37. Mismatch is only one check

63:00–64:00 / 1 minutes.

Mismatch J measures how well the model fits the readings. It is different from the control-cost score used in the solar case. The simulation also supplies a known true state, allowing an estimation error to be measured. That true state is not normally available to a real operator.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Fred C. Schweppe, J. Wildes. Power System Static-State Estimation, Part I: Exact Model. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), pp. 120–125. January 1970.
Full source: https://doi.org/10.1109/TPAS.1970.292678

## 38. Two patterns of wrong readings

64:00–67:00 / 3 minutes.

One biased reading can disagree with the remaining data. Coordinated changes can agree with one another and still move the estimated state away from truth. This is a conceptual illustration of the two tested patterns; it is not an instruction for creating an attack.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 39. Read the alarm and the estimation error

67:00–68:00 / 1 minutes.

The left plot compares mismatch with the alarm threshold. The right compares the state estimate with known simulation truth. A quiet alarm can coexist with a growing error. The agent should preserve this distinction when summarizing results.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 40. A coordinated change can escape the alarm

68:00–69:00 / 1 minutes.

At the reference change size, an isolated bias gives mismatch about 277.50 and triggers the alarm. A coordinated change gives about 3.92, no alarm, and about 0.02678 radians of state error. A low mismatch is incomplete evidence about data trust.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Yao Liu, Peng Ning, Michael K. Reiter. False Data Injection Attacks against State Estimation in Electric Power Grids. ACM Transactions on Information and System Security, 14(1), Article 13, 33 pages. May 2011.
Full source: https://doi.org/10.1145/1952982.1952995
Full paper: https://reitermk.github.io/papers/2011/TISSEC2.pdf

## 41. What if the data change is small?

69:00–75:00 / 6 minutes.

Ask pairs to predict what a smaller error does to the alarm. Use one tenth of the reference change size. The question is whether a quiet alarm proves correct readings and what independent information an operator would need. Reveal the calculated example on the next slide.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 42. A quiet alarm can still hide an error

75:00–77:00 / 2 minutes.

For the smaller change, mismatch is about 10.14 for isolated bias and 3.92 for the coordinated pattern. Both are below the threshold of about 15.09. Both estimates still contain error. No alarm means this test has not crossed its threshold; it does not authenticate the readings.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L8; cell classroom-023; four-bus DC fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 43. Trusted information is needed before recovery

77:00–77:30 / 0.5 minutes.

The recovery example assumes additional trustworthy readings are available. Without that required condition the result is HOLD. With the assumption, the tool can calculate a bounded proposal. Neither the fitting algorithm nor Llama authenticates those channels.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 44. The tool calculates a small correction

77:30–78:00 / 0.5 minutes.

The fixed recovery example proposes an adjustment of about 0.121694 per unit. The model predicts a monitored flow of 0.17000, while the offline synthetic-truth check gives 0.17046; both are below the 0.18000 limit. Per unit expresses values relative to a common model base. The offline truth check is an experimental aid, not guaranteed field information.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L9; cell classroom-026; fixed trusted-recovery fixture. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 45. Recorded example: request the recovery tool

78:00–79:30 / 1.5 minutes.

Read the actual recorded Llama request. The task already supplies a permitted recovery tool and the trusted-reading assumption. Python estimates the state and calculates the correction. The language model routes the request; it does not provide the numerical estimate.

Full sources:

Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 46. Recorded example: keep human review

79:30–81:30 / 2 minutes.

The recorded model checks pass, but the overall result remains REVIEW and human acknowledgement is pending. The operator still needs a trusted data basis and operating authority. The fixed workflow obtains the same numerical correction, so this is not evidence that Llama improves estimation.

Full sources:

Workshop recorded model replies and numerical study records. Standard four-bus cyber study: Llama 3.1:8b tool selection and REVIEW calls 7–8. Public teaching archive. 21 September 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/standard_stage_20260921T143826Z_42d19a61/llama_calls.json

Classroom Labs notebook and Python helper. L10B: Watch how Llama chooses a tool; src/llama_walkthrough.py. Public reproducible teaching material. 24 October 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/llama_walkthrough.py

## 47. Review must refer to the same proposal

81:30–82:30 / 1 minutes.

A reviewer must refer to the same proposal and scope that were checked. A changed proposal ID or a wider request cannot inherit an earlier passing result. In the teaching example, readback is simulated and sends no equipment command.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 48. The operator chooses the next step

82:30–83:30 / 1 minutes.

The operator can request more evidence, reject the proposal or continue with a defined authorized step. Review the case, returned limits, model coverage and missing studies. Acceptance of a study is separate from issuing a field command.

Full sources:

Classroom Labs notebook. Classroom_Labs.ipynb, L12; cell classroom-033; simulated readback only. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

Keith Stouffer, Michael Pease, CheeYee Tang, Timothy Zimmerman, Victoria Pillitteri, Suzanne Lightman, Adam Hahn, Stephanie Saravia, Aslam Sherule, Michael Thompson. Guide to Operational Technology (OT) Security. National Institute of Standards and Technology, NIST SP 800-82 Revision 3. September 2023 (final).
Full source: https://doi.org/10.6028/NIST.SP.800-82r3
Full paper: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf
Publication: https://csrc.nist.gov/pubs/sp/800/82/r3/final

National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 26 January 2023.
Full source: https://doi.org/10.6028/NIST.AI.100-1
Full paper: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

## 49. Multi-agent framework used in these cases

83:30–87:30 / 4.0 minutes.

Awareness reads the shared case. Planning prepares permitted options and uses Llama to choose a study. Simulation calculates. Verification checks limits and case identity. The Llama optimizer requests a bounded change or ranks passing options. Every changed trial returns for simulation and verification. Python guards the final choice before operator review. One Llama model fills two roles; this is not five independent language models. The implementation uses case-specific numerical tools behind the same stages.

Full sources:

Alaa Selim and Mohamed Chehada. Five-role operator study workflow: implementation and recorded cases. GridGuard Agentic AI Tutorials, reproducible Python source and saved study archive. 2026.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/src/proposal_workflow.py
Publication: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/results/proposal_complete_workflow.json

Classroom Labs notebook. Classroom_Labs.ipynb, L10–L11; cells classroom-028 and classroom-030. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb

## 50. Explain one case in your own words

87:30–90:00 / 2.5 minutes.

Ask participants to choose one case and explain the complete loop in their own words. They should name the problem, an agent request, a returned numerical fact and a remaining human decision. Optional practice materials can be used after the concept tutorial, but no account or code is needed for this discussion.

Full sources:

Classroom Labs notebook. Setup: COLAB_GUIDE.md; Classroom_Labs.ipynb. Public notebook and Python source. 24 October 2026; stable notebook cell IDs checked.
Full source: https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/COLAB_GUIDE.md

