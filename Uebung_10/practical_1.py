from scipy.signal import correlate
from soundfile import read

import numpy as np
import matplotlib.pyplot as plt  

if __name__ == "__main__":
    signal, fs = read("echosig.wav")
    X = range(len(signal))

    plt.plot(X,signal)
    plt.show()

    auto_correlation = correlate(signal,signal)
    auto_correlation = auto_correlation[len(auto_correlation)//2:]

    # echo peak at roughly 159
    plt.plot(range(200),auto_correlation[:200])
    plt.show()

    print("Sampling rate: " + str(fs) + "Hz")
    print("Echo peak at sample 159.")

    seconds = 159/fs
    print("Echo peak after 159/sampling rate seconds: " + str(seconds) + "s")

    meters = (seconds * 343)/2
    print("Total distance to wall is time of the echo times speed of sound divided by 2: " + str(meters) + "m")
