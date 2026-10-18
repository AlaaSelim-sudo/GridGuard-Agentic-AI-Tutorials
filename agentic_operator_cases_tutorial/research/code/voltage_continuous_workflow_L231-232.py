point = plant.solve(
    candidate['control'],
    load_mult=case.forecast_loads[0],
    rating_fraction=case.rating_fraction,
)
failures = verify_control(point, case)
