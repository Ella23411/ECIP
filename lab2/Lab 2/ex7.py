# Task 7
# Modify the value of the weight of the state B to 0.5. 
# PLot the evolution of the population for 15 steps based on sequence "S". 
# Answer the question: Does the population survive after 15 steps?
# Write a report which must contain the plot of these 15 steps and the answer to the quesstion.

import random
import matplotlib.pyplot as plt

# State weights (growth factors)
weights = {
    "A": 1.5,
    "B": 0.5,   # modified weight
    "C": 3.3
}

# Markov transition probabilities (from the diagram)
transitions = {
    "A": [("B", 0.4), ("C", 0.6)],
    "B": [("A", 0.5), ("B", 0.5)],
    "C": [("A", 0.2), ("B", 0.2), ("C", 0.6)]
}

def next_state(current):
    r = random.random()
    cumulative = 0
    for state, prob in transitions[current]:
        cumulative += prob
        if r <= cumulative:
            return state

# Generate sequence S of 15 states
current_state = "A"
S = [current_state]

for _ in range(14):
    current_state = next_state(current_state)
    S.append(current_state)

print("State sequence S:")
print(S)

# Logistic population simulation
population = 0.5
populations = [population]

for state in S:
    r = weights[state]
    population = r * population * (1 - population)
    populations.append(population)

# Plot population evolution
steps = list(range(len(populations)))

plt.figure()
plt.plot(steps, populations, marker='o')
plt.xlabel("Step")
plt.ylabel("Population")
plt.title("Population Evolution for 15 Steps (Modified weight B = 0.5)")
plt.grid(True)
plt.show()

print("\nFinal population after 15 steps:", population)