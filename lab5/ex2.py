import numpy as np
import matplotlib.pyplot as plt

T = 50
t = np.arange(T)

A = np.array([[1.0]])
B = np.array([[0.5]])

u = np.ones(T)

x_true = np.zeros(T)
process_noise = 0.1 * np.random.randn(T)

for k in range(1, T):
    x_true[k] = (A @ np.array([[x_true[k - 1]]]) + B @ np.array([[u[k]]]))[0, 0] + process_noise[k]

x_hat = np.zeros(T)
x_hat[0] = 0

for k in range(1, T):
    x_hat[k] = (A @ np.array([[x_hat[k - 1]]]) + B @ np.array([[u[k]]]))[0, 0]

plt.plot(t, x_true, label='True state')
plt.plot(t, x_hat, '--', label='Predicted state')
plt.xlabel('Time step')
plt.ylabel('State')
plt.title('Exercise 2: Prediction step')
plt.legend()
plt.grid(True)

plt.show()