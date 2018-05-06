import os
import FileProcessing

def renameImages():
    i=0
    FileProcessing.getFileList()
    file_list = open("list_file.txt", "r")
    for fileName in file_list:
        fileName = fileName[:-1]
        if FileProcessing.rightFileType(FileProcessing.getFileType(fileName)):
            os.rename(fileName, str(i) +"." + FileProcessing.getFileType(fileName))
            i+=1