# Practical operator interactions for teaching

**Status:** proposed illustrative workflows, reviewed October 17, 2026. Names such as Feeder F12, study S24 and outage O784 are invented. Tool names below are proposed interface names, not existing GridGuard features or vendor API names. None of these examples asserts a company deployment.

## Start with the desk and the authority

- **ISO/RTO or transmission desk:** use an authorized EMS study snapshot, transmission contingencies and the relevant outage/market records. CAISO describes its role in transmission operation and wholesale markets. [O01](https://www.caiso.com/about/our-business)
- **Distribution desk:** use ADMS/OMS, feeder models, GIS and distribution telemetry. ADMS can include monitoring, control, outage management and automated restoration; these teaching examples expose its read-only and study interfaces. [O02](https://www.gevernova.com/software/products/gridos/advanced-distribution-management-system)
- **Protection and time-critical automatic control:** keep the agent outside the protection/control execution path. In this tutorial it prepares evidence and study results for people. Protection devices and automated systems must act quickly to isolate faults; an agent discussion is not that mechanism. [O03](https://www.energy.gov/cmei/systems/solar-grid-planning-and-operation-basics)

Do not use the terms “ISO dispatch” and “ADMS feeder switching” interchangeably. GridGuard's OpenDSS example is a distribution study. A transmission contingency exercise needs the operator's approved transmission analysis tool and model. The boundaries and workflows here are instructional design choices.

## 1. Shift handover — turn logs into a checked briefing

**Desk:** either transmission or distribution; select one desk and its authorized sources.

**Operator prompt:** “Prepare the 07:00 distribution-desk handover from the last shift's logs. Link unresolved alarms, active outages and pending follow-ups to their records.”

**Governed tools:** `read_shift_log` → `read_active_outages` → `read_alarm_status` → `read_current_procedures`. All are scoped read-only to the selected desk and period.

**Expected output:** draft briefing with current status, last observation time, source link, assigned owner and next review time for each open item. Mark unknown ownership and conflicting records explicitly.

**Operator check:** compare the draft with the official log and outgoing operator's account; confirm which items remain open before accepting the briefing.

**Stop condition:** the log is unavailable, timestamps conflict, or an unresolved item lacks a reliable current status. Return the gap for human reconciliation.

**Teaching connection:** state and provenance (T01/T02); this is a proposed workflow.

## 2. Distribution alarm triage — gather before proposing

**Desk:** distribution operator using ADMS and historian views.

**Operator prompt:** “Investigate the high-voltage alarm on Feeder F12. Build an evidence timeline and identify the next permitted checks.”

**Governed tools:** `read_alarm` → `read_historian_window` → `read_topology_version` → `read_asset_metadata` → `retrieve_approved_procedure`. A separately allowed `run_feeder_study` can evaluate a candidate in a sandbox.

**Expected output:** time-aligned observations, quality flags, affected asset IDs, competing explanations, supporting sources and the procedure section for the next check. Separate observed facts from hypotheses.

**Operator check:** confirm asset mapping, data quality and topology against the operating display; review all modeled constraints before using study results.

**Stop condition:** stale/invalid telemetry, inconsistent device status, changed topology or failed study convergence. Refresh or escalate instead of ranking unsupported actions.

**Teaching connection:** leads directly into the existing illustrative GridGuard voltage exercise (L01); the proposed ADMS/historian integration is additional work.

## 3. Transmission contingency analysis — summarize solver evidence

**Desk:** ISO/RTO or transmission operations analyst using an approved EMS study environment.

**Operator prompt:** “Using approved snapshot S24 and contingency set C7, summarize the solved cases that exceed the study's declared limits and link the solver evidence.”

**Governed tools:** `read_approved_ems_snapshot` → `read_contingency_set` → `run_approved_contingency_analysis` → `retrieve_study_limits`. Preserve model, rating and solver versions.

**Expected output:** case-by-case solve status, monitored element, calculated value, applicable declared limit, assumptions and result-file link. Identify checks outside the study scope, such as any dynamic analysis not performed.

**Operator check:** verify the snapshot, contingency list, ratings and study assumptions; use the approved operational process to assess options.

**Stop condition:** nonconvergence, missing ratings, unauthorized contingency set, or a relevant network change after the snapshot. A converged power-flow result alone does not establish every aspect of system security.

**Teaching connection:** an illustrative transmission workflow; do not present OpenDSS feeder verification as an EMS transmission-security assessment.

## 4. Planned-outage coordination — prepare a review memo

**Desk:** transmission outage coordinator; distribution outage coordination would use its own records and procedures.

**Operator prompt:** “Screen proposed outage O784 against tomorrow's accepted outages and approved study results. Prepare questions and conflicts for the outage reviewer.”

**Governed tools:** `read_outage_request` → `read_accepted_outage_schedule` → `read_study_snapshot` → `run_approved_outage_screen` → `retrieve_coordination_procedure`.

**Expected output:** draft conflict memo listing overlapping work, affected modeled elements, screening evidence, missing confirmations and the record owner to contact. Every conclusion carries request/status times and model version.

**Operator check:** confirm current outage status and required coordination through the organization's established process; the reviewer owns acceptance or rejection.

**Stop condition:** a request changes, records disagree, required confirmation is absent, or the screening tool cannot resolve the case. Route the exception to the reviewer.

**Teaching connection:** CAISO's published outage-assistance case supports the general pattern (C01/C02); these exact interactions and interface names are proposed.

## 5. Operator training — rehearse in an isolated scenario

**Desk:** instructor-led distribution training; use a separate transmission simulator for transmission training.

**Operator prompt:** “Run training case F12-T with a missing telemetry signal. Ask me for the next diagnostic step, reveal the simulated evidence on request, then score my reasoning against the instructor rubric.”

**Governed tools:** `load_training_case` → `read_simulated_telemetry` → `run_training_power_flow` → `score_against_approved_rubric`. Training data and simulated controls remain isolated from production endpoints.

**Expected output:** a timed event narrative, visible tool-action log, learner decisions and a debrief showing evidence used, missed checks and unresolved questions. Label all displayed measurements “simulated.”

**Operator/instructor check:** the instructor validates the answer key and engineering findings; the agent supplies a structured debrief.

**Stop condition:** the session points to a production endpoint, the scenario lacks a validated answer key, or model scoring conflicts with simulator evidence. Pause for the instructor.

**Teaching connection:** controlled evaluation and human coordination (T11/T12/T14); no claim that the benchmarks certify operator training.

## Suggested slide treatment

Use one short role/authority slide, then an interaction slide with five reveal stages: **operator request → allowed tools → evidence packet → operator check → stop/escalate**. Animate the approved tool path and reveal the stop condition last. A photo establishes the control-room context; an adjacent evidence panel should show labeled mock records rather than invented live screenshots.

For a compact revision, devote full slides to handover, alarm triage and outage coordination, and combine contingency analysis with training on a two-column slide. Include an instructor note that all prompts and records are illustrative.

## Additional primary references for role boundaries

- **O01:** California ISO, “Our business,” live page reviewed October 17, 2026. https://www.caiso.com/about/our-business
- **O02:** GE Vernova, “Advanced Distribution Management System (ADMS) Software,” live product documentation reviewed October 17, 2026. https://www.gevernova.com/software/products/gridos/advanced-distribution-management-system
- **O03:** U.S. Department of Energy, “Solar Grid Planning and Operation Basics,” live educational page reviewed October 17, 2026. https://www.energy.gov/cmei/systems/solar-grid-planning-and-operation-basics

Existing C and T IDs resolve in research/source_map.json. O01–O03 are local memo IDs only; the builder registry was not edited.

