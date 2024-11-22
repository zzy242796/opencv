# 角点检测  harris

# import cv2
# import numpy as np

# blockSize = 2   #检测窗口大小
# ksize = 3       #卷积核
# k = 0.04        #权重系数

# img = cv2.imread('view.jpg')

# #灰度化
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# #角点检测
# dst = cv2.cornerHarris(gray,blockSize,ksize,k)

# img[dst>0.01*dst.max()] = [0,0,255]

# cv2.imshow('harris',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# --------------------------------------------------------------------



#shi-Tomasi角点检测
# import cv2
# import numpy as np

# maxCorners = 1000
# ql = 0.01
# minDistance = 40

# img = cv2.imread('view.jpg')

# #灰度化
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# #角点检测
# corners = cv2.goodFeaturesToTrack(gray,maxCorners,ql,minDistance)
# corners = np.int0(corners)

# #shi-Tomasi绘制角点
# for i in corners:
#     x,y = i.ravel()
#     cv2.circle(img,(x,y),3,(255,0,0),-1)

# cv2.imshow('harris',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# ------------------------------------------------------------------------------



#SIFT

# import cv2
# import numpy as np

# img = cv2.imread('view.jpg')

# #灰度化
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #创建对象
# sift = cv2.SIFT_create()
# #进行检测
# kp = sift.detect(gray,None)
# kp,des = sift.detectAndCompute(gray,None)
# #绘制
# cv2.drawKeypoints(gray,kp,img)

# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# or

# import cv2 as cv

# # 读取图像
# img_path = 'view.jpg'  # 替换为你的图像路径
# img = cv.imread(img_path)

# # 转换为灰度图像
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # 初始化 SIFT 检测器
# sift = cv.SIFT_create()

# # 使用 SIFT 检测关键点和描述子
# keypoints, descriptors = sift.detectAndCompute(gray, None)

# # 绘制关键点
# img_with_keypoints = cv.drawKeypoints(img, keypoints, None, color=(255, 0, 255), flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# # 显示带有关键点的图像
# cv.imshow('SIFT Keypoints', img_with_keypoints)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # 如果需要，可以保存关键点和描述子
# # cv.imwrite('sift_keypoints.jpg', img_with_keypoints)



# ------------------------------------------------------------------------------------------------------------------------



#SURF

# import cv2
# import numpy as np

# img = cv2.imread('view.jpg')

# #灰度化
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #创建对象
# surf = cv2.xfeatures2d.SURF_create()
# #进行检测

# kp,des = surf.detectAndCompute(gray,None)
# #绘制
# cv2.drawKeypoints(gray,kp,img)

# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# -----------------------------------------------------------------------------------------------------



#ORB


# import cv2
# import numpy as np

# img = cv2.imread('view.jpg')

# #灰度化
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #创建对象
# orb = cv2.ORB_create()
# #进行检测

# kp,des = orb.detectAndCompute(gray,None)
# #绘制
# cv2.drawKeypoints(gray,kp,img)

# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -----------------------------------------------------------------------------------



#暴力特征匹配

# import cv2
# import numpy as np

# img1 = cv2.imread('eee.jpg')
# img1 = cv2.resize(img1,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# img2 = cv2.imread('eee.jpg')
# img2 = cv2.resize(img2,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

# #灰度化
# gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# #创建对象
# sift = cv2.SIFT_create()
# #进行检测
# kp1,des1 = sift.detectAndCompute(gray1,None)
# kp2,des2 = sift.detectAndCompute(gray2,None)

#创建匹配器
# bf = cv2.BFMatcher(cv2.NORM_L1)
# match = bf.match(des1,des2)
# #绘制
# img3 = cv2.drawMatches(img1,kp1,img2,kp2,match,None)

# cv2.imshow('img3',img3)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# -----------------------------------------------------------------------------------



# #Flann特征匹配

# import cv2
# import numpy as np

# img1 = cv2.imread('d.jpg')
# img1 = cv2.resize(img1,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# img2 = cv2.imread('c.jpg')
# img2 = cv2.resize(img2,None,fx=0.9,fy=0.9,interpolation=cv2.INTER_AREA)

# #灰度化
# gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# #创建对象
# sift = cv2.SIFT_create()
# #进行检测
# kp1,des1 = sift.detectAndCompute(gray1,None)
# kp2,des2 = sift.detectAndCompute(gray2,None)

# #创建匹配器
# index_params = dict(algorithm = 1,trees = 5)
# search_params = dict(checks = 50)
# flann = cv2.FlannBasedMatcher(index_params,search_params)

# #对描述子进行匹配计算
# matchs = flann.knnMatch(des1,des2, k=2)

# good = []
# for i, (m,n) in enumerate(matchs):
#     if m.distance < 0.7 * n.distance:
#         good.append(m)

# #绘制
# img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)

# cv2.imshow('img3',img3)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# -----------------------------------------------------------------------------------------------


#图像查找画框
import cv2
import numpy as np

img1 = cv2.imread('d.jpg')
img1 = cv2.resize(img1,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
img2 = cv2.imread('c.jpg')
img2 = cv2.resize(img2,None,fx=0.9,fy=0.9,interpolation=cv2.INTER_AREA)

#灰度化
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#创建对象
sift = cv2.SIFT_create()
#进行检测
kp1,des1 = sift.detectAndCompute(gray1,None)
kp2,des2 = sift.detectAndCompute(gray2,None)

#创建匹配器
index_params = dict(algorithm = 1,trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params,search_params)

#对描述子进行匹配计算
matchs = flann.knnMatch(des1,des2, k=2)

good = []
for i, (m,n) in enumerate(matchs):
    if m.distance < 0.6 * n.distance:
        good.append(m)



if len(good) >= 4:
    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    H, _ = cv2.findHomography(srcPts,dstPts,cv2.RANSAC,5.0)

    h,w = img1.shape[:2]
    pts = np.float32([[0,0],[0, h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,H)

    cv2.polylines(img2,[np.int32(dst)],True,(0,0,255))
else:
    print('the number of good is less than 4.')
    exit()

#绘制
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)

cv2.imshow('img3',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()