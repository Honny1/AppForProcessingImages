import os
import shutil
from threading import Thread

import MakeDirectory

def copyFiles(src,dest):

    MakeDirectory.makeDirectory(dest)

    progress = open("Progress.txt", "w")
    progress.write(str(0))
    progress.close()
    progress = open("Progress1.txt", "w")
    progress.write("Copy...")
    progress.close()

    z = 0
    path, dirs, files = next(os.walk(src))
    file_count = len(files)

    src_files = os.listdir(src)
    for file_name in src_files:

        z += 1
        procenta=(z * (100 / float(file_count)))
        progress = open("Progress.txt", "w")
        progress.write(str(procenta))
        progress.close()

        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)