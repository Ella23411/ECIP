import numpy as np
import matplotlib.pyplot as plt

T = 50
t = np.arange(T)

A = np.array([[1.0]])
B = np.array([[0.5]])
C = np.array([[1.0]])

u = np.ones(T)

x_true = np.zeros(T)
y = np.zeros(T)

process_noise = 0.1 * np.random.randn(T)
measurement_noise = 0.2 * np.random.randn(T)

for k in range(1, T):
    x_true[k] = (A @ np.array([[x_true[k - 1]]]) + B @ np.array([[u[k]]]))[0, 0] + process_noise[k]
    y[k] = (C @ np.array([[x_true[k]]]))[0, 0] + measurement_noise[k]

x_hat = np.zeros(T)

for k in range(1, T):
    x_pred = (A @ np.array([[x_hat[k - 1]]]) + B @ np.array([[u[k]]]))[0, 0]
    x_hat[k] = x_pred

innovation = np.zeros(T)

for k in range(1, T):
    innovation[k] = y[k] - (C @ np.array([[x_hat[k]]]))[0, 0]

plt.plot(t, innovation, label='Innovation')
plt.xlabel('Time step')
plt.ylabel('Innovation')
plt.title('Exercise 3: Innovation')
plt.legend()
plt.grid(True)

plt.show()