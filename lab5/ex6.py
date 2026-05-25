import numpy as np
import matplotlib.pyplot as plt

T = 50
t = np.arange(T)

A = 1.0
B = 0.5
C = 1.0

R = 0.5
P0 = 1.0

u = np.ones(T)

Q_true = 0.01
process_noise = np.sqrt(Q_true) * np.random.randn(T)
measurement_noise = np.sqrt(R) * np.random.randn(T)

x_true = np.zeros(T)
y = np.zeros(T)

for k in range(1, T):
    x_true[k] = A * x_true[k - 1] + B * u[k] + process_noise[k]
    y[k] = C * x_true[k] + measurement_noise[k]

Q_values = [0.0001, 0.01, 1]
estimates = []

for Q in Q_values:
    x_hat = np.zeros(T)
    P = P0

    for k in range(1, T):
        x_pred = A * x_hat[k - 1] + B * u[k]
        P_pred = A * P * A + Q

        K = P_pred * C / (C * P_pred * C + R)

        x_hat[k] = x_pred + K * (y[k] - C * x_pred)
        P = (1 - K * C) * P_pred

    estimates.append(x_hat)

plt.figure()
plt.plot(t, x_true, label='True state', linewidth=2)
plt.plot(t, estimates[0], label='Q = 0.0001')
plt.plot(t, estimates[1], label='Q = 0.01')
plt.plot(t, estimates[2], label='Q = 1')
plt.xlabel('Time step')
plt.ylabel('State')
plt.title('Exercise 6: Effect of process noise covariance Q')
plt.legend()
plt.grid(True)
plt.show()