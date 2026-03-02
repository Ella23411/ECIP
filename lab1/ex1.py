import numpy as np
import matplotlib.pyplot as plt

num_steps = 50
x0 = 0  # initial true state


t = np.arange(num_steps)


x = np.zeros(num_steps)


x[0] = x0

for k in range(1, num_steps):
    x[k] = x[k-1] + 1


plt.figure()
plt.plot(t, x)
plt.xlabel("Time step (t)")
plt.ylabel("True state x(t)")
plt.title("True State Evolution: x(t+1) = x(t) + 1")
plt.grid(True)
plt.show()