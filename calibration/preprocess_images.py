import os
import cv2

P = r"C:\Users\B1ACB1RD\Desktop\01.1 Code - Modern Computer Vision_05_06_2022\Modern Computer Vision\My-computer-vision-and-autonomy-journey\calibration\cam_caliberation_pictures"

for i in os.scandir(P):
    image = cv2.imread(i.path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image  = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(f"output_image{i.name}.jpg", image)
    print("succes")