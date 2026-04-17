import cv2
import os
from pathlib import Path

# 1. Load the video
video_path = 'calibration/Calberation_pictures/20260411_223825.mp4'
cap = cv2.VideoCapture(video_path)

# Create an output directory if it doesn't exist
output_dir = 'frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

frame_count = 0
next_target = 71.5
frame_count = 0
while True:
    # 2. Read the next frame
    ret, frame = cap.read()
    
    # 3. If frame is not read correctly, end of video
    if not ret:
        break
    
    # 4. Save the current frame as an image
    frame_count += 1
    if frame_count > next_target:
        filename = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(filename, frame)

        next_target += 71.5
    
    count = sum(1 for x in Path(r'C:\Users\B1ACB1RD\Desktop\01.1 Code - Modern Computer Vision_05_06_2022\Modern Computer Vision\My-computer-vision-and-autonomy-journey\frames').iterdir() if x.is_file())

    if count == 30:
        break
    frame_count += 1

# 5. Cleanup
cap.release()
print(f"Extraction complete. {frame_count} frames saved.")
