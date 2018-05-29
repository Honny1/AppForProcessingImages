import os
from threading import Thread

import FileProcessing

def renameJpgImages(src):

    i = 0
    FileProcessing.getFileList(src)
    file_list = open("list_file.txt", "r")

    progress = open("Progress.txt", "w")
    progress.write(str(0))
    progress.close()
    progress = open("Progress1.txt", "w")
    progress.write("Rename JPG...")
    progress.close()

    z = 0
    path, dirs, files = next(os.walk(src))
    file_count = len(files)

    for fileName in file_list:
        z += 1
        procenta = (z * (100 / float(file_count)))
        progress = open("Progress.txt", "w")
        progress.write(str(procenta))
        progress.close()

        fileName = fileName[:-1]
        if FileProcessing.rightJpgType(FileProcessing.getFileType(src,fileName)):
            os.rename(src+"/"+fileName, src+"/"+str(i) +"." + FileProcessing.getFileType(src,fileName))
            i+=1
    file_list.close()


def renameNefImages(src):



    i = 0
    FileProcessing.getFileList(src)
    file_list = open("list_file.txt", "r")


    progress = open("Progress.txt", "w")
    progress.write(str(0))
    progress.close()
    progress = open("Progress1.txt", "w")
    progress.write("Rename RAW...")
    progress.close()

    z = 0
    path, dirs, files = next(os.walk(src))
    file_count = len(files)

    for fileName in file_list:

        z += 1
        procenta = (z * (100 / float(file_count)))
        progress = open("Progress.txt", "w")
        progress.write(str(procenta))
        progress.close()

        fileName = fileName[:-1]
        if FileProcessing.rightNefType(FileProcessing.getFileType(src, fileName)):
            os.rename(src+"/"+fileName, src+"/"+str(i) +"." + FileProcessing.getFileType(src, fileName))
            i+=1
    file_list.close()