from threading import Thread
from gevent import os
import CopyFilesFromSDCart
import FileProcessing
import cv2
import pexif


# Autor: HoNnY


def flipImage(src,fileName, flipnum):
    img = cv2.imread(src+"/"+fileName)
    new = cv2.flip(img, flipnum)
    cv2.imwrite(src+"/"+fileName, new)


def rotateImage(src, fileName, angle):
    image = cv2.imread(src+"/"+fileName)
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    new = cv2.warpAffine(image, M, (w, h))
    cv2.imwrite(src+"/"+fileName, new)


def fixImage(src):

    src1 = src
    CopyFilesFromSDCart.copyFiles(src, "C:/core")
    FileProcessing.getFileList("C:/core")
    src = "C:/core"
    file_list = open("list_file.txt", "r")

    progress = open("Progress.txt", "w")
    progress.write(str(0))
    progress.close()
    progress = open("Progress1.txt", "w")
    progress.write("Fixing Images...")
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
            img = pexif.JpegFile.fromFile(src+"/"+fileName)
            try:
                orientation = img.exif.primary.Orientation[0]

                if orientation is 6:
                    rotateImage(src, fileName, 360)
                elif orientation is 8:
                    rotateImage(src, fileName, 360)
                elif orientation is 3:
                    rotateImage(src, fileName, 180)
                elif orientation is 2:
                    flipImage(src, fileName, 1)
                elif orientation is 5:
                    flipImage(src, fileName, 1)
                    rotateImage(src, fileName, 360)
                elif orientation is 7:
                    flipImage(src, fileName, 1)
                    rotateImage(src, fileName, 360)
                elif orientation is 4:
                    flipImage(src, fileName, 1)
                    rotateImage(src, fileName, 180)
                else:
                    rotateImage(src, fileName, 360)
                print("Image Saved")
            except:
                pass
    file_list.close()
    CopyFilesFromSDCart.copyFiles(src, src1)