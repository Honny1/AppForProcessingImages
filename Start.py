import CopyFilesFromSDCart
import ImageProcessing
import RenameImages
import SortFilesToDirectory

newDirectory="C:/Hony"
sourceDirectory="D:/100D3300"
nefDirectory=newDirectory+"/Nef"
jpgDirectory=newDirectory+"/Jpg"

CopyFilesFromSDCart.copyFiles(sourceDirectory,newDirectory)
print("20%")
SortFilesToDirectory.sortFilesToDirectory(newDirectory)
print("40%")
RenameImages.renameJpgImages(jpgDirectory)
print("60%")
RenameImages.renameNefImages(nefDirectory)
print("80%")
ImageProcessing.fixImage(jpgDirectory)
print("100%")

print("The End")

