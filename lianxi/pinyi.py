# #图像平移
# import cv2
# import numpy as np

# hzw = cv2.imread('./222.jpg')
# h,w,ch = hzw.shape
# M = np.float32([[1,0,300],[0,1,0]])
# new = cv2.warpAffine(hzw, M,(w,h))

# cv2.imshow('hzw',hzw)
# cv2.imshow('new',new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#变换矩阵  旋转
import cv2
import numpy as np

hzw = cv2.imread('./222.jpg')
h,w,ch = hzw.shape

#  中心点 角度  缩放比例
# M = cv2.getRotationMatrix2D((100,100),15,0.5)
M = cv2.getRotationMatrix2D((w/2,h/2),15,0.5)


new = cv2.warpAffine(hzw, M,(w,h))

cv2.imshow('new',new)
cv2.waitKey(0)
cv2.destroyAllWindows()



# #斜拉图片
# import cv2
# import numpy as np

# hzw = cv2.imread('./222.jpg')
# h,w,ch = hzw.shape

# src = np.float32([[400,300],[800,300],[400,1000]])
# dst = np.float32([[200,400],[600,500],[150,1100]])

# M = cv2.getAffineTransform(src,dst)


# new = cv2.warpAffine(hzw, M,(w,h))

# cv2.imshow('new',new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# #切割图片
# import cv2
# import numpy as np

# hzw = cv2.imread('./777.jpg')
# h,w,ch = hzw.shape
# print(h,w)
# src = np.float32([[300,250],[1100,250],[300,550],[1100,550]])
# dst = np.float32([[0,0],[800,0],[0,300],[800,300]])

# M = cv2.getPerspectiveTransform(src,dst)

# new = cv2.warpPerspective(hzw, M,(800,300))

# cv2.imshow('new',new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()