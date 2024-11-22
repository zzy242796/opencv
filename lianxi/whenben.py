#绘制文本
import cv2
import numpy as np
from PIL import ImageFont,ImageDraw,Image



# #英文  FONT_.......
# img = np.zeros((600,1000,3),np.uint8)

# cv2.putText(img,'西安市擦',(50,400),cv2.FONT_HERSHEY_COMPLEX,2,[0,0,255])


#中文

#纯白
img = np.full((600,800,3),fill_value=255,dtype=np.uint8)
#导入字体文件
font = ImageFont.truetype('./GB2312.TTF',30)
#创建一个pillow的图片
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
#利用draw去绘制中文
draw.text((50,150),'服务范围',font=font,fill=(0,0,0,0))

#重新变回ndarray

img = np.array(img_pil)

cv2.imshow('draw',img)
cv2.waitKey(0)
cv2.destroyAllWindows()