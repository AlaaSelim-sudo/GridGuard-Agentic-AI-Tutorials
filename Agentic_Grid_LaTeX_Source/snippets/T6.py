for run in evidence['standard_runs']:
    if run['case'] == 'cyber':
        print('\nCYBER:', run['supervisor'], run['status'])
        print('Numerical summary:', json.dumps(run['summary'], indent=2))
        display(pd.DataFrame(stage_rows(run)))
for call in evidence['calls']:
    if call['case'] == 'cyber':
        print(call['role'], call['choice'], '\nReturned reason:', call['reason'])
