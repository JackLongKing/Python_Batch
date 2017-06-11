# coding=UTF-8

import os
import cv2
import numpy as np

def get_image_type(imagename):
    str=imagename[-4:]
    return str

def get_image_name_prefix(imagename):
    tempStr=imagename.split('.t')[0]
    str=tempStr.split('20161010_')[0]+'20161010_'
    return str

def get_image_name_number(imagename):
    tempStr=imagename.split('.t')[0]
    number=tempStr.split('20161010_')[1]
    number=int(number)
    return number

def set_image_name(prefix,number,image_type=".tif"):
    name=prefix+str(number)+image_type
    return name

def delete_image(imagename):
    os.remove(imagename)

def get_file_total_number(path):
    n=sum([len(x) for _, _, x in os.walk(os.path.dirname(path))])
    print n
    return n

def judge_image_is_zero(image):
    for x in range(0, image.shape[0]):
        for y in range(0, image.shape[1]):
            if image[x, y][0] != 0 or image[x, y][1] != 0 or image[x][y][2] != 0:
                print "The image is not None.\n"
                return False
    print "It is None.\n"
    return True

def judge_file_name(filename):
    str=filename[-3:-1]+filename[-1]
    if "_1" in str:
        return 1
    elif "_2" in str:
        return 2
    elif "_3" in str:
        return 3
    elif "_4" in str:
        return 4
    elif "_5" in str:
        return 5
    elif "_6" in str:
        return 6
    elif "_7" in str:
        return 7
    elif "_8" in str:
        return 8
    elif "_9" in str:
        return 9
    elif "_10" in str:
        return 10
    elif "_11" in str:
        return 11
    else:
        return 0

def batch_resize(path,img_size=32):
    print "Resize Start:\n"
    for tempFile in os.listdir(path):
        path1=os.path.join(path,tempFile)
        print path1
        for tempImg in os.listdir(path1):
            tempImg=os.path.join(path1,tempImg)
            img=cv2.imread(tempImg)
            img1=cv2.resize(img,(img_size,img_size),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(tempImg,img1)
            print tempImg+" resize successfully\n"
    print "Resize Done"

def batch_delete(path):
    print "Judge and delete start:\n"
    for tempFile in os.listdir(path):
        path1=os.path.join(path,tempFile)
        print path1
        x=judge_file_name(tempFile)
        m = get_file_total_number(path1 + "\\")
        for tempImg in os.listdir(path1):
            tempImg=os.path.join(path1,tempImg)
            print tempImg
            n=get_image_name_number(tempImg)
            prefix=get_image_name_prefix(tempImg)
            img1=cv2.imread(tempImg)
            if img1 is not None:
                for i in range(n + 1, m, 1):
                    temp_Compare_Img = set_image_name(prefix, i)
                    img2=cv2.imread(temp_Compare_Img)
                    if img2 is not None:
                        img1_2=cv2.absdiff(img1,img2)
                        if judge_image_is_zero(img1_2):
                            delete_image(temp_Compare_Img)



if __name__=="__main__":
    # batch_resize(r"E:\Batch_Test",96)
    # batch_delete(r"E:\OUTPUT_DATA_FOR_CLASSIFICATION")
    batch_delete(r'E:\MySynData')
    # time: 161105_2107
    # get_file_total_number(r"E:\Batch_Test\img_20\\")
    # set_image_name("img_20_20161010_",20,'.tif')
    # delete_image(r"E:\Batch_Test\img_20_20161010_0.tif")
    # img_1=cv2.imread(r"E:\Batch_Test\img_20_20161010_2320.tif")
    # img_2=cv2.imread(r"E:\Batch_Test\img_20_20161010_2321.tif")
    # img_3=cv2.subtract(img_1,img_2)
    # cv2.imwrite(r"E:\Batch_Test\new.jpg",img_3)
    # result=judge_image_is_zero(img_3)
    # print result


