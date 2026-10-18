workflows = pd.DataFrame(evidence['workflows'])
display(workflows[['protocol', 'case', 'backend', 'route', 'status',
    'seconds', 'llm_calls', 'llm_client_s', 'other_in_interval_s', 'scope']].round(6))
preparation = []
for backend, run in evidence['voltage'].items():
    preparation.append({'backend': backend,
        'precomputed_MPC_s': run['continuous_plans']['P3_current_reserve']['seconds'],
        'actor_interval_s': run['continuous_proposals']['P3_current_reserve']['seconds']})
display(pd.DataFrame(preparation))
figure = plot_workflow_latency(evidence)
plt.show()
