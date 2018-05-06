from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('DSC_0203.jpg')
exifdict = img._getexif()
if len(exifdict):
    for k in exifdict.keys():
        if k in TAGS.keys():
            print (TAGS[k], exifdict[k])
        else:
            print (k, exifdict[k])