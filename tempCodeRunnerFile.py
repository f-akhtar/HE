data = [25, 4, 6, 1]
model_coefficients = model.model_output()
print("Prediction value:", sum([data[i] * model_coefficients[i] for i in range(len(data))]))