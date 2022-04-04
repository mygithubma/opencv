import cv2
import numpy as np

if __name__ == "__main__":
    video=cv2.VideoCapture('imgs\性格--错觉.mp4')
    face_detector=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
   
    while True:
        retval,image=video.read()  #retval boolean表明是否获得了图片，true
        image=cv2.resize(image,(215,162))
        if retval == False:
            print('收到v')
            break
        gray=cv2.cvtColor(image,code=cv2.COLOR_BGR2GRAY)
        faces=face_detector.detectMultiScale(gray)  #耗时操作
        for x,y,w,h in faces:
            cv2.rectangle(image,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=2) 
        cv2.imshow('img',image)
        key=cv2.waitKey(1)  #1ms
        if key == ord('q'):
            print('退出')
            break
    cv2.destroyAllWindows()
    video.release()  #释放内存
