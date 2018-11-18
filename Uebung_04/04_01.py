#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


def square_wave():
    y = np.linspace(-2, 2, 100)

    for i in range(len(y)):
        if y[i] < -0.5 or y[i] > 0.5:
            y[i] = 0
        else:
            y[i] = 1

    return y


def square_wave_convolution(n):
    convolution = square_wave()

    for i in range(n):
        convolution = np.convolve(convolution, convolution, mode='full')

    x = np.linspace(-2, 2, len(convolution))
    plt.plot(x, convolution)
    plt.show()


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    square_wave_convolution(n)
