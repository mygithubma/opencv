import numpy as np
import cv2

if __name__ == "__main__":
    img=cv2.imread('imgs/v.jpg',flags=cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    #颜色翻转
    # img=(img-255)*255
    cv2.namedWindow('erode',cv2.WINDOW_NORMAL)
    cv2.namedWindow('dilate',cv2.WINDOW_NORMAL)
    kernel=np.ones(shape=(5,5),dtype=np.uint8)
    #腐蚀
    img2=cv2.erode(img,kernel,iterations=1)
    #膨胀
    img3=cv2.dilate(img2,kernel,iterations=1)
    cv2.imshow('img',img)
    cv2.imshow('erode',img2)
    cv2.imshow('dilate',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()