# Task 5
# Make a series of experiments in which the population number starts from:
# a) 0.1 b) 0.5 c) 1.0 d) 2
# Make a report in which you note the observations for r = 4.

import matplotlib.pyplot as plt

r = 4
steps = 20

initial_values = [0.1, 0.5, 1.0, 2.0]

plt.figure(figsize=(10,6))

for x0 in initial_values:
    population = x0
    populations = []
    time = []

    for step in range(steps):
        populations.append(population)
        time.append(step)

        population = r * population * (1 - population)

    print(f"\nInitial population = {x0}")
    for t, p in zip(time, populations):
        print(f"Step {t}: {p}")

    plt.plot(time, populations, marker='o', label=f"x0 = {x0}")

plt.xlabel("Iteration")
plt.ylabel("Population")
plt.title("Logistic Map Experiments (r = 4)")
plt.legend()
plt.grid(True)

plt.show()