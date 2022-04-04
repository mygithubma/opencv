import cv2
import numpy as np

if __name__ == "__main__":
    img=cv2.imread('imgs\v.jpg')
    hsv=cv2.cvtColor(img,code=cv2.COLOR_BGR2HSV)
    # 轮廓查找，按照颜色的值
    lower_red=(156,43,46)  
    upper_red=(180,255,255)
    mask=cv2.inRange(hsv,lower_red,upper_red)
    #手工绘制轮廓
    # h,w,c=img.shape
    # mask=np.zeros((h,w),dtype=np.uint8)
    # x_data=np.array([100,800,400,500,200,940])
    # y_data=np.array([600,500,500,300,400,900])

    # pts=np.vstack((x_data,y_data)).astype(np.uint8).T#转置

    # pts=np.c_[x_data,y_data]  #横纵坐标合并

    # cv2.fillPoly(mask,[pts],(255),8,0)
    # cv2.imshow('mask',mask)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('opencv',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

