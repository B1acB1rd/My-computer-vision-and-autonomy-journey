import numpy as np
import cv2
img = np.zeros((500, 500, 3 ), dtype=np.uint8)

#img[0:50, 100:150] = [255, 255, 255]
for i in range(0, img.shape[0], 100):
    for j in  range(0, img.shape[1], 100):
        if ((i // 100) + (j // 100)) % 2 == 0:
            img[i: i +100, j: j+100] = (255, 255, 255)
        else:
            img[i, j] = (0, 0, 0)
cv2.imshow("Test", img)
cv2.waitKey(0)