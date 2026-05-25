import numpy as np
import matplotlib.pyplot as plt

X_uniform = np.random.uniform(0, 1, 10000)
X_gaussian = np.random.normal(0.5, 0.15, 10000)  # centered to compare visually

plt.figure()
plt.hist(X_uniform, bins=30, alpha=0.5, label="Uniform(0,1)")
plt.hist(X_gaussian, bins=30, alpha=0.5, label="Gaussian (μ=0.5, σ=0.15)")

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Uniform vs Gaussian Distribution")

plt.legend
()
plt.show()