# import cv2
# import numpy as np

# img = cv2.imread('F:\\picture\\wwww.jpg')

# #浅拷贝
# # img2=img
# img2 = img.view()

# #深拷贝
# img3 = img.copy()

# img[10:100,10:100]=[0,0,255]

# # cv2.imshow('img',img)
# # cv2.imshow('img2',img2)
# # cv2.imshow('img3',img3)
# cv2.imshow('img', np.hstack((img,img2,img3)))  #横 并排显示
# # cv2.imshow('img', np.vstack((img,img2,img3)))  #竖 并排显示

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#-------------------------------------------------------------------------------------------

#图像的分割与融合

import cv2
import numpy as np
img = np.zeros((200,200,3),np.uint8)
#分割通道
b, g, r = cv2.split(img)
#修改部分颜色
b[10:100,10:100] = 255
g[10:100,10:100] = 255
#合并通道
img2 = cv2.merge((b, g, r))
cv2.imshow('img',np.hstack((b,g)))
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()