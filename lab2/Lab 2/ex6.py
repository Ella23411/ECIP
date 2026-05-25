# Task 6
# Simulate a Marco-machine containing free states A B and C. 
# Run this machine 15 times and record the sequence of states. 
# Store the states as sequence "S". Each state carries a weight. 
# State A = 1.5. B = 2. C = 3.3. 
# Use these weights as values for the growth factor r and calculate 
# the population size on 15 steps according to the weights from sequence "S". 
# Start the population from 0.5.

import random

# State weights (growth factors)
weights = {
    "A": 1.5,
    "B": 2.0,
    "C": 3.3
}

# Transition probabilities from the diagram
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

# Start from state A (can be changed)
current_state = "A"

# Generate sequence S of 15 states
S = [current_state]

for _ in range(14):
    current_state = next_state(current_state)
    S.append(current_state)

print("State sequence S:")
print(S)

# Logistic population calculation
population = 0.5
print("\nPopulation evolution:")

for i, state in enumerate(S):
    r = weights[state]
    population = r * population * (1 - population)
    print(f"Step {i+1} | State {state} | r = {r} | Population = {population:.5f}")