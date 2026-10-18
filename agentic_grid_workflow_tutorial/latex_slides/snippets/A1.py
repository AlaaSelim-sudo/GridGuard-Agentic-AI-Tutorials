study_case = continuous_casebook['P3_current_reserve']
shared = {'proposal': proposals[study_case.id], 'plan': plans[study_case.id]}
fixed = run_continuous_workflow(study_case, BACKEND, method='fixed', **shared)
if LIVE_LLM:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    llama = ContinuousLlama(ROOT / 'results' / ('continuous_llama_' + BACKEND + '_' + stamp + '.json'))
    agentic = run_continuous_workflow(study_case, BACKEND, method='agentic', llama=llama, **shared)
    agent_source = 'NEW local Llama calls on continuous SAC/MPC workflow'
else:
    saved = read_record('workshop_run_' + BACKEND + '.json')
    assert saved['schema'] == SCHEMA
    agentic = saved['agentic']
    assert agentic['case_definition'] == json.loads(json.dumps(contract['case']))
    agent_source = 'RECORDED continuous workflow; no new Llama calls'
print(agent_source)
table_rows([fixed, agentic], ['case', 'backend', 'method', 'status', 'candidate', 'llm_calls'])
