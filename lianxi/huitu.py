#绘制图形

# 直线  line(img(图片),pt1(起始点),pt2(结束点),color,thickness(线的粗细),lineType(类型)(-1,4,8,16),shift坐标缩放比例))

# 矩形  rectangle(.....) 参数同line

# 圆    circle(img,center,radius,color,thickness,lineType,shift)

# 椭圆  elipse(img,中心点，长宽半径，角度，从哪个角度开始，从哪个角度结束，....)

#多边形 polylines(img,[pts],isClosed(True,False),color,thickness......)
#       pts = np.array([(250,10),(150,100),(450,100)], np.int32)   32位 
#填充多边形  fillPoly


import cv2
import numpy as np

img = np.zeros((600,1000,3),np.uint8)
## 直线
# cv2.line(img,(10,20),(300,400),(0,0,255),5,4)
# cv2.line(img,(80,100),(380,480),(0,0,255),5,16)

# 矩形
cv2.rectangle(img,(80,100),(380,440),(0,120,70),2,16)

# 圆
cv2.circle(img,(200,200),50,(0,0,255))

# 椭圆
cv2.ellipse(img,(200,200),(100,60),0,0,360,(0,255,0))

#多边形
pts = np.array([(250,100),(150,200),(200,100)], np.int32)
cv2.polylines(img,[pts],True,(255,0,0))

#填充多边形
pts2 = np.array([(300,100),(200,200),(400,100)], np.int32)
cv2.fillPoly(img,[pts2],(255,0,0))



cv2.imshow('draw',img)
cv2.waitKey(0)
cv2.destroyAllWindows()