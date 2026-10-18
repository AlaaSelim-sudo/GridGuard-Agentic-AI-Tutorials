    elif case == 'restoration':
        result = solve_restoration_milp(100.)
        summary = {k: result['milp'][k] for k in ('objective', 'served_kw', 'critical_served_kw', 'pickup', 'closed_edges', 'mip_gap')}
        summary['scope'] = SCOPES[case]
        accepted = bool(result['milp']['success'] and result['agreement'])
        checks = {'solver_success': result['milp']['success'], 'independent_enumeration_agreement': result['agreement'],
                  'scope': 'Discrete pickup and graph-flow constraints only; no AC voltage or protection check'}
