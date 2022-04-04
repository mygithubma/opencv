import cv2
import numpy as np
if __name__ == "__main__":
    video=cv2.VideoCapture('imgs\性格--错觉.mp4')

    writer=cv2.VideoWriter(filename='imgs\gray2.mp4',
                    fourcc=cv2.VideoWriter.fourcc(*'MP4V'),   #视频编码  *mp4v->m p 4 v
                                                             #c1='m' c2='p'  c3='4'
                    fps=24,   #帧率
                    frameSize=(432,324))
    # fps=video.get(propId=cv2.CAP_PROP_FPS)   #视频帧率
    # width=video.get(propId=cv2.CAP_PROP_FRAME_WIDTH)
    # height=video.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)
    # count=video.get(propId=cv2.CAP_PROP_FRAME_COUNT)
    # print('视频帧率:',fps)
    # print(width,height,count)

    face_detector=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    while True:
        cv2.namedWindow('img',cv2.WINDOW_NORMAL)
        revtal,image=video.read()
        if revtal == False:
            print('fhsg0')
            break
        gray=cv2.cvtColor(image,code=cv2.COLOR_BGR2GRAY)
        gray2=np.repeat(gray.reshape(432,324,1),3,axis=2)
        writer.write(gray2)

        faces=face_detector.detectMultiScale(gray)  #耗时操作
        for x,y,w,h in faces:
            # cv2.rectangle(image,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=2) 
            face=image[y:y+h,x:x+w]
            face[::10,::10]
            face=np.repeat(np.repeat(face,10,axis=0),10,axis=1)
            image[y:y+h,x:x+w]=face[:h,:w]
        # writer.write(image)
        cv2.imshow('img',image)
        key=cv2.waitKey(1)  #1ms
        if key == ord('q'):
            print(image.shape)
            print('退出')
            break
    cv2.destroyAllWindows()
    video.release()  #释放内存Q
    writer.release()