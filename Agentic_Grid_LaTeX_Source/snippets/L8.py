ATTACK_SCALES = (0., .25, .5, 1., 1.5)
started = time.perf_counter()
cyber = lab.cyber_sweep(ATTACK_SCALES)
timings['L8 fresh WLS attack sweep'] = time.perf_counter() - started
display(cyber['table'])
fig, axes = plt.subplots(1, 2, figsize=(10, 3.2))
for attack, group in cyber['table'].groupby('attack', sort=False):
    axes[0].plot(group.scale, group.J, 'o-', label=attack)
    axes[1].plot(group.scale, group.state_error_rad, 'o-', label=attack)
axes[0].axhline(cyber['table'].threshold.iloc[0], color='#b7502e', linestyle='--', label='99% threshold')
axes[0].set_yscale('symlog', linthresh=10)
axes[0].set_yticks([0, 5, 15, 50, 200, 600], labels=['0', '5', '15', '50', '200', '600'])
axes[0].annotate('Threshold = 15.09', xy=(1.5, 15.086), xytext=(.87, 22),
                 color='#b7502e', fontsize=8)
axes[0].set(xlabel='Attack scale', ylabel='WLS residual J (symlog scale)', ylim=(0, 700))
axes[1].set(xlabel='Attack scale', ylabel='Offline state error (rad)')
axes[0].legend(fontsize=8, loc='upper left'); axes[1].legend(fontsize=8)
plt.tight_layout(); plt.show()
