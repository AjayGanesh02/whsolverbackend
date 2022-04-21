import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
   
    # Capture frame-by-frame
    ret, frame = cap.read()
     
    # Show the captured image
    cv2.imshow('WebCam', frame)
    cv2.namedWindow('WebCam', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('WebCam', 300, 300)
     
    # wait for the key and come out of the loop
    if cv2.waitKey(1) == ord('q'):
        break
 
# Discussed below
cap.release()
cv2.destroyAllWindows()