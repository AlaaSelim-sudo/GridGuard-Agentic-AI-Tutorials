                else:
                    evaluations += 1
                    point = plant.solve(candidate['control'], load_mult=case.forecast_loads[0], rating_fraction=case.rating_fraction)
                    failures = verify_control(point, case)
                    if point.get('backend') != backend or any(abs(a-b)>1e-12 for a,b in zip(point['control'], candidate['control'])):
                        failures.append('candidate_evidence_mismatch')
