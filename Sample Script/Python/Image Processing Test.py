#!/usr/bin/env python
# coding: utf-8

# In[21]:


## PRESS 'q' FOR QR CODE SCANNER
## PRESS 'o' FOR OBJECT DETECTION
## PRESS 'l' FOR LINE DETECTION
## PRESS 'w' TO STOP

from __future__ import print_function
import cv2 
import time
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

prev_frame_time = 0
new_frame_time = 0
font = cv2.FONT_HERSHEY_SIMPLEX 
avgFPS = []
i = 0
font = cv2.FONT_HERSHEY_SIMPLEX
mode = 'obj'


def decode(im) : 
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    # Print results
    #for obj in decodedObjects:
        #print('Type : ', obj.type)
       # print('Data : ', obj.data,'\n')     
    return decodedObjects

while True:
    if cv2.waitKey(1) & 0xFF == ord("w"):
        break
    elif (cv2.waitKey(1) & 0xFF == ord("o")) and mode != 'obj':
        mode = 'obj'
        cv2.destroyAllWindows()
        #time.sleep(2)
    elif (cv2.waitKey(1) & 0xFF == ord("l")) and mode != 'line':
        mode = 'line'
        cv2.destroyAllWindows()
        #time.sleep(2)
    elif (cv2.waitKey(1) & 0xFF == ord("q")) and mode != 'qr':
        mode = 'qr'
        cv2.destroyAllWindows()
        #time.sleep(2)
    
    new_frame_time = time.time()  
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time

    if i < 1000:
        avgFPS.append(fps)
        i+=1

    fps = int(fps)  
    fps = str(fps) 
        
    if mode == 'obj':
        success, img = cap.read()
        noise = cv2.bilateralFilter(img,9,75,75)
        edge = cv2.Canny(noise, 50, 150)    
        kernel = np.ones((3,3), np.uint8)
        dilated = cv2.dilate(edge,kernel,iterations=1)

        contours, h = cv2.findContours(dilated, 1, 2)
        contours= sorted(contours, key = cv2.contourArea, reverse = True)[:1]
        pt = (180, 3 * img.shape[0] // 4)

        for cnt in contours:
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            # print len(cnt)
            if len(approx) >= 4 and len(approx) <= 8:
                cv2.drawContours(img,[cnt],-1,(255,0,0),3)
                cv2.putText(img,'Cube', pt ,font, 2, [0,255, 255], 2)

        cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA) 
        cv2.namedWindow("Shape", cv2.WINDOW_NORMAL)
        cv2.imshow('Shape',img)

        corners    = cv2.goodFeaturesToTrack(edge,6,0.06,25)
        corners    = np.float32(corners)

        for    item in    corners:
            x,y    = item[0]
            cv2.circle(img,(x,y),10,255,-1)

        #cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA) 
        #cv2.namedWindow("Corners", cv2.WINDOW_NORMAL)
        #cv2.imshow("Corners",img)



        #cv2.putText(edge, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA) 
        #cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
        #cv2.imshow("Webcam", edge)

    if mode == 'qr':
        # Capture frame-by-frame
        success, img = cap.read()
        # Our operations on the frame come here
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        decodedObjects = decode(im)

        for decodedObject in decodedObjects: 
            points = decodedObject.polygon

            # If the points do not form a quad, find convex hull
            if len(points) > 4 : 
              hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
              hull = list(map(tuple, np.squeeze(hull)))
            else : 
              hull = points;

            # Number of points in the convex hull
            n = len(hull)     
            # Draw the convext hull
            for j in range(0,n):
              cv2.line(img, hull[j], hull[ (j+1) % n], (255,0,0), 3)

            x = decodedObject.rect.left
            y = decodedObject.rect.top

            #print(x, y)

            #print('Type : ', decodedObject.type)
            #print('Data : ', decodedObject.data,'\n')

            barCode = str(decodedObject.data)
            cv2.putText(img, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)

        # Display the resulting frame
        cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA) 
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.imshow('frame',img)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('s'): # wait for 's' key to save 
            cv2.imwrite('Capture.png', img)
    
    elif mode == 'line':
        success, img = cap.read()
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img, 50, 100, apertureSize=3)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 10, maxLineGap=100)
        for line in lines:
            x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 4)

        #cv2.imshow("linesEdges", edges)
        cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA) 
        cv2.namedWindow("linesDetected", cv2.WINDOW_NORMAL)
        cv2.imshow("linesDetected", img)   

avg = sum(avgFPS)/len(avgFPS)
print("Avg. FPS = ", avg)
cap.release() 
cv2.destroyAllWindows() 

