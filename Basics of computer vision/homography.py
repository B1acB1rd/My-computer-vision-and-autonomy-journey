import numpy as np

point = np.array([100, 150, 1])# z = 1, because we have converted from homogenous coordiantes to image coordinates

print(point)
H = np.array([
    [29.5075, 0.0, 1173.68729,],
    [0.0, 22.48957, 1812.30508,],
    [ 0.0, 30, 1.0]
])

#Transform to another point
new_point = H @ point
print(new_point)
new_point = new_point/new_point[2]
print(new_point)