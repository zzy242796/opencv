import cv2
import numpy as np

# 定义形状检测函数
def ShapeDetection(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓点
    for obj in contours:
        area = cv2.contourArea(obj)  # 计算轮廓内区域的面积
        cv2.drawContours(imgContour, obj, -1, (255, 0, 0), 4)  # 绘制轮廓线
        perimeter = cv2.arcLength(obj, True)  # 计算轮廓周长
        approx = cv2.approxPolyDP(obj, 0.02 * perimeter, True)  # 获取轮廓角点坐标
        CornerNum = len(approx)   # 轮廓角点的数量
        x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度

        # 轮廓对象分类
        if CornerNum == 3:
            objType = "triangle"
        elif CornerNum == 4:
            if w == h:
                objType = "Square"
            else:
                objType = "Rectangle"
        elif CornerNum > 4:
            objType = "Circle"
        else:
            objType = "N"

        cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 绘制边界框
        cv2.putText(imgContour, objType, (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 1)  # 绘制文字

# 启动摄像头
cap = cv2.VideoCapture(0)

while True:
    # 从摄像头捕获一帧
    ret, frame = cap.read()
    if not ret:
        break

    imgContour = frame.copy()  # 复制原始帧用于绘制轮廓

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转灰度图
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # 高斯模糊
    imgCanny = cv2.Canny(imgBlur, 60, 60)  # Canny算子边缘检测

    ShapeDetection(imgCanny, imgContour)  # 形状检测

    # 显示结果
    cv2.imshow("Original Frame", frame)
    # cv2.imshow("Canny Edges", imgCanny)
    cv2.imshow("Shape Detection", imgContour)

    # 按'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
cv2.destroyAllWindows()
