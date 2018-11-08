#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def euler_circle_approximation(n):
    z = complex(0, np.pi)
    values = np.arange(0, n + 1)
    values = (1 + z / n) ** values

    return values


def plot_values(values, n):
    label = "n = " + str(n)
    plt.plot(values.real, values.imag, label=label)


def visualize_convergence():
    for n in [1, 5, 10, 50, 100]:
        values = euler_circle_approximation(n)
        plot_values(values, n)

    plt.xlabel('real')
    plt.ylabel('imaginary')
    plt.grid(True)
    plt.xlim(-2.0, 2.0)
    plt.legend()
    plt.show()


def scatter_plot_e(n):
    z = complex(0, np.pi)
    x = np.arange(0, n+1)
    y = (1 + (z/n))**x
    plt.scatter(y.real, y.imag)
    plt.show()


if __name__ == "__main__":
    visualize_convergence()
