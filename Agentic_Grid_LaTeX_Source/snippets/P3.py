voltage_mv = show_case(suite, "voltage", "lindistflow3")
display(Markdown("**Cross-model scope:** compare each agentic route with its own matched fixed baseline."))
display(pair_summary_table(suite, "voltage", "opendss"))
display(pair_summary_table(suite, "voltage", "lindistflow3"))
if suite.get("model_portability_example"):
    voltage_qwen = show_case(suite, "voltage", "lindistflow3", portability=True)
else:
    print("No optional Qwen run is included in this saved suite.")
