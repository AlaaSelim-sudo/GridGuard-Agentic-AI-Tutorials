checked = selected_trials['evaluations']['frozen LinUCB']
handoff_request = {'case': asdict(selected_trials['case']), 'revision': 1}
handoff_candidate = checked['candidate']
handoff_evidence = lab.bind_evidence(handoff_request, handoff_candidate, checked['summary'])
full_scope = lab.operator_packet(handoff_request, handoff_candidate, handoff_evidence,
    checked['feasible'], scope='MV phases only', required_scope='full MV/LV')
mv_scope = lab.operator_packet(handoff_request, handoff_candidate, handoff_evidence,
    checked['feasible'], scope='MV phases only', required_scope='MV phases only')
wrong_id = lab.acknowledge(mv_scope, 'wrong-id', 'Student operator')
readback = lab.acknowledge(mv_scope, mv_scope['recommendation_id'], 'Student operator')
display(pd.DataFrame([{'request': 'full MV/LV', **full_scope},
                     {'request': 'explicit MV teaching scope', **readback}]))
assert full_scope['state'] == 'HOLD' and not full_scope['acknowledged']
assert wrong_id['acknowledgment_result'] == 'REJECTED'
assert readback['acknowledged'] and not readback['equipment_dispatch']