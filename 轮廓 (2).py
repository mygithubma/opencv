import cv2
import numpy as np

if __name__ == "__main__":
    img=cv2.imread('imgs/v.jpg')
    cv2.namedWindow('opencv',cv2.WINDOW_NORMAL)
    gray=cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)

    ret,binary=cv2.threshold(gray,100,255,cv2.THRESH_BINARY) #阈值处理二值化
                                                              #THRESH_BINARY
    img,contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)     #寻找轮廓  
    mask=cv2.drawContours(gray,contours,-1,(0,255,255),thickness=2) #第一个参数是指明在哪幅图像上绘制轮廓；
                                                                    #第二个参数是轮廓本身，在Python中是一个list。
                                                                    #第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓。
    cv2.imshow('opencv',mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

