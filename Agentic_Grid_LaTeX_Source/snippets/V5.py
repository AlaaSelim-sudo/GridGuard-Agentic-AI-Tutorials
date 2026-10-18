checks = []
for key, case in continuous_casebook.items():
    raw = plant.solve(proposals[key]['candidate']['control'], case.forecast_loads[0], case.rating_fraction)
    first = plans[key]['candidate']
    mpc_point = None if first is None else plant.solve(first['control'], case.forecast_loads[0], case.rating_fraction)
    checks.append({'case': key, 'sac_point': point_summary(raw), 'sac_failures': verify_control(raw, case),
        'mpc_point': point_summary(mpc_point) if mpc_point else None,
        'mpc_failures': verify_control(mpc_point, case), 'mpc_horizon_feasible': plans[key].get('horizon_feasible', False)})
display(pd.DataFrame([{'case': r['case'], 'SAC_failed_checks': r['sac_failures'],
    'MPC_failed_checks': r['mpc_failures'], 'MPC_horizon_feasible': r['mpc_horizon_feasible']} for r in checks]))
plot_continuous_checks(checks, BACKEND)
