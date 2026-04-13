""""I used this to debug the horizontl and vertical problems i was having"""


import cv2
CHECKERBOARD = (16,6)


img = cv2.imread(r'C:\Users\B1ACB1RD\Desktop\01.1 Code - Modern Computer Vision_05_06_2022\Modern Computer Vision\My-computer-vision-and-autonomy-journey\frames\frame_0278.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray) # Invert the image

    # Find the chess board corners
    # If desired number of corners are found in the image then ret = true
ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK+ cv2.CALIB_CB_NORMALIZE_IMAGE)
drawn = cv2.drawChessboardCorners(gray, CHECKERBOARD, corners, ret)
cv2.imshow("Pattern drawn", drawn)
cv2.waitKey(0)
print(corners)