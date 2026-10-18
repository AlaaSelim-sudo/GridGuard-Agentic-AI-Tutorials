control_rows = [{'source': 'stealth estimate', **cyber['cases'][2]['control']},
                {'source': 'protected estimate', **cyber['trusted_recovery']['control']}]
table_rows(control_rows, ['source', 'status', 'flexible_injection_pu',
                         'objective', 'actual_violation_count'])
plot_trusted_control(cyber)
print('Protected-set residual degrees of freedom:', cyber['trusted_recovery']['chi_square']['degrees_of_freedom'])
