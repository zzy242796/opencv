#拼接两张图片

import cv2
import numpy as np

img1 = cv2.imread('mmm.png')
img2 = cv2.imread('nnn.png')

img1 = cv2.resize(img1,(640,480))
img2 = cv2.resize(img2,(640,480))

inputs = np.hstack((img1,img2))


cv2.imshow('inputs',inputs)   #两张图横向显示

cv2.waitKey(0)
cv2.destroyAllWindows()