import cv2
import numpy as np

# cap = cv2.VideoCapture('ddd.mp4')
cap = cv2.VideoCapture(700) #摄像头

bgsubmog = cv2.createBackgroundSubtractorMOG2(history=100)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

while True:
    ret, cc = cap.read()

    if(ret == True):
        #灰度
        frame = cv2.cvtColor(cc,cv2.COLOR_BGR2GRAY)
        #去噪（高斯）
        blur = cv2.GaussianBlur(frame,(21,21),7)
        #去背景
        frame = bgsubmog.apply(frame)
        #腐蚀
        frame = cv2.erode(frame,kernel,iterations=1)
        # #膨胀
        frame = cv2.dilate(frame,kernel,iterations=3)
        # erode = cv2.erode(dilate,kernel,iterations=3)
        # dilate = cv2.dilate(erode,kernel,iterations=7)
        # erode = cv2.erode(dilate,kernel,iterations=4)
        # dilate = cv2.dilate(erode,kernel,iterations=10)
        #闭操作，去掉物体内部的小块
        frame = cv2.morphologyEx(frame,cv2.MORPH_CLOSE,kernel)
        frame = cv2.morphologyEx(frame,cv2.MORPH_CLOSE,kernel)

        #查找轮廓
        cnts,h = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for (i,c) in enumerate(cnts):
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(cc,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('close',cc)
        # cv2.imshow('dilate',dilate)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()