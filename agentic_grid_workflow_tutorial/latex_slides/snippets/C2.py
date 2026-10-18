plot_cyber(cyber)
display({'H': cyber['measurement_model']['H'],
         'known_synthetic_state': cyber['measurement_model']['true_state']})
