import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from ga.algorithm import fitness_function, function_for_plot


def print_plot():

    x = np.linspace(-60, 60, 30)
    y = np.linspace(-60, 60, 30)

    X, Y = np.meshgrid(x, y)
    Z = function_for_plot(X, Y)

    fig = plt.figure()
    # ax = plt.axes(projection='3d')

    ax = Axes3D(fig)
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.view_init(60, 35)
    plt.show()
