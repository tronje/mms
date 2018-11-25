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

    plt.subplot(221)
    plt.plot(x, np.sin(x))
    plt.title('Signal without added noise')

    plt.subplot(222)
    plt.plot(x, autocorrelation(np.sin(x)))
    plt.title('Autocorrelation of "normal" signal')

    plt.subplot(223)
    plt.plot(x, s)
    plt.title('Signal with added random noise')

    plt.subplot(224)
    plt.plot(x, autocorrelation(s))
    plt.title('Autocorrelation of signal with added noise')

    plt.show()


if __name__ == "__main__":
    main()
