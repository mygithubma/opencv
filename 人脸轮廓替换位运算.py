import cv2
import numpy as np

if __name__ == "__main__":
    img=cv2.imread('imgs/v.jpg')
    print(img.shape)
    cv2.imshow('opencv',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()