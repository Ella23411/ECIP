import numpy as np
import matplotlib.pyplot as plt

T = 50                 
x0 = 0                 
noise_mean = 0.0
noise_std = 2.0

np.random.seed(0)


x = np.zeros(T)
x[0] = x0
for t in range(T - 1):
    x[t + 1] = x[t] + 1

noise = np.random.normal(loc=noise_mean, scale=noise_std, size=T)
y = x + noise

t = np.arange(T)
plt.figure()
plt.plot(t, x, label="True state x(t)")
plt.scatter(t, y, label="Observations y(t) = x(t) + noise", marker="o")
plt.xlabel("Time step t")
plt.ylabel("Value")
plt.title("True State and Noisy Observations")
plt.grid(True)
plt.legend()
plt.show()