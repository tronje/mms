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
    vert_image = vertical_edge_image()
    diag_image = diagonal_edge_image()

    plt.subplot(321)
    plt.imshow(vert_image, cmap='gray')
    plt.title('Vertical line')

    plt.subplot(322)
    plt.imshow(diag_image, cmap='gray')
    plt.title('Diagonal line')

    A, P = CenteredAmplitudeAndPhase(fft2(vert_image))
    plt.subplot(323)
    plt.imshow(A)
    plt.title("Amplitude spectrum")

    plt.subplot(325)
    plt.imshow(P)
    plt.title("Phase spectrum")

    A, P = CenteredAmplitudeAndPhase(fft2(diag_image))
    plt.subplot(324)
    plt.imshow(A)
    plt.title("Amplitude spectrum")

    plt.subplot(326)
    plt.imshow(P)
    plt.title("Phase spectrum")


    plt.show()


def vertical_edge_image():
    s = np.zeros((20, 20))

    for i in range(20):
        s[i][10] = 255

    return s


def diagonal_edge_image():
    s = np.zeros((20,20))

    for i in range(20):
        s[i][i] = 255

    return s


if __name__ == "__main__":
    Aufgabe2a()
    Aufgabe2c()

