h06 = evidence['h06']
print('Operator request:', h06[0]['request'])
display(pd.DataFrame([{k: r[k] for k in ['method', 'intake_seconds',
    'runtime_seconds', 'machine_seconds', 'llm_calls', 'correct_automatic_completion']}
    for r in h06]))
for row in h06:
    print(row['method'], json.dumps(row['interpretation'], indent=2))
hybrid = next(r for r in h06 if r['llm_calls'] == 1)
print('Downstream status:', hybrid['runtime']['status'])
print('Actual Interpreter reason:', next(c['reason'] for c in evidence['calls'] if c['case'] == 'h06'))
