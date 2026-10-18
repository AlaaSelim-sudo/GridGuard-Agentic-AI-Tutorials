if RUN_LOCAL_LLAMA:
    from datetime import datetime, timezone
    from src.proposal_workflow import ProposalLlama
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    journal = ROOT / 'results' / f'classroom_llama_{stamp}.json'
    client = ProposalLlama(journal, model='llama3.1:8b')
    live_reply = client.ask('Optimization Agent', pool['context']['public_context'],
                            list(pool['context']['catalog']))
    print('NEW LOCAL CALL; no dispatch:', live_reply)
    print('Exact journal:', journal)
else:
    print('SKIPPED: no new model call. L3 and L10 remain explicitly archived actual responses.')