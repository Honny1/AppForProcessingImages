import shutil
import MakeDirectory
import os
import FileProcessing

def sortFilesToDirectory(src):
    FileProcessing.getFileList(src)
    MakeDirectory.makeDirectory(src+"/Nef")
    MakeDirectory.makeDirectory(src+"/Jpg")
    file_list = open("list_file.txt", "r")
    for file_name in file_list:
        file_name = file_name[:-1]
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            if FileProcessing.rightNefType(FileProcessing.getFileType(src, file_name)):
                shutil.copy(full_file_name, src+"/Nef")
            elif FileProcessing.rightJpgType(FileProcessing.getFileType(src, file_name)):
                shutil.copy(full_file_name, src+"/Jpg")
            else:
                print(FileProcessing.getFileType(src, file_name))
