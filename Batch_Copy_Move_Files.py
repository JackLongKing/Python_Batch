#coding=UTF-8

import os
import shutil

def copy_files(src_path_file,dst_path_file):
    print "Copy Start:\n"
    shutil.copy(src_path_file,dst_path_file)
    print "Copy End;\n"

def batch_copy_files(path1,path2):
    print "Copy Start:\n"
    shutil.copytree(path1,path2)
    print "Copy End;\n"




if __name__=="__main__":
    print "hello world"
    #batch_copy_files(r"E:\CNN_DATA\test\img_22",r"E:\CNN_DATA\test2\\img_22")
