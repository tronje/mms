import numpy as np
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt

lena = np.load("lena.npy")
plt.imshow(lena, cmap='gray')
plt.show()

# Gabor_sin in pixel domain
def Gabor(x, y, angle, tuning, sigma):
    omega0 = (2*np.pi)/tuning
    omega0x = np.cos(angle)*omega0
    omega0y = np.sin(angle)*omega0
    sigma2 = sigma*sigma
    
    return (np.sin(omega0x*x+omega0y*y)/(2*np.pi*sigma2))*np.exp(-((x*x+y*y)/(2*sigma2)))


x = np.linspace(-16,15,32)
y = np.linspace(-16,15,32)

X,Y = np.meshgrid(x,y)

gabor_filter_pixel = Gabor(X,Y,0*np.pi,8,5.0)

plt.imshow(gabor_filter_pixel, cmap='gray')
plt.show()

filtered_lena_pixel = fftconvolve(gabor_filter_pixel, lena)

plt.imshow(np.abs(filtered_lena_pixel), cmap='gray')
plt.show()



