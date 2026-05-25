# Task 1
# Make a simulation by using the logistic regression expression = population growth
# Equation: x(n+1) = r * x(n) * (1 - x(n))
# Use a growth factor r = 0.9
# Make a raport (word doc) that describes the fate of the population for r = 0.9

import matplotlib.pyplot as plt

r = 0.9
population = 0.5
steps = 50

populations = []
time_steps = []

print(f"Growth factor r = {r}")
print(f"Initial population = {population}\n")

for step in range(steps + 1):
    print(f"Step {step}: population = {population:.6f}")
    
    time_steps.append(step)
    populations.append(population)
    
    population = r * population * (1 - population)

# Plot the results
plt.figure()
plt.plot(time_steps, populations, marker='o')
plt.xlabel("Time step")
plt.ylabel("Population")
plt.title("Logistic Population Growth (r = 0.9)")
plt.grid(True)

plt.show()