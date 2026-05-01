import cv2
import numpy as np

image = cv2.imread(r"C:\Users\B1ACB1RD\Downloads\Screenshot_20260427_135747_Expo Go.jpg")



h, w = image.shape[:2]

# 1. Create a blank black mask (same size as image, 1 channel)
mask = np.zeros((h, w), dtype="uint8")

# 2. Define the region to isolate (e.g., a circle or a polygon)
# This is the "window" through which you will see your image
cv2.circle(mask, (w//2, h//2), 100, 255, -1) 

# 3. Apply the mask using bitwise_and
# Notice src1 and src2 are both the 'image'
isolated_region = cv2.bitwise_and(image, image, mask=mask)

# Show results
cv2.imshow("Isolated Region", isolated_region)
cv2.waitKey(0)
