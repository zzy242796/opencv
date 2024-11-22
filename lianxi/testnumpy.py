# import numpy as np
# #矩阵
# a = np.array([1,2,3])
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
# print(b)

# #zero矩阵 全0
# c = np.zeros((4, 4), np.uint8)
# print(c)

# #全1
# d = np.ones((4,4),np.uint8)
# print(d)

# #全定义
# e = np.full((4,4),12,np.uint8)
# print(e)

# #单位矩阵  斜对角线为1
# f = np.identity(4)
# print(f)

# #非正方单位矩阵
# g = np.eye(3,5,k=0)
# print(g)
# g = np.eye(3,5,k=1)
# print(g)


# -----------------------------------------------

# #黑白变色

# import numpy as np
# import cv2

# #读元素值
# img = np.zeros((480, 640), np.uint8)
# print(img[100,100])

# #赋值，改变颜色
# count = 0
# while count < 200:
#     img[count, 100] = 255
#     count = count + 1

# cv2.imshow('img',img)
# key = cv2.waitKey(0)
# if key & 0xFF == ord('q'):
#     cv2.destroyAllWindows()


# #彩色变色
# import numpy as np
# import cv2

# #读元素值
# img = np.zeros((480, 640, 3), np.uint8)
# print(img[100,100])

# #赋值，改变颜色
# count = 0
# while count < 200:
#     # img[count, 100, 0] = 255   #BGR 0为B
#     img[count, 100] = [0, 0, 255]
#     count = count + 1

# cv2.imshow('img',img)
# key = cv2.waitKey(0)
# if key & 0xFF == ord('q'):
#     cv2.destroyAllWindows()



#部分方块变色
import numpy as np
import cv2

#生成窗口
img = np.zeros((480, 640, 3), np.uint8)

#大小
roi = img[100:400, 100:600]
#全红
# roi[:,:] = [0,0,255]
roi[:] = [0,0,255]
#部分块变绿色
roi[10:200,10:200] = [0,255,0]

cv2.imshow('img',roi)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()