# coding=utf-8

import os
import cv2

def batch_alter(path,myformat):
    print "Start:\n"
    for tempImg in os.listdir(path):
        tempImg=os.path.join(path,tempImg)
        # print tempImg
        temp=tempImg[:-3]+myformat
        # print temp
        img=cv2.imread(tempImg)
        cv2.imwrite(temp,img)
    print "Done!\n"
def batch_remove(path,myformat):
    print "Start:\n"
    for tempImg in os.listdir(path):
        tempImg = os.path.join(path, tempImg)
        if myformat in tempImg:
            os.remove(tempImg)
    print "Done!\n"
if __name__=="__main__":
    # batch_alter(r"E:\MySynDataORI",'jpg')
    batch_remove(r"E:\MySynDataORI",'PNG')