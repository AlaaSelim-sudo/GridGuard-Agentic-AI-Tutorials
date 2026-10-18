voltage_ac = show_case(suite, "voltage", "opendss")
voltage_ac_responses = language_table(suite, voltage_ac)
print("Final selected action:", voltage_ac["selected"]["candidate"] if voltage_ac["selected"] else "REVIEW")
print("Refinement operations used:", voltage_ac["used_operations"])
