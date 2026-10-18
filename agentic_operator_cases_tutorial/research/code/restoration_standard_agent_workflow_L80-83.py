result = solve_restoration_milp(100.)
accepted = bool(
    result['milp']['success']
    and result['agreement']
)
