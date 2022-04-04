import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

#直方图均衡化，增强对比度

# moon=data.moon()
# print(moon.shape)
# plt.hist(moon.ravel(),256,[0,256])
# plt.show()
# moon2=cv2.equalizeHist(moon)#直方图均衡化
# plt.hist(moon2.ravel(),256,[0,256])
# plt.show()
# cv2.imshow('moon',moon)
# cv2.imshow('moon2',moon2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# moon=data.moon()
# hist=cv2.calcHist([moon],[0],None,[256],[0,256])
# print(hist)
# print(hist.shape)
# plt.plot(hist)#线性图
# plt.bar(x=np.arange(0,256),height=hist.reshape(-1))#柱状图
# plt.show()
# cv2.imshow('moon',moon)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''先转换为灰度图'''
# img=cv2.imread('imgs/v.jpg',0)
# plt.hist(img.ravel(),256,[0,256])
# plt.show()
# img2=cv2.equalizeHist(img)#直方图均衡化
# plt.hist(img2.ravel(),256,[0,256])
# plt.show()
# cv2.imshow('img',img)
# cv2.imshow('img2',img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()