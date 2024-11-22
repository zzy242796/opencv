import torch
import cv2

# 加载训练好的YOLOv5模型
model = torch.load('F:\opencv\lianxi\yolov5s.pt')  # 或者你的自定义模型路径

# 读取图像
img = cv2.imread('F:\opencv\picture\wuti.jpg')

# 使用YOLOv5模型进行预测
results = model(img)

# 打印预测结果
results.print()  # 或者使用results.xyxy[0]获取检测框的坐标和置信度

# 可视化检测结果
results.show()