#卷积核滤波  模糊图片
#图片  位深（-1） 卷积核  锚点（中心点） 0  边界类型
#filter2D(src,ddepth,kernel,anchor,delta,borderType)

# import cv2
# import numpy as np

# img = cv2.imread('333.jpeg')

# kernel = np.ones((5,5),np.float32) / 25

# dst = cv2.filter2D(img,-1,kernel)

# cv2.imshow('dst',dst)
# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




#方盒滤波 boxFilter()

#均值滤波 blur()
# import cv2
# import numpy as np
# from PIL import ImageFont,ImageDraw,Image

# img = cv2.imread('ccc.png')

# dst = cv2.blur(img,(5,5))

# font = ImageFont.truetype('./GB2312.TTF',30)

# img_pil = Image.fromarray(img)
# draw1 = ImageDraw.Draw(img_pil)
# draw1.text((40,40),'原图',font=font,fill=(0,0,0,0))

# dst_pil = Image.fromarray(dst)
# draw2 = ImageDraw.Draw(dst_pil)
# draw2.text((40,40),'均值滤波',font=font,fill=(0,0,0,0))
# img = np.array(img_pil)
# dst = np.array(dst_pil)

# cv2.imshow('dst',dst)
# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




#高斯滤波 GaussianBlur()

# import cv2
# import numpy as np

# img = cv2.imread('333.jpeg')

# dst = cv2.GaussianBlur(img,(5,5),sigmaX=1,sigmaY=1)

# cv2.imshow('dst',dst)
# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




#中值滤波  medianBlur()

# import cv2
# import numpy as np

# img = cv2.imread('333.jpeg')

# dst = cv2.medianBlur(img,5)

# cv2.imshow('dst',dst)
# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




#双边滤波 bilateralFilter()
# import cv2
# import numpy as np

# img = cv2.imread('333.jpeg')

# dst = cv2.bilateralFilter(img,5,20,50)

# cv2.imshow('dst',dst)
# cv2.imshow('img',img)
# # cv2.imwrite("./zzzz.png", dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# from PIL import ImageFont,ImageDraw,Image

# img = cv2.imread('ccc.png')

# dst = cv2.medianBlur(img,5)

# font = ImageFont.truetype('./GB2312.TTF',30)

# img_pil = Image.fromarray(img)
# draw1 = ImageDraw.Draw(img_pil)
# draw1.text((40,40),'原图',font=font,fill=(0,0,0,0))

# dst_pil = Image.fromarray(dst)
# draw2 = ImageDraw.Draw(dst_pil)
# draw2.text((40,40),'中值滤波',font=font,fill=(0,0,0,0))
# img = np.array(img_pil)
# dst = np.array(dst_pil)

# cv2.imshow('dst',dst)
# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()






#高通滤波   索贝尔算子Sobel()    Scharr()  Laplacian()

# import cv2
# import numpy as np
# 
# img = cv2.imread('ww.png')

# dst = cv2.bilateralFilter(img,5,20,50)

# #y方向边缘
# dst1 = cv2.Sobel(img,cv2.CV_64F,1,0, ksize=5)
# #x方向边缘
# dst2 = cv2.Sobel(img,cv2.CV_64F,0,1, ksize=5)

# dst1 = cv2.Scharr(img,cv2.CV_64F,1,0)
# dst2 = cv2.Sobel(img,cv2.CV_64F,0,1)

# c = cv2.add(dst1,dst2)

# cv2.imshow('img',img)
# cv2.imshow('dst1',dst1)
# cv2.imshow('dst2',dst2)
# cv2.imshow('c',c)
# cv2.imwrite("./zzzz.png", dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



#拉普拉斯   求边缘
# import cv2
# import numpy as np

# img = cv2.imread('ww.png')

# ldst = cv2.Laplacian(img,cv2.CV_64F, ksize=5)


# cv2.imshow('img',img)
# cv2.imshow('ldst',ldst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#边缘检测  Canny
import cv2
import numpy as np

img = cv2.imread('F:/opencv/picture/777.jpg')

ldst = cv2.Canny(img,100,200)


cv2.imshow('img',img)
cv2.imshow('ldst',ldst)

cv2.waitKey(0)
cv2.destroyAllWindows()