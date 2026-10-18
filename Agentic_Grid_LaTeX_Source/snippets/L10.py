archived_reasons = []
for case, backend in [('voltage', 'lindistflow3'), ('restoration', 'lindistflow3'), ('cyber_stealth', 'dc')]:
    run = lab.archived_stage_replies(case, backend)
    for event in run['trace']:
        response = event.get('response', {})
        reply = response.get('language_response') if isinstance(response, dict) else None
        if reply:
            archived_reasons.append({'case': case, 'stage': event['stage'],
                'choice': reply.get('choice', reply.get('ranking')),
                'exact_public_reason': reply['reason'], 'recorded_call_s': reply['seconds']})
display(pd.DataFrame(archived_reasons))
display(pd.DataFrame([{'fresh_operation': key, 'this_run_seconds': value} for key, value in timings.items()]))
print('Recorded model latency and this-run calculation times are different measurement boundaries.')

# Every actual trace event, including deterministic simulation and verification.
from IPython.display import HTML
for case, backend in [('voltage', 'lindistflow3'), ('restoration', 'lindistflow3'), ('cyber_stealth', 'dc')]:
    full_trace = lab.archived_stage_table(lab.archived_stage_replies(case, backend))
    assert full_trace.stage.nunique() == 5
    display(HTML('<details open><summary>ARCHIVED ACTUAL: ' + case +
        ' — all five stages, every recorded event</summary>' +
        full_trace.drop(columns='role_group').to_html(index=False, escape=True) + '</details>'))
print('Selected returned fields are exact archive values; complete records: results/proposal_complete_workflow.json')
