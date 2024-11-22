import cv2
import numpy as np
from PIL import ImageFont,ImageDraw,Image

# 读取图像
image = cv2.imread('ccc.png')

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用高斯模糊，减少噪声
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# 应用Canny边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 寻找轮廓
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 遍历轮廓，寻找矩形
for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    area = cv2.contourArea(contour)
    text = str(area)  # 将变量转换为字符串
    cv2.putText(image,text,(70,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0))

# 显示原始图像
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()