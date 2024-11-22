# import cv2
# import numpy as np

# # 读取图像
# image = cv2.imread('d.jpg')
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

# # 将图像从 BGR 转换到 HSV 颜色空间
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # 定义红色在 HSV 空间的上下界限
# lower_red = np.array([0, 120, 70])
# upper_red = np.array([10, 255, 255])

# # 创建掩码，只保留红色
# mask = cv2.inRange(hsv_image, lower_red, upper_red)

# #膨胀
# mask = cv2.dilate(mask,kernel,iterations=2)
# #腐蚀
# mask = cv2.erode(mask,kernel,iterations=3)

# # 应用掩码到原图像
# result = cv2.bitwise_and(image, image, mask=mask)

# # 显示结果
# cv2.imshow('Original Image', image)
# cv2.imshow('Mask', mask)
# cv2.imshow('Result', result)

# # 等待按键，然后关闭所有窗口
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#摄像头识别红色
import cv2
import numpy as np

# 定义红色在HSV颜色空间的阈值范围
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# 启动摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头的帧
    ret, frame = cap.read()
    
    # 将BGR颜色空间转换为HSV颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 创建红色掩膜
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    
    # 对掩膜应用形态学操作以去除噪声
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    # 寻找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 找到最大的轮廓
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour
    
    # 如果存在最大的轮廓，则绘制边界框和中心点
    if max_contour is not None:
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        # 计算中心点坐标
        center_x, center_y = x + w // 2, y + h // 2
        print(f"Detected red object center: ({center_x}, {center_y})")
        
        # 在图像上绘制中心点
        cv2.circle(frame, (int(center_x), int(center_y)), 5, (0, 0, 255), -1)
        
        # 也可以在中心点上绘制十字标记
        cv2.line(frame, (int(center_x) - 5, int(center_y)), (int(center_x) + 5, int(center_y)), (0, 255, 0), 1)
        cv2.line(frame, (int(center_x), int(center_y) - 5), (int(center_x), int(center_y) + 5), (0, 255, 0), 1)

    # 显示结果
    cv2.imshow('Red Detection', frame)
    
    # 按'q'退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭所有OpenCV窗口
cv2.destroyAllWindows()