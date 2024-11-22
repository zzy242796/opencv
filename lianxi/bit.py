# import cv2
# import numpy as np

# img = np.zeros((400,400),np.uint8)


# img[50:200,50:200] = 255

# #非运算
# new_img = cv2.bitwise_not(img)

# cv2.imshow('img',img)
# cv2.imshow('new_img',new_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# import cv2
# import numpy as np

# img = np.zeros((400,400),np.uint8)
# img2 = np.zeros((400,400),np.uint8)


# img[50:200,50:200] = 255
# img2[150:300,150:300] = 255

# #与运算
# new_img = cv2.bitwise_and(img,img2)

# cv2.imshow('img2',img2)
# cv2.imshow('img',img)
# cv2.imshow('new_img',new_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# import cv2
# import numpy as np

# img = np.zeros((400,400),np.uint8)
# img2 = np.zeros((400,400),np.uint8)


# img[50:200,50:200] = 255
# img2[150:300,150:300] = 255

# #或运算
# new_img = cv2.bitwise_or(img,img2)

# cv2.imshow('img2',img2)
# cv2.imshow('img',img)
# cv2.imshow('new_img',new_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np


img = np.zeros((400,400),np.uint8)
img2 = np.zeros((400,400),np.uint8)


img[50:200,50:200] = 255
img2[150:300,150:300] = 255

#异或运算
new_img = cv2.bitwise_xor(img,img2)

cv2.imshow('img2',img2)
cv2.imshow('img',img)
cv2.imshow('new_img',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()