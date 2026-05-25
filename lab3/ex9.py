import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(10000)

Y = 2*X + np.random.randn(10000) * 0.5 

cov_matrix = np.cov(X, Y)
cov_xy = cov_matrix[0, 1]

print("Covariance:", cov_xy)

plt.figure()
plt.scatter(X, Y, s=5)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Correlated Variables X and Y")
plt.show()