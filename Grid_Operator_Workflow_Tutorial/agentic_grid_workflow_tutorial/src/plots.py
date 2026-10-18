"""Figures are calculated from saved measurements; labels state their units."""
import json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from .control_tools import ROOT, DATA, ac_table, CAPS, LOADS

TEAL, INK, ORANGE, RED = '#087e8b','#16324f','#de8c2d','#c6404a'

def finish(fig,name):
    out=ROOT/'figures';out.mkdir(exist_ok=True)
    fig.savefig(out/f'{name}.png',dpi=170,bbox_inches='tight',facecolor='white')
    fig.savefig(out/f'{name}.svg',bbox_inches='tight',facecolor='white')
    plt.close(fig)

def linear_example():
    """Separate balanced two-bus illustration, not the unbalanced feeder solver."""
    import opendssdirect as dss
    rows=[];Vll=12.47e3;R=.2;X=.3
    for length in [.25,.5,1,2,4,6]:
        dss.Basic.ClearAll()
        dss.Text.Command('New Circuit.example basekv=12.47 pu=1 phases=3 bus1=source mvasc3=1000000 mvasc1=1000000')
        dss.Text.Command(f'New Line.branch phases=3 bus1=source bus2=load r1={R} x1={X} r0={R} x0={X} c1=0 c0=0 units=km length={length}')
        dss.Text.Command('New Load.customer phases=3 bus1=load conn=wye kv=12.47 kw=3000 kvar=1000 model=1 vminpu=.8')
        dss.Text.Command('set voltagebases=[12.47]');dss.Text.Command('calcvoltagebases');dss.Solution.Solve()
        if not dss.Solution.Converged():raise RuntimeError('Illustrative circuit did not converge')
        dss.Circuit.SetActiveBus('load');actual=float(np.mean(dss.Bus.puVmagAngle()[::2]))
        approx=1-length*(R*3e6+X*1e6)/Vll**2
        rows.append({'length_km':length,'linear_pu':approx,'opendss_pu':actual,'error_pu':approx-actual})
    (ROOT/'results/linear_example.json').write_text(json.dumps(rows,indent=2))
    return rows

def make_figures(results=None):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,
                         'axes.spines.right':False,'axes.titleweight':'bold','figure.dpi':110})
    T=ac_table()
    if results is None:results=json.loads((ROOT/'results/labs.json').read_text())
    coords={}
    for line in (DATA/'Buscoords.dss').read_text().splitlines():
        fields=re.split(r'[,\s]+',line.strip())
        if len(fields)>=3:
            try:coords[fields[0].lower()]=(float(fields[1]),float(fields[2]))
            except ValueError:pass
    segments=[(coords[a],coords[b]) for _,a,b in T[3][0]['line_endpoints'] if a in coords and b in coords]
    fig,ax=plt.subplots(figsize=(9,5));ax.add_collection(LineCollection(segments,colors=TEAL,linewidths=.55,alpha=.7))
    ax.autoscale();ax.set_aspect(1/np.cos(np.deg2rad(36.12)))
    ax.set(xlabel='Longitude (degrees)',ylabel='Latitude (degrees)',title='One synthetic Greensboro feeder: udt8894')
    ax.ticklabel_format(useOffset=False);ax.text(.02,.02,'SMART-DS synthetic network • teaching overlays are not utility assets',transform=ax.transAxes,fontsize=9)
    finish(fig,'feeder')
    fig,axes=plt.subplots(1,2,figsize=(11,4.5))
    axes[0].plot(CAPS,[m['vmax'] for m in T[3]],'o-',color=TEAL,label='Maximum bus voltage')
    axes[0].plot(CAPS,[m['vmin'] for m in T[3]],'o-',color=INK,label='Minimum bus voltage')
    for limit in [.95,1.05]:axes[0].axhline(limit,ls='--',color=RED,lw=1)
    axes[0].set(xlabel='PV active-power cap (%)',ylabel='Voltage (pu)',title='Voltage alone does not determine feasibility');axes[0].legend(fontsize=9)
    axes[1].plot(CAPS,[m['max_line_pct'] for m in T[3]],'o-',color=ORANGE)
    axes[1].axhline(100,ls='--',color=RED);axes[1].set(xlabel='PV active-power cap (%)',ylabel='Maximum line loading (%)',title='Check current limits too')
    fig.tight_layout();finish(fig,'voltage_constraints')
    rows=linear_example();fig,axes=plt.subplots(1,2,figsize=(11,4))
    x=[r['length_km'] for r in rows]
    axes[0].plot(x,[r['opendss_pu'] for r in rows],'o-',color=TEAL,label='OpenDSS')
    axes[0].plot(x,[r['linear_pu'] for r in rows],'s--',color=ORANGE,label='First-order voltage drop')
    axes[0].set(xlabel='Line length (km)',ylabel='Receiving voltage (pu)',title='A separate balanced two-bus illustration');axes[0].legend()
    axes[1].plot(x,[1000*r['error_pu'] for r in rows],'o-',color=INK)
    axes[1].set(xlabel='Line length (km)',ylabel='Approximation error (millipu)',title='Approximation error grows with stress')
    fig.tight_layout();finish(fig,'linear_vs_ac')
    rows=results['mpc_rollout'];fig,axes=plt.subplots(3,1,figsize=(10,7),sharex=True)
    x=[r['minutes'] for r in rows]
    axes[0].step(x,[r['candidate']['pv_cap'] for r in rows],where='post',color=TEAL)
    axes[0].set(ylabel='PV cap (%)',title='Receding-horizon MPC: apply one action, then replan')
    axes[1].plot(x,[r['metrics']['max_line_pct'] for r in rows],'o-',color=ORANGE)
    axes[1].axhline(100,ls='--',color=RED);axes[1].set(ylabel='Line loading (%)')
    axes[2].plot(x,[r['metrics']['vmin'] for r in rows],'o-',label='Minimum',color=INK)
    axes[2].plot(x,[r['metrics']['vmax'] for r in rows],'o-',label='Maximum',color=TEAL)
    axes[2].axhline(.95,ls='--',color=RED);axes[2].axhline(1.05,ls='--',color=RED)
    axes[2].set(xlabel='Time (minutes)',ylabel='Voltage (pu)');axes[2].legend(ncol=2)
    for ax in axes:ax.axvspan(25,40,color=ORANGE,alpha=.12)
    fig.text(.14,.005,'Shaded interval: allowed line current is 80% of nominal. All actions freshly checked in OpenDSS.',fontsize=9)
    fig.tight_layout(rect=[0,.03,1,1]);finish(fig,'mpc_rollout')
    fig,axes=plt.subplots(1,2,figsize=(11,4.5))
    for ax,case in zip(axes,['R1','R2']):
        run=next(r for r in results['runs'] if r['case']==case and r['method']=='fixed')
        cat=next(t['result']['catalog'] for t in run['trace'] if t['role']=='Tool')
        labels=[r['candidate']['tie']+'\n'+str(round(r['candidate']['shed_fraction']*100))+'% shed' for r in cat]
        ax.bar(range(len(cat)),[r['metrics']['served_kw']/1000 for r in cat],color=[RED if r['failures'] else TEAL for r in cat])
        ax.set_xticks(range(len(cat)),labels,fontsize=8);ax.set(ylabel='Connected nominal demand (MW)',title=case+': catalog feasibility')
    fig.text(.13,.01,'Teal: passes the model checks. Red: rejected. Shedding is a fraction of noncritical load objects.',fontsize=9)
    fig.tight_layout(rect=[0,.03,1,1]);finish(fig,'restoration')
    selected=['V1','V2','R1','R2','C3'];fig,axes=plt.subplots(1,2,figsize=(11,4))
    for i,method in enumerate(['fixed','agentic']):
        runs=[next(r for r in results['runs'] if r['case']==c and r['method']==method) for c in selected]
        values=[(r['metrics']['pv_kw']/1000 if r['case'].startswith(('V','C')) else r['metrics']['served_kw']/1000) if r['metrics'] else np.nan for r in runs]
        axes[0].bar(np.arange(len(selected))+(i-.5)*.34,values,width=.34,label=method,color=[INK,TEAL][i])
        for j,r in enumerate(runs):
            if not r['metrics']:axes[0].text(j,0,'No recommendation',rotation=90,fontsize=8)
        axes[1].bar(np.arange(len(selected))+(i-.5)*.34,[r['seconds'] for r in runs],width=.34,label=method,color=[INK,TEAL][i])
    for ax in axes:ax.set_xticks(range(len(selected)),selected);ax.legend()
    axes[0].set(ylabel='PV MW (V/C); connected MW (R)',title='Compare outcomes under identical checks')
    axes[1].set(ylabel='Measured wall time (seconds)',title='LLM coordination has a runtime cost')
    fig.tight_layout();finish(fig,'comparison')
    hist=json.loads((ROOT/'models/training_seed_11.json').read_text())['history']
    fig,axes=plt.subplots(1,2,figsize=(10,3.5))
    axes[0].plot([h['step'] for h in hist],[h['mean_reward'] for h in hist],color=TEAL)
    axes[1].plot([h['step'] for h in hist],[h['unsafe_proposal_fraction'] for h in hist],color=ORANGE)
    axes[0].set(xlabel='Training step',ylabel='Mean reward / 600 steps',title='Reward-based learning')
    axes[1].set(xlabel='Training step',ylabel='Unsafe exploratory proposals / 600 steps',title='Training exploration is not deployment')
    fig.tight_layout();finish(fig,'training')
