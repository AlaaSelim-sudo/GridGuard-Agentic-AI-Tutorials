"""Post-run common-domain comparison and separately labeled full-feeder AC audit."""
from dataclasses import asdict
import json
import math
import time
from .stage_workflow import ROOT, StageCase, ElectricalModel, model_failures, compact, canonical_hash


def classify_failure_scope(reference, rating_fraction, bus_base_kv, line_endpoints, failures=()):
    """Localize AC voltage/current failures using the AC network's own bases.

    Voltage counts are energized buses, not individual phases. Current counts
    are energized lines using their maximum terminal/conductor current and the
    actual permitted rating fraction. Transformers are not classified as lines.
    This classification explains coverage; it does not change the AC verdict.
    """
    if (type(rating_fraction) not in (int, float) or not math.isfinite(rating_fraction)
            or not 0 < rating_fraction <= 1):
        raise ValueError('A valid permitted current fraction is required.')
    bases = {str(bus).lower(): kv for bus, kv in bus_base_kv.items()}
    endpoints = {str(name).lower(): (a.lower(), b.lower()) for name, a, b in line_endpoints}
    energized = {row['bus'].lower() for row in reference['buses']}
    violations = {f'{domain}_{kind}': [] for domain in ('mv', 'lv', 'unknown')
                  for kind in ('voltage_buses', 'overloaded_lines')}
    evaluated = {f'{domain}_{kind}': 0 for domain in ('mv', 'lv', 'unknown')
                 for kind in ('buses', 'lines')}
    invalid_rows = []
    def domain(bus):
        kv = bases.get(bus)
        return ('unknown' if type(kv) not in (int, float) or not math.isfinite(kv) or kv <= 0
                else 'mv' if kv > 1 else 'lv')
    for row in reference['buses']:
        bus = row['bus'].lower()
        level = domain(bus)
        evaluated[f'{level}_buses'] += 1
        if any(type(row.get(k)) not in (int, float) or not math.isfinite(row[k]) for k in ('vmin', 'vmax')):
            invalid_rows.append('bus:'+bus)
            continue
        if row['vmin'] < .95-1e-6 or row['vmax'] > 1.05+1e-6:
            violations[f'{level}_voltage_buses'].append(bus)
    skipped_unenergized = 0
    for row in reference['lines']:
        name = row['line'].lower()
        ends = endpoints.get(name)
        if ends is not None and not all(bus in energized for bus in ends):
            skipped_unenergized += 1
            continue
        levels = {domain(bus) for bus in ends} if ends else {'unknown'}
        level = next(iter(levels)) if len(levels) == 1 else 'unknown'
        evaluated[f'{level}_lines'] += 1
        if (type(row.get('normal_amps')) not in (int, float) or not math.isfinite(row['normal_amps'])
            or row['normal_amps'] <= 0 or type(row.get('max_current_amps')) not in (int, float)
            or not math.isfinite(row['max_current_amps']) or row['max_current_amps'] < 0):
            invalid_rows.append('line:'+name)
            continue
        utilization = 100*row['max_current_amps']/(row['normal_amps']*rating_fraction)
        if utilization > 100+1e-4:
            violations[f'{level}_overloaded_lines'].append(name)
    counts = {key: len(value) for key, value in violations.items()}
    mv = bool(counts['mv_voltage_buses'] or counts['mv_overloaded_lines'])
    lv = bool(counts['lv_voltage_buses'] or counts['lv_overloaded_lines'])
    unknown = bool(counts['unknown_voltage_buses'] or counts['unknown_overloaded_lines'])
    label = ('MV_AND_LV' if mv and lv else 'MV_ONLY' if mv else 'LV_ONLY' if lv else 'NONE')
    if unknown or invalid_rows:
        label += '_WITH_UNCLASSIFIED_EVIDENCE' if label != 'NONE' else 'UNCLASSIFIED_EVIDENCE'
    return {
        'voltage_current_failure_scope': label,
        'counts': counts, 'violating_elements': violations, 'evaluated': evaluated,
        'invalid_rows': invalid_rows, 'skipped_unenergized_lines': skipped_unenergized,
        'other_failure_reasons': [reason for reason in failures if reason not in ('voltage', 'thermal')],
        'rating_fraction': rating_fraction,
        'definition': 'MV: AC bus voltage base >1 kV; LV: base <=1 kV. Counts concern energized buses and lines. Current uses maximum terminal/conductor magnitude, not phase-aligned current errors.',
    }


def common_mv_errors(prediction, audit):
    """Align by electrical identity; expose omissions instead of hiding them."""
    def unique(rows, key, value):
        result = {}
        for row in rows:
            identity = key(row)
            numeric = row[value]
            if identity in result:
                raise ValueError('Duplicate electrical identity in comparison: '+str(identity))
            if type(numeric) not in (int, float) or not math.isfinite(numeric):
                raise ValueError('Nonfinite comparison evidence: '+str(identity))
            result[identity] = row
        return result
    phase_key = lambda row: (row['bus'].lower(), row['phase'])
    predicted_phases = unique(prediction.get('node_phase_voltages', []), phase_key, 'v_pu')
    actual_phases = unique(audit['node_phase_voltages'], phase_key, 'v_pu')
    predicted_lines = unique(prediction['lines'], lambda row: row['line'].lower(), 'max_current_amps')
    actual_lines = unique(audit['lines'], lambda row: row['line'].lower(), 'max_current_amps')
    phase_pairs = [{**row, 'ac_v_pu': actual_phases[key]['v_pu'],
                    'error_pu': row['v_pu']-actual_phases[key]['v_pu']}
                   for key, row in predicted_phases.items() if key in actual_phases]
    line_pairs = [{'line': row['line'], 'linear_current_amps': row['max_current_amps'],
                   'ac_current_amps': actual_lines[key]['max_current_amps'],
                   'error_amps': row['max_current_amps']-actual_lines[key]['max_current_amps']}
                  for key, row in predicted_lines.items() if key in actual_lines]
    ve = [abs(row['error_pu']) for row in phase_pairs]
    ie = [abs(row['error_amps']) for row in line_pairs]
    missing_phases = [f'{bus}.{phase}' for bus, phase in predicted_phases if (bus, phase) not in actual_phases]
    missing_lines = [line for line in predicted_lines if line not in actual_lines]
    error = {
        'common_mv_phase_count': len(phase_pairs),
        'predicted_mv_phase_count': len(predicted_phases),
        'unmatched_predicted_mv_phase_count': len(missing_phases),
        'unmatched_predicted_mv_phases': missing_phases,
        'voltage_mae_pu': sum(ve)/len(ve) if ve else None,
        'voltage_max_abs_error_pu': max(ve) if ve else None,
        'common_mv_line_count': len(line_pairs),
        'predicted_mv_line_count': len(predicted_lines),
        'unmatched_predicted_mv_line_count': len(missing_lines),
        'unmatched_predicted_mv_lines': missing_lines,
        'current_mae_amps': sum(ie)/len(ie) if ie else None,
        'current_max_abs_error_amps': max(ie) if ie else None,
        'alignment_complete_for_prediction': bool(phase_pairs and line_pairs) and not missing_phases and not missing_lines,
        'current_statistic': 'Maximum terminal/conductor current per aligned MV line; not per-phase current error.',
    }
    return error, phase_pairs, line_pairs


def audit_candidate(row):
    """Offline AC reference: does not repair or silently alter a linear proposal."""
    import opendssdirect as dss
    from .power_tools import verify_physics
    case = StageCase(**row['case_definition'])
    candidate = row['candidate']
    ac = ElectricalModel('opendss')
    started = time.perf_counter()
    reference = ac.solve(case, candidate)
    phase_values, bus_bases = [], {}
    for bus in dss.Circuit.AllBusNames():
        dss.Circuit.SetActiveBus(bus)
        bus_bases[bus.lower()] = float(dss.Bus.kVBase())
        if bus_bases[bus.lower()] <= 1:
            continue
        nodes = dss.Bus.Nodes()
        volts = dss.Bus.puVmagAngle()[::2]
        phase_values.extend({'bus': bus.lower(), 'phase': int(p), 'v_pu': float(v)}
                            for p, v in zip(nodes, volts) if p in (1, 2, 3) and v > 0)
    failures = verify_physics(reference, allow_unserved=case.task == 'restoration',
                              rating_fraction=case.rating_fraction)
    if case.task == 'restoration' and reference['served_kw'] <= .1:
        failures.append('no_service_restored')
    failure_scope = classify_failure_scope(reference, case.rating_fraction, bus_bases,
                                           reference['line_endpoints'], failures)
    return {'accepted': not failures, 'failures': failures, 'metrics': compact(reference, case),
            'seconds': time.perf_counter() - started, 'node_phase_voltages': phase_values,
            'lines': reference['lines'], 'failure_scope': failure_scope,
            'scope': 'Full-feeder AC reference check; no physical actuation.'}


def build_comparison(data=None):
    data = data or json.loads((ROOT / 'results/model_workflow.json').read_text())
    audits, summary = [], []
    for row in data['runs']:
        audit = audit_candidate(row) if row['candidate'] else None
        row['ac_audit'] = audit
        row['final_review_status'] = ('AC_CHECK_PASSED' if audit and audit['accepted'] else
                                      'MODEL_DISAGREEMENT_REVIEW' if audit else 'NO_RECOMMENDATION')
        # Acknowledgment must bind the audit as well as the proposed action.
        row['review_id'] = canonical_hash({'recommendation_id': row['recommendation_id'],
                                          'audit': None if audit is None else {
                                              'accepted': audit['accepted'], 'failures': audit['failures'],
                                              'metrics': audit['metrics'], 'failure_scope': audit['failure_scope']}})
        row['trace'][-1]['inputs']['review_id'] = row['review_id']
        error = {'common_mv_phase_count': 0, 'voltage_mae_pu': None, 'voltage_max_abs_error_pu': None,
                 'common_mv_line_count': 0, 'current_mae_amps': None, 'current_max_abs_error_amps': None}
        if row['backend'] == 'lindistflow3' and audit:
            error, pairs, line_pairs = common_mv_errors(row['prediction'], audit)
            audits.append({'case': row['case'], 'method': row['method'], 'candidate': row['candidate'],
                           'phase_pairs': pairs, 'line_pairs': line_pairs, **error})
        row['common_domain_error'] = error
        summary.append({'case': row['case'], 'backend': row['backend'], 'method': row['method'],
                        'model_status': row['status'], 'final_review_status': row['final_review_status'],
                        'pv_cap': row['candidate']['pv_cap'] if row['candidate'] else None,
                        'tie': row['candidate']['tie'] if row['candidate'] else None,
                        'shed_fraction': row['candidate']['shed_fraction'] if row['candidate'] else None,
                        'predicted_served_kw': row['metrics']['served_kw'] if row['metrics'] else None,
                        'predicted_vmin': row['metrics']['vmin'] if row['metrics'] else None,
                        'predicted_vmax': row['metrics']['vmax'] if row['metrics'] else None,
                        'predicted_allowed_current_pct': row['metrics']['allowed_current_utilization_pct'] if row['metrics'] else None,
                        'ac_vmin': audit['metrics']['vmin'] if audit else None,
                        'ac_vmax': audit['metrics']['vmax'] if audit else None,
                        'ac_allowed_current_pct': audit['metrics']['allowed_current_utilization_pct'] if audit else None,
                        'ac_failures': audit['failures'] if audit else [],
                        'ac_failure_scope': audit['failure_scope'] if audit else None,
                        'model_solves': row['model_solves'], 'llm_calls': row['llm_calls'],
                        'workflow_seconds': row['seconds'], 'separate_ac_audit_seconds': audit['seconds'] if audit else 0.,
                        **error})
    report = {'metadata': {'scope': 'Common MV phase voltages and aligned MV line currents only for prediction errors. Full-feeder AC checks reported separately.',
                            'timing': 'Single local fixed-order run; setup tables and offline reference audits excluded from per-workflow times.',
                            'no_repair': 'Reference failures remain visible; the AC audit does not repair a linear recommendation.'},
              'summary': summary, 'paired_predictions': audits}
    (ROOT / 'results/model_workflow_reviewed.json').write_text(json.dumps(data, indent=2, allow_nan=False))
    (ROOT / 'results/model_comparison.json').write_text(json.dumps(report, indent=2, allow_nan=False))
    return data, report


def plots(report=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    report = report or json.loads((ROOT / 'results/model_comparison.json').read_text())
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'axes.spines.top': False, 'axes.spines.right': False})
    out = ROOT / 'figures'
    rows = [r for r in report['summary'] if r['method'] == 'agentic']
    labels = list(dict.fromkeys(r['case'] for r in rows))
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.2))
    for offset, backend, color, label in [(-.18, 'opendss', '#087e83', 'OpenDSS'),
                                          (.18, 'lindistflow3', '#d1762b', 'LinDistFlow MV')]:
        subset = {r['case']: r for r in rows if r['backend'] == backend}
        values = [subset[k]['pv_cap'] if subset[k]['pv_cap'] is not None else 0 for k in labels]
        axs[0].bar(np.arange(len(labels)) + offset, values, .34, label=label, color=color)
        axs[1].bar(np.arange(len(labels)) + offset, [subset[k]['workflow_seconds'] for k in labels],
                   .34, label=label, color=color)
        for i, k in enumerate(labels):
            if subset[k]['pv_cap'] is None:
                axs[0].text(i + offset, 1.5, '—', ha='center', color=color)
            elif subset[k]['final_review_status'] != 'AC_CHECK_PASSED':
                axs[0].text(i + offset, values[i] + 1, '×', ha='center', color='#a22222', fontsize=14)
    for ax in axs:
        ax.set_xticks(range(len(labels)), labels)
        ax.set_xlabel('Same declared scenario')
        ax.grid(axis='y', alpha=.18)
        ax.set_axisbelow(True)
    axs[0].set_ylabel('Recommended PV cap (%)')
    axs[0].set_title('Action proposed by each model workflow')
    axs[1].set_ylabel('Workflow elapsed time (s)')
    axs[1].set_title('Includes Llama; excludes setup and AC audit')
    axs[0].legend(fontsize=9)
    fig.text(.07, .015, '— no recommendation; × failed the separate full-feeder AC check. A 0% cap can be a valid restoration action.', fontsize=9)
    fig.tight_layout(rect=[0, .05, 1, 1])
    for suffix in ('png', 'svg'):
        fig.savefig(out / ('dual_model_workflow.' + suffix), dpi=170)
    plt.close(fig)
    paired = [r for r in report['paired_predictions'] if r['method'] == 'agentic']
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.5))
    for row in paired:
        x = [r['ac_v_pu'] for r in row['phase_pairs']]
        y = [r['v_pu'] for r in row['phase_pairs']]
        axs[0].scatter(x, y, s=9, alpha=.4, label=row['case'])
    low, high = axs[0].get_xlim()
    axs[0].plot([low, high], [low, high], color='#3d5360', ls='--', lw=1)
    axs[0].set_xlabel('OpenDSS common MV voltage (pu)')
    axs[0].set_ylabel('LinDistFlow MV voltage (pu)')
    axs[0].set_title('Same action, same MV bus and phase')
    axs[0].legend(fontsize=8)
    axs[1].bar([r['case'] for r in paired], [r['voltage_max_abs_error_pu'] or 0 for r in paired], color='#087e83')
    axs[1].set_ylabel('Maximum absolute MV voltage error (pu)')
    axs[1].set_title('No LV or transformer-error claim')
    fig.tight_layout()
    for suffix in ('png', 'svg'):
        fig.savefig(out / ('dual_model_voltage_error.' + suffix), dpi=170)
    plt.close(fig)


if __name__ == '__main__':
    _, report = build_comparison()
    plots(report)
    print(json.dumps(report['summary'], indent=2))
