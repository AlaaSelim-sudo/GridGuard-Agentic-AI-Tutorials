LOAD_SCALE = 1.0
RATING_FRACTION = 0.80
started = time.perf_counter()
voltage = lab.voltage_lab(LOAD_SCALE, RATING_FRACTION)
timings['L2 fresh MPC + SAC + checks'] = time.perf_counter() - started
print(voltage['mode'])
display(voltage['table'])
fig, axes = plt.subplots(1, 2, figsize=(10, 3.2))
for row in voltage['evaluations']:
    v = np.asarray(row['evidence'].get('voltages_pu', []))
    axes[0].plot(np.sort(v), label=row['method'])
voltage['table'].plot.bar(x='method', y='max_allowed_current_pct', ax=axes[1], legend=False, color='#16817a')
axes[0].axhspan(.95, 1.05, color='#16817a', alpha=.08)
axes[0].set(xlabel='Voltage rank (each curve sorted separately)', ylabel='Voltage (p.u.)', title='Fresh voltage distributions')
axes[0].legend(); axes[1].axhline(100, color='#b7502e', linestyle='--')
axes[1].set(ylabel='Allowed-current utilization (%)', title='Feasibility precedes ranking', xlabel='')
axes[1].tick_params(axis='x', rotation=0)
plt.tight_layout(); plt.show()