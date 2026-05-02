"""
Task: Image region statistics calculator
1. Load an image
2. Let user click two points to define a rectangle 
3. Extract the rectangele region
4. Compute and print:
    - Mean color (rgb)
    - Standard deviation 
    - Min/Max values
    -Histogram
5. Display the region in a seperate window
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\B1ACB1RD\Pictures\Screenshot 2026-01-23 180136.png')
pts = []
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
points = plt.ginput(2)
points = [int(x) for x in points]
plt.close

print(points)
#selected_roi = img[]

