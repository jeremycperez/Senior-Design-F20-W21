#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

new_frame_time = 0
prev_frame_time = 0
avgFPS = []
i = 0

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 100, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 10, maxLineGap=100)
    for line in lines:
        x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 4)
    
    new_frame_time = time.time()  
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time
    
    if i < 500:
        avgFPS.append(fps)
        i+=1

    
    #cv2.imshow("linesEdges", edges)
    cv2.imshow("linesDetected", img)
    if cv2.waitKey(1) & 0xFF == ord("w"):
        break

avg = sum(avgFPS)/len(avgFPS)
print("Avg. FPS = ", avg)
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




