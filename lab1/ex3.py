import numpy as np
import matplotlib.pyplot as plt

T = 50
x0 = 0
noise_mean = 0.0
noise_std = 2.0
window = 5  

np.random.seed(0)
x = np.zeros(T)
x[0] = x0
for t in range(T - 1):
    x[t + 1] = x[t] + 1


noise = np.random.normal(loc=noise_mean, scale=noise_std, size=T)
y = x + noise


x_hat = np.zeros(T)
for t in range(T):
    start = max(0, t - window + 1)
    x_hat[t] = np.mean(y[start:t + 1])


t = np.arange(T)
plt.figure()
plt.plot(t, x, label="True state x(t)")
plt.scatter(t, y, color="orange", marker="o", label="Noisy observations y(t)")
plt.plot(t, x_hat, linestyle="--", label=f"Moving average estimate (window={window})")
plt.xlabel("Time step t")
plt.ylabel("Value")
plt.title("True State, Noisy Observations, and Moving Average Estimate")
plt.grid(True)
plt.legend()
plt.show()