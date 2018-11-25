#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


def signal(x):
    return np.sin(x) + np.random.normal(size=x.size)


def autocorrelation(f):
    # see https://stackoverflow.com/a/676302
    result = np.correlate(f, f, mode='full')
    return result[result.size // 2:]


def main():
    x = np.linspace(0, 2 * np.pi * 120, 2000)
    s = signal(x)
    plt.subplot(211)
    plt.plot(x, s)
    plt.title('Signal with added random noise')

    plt.subplot(212)
    plt.plot(x, autocorrelation(s))
    plt.title('Autocorrelation of above signal')

    plt.show()


if __name__ == "__main__":
    main()
