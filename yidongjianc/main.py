# import cv2
# import processor

# if __name__=="__main__":
#     cap = cv2.VideoCapture(0)

#     proc = processor.ImageProcessorCloseLoop(tracker_type="MIL")

#     ret, frame = cap.read()
#     if not ret:
#         exit(1)

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         bboxes = proc.process_one_frame(frame)
#         for bbox in bboxes:
#             x, y, w, h = bbox
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0xff), 1)

#         cv2.imshow("Video", frame)
#         key = cv2.waitKey(10)
#         if key == ord(" "):
#             k1 = cv2.waitKey()


#     cap.release()
#     cv2.destroyAllWindows()



import cv2  # 导入OpenCV库
import processor  # 导入自定义的处理模块

if __name__=="__main__":  # 确保以下代码仅在此文件被直接运行时执行
    cap = cv2.VideoCapture(0)  # 通过摄像头捕获视频，参数0表示默认摄像头

    proc = processor.ImageProcessorCloseLoop(tracker_type="MIL")  # 创建一个处理器实例，使用MIL跟踪算法

    while True:  # 循环读取视频帧
        ret, frame = cap.read()  # 读取下一帧图像
        if not ret:  # 如果未成功读取图像
            break  # 跳出循环

        bboxes = proc.process_one_frame(frame)  # 处理当前帧，获取检测到的边界框
        if bboxes:  # 确保检测到至少一个边界框
            # 找到面积最大的边界框
            largest_bbox = max(bboxes, key=lambda bbox: bbox[2] * bbox[3])  # bbox[2]为宽，bbox[3]为高
            x, y, w, h = largest_bbox  # 解包最大的边界框的坐标和尺寸
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0xff), 1)  # 在图像上绘制矩形框

        cv2.imshow("Video", frame)  # 显示当前帧
        key = cv2.waitKey(10)  # 等待10毫秒检查按键
        if key == ord(" "):  # 如果按下空格键
            k1 = cv2.waitKey()  # 等待其他按键输入

    cap.release()  # 释放摄像头资源
    cv2.destroyAllWindows()  # 关闭所有OpenCV窗口
