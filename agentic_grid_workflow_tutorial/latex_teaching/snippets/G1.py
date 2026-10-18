class TrialState(TypedDict):
    command: float
    limit: float
    attempts: int
    max_repairs: int
    current: float
    passed: bool
    status: str
    acknowledged: bool
    trace: Annotated[list[str], add]

seed = initial_state(command=0.75, limit=0.80, max_repairs=2)
print("Append reducer:", add(["simulate"], ["verify"]))
print("Initial validated state:", seed)