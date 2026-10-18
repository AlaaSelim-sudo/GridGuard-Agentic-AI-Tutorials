current_review = {'schema': SCHEMA, 'backend': BACKEND, 'created_utc': datetime.now(timezone.utc).isoformat(),
                  'fixed': fixed, 'agentic': agentic}
display(pd.DataFrame(comparison_rows(current_review)))
print('CURRENT continuous workflow above. HISTORICAL finite-action restoration comparison below:')
model_comparison = read_record('model_comparison.json')
display(pd.DataFrame([row for row in model_comparison['summary'] if row['case'] == 'R2'])[
    ['case', 'backend', 'method', 'model_status', 'final_review_status', 'pv_cap', 'tie', 'shed_fraction']])
