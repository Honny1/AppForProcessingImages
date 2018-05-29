import shutil
import MakeDirectory
import os
import FileProcessing

def sortFilesToDirectory(src):


    FileProcessing.getFileList(src)
    MakeDirectory.makeDirectory(src+"/Nef")
    MakeDirectory.makeDirectory(src+"/Jpg")
    file_list = open("list_file.txt", "r")


    progress = open("Progress.txt", "w")
    progress.write(str(0))
    progress.close()
    progress = open("Progress1.txt", "w")
    progress.write("Sort...")
    progress.close()

    z = 0
    path, dirs, files = next(os.walk(src))
    file_count = len(files)

    for file_name in file_list:

        z += 1
        procenta = (z * (100 / float(file_count)))
        progress = open("Progress.txt", "w")
        progress.write(str(procenta))
        progress.close()

        file_name = file_name[:-1]
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            if FileProcessing.rightNefType(FileProcessing.getFileType(src, file_name)):
                shutil.copy(full_file_name, src+"/Nef")
            elif FileProcessing.rightJpgType(FileProcessing.getFileType(src, file_name)):
                shutil.copy(full_file_name, src+"/Jpg")
            else:
                print(FileProcessing.getFileType(src, file_name))

    file_list.close()