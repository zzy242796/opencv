# 轮廓 

# 轮廓查找  findContours  
# RETR_EXTERNAL = 0 ,表示只检测外轮廓
# RETR_LIST = 1, 检测的轮廓不建立等级关系
# RETR_CCOMP = 2, 每层最多两级
# RETR_TREE = 3, 按树形存储轮廓
# CHAIN_APPROX_NONE  保存所有轮廓上的点
# CHAIN_APPROX_SIMPLE  只保存角点

#轮廓绘制  drawContours(img,-1 绘制所有轮廓，color，-1 线宽 全部填充)

# import cv2
# import numpy as np

# img = cv2.imread('hak.jpg')
# #变黑白
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #二值化
# ret, binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

# #轮廓查找
# contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # print(contours)

# #绘制轮廓
# cv2.drawContours(img,contours,-1,(0,0,255),1)

# cv2.imshow('img',img)
# # cv2.imshow('bin',binary)

# cv2.waitKey(0)
# cv2.destroyAllWindows()





#--------------------------------------------------------------------------------------------





#轮廓面积周长  arcLength(curve 轮廓,closed 是否是闭合轮廓)

# import cv2
# import numpy as np

# img = cv2.imread('zzz.jpg')
# #变黑白
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #二值化
# ret, binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

# #轮廓查找
# contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # print(contours)

# #绘制轮廓
# cv2.drawContours(img,contours,1,(0,0,255),1)

# #计算面积
# area = cv2.contourArea(contours[1])
# print("area=%d"%(area))

# #计算周长
# len = cv2.arcLength(contours[1],True)
# print("len=%d"%(len))

# cv2.imshow('img',img)
# # cv2.imshow('bin',binary)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




# -----------------------------------------------------------------------------------------------



#多边形逼近与凸包 

# 逼近 apprxoPolyDP(curve 轮廓,epsilon 精度，closed 是否闭合)
# 凸包 convexHull(points 轮廓，clockwise 顺时针绘制)

# import cv2
# import numpy as np
# def drawShape(src, points):
#     i = 0
#     while i < len(points):
#         if(i == len(points) - 1):
#             x,y = points[i][0]
#             x1,y1 = points[0][0]
#             cv2.line(src,(x,y),(x1,y1),(0,0,255),2)
#         else:
#             x,y = points[i][0]
#             x1,y1 = points[i+1][0]
#             cv2.line(src,(x,y),(x1,y1),(0,0,255),2)
#         i = i + 1

# img = cv2.imread('shou.jpg')
# #变黑白
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #二值化
# ret, binary = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

# #轮廓查找
# contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # print(contours)

# #绘制轮廓
# cv2.drawContours(img,contours,-1,(0,255,0),1)

# #逼近
# e = 5  #精度
# approx = cv2.approxPolyDP(contours[0],e,True)

# #凸包
# hull = cv2.convexHull(contours[0])

# #画直线
# drawShape(img,approx)
# drawShape(img,hull)



# cv2.imshow('img',img)
# # cv2.imshow('bin',binary)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




# -------------------------------------------------------------------------------------------




#外接矩形  框框

#最小矩形  minAreaRect(points)   返回值：RotatedRect （ x,y   width,height  angle角度）
#最大矩形  boundingRect(array)   返回值：Rect

import cv2
import numpy as np
def drawShape(src, points):
    i = 0
    while i < len(points):
        if(i == len(points) - 1):
            x,y = points[i][0]
            x1,y1 = points[0][0]
            cv2.line(src,(x,y),(x1,y1),(0,0,255),2)
        else:
            x,y = points[i][0]
            x1,y1 = points[i+1][0]
            cv2.line(src,(x,y),(x1,y1),(0,0,255),2)
        i = i + 1

img = cv2.imread('F:/opencv/picture/ccc.png')
#变黑白
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret, binary = cv2.threshold(gray,250,255,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# print(contours)

#最小矩形
r = cv2.minAreaRect(contours[1])
#画出矩形
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)

#最大矩形
x,y,w,h = cv2.boundingRect(contours[1])
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



cv2.imshow('img',img)
# cv2.imshow('bin',binary)

cv2.waitKey(0)
cv2.destroyAllWindows()