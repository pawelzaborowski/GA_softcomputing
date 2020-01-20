import numpy as np
import random
import math


def function_picker():
    return 1

def fitness_function(x, y):
    if function_picker() == 1:
        return 20 * (x ** 2) + (y ** 2) - 10 * (math.sin(2 * math.pi * x) + math.cos(2 * math.pi * y))
    else:
        return math.sin(3 * x) * math.cos(3 * y) / 3


def function_for_plot(x, y):
    if function_picker() == 1:
        return 20 * (x ** 2) + (y ** 2) - 10 * (np.sin(2 * math.pi * x) + np.cos(2 * math.pi * y))
    else:
        return np.sin(3 * x) * np.cos(3 * y) / 3


def evaluate_generation(population):
    scores = []
    total = 0
    for individual in population:
        r = fitness_function(individual[0], individual[1])
        scores.append(r)
        total += r
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
