import rawpy
import imageio
import os
from tqdm import tqdm


def Nef2Jpg(src):
    Images = []
    src_files = os.listdir(src)
    for file in src_files:
        Images.append(os.path.join(src, file))

    try:
        os.makedirs(os.path.join(src, "Jpg"))
    except OSError:
        if not os.path.isdir(os.path.join(src, "Jpg")):
            raise

    for i in tqdm(range(len(Images))):
        if (Images[i].endswith(".nef")):
            with rawpy.imread(Images[i]) as raw:
                rgb = raw.postprocess()
            imageio.imsave(os.path.join(src, "Jpg", 'file_' + str(i) + '.jpg'), rgb)
        else:
            print("This isn't .nef File!")


src = input("SOURCE IMAGES:")
Nef2Jpg(src)