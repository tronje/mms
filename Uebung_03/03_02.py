#!/usr/bin/python3.5
import matplotlib.pyplot as plt
import numpy as np
import math

def PlotE(n):
    z = complex(0,np.pi)
    x = np.arange(0,n+1)
    y = (1+(z/n))**x
    imag, =plt.plot(x,y.imag)
    real, =plt.plot(x,y.real)
    plt.legend([real,imag], ['real','imag'])
    plt.show()
    #plt.scatter(y.real,y.imag)
    #plt.show()
    
if __name__ == "__main__":
    PlotE(1)
    PlotE(5)
    PlotE(10)
    PlotE(50)
    PlotE(100)
    PlotE(10000)
