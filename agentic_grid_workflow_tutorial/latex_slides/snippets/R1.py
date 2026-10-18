restoration = {label: solve_restoration_milp(capacity)
               for label, capacity in [('normal', 220.), ('limited', 100.)]}
display(pd.DataFrame([{'case': label, **{key: row['milp'][key] for key in
                      ('served_kw', 'critical_served_kw', 'objective', 'mip_gap')},
                      'enumeration_agrees': row['agreement']}
                     for label, row in restoration.items()]))
display(pd.DataFrame(restoration['limited']['graph']['edges']))
