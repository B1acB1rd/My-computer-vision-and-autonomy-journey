import cv2
import time

url = r'C:\Users\B1ACB1RD\Desktop\01.1 Code - Modern Computer Vision_05_06_2022\Modern Computer Vision\My-computer-vision-and-autonomy-journey\Homography computated\video-from-rawpixel-id-17027305-sd.mp4'

def streaming(url, int = None, blur = None):
    prev_frame_time = time.time() # Initialize here to avoid 1/0 error
    
    while True:
        cap = cv2.VideoCapture(url)
        if not cap.isOpened():
            print("Cannot connect. Retrying...")
            time.sleep(2)
            continue

        print("Connected!")

        while True:
            ret, frame = cap.read()
            if int == 1:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #Blur 
            if blur:
                frame = cv2.GaussianBlur(frame, (blur, blur), 0)

            if not ret or frame is None:
                print("Lost stream...")
                break
            
            # Calculate FPS
            next_frame_time = time.time()
            fps = 1 / (next_frame_time - prev_frame_time)
            prev_frame_time = next_frame_time
            
            yield frame, fps

        cap.release() # Always release before trying to reconnect

# Testing the generator
for frame, fps in streaming(url): # Use 'url' variable here
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Stream', frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
