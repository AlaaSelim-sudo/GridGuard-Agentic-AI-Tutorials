CASE = 'test_01'
for backend in ('lindistflow3', 'opendss'):
    print('\nPlanning and first-action gate:', backend)
    display(initial_candidates(CASE, backend).round(6))
