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


def additive_cosine(cos_a, cos_b):
    return cos_a + cos_b


def write_additive_cosine(cos_a, freq_a, srate_a, cos_b, freq_b, srate_b):
    import os
    import sys
    from scipy.io import wavfile

    if srate_a != srate_b:
        print("write_additive_cosine: Non-equal sample rates! "
              "Returning early...", file=sys.stderr)
        return

    filename = "additive_cosine_" + str(freq_a) + "_" + str(freq_b) + ".wav"

    if (os.path.isfile(filename)):
        print(filename + " already exists!", file=sys.stderr)
        return
    else:
        wavfile.write(filename, srate_a, additive_cosine(cos_a, cos_b))


def main():
    # 400 Hz, 6000 sample rate cosine
    cos_400_6k = cosine(400, 6000)
    write_cosine(cos_400_6k, 400, 6000)

    # 400 Hz, 12000 sample rate cosine
    cos_400_12k = cosine(400, 12000)
    write_cosine(cos_400_12k, 400, 12000)

    # 630 Hz, 6000 sample rate cosine
    cos_630_6k = cosine(630, 6000)
    write_cosine(cos_630_6k, 630, 6000)

    # 800 Hz, 6000 sample rate cosine
    cos_800_6k = cosine(800, 6000)
    write_cosine(cos_800_6k, 800, 6000)

    # 400 Hz and 630 Hz
    write_additive_cosine(cos_400_6k, 400, 6000, cos_630_6k, 630, 6000)

    # 400 Hz and 800 Hz
    write_additive_cosine(cos_400_6k, 400, 6000, cos_800_6k, 800, 6000)


if __name__ == "__main__":
    main()
