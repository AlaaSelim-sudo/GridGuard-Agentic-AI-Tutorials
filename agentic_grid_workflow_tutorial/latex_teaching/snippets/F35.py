from src.graph_workflow_lab import fixed_baseline
for name, args in cases.items():
    baseline = fixed_baseline(initial_state(*args), simulate, verify, repair, route, ready, hold)
    assert summary(baseline) == summary(results[name])
print("Direct Python baseline matches every command, outcome and trace: 3/3.")
