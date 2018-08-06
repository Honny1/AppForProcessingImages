import os
import shutil

def split(src):
    Images = []
    x=0
    src_files = os.listdir(src)
    for file in src_files:
        Images.append(os.path.join(src, file))

    for i in range(len(Images)):
        if i == 99:
            x+=1
            copyFile(Images[i],os.path.join(src, x))
        else:
            copyFile(Images[i], os.path.join(src, x))

def copyFile(src, dest):
    try:
        os.makedirs(dest)
    except OSError:
        if not os.path.isdir(dest):
            raise

    if os.path.isfile(src):
        shutil.copy(src, dest)

src = raw_input("SOURCE IMAGES:")
split(src)