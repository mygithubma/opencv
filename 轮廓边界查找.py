import cv2
import numpy as np

if __name__ == "__main__":
    img=cv2.imread('v.jpg')
    cv2.namedWindow('opencv1',cv2.WINDOW_NORMAL)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # gray2=cv2.GaussianBlur(gray,(11,11),1)
    # canny=cv2.Canny(gray2,75,200)
    res=img,contours=cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow('opencv1',gray)
    
    cv2.imshow('opencv1',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()