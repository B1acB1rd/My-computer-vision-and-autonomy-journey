from PIL import Image
from pylab import *

im = array(Image.open(r"C:\Users\B1ACB1RD\Pictures\Screenshot 2026-01-23 180136.png").convert('L'))
figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')
figure()
hist(im.flatten(), 128)
show()