# #识别二维码图片

# import cv2
# import pyzbar.pyzbar as pyzbar
# from PIL import Image

# # 你的图片文件路径
# image_path = 'ewm.png'

# # 使用PIL库打开图片
# image = Image.open(image_path)

# # 使用pyzbar的decode函数识别图片中的二维码或条形码
# codes = pyzbar.decode(image)

# # 遍历识别到的条码对象
# for code in codes:
#     # 获取条码的数据
#     data = code.data.decode('utf-8')
#     print("Detected code:", data)
#     # 还可以获取其他属性，如码的类型、位置等
#     # print("Type:", code.type)
#     # print("Rect:", code.rect)

# # 变量信息
# variable_info = data
# x, y = 25,25  # 文本显示的位置
# font = cv2.FONT_HERSHEY_SIMPLEX  # 字体
# font_scale = 1  # 字体大小
# font_color = (255, 0, 0)  # 文本颜色，白色
# thickness = 1  # 文本线条粗细

# # 读取图片
# image = cv2.imread('ewm.png')

# # 在图片上显示变量信息
# cv2.putText(image, variable_info, (x, y), font, 
#              font_scale, font_color, thickness, cv2.LINE_AA)

# # 显示图片
# cv2.imshow('Image with Variable Info', image)

# # 等待键盘事件，按任意键退出
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -----------------------------------------------------------------------


#摄像头二维码识别
import cv2
from pyzbar.pyzbar import decode

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头的每一帧
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 解码二维码
    decoded_objects = decode(frame)
    
    # 遍历解码对象
    for obj in decoded_objects:
        # 绘制矩形框
        cv2.rectangle(frame, (obj.rect.left, obj.rect.top), (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height), (0, 255, 0), 2)
        
        # 显示二维码数据
        text = obj.data.decode("utf-8")
        cv2.putText(frame, text, (obj.rect.left, obj.rect.top), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # 显示结果
    cv2.imshow("QR Code Scanner", frame)
    
    # 按'q'退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭所有OpenCV窗口
cv2.destroyAllWindows()