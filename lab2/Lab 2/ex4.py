# Task 4
# Consider the above vector as value of the r factor measured here, across 17 years. 
# Answer the question: what will be the population growth in year 17th?

r_values = [2, 2.5, 1, 1.2, 3, 4, 0.5, 4.4, 3.2, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]

population = 0.5

for year, r in enumerate(r_values, start=1):
    population = r * population * (1 - population)
    print(f"Year {year}: r = {r}, population = {population:.5f}")

print("\nPopulation in year 17 =", round(population,5))