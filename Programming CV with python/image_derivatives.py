""" How images intensity changes over the image
    The intensity change is described with the x and y derivatives Ix, and Iy of the grayscale image I.
   The image gradient is the vector <> I = [Ix Iy]^T

   The image gradient has two important properties. 
   The gradient magnitude(This describes how strong the image intenssity change is) and the gradient angle(This describes the direction of the largest image intesity).

"""

from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open(r'C:\Users\B1ACB1RD\Pictures\Screenshot 2026-01-23 180136.png').convert('L'))
print(im)
imx = zeros(im.shape)
print(im.shape)
filters.sobel(im, 1, imx)
print(imx)

imy = zeros(im.shape)
filters.sobel(im, 0, imy)
print(imy)