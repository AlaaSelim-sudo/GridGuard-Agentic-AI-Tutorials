def build_graph(report_node=ready, checkpointer=None):
    builder = StateGraph(TrialState)
    nodes = {"simulate": simulate, "verify": verify, "repair": repair,
             "report": report_node, "hold": hold}
    for name, function in nodes.items():
        builder.add_node(name, function)
    builder.add_edge(START, "simulate")
    builder.add_edge("simulate", "verify")
    builder.add_conditional_edges("verify", route,
        {"report": "report", "repair": "repair", "hold": "hold"})
    builder.add_edge("repair", "simulate")
    builder.add_edge("report", END)
    builder.add_edge("hold", END)
    return builder.compile(checkpointer=checkpointer)

app = build_graph()
print("Compiled nodes:", sorted(app.get_graph().nodes))