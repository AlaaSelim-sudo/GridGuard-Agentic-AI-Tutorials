cyber = run_wls_demo()
display(pd.DataFrame([{'case': row['name'], 'state_error_rad': row['state_error_norm'],
                      **row['chi_square'], 'control_status': row['control']['status'],
                      'actual_toy_violations': row['control'].get('actual_violation_count')}
                     for row in cyber['cases']]))
print('Suspect measurement index:', cyber['isolated_removal']['removed_index'])
