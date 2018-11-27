import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fft2(s):
    X = np.fft.fft(s,axis=0)
    Result = np.fft.fft(X,axis=1)
    return Result

if __name__ == "__main__":
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
