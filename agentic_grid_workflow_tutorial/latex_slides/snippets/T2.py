for backend, run in evidence['voltage'].items():
    print('\nBACKEND:', backend)
    display(pd.DataFrame(stage_rows(run['agentic'])))
    print('Fixed / agentic:', run['fixed']['status'], '/', run['agentic']['status'])
    print('Same final candidate:', run['fixed']['candidate'] == run['agentic']['candidate'])
    print('Operator card:', json.dumps(run['agentic']['trace'][-1]['response'], indent=2))
