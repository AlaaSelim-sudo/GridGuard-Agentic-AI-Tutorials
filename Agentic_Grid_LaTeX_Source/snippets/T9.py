sources = pd.DataFrame([{'file': p, 'sha256': digest}
    for p, digest in evidence['source_sha256'].items()])
display(sources)
assert len(calls) == 10 and len(workflows) == 8
assert all(calls['client_s'] >= 0) and all(workflows['other_in_interval_s'] >= 0)
print('Exact reply/journal matching passed; all containing intervals are consistent.')
print('No equipment was operated; this notebook only reads the saved evidence.')
