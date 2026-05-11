from PIL import Image
from numpy import *
from pylab import *
import pca

im  = array(Image.open(r"C:\Users\B1ACB1RD\Pictures\Screenshot 2026-01-23 180136.png"))

m, n = im.shape[0:2]

immatrix = array(im.flatten())

print(immatrix)

V, S, imean = pca.pca(immatrix)
figure()
gray()
subplot(2, 4, 1)
imshow(imean.reshape(m, n))

for i in range(7):
    subplot(2, 4, i+2)
    imshow(V[i].reshape(m,n))
show()
