import os

def getFileList(src):
    file_list = open("list_file.txt", "w")
    src_files = os.listdir(src)
    for file in src_files:
        file += "\n"
        file_list.write(file)
    file_list.close()


def getFileType(src,fileName):
    if os.path.isdir(src+"/"+fileName):
        return "dir"
    else:
        file = fileName.split(".")
        fileType = file[1]
        fileType = str.upper(fileType)
        return fileType


def rightJpgType(fileType):
    if (fileType == 'IMAGE/JPEG' or fileType == "JPG" or fileType == "JPEG"):
        return True
    else:
        return False


def rightNefType(fileType):
    if (fileType == 'CR2' or fileType == "NEF" or fileType == "RAW"):
        return True
    else:
        return False
