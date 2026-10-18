learning = analysis['protocol']
history = next(h for h in analysis['training'] if h['seed'] == learning['primary_seed'])
first = history['records'][0]
context = contexts[first['context_id']]
learner = LinUCB(learning['operation_ids'], learning['alpha'], learning['regularization'])
choice = learner.select(context['pretrial_features'], canonical_pool(context['id'])['candidates'])
# The selected simulator outcome is opened only after selection.
trial = read(f"counterfactuals/{context['id']}_{choice.operation_id}.json")['planning_model_trial']
reward = reward_from_selected_feedback(context, trial, learning)
learner.update(choice, reward)
assert choice.operation_id == first['operation_id'] and abs(reward-first['selected_reward']) < 1e-12
frozen = LinUCB.load(DATA/history['checkpoint'])
print('Reproduced first update:', choice.operation_id, 'reward:', reward)
print('Delivered policy updates:', frozen.updates, 'frozen:', frozen.frozen)
display(pd.DataFrame(history['records']).head(4)[['context_id','operation_id','selected_reward','updates_after']])
fig, ax = plt.subplots(figsize=(8.6,3.3), constrained_layout=True)
for h in analysis['training']:
    ax.plot(range(1,len(h['records'])+1), [r['selected_reward'] for r in h['records']],
            marker='.', label=f"Training order {h['seed']}", alpha=.8)
ax.set(xlabel='Selected-feedback update', ylabel='Recorded reward', title='Small training replay; each order sees 24 scenarios')
ax.grid(alpha=.2); ax.legend(fontsize=8)
plt.show()
