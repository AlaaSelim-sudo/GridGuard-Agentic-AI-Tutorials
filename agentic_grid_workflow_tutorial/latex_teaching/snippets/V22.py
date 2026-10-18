decision = pool['selection']
print('Frozen:', pool['frozen'], '| selected-feedback training updates:', pool['training_updates'])
print('Bandit operation:', decision.operation_id, '| predicted reward:', round(decision.predicted_reward, 4))
print('Same canonical choice as majority:', decision.candidate_id == pool['vote_id'])
started = time.perf_counter()
selected_trials = lab.trial_saved_selection(pool)
timings['L4 new verification of archived choices'] = time.perf_counter() - started
display(selected_trials['table'])
