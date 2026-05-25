import numpy as np
import matplotlib.pyplot as plt

A = 1
B = 1
C = 1

n_steps = 30
u = 1
x0 = 0

np.random.seed(42)

w_std = 0.2
v_std = 0.5

x = np.zeros(n_steps + 1)
y = np.zeros(n_steps)

x[0] = x0

for t in range(n_steps):
    w = np.random.normal(0, w_std)
    v = np.random.normal(0, v_std)

    x[t + 1] = A * x[t] + B * u + w
    y[t] = C * x[t] + v

time_x = np.arange(n_steps + 1)
time_y = np.arange(n_steps)

plt.figure(figsize=(10, 5))
plt.plot(time_x, x, label='True state x(t)', marker='o')
plt.plot(time_y, y, label='Measured output y(t)', marker='x')
plt.xlabel('Time step')
plt.ylabel('Value')
plt.title('1D Linear Dynamic System')
plt.legend()
plt.grid(True)
plt.show()