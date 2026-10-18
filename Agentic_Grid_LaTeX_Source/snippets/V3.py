standard = read_record('standard_formulations.json')
comparison = []
for backend, result in standard['voltvar'].items():
    for evaluation in ('baseline', 'optimized', 'reference_full_ac_audit'):
        if evaluation in result:
            comparison.append({'backend': backend, 'evaluation': evaluation,
                               **{key: result[evaluation][key] for key in
                                  ('vmin', 'vmax', 'max_line_utilization_pct', 'accepted')}})
print('RECORDED results and separate full-AC audit:')
display(pd.DataFrame(comparison))
