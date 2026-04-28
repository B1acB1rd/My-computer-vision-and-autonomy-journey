""""I used this to debug the horizontal and vertical problems i was having"""

import os, glob
import cv2
CHECKERBOARD = (7, 7)


#img = cv2.imread(r'calibration/cam_caliberation_pictures/20260410_082052.jpg')
folder_path = r'C:\Users\B1ACB1RD\Desktop\01.1 Code - Modern Computer Vision_05_06_2022\Modern Computer Vision\My-computer-vision-and-autonomy-journey\3'
images = glob.glob(os.path.join(folder_path, '*.jpg'))
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray = cv2.bitwise_not(gray) # Invert the image

    # Find the chess board corners
    # If desired number of corners are found in the image then ret = true
for fname in images:
    pic = cv2.imread(fname)
    pic = cv2.resize(pic, (600, 600))
    ret, corners = cv2.findChessboardCorners(pic, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK+ cv2.CALIB_CB_NORMALIZE_IMAGE)
        
    
    drawn = cv2.drawChessboardCorners(pic, CHECKERBOARD, corners, ret)
    cv2.imshow(fname, drawn)
    if not ret:
        os.remove(fname) 
    cv2.waitKey(0)
    print(fname)