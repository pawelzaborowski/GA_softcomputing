import numpy as np
from scipy.optimize import fmin, fmin_l_bfgs_b
import scipy.optimize as opt
import math

from ga.algorithm import function_picker, fitness_function


def f(x):
    if function_picker() == 1:
        return 20 * (x[0] ** 2) + (x[1] ** 2) - 10 * (math.cos(2 * math.pi * x[0]) + math.cos(2 * math.pi * x[1]))
    else:
        return math.sin(3 * x[0]) * math.cos(3 * x[1]) / 3

def print_score():
    # max(1, f)
    # global_maxima = f[np.argmax(f[:, -1])][:-1]
    # fmin_l_bfgs_b(lambda x: -f(x), np.array([0,0]))

    min_loc = opt.fmin(lambda vec: -fitness_function(vec[0], vec[1]), [-1.0, 1.0])

    print(min_loc)

