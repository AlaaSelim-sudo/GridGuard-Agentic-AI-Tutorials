"""Executable five-module proposal: propose, simulate, verify, refine and rank.

Numerical adapters own physics, constraints and scores. The language model can
choose only listed refinement operations and rank already verified candidate
IDs. An independently checked numerical ordering remains visible. This is an
advisory simulation, with no field command or automatic human acknowledgment.
"""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_VERSION = '1.1'
CORE_STAGES = ['Awareness Agent', 'Planning Agent', 'Simulation Agent',
               'Verification Agent', 'LLM Optimizer']


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def stage_contract():
    return [
        {'proposal_module': CORE_STAGES[0], 'method': 'Numerical telemetry/alarm summary and declared context',
         'output': 'State, topology, availability, forecast and model scope'},
        {'proposal_module': CORE_STAGES[1], 'method': 'Model-free policy and/or model-based candidate tools',
         'output': 'Explicit candidate controls with immutable operating limits'},
        {'proposal_module': CORE_STAGES[2], 'method': 'Fresh OpenDSS, three-phase LinDistFlow or declared DC model',
         'output': 'Candidate-specific numerical consequences and evidence identity'},
        {'proposal_module': CORE_STAGES[3], 'method': 'Independent numerical and policy checks',
         'output': 'PASS or rejection reasons, scoped to the model and trusted inputs'},
        {'proposal_module': CORE_STAGES[4], 'method': 'Llama critique, bounded repair/refinement and feasible ranking',
         'output': 'A revised candidate for rechecking and an auditable ranking'},
    ]


class ProposalLlama:
    """Actual local calls; full raw output, settings, tokens and clocks retained."""
    def __init__(self, journal, model='llama3.1:8b'):
        import requests
        self.requests, self.journal, self.model = requests, Path(journal), model
        self.calls = []

    def ask(self, role, context, choices, ranking=False):
        if not choices or len(set(choices)) != len(choices):
            raise ValueError('Unique bounded choices are required')
        field = 'ranking' if ranking else 'choice'
        selection = ({'type': 'array', 'items': {'type': 'string', 'enum': choices},
                      'minItems': len(choices), 'maxItems': len(choices), 'uniqueItems': True}
                     if ranking else {'type': 'string', 'enum': choices})
        schema = {'type': 'object', 'properties': {field: selection, 'reason': {'type': 'string'}},
                  'required': [field, 'reason'], 'additionalProperties': False}
        system = (
            'You are the named role in a grid-operator teaching simulation. Numerical tools compute '
            'the controls and check them. Your public reason must cite supplied evidence briefly. '
            'A refinement choice requests a NEW SIMULATION, never approves equipment operation. '
            'Never change hard limits, model scope, quarantined equipment or measurement trust. '
            'The objective is minimized among verified candidates. A failed candidate can be '
            'repaired with a listed numerical tool; a feasible candidate can be refined. '
            'For Planning, GENERATE_CANDIDATES requests the stated bounded numerical tools; their '
            'outputs will still need fresh simulation and verification. For Optimization choose '
            'one listed unused operation whose described effect addresses failures or improves '
            'the stated cost. Selecting an operation immediately requests its fresh simulation and verification; '
            'you do not wait for a separate simulation request. KEEP_INCUMBENT stops search and proceeds to '
            'ranking, without asserting a global optimum. Never describe a feasible candidate as failed. '
            'For Ranking return ALL supplied feasible IDs exactly once, best to worst according '
            'to the displayed numerical cost. Do not invent IDs or rank rejected candidates. '
            'Return only schema-valid JSON with a concise reason, not a private reasoning trace.')
        payload = {'model': self.model, 'messages': [{'role': 'system', 'content': system},
                    {'role': 'user', 'content': json.dumps({'role': role, **context}, allow_nan=False)}],
                   'format': schema, 'stream': False, 'keep_alive': '30m',
                   'options': {'temperature': 0, 'seed': 29, 'num_ctx': 8192, 'num_predict': 260}}
        record = {'role': role, 'utc': datetime.now(timezone.utc).isoformat(), 'payload': payload}
        tick = time.perf_counter()
        try:
            response = self.requests.post('http://127.0.0.1:11434/api/chat', json=payload, timeout=120)
            response.raise_for_status()
            record['raw_response'] = raw = response.json()
            reply = json.loads(raw['message']['content'])
            if set(reply) != {field, 'reason'} or not isinstance(reply['reason'], str) or not reply['reason'].strip():
                raise ValueError('Response shape or reason is invalid')
            if ranking:
                order = reply['ranking']
                if not isinstance(order, list) or any(not isinstance(v, str) for v in order) or len(order) != len(choices) or set(order) != set(choices):
                    raise ValueError('Ranking must be a permutation of verified IDs')
            elif reply['choice'] not in choices:
                raise ValueError('Choice is outside the permitted operation set')
            record['response'] = reply
            record['source'] = 'actual_local_llm'
        except Exception as error:
            record['error'] = f'{type(error).__name__}: {error}'
            record['response'] = {field: [] if ranking else 'REVIEW',
                                  'reason': 'Model call or schema failed; inspect the retained journal.'}
            record['source'] = 'local_failure_fallback'
        record['seconds'] = time.perf_counter() - tick
        record['call_id'] = len(self.calls) + 1
        self.calls.append(record)
        self.journal.parent.mkdir(parents=True, exist_ok=True)
        self.journal.write_text(json.dumps(self.calls, indent=2, allow_nan=False), encoding='utf-8')
        return {**record['response'], 'call_id': record['call_id'], 'seconds': record['seconds'],
                'source': record['source'], 'error': record.get('error')}


def _rank(evaluations):
    return sorted((r for r in evaluations if not r['failures']), key=lambda r: (r['score'], r['id']))


def _public(row):
    view = deepcopy({k: row[k] for k in ('id', 'candidate', 'failures', 'score', 'summary', 'candidate_hash', 'evidence_hash')})
    # The authored DC truth oracle is for offline assessment, never model input.
    view['summary'].pop('offline_truth_audit', None)
    return view


def run_proposal_case(case, backend, supervisor='fixed', client=None, refinement_budget=2):
    from .proposal_case_tools import make_adapter
    if supervisor not in ('fixed', 'agentic') or (supervisor == 'agentic' and client is None):
        raise ValueError('Agentic execution requires an actual local model client')
    if type(refinement_budget) is not int or not 0 <= refinement_budget <= 2:
        raise ValueError('This lesson permits at most two refinement evaluations')
    adapter = make_adapter(case, backend)
    trace, evaluations, progress, used_operations = [], [], [], []
    started, first_call = time.perf_counter(), len(client.calls) if client else 0
    stage_index = 0

    def stage(name, method, response, status, elapsed, **extra):
        nonlocal stage_index
        stage_index += 1
        trace.append({'event': stage_index, 'stage': name, 'method': method, 'status': status,
                      'seconds': elapsed, 'response': deepcopy(response), **extra})

    tick = time.perf_counter()
    awareness = adapter.awareness()
    contract = {'case': case, 'backend': backend, 'scope': adapter.scope,
                'objective': adapter.objective, 'refinement_budget': refinement_budget,
                'authority': 'Advisory simulation; human acknowledgment is separate from dispatch',
                'awareness': awareness}
    contract_id = canonical_hash(contract)
    stage(CORE_STAGES[0], 'Fuse synthetic numerical telemetry and declared context',
          contract, 'OBSERVED', time.perf_counter() - tick)

    tick = time.perf_counter()
    seeds = adapter.plan()
    if not isinstance(seeds, list) or len(seeds) != 2:
        raise ValueError('The matched protocol requires two initial candidates')
    planning_context = {'contract': contract, 'candidate_tools': seeds,
                        'meaning': 'Request both initial simulations; no candidate has been approved.'}
    decision = ({'choice': 'GENERATE_CANDIDATES', 'reason': 'Fixed use of the same two numerical proposals',
                 'source': 'deterministic', 'seconds': 0.} if supervisor == 'fixed' else
                client.ask('Planning Agent', planning_context, ['GENERATE_CANDIDATES', 'REVIEW']))
    stage(CORE_STAGES[1], 'Declared candidate tools with bounded language or fixed routing',
          {'candidates': seeds, 'language_response': decision, 'setup': deepcopy(getattr(adapter, 'setup', {}))},
          'PROPOSED' if decision['choice'] == 'GENERATE_CANDIDATES' else 'REVIEW', time.perf_counter() - tick)

    def evaluate(candidate, phase):
        candidate = deepcopy(candidate)
        identity = canonical_hash({'contract_id': contract_id, 'candidate': candidate})
        tick = time.perf_counter()
        try:
            evidence = adapter.simulate(candidate)
            if identity != canonical_hash({'contract_id': contract_id, 'candidate': candidate}):
                raise ValueError('Numerical adapter mutated the candidate')
            evidence_hash = canonical_hash(evidence)
            summary = adapter.summary(candidate, evidence)
            error = None
        except Exception as failure:
            evidence = {'error': f'{type(failure).__name__}: {failure}'}
            evidence_hash, summary, error = canonical_hash(evidence), evidence, evidence['error']
        identifier = f'E{len(evaluations)+1:02d}'
        stage(CORE_STAGES[2], 'Fresh ' + backend + ' candidate evaluation',
              {'candidate_id': identifier, 'candidate_hash': identity, 'evidence_hash': evidence_hash,
               'candidate': candidate, 'metrics': summary, 'phase': phase},
              'FAILED' if error else 'EVALUATED', time.perf_counter() - tick)
        tick = time.perf_counter()
        try:
            failures = ['model_evaluation_failure'] if error else list(adapter.verify(candidate, evidence))
            if evidence_hash != canonical_hash(evidence):
                failures.append('verification_mutated_evidence')
            raw_score = adapter.score(candidate, evidence) if not failures else None
            score = float(raw_score) if raw_score is not None and not isinstance(raw_score, bool) else None
            if not failures and (score is None or not math.isfinite(score)):
                failures.append('nonfinite_score'); score = None
        except Exception as failure:
            failures, score = ['verification_failure:' + type(failure).__name__], None
        try:
            if identity != canonical_hash({'contract_id': contract_id, 'candidate': candidate}):
                failures.append('verification_mutated_candidate')
            if evidence_hash != canonical_hash(evidence):
                failures.append('verification_mutated_evidence')
            if contract_id != canonical_hash(contract):
                failures.append('verification_mutated_contract')
        except (ValueError, TypeError, OverflowError):
            failures.append('invalid_postverification_identity')
        failures = sorted(set(failures))
        if failures:
            score = None
        stage(CORE_STAGES[3], 'Independent engineering and policy gate',
              {'candidate_id': identifier, 'contract_id': contract_id, 'candidate_hash': identity,
               'evidence_hash': evidence_hash, 'failures': failures, 'score': score,
               'rank_eligible': not failures, 'scope': adapter.scope},
              'REJECT' if failures else 'PASS', time.perf_counter() - tick)
        row = {'id': identifier, 'phase': phase, 'candidate': candidate, 'evidence': evidence,
               'candidate_hash': identity, 'evidence_hash': evidence_hash, 'summary': summary,
               'failures': failures, 'score': score}
        evaluations.append(row)
        ranked = _rank(evaluations)
        progress.append({'evaluated': len(evaluations), 'phase': phase,
                         'best_cost': ranked[0]['score'] if ranked else None,
                         'best_id': ranked[0]['id'] if ranked else None})
        return row

    held = decision['choice'] != 'GENERATE_CANDIDATES'
    if not held:
        for candidate in seeds:
            evaluate(candidate, 'initial')
        for iteration in range(refinement_budget):
            offered = {k: v for k, v in adapter.operations(evaluations).items() if k not in used_operations}
            if not offered:
                break
            tick = time.perf_counter()
            incumbent = _rank(evaluations)[0] if _rank(evaluations) else None
            context = {'case': case, 'backend': backend, 'scope': adapter.scope,
                       'objective': adapter.objective, 'iteration': iteration + 1,
                       'remaining_evaluations': refinement_budget - iteration,
                       'evaluated_candidates': [{'id': r['id'], 'action': r['candidate'],
                          'gate': 'REJECT' if r['failures'] else 'PASS',
                          'failures': r['failures'], 'cost': r['score']} for r in evaluations],
                       'lowest_cost_passed_candidate': ({'id': incumbent['id'], 'cost': incumbent['score']}
                                                        if incumbent else None),
                       'permitted_refinements': offered,
                       'operating_rule': 'Every listed operation is available now. Selecting it requests a new simulation automatically. All engineering limits remain fixed.',
                       'instruction': 'Name a supplied failure or cost in your concise public critique, then select a listed operation. The protocol requires one refinement trial when tools are available; later rounds may KEEP_INCUMBENT and proceed to ranking.'}
            if supervisor == 'fixed':
                operation = adapter.fixed_choice(evaluations, offered)
                reply = {'choice': operation, 'reason': 'Deterministic search using the same numerical methods and budget',
                         'source': 'deterministic', 'seconds': 0.}
            else:
                reply = client.ask('LLM Optimizer: critique and refine', context,
                                   list(offered) + (['KEEP_INCUMBENT'] if iteration else []))
            operation = reply['choice']
            if operation not in offered and operation not in ('KEEP_INCUMBENT', 'REVIEW'):
                raise ValueError('Supervisor selected an unknown refinement')
            stage(CORE_STAGES[4], 'Verifier-guided critique, repair and local candidate refinement',
                  {'phase': 'critique_refine', 'iteration': iteration + 1, 'offered_operations': offered,
                   'language_response': reply, 'incumbent': _public(_rank(evaluations)[0]) if _rank(evaluations) else None},
                  'REFINE' if operation in offered else operation, time.perf_counter() - tick)
            if operation == 'REVIEW':
                held = True; break
            if operation == 'KEEP_INCUMBENT':
                break
            used_operations.append(operation)
            try:
                candidate = adapter.propose(operation, evaluations)
            except Exception as failure:
                stage(CORE_STAGES[4], 'Bounded numerical refinement tool',
                      {'operation': operation, 'error': f'{type(failure).__name__}: {failure}'},
                      'REVIEW', 0.)
                held = True; break
            evaluate(candidate, 'refinement_' + str(iteration + 1))

    numerical_order = _rank(evaluations)
    language_order = None
    if numerical_order and not held:
        tick = time.perf_counter()
        ids = [r['id'] for r in numerical_order]
        ranking_context = {'objective': adapter.objective, 'smaller_is_better': True,
                           'verified_candidates': [_public(r) for r in numerical_order],
                           'scope': adapter.scope, 'rule': 'Return every supplied feasible ID in ascending cost order.'}
        ranking = ({'ranking': ids, 'reason': 'Deterministic ascending numerical cost, stable ID tie break',
                    'source': 'deterministic', 'seconds': 0.} if supervisor == 'fixed' else
                   client.ask('LLM Optimizer: feasible ranking', ranking_context, ids, ranking=True))
        language_order = ranking['ranking']
        valid_ranking = not ranking.get('error') and sorted(language_order) == sorted(ids)
        agrees = valid_ranking and all(next(r['score'] for r in numerical_order if r['id'] == a) <=
                     next(r['score'] for r in numerical_order if r['id'] == b) + 1e-9
                     for a, b in zip(language_order, language_order[1:]))
        stage(CORE_STAGES[4], 'Best-of-evaluated feasible set with an explicit numerical ranking guard',
              {'phase': 'ranking', 'language_response': ranking, 'numerical_order': ids,
               'language_order_agrees_with_cost': agrees,
               'selection_rule': 'Minimum verified numerical cost; language order is visible and cannot override cost or feasibility.'},
              'RANKED' if valid_ranking else 'REVIEW', time.perf_counter() - tick)
        held = not valid_ranking
    elif not any(s['stage'] == CORE_STAGES[4] for s in trace):
        stage(CORE_STAGES[4], 'No candidate can enter refinement/ranking',
              {'reason': 'Planning stopped or no candidates were evaluated'}, 'NOT_RUN', 0.)

    best = numerical_order[0] if numerical_order else None
    final = evaluate(best['candidate'], 'final_independent_recheck') if best and not held else None
    if final and final['failures']:
        held = True
    status = 'MODEL_RECOMMEND' if final and not held else 'REVIEW'
    # Ranking excludes the duplicate final recheck, preserving the evaluated search set.
    ranked_actions = [_public(r) for r in numerical_order]
    result = {'schema': 'proposal_complete_v1', 'protocol_version': PROTOCOL_VERSION,
              'case': case, 'backend': backend,
              'supervisor': supervisor, 'model': client.model if client else None,
              'created_utc': datetime.now(timezone.utc).isoformat(),
              'status': status, 'scope': adapter.scope, 'objective': adapter.objective,
              'contract': contract, 'contract_id': contract_id,
              'evaluations': evaluations, 'trace': trace, 'progress': progress,
              'ranked_actions': ranked_actions, 'language_ranking': language_order,
              'selected': _public(final) if status == 'MODEL_RECOMMEND' else None,
              'used_operations': used_operations, 'refinement_budget': refinement_budget,
              'counts': {'initial': sum(r['phase'] == 'initial' for r in evaluations),
                         'refinement': sum(r['phase'].startswith('refinement_') for r in evaluations),
                         'final_recheck': sum(r['phase'] == 'final_independent_recheck' for r in evaluations)},
              'setup': deepcopy(getattr(adapter, 'setup', {})),
              'core_stage_coverage': {name: any(s['stage'] == name and s['status'] != 'NOT_RUN' for s in trace) for name in CORE_STAGES},
              'operator': {'acknowledged': False, 'dispatch_authorized': False, 'equipment_operated': False,
                           'readback': ['Selected action', 'Limits and model scope', 'Rejected alternatives', 'Remaining operating authority']}}
    result['llm_calls'] = len(client.calls) - first_call if client else 0
    result['seconds'] = time.perf_counter() - started
    result['timing_scope'] = 'Includes awareness, candidate preparation, simulation, verification, refinement and language calls; excludes adapter construction/imports and prior training. One observed run, not a latency benchmark.'
    result['recommendation_id'] = canonical_hash({'contract_id': contract_id, 'status': status,
                                                'ranked_actions': ranked_actions, 'selected': result['selected']})
    return result


def run_suite(include_qwen=True):
    folder = ROOT / 'results' / ('proposal_run_' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:6])
    folder.mkdir(parents=True)
    client = ProposalLlama(folder / 'llama_calls.json')
    settings = [('voltage', 'opendss'), ('voltage', 'lindistflow3'),
                ('restoration', 'opendss'), ('restoration', 'lindistflow3'),
                ('cyber_isolated', 'dc'), ('cyber_stealth', 'dc')]
    result = {'schema': 'proposal_suite_v1', 'protocol_version': PROTOCOL_VERSION,
              'created_utc': datetime.now(timezone.utc).isoformat(),
              'protocol': 'Authored development demonstration; fixed then Llama on each case, same tools and maximum search budget. One observed run per setting, no statistical superiority claim.',
              'journal_folder': folder.relative_to(ROOT).as_posix(), 'runs': [],
              'source_sha256': {name: hashlib.sha256((ROOT / 'src' / name).read_bytes()).hexdigest()
                                for name in ('proposal_workflow.py', 'proposal_case_tools.py')}}
    for case, backend in settings:
        for route in ('fixed', 'agentic'):
            print(case, backend, route, flush=True)
            run = run_proposal_case(case, backend, route, client if route == 'agentic' else None)
            result['runs'].append(run)
            (folder / 'workflow.json').write_text(json.dumps(result, indent=2, allow_nan=False), encoding='utf-8')
    if include_qwen:
        print('Optional model portability: Qwen / voltage / lindistflow3', flush=True)
        qwen = ProposalLlama(folder / 'qwen_calls.json', 'qwen2.5:7b-instruct')
        result['model_portability_example'] = run_proposal_case('voltage', 'lindistflow3', 'agentic', qwen)
    (folder / 'workflow.json').write_text(json.dumps(result, indent=2, allow_nan=False), encoding='utf-8')
    (ROOT / 'results/proposal_complete_workflow.json').write_text(json.dumps(result, indent=2, allow_nan=False), encoding='utf-8')
    return result


if __name__ == '__main__':
    run_suite()
