# coding=utf-8
import os

def get_file_total_number(path):
    n=sum([len(x) for _, _, x in os.walk(os.path.dirname(path))])
    return n

def batch_count_number(path):
    print "Start:\n"
    for tempFile in os.listdir(path):
        path1=os.path.join(path,tempFile)
        m=get_file_total_number(path1 + "\\")
        if m > 10000:
            print path1 + " " + str(m)
    print "End:\n"
    return 1

if __name__=="__main__":
    batch_count_number(r"E:\161220_ICDAR_TEST")


