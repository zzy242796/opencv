#打开图片
# import cv2
# img = cv2.imread('F:\\picture\\wwww.jpg')
# cv2.imshow('img', img)
# cv2.waitKey(0)


#设置窗口
# import cv2
# cv2.namedWindow('new',cv2.WINDOW_NORMAL)  #创建窗口
# cv2.resizeWindow('new',640, 480)  #窗口大小
# cv2.imshow('new',0)
# key = cv2.waitKey(0)
# if(key == 'q'):
#     exit()   #退出
# cv2.destroyAllWindows()   #释放窗口资源


# 加载图片
import cv2
cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
img = cv2.imread('F:\\picture\\wwww.jpg')
while True:
    cv2.imshow('img',img)
    key = cv2.waitKey(0)
    # print(key)
    # print('q')
    # print(ord('q'))
    if(key & 0xFF == ord('q')):
        print(11111)
        break
    elif(key & 0xFF == ord('s')):
        cv2.imwrite("F:\\picture\\zzzz.png", img)   # 将img图片保存为png格式
    else:
        print(key)
cv2.destroyAllWindows()   #释放窗口资源
