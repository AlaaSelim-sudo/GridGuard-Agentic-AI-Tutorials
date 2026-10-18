        result = run_wls_demo()
        recovery = result['trusted_recovery']
        control = recovery['control']
        summary = {'trusted_state_estimate': recovery['estimate'], 'rank': recovery['rank'],
                   'residual_degrees_of_freedom': recovery['chi_square']['degrees_of_freedom'], 'control': control,
                   'scope': SCOPES[case]}
        accepted = bool(recovery['rank'] == 3 and control['status'] == 'PROPOSE' and control['actual_violation_count'] == 0)
