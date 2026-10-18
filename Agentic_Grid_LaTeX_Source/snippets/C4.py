cyber_agent = next(row for row in standard_stages['runs']
                  if row['case'] == 'cyber' and row['supervisor'] == 'agentic')
print('RECORDED WLS/recovery integration:', cyber_agent['status'])
show_trace(cyber_agent)
display(pd.DataFrame(cyber_comparison()))
