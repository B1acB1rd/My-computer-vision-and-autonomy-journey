import numpy as np
img = np.arange(20).reshape(4, 5)
#print(img)

#[[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]
# [15 16 17 18 19]]

#print(img[0])#prints first row
#print(img[:, 0])#Print first column
#print(img[1:3])
#print(img[:, 2:4])
#print(img[1:3, 2:4])
print(img[::2, ::2])