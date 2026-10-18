restoration_runs = [r for r in evidence['standard_runs'] if r['case'] == 'restoration']
for run in restoration_runs:
    print('\nRESTORATION:', run['supervisor'], run['status'])
    print('Numerical summary:', json.dumps(run['summary'], indent=2))
    display(pd.DataFrame(stage_rows(run)))
for call in evidence['calls']:
    if call['case'] == 'restoration':
        print(call['role'], call['choice'], '\nReturned reason:', call['reason'])
