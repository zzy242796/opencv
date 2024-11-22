# import cv2

# # 读取图像
# rgb_image = cv2.imread('zzz.jpg')
# new1 = cv2.resize(rgb_image,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

# # 检查图像是否正确加载
# if rgb_image is None:
#     print("错误：未找到图像。")
# else:
#     # 将图像从RGB转换到YUV
#     new2 = cv2.resize(rgb_image,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)
#     yuv_image = cv2.cvtColor(new2, cv2.COLOR_RGB2YUV)

#     # 显示原始RGB图像
#     cv2.imshow('RGB Image', new1)

#     # 显示YUV图像
#     cv2.imshow('YUV Image', yuv_image)

#     # 等待用户按键，再退出
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()




# import cv2
# import numpy as np

# # 读取RGB图像
# rgb_image = cv2.imread('zzz.jpg')
# new1 = cv2.resize(rgb_image,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

# # 检查图像是否正确加载
# if rgb_image is None:
#     print("错误：未找到图像。")
# else:
#     # 将图像数据转换为浮点型以进行计算
#     rgb_image_float = rgb_image.astype(np.float32)

#     # 应用YIQ转换公式
#     Y = 0.299 * rgb_image_float[:, :, 0] + 0.587 * rgb_image_float[:, :, 1] + 0.114 * rgb_image_float[:, :, 2]
#     I = 0.596 * rgb_image_float[:, :, 0] - 0.274 * rgb_image_float[:, :, 1] - 0.322 * rgb_image_float[:, :, 2]
#     Q = 0.211 * rgb_image_float[:, :, 0] - 0.523 * rgb_image_float[:, :, 1] + 0.312 * rgb_image_float[:, :, 2]

#     # 将YIQ分量合并为一个图像
#     YIQ_image = np.dstack((Y, I, Q))

#     # 显示原始RGB图像
#     cv2.imshow('RGB Image', new1)

#     # 显示YIQ图像
#     YIQ_image_scaled = cv2.convertScaleAbs(YIQ_image)
#     new2 = cv2.resize(YIQ_image_scaled,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

#     cv2.imshow('YIQ Image', new2)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()




# import cv2

# # 读取RGB图像
# rgb_image = cv2.imread('zzz.jpg')
# new1 = cv2.resize(rgb_image,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

# # 检查图像是否正确加载
# if rgb_image is None:
#     print("错误：未找到图像。")
# else:
#     # 将图像从RGB转换到HSV
#     hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
#     new2 = cv2.resize(hsv_image,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

#     # 显示原始RGB图像
#     cv2.imshow('RGB Image', new1)

#     # 显示转换后的HSV图像
#     cv2.imshow('HSV Image', new2)

#     # 等待用户按键，再退出
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()




import cv2
import numpy as np

# 读取RGB图像
rgb_image = cv2.imread('zzz.jpg')
new1 = cv2.resize(rgb_image,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

# 检查图像是否正确加载
if rgb_image is None:
    print("错误：未找到图像。")
else:
    # 将图像从BGR转换到HSV，因为cv2.imread默认读取的是BGR格式
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)

    # 从HSV图像中分离出H和S通道
    h, s, v = cv2.split(hsv_image)

    # 计算Intensity分量
    rgb_image_float = rgb_image.astype(np.float32) / 255.0  # 归一化到[0,1]
    i = np.mean(rgb_image_float, axis=2)

    # 将H, S, I合并为一个图像
    hsi_image = np.dstack((h, s, i * 255)).astype(np.uint8)  # 将I转换回0-255范围
    new2 = cv2.resize(hsi_image,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

    # 显示原始RGB图像
    cv2.imshow('RGB Image', new1)

    # 显示HSI图像
    cv2.imshow('HSI Image', new2)

    # 等待用户按键，再退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()