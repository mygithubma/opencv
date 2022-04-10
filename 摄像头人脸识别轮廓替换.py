import cv2
import numpy as np

if __name__ == "__main__":
    cap=cv2.VideoCapture(0)  #表示打开本机的摄像头
    face_detector=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    img=cv2.imread('imgs\\v.jpg')
    while True:
        flag,frame=cap.read()  #flag是否读取了图片，frane  图片
        if not flag:
            break
        gray=cv2.cvtColor(frame,code=cv2.COLOR_BGR2GRAY)
        faces=face_detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)
        
        for x,y,w,h in faces:
            img1=cv2.resize(img,dsize=(w,h))
            
            img1_gray=cv2.cvtColor(img1,code=cv2.COLOR_BGR2GRAY)
            threshold,otsu=cv2.threshold(img1_gray,50,155,cv2.THRESH_OTSU)
            image,contours,hierarchy=cv2.findContours(otsu,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            areas=[]
            for c in contours:
                areas.append(cv2.contourArea(c))
            areas=np.asarray(areas)
            index=areas.argsort()
            mask=np.zeros(shape = [h,w],dtype=np.uint8)
            cv2.drawContours(mask,contours,index[-2],color=[0,0,255],thickness=-1)
            for i in range(h):
                for j in range(w):
                    if mask[i,j] == 255:
                        frame[i+y,j+x]=img1[i,j]


        cv2.imshow('face',frame)
        key=cv2.waitKey(1000//24)
        if key ==ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()
        
        