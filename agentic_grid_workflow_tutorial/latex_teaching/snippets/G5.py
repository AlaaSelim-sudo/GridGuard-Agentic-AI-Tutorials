def human_review(s):
    token = recommendation_id(s)
    reply = interrupt({"recommendation_id": token, "command": s["command"],
                       "toy_current": s["current"], "scope": "invented toy equation only"})
    accepted = (isinstance(reply, dict) and reply.get("approve") is True
                and reply.get("recommendation_id") == token)
    return {"acknowledged": accepted,
            "status": "TOY_ACKNOWLEDGED" if accepted else "TOY_HOLD",
            "trace": [f"human review: {accepted}"]}

review_app = build_graph(human_review, InMemorySaver())
config = {"configurable": {"thread_id": "student-" + uuid.uuid4().hex}, "recursion_limit": 40}
pause = review_app.invoke(initial_state(0.75, 0.80, 2), config)
snapshot = review_app.get_state(config)
print("Pending node:", snapshot.next, "| acknowledged:", snapshot.values["acknowledged"])
print("Interrupt payload:", pause["__interrupt__"][0].value)
assert snapshot.next == ("report",) and not snapshot.values["acknowledged"]
response = {"approve": True, "recommendation_id": recommendation_id(snapshot.values)}
resumed = review_app.invoke(Command(resume=response), config)
print("After simulated readback:", summary(resumed))
assert resumed["acknowledged"] and review_app.get_state(config).next == ()