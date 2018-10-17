from image import *

import shutil
import rawpy
import imageio
import os

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

class AppGUI:
    def __init__(self, master):
        self.master = master
        master.title("HonyJeBuh")
        self.master.configure(background='grey93')
        self.label = Label(master, text="Source directory:")
        self.label.grid(row=0, column=0, sticky=N + S + W)

        self.entry = Entry(master, textvariable=src, width=20)
        self.entry.grid(row=0, column=1)

        self.label1 = Label(master, text="New directory:")
        self.label1.grid(row=2, column=0, sticky=N + S + W)

        self.entry1 = Entry(master, textvariable=newdir, width=20)
        self.entry1.grid(row=2, column=1)

        self.button = Button(master, text="RUN", bg="green", command=self.run)
        self.button.grid(row=3, column=2, sticky=N + S + E + W)

        self.label2 = Label(master, text="                                           ")
        self.label2.grid(row=4, column=2)

        self.button2 = Button(master, text="OPEN", bg="red", command=self.getFilePatch)
        self.button2.grid(row=0, column=2, sticky=N + S + E + W)

        self.button3 = Button(master, text="SAVE", bg="yellow", command=self.getNewFilePatch)
        self.button3.grid(row=2, column=2, sticky=N + S + E + W)

        self.button4 = Button(master, text="PUSH ON WEB", bg="blue", command=self.pushOnWeb)
        self.button4.grid(row=4, column=2, sticky=N + S + E + W)

        self.label3 = Label(master,
                            text="Random TEXT  Random TEXT Random TEXT\nRandom TEXT Random TEXT Random TEXT\nRandom TEXT Random TEXT Random TEXT",
                            bg="white")
        self.label3.grid(row=30, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)

        self.check_button4 = Checkbutton(master, text="NEF2JPG", variable=ch5, command=self.selectedAll)
        self.check_button4.grid(row=5, column=1, sticky=N + S + W)

        self.check_button5 = Checkbutton(master, text="divide by 100 ", variable=ch6, command=self.selectedAll)
        self.check_button5.grid(row=5, column=0, sticky=N + S + W)

        self.check_button1 = Checkbutton(master, text="Copy", variable=ch2, command=self.selectedCopy)
        self.check_button1.grid(row=4, column=0, sticky=N + S + W)

        self.check_button2 = Checkbutton(master, text="Separate Jpg and Nef", variable=ch3, command=self.selectedAll)
        self.check_button2.grid(row=4, column=1, sticky=N + S + W)

        self.check_button3 = Checkbutton(master, text="Fix Images", variable=ch4, command=self.selectedAll)
        self.check_button3.grid(row=3, column=1, sticky=N + S + W)

        self.check_button = Checkbutton(master, text="ALL", command=self.checkAll)
        self.check_button.grid(row=3, column=0, sticky=N + S + W)

        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.grid(row=9, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)
        self.progress_bar["maximum"] = 100

        self.label4 = Label(master, text="Ready")
        self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)

        self.selectedCopy()
        self.progress_bar["value"] = 0

    def selectedCopy(self):
        self.selectedAll()
        if ch2.get() != 1:
            self.entry1.configure(bg="grey", state='disabled')
        else:
            self.entry1.configure(bg="white",state='normal')

    def selectedAll(self):
        if ch2.get() == 1 and ch3.get() == 1 and ch4.get() == 1 and ch5.get() == 1 and ch6.get() == 1:
            self.check_button.select()
        else:
            self.check_button.deselect()

    def checkAll(self):
        cbs = [self.check_button1, self.check_button2, self.check_button3, self.check_button4, self.check_button5]

        for cb in cbs:
            cb.select()

        self.selectedCopy()

    def pushOnWeb(self):
        print("in progress...")

    def getFilePatch(self):
        self.entry.delete(0, 'end')
        self.master.update()
        sourceDir = filedialog.askdirectory(parent=self.master, initialdir="home")
        self.entry.insert(INSERT, sourceDir)
        self.master.update()

    def getNewFilePatch(self):
        self.entry1.delete(0, 'end')
        self.master.update()
        newDir = filedialog.asksaveasfilename(parent=self.master, initialdir="home")
        self.entry1.insert(INSERT, newDir)
        self.master.update()

    def imagesFix(self, src):
        self.progress_bar["value"] = 0
        self.label4 = Label(self.master, text="Fixing images...")
        self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)

        self.master.update()
        srcImages = []
        images = []
        src_files = os.listdir(src)
        for file in src_files:
            srcImages.append(os.path.join(src,file))

        for i in range(len(srcImages)):
            images.append(obrazek(srcImages[i], i))
        fileNum = 1
        file_count = len(images)
        for imageFile in images:
            fileNum += 1
            procenta = (fileNum * (100 / float(file_count)))
            self.progress_bar["value"] = procenta
            imageFile.fixImage()
            self.master.update()

    def copyFiles(self, src, dest):
        self.progress_bar["value"] = 0
        self.label4 = Label(self.master, text="Copying...")
        self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)

        self.master.update()
        try:
            os.makedirs(dest)
        except OSError:
            if not os.path.isdir(dest):
                raise

        src_files = os.listdir(src)
        fileNum = 1
        file_count = len(src_files)
        for file_name in src_files:
            fileNum += 1
            procenta = (fileNum * (100 / float(file_count)))
            self.progress_bar["value"] = procenta
            self.master.update()
            full_file_name = os.path.join(src, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest)

    def sortFilesToDirectory(self, src):
        self.progress_bar["value"] = 0
        self.label4 = Label(self.master, text="Separation...")
        self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)
        self.master.update()
        try:
            os.makedirs(src + "/Nef")
        except OSError:
            if not os.path.isdir(os.path.join(src, "Nef")):
                raise
        src_files = os.listdir(src)
        fileNum = 1
        file_count = len(src_files)
        for file_name in src_files:
            fileNum += 1
            procenta = (fileNum * (100 / float(file_count)))
            self.progress_bar["value"] = procenta
            self.master.update()
            full_file_name = os.path.join(src, file_name)
            if os.path.isfile(full_file_name):
                filename, file_extension = os.path.splitext(full_file_name)
                file_extension = file_extension.lower()
                if file_extension == ".nef":
                    shutil.move(full_file_name, src + "/Nef")
                else:
                    print(file_extension)

    def split(self,src):
        self.progress_bar["value"] = 0
        self.label4 = Label(self.master, text="Dividing...")
        self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)
        self.master.update()
        def copyFile(src, dest):
            try:
                os.makedirs(dest)
            except OSError:
                if not os.path.isdir(dest):
                    raise

            if os.path.isfile(src):
                shutil.copy(src, dest)
        Images = []
        x = 0
        xx = 1
        src_files = os.listdir(src)
        for file in src_files:
            Images.append(os.path.join(src, file))
        fileNum = 1
        for i in range(len(Images)):
            fileNum += 1
            procenta = (fileNum * (100 / float(len(Images))))
            self.progress_bar["value"] = procenta
            self.master.update()
            xx += 1
            if xx == 99:
                x += 1
                copyFile(Images[i], os.path.join(src, str(x)))
                xx = 0
            else:
                copyFile(Images[i], os.path.join(src, str(x)))

    def Nef2Jpg(self, src):
        self.progress_bar["value"] = 0
        self.label4 = Label(self.master, text="Converting...")
        self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)
        self.master.update()
        Images = []
        src_files = os.listdir(src)
        for file in src_files:
            Images.append(os.path.join(src, file))

        try:
            os.makedirs(os.path.join(src, "Jpg"))
        except OSError:
            if not os.path.isdir(os.path.join(src, "Jpg")):
                raise
        fileNum = 1
        for i in range(len(Images)):
            if (Images[i].endswith(".NEF")):
                fileNum += 1
                procenta = (fileNum * (100 / float(len(Images))))
                self.progress_bar["value"] = procenta
                self.master.update()
                with rawpy.imread(Images[i]) as raw:
                    rgb = raw.postprocess()
                imageio.imsave(os.path.join(src, "Jpg", 'file_' + str(i) + '.jpg'), rgb)
            else:
                fileNum += 1
                procenta = (fileNum * (100 / float(len(Images))))
                self.progress_bar["value"] = procenta
                self.master.update()

                print("This isn't .nef File!")

    def run(self):
        global x
        copy = ch2.get()
        sort = ch3.get()
        fixImage = ch4.get()
        nefToJpg = ch5.get()
        split = ch6.get()

        newDir = newdir.get()
        sourceDir = src.get()

        if self.againPressButton(newDir, sourceDir, copy, sort, fixImage,nefToJpg, split):
            result = messagebox.askquestion("Are You Sure?", "Again on the same?", icon='warning')
            if result == 'yes':
                print("run")

                print(copy, sort, fixImage, newDir, sourceDir, nefToJpg, split)

                if copy == 1:
                    self.copyFiles(sourceDir, newDir)
                if sort == 1:
                    if newDir == "":
                        self.sortFilesToDirectory(sourceDir)
                    else:
                        self.sortFilesToDirectory(newDir)
                if nefToJpg == 1:
                    if copy == 0:
                        self.Nef2Jpg(sourceDir)
                    else:
                        self.Nef2Jpg(newDir)
                if fixImage == 1:
                    if copy == 0:
                        self.imagesFix(sourceDir)
                    else:
                        self.imagesFix(newDir)
                if split == 1:
                    if copy == 0:
                        self.split(sourceDir)
                    else:
                        self.split(newDir)

                self.label4 = Label(self.master, text="Done")
                self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)
                print("Done")
                x = 1
            else:
                self.label4 = Label(self.master, text="I'm do nothing")
                self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)
                print("I'm do nothing")

        else:
            print("run")

            print(copy, sort, fixImage, newDir, sourceDir, nefToJpg, split)

            if copy == 1:
                self.copyFiles(sourceDir, newDir)
            if sort == 1:
                if newDir == "":
                    self.sortFilesToDirectory(sourceDir)
                else:
                    self.sortFilesToDirectory(newDir)
            if nefToJpg == 1:
                if copy == 0:
                    self.Nef2Jpg(sourceDir)
                else:
                    self.Nef2Jpg(newDir)
            if fixImage == 1:
                if copy == 0:
                    self.imagesFix(sourceDir)
                else:
                    self.imagesFix(newDir)
            if split == 1:
                if copy == 0:
                    self.split(sourceDir)
                else:
                    self.split(newDir)

            self.label4 = Label(self.master, text="Done")
            self.label4.grid(row=20, column=0, rowspan=3, columnspan=3, sticky=N + S + E + W)
            print("Done")
            x = 1

    def againPressButton(self, newDir, sourceDir, copy, sort, fixImage, nefToJpg, split):
        global x, oldNewDir, oldSourceDir, oldCopy, oldSort, oldFixImage, oldNefToJpg, oldSplit

        if x == 0:
            oldNewDir = newdir.get()
            oldSourceDir = src.get()
            oldCopy = ch2.get()
            oldSort = ch3.get()
            oldFixImage = ch4.get()
            oldNefToJpg = ch5.get()
            oldSplit = ch6.get()
            return False
        elif x == 1 and oldNewDir == newDir and oldSourceDir == sourceDir and oldCopy == copy and oldSort == sort and oldFixImage == fixImage and oldNefToJpg == nefToJpg and oldSplit == split:
            oldNewDir = newdir.get()
            oldSourceDir = src.get()
            oldCopy = ch2.get()
            oldSort = ch3.get()
            oldFixImage = ch4.get()
            oldNefToJpg = ch5.get()
            oldSplit = ch6.get()
            return True
        elif x == 1 and oldNewDir != newDir and oldSourceDir != sourceDir and oldCopy != copy and oldSort != sort and oldFixImage != fixImage and oldNefToJpg != nefToJpg and oldSplit != split:
            oldNewDir = newdir.get()
            oldSourceDir = src.get()
            oldCopy = ch2.get()
            oldSort = ch3.get()
            oldFixImage = ch4.get()
            oldNefToJpg = ch5.get()
            oldSplit = ch6.get()
            x = 0
            return False
        elif x == 1 and (
                oldNewDir != newDir or oldSourceDir != sourceDir or oldCopy != copy or oldSort != sort or oldFixImage != fixImage or oldNefToJpg != nefToJpg or oldSplit != split):
            oldNewDir = newdir.get()
            oldSourceDir = src.get()
            oldCopy = ch2.get()
            oldSort = ch3.get()
            oldFixImage = ch4.get()
            oldNefToJpg = ch5.get()
            oldSplit = ch6.get()
            x = 0
            return False
        else:
            print(newDir, sourceDir, x, oldSourceDir, oldNewDir)


root = Tk()
ch2 = IntVar()
ch3 = IntVar()
ch4 = IntVar()
ch6 = IntVar()
ch5 = IntVar()
x = 0

src = StringVar()
newdir = StringVar()
srcImages = []
images = []

my_gui = AppGUI(root)
root.mainloop()