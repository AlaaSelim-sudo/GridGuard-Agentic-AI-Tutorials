columns = ['method','contexts','improved_contexts','trial_rejections',
    'final_model_passes','final_ac_passes','mean_final_objective_on_model_passes',
    'mean_response_calls_accounted','mean_refinement_trials']
display(pd.DataFrame(analysis['test']['summaries'])[columns].round(6))
display(pd.DataFrame(analysis['paired_test_comparison']))
from src.selector_display import plot_selection_results
fig = plot_selection_results(analysis)
plt.show()
from src.selector_display import fixed_rule_diagnostic
display(fixed_rule_diagnostic().round(8))
from src.selector_display import uniform_sensitivity
display(uniform_sensitivity(analysis).round(8))
