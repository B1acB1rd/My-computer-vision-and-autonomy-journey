import numpy as np

a = np.zeros((5, 3))
#[
#[0, 0, 0],
#[0, 0, 0],
#[0, 0, 0],
#[0, 0, 0],
#[0, 0, 0]
#] Guessed shape
#print(a)

b = np.ones((2, 4, 3))
#[[[1, 1, 1],
#[1, 1, 1],
#[1, 1, 1],
#[1, 1, 1]],
#[[1, 1, 1],
#[1, 1, 1],
#[1, 1, 1],
#[1, 1, 1],
#[1, 1, 1]]]
print(b)
c = np.arange(12).reshape(3, 4)
#np.arange creates an array of evenly spaced values within a defined interval
#[[0, 1, 2, 3],
#[4, 5, 6, 7],
#[8, 9, 10, 11]]
print(c)