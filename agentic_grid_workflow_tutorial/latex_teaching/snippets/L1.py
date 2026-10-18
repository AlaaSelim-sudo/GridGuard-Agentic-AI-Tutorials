request = lab.validate_request(dict(task='voltage', backend='lindistflow3',
    load_scale=1.0, rating_fraction=0.80, revision=1))
candidate = {'control': [0.25, 0.0]}
evidence = lab.bind_evidence(request, candidate, {'example_only': True, 'passed': True})
changed_request = {**request, 'load_scale': 1.10, 'revision': 2}
guard = pd.DataFrame([
    {'test': 'same request + same command', 'binding_pass': lab.bound_to(request, candidate, evidence)},
    {'test': 'changed load; old evidence', 'binding_pass': lab.bound_to(changed_request, candidate, evidence)},
    {'test': 'changed command; old evidence', 'binding_pass': lab.bound_to(request, {'control': [0.50, 0.]}, evidence)}])
display(guard)
assert guard.binding_pass.tolist() == [True, False, False]