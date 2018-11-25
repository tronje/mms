#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


def main():
    x = np.linspace(-np.pi, np.pi, 201)
    sin1 = np.sin(x)

    i = 0
    for factor in [0, 1/4, 2/4, 3/4, 1]:
        i += 1

        sin2 = np.sin(x + factor * np.pi)

        # see https://stackoverflow.com/a/3425548
        cc = np.corrcoef(sin1, sin2)[1, 0]

        plt.subplot(3, 2, i)
        plt.plot(x, sin1)
        plt.plot(x, sin2)
        plt.title(f"Sine shifted by {factor} * pi. Corr. coefficient = {cc}")

        print(f"Correlation coefficient of sin(x) and sin(x + {factor} * pi):")
        print(cc)

    plt.show()

    # plt.plot(x, np.sin(x + 2 * np.pi / 4), label="sin")
    # plt.plot(x, np.cos(x), label="cos")
    # plt.axis('tight')
    # plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()
