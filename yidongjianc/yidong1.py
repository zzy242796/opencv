import numpy as np
import cv2 as cv
import argparse
# '''
# 使用CamShift算法跟踪物体，该算法改进了MeanShift，它的窗口大小会进行自定义调整
# '''
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

ret,frame = cap.read()
#定义一个范围作为要追踪的物体，在这选取的是一辆车
x, y, w, h = 306, 194, 80, 40 # simply hardcoded the values
track_window = (x, y, w, h)
# 从第一帧frame中，把范围中的图片提取出来
roi = frame[y:y+h, x:x+w]
# 转化为hsv颜色，因为画直方图一般会用这个色彩格式
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
#生成一个蒙版，把不在范围内的颜色筛去
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
#生成直方图
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
#进行直方图归一化
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
# 设置终止标准，10 次迭代或移动至少 1 像素
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
    #读取视频下一帧
    ret, frame = cap.read()
    #ret用来判断视频是否读取成功
    if ret == True:
        # 保持跟上面一致的色彩格式hsv
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # 这一步计算hist的反投影，是为了下面作为输入便于读取
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # 使用CamShift找到匹配的窗口
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        #下面的代码就是用一个四边形把识别到的物体框出来
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame,[pts],True, 255,2)
        cv.imshow('img2',img2)
        k = cv.waitKey(30) & 0xff
        # 等待30毫秒，按ESC退出
        if k == 27:
            break
    else:
        break