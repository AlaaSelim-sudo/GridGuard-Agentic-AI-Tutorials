cyber_runs = {}
for attack in ("cyber_isolated", "cyber_stealth"):
    run = show_case(suite, attack, "dc")
    cyber_runs[attack] = run
    aware = run["contract"]["awareness"]
    print(attack, "residual alarm:", aware["residual_test"]["alarm"])
    print("Awareness alarms:", aware["alarms"])
    print("Protected-data assumptions:", aware["scope"])
