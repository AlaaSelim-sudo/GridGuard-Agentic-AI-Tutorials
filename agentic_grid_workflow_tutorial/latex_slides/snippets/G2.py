def simulate(s):
    value = 0.4 + 0.8 * s["command"]
    return {"current": value, "trace": [f"simulate: {value:.3f}"]}

def verify(s):
    ok = s["current"] <= s["limit"] + 1e-12
    return {"passed": ok, "trace": [f"verify: {ok}"]}

def repair(s):
    return {"command": max(0., s["command"] - 0.25),
            "attempts": s["attempts"] + 1, "trace": ["repair: -0.25"]}

def ready(s):
    return {"status": "TOY_READY", "trace": ["report: ready"]}

def hold(s):
    return {"status": "TOY_HOLD", "trace": ["hold: budget exhausted"]}

def route(s):
    if s["passed"]:
        return "report"
    return "repair" if s["attempts"] < s["max_repairs"] else "hold"
