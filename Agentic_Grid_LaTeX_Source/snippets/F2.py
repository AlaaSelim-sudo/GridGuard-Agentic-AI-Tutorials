run_record = {'schema': SCHEMA, 'backend': BACKEND, 'created_utc': datetime.now(timezone.utc).isoformat(),
    'agent_source': agent_source, 'voltage': voltage, 'continuous_checks': checks,
    'continuous_plans': plans, 'continuous_proposals': proposals,
    'fixed': fixed, 'agentic': agentic, 'restoration': restoration,
    'feeder_restoration': feeder_restoration, 'cyber': cyber}
output = save_workshop_run(run_record)
print('Saved new continuous-workflow evidence:', output.name)
display(HTML('<a href="Workshop_Operator_Dashboard.html" target="_blank">Open the current operator review screen</a>'))
