import numpy as np
import matplotlib.pyplot as plt

lena = np.load("lena.npy")
#print(lena)

# Gabor_sin in pixel domain
def Gabor(x, y, tuning, bandwidth, width):
    omega0 = (2*np.pi)/tuning
    sigma2 = (width*(bandwidth+1))/(omega0*(bandwidth-1))

    # in den folien steht omega0x und omega0y
    return (np.sin(omega0*x+omega0*y)/(2*np.pi*sigma2))*np.exp(-((x*x+y*y)/(2*sigma2)))


x = np.linspace(-100,100,200)
y = np.linspace(-100,100,200)
X,Y = np.meshgrid(x,y)

gabor_filter_pixel = Gabor(X,Y,100,100,100)
gabor_filter_freq = np.fft.fft2(gabor_filter_pixel) # muss man hier fft.fftshift benutzen?

plt.imshow(gabor_filter_pixel, cmap='gray')
plt.show()
