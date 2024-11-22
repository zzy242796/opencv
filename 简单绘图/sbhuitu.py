import cv2
import numpy as np

#这是一个全局标志，判断要画什么类型的图
curshape = 3
startpos = (0,0)

#创建背景图
img = np.zeros((540,960,3),np.uint8)

#要监听鼠标的行为，所以必须通过鼠标回调函数实现
def mouse_callback(event,x,y,flags,userdata):
    #引入全局变量
    global curshape,startpos
    #引入非本层的局部变量用什么关键字nonlocal
    if event == cv2.EVENT_LBUTTONDOWN:
        #记录起始位置
        startpos = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        #判断要画什么类型的图
        if curshape == 0:    #画直线
            cv2.line(img,startpos,(x,y),(0,0,255),3)
        elif curshape == 1:  #画矩形
            cv2.rectangle(img,startpos,(x,y),(0,0,255),3)
        elif curshape == 2:  #画圆
            #注意计算半径
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a**2 + b**2) ** 0.5)
            #h画圆的时候半径必须是整数
            cv2.circle(img,startpos,r,(0,0,255),3)
        else:
            print('暂不支持绘制其他图形')

#创建窗口
cv2.namedWindow('drawshape',cv2.WINDOW_NORMAL)
#设置鼠标回调函数
cv2.setMouseCallback('drawshape',mouse_callback)
print('按键说明：\n'
      'l:画直线\nr:画矩形\nc:画圆')

while True:
    cv2.imshow('drawshape',img)
    #检测按键
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('l'):
        curshape = 0
    elif key == ord('r'):
        curshape = 1
    elif key == ord('c'):
        curshape = 2

cv2.destroyAllWindows()