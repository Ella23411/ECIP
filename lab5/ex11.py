import numpy as np
import matplotlib.pyplot as plt

T = 50
t = np.arange(T)

x = np.zeros(T)
u = np.zeros(T)

x[0] = 0.5

for k in range(T - 1):
    u[k] = -0.1
    x[k + 1] = x[k] + 0.1 * x[k]**2 + u[k]

plt.figure()
plt.plot(t, x, label='State x(t)')
plt.xlabel('Time step')
plt.ylabel('State')
plt.title('Exercise 11: Nonlinear system')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(t, u, label='Control input u(t)')
plt.xlabel('Time step')
plt.ylabel('Input')
plt.title('Exercise 11: Input signal')
plt.legend()
plt.grid(True)

plt.show()