import cv2
import numpy as np

if __name__ == "__main__":
    #马赛克
    # image=cv2.imread('imgs\\NBA.webp')
    # cv2.namedWindow('my_opencv',cv2.WINDOW_NORMAL)  #可调节屏幕大小，'img'--窗口名
    # img2=image[::10,::10]    #每十个数里面取一个
    # img2=np.repeat(img2,10,axis=0)  #axis=None，时候就会flatten当前矩阵，实际上就是变成了一个行向量
    #                                 #axis=0,沿着y轴复制，实际上增加了行数
    #                                 #axis=1,沿着x轴复制，实际上增加列数
    # img2=np.repeat(img2,10,axis=1)
    # cv2.imshow('my_opencv',img2)
    # cv2.waitKey(0)   #key0等待按下任意键退出
    # cv2.destroyAllWindows()


    #提升--模糊部分区域
    image=cv2.imread('imgs\\NBA.webp')
    cv2.namedWindow('my_opencv',cv2.WINDOW_NORMAL) 
    img2=image[100:1000,200:1200]
    img2=img2[::10,::10]
    img2=np.repeat(img2,10,axis=0)
    img2=np.repeat(img2,10,axis=1)
    image[100:1000,200:1200]=img2[:400,:633]
    cv2.imshow('my_opencv',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()