import numpy as np
import cv2

checkerboard = (7, 7)

objp = np.zeros((checkerboard[0] * checkerboard[1],3), np.float32)
print(objp.shape)
objp[:,:2] = np.mgrid[0:checkerboard[0],0:checkerboard[1]].T.reshape(-1,2)
objpoints = [] # 3d point in real world space
imgpoints = []

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

found = 0

cap = cv2.VideoCapture(r"C:\Users\B1ACB1RD\Downloads\20260510_092302~2.mp4")
frame_count = 0
valid_count = 0

while frame_count < 400 and valid_count < 40:
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # skip frames: only process every 10th frame
    if frame_count % 10 == 0:
        ret_cb, corners = cv2.findChessboardCorners(gray, (7,7), None)

        if ret_cb:
            objpoints.append(objp.copy())
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)

            valid_count += 1
            print("valid:", valid_count)

    frame_count += 1
cap.release()
cv2.destroyAllWindows()


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)



print("Camera matrix : \n")
print(mtx)
print("dist : \n")
print(dist)
print("rvecs : \n")
print(rvecs)
print("tvecs : \n")
print(tvecs)