restoration_mv = show_case(suite, "restoration", "lindistflow3")
for run in (restoration_ac, restoration_mv):
    selected = run["selected"]
    print(run["backend"], "scope:", run["scope"])
    print("Selected metrics:", json.dumps(selected["summary"], indent=2) if selected else "REVIEW")
