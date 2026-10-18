CAPACITIES_KW = (40., 60., 80., 100., 120.)
started = time.perf_counter()
restoration = lab.restoration_sweep(CAPACITIES_KW)
timings['L6 fresh MILP sweep + independent enumeration'] = time.perf_counter() - started
display(restoration['table'].drop(columns='pickup'))
fig, axes = plt.subplots(1, 2, figsize=(10, 3.2))
for i, (method, group) in enumerate(restoration['table'].groupby('method', sort=False)):
    style = dict(marker='o' if i == 0 else 's', linestyle='None', markersize=7 if i == 0 else 10,
                 markerfacecolor='#1f77b4' if i == 0 else 'none', markeredgewidth=1.7)
    axes[0].plot(group.tie_capacity_kw, group.served_kw, label=method, **style)
    axes[1].plot(group.tie_capacity_kw, group.critical_kw, label=method, **style)
axes[0].set(ylabel='Total served (kW)', xlabel='Tie capacity (kW)')
axes[1].set(ylabel='Critical served (kW)', xlabel='Tie capacity (kW)')
axes[0].legend(fontsize=8); axes[1].set_ylim(0, 100)
fig.suptitle('Sampled capacity levels; coincident markers indicate equal outcomes', fontsize=10)
plt.tight_layout(); plt.show()
assert restoration['table'].MILP_matches_exhaustive_check.all()
