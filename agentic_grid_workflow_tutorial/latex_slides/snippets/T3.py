voltage_calls = [r for r in evidence['calls'] if r['case'] == 'voltage']
for call in voltage_calls:
    print(f"\n{call['backend']} / {call['role']}: {call['choice']}")
    print('Returned reason:', call['reason'])
    print(f"Client {call['client_s']:.6f} s; server {call['server_s']:.6f} s")
display(pd.DataFrame(voltage_calls)[['backend', 'role', 'model', 'options',
    'prompt_tokens', 'cached_prompt_tokens', 'output_tokens', 'source', 'journal_index']])
