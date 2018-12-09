#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


def reconstruct(ns, label):
    """Reconstruct a signal with the sinc terms described by `ns`.

    `ns` shall be a list like [-1, 0, 1] or [-2, -1, -, 1, 2], etc,
    giving the `sinc` functions to use.
    """

    def s(t):
        """Constant function s(t) = s_0"""
        return 1.5  # arbitrary value

    T = 5  # period
    space = np.linspace(-T, T, 1000)
    signal = np.zeros(1000)

    for n in ns:
        signal += s(n) * np.sinc(space + n)

    plt.plot(space, signal, label=label)


if __name__ == "__main__":
    reconstruct([-1, 0, 1], "three sincs")
    reconstruct([-2, -1, 0, 1, 2], "five sincs")
    reconstruct([-3, -2, -1, 0, 1, 2, 3], "seven sincs")
    reconstruct([i for i in range(-100, 100)], "two-hundred sincs (test)")
    plt.legend(loc="lower center")
    plt.show()
