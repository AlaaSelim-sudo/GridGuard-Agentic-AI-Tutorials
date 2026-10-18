restoration_ac = show_case(suite, "restoration", "opendss")
print("Retained numerical order:", [r["id"] for r in restoration_ac["ranked_actions"]])
print("Llama returned order:", restoration_ac["language_ranking"])
print("Numerical cost guard selects the best verified action even if wording or ordering is imperfect.")
