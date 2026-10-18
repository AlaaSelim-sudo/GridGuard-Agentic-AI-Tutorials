pool = lab.saved_pool('test_01')
display(pd.DataFrame(pool['responses'])[['model_id', 'operation_id', 'reason', 'seconds', 'source']])
display(pd.DataFrame([{'operation': ', '.join(c['operation_ids']),
    'votes': c['vote_count'], 'share': c['vote_share'], 'parameters': c['operation']['parameters']}
    for c in pool['pool']['candidates']]))
print('ARCHIVED ACTUAL LLM; original context:', pool['context']['id'])
print('Distinct physical candidates:', len(pool['pool']['candidates']))
print('Malformed/duplicate votes rejected:', len(pool['pool']['rejected']))
