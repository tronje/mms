#!/usr/bin/env python3

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


def square_wave_convolution(n):
    t = np.linspace(0, 2, 500, endpoint=False)
    sq_wave = signal.square(5 * np.pi * t)

    convolution = sq_wave

    for i in range(n):
        convolution = np.convolve(convolution, convolution, mode='same')

    plt.plot(t, convolution)
    plt.show()


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    square_wave_convolution(n)
