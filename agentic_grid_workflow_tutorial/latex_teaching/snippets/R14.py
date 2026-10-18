rest_request = {'task': 'restoration', 'capacity_kw': CAPACITIES_KW[0],
                'critical_nodes': [2, 5], 'model': 'six_node_active_transport', 'revision': 1}
rest_candidate = {'pickup': rest_record['milp']['pickup'], 'closed_edges': rest_record['milp']['closed_edges']}
rest_evidence = lab.bind_evidence(rest_request, rest_candidate,
    {'objective': rest_record['milp']['objective'], 'enumeration_agrees': rest_record['agreement']})
new_rest_request = {**rest_request, 'capacity_kw': 20., 'revision': 2}
print('Original contract:', lab.bound_to(rest_request, rest_candidate, rest_evidence))
print('Changed rating with old evidence:', lab.bound_to(new_rest_request, rest_candidate, rest_evidence))
