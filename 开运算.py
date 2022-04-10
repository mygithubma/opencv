import numpy as np
import cv2

if __name__ == "__main__":
    #开运算
    # img=cv2.imread('imgs/v.jpg',flags=cv2.IMREAD_GRAYSCALE)
    # cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('result',cv2.WINDOW_NORMAL)
    # result=cv2.morphologyEx(img,op=cv2.MORPH_OPEN,
    #                             kernel=np.ones(shape=(10,10),
    #                             dtype=np.uint8),
    #                             iterations=1)
    # cv2.imshow('img',img)
    # cv2.imshow('result',result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #闭运算
    # img=cv2.imread('imgs/v.jpg',flags=cv2.IMREAD_GRAYSCALE)
    # cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('result',cv2.WINDOW_NORMAL)
    # result=cv2.morphologyEx(img,op=cv2.MORPH_CLOSE,
    #                             kernel=np.ones(shape=(10,10),
    #                             dtype=np.uint8),
    #                             iterations=1)
    # cv2.imshow('img',img)
    # cv2.imshow('result',result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #形态学梯度
    # img=cv2.imread('imgs/v.jpg',flags=cv2.IMREAD_GRAYSCALE)
    # cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('result',cv2.WINDOW_NORMAL)
    # result=cv2.morphologyEx(img,op=cv2.MORPH_GRADIENT,
    #                             kernel=np.ones(shape=(10,10),
    #                             dtype=np.uint8),
    #                             iterations=1)
    # cv2.imshow('img',img)
    # cv2.imshow('result',result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #礼帽
    # img=cv2.imread('imgs/v.jpg',flags=cv2.IMREAD_GRAYSCALE)
    # cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('result',cv2.WINDOW_NORMAL)
    # result=cv2.morphologyEx(img,op=cv2.MORPH_TOPHAT,
    #                             kernel=np.ones(shape=(10,10),
    #                             dtype=np.uint8),
    #                             iterations=1)
    # cv2.imshow('img',img)
    # cv2.imshow('result',result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #黑帽
    img=cv2.imread('imgs/v.jpg',flags=cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    cv2.namedWindow('result',cv2.WINDOW_NORMAL)
    result=cv2.morphologyEx(img,op=cv2.MORPH_BLACKHAT,
                                kernel=np.ones(shape=(10,10),
                                dtype=np.uint8),
                                iterations=1)
    cv2.imshow('img',img)
    cv2.imshow('result',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()