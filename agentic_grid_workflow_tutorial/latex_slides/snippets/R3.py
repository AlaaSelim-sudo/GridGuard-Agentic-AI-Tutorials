electrical = ElectricalModel(BACKEND)
feeder_restoration = [run_stages(casebook[key], electrical, None, method='fixed')
                      for key in ('R1', 'R2')]
display(pd.DataFrame([{'case': row['case'], 'status': row['status'],
    'candidate': row['candidate'], **(row['metrics'] or {})} for row in feeder_restoration]))
