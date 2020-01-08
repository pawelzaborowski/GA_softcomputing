import sys

from ga.algorithm import initialize, evaluate_generation, mutate, find_best, termination

if __name__ == "__main__":

    num_attributes = 2
    population_size = 100
    total_iterations = 100

    # num_attributes = int(sys.argv[1])
    # population_size =int(sys.argv[2])
    # total_iterations = int(sys.argv[3])

    population = initialize(num_attributes, population_size)
    for iteration in range(total_iterations):
        scores, avg = evaluate_generation(population)
        deleted = 0
        new_population = []
        for i in range(len(population)):
            if scores[i] < avg:
                deleted += 1
            else:
                new_population.append(population[i])
        for i in range(deleted):
            new_population.append(mutate(new_population[i % len(new_population)]))
        population = new_population
    best, val = find_best(population)
    termination(best, val, total_iterations, population_size, num_attributes)
