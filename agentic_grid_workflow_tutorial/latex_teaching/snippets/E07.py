    client = ProposalLlama(journal, model='llama3.1:8b')
    live_reply = client.ask('Optimization Agent', pool['context']['public_context'],
                            list(pool['context']['catalog']))
