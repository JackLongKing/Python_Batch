# coding:UTF-8
import os
import cv2

img=cv2.imread(r"E:\PyCharmFile\Python_Batch\TrainImages\0\0_00001.jpg")
cv2.imshow("JPG",img)
print img.size
print img.shape
cv2.waitKey(0)