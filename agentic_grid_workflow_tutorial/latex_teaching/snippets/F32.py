def route(s):
    if s["passed"]:
        return "report"
    return "repair" if s["attempts"] < s["max_repairs"] else "hold"
