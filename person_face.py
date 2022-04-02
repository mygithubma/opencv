import numpy as np
import cv2

if __name__ == "__main__":
    img=cv2.imread('E:\\xuexibiji\\VSCODE\\opencv\\NBA.webp')
    gray=cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
    face_detector=cv2.CascadeClassifier('E:\\xuexibiji\\VSCODE\\opencv\\haarcascade_frontalface_alt.xml')
    faces=face_detector.detectMultiScale(gray,
                                    scaleFactor=1.1,#缩放，调大识别少
                                    minNeighbors=3,
                                    # minSize=(50,50)
                                    )#坐标x,y,w,h
    print(faces)
    for x,y,w,h in faces:
        # cv2.rectangle(img,
        #             pt1=(x,y),
        #             pt2=(x+w,y+h),
        #             color=[0,0,255],
        #             thickness=2)
        cv2.circle(img,
                    center=(x+w//2,y+h//2),
                    radius=w//2,
                    color=[0,255,0],
                    thickness=2)
    cv2.namedWindow('face',cv2.WINDOW_NORMAL)    
    cv2.imshow('face',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



