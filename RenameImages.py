import os
import FileProcessing

def renameJpgImages(src):
    i=0
    FileProcessing.getFileList(src)
    file_list = open("list_file.txt", "r")
    for fileName in file_list:
        fileName = fileName[:-1]
        if FileProcessing.rightJpgType(FileProcessing.getFileType(src,fileName)):
            os.rename(src+"/"+fileName, src+"/"+str(i) +"." + FileProcessing.getFileType(src,fileName))
            i+=1

def renameNefImages(src):
    i=0
    FileProcessing.getFileList(src)
    file_list = open("list_file.txt", "r")
    for fileName in file_list:
        fileName = fileName[:-1]
        if FileProcessing.rightNefType(FileProcessing.getFileType(src, fileName)):
            os.rename(src+"/"+fileName, src+"/"+str(i) +"." + FileProcessing.getFileType(src, fileName))
            i+=1