import CopyFilesFromSDCart
import ImageProcessing
import RenameImages
import SortFilesToDirectory

def start(copy, sort, fixImage, renameRaw, renameJpg,  newDirectory, sourceDirectory):

    nefDirectory=newDirectory+"/Nef"
    jpgDirectory=newDirectory+"/Jpg"
    if copy == 0 and sort == 0 and renameJpg == 0 and renameRaw == 0 and fixImage == 0:
        return "NothingIsSelected"
    elif copy == 0 and sort == 0 and renameJpg == 0 and renameRaw == 0 and fixImage == 1:
        ImageProcessing.fixImage(sourceDirectory)
    elif copy == 0 and sort == 0 and renameJpg == 0 and renameRaw == 1 and fixImage == 0:
    elif copy == 0 and sort == 0 and renameJpg == 0 and renameRaw == 1 and fixImage == 1:
    elif copy == 0 and sort == 0 and renameJpg == 1 and renameRaw == 0 and fixImage == 0:
    elif copy == 0 and sort == 0 and renameJpg == 1 and renameRaw == 0 and fixImage == 1:
    elif copy == 0 and sort == 0 and renameJpg == 1 and renameRaw == 1 and fixImage == 0:
    elif copy == 0 and sort == 0 and renameJpg == 1 and renameRaw == 1 and fixImage == 1:
    elif copy == 0 and sort == 1 and renameJpg == 0 and renameRaw == 0 and fixImage == 0:
    elif copy == 0 and sort == 1 and renameJpg == 0 and renameRaw == 0 and fixImage == 1:
    elif copy == 0 and sort == 1 and renameJpg == 0 and renameRaw == 1 and fixImage == 0:
    elif copy == 0 and sort == 1 and renameJpg == 0 and renameRaw == 1 and fixImage == 1:
    elif copy == 0 and sort == 1 and renameJpg == 1 and renameRaw == 0 and fixImage == 0:
    elif copy == 0 and sort == 1 and renameJpg == 1 and renameRaw == 0 and fixImage == 1:
    elif copy == 0 and sort == 1 and renameJpg == 1 and renameRaw == 1 and fixImage == 0:
    elif copy == 0 and sort == 1 and renameJpg == 1 and renameRaw == 1 and fixImage == 1:
    elif copy == 1 and sort == 0 and renameJpg == 0 and renameRaw == 0 and fixImage == 0:
    elif copy == 1 and sort == 0 and renameJpg == 0 and renameRaw == 0 and fixImage == 1:
    elif copy == 1 and sort == 0 and renameJpg == 0 and renameRaw == 1 and fixImage == 0:
    elif copy == 1 and sort == 0 and renameJpg == 0 and renameRaw == 1 and fixImage == 1:
    elif copy == 1 and sort == 0 and renameJpg == 1 and renameRaw == 0 and fixImage == 0:
    elif copy == 1 and sort == 0 and renameJpg == 1 and renameRaw == 0 and fixImage == 1:
    elif copy == 1 and sort == 0 and renameJpg == 1 and renameRaw == 1 and fixImage == 0:
    elif copy == 1 and sort == 0 and renameJpg == 1 and renameRaw == 1 and fixImage == 1:
    elif copy == 1 and sort == 1 and renameJpg == 0 and renameRaw == 0 and fixImage == 0:
    elif copy == 1 and sort == 1 and renameJpg == 0 and renameRaw == 0 and fixImage == 1:
    elif copy == 1 and sort == 1 and renameJpg == 0 and renameRaw == 1 and fixImage == 0:
    elif copy == 1 and sort == 1 and renameJpg == 0 and renameRaw == 1 and fixImage == 1:
    elif copy == 1 and sort == 1 and renameJpg == 1 and renameRaw == 0 and fixImage == 0:
    elif copy == 1 and sort == 1 and renameJpg == 1 and renameRaw == 0 and fixImage == 1:
    elif copy == 1 and sort == 1 and renameJpg == 1 and renameRaw == 1 and fixImage == 0:
    elif copy == 1 and sort == 1 and renameJpg == 1 and renameRaw == 1 and fixImage == 1:

        CopyFilesFromSDCart.copyFiles(sourceDirectory, newDirectory)
        SortFilesToDirectory.sortFilesToDirectory(newDirectory)
        RenameImages.renameJpgImages(jpgDirectory)
        RenameImages.renameNefImages(nefDirectory)
        ImageProcessing.fixImage(jpgDirectory)

    return 1
