policy = load_continuous_policy()
plans = {key: optimize_continuous_mpc(case, BACKEND) for key, case in continuous_casebook.items()}
proposals = {key: sac_proposal(case, policy) for key, case in continuous_casebook.items()}
display(pd.DataFrame([{'case': key, 'sac_control_a_b': proposals[key]['candidate']['control'],
    'mpc_control_sequence': plans[key]['control_sequence'], 'mpc_horizon_cost': plans[key]['objective'],
    'mpc_status': plans[key]['status']} for key in plans]))
print(proposals['P3_current_reserve']['training_scope'])
display(Image(filename=str(ROOT / 'figures/continuous_training.png')))
