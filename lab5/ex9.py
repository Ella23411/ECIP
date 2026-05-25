import numpy as np
import matplotlib.pyplot as plt

T = 50
dt = 1.0
t = np.arange(T)

A = np.array([[1, dt],
              [0, 1]])

C = np.array([[1, 0]])

Q = np.array([[0.01, 0],
              [0, 0.01]])

R = np.array([[0.5]])

x_true = np.zeros((2, T))
y = np.zeros(T)

x_true[:, 0] = np.array([0.0, 1.0])

process_noise = np.random.multivariate_normal([0, 0], Q, T).T
measurement_noise = np.sqrt(R[0, 0]) * np.random.randn(T)

for k in range(1, T):
    x_true[:, k] = A @ x_true[:, k - 1] + process_noise[:, k]

for k in range(T):
    y[k] = (C @ x_true[:, k])[0] + measurement_noise[k]

x_hat = np.zeros((2, T))
x_hat[:, 0] = np.array([0.0, 0.0])

P = np.eye(2)

estimated_position = np.zeros(T)
estimated_velocity = np.zeros(T)
estimated_position[0] = x_hat[0, 0]
estimated_velocity[0] = x_hat[1, 0]

for k in range(1, T):
    x_pred = A @ x_hat[:, k - 1]
    P_pred = A @ P @ A.T + Q

    S = C @ P_pred @ C.T + R
    K = P_pred @ C.T @ np.linalg.inv(S)

    innovation = y[k] - (C @ x_pred)[0]
    x_hat[:, k] = x_pred + (K.flatten() * innovation)

    P = (np.eye(2) - K @ C) @ P_pred

    estimated_position[k] = x_hat[0, k]
    estimated_velocity[k] = x_hat[1, k]

plt.figure()
plt.plot(t, x_true[0, :], label='True position')
plt.plot(t, estimated_position, '--', label='Estimated position')
plt.xlabel('Time step')
plt.ylabel('Position')
plt.title('True position vs Estimated position')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(t, x_true[1, :], label='True velocity')
plt.plot(t, estimated_velocity, '--', label='Estimated velocity')
plt.xlabel('Time step')
plt.ylabel('Velocity')
plt.title('True velocity vs Estimated velocity')
plt.legend()
plt.grid(True)

plt.show()