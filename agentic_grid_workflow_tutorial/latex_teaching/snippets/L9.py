without_trust = lab.trusted_response(cyber, protected_available=False)
with_trust = lab.trusted_response(cyber, protected_available=True)
display(pd.DataFrame([
    {'condition': 'No trusted replacement channels', 'status': without_trust['status'],
     'u_pu': None, 'offline_actual_violations': None},
    {'condition': 'Three trusted channels assumed', 'status': with_trust['status'],
     'u_pu': with_trust.get('flexible_injection_pu'),
     'offline_actual_violations': with_trust.get('actual_violation_count')}]))
print(with_trust['assumption'])
assert without_trust['status'] == 'HOLD'
assert with_trust['actual_violation_count'] == 0