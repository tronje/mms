#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


def rect_wave():
    y = np.linspace(-2, 2, 100)

    for i in range(len(y)):
        if y[i] < -0.5 or y[i] > 0.5:
            y[i] = 0
        else:
            y[i] = 1

    return y


def cosine():
    sampling_points = np.linspace(-2, 2, 100)
    return np.cos(2 * np.pi * sampling_points)


def main():
    cos = cosine()
    rect = rect_wave()

    # convolution - simple
    convolution = np.convolve(cos, rect, mode='full')

    # convolution has length N+M-1, but FFT has length N
    # we just append some zeros to get to the same dimension as the convolution
    cos2 = np.append(cos, np.array([0 for i in range(len(cos))]))
    rect2 = np.append(rect, np.array([0 for i in range(len(rect))]))

    # inverse fft of the product of the ffts of both functions
    inv_fft_of_fft_product = np.fft.ifft(np.fft.fft(cos2) * np.fft.fft(rect2))

    # this is a bit stupid - both of these graphs are the same, so we can't
    # actually see this, as they overlap exactly.
    # so we just show them one after the other.
    plt.plot(convolution, label="Convolution of cos and rect")
    plt.legend()
    plt.show()
    plt.plot(inv_fft_of_fft_product, label="FFT(FFT(cos) * FFT(rect))")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
