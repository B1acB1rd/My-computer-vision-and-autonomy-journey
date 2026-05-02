import numpy as np

k = np.array([[800, 0, 320],
             [0, 800, 240],
             [0, 0, 1]])

point_3d = np.array([0.5, 0.3, 3, 1])
print(point_3d[:3])
point_2d = k @ point_3d[:3]
point_2d = point_2d/point_2d[2]
print(point_2d)