import os
import cv2
import pexif

#Autor: HoNnY

def flipImage(fileName,flipnum):
    img = cv2.imread(fileName)
    new = cv2.flip(img, flipnum)
    cv2.imwrite(fileName, new)

def rotateImage(fileName,angle):
    image = cv2.imread(fileName)
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    new = cv2.warpAffine(image, M, (w, h))
    cv2.imwrite(fileName, new)

def getFileList():
    file_list=open("list_file.txt","w")
    for file in os.listdir('.'):
        file+="\n"
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

def fixImage():
    getFileList()
    file_list = open("list_file.txt", "r")
    for fileName in file_list:
        fileName = fileName[:-1]
        if (rightFileType(getFileType(fileName))):
            img = pexif.JpegFile.fromFile(fileName)
            try:
                orientation = img.exif.primary.Orientation[0]

                if orientation is 6:
                    rotateImage(fileName,360)
                elif orientation is 8:
                    rotateImage(fileName, 360)
                elif orientation is 3:
                    print(fileName)
                    rotateImage(fileName, 180)
                elif orientation is 2:
                    flipImage(fileName,1)
                elif orientation is 5:
                    flipImage(fileName, 1)
                    rotateImage(fileName, 360)
                elif orientation is 7:
                    flipImage(fileName, 1)
                    rotateImage(fileName, 360)
                elif orientation is 4:
                    flipImage(fileName, 1)
                    rotateImage(fileName, 180)
                print("Image Saved")
            except: pass
    file_list.close()


fixImage()
