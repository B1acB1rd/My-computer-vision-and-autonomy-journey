import cv2
import os

# This usually points to where Haar cascades are, which is near the samples folder
data_path = cv2.data.haarcascades
print(f"OpenCV data folder: {data_path}")

# Go up one level and look for a 'samples' or 'data' folder manually
base_cv2 = os.path.dirname(data_path)
print(f"Base CV2 folder: {base_cv2}")
