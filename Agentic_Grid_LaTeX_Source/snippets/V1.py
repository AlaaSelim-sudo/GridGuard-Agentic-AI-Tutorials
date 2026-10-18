voltage = run_voltvar(BACKEND)
columns = ['p_actual_kw', 'q_actual_kvar', 'vmin', 'vmax',
           'max_line_utilization_pct', 'objective', 'accepted']
display(pd.DataFrame({name: {key: voltage[name][key] for key in columns}
                     for name in ('baseline', 'optimized')}).T)
display({'scope': voltage['scope'], 'validation': voltage['validation'],
         'remaining_violations': voltage['optimized']['violations']})
