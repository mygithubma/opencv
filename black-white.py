import numpy as np
import cv2

if __name__ == "__main__":
    img=cv2.imread('E:\\xuexibiji\\VSCODE\\opencv\\001.jpg')
    img2=cv2.resize(img,(400,600))
    # gray=cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
    # hsv=cv2.cvtColor(img,code=cv2.COLOR_BGR2HLS)
    # cv2.imshow('img',hsv)
    # cv2.waitKey(00)
    # #0无限等待，1000=1s
    # cv2.destroyAllWindows()

    #define range of biue color in HSV
    lower_blue=np.array([0,50,50])
    upper_blue=np.array([180,255,255])

    img2=cv2.cvtColor(img,code = cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(img2,lower_blue,upper_blue)
    img3=cv2.bitwise_and(img,img2,mask=mask)

    for i in range(img3.shape[0]):          #更改背景色,高度
        for j in range(img3.shape[1]):      #宽度
            if (img3[i,j]==0).all():
                img3[i,j]=250

    cv2.imshow('img',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#cv2.bitwise_and()
''' a=np.random.randint(0,20,size=(3,3,3))
    b=np.random.randint(0,20,size=(3,3,3))
    print(a,'\n\n',b)
    c=cv2.bitwise_and(a,b,mask=np.array([[1,0,0],[0,0,1],[0,1,0]],dtype=np.uint8))
    print(c)
'''