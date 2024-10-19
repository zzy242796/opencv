##图片

# import cv2

# # 加载Haar级联分类器
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # 读取图像
# img = cv2.imread('rl.jpg')

# # 转换为灰度图像
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 检测图像中的人脸
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# # 在检测到的人脸周围画矩形框
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# # 显示图像
# cv2.imshow('Face Detection', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -------------------------------------------------------------------------------------------------------------


#视频检测

import cv2

# 指定Haar级联分类器文件路径
face_cascade_path = 'haarcascade_frontalface_default.xml'

# 加载Haar级联分类器
# face_cascade = cv2.CascadeClassifier(face_cascade_path)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 启动摄像头
cap = cv2.VideoCapture(0)  # 参数0通常表示系统的默认摄像头

while True:
    # 逐帧捕获
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用Haar分类器检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 在检测到的人脸周围绘制矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 显示结果帧
    cv2.imshow('Face Detection', frame)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭所有OpenCV窗口
cv2.destroyAllWindows()