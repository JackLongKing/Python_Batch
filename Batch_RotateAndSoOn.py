# coding=utf-8

import os
import cv2
import numpy as np

def batch_rotate_images_cross_files(path1,path2,angle):
    print "Write Labels Starts:\n"
    print path1
    for tempFile in os.listdir(path2):
        path3=os.path.join(path2,tempFile)
        print path3
        for tempImg in os.listdir(path3):
            tempImg=os.path.join(path3,tempImg)
            rotate_images(tempImg)
    print "Done!\n"

def rotate_images(filename):
    print "Rotate Start:\n"
    img=cv2.imread(filename)
    rows,cols=img.shape[:2]
    M=cv2.getRotationMatrix2D((cols/2,rows/2),10,1)
    dst=cv2.warpAffine(img,M,(cols/2,rows/2))
    cv2.imwrite(r"C:\Users\Administrator\Desktop\rotate15.tif",dst)
    print "Done! \n"

def affine_transform_images(filename):
    print "Affine Start:\n"
    img = cv2.imread(filename)
    rows, cols = img.shape[:2]
    pts1 = np.float32([[1, 1], [10, 1], [1, 10]])
    pts2 = np.float32([[4, 4], [10, 4], [4, 7]])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imwrite(r"C:\Users\Administrator\Desktop\affine.tif",dst)
    print "Done!\n"




if __name__=="__main__":
    # rotate_images(r"C:\Users\Administrator\Desktop\20_20161010_1055.tif")
    affine_transform_images(r"C:\Users\Administrator\Desktop\20_20161010_1055.tif")