# Optional integrity checks

Run from the tutorial folder with Python:

```text
python tests/test_proposal_workflow.py
python tests/audit_proposal_records.py
```

The first script uses synthetic test doubles to check orchestration boundaries; its numbers are not experiment results. The second audits the delivered 13-run record and exact source/call/evidence identities without running models. It is specific to the delivered suite and its retained pilot, including Qwen. These checks do not establish electrical model fidelity or field safety. The notebooks validate the scientific evidence they display separately.


For the new learned selector, run `python tests/test_response_selector.py`. Thirteen tests check canonicalization, selected-feedback updates, feature restrictions, frozen evaluation and checkpoint integrity. The actual collection audit is `results/ensemble_voltage_pilot/verification_audit.json`; it checks recorded identities and numerical evidence, not field reliability. The source-bound analysis enforces zero held-out learning updates. E1–E8 runs saved evidence without solver or LLM calls and reproduces one actual training update.
