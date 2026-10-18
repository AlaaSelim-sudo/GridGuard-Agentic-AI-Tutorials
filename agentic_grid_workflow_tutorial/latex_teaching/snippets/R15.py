from IPython.display import HTML
for case, backend in [('voltage', 'lindistflow3'), ('restoration', 'lindistflow3'), ('cyber_stealth', 'dc')]:
    full_trace = lab.archived_stage_table(lab.archived_stage_replies(case, backend))
    assert full_trace.stage.nunique() == 5
    display(HTML('<details open><summary>ARCHIVED ACTUAL: ' + case +
        ' — all five stages, every recorded event</summary>' +
        full_trace.drop(columns='role_group').to_html(index=False, escape=True) + '</details>'))
print('Selected returned fields are exact archive values; complete records: results/proposal_complete_workflow.json')
