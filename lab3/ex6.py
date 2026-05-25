import numpy as np
import matplotlib.pyplot as plt

X1 = np.random.normal(0, 0.5, 10000)   # smaller variance
X2 = np.random.normal(0, 1.0, 10000)   # medium variance
X3 = np.random.normal(0, 2.0, 10000)   # larger variance

plt.figure()
plt.hist(X1, bins=30, alpha=0.5, label='Gaussian σ=0.5')
plt.hist(X2, bins=30, alpha=0.5, label='Gaussian σ=1.0')
plt.hist(X3, bins=30, alpha=0.5, label='Gaussian σ=2.0')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Gaussian Noise with Different Variances")
plt.legend()
plt.show()