import numpy as np
import matplotlib.pyplot as plt

T = 50
t = np.arange(T)

A = 1.0
B = 0.5
C = 1.0

Q = 0.01
R = 0.5
P0 = 1.0

u = np.ones(T)

x_true = np.zeros(T)
y = np.zeros(T)

process_noise = np.sqrt(Q) * np.random.randn(T)
measurement_noise = np.sqrt(R) * np.random.randn(T)

for k in range(1, T):
    x_true[k] = A * x_true[k - 1] + B * u[k] + process_noise[k]
    y[k] = C * x_true[k] + measurement_noise[k]

x_pred_only = np.zeros(T)
x_pred_only[0] = 0.0

for k in range(1, T):
    x_pred_only[k] = A * x_pred_only[k - 1] + B * u[k]

x_kalman = np.zeros(T)
K_values = np.zeros(T)
P_values = np.zeros(T)

x_kalman[0] = 0.0
P = P0
P_values[0] = P

for k in range(1, T):
    x_pred = A * x_kalman[k - 1] + B * u[k]
    P_pred = A * P * A + Q

    K = P_pred * C / (C * P_pred * C + R)

    x_kalman[k] = x_pred + K * (y[k] - C * x_pred)
    P = (1 - K * C) * P_pred

    K_values[k] = K
    P_values[k] = P

mse_pred_only = np.mean((x_true - x_pred_only) ** 2)
mse_kalman = np.mean((x_true - x_kalman) ** 2)

print("MSE for prediction only:", mse_pred_only)
print("MSE for full Kalman filter:", mse_kalman)

if mse_kalman < mse_pred_only:
    print("The full Kalman filter gives a smaller MSE.")
else:
    print("The prediction-only case gives a smaller MSE.")

plt.figure()
plt.plot(t, x_true, label='True state')
plt.plot(t, x_pred_only, '--', label='Prediction only')
plt.plot(t, x_kalman, label='Kalman estimate')
plt.xlabel('Time step')
plt.ylabel('State')
plt.title('Prediction only vs Full Kalman filter')
plt.legend()
plt.grid(True)

plt.show()