import random
import sys
import math


# Simpler fitness_function of two variables with a maximum at (x=1, y=2)
def fitness_function(x, y):
    return 20 * (x ** 2) + (y ** 2) - 10 * (math.cos(2 * 3.14 * x) + math.cos(2 * 3.14 * y))


def evaluate_generation(population):
    scores = []
    total = 0
    for individual in population:
        r = fitness_function(individual[0], individual[1])
        scores.append(r)
        total += r
    else:
        print("error: Wrong number of arguments received")
    avg = total / len(scores)
    return scores, avg


def mutate(individual):
    new = []
    for attribute in individual:
        new.append(attribute + random.normalvariate(0, attribute + .1))  # Random factor of normal distribution
    return new


def initialize(n, p):
    pop = [[0] * n]
    for i in range(p):
        pop.append(mutate(pop[0]))
    return pop


def termination(best, val, total_iterations, population_size, num_attributes):
    best = [round(x, 3) for x in best]
    print(total_iterations, "iterations on a population of", population_size)
    print("The optimal input is", best, "with a value of", round(val, 3))


def find_best(population):
    best = None
    val = None
    for individual in population:
        r = fitness_function(individual[0], individual[1])
        try:
            if r > val:
                best = individual
                val = r
        except:
            best = individual
            val = r
    return best, val
