# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("DSC_0202.jpg")
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(center, 360, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imwrite("IDK.jpg", rotated)