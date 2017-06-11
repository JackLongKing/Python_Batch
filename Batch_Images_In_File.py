# coding:UTF-8
import cv2
import os
import os.path
import sys



def judge_Resize(path):
    print "Process start:\n"
    for tempImg in os.listdir(path):
        tempImg = path+"\\" + tempImg
        img = cv2.imread(tempImg)
        # 判断图片大小
        # sp = img.shape
        # if sp[0] != 28 and sp[1] != 28:
        #     print tempImg + "'s size is not 28*28.\n"
        img1=cv2.resize(img, (32, 32),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(tempImg, img1)
    print "Process done.\n"

def judge_Resize_Cross_File(path):
    print "Process Start:\n"
    for tempFile in os.listdir(path):
        path1=os.path.join(path,tempFile)
        print path1
        for tempImg in os.listdir(path1):
            tempImg=os.path.join(path1,tempImg)
            img=cv2.imread(tempImg)
            img1=cv2.resize(img,(32,32),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(tempImg, img1)
    print "Process done.\n"

if __name__ == "__main__":
    # judge_Resize(r"E:\VS2013File\caffe\caffe_master\examples\cifar10\TestImages")
    judge_Resize_Cross_File(r"E:\Chars74K\EnglishImg\GoodImg")
