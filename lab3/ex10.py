import numpy as np

N = 10000

A = np.random.rand(N) < 0.4   
B = np.random.rand(N) < 0.6  

# Estimate P(A|B)
P_A_given_B = np.sum(A & B) / np.sum(B)

print("Estimated P(A|B):", P_A_given_B)