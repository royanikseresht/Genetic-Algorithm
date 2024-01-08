
# Genetic Algorithm

This repository contains a simple implementation of a genetic algorithm in Python. The genetic algorithm is a search heuristic that mimics the process of natural selection to evolve solutions to optimization and search problems.

## Usage

To use the genetic algorithm, you can follow these steps:

1. Import the required library:
   ```python
   import random
   ```

2. Define the fitness function:
   ```python
   def fitness_function(x):
       return x**2 + 5*x + 6  # Replace this with your own fitness function
   ```

3. Initialize the population:
   ```python
   def initialize_population(population_size):
       return [random.uniform(-10, 10) for _ in range(population_size)]
   ```

4. Perform selection and crossover:
   ```python
   def selection(population, fitness_values):
       # ...
   
   def crossover(parent1, parent2):
       # ...
   ```

5. Perform mutation:
   ```python
   def mutation(individual, mutation_rate):
       # ...
   ```

6. Run the genetic algorithm:
   ```python
   def genetic_algorithm(population_size, generations):
       # ...
   
   population_size = 10
   generations = 100
   
   final_population = genetic_algorithm(population_size, generations)
   print("Final population:", final_population)
   ```

## License

Feel free to modify and use this code for your own projects!
