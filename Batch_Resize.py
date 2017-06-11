# coding=utf-8

import os
import cv2
# for double file contents
def batch_resize1(path,img_height=32,img_width=32):
    print "Resize Start:\n"
    for tempFile in os.listdir(path):
        path1=os.path.join(path,tempFile)
        print path1
        for tempImg in os.listdir(path1):
            tempImg=os.path.join(path1,tempImg)
            img=cv2.imread(tempImg)
            img1=cv2.resize(img,(img_height,img_width),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(tempImg,img1)
            print tempImg+" resize successfully\n"
    print "Resize Done"

# for single content
def batch_resize2(path,img_height=32,img_width=32):
    print "Resize Start:\n"
    for tempFile in os.listdir(path):
        tempImg = os.path.join(path, tempFile)
        img = cv2.imread(tempImg)
        img1 = cv2.resize(img, (img_height, img_width), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(tempImg, img1)
        print tempImg + " resize successfully\n"
    print "Resize Done"



if __name__=="__main__":
    # batch_resize2(r"E:\Challenge2_Training_Task12_Images",640,640)
    batch_resize2(r"E:\TestImage\BatchTest\CKEFPositive\img_1_true",227,227)