import numpy as np
import matplotlib.pyplot as plt

x = 10
noise = np.random.normal(0, 1, 10000)
y = x + noise

plt.figure()
plt.hist(y, bins=30, edgecolor='black')

plt.xlabel("Measured value")
plt.ylabel("Frequency")
plt.title("Measurements y = x + noise (x = 10)")

plt.show()