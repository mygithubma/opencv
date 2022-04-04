import cv2

if __name__ == "__main__":
    img=cv2.imread('NBA.webp')
    cv2.namedWindow('face',cv2.WINDOW_NORMAL)
    gray=cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
    face_detector=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    faces=face_detector.detectMultiScale(gray)
    star=cv2.imread('./001.jpg')
    for x,y,w,h in faces:
        '''
        cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),
        color=[0,0,255],thickness=2)
        img[y:y+h//4,x+(3*w)//8:x+(3*w)//8+w//4]=cv2.resize(star,(w//4,h//4))
        '''

        star_s=cv2.resize(star,(w//4,h//4))
        w1=w//4
        h1=h//4
        for i in range(h1):
            for j in range(w1):  #遍历图片数据
                if not (star_s[i,j]>180).all():
                    img[i+y,j+x+3*w//8]=star_s[i,j]

    cv2.imshow('face',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()