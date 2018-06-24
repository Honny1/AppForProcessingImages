import cv2
import pexif
import os


class obrazek:

    def __init__(self, src="", num=0):
        self.src = src
        self.num = num

    def __str__(self):
        return "SOURCE IMAGE: " + self.src + " NUM IMAGE: " + str(self.num)

    def flipImage(self, flipNum):
        img = cv2.imread(self.src)
        new = cv2.flip(img, flipNum)
        cv2.imwrite(self.src, new)

    def rotateImage(self, angle):
        image = cv2.imread(self.src)
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        new = cv2.warpAffine(image, M, (w, h))
        cv2.imwrite(self.src, new)

    def fixImage(self):
        filename, file_extension = os.path.splitext(self.src)
        file_extension = file_extension.lower()
        if file_extension == ".jpg" or file_extension == ".jpeg":
            img = pexif.JpegFile.fromFile(self.src)
            try:
                orientation = img.exif.primary.Orientation[0]
                if orientation is 6:
                    self.rotateImage(360)
                elif orientation is 8:
                    self.rotateImage(360)
                elif orientation is 3:
                    self.rotateImage(180)
                elif orientation is 2:
                    self.flipImage(1)
                elif orientation is 5:
                    self.flipImage(1)
                    self.rotateImage(360)
                elif orientation is 7:
                    self.flipImage(1)
                    self.rotateImage(360)
                elif orientation is 4:
                    self.flipImage(1)
                    self.rotateImage(180)
                else:
                    self.rotateImage(360)
                print("Image Saved")
            except:
                pass