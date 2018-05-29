import os
import shutil

def delete():
    try:
        os.remove("list_file.txt")
        os.remove("Progress1.txt")
        os.remove("Progress.txt")
        shutil.rmtree("C:/core")
    except OSError, e:
        print ("Error: %s - %s." % (e.filename, e.strerror))