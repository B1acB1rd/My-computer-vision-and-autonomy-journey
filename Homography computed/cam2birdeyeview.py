import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(r'Homography computated\video-from-rawpixel-id-17027305-sd.mp4')
pts = None
points = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if not points:
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Fix color for matplotlib
        print("Pick 4 points for the trapezium. This trapezium will be used for selection.")
        points = plt.ginput(4)
        plt.close()
    
    pts = np.array(points, dtype=np.int32)

    # Create a mask
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
    cv2.fillConvexPoly(mask, pts, 255)

    # Apply mask to isolate ROI
    roi = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Convert to grayscale and blur
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_roi, (5, 5), 0)
    
    # Use OTSU thresholding instead of Canny (creates solid blobs, not edges)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Morphological closing: fills gaps and holes in the road surface
    kernel = np.ones((9, 9), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # Optional: Opening to remove small noise
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Find contours on the cleaned binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Get the largest contour
        road_contour = max(contours, key=cv2.contourArea)
        
        # Only draw if it's significant (not just noise)
        if cv2.contourArea(road_contour) > 500:
            # Fill with green (-1 thickness fills the shape)
            cv2.drawContours(frame, [road_contour], -1, (0, 175, 0), -1)
    
    # Display results
    cv2.imshow("Road Detection", frame)
    cv2.imshow("Debug Threshold", thresh)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()