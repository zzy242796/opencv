import cv2
# cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)   #创建窗口

cv2.namedWindow('video', cv2.WINDOW_NORMAL)   #设置窗口大小时用WINDOW_NORMAL
cv2.resizeWindow('video',720, 560)

#获取视频设备

cap = cv2.VideoCapture(1) #摄像头

# cap = cv2.VideoCapture("F:\\picture\\hzw.mp4")

while True:
    #从摄像头读视频帧
    ret, frame = cap.read()
    cv2.imshow('video', frame) #展示视频
    #等待键盘事件
    key = cv2.waitKey(22)  #在此修改读帧频率
    if(key & 0xFF == ord('q')):
       
        break
#释放视频
cap.release()
#释放窗口
cv2.destroyAllWindows()



# import cv2
# #创建videowriter为写多媒体文件
# fourcc=cv2.VideoWriter_fourcc(*'MPEG')
# vw = cv2.VideoWriter('out.mp4', fourcc , 25, (640, 480))  #输出路径  获取的视频  视频帧 摄像头像素
# # cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)   #创建窗口

# cv2.namedWindow('video', cv2.WINDOW_NORMAL)   #设置窗口大小时用WINDOW_NORMAL
# cv2.resizeWindow('video', 640, 360)

# #获取视频设备

# cap = cv2.VideoCapture(0) #摄像头

# # cap = cv2.VideoCapture("F:\\picture\\hzw.mp4")

# while cap.isOpened():
#     #从摄像头读视频帧
#     ret, frame = cap.read()
#     if ret == True:

#         cv2.imshow('video', frame) #展示视频

#         #重新设置窗口为指定大小
#         cv2.resizeWindow('video', 640, 360)

#         #输出视频
#         vw.write(frame)
#         #等待键盘事件
#         key = cv2.waitKey(1)  #在此修改读帧频率
#         if(key & 0xFF == ord('q')):
#             break
#     else:
#         break

# #释放视频
# cap.release()
# #释放资源
# vw.release()
# #释放窗口
# cv2.destroyAllWindows()