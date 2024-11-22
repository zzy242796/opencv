# # 基于OpenCV的背景减法器实时跟踪物体


# import cv2
# import numpy as np

# # KNN
# KNN_subtractor = cv2.createBackgroundSubtractorKNN(detectShadows=True)

# MOG2_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows=True)  # 从检测到的物体中排除阴影区域

# # 选择背景减法器
# bg_subtractor = MOG2_subtractor

# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("无法打开摄像头")
#     exit()

# # 消抖参数
# stable_frame_count = 5  # 要求的稳定帧数
# current_stable_count = 0  # 当前稳定帧计数
# last_max_contour = None  # 上一帧的最大轮廓

# # 背景更新参数
# update_background_interval = 3  # 每隔几帧更新背景
# frame_count = 0  # 当前帧计数

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("无法读取第一帧")
#         exit()

#     # 更新背景的逻辑
#     if frame_count % update_background_interval == 0:
#         # 每帧都用于计算前景掩码，并用于更新背景
#         foreground_mask = bg_subtractor.apply(frame)

#         # 如果大于120像素则为255，小于则为0
#         # 创建二值图像，仅包含黑白像素
#         ret, treshold = cv2.threshold(foreground_mask.copy(), 120, 255, cv2.THRESH_BINARY)

#         # 膨胀操作扩展或加厚图像中的感兴趣区域
#         dilated = cv2.dilate(treshold, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)

#         # 查找轮廓
#         contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         # 检查每个轮廓，如果超过某个值则绘制边界框
#         max_area = 0
#         max_contour = None

#         for contour in contours:
#             # 如果面积超过某个值，则检查最大区域
#             if cv2.contourArea(contour) > 50:
#                 area = cv2.contourArea(contour)
#                 if area > max_area:
#                     max_area = area
#                     max_contour = contour

#         # 检查最大轮廓是否稳定
#         if max_contour is not None:
#             if last_max_contour is not None and cv2.contourArea(last_max_contour) > 50:
#                 # 如果检测到相同的轮廓，增加稳定计数
#                 current_stable_count += 1
#             else:
#                 # 如果检测到不同的轮廓，重置计数
#                 current_stable_count = 0

#             # 更新上一次最大轮廓
#             last_max_contour = max_contour

#             # 如果稳定帧数达到要求，则绘制矩形框
#             if current_stable_count >= stable_frame_count:
#                 (x, y, w, h) = cv2.boundingRect(max_contour)
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
#         else:
#             # 如果没有找到轮廓，重置计数
#             current_stable_count = 0
#             last_max_contour = None

#     frame_count += 1  # 增加帧计数

#     # 显示图像
#     cv2.imshow("Subtractor", foreground_mask)
#     cv2.imshow("threshold", treshold)
#     cv2.imshow("detection", frame)

#     if cv2.waitKey(30) & 0xff == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np

# KNN
KNN_subtractor = cv2.createBackgroundSubtractorKNN(detectShadows=True)
MOG2_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows=True)  # 从检测到的物体中排除阴影区域

# 选择背景减法器
bg_subtractor = MOG2_subtractor

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 消抖参数
stable_frame_count = 5  # 要求的稳定帧数
current_stable_count = 0  # 当前稳定帧计数
last_max_contour = None  # 上一帧的最大轮廓

# 背景更新参数
update_background_interval = 3  # 每隔几帧更新背景
frame_count = 0  # 当前帧计数

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法读取第一帧")
        exit()

    # 更新背景的逻辑
    if frame_count % update_background_interval == 0:
        # 每帧都用于计算前景掩码，并用于更新背景
        foreground_mask = bg_subtractor.apply(frame)

        # 如果大于120像素则为255，小于则为0
        # 创建二值图像，仅包含黑白像素
        ret, treshold = cv2.threshold(foreground_mask.copy(), 120, 255, cv2.THRESH_BINARY)

        # 膨胀操作扩展或加厚图像中的感兴趣区域
        dilated = cv2.dilate(treshold, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)

        # 查找轮廓
        contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 检查每个轮廓，如果超过某个值则绘制边界框
        max_area = 0
        max_contour = None

        for contour in contours:
            # 如果面积超过某个值，则检查最大区域
            if cv2.contourArea(contour) > 50:
                area = cv2.contourArea(contour)
                if area > max_area:
                    max_area = area
                    max_contour = contour

        # 检查最大轮廓是否稳定
        if max_contour is not None:
            if last_max_contour is not None and cv2.contourArea(last_max_contour) > 50:
                # 如果检测到相同的轮廓，增加稳定计数
                current_stable_count += 1
            else:
                # 如果检测到不同的轮廓，重置计数
                current_stable_count = 0

            # 更新上一次最大轮廓
            last_max_contour = max_contour

            # 如果稳定帧数达到要求，则绘制矩形框
            if current_stable_count >= stable_frame_count:
                (x, y, w, h) = cv2.boundingRect(max_contour)
                frame_height, frame_width = frame.shape[:2]
                
                # 检查矩形框是否占满整个屏幕
                if not (w >= frame_width and h >= frame_height):
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        else:
            # 如果没有找到轮廓，重置计数
            current_stable_count = 0
            last_max_contour = None

    frame_count += 1  # 增加帧计数

    # 显示图像
    cv2.imshow("Subtractor", foreground_mask)
    cv2.imshow("threshold", treshold)
    cv2.imshow("detection", frame)

    if cv2.waitKey(30) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
