import numpy as np
import matplotlib.pyplot as plt

A = 1
C = 1
Q = 0.2
R = 0.5

n_steps = 30

P_updated = np.zeros(n_steps)
P_predicted = np.zeros(n_steps)

P = 1.0

for t in range(n_steps):
    P_minus = A * P * A + Q
    K = P_minus * C / (C * P_minus * C + R)
    P_plus = (1 - K * C) * P_minus

    P_predicted[t] = P_minus
    P_updated[t] = P_plus

    P = P_plus

time = np.arange(1, n_steps + 1)

plt.figure(figsize=(10, 5))
plt.plot(time, P_predicted, marker='o', label='Predicted covariance P(t|t-1)')
plt.plot(time, P_updated, marker='x', label='Updated covariance P(t|t)')
plt.xlabel('Time step')
plt.ylabel('Covariance')
plt.title('Predicted vs Updated Covariance')
plt.legend()
plt.grid(True)
plt.show()