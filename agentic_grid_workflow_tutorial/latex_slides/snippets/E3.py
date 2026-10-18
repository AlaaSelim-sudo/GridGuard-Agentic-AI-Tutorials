display(response_table(CASE))
pool = canonical_pool(CASE)
display(pd.DataFrame([{'operation': ', '.join(c['operation_ids']),
    'votes': c['vote_count'], 'vote share': c['vote_share'],
    'control': c['operation']['parameters']['control']}
    for c in pool['candidates']]))
print('Invalid responses retained:', pool['rejected'])
