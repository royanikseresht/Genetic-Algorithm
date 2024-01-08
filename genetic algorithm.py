import random

def fitness_function(x):
    return x**2 + 5*x + 6  # this is an example, must be changed

def initialize_population(population_size):
    return [random.uniform(-10, 10) for _ in range(population_size)]

def selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    normalized_fitness = [fitness / total_fitness for fitness in fitness_values]
    return random.choices(population, weights=normalized_fitness, k=2)

def crossover(parent1, parent2):
    crossover_point = random.uniform(0, 1) 
    offspring1 = crossover_point * parent1 + (1 - crossover_point) * parent2
    offspring2 = crossover_point * parent2 + (1 - crossover_point) * parent1
    return offspring1, offspring2

def mutation(individual, mutation_rate):
    if random.random() < mutation_rate:
        return individual + random.uniform(-0.5, 0.5)
    else:
        return individual

def genetic_algorithm(population_size, generations):
    population = initialize_population(population_size)
    for _ in range(generations):
        fitness_values = [fitness_function(x) for x in population]
        selected_parents = selection(population, fitness_values)
        offspring1, offspring2 = crossover(selected_parents[0], selected_parents[1])
        mutated_offspring1 = mutation(offspring1, 0.1)
        mutated_offspring2 = mutation(offspring2, 0.1)
        population.extend([mutated_offspring1, mutated_offspring2])

        population.sort(key=fitness_function, reverse=True)
        population = population[:population_size]

    return population

# example
population_size = 10
generations = 100

final_population = genetic_algorithm(population_size, generations)
print("Final population:", final_population)