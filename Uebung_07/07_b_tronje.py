#!/usr/bin/env python3

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


def sine_signal(sampling_rate):
    return np.sin(np.linspace(0, 2 * np.pi * 120, sampling_rate))


def butter_filter(arr):
    # see Examples section here:
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html
    b, a = signal.butter(3, 0.15)
    zi = signal.lfilter_zi(b, a)
    lowpass_signal, _ = \
        signal.lfilter(b, a, arr, zi=zi*arr[0])

    return lowpass_signal


def sinc_filter(arr):
    return np.sinc(arr)


def undersampling(filter_function):
    plt.suptitle("2b) -- low-pass filter function used: " +
                 filter_function.__name__)
    base_signal = sine_signal(2000)
    plt.subplot(5, 2, 1)
    plt.plot(base_signal)
    plt.title("base signal (sampling rate 2000)")

    sampling_rates = [50, 100, 250, 500]

    lowpass_signal = filter_function(base_signal)
    plt.subplot(5, 2, 2)
    plt.plot(lowpass_signal)
    plt.title("base signal (low-pass filtered)")

    idx = 3
    for srate in sampling_rates:
        plt.subplot(5, 2, idx)
        plt.plot(signal.resample(base_signal, srate))
        plt.title(f"sampling rate {srate}")
        idx += 1

        plt.subplot(5, 2, idx)
        plt.plot(signal.resample(lowpass_signal, srate))
        plt.title(f"sampling rate {srate} with low-pass filter")
        idx += 1

    plt.show()


if __name__ == "__main__":
    undersampling(butter_filter)
    undersampling(sinc_filter)
