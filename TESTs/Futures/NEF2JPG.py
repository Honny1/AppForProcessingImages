import rawpy
import imageio
import os
def Nef2Jpg(src):
    Images = []
    i=0
    src_files = os.listdir(src)
    for file in src_files:
        Images.append(os.path.join(src, file))

    try:
        os.makedirs(os.path.join(src, "Jpg"))
    except OSError:
        if not os.path.isdir(os.path.join(src, "Jpg")):
            raise

    for image in Images:
        i+=1
        with rawpy.imread(image) as raw:
            rgb = raw.postprocess()
        imageio.imsave(os.path.join(src, "Jpg", 'file_' + str(i) + '.jpg'), rgb)

    print("hotovo")



src = raw_input("SOURCE IMAGES:")
Nef2Jpg(src)