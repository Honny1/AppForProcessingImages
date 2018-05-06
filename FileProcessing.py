import os

def getFileList():
    file_list = open("list_file.txt", "w")
    for file in os.listdir('.'):
        file += "\n"
        file_list.write(file)
    file_list.close()


def getFileType(fileName):
    file = fileName.split(".")
    fileType = file[1]
    fileType = str.upper(fileType)
    return fileType


def rightFileType(fileType):
    if (fileType == 'IMAGE/JPEG' or fileType == "JPG" or fileType == "JPEG"):
        return True
    else:
        return False