##     图片的加减法
# import cv2
# import numpy as np

# b = cv2.imread('./777.jpg')
# f = cv2.imread('./222.jpg')

# print(b.shape)
# print(f.shape)

# new_f = f[150:937,260:1660]
# print(new_f.shape)

# #加法
# new_img = cv2.add(b,new_f)
# cv2.imshow('new_img',new_img)

# #减法
# new_img2 = cv2.subtract(b,new_f)
# cv2.imshow('new_img2', new_img2)

# # 乘法   cv2.multiply
# # 除法   cv2.dilate

# b += 50
# cv2.imshow('b',b)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



#两个图片融合到一起
import cv2
import numpy as np

b = cv2.imread('./777.jpg')
f = cv2.imread('./222.jpg')
new_f = f[150:937,260:1660]

# cv2.addWeighted(img,alpha,img,bate,gamma)
new_img = cv2.addWeighted(new_f,0.2,b,0.8,0)   #权重
cv2.imshow('new_img',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()