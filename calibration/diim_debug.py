""""I used this to debug the horizontl and vertical problems i was having"""


import cv2
CHECKERBOARD = (6,6)


img = cv2.imread(r'calibration/cam_caliberation_pictures/20260410_082052.jpg')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray = cv2.bitwise_not(gray) # Invert the image

    # Find the chess board corners
    # If desired number of corners are found in the image then ret = true
ret, corners = cv2.findChessboardCorners(img, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK+ cv2.CALIB_CB_NORMALIZE_IMAGE)
drawn = cv2.drawChessboardCorners(img, CHECKERBOARD, corners, ret)
cv2.imshow("Pattern drawn", drawn)
cv2.waitKey(0)
print(corners)