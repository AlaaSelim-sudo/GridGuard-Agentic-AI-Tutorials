plant = ContinuousPlant(BACKEND)
smoke = plant.solve([0.25, 0.0])
display(point_summary(smoke))
print('Fresh first-action check:', verify_control(smoke))
