##英文图片文本识别

# import cv2
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'F:\OCR\tesseract.exe'

# # 读取图像
# img = cv2.imread('Ewenben.png')

# # 将图像转换为灰度图
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 可选：应用一些图像预处理技术，比如二值化
# _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# # 使用pytesseract进行文字识别
# text = pytesseract.image_to_string(binary)

# # 打印识别结果
# print("识别结果：", text)

# ----------------------------------------------------------------------

# #摄像头英文文本识别

# import cv2
# import pytesseract

# # 配置pytesseract的Tesseract-OCR路径（如果需要）
# pytesseract.pytesseract.tesseract_cmd = r'F:\OCR\tesseract.exe'

# # 打开摄像头
# cap = cv2.VideoCapture(1)

# while True:
#     # 读取摄像头的帧
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # 将图像转换为灰度图
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # 可选：应用一些图像预处理技术，比如二值化
#     _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

#     # 使用pytesseract进行文字识别
#     text = pytesseract.image_to_string(binary)


#     # 检查识别的文本是否为 "rude"
#     if text.strip().lower() == 'rude':
#         print('qqqqqqqqq')  # 如果文本是 "rude"，则打印 "qqqqqqqqq"


#     # 在原始帧上显示识别的文本
#     cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     # 显示带有识别文本的帧
#     cv2.imshow('Real-time Text Recognition', frame)

#     # 按'q'退出循环
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # 释放摄像头
# cap.release()
# # 关闭所有OpenCV窗口
# cv2.destroyAllWindows()


# -------------------------------------------------------------------------------------------

# # 中文图片文本识别
# import cv2
# import pytesseract
# from PIL import Image

# # 指定Tesseract可执行文件的路径
# pytesseract.pytesseract.tesseract_cmd = r'F:\OCR\tesseract.exe'

# # 加载图片
# img = Image.open('F:/opencv/picture/Cwenben.png')

# # 使用中文简体语言包进行文字识别
# text = pytesseract.image_to_string(img, lang='chi_sim')
# print("识别的文本:", text)


#优化代码
import cv2
import pytesseract
from PIL import Image
# from pytesseract import Output

# 指定Tesseract可执行文件的路径
pytesseract.pytesseract.tesseract_cmd = r'F:\OCR\tesseract.exe'

# 配置Tesseract的额外参数
custom_config = r'--oem 3 --psm 6'

# 打开图片
def open_image(image_path):
    return cv2.imread(image_path)

# 图像预处理
def preprocess_image(image):
    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    # 可选：进行其他预处理步骤，如去噪、滤波等
    return binary

# 识别文本
def recognize_text(image, lang='chi_sim'):
    try:
        # 调用Tesseract进行文字识别
        result = pytesseract.image_to_string(image, lang=lang, config=custom_config)
        return result
    except Exception as e:
        print(f"识别过程中发生错误: {e}")
        return None

# 主函数
def main(image_path):
    # 读取图片
    img = open_image(image_path)
    if img is None:
        print("图片加载失败，请检查文件路径。")
        return

    # 预处理图片
    processed_img = preprocess_image(img)

    # 将OpenCV图像转换为PIL图像格式
    pil_img = Image.fromarray(processed_img)

    # 识别文本
    text = recognize_text(pil_img)
    if text:
        print("识别的文本:\n", text)

# 调用主函数
if __name__ == "__main__":
    image_path = 'F:/opencv/picture/Cwenben.png'  # 替换为你的图片路径
    main(image_path)






# import cv2
# import pytesseract

# # 指定Tesseract可执行文件的路径
# pytesseract.pytesseract.tesseract_cmd = r'F:\OCR\tesseract.exe'

# # 配置Tesseract的额外参数
# custom_config = r'--oem 3 --psm 6'

# # 图像预处理
# def preprocess_image(image):
#     # 转换为灰度图
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # 二值化
#     _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
#     return binary

# # 识别文本
# def recognize_text(image, lang='chi_sim'):
#     try:
#         # 调用Tesseract进行文字识别
#         result = pytesseract.image_to_string(image, lang=lang, config=custom_config)
#         return result.strip()  # 使用strip()去除可能的前后空白字符
#     except Exception as e:
#         print(f"识别过程中发生错误: {e}")
#         return None

# # 主函数
# def main():
#     # 创建视频捕获对象
#     cap = cv2.VideoCapture(1)
    
#     if not cap.isOpened():
#         print("无法打开摄像头")
#         return

#     while True:
#         # 从摄像头读取一帧
#         ret, frame = cap.read()
#         if not ret:
#             print("无法读取帧")
#             break

#         # 预处理图片
#         processed_img = preprocess_image(frame)

#         # 识别文本
#         text = recognize_text(processed_img)
#         if text:
#             print("识别的文本:\n", text)

#         # 显示图像
#         cv2.imshow('frame', frame)

#         # 按'q'退出
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # 释放资源
#     cap.release()
#     cv2.destroyAllWindows()

# # 调用主函数
# if __name__ == "__main__":
#     main()