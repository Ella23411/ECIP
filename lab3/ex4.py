import numpy as np
import matplotlib.pyplot as plt

# Dataset 1: Uniform(0,1)
X1 = np.random.uniform(0, 1, 10000)

# Dataset 2: Normal with small variance
X2 = np.random.normal(0.5, 0.1, 10000)  # mean=0.5, std=0.1

# Dataset 3: Normal with larger variance
X3 = np.random.normal(0.5, 0.3, 10000)  # mean=0.5, std=0.3

print("Variance X1 (Uniform):", np.var(X1))
print("Variance X2 (Small spread):", np.var(X2))
print("Variance X3 (Large spread):", np.var(X3))

plt.figure()
plt.hist(X1, bins=30, alpha=0.5, label="Uniform(0,1)")
plt.hist(X2, bins=30, alpha=0.5, label="Normal σ=0.1")
plt.hist(X3, bins=30, alpha=0.5, label="Normal σ=0.3")

plt.legend()
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Comparison of Distributions with Different Variance")
plt.show()