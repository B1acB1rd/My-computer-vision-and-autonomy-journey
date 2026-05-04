from PIL import Image
import matplotlib.pyplot as plt
from pylab import *

#Read image to an array
im =  array(Image.open(r"C:\Users\B1ACB1RD\Pictures\Screenshot 2026-01-23 180136.png"))
print(im)
imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x, y, 'r*')
plot(x[:2], y[:2])
show()