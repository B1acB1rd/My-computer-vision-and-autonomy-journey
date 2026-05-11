import cv2
cap = cv2.VideoCapture(r"C:\Users\B1ACB1RD\Downloads\20260510_092302~2.mp4")
frame_count = 0

while frame_count < 100:
    ret, img = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.convertScaleAbs(gray, alpha=0.7, beta=0)
    ret_cb, corners = cv2.findChessboardCorners(gray, (7,7), None)
    
    if ret_cb:
        print(f"FOUND at frame {frame_count}")
        # Draw and show it
        cv2.drawChessboardCorners(img, (7,7), corners, ret_cb)
        cv2.imshow(f"Frame {frame_count}", img)
        cv2.waitKey(0)
    
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
