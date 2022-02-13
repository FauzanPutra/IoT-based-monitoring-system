# define region of ROI (exclude unit)
(x_min,y_min) = (120,200)
(x_max,y_max) = (440,290)

import cv2
import numpy as np

cap= cv2.VideoCapture("output2.mp4")

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")


while (cap.isOpened()):
    ret,frame= cap.read()
    
    # crop image, only process roi
    roi = frame[y_min:y_max,x_min:x_max]
    
    # convert to gray scale
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # emlarge roi
    roi = cv2.resize(roi, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    
    roi = cv2.GaussianBlur(roi, (15,15), 0)
    
    #binarise roi
    roi = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    
    kernel = np.ones((5,5),np.uint8)
    roi = cv2.erode(roi,kernel,iterations = 1)
    
    roi = cv2.medianBlur(roi, 15)
    roi = cv2.medianBlur(roi, 15)

    kernel = np.ones((3,3),np.uint8)
    roi = cv2.erode(roi,kernel,iterations = 1)
    
    roi = cv2.medianBlur(roi, 13)

    if ret == True:
#         cv2.imshow('frame', frame)
        cv2.imshow('roi', roi)

    if cv2.waitKey(15) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
