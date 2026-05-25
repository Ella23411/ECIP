# Task 3
# For each value of r calculate the population size and plot the data. 

import matplotlib.pyplot as plt

# r values from the assignment
r_values = [2, 2.5, 1, 1.2, 3, 4, 0.5, 4.4, 3.2, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]

# simulation settings
initial_population = 0.5
steps = 50

plt.figure(figsize=(10,6))

for r in r_values:
    population = initial_population
    populations = []
    time_steps = []

    for step in range(steps):
        populations.append(population)
        time_steps.append(step)
        population = r * population * (1 - population)

    plt.plot(time_steps, populations, label=f"r = {r}")

plt.xlabel("Time step")
plt.ylabel("Population size")
plt.title("Logistic Population Growth for Different r Values")
plt.legend()
plt.grid(True)

plt.show()