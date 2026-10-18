from pathlib import Path
import json
from IPython.display import display, Markdown
import matplotlib.pyplot as plt
from src.proposal_workflow import run_suite
from src.proposal_display import (
    load_suite, contract_table, source_audit, select_run, show_case,
    candidate_table, stage_table, language_table, pair_summary_table,
    comparison_table, interpretation, stage_coverage_table, call_table,
    plot_comparison, plot_progress, show_stage_outputs, show_operator,
)
%matplotlib inline

RUN_LIVE = False
INCLUDE_QWEN_IN_LIVE_RUN = False
if RUN_LIVE:
    run_suite(include_qwen=INCLUDE_QWEN_IN_LIVE_RUN)

suite = load_suite()  # verifies response-to-journal and source-hash agreement
display(Markdown("**Mode:** " + ("new live suite, now inspecting its record" if RUN_LIVE else "saved replay")))
display(contract_table())
display(source_audit(suite)[["source", "matches"]])
print("Recorded:", suite["created_utc"])
print("Protocol:", suite["protocol"])
print("Protocol version:", suite.get("protocol_version", "see recorded protocol"))
print("Journal:", suite["journal_folder"])
