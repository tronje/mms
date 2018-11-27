import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Aufgabe 2. a)
def fft2(s):
    X = np.fft.fft(s,axis=0)
    Result = np.fft.fft(X,axis=1)
    return Result

def Aufgabe2a():
    x = np.arange(-np.pi, np.pi,0.1)
    y = np.arange(-np.pi, np.pi,0.1)
    X,Y = np.meshgrid(x,y)
    R = np.sqrt(X**2+Y**2)
    s = np.sin(R)
    
    fig = plt.figure()
    ax = fig.add_subplot(111,projection="3d")
    surf = ax.plot_surface(X,Y, s)
    plt.show()
    
    S1 = fft2(s)
    fig = plt.figure()
    ax = fig.add_subplot(221,projection="3d")
    ax.set_title("our fft2 magnitude")
    surf = ax.plot_surface(X,Y, np.abs(S1))

    ax = fig.add_subplot(222,projection="3d")
    ax.set_title("our fft2 phase")
    surf = ax.plot_surface(X,Y, np.angle(S1))

    S2 = np.fft.fft2(s)
    ax = fig.add_subplot(223,projection="3d")
    ax.set_title("numpy fft2 magnitude")
    surf = ax.plot_surface(X,Y, np.abs(S2))

    ax = fig.add_subplot(224,projection="3d")
    ax.set_title("numpy fft2 phase")
    surf = ax.plot_surface(X,Y, np.angle(S2))

    plt.show()

    error = np.sum(S1-S2)
    
    print("Total difference: " + str(error))

# Aufgabe 2. b)
def CenteredAmplitudeAndPhase(S):
    Phase = np.angle(S)
    Amplitude = np.abs(S)
    return Amplitude, Phase

def Aufgabe2c():
    x = np.arange(0, 20,1)
    y = np.arange(0, 20,1)
    X,Y = np.meshgrid(x,y)
    s = np.zeros((20,20))
    s[X==10] = 255
    
    plt.imshow(s, cmap='gray')
    plt.suptitle('Vertical line')
    plt.show()

    A,P = CenteredAmplitudeAndPhase(fft2(s))
    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax.imshow(A)
    ax.set_title("Amplitude spectrum")
    ax = fig.add_subplot(122)
    ax.imshow(P)
    ax.set_title("Phase spectrum")
    plt.show()

if __name__ == "__main__":
    Aufgabe2a()
    Aufgabe2c()

