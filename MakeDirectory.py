import os

def makeDirectory(src):
    try:
        os.makedirs(src)
    except OSError:
        if not os.path.isdir(src):
            raise