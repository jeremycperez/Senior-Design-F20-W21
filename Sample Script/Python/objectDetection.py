#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2 as cv
import time
import numpy as np

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

prev_frame_time = 0
new_frame_time = 0
font = cv.FONT_HERSHEY_SIMPLEX 
avgFPS = []
i = 0

while True:
    success, img = cap.read()
    noise = cv.bilateralFilter(img,9,75,75)
    edge = cv.Canny(noise, 50, 150)    
    kernel = np.ones((3,3), np.uint8)
    dilated = cv.dilate(edge,kernel,iterations=1)
    
    new_frame_time = time.time()  
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time
    
    if i < 500:
        avgFPS.append(fps)
        i+=1
    
    fps = int(fps)  
    fps = str(fps) 
    
    contours, h = cv.findContours(dilated, 1, 2)
    contours= sorted(contours, key = cv.contourArea, reverse = True)[:1]
    pt = (180, 3 * img.shape[0] // 4)
    
    for cnt in contours:
        approx = cv.approxPolyDP(cnt,0.01*cv.arcLength(cnt,True),True)
        # print len(cnt)
        if len(approx) >= 4 and len(approx) <= 8:
            cv.drawContours(img,[cnt],-1,(255,0,0),3)
            cv.putText(img,'Cube', pt ,font, 2, [0,255, 255], 2)
 
    cv.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA) 
    cv.namedWindow("Shape", cv.WINDOW_NORMAL)
    cv.imshow('Shape',img)

    corners    = cv.goodFeaturesToTrack(edge,6,0.06,25)
    corners    = np.float32(corners)
    
    for    item in    corners:
        x,y    = item[0]
        cv.circle(img,(x,y),10,255,-1)
    
    cv.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA) 
    cv.namedWindow("Corners", cv.WINDOW_NORMAL)
    cv.imshow("Corners",img)
     
   
    
    cv.putText(edge, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA) 
    cv.namedWindow("Webcam", cv.WINDOW_NORMAL)
    cv.imshow("Webcam", edge)
    
    if cv.waitKey(1) & 0xFF == ord("w"):
        break
        
avg = sum(avgFPS)/len(avgFPS)
print("Avg. FPS = ", avg)
cap.release() 
cv.destroyAllWindows() 


# In[ ]:





# In[ ]:




