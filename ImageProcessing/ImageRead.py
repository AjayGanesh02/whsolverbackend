import cv2
import numpy as np
import pytesseract

cap = cv2.VideoCapture(0)

isProcessed = False

while not isProcessed:
   
    # Capture frame-by-frame
    ret, frame = cap.read()
     
    # Show the captured image
    cv2.imshow('WebCam', frame)

    #parse letters in the image
    
    #convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #apply threshold
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)
    im2 = frame.copy()

    
    # wait for the key and come out of the loop
    if cv2.waitKey(1) == ord('q'):
        break
 
# Discussed below
cap.release()
cv2.destroyAllWindows()