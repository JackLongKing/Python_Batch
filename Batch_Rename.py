#coding=UTF-8

import os

def batchrename_addpre(path,ch):
    print "Rename Start:\n"
    for tempImg in os.listdir(path):
        os.rename(path+"\\"+tempImg,path+"\\"+ch+tempImg)
    print "Rename End:\n"

def batchrenamefile_addpost(path,ch):
    print "Rename Start:\n"
    for tempFile in os.listdir(path):
        os.rename(path+"\\"+tempFile,path+"\\"+tempFile+ch)
    print "Rename End:\n"

def batchrename_deletepre(path,ch):
    print "Rename Start:\n"
    for tempImg in os.listdir(path):
        os.rename(path+"\\"+tempImg,path+"\\"+tempImg.split(ch)[-1])
    print "Rename End:\n"

def batchfilerename_deletepost(path):
    print "Rename Start:\n"
    for tempFile in os.listdir(path):
        length=len(tempFile)
        temp=tempFile[0:length-4]
        os.rename(path+"\\"+tempFile,path+"\\"+temp)
    print "Rename End:\n"

def batchrename(path,ch1,ch2):
    print "Rename Start:\n"
    for tempFile in os.listdir(path):
        if ch1 in tempFile:
            tempFile1=tempFile[0:2]+ch2+tempFile[4:]
            os.rename(path + "\\" + tempFile, path + "\\" + tempFile1)
    print "Rename End:\n"

if __name__=="__main__":
    # batchrename_deletepre(r"E:\CNN_DATA\test\img_22","P_P")
    # batchrename_addpre(r"E:\CNN_DATA\ClassifiedDataFoTrainTest\TestData\NegativeSamples","N_")
    # batchrenamefile_addpost(r"E:\temp", "_1")
    # batchfilerename_deletepost(r"E:\temp")
    batchrename(r"E:\DogCat\Train\NCat", "t.", "t_")
