#coding=UTF-8

import os

def batch_write_labels(path1,path2,filename,label):
    print "Write Labels Start:\n"
    f=open(path1+"\\"+filename+".txt",'a')
    for tempImg in os.listdir(path2):
        tempImg = os.path.join(path2, tempImg)
        f.write(tempImg+" "+label+"\n")
    f.close()
    print "Write Labels End:\n"

def batch_write_labels_cross_files(path1,path2,filename,label):
    print "Write Labels Starts:\n"
    print path1
    f=open(path1+"\\"+filename+".txt",'a')
    for tempFile in os.listdir(path2):
        path3=os.path.join(path2,tempFile)
        print path3
        for tempImg in os.listdir(path3):
            tempImg=os.path.join(path3,tempImg)
            f.write(tempImg+" "+label+"\n")

if __name__=="__main__":
    # label文件所在文件夹,label文件名称,图像文件所在文件夹
    # batch_write_labels(r"C:\Users\Administrator\Desktop",r"F:\ProgramData\160901_161010\mnist_learning\official_data2jpg\TempTest\9","170220_TEST_9",'9')
    # batch_write_labels(r"C:\Users\Administrator\Desktop",r"E:\DogCat\Test\PDog","DOGCAT_TEST_POSITIVE",'1')
    # path1:txt文件所在目录，path2:图片所在目录(目录下包含一层文件夹，之后是图片)，filename:txt文件名，label:样本标签，如0,1
    # batch_write_labels_cross_files(r"C:\Users\Administrator\Desktop",r"E:\161220_ICDAR_TEST\NegativeSamples","TEST170217_NEGATIVE","0")
    batch_write_labels_cross_files(r"C:\Users\Administrator\Desktop", r"E:\TEMP_TEST\Data\true", "0308_POSITIVE", "1")