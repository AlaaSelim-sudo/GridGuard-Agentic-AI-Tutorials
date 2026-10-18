calls = pd.DataFrame(evidence['calls'])
display(calls[['protocol', 'case', 'backend', 'role', 'choice', 'client_s',
    'server_s', 'load_s', 'prompt_s', 'generation_s', 'prompt_tokens',
    'cached_prompt_tokens', 'output_tokens', 'generation_tokens_per_s']].round(4))
figure = plot_call_latency(evidence)
plt.show()
