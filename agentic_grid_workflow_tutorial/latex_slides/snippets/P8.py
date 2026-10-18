display(stage_coverage_table(suite))
REVIEW_CASE, REVIEW_BACKEND = "restoration", "opendss"
review_run = select_run(suite, REVIEW_CASE, REVIEW_BACKEND)
show_stage_outputs(review_run)
operator_record = show_operator(review_run)
print("Acknowledged:", operator_record["operator"]["acknowledged"])
print("Dispatch authorized:", operator_record["operator"]["dispatch_authorized"])
print("Equipment operated:", operator_record["operator"]["equipment_operated"])
