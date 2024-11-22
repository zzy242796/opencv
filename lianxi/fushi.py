# #腐蚀  erode

# import cv2
# import numpy as np

# img = cv2.imread('222.png')

# #卷积核
# kernel = np.ones((3,3),np.uint8)

# dst = cv2.erode(img,kernel,iterations=1)

# cv2.imshow('img',img)
# cv2.imshow('dst',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




# MORPH_RECT  矩形
# MORPH_ELLIPSE  椭圆
#MORPH_CROSS   十字架

# import cv2
# import numpy as np

# img = cv2.imread('ww.png')

# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
# print(kernel)
# dst = cv2.erode(img,kernel,iterations=1)

# cv2.imshow('img',img)
# cv2.imshow('dst',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -------------------------------------------------------


# 膨胀  dilate

# import cv2
# import numpy as np

# img = cv2.imread('ww.png')

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
# # print(kernel)
# dst = cv2.dilate(img,kernel,iterations=1)

# cv2.imshow('img',img)
# cv2.imshow('dst',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# ---------------------------------------------------------------



#开运算  morphologyEx   MORPH_OPEN

# import cv2
# import numpy as np

# img = cv2.imread('ww.png')

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
# # print(kernel)
# dst = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

# cv2.imshow('img',img)
# cv2.imshow('dst',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ------------------------------------------------------------------



#闭运算   morphologyEx     MORPH_CLOSE
 
# import cv2
# import numpy as np

# img = cv2.imread('ww.png')

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
# # print(kernel)
# dst = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

# cv2.imshow('img',img)
# cv2.imshow('dst',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -------------------------------------------------------------------------


#形态学梯度 = 原图 - 腐蚀   轮廓  MORPH_GRADIENT

# import cv2
# import numpy as np

# img = cv2.imread('ww.png')

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
# # print(kernel)
# dst = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

# cv2.imshow('img',img)
# cv2.imshow('dst',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ---------------------------------------------------------------------------------


#顶帽运算 = 原图 - 开运算  去大保小 显示噪点  MORPH_TOPHAT

# import cv2
# import numpy as np

# img = cv2.imread('hak.jpg')

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
# # print(kernel)
# dst = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

# cv2.imshow('img',img)
# cv2.imshow('dst',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ------------------------------------------------------------------------------


#黑帽运算 = 原图 - 闭运算

# import cv2
# import numpy as np

# img = cv2.imread('hak.jpg')

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
# # print(kernel)
# dst = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

# cv2.imshow('img',img)
# cv2.imshow('dst',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
