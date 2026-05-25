import numpy as np
import matplotlib.pyplot as plt

T = 50
t = np.arange(T)

A = 1.0
B = 0.5
C = 1.0

Q = 0.01
R = 0.5
P = 1.0

u = np.ones(T)

x_true = np.zeros(T)
y = np.zeros(T)

process_noise = np.sqrt(Q) * np.random.randn(T)
measurement_noise = np.sqrt(R) * np.random.randn(T)

for k in range(1, T):
    x_true[k] = A * x_true[k - 1] + B * u[k] + process_noise[k]
    y[k] = C * x_true[k] + measurement_noise[k]

x_hat = np.zeros(T)
K_values = np.zeros(T)
P_values = np.zeros(T)

x_hat[0] = 0.0
P_values[0] = P

for k in range(1, T):
    x_pred = A * x_hat[k - 1] + B * u[k]
    P_pred = A * P * A + Q

    K = P_pred * C / (C * P_pred * C + R)

    x_hat[k] = x_pred + K * (y[k] - C * x_pred)
    P = (1 - K * C) * P_pred

    K_values[k] = K
    P_values[k] = P

plt.figure()
plt.plot(t, x_true, label='True state')
plt.plot(t, y, label='Noisy measurement')
plt.plot(t, x_hat, label='Kalman estimate')
plt.xlabel('Time step')
plt.ylabel('State')
plt.title('Full Kalman Filter')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(t, K_values, label='Kalman gain K(t)')
plt.xlabel('Time step')
plt.ylabel('Kalman gain')
plt.title('Kalman Gain')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(t, P_values, label='Covariance P(t|t)')
plt.xlabel('Time step')
plt.ylabel('Covariance')
plt.title('Error Covariance')
plt.legend()
plt.grid(True)

plt.show()