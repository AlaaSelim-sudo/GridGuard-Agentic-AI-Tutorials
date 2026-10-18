cases = {"passing": (0.25, 0.80, 2), "repair": (0.75, 0.80, 2),
         "exhausted": (0.90, 0.50, 1)}
results, elapsed_ms = {}, {}
for name, args in cases.items():
    started = time.perf_counter()
    results[name] = app.invoke(initial_state(*args), {"recursion_limit": 40})
    elapsed_ms[name] = 1000 * (time.perf_counter() - started)
    print(name, json.dumps(summary(results[name])), f"{elapsed_ms[name]:.3f} ms")

assert [results[k]["status"] for k in cases] == ["TOY_READY", "TOY_READY", "TOY_HOLD"]
assert [results[k]["attempts"] for k in cases] == [0, 1, 1]
assert results["repair"]["trace"] == ["simulate: 1.000", "verify: False",
    "repair: -0.25", "simulate: 0.800", "verify: True", "report: ready"]

from src.graph_workflow_lab import fixed_baseline
for name, args in cases.items():
    baseline = fixed_baseline(initial_state(*args), simulate, verify, repair, route, ready, hold)
    assert summary(baseline) == summary(results[name])
print("Direct Python baseline matches every command, outcome and trace: 3/3.")