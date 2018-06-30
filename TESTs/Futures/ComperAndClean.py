import os
import shutil

def comper(src):
    JpgImages = []
    NefImages = []
    src_files = os.listdir(src)
    for file in src_files:
        JpgImages.append(os.path.join(src, file))

    src_files = os.listdir(os.path.join(src, "Nef"))
    for file in src_files:
        NefImages.append(os.path.join(os.path.join(src, "Nef"), file))

    for i in range(len(NefImages)):
        for j in range(len(JpgImages)):
            filename, file_extension = os.path.splitext(os.path.basename(JpgImages[j]))
            filename1, file_extension1 = os.path.splitext(os.path.basename(NefImages[i]))

            if filename == filename1:
                copyFile(NefImages[i],os.path.join(src, "Nef1"))

def copyFile(src, dest):
    try:
        os.makedirs(dest)
    except OSError:
        if not os.path.isdir(dest):
            raise

    if os.path.isfile(src):
        shutil.copy(src, dest)

src = raw_input("SOURCE IMAGES:")
comper(src)