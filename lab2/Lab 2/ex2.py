# Task 2
# Use your simulation to point out at what value of r the population growth becomes chaotic.
# Show your result with a screenshot.

import matplotlib.pyplot as plt

# Same logistic function idea from Task 1
def next_population(r, population):
    return r * population * (1 - population)

# Range of r values to test
r_min = 2.5
r_max = 4.0
r_step = 0.001

# Simulation settings
initial_population = 0.5
iterations = 1000
last_iterations = 100   # only plot the final values for each r

r_values_plot = []
population_values_plot = []

r = r_min
while r <= r_max:
    population = initial_population

    # Run the simulation for this r
    for step in range(iterations):
        population = next_population(r, population)

        # Keep only the last values, to show long-term behavior
        if step >= iterations - last_iterations:
            r_values_plot.append(r)
            population_values_plot.append(population)

    r += r_step

# Plot the bifurcation diagram
plt.figure(figsize=(10, 6))
plt.scatter(r_values_plot, population_values_plot, s=0.1)
plt.xlabel("Growth factor r")
plt.ylabel("Population")
plt.title("Logistic Map Bifurcation Diagram")
plt.grid(True)

# Mark approximate onset of chaos
chaos_start = 3.57
plt.axvline(x=chaos_start, linestyle='--', linewidth=1)
plt.text(3.58, 0.9, "Chaos starts around r = 3.57")

plt.show()

print("Using the logistic simulation from Task 1, the population growth")
print("becomes chaotic at approximately r = 3.57.")