# import cv2
# import numpy as np

# img = cv2.imread('222.png')
# img = cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)
# #转灰度
# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #二值化
# ret, dst = cv2.threshold(img1,240,255,cv2.THRESH_BINARY)
# # #白变黑，黑变白
# # ret, dst = cv2.threshold(img1,120,255,cv2.THRESH_BINARY_INV)


# cv2.imshow('img',img)
# cv2.imshow('gray',img1)
# cv2.imshow('bin',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 二值化  自适应阈值
# import cv2
# import numpy as np

# img = cv2.imread('222.png')
# new1 = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# #转灰度
# img1 = cv2.cvtColor(new1,cv2.COLOR_BGR2GRAY)
# #二值化   可改13
# dst = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,0)

# cv2.imshow('new1',new1)
# cv2.imshow('gray',img1)
# cv2.imshow('bin',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()






import cv2
import numpy as np

img = cv2.imread('222.png')
img = cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)
#转灰度
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret, dst = cv2.threshold(img1,220,255,cv2.THRESH_BINARY)
#卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
#闭运算
b = cv2.morphologyEx(dst,cv2.MORPH_CLOSE,kernel)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('b',b)

cv2.waitKey(0)
cv2.destroyAllWindows()
