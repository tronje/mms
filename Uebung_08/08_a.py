import numpy as np
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt

lena = np.load("lena.npy")
plt.imshow(lena, cmap='gray')
plt.show()

#print(lena)

# Gabor_sin in pixel domain
#def Gabor(x, y, angle, tuning, bandwidth, width):
def Gabor(x, y, angle, tuning, sigma):
    omega0 = (2*np.pi)/tuning
    omega0x = np.cos(angle)*omega0
    omega0y = np.sin(angle)*omega0

    a = 255.0
    b = (omega0+a*(1/sigma))/(omega0-a*(1/sigma))
    sigma2 = sigma*sigma
    
    #b = pow(2,bandwidth)
    #sigma2 = (width*(b+1))/(omega0*(b-1))*(width*(b+1))/(omega0*(b-1))

    # in den folien steht omega0x und omega0y
    #print(omega0 + width*((width*(b+1))/(omega0*(b-1))))
    return (np.sin(omega0x*x+omega0y*y)/(2*np.pi*sigma2))*np.exp(-((x*x+y*y)/(2*sigma2)))


#x = np.linspace(-128,127,256)
#y = np.linspace(-128,127,256)
#x = np.linspace(0,255,256)
#y = np.linspace(0,255,256)
x = np.linspace(-16,15,32)
y = np.linspace(-16,15,32)

X,Y = np.meshgrid(x,y)

gabor_filter_pixel = Gabor(X,Y,0*np.pi,8,5.0)
#gabor_filter_pixel = Gabor(X,Y,0*np.pi,8,255,5.0)

#gabor_filter_freq = np.fft.fft2(gabor_filter_pixel) # muss man hier fft.fftshift benutzen?

plt.imshow(gabor_filter_pixel, cmap='gray')
plt.show()

#lena_freq = np.fft.fft2(lena)
#filtered_lena_freq = np.multiply(lena_freq,gabor_filter_freq)
#filtered_lena_pixel = np.fft.ifft2(filtered_lena_freq)

filtered_lena_pixel = fftconvolve(gabor_filter_pixel, lena)

plt.imshow(np.abs(filtered_lena_pixel).astype(np.uint8), cmap='gray')
plt.show()

print(np.abs(filtered_lena_pixel).astype(np.uint8))

