#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


# 2.1, (4 P.)
def fourier_synthesis(n):
    p = 1000
    x = np.linspace(-1, 1, p)
    f = np.sign(x)

    plt.plot(x, f, color='blue', linewidth=2)

    sum = np.zeros_like(x)

    for k in range(1, n, 2):
        sum = sum + 4 / np.pi * np.sin(k * np.pi * x) / k

    plt.plot(x, sum, color='red')
    plt.show()


def print_help(file):
    print("Usage:", file=file)
    print("./02_01_fourier_synth.py <n>", file=file)


if __name__ == "__main__":
    import sys

    try:
        n = int(sys.argv[1])
    except IndexError:
        print("Invalid arguments!\n", file=sys.stderror)
        print_help(sys.stderr)

    fourier_synthesis(n)
