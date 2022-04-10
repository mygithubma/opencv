import numpy as np
import cv2

if __name__ == "__main__":
    car=cv2.imread('imgs/R-C.jpg')
    gray=cv2.cvtColor(car,code=cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('car',cv2.WINDOW_NORMAL)
    car_detector=cv2.CascadeClassifier('')
    plates=car_detector.detectMultiScale(gray)
    for x,y,w,h in plates:
        cv2.rectangle(car,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=2)
    cv2.imshow('car',car)
    cv2.waitKey(0)
    cv2.destroyAllWindows()