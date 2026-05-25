import numpy as np
import matplotlib.pyplot as plt

T = 50
t = np.arange(T)

A = 1.0
B = 1.0
C = 1.0

Q = 0.01
R = 0.5
P = 1.0

L = 0.5

x_true = np.zeros(T)
x_hat = np.zeros(T)
y = np.zeros(T)
u = np.zeros(T)
K_values = np.zeros(T)

x_true[0] = 5.0
x_hat[0] = 0.0

process_noise = np.sqrt(Q) * np.random.randn(T)
measurement_noise = np.sqrt(R) * np.random.randn(T)

for k in range(1, T):
    u[k - 1] = -L * x_hat[k - 1]

    x_true[k] = A * x_true[k - 1] + B * u[k - 1] + process_noise[k]
    y[k] = C * x_true[k] + measurement_noise[k]

    x_pred = A * x_hat[k - 1] + B * u[k - 1]
    P_pred = A * P * A + Q

    K = P_pred * C / (C * P_pred * C + R)
    x_hat[k] = x_pred + K * (y[k] - C * x_pred)
    P = (1 - K * C) * P_pred

    K_values[k] = K

u[T - 1] = -L * x_hat[T - 1]

plt.figure()
plt.plot(t, x_true, label='True state')
plt.plot(t, x_hat, '--', label='Estimated state')
plt.xlabel('Time step')
plt.ylabel('State')
plt.title('Exercise 10: State feedback from estimate')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(t, u, label='Control signal u(t)')
plt.xlabel('Time step')
plt.ylabel('Control')
plt.title('Exercise 10: Control signal')
plt.legend()
plt.grid(True)

plt.show()