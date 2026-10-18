"""Display helpers for the checkpoint workshop; no optimization or control logic."""
from pathlib import Path
import html
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, HTML, Image

ROOT = Path(__file__).resolve().parents[1]
TEAL, ORANGE, RED = '#007f83', '#b56624', '#a7353d'

def read_record(name):
    return json.loads((ROOT / 'results' / name).read_text(encoding='utf-8'))

def table_rows(rows, columns):
    display(pd.DataFrame([{k: row.get(k) for k in columns} for row in rows]))

def show_trace(run):
    display(pd.DataFrame([{k: step.get(k) for k in ('stage', 'method', 'status', 'response_source')}
                          for step in run['trace']]))
    for step in run['trace']:
        label = html.escape(step['stage'] + ' | ' + step.get('status', ''))
        response = html.escape(json.dumps(step.get('response'), indent=2, ensure_ascii=False))
        display(HTML('<details><summary>' + label + ': exact response</summary><pre>' + response + '</pre></details>'))

def _finish(fig, name):
    fig.tight_layout()
    path=ROOT / 'figures' / name
    fig.savefig(path, dpi=180, facecolor='white')
    # Explicit image display also works in automated kernels using the Agg backend.
    display(Image(filename=str(path)))
    plt.close(fig)

def plot_voltage(voltage):
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))
    for key, color in [('baseline', ORANGE), ('optimized', TEAL)]:
        axes[0].plot(np.sort(voltage[key]['voltages_pu']), color=color, label=key)
        axes[1].plot(np.sort(voltage[key]['current_pu']) * 100, color=color, label=key)
    for bound in (.95, 1.05):
        axes[0].axhline(bound, color=RED, ls='--', lw=1)
    axes[1].axhline(100, color=RED, ls='--', lw=1)
    axes[0].set(xlabel='Sorted modeled phase sample', ylabel='Voltage (p.u.)', title=voltage['scope'])
    axes[1].set(xlabel='Sorted modeled line sample', ylabel='Rated-current utilization (%)', title=voltage['backend'])
    for ax in axes:
        ax.legend()
    _finish(fig, 'workshop_voltage_' + voltage['backend'] + '.png')

def plot_dqn_mpc(checks, backend):
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.3))
    labels = [r['case'] for r in checks]
    x = np.arange(len(labels))
    axes[0].bar(x-.18, [r['dqn_cap'] for r in checks], .36, label='DQN proposal', color=ORANGE)
    axes[0].bar(x+.18, [r['mpc_cap'] if r['mpc_cap'] is not None else 0. for r in checks],
                .36, label='MPC first move', color=TEAL)
    for i,r in enumerate(checks):
        if r['mpc_cap'] is None:
            axes[0].annotate('infeasible', (i+.18, 0.), xytext=(0, 6),
                             textcoords='offset points', ha='center', rotation=90)
    axes[0].set(xticks=x, xticklabels=labels, ylabel='PV cap (%)', title='Same catalog; distinct proposal methods')
    axes[0].legend()
    for i, r in enumerate(checks):
        text = ('Fresh physics: ' + ('pass' if not r['physics_failures'] else ', '.join(r['physics_failures']))
                + '\nHorizon: ' + ('feasible' if r['feasible_horizon'] else 'infeasible')
                + '\nValue gap: ' + ('n/a' if r['value_gap'] is None else f"{r['value_gap']:.3f}"))
        axes[1].text(.03, .91-i*.48, r['case']+' | '+text, transform=axes[1].transAxes, va='top', fontsize=11)
    axes[1].axis('off')
    axes[1].set_title('Separate the three acceptance questions')
    _finish(fig, 'workshop_dqn_mpc_' + backend + '.png')

def plot_restoration(restoration):
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), gridspec_kw={'width_ratios':[1,1,1.4]})
    pos = {0:(0,1),1:(1,1),2:(2,1),3:(2,0),4:(1,0),5:(2.7,1.9)}
    for ax, (label, row) in zip(axes, restoration.items()):
        closed = row['milp']['closed_edges']
        for edge in row['graph']['edges']:
            ends = (edge.get('i', edge.get('from')), edge.get('j', edge.get('to')))
            # Graph schema uses u/v endpoint names.
            if ends[0] is None:
                ends = (edge['u'], edge['v'])
            xx, yy = zip(*(pos[n] for n in ends))
            ax.plot(xx, yy, color=TEAL if edge['name'] in closed else '#bac6cc',
                    lw=3 if edge['name'] in closed else 1.5, ls='-' if edge['name'] in closed else '--')
        for n, xy in pos.items():
            on = row['milp']['energized'][n]
            ax.scatter(*xy, s=450, color=TEAL if on else '#bac6cc', zorder=3)
            ax.text(*xy, str(n), ha='center', va='center', color='white', zorder=4)
        ax.set(title=label + ' tie', xlim=(-.4,3.4), ylim=(-.5,2.4)); ax.axis('off')
    loads = np.array(restoration['normal']['graph']['demand_kw'])[1:]
    x = np.arange(len(loads))
    for offset, (label,row), color in zip([-.18,.18],restoration.items(),[TEAL,ORANGE]):
        axes[2].bar(x+offset, loads*np.array(row['milp']['pickup'])[1:], .36, label=label,color=color)
    axes[2].set(xticks=x,xticklabels=['1','2*','3','4','5*'],xlabel='Node (* priority 10)',ylabel='Picked-up load (kW)')
    axes[2].legend()
    _finish(fig, 'workshop_restoration.png')

def plot_cyber(cyber):
    fig, axes = plt.subplots(1,2,figsize=(11,3.5))
    labels=['Nominal','Isolated corruption','Stealth Hc']; colors=[TEAL,ORANGE,RED]
    axes[0].bar(labels,[r['chi_square']['statistic'] for r in cyber['cases']],color=colors)
    axes[0].axhline(cyber['cases'][0]['chi_square']['threshold'],color='black',ls='--',label='1% nominal chi-square threshold')
    axes[0].set(ylabel='Weighted residual statistic',title='Does the residual alarm?'); axes[0].legend()
    axes[1].bar(labels,[r['state_error_norm'] for r in cyber['cases']],color=colors)
    axes[1].set(ylabel='State-error norm (radians)',title='Compare with the known synthetic truth')
    for ax in axes: ax.tick_params(axis='x',labelrotation=10)
    _finish(fig,'workshop_cyber.png')

def plot_trusted_control(cyber):
    fig,ax=plt.subplots(figsize=(10,3.4)); x=np.arange(4)
    for offset,label,row,color in [(-.18,'Stealth estimate',cyber['cases'][2]['control'],ORANGE),
                                  (.18,'Protected estimate',cyber['trusted_recovery']['control'],TEAL)]:
        ax.bar(x+offset,np.abs(row['actual_toy_model_flows_pu']),.36,label=label,color=color)
    ax.plot(x,cyber['trusted_recovery']['control']['line_limits_pu'],'o--',color=RED,label='Branch limit')
    ax.set(xticks=x,xticklabels=['01','12','23','03'],xlabel='Four-bus DC branch',ylabel='Absolute actual flow (p.u.)')
    ax.legend(ncol=3)
    _finish(fig,'workshop_trusted_control.png')


def plot_continuous_checks(checks, backend):
    """Actual first-action P/Q proposals and their fresh-model current checks."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.7))
    theta = np.linspace(-np.pi/2, np.pi/2, 200)
    axes[0].plot(np.cos(theta), np.sin(theta), '--', color='#aebeb6', label='Inverter circle')
    for i, row in enumerate(checks):
        for tool, key, marker, color in [('SAC', 'sac_point', 'o', ORANGE), ('MPC', 'mpc_point', 'x', TEAL)]:
            point = row.get(key)
            if not point:
                continue
            a,b = point['control']
            axes[0].scatter(a,b,marker=marker,color=color,s=65,label=tool if i==0 else None)
            axes[0].annotate(row['case'].split('_')[0],(a,b),xytext=(5,6 if tool=='SAC' else -13),textcoords='offset points',fontsize=8)
    axes[0].set(xlabel='Active participation a = p/S', ylabel='Reactive participation b = q/S',
                xlim=(-.02,1.05), ylim=(-.5,.5), title='Continuous controls: no cap catalog')
    axes[0].set_aspect('equal',adjustable='box');axes[0].legend(fontsize=8)
    x=np.arange(len(checks))
    for offset,key,label,color in [(-.18,'sac_point','SAC proposal',ORANGE),(.18,'mpc_point','MPC first action',TEAL)]:
        vals=[r[key]['max_allowed_current_pct'] if r.get(key) else np.nan for r in checks]
        axes[1].bar(x+offset,vals,.36,label=label,color=color)
    axes[1].axhline(100,color=RED,ls='--',lw=1,label='Allowed current')
    axes[1].set(xticks=x,xticklabels=[r['case'].split('_')[0] for r in checks],
                ylabel='Maximum current / allowed rating (%)', title=backend+' fresh first-action checks')
    axes[1].legend(fontsize=8)
    _finish(fig,'workshop_continuous_'+backend+'.png')
