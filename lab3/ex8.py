import numpy as np

true_value = 10.0
noise = np.random.normal(0, 2, 1000)
measurements = true_value + noise

estimated_value = np.mean(measurements)
estimation_error = abs(estimated_value - true_value)

print(f"True Value: {true_value}")
print(f"Estimated Value: {estimated_value:.4f}")
print(f"Estimation Error: {estimation_error:.4f}")