# coding=utf-8

import os

def mkdir(path,i):
    path=path+"img_"+str(i)+"_Inter"
    path=path.strip()
    path=path.rstrip("\\")
    isExist=os.path.exists(path)

    if not isExist:
        os.mkdir(path)
        print path+" create successfully.\n"
        return True
    else:
        print path+"already existed.\n"
        return False

def mkdir2(path,i):
    path=path+"0"+str(i)
    path=path.strip()
    path=path.rstrip("\\")
    isExist=os.path.exists(path)

    if not isExist:
        os.mkdir(path)
        print path+" create successfully.\n"
        return True
    else:
        print path+"already existed.\n"
        return False

def alterfilename(path,mystring):
    print "Alter Start:\n"
    for tempImg in os.listdir(path):
        oldPath=os.path.join(path,tempImg)
        dstImg=mystring+tempImg
        newPath=os.path.join(path,dstImg)
        os.rename(oldPath,newPath)
    print "Alter End.\n"



if __name__=="__main__":
    print "Process start:\n"
    # mkpath = "E:\\ClassifiedData\\IntermediateSamples\\"
    mkpath="C:\\Users\\Administrator\\Desktop\\temp\\"
    for i in range(1,21,1):
        mkdir2(mkpath, i)
    # alterfilename(r"E:\Chars74K\EnglishImg\Img\GoodImg","CKEIG")

