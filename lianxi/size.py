# #图像缩放
# import cv2
# import numpy as np

# hzw = cv2.imread('./777.jpg')
# # new = cv2.resize(hzw,(700,393))
# new = cv2.resize(hzw,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

# print(hzw.shape)

# cv2.imshow('hzw',hzw)
# cv2.imshow('new',new)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



#图像翻转
#flip(img,flipCode)
#flipCode==0  上下
#flipCode>0   左右
#flipCode<0   上下+左右
import cv2
import numpy as np

hzw = cv2.imread('ddd.JPG')

new = cv2.flip(hzw,1)

cv2.imshow('hzw',hzw)
cv2.imshow('new',new)

cv2.waitKey(0)
cv2.destroyAllWindows()


#图像旋转
#rotate(img,rotateCode)
#ROTATE_90_CLOCKWISE           顺时针旋转90°
#ROTATE_180                    顺时针180
#ROTATE_90_COUNTERCLOCKWISE    逆时针90
# import cv2
# import numpy as np

# hzw = cv2.imread('./777.jpg')

# new = cv2.rotate(hzw,cv2.ROTATE_90_COUNTERCLOCKWISE)

# cv2.imshow('new',new)

# cv2.waitKey(0)
# cv2.destroyAllWindows()