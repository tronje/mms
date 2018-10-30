#!/usr/bin/env python3


def cosine(frequency, sample_rate):
    import numpy as np

    duration = 3
    sampling_points = np.linspace(0, duration, sample_rate * duration)
    cos = np.cos(2 * np.pi * sampling_points * frequency)

    return cos


def write_cosine(cos, frequency, sample_rate):
    import os
    import sys
    from scipy.io import wavfile

    filename = "cosine_" + str(frequency) + "_" + str(sample_rate) + ".wav"

    if (os.path.isfile(filename)):
        print(filename + " already exists!", file=sys.stderr)
        return
    else:
        wavfile.write(filename, sample_rate, cos)


def print_help(file):
    print("Usage:", file=file)
    print("./02_02_cosine.py <frequency> <sample_rate>", file=file)


if __name__ == "__main__":
    import sys

    try:
        freq = int(sys.argv[1])
        srate = int(sys.argv[2])
    except IndexError:
        print("Invalid arguments!", file=sys.stderr)
        print("Expected frequency and sample rate!\n", file=sys.stderr)
        print_help(sys.stderr)
        sys.exit(1)

    cos = cosine(freq, srate)
    write_cosine(cos, freq, srate)
