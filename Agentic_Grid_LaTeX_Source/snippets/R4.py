standard_stages = read_record('standard_agent_workflow.json')
restoration_agent = next(row for row in standard_stages['runs']
                         if row['case'] == 'restoration' and row['supervisor'] == 'agentic')
print('RECORDED standard-MILP integration:', restoration_agent['status'])
show_trace(restoration_agent)
