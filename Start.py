import time
from threading import Thread

import cleanData
runned=False


def startProgress():
    print(t.is_alive())
    if(t.is_alive()):
        t.join()
    t.start()


def start(copy, sort, fixImage, renameRaw, renameJpg,  newDirectory, sourceDirectory):

    import CopyFilesFromSDCart
    import ImageProcessing
    import RenameImages
    import SortFilesToDirectory
    import os

    nefDirectory = newDirectory+"/Nef"
    jpgDirectory = newDirectory+"/Jpg"
    if sourceDirectory == "" or False == os.path.exists(sourceDirectory):
        return "NotFoundSourceDir"
    elif copy == 1 and newDirectory == "":
        return "MissingNewDir"
    else:
        if copy == 0 and sort == 0 and renameJpg == 0 and renameRaw == 0 and fixImage == 0:
         return "NothingIsSelected"
        elif copy == 0 and sort == 0 and renameJpg == 0 and renameRaw == 0 and fixImage == 1:
            ImageProcessing.fixImage(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 0 and renameJpg == 0 and renameRaw == 1 and fixImage == 0:
            RenameImages.renameNefImages(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 0 and renameJpg == 0 and renameRaw == 1 and fixImage == 1:
            RenameImages.renameNefImages(sourceDirectory)
            ImageProcessing.fixImage(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 0 and renameJpg == 1 and renameRaw == 0 and fixImage == 0:
            RenameImages.renameJpgImages(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 0 and renameJpg == 1 and renameRaw == 0 and fixImage == 1:
            RenameImages.renameJpgImages(sourceDirectory)
            ImageProcessing.fixImage(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 0 and renameJpg == 1 and renameRaw == 1 and fixImage == 0:
            RenameImages.renameJpgImages(sourceDirectory)
            RenameImages.renameNefImages(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 0 and renameJpg == 1 and renameRaw == 1 and fixImage == 1:
            RenameImages.renameJpgImages(sourceDirectory)
            RenameImages.renameNefImages(sourceDirectory)
            ImageProcessing.fixImage(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 1 and renameJpg == 0 and renameRaw == 0 and fixImage == 0:
            SortFilesToDirectory.sortFilesToDirectory(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 1 and renameJpg == 0 and renameRaw == 0 and fixImage == 1:
            SortFilesToDirectory.sortFilesToDirectory(sourceDirectory)
            ImageProcessing.fixImage(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 1 and renameJpg == 0 and renameRaw == 1 and fixImage == 0:
            SortFilesToDirectory.sortFilesToDirectory(sourceDirectory)
            RenameImages.renameNefImages(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 1 and renameJpg == 0 and renameRaw == 1 and fixImage == 1:
            SortFilesToDirectory.sortFilesToDirectory(sourceDirectory)
            RenameImages.renameNefImages(sourceDirectory)
            ImageProcessing.fixImage(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 1 and renameJpg == 1 and renameRaw == 0 and fixImage == 0:
            SortFilesToDirectory.sortFilesToDirectory(sourceDirectory)
            RenameImages.renameJpgImages(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 1 and renameJpg == 1 and renameRaw == 0 and fixImage == 1:
            RenameImages.renameJpgImages(sourceDirectory)
            ImageProcessing.fixImage(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 1 and renameJpg == 1 and renameRaw == 1 and fixImage == 0:
            SortFilesToDirectory.sortFilesToDirectory(sourceDirectory)
            RenameImages.renameJpgImages(sourceDirectory)
            RenameImages.renameNefImages(sourceDirectory)
            return "OK"
        elif copy == 0 and sort == 1 and renameJpg == 1 and renameRaw == 1 and fixImage == 1:
            SortFilesToDirectory.sortFilesToDirectory(sourceDirectory)
            RenameImages.renameJpgImages(sourceDirectory)
            RenameImages.renameNefImages(sourceDirectory)
            ImageProcessing.fixImage(sourceDirectory)
            return "OK"
        elif copy == 1 and sort == 0 and renameJpg == 0 and renameRaw == 0 and fixImage == 0:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            return "OK"
        elif copy == 1 and sort == 0 and renameJpg == 0 and renameRaw == 0 and fixImage == 1:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            ImageProcessing.fixImage(newDirectory)
            return "OK"
        elif copy == 1 and sort == 0 and renameJpg == 0 and renameRaw == 1 and fixImage == 0:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            RenameImages.renameNefImages(newDirectory)
            return "OK"
        elif copy == 1 and sort == 0 and renameJpg == 0 and renameRaw == 1 and fixImage == 1:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            ImageProcessing.fixImage(newDirectory)
            RenameImages.renameNefImages(newDirectory)
            return "OK"
        elif copy == 1 and sort == 0 and renameJpg == 1 and renameRaw == 0 and fixImage == 0:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            RenameImages.renameJpgImages(newDirectory)
            return "OK"
        elif copy == 1 and sort == 0 and renameJpg == 1 and renameRaw == 0 and fixImage == 1:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            ImageProcessing.fixImage(newDirectory)
            RenameImages.renameJpgImages(newDirectory)
            return "OK"
        elif copy == 1 and sort == 0 and renameJpg == 1 and renameRaw == 1 and fixImage == 0:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            RenameImages.renameJpgImages(newDirectory)
            RenameImages.renameNefImages(newDirectory)
            return "OK"
        elif copy == 1 and sort == 0 and renameJpg == 1 and renameRaw == 1 and fixImage == 1:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            ImageProcessing.fixImage(newDirectory)
            RenameImages.renameJpgImages(newDirectory)
            RenameImages.renameNefImages(newDirectory)
            return "OK"
        elif copy == 1 and sort == 1 and renameJpg == 0 and renameRaw == 0 and fixImage == 0:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            SortFilesToDirectory.sortFilesToDirectory(newDirectory)
            return "OK"
        elif copy == 1 and sort == 1 and renameJpg == 0 and renameRaw == 0 and fixImage == 1:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            SortFilesToDirectory.sortFilesToDirectory(newDirectory)
            ImageProcessing.fixImage(jpgDirectory)
            return "OK"
        elif copy == 1 and sort == 1 and renameJpg == 0 and renameRaw == 1 and fixImage == 0:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            SortFilesToDirectory.sortFilesToDirectory(newDirectory)
            RenameImages.renameNefImages(nefDirectory)
            return "OK"
        elif copy == 1 and sort == 1 and renameJpg == 0 and renameRaw == 1 and fixImage == 1:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            SortFilesToDirectory.sortFilesToDirectory(newDirectory)
            RenameImages.renameNefImages(nefDirectory)
            ImageProcessing.fixImage(jpgDirectory)
            return "OK"
        elif copy == 1 and sort == 1 and renameJpg == 1 and renameRaw == 0 and fixImage == 0:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            SortFilesToDirectory.sortFilesToDirectory(newDirectory)
            RenameImages.renameJpgImages(jpgDirectory)
            return "OK"
        elif copy == 1 and sort == 1 and renameJpg == 1 and renameRaw == 0 and fixImage == 1:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            SortFilesToDirectory.sortFilesToDirectory(newDirectory)
            RenameImages.renameJpgImages(jpgDirectory)
            ImageProcessing.fixImage(jpgDirectory)
            return "OK"
        elif copy == 1 and sort == 1 and renameJpg == 1 and renameRaw == 1 and fixImage == 0:
            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            SortFilesToDirectory.sortFilesToDirectory(newDirectory)
            RenameImages.renameJpgImages(renameJpg)
            RenameImages.renameNefImages(renameRaw)
            return "OK"
        elif copy == 1 and sort == 1 and renameJpg == 1 and renameRaw == 1 and fixImage == 1:
            """import ProgressBar
            t = Thread(target=ProgressBar.run)
            t.start()"""

            startProgress()


            CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
            print(1)
            SortFilesToDirectory.sortFilesToDirectory(newDirectory)
            print(2)
            RenameImages.renameJpgImages(jpgDirectory)
            print(3)
            RenameImages.renameNefImages(nefDirectory)
            print(4)
            ImageProcessing.fixImage(jpgDirectory)
            progress = open("Progress1.txt", "w")
            progress.write("END")
            progress.close()

            time.sleep(2)

            cleanData.delete()
            return "OK"
        return "ERROR"

import ProgressBar
t = Thread(target=ProgressBar.run)