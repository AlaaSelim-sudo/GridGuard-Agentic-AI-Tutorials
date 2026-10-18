from src.selector_display import operator_record, stage_outputs
for backend in ('lindistflow3','opendss'):
    print('\nOperator view:', backend)
    display(pd.DataFrame([operator_record(analysis, CASE, backend)]).T)
display(stage_outputs(analysis, CASE, 'opendss'))
print('Human acknowledgment remains pending. No equipment command was sent.')
