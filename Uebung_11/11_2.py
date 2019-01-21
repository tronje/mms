#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


def gauss_matrix(l):
    output = np.empty((1000, l))
    for i in range(1000):
        output[i] = np.random.randn(l)

    return np.matrix(output)


def periodogram(m, l):
    return (np.absolute(np.fft.rfft(m)) ** 2) / l


def variance(m, l):
    return np.var(m, axis=1)


def main():
    for l in [32, 256, 1024]:
        matrix = gauss_matrix(l)
        per = periodogram(matrix, l)
        var = variance(per, l)
        plt.plot(np.linspace(0, 1000, 1000), var)
        plt.show()


if __name__ == "__main__":
    main()
