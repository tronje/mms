import numpy as np
import matplotlib.pyplot as plt

# TODO: label the plots etc
if __name__ == "__main__":
    f, ax = plt.subplots(5, 3)

    t = np.linspace(0,2*np.pi*120,2000)
    signal  = np.sin(t)
    fourier = np.fft.fft(signal) 
    ax[0][0].plot(t,signal)
    ax[0][1].plot(t,np.abs(fourier))
    ax[0][2].plot(t,np.angle(fourier))

    t = np.linspace(0,2*np.pi*120,1000)
    signal  = np.sin(t)
    fourier = np.fft.fft(signal)
    ax[1][0].plot(t,signal)
    ax[1][1].plot(t,np.abs(fourier))
    ax[1][2].plot(t,np.angle(fourier))

    t = np.linspace(0,2*np.pi*120,500)
    signal  = np.sin(t)
    fourier = np.fft.fft(signal)
    ax[2][0].plot(t,signal)
    ax[2][1].plot(t,np.abs(fourier))
    ax[2][2].plot(t,np.angle(fourier))

    t = np.linspace(0,2*np.pi*120,250)
    signal  = np.sin(t)
    fourier = np.fft.fft(signal)
    ax[3][0].plot(t,signal)
    ax[3][1].plot(t,np.abs(fourier))
    ax[3][2].plot(t,np.angle(fourier))

    t = np.linspace(0,2*np.pi*120,125)
    signal  = np.sin(t)
    fourier = np.fft.fft(signal)
    ax[4][0].plot(t,signal)
    ax[4][1].plot(t,np.abs(fourier))
    ax[4][2].plot(t,np.angle(fourier))

    plt.show()
