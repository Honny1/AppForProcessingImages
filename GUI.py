from tkinter import *
from tkinter import filedialog
import tkMessageBox
import Start


def inicializaceOkna():
    okno.title("AppForProcessingImages")
    okno.geometry("400x200")

    okno.update_idletasks()
    w = okno.winfo_screenwidth()
    h = okno.winfo_screenheight()
    size = tuple(int(_) for _ in okno.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    okno.geometry("%dx%d+%d+%d" % (size + (x, y)))


def obsahOkna():
    L1 = Label(okno, text="Source directory:")
    L1.grid(row=0, column=0, sticky=N+S+W)

    global E1, E2, ch1, ch2, ch3, ch4
    E1 = Entry(okno, textvariable=src, width=20)
    E1.grid(row=0, column=1)

    L2 = Label(okno, text="New directory:")
    L2.grid(row=2, column=0, sticky=N+S+W)

    E2 = Entry(okno, textvariable=Dir, width=20)
    E2.grid(row=2, column=1)

    B1 = Button(okno, text="RUN", bg="green", command=run)
    B1.grid(row=3, column=2, sticky=N+S+E+W)

    L3 = Label(okno, text="                                           ")
    L3.grid(row=4, column=2)

    B2 = Button(okno, text="PUSH ON WEB", bg="blue", command=pushOnWeb)
    B2.grid(row=6, column=0, sticky=N+S+E+W)

    B3 = Button(okno, text="OPEN", bg="red", command=getFilePatch)
    B3.grid(row=0, column=2, sticky=N+S+E+W)

    B4 = Button(okno, text="SAVE", bg="yellow", command=getNewFilePatch)
    B4.grid(row=2, column=2, sticky=N+S+E+W)

    B5 = Button(okno, text="Just a few images", bg="blue", command=justAFewImages)
    B5.grid(row=6, column=1, sticky=N + S + E + W)

    B6 = Button(okno, text="Open new directory", bg="blue", command=openNewDir)
    B6.grid(row=6, column=2, sticky=N + S + E + W)

    L4 = Label(okno, text="Random TEXT  Random TEXT Random TEXT\nRandom TEXT Random TEXT Random TEXT\nRandom TEXT Random TEXT Random TEXT", bg="white")
    L4.grid(row=7,column=0,rowspan = 3, columnspan = 3,sticky=N + S + E + W)

    Ch6 = Checkbutton(okno, text="ALL", variable=ch6)
    Ch6.grid(row=3, column=0, sticky=N + S + W)

    Ch1 = Checkbutton(okno, text="Copy", variable=ch1)
    Ch1.grid(row=4, column=0, sticky=N+S+W)

    Ch2 = Checkbutton(okno, text="Sort  (on Jpg and Nef)", variable=ch2)
    Ch2.grid(row=5, column=0, sticky=N+S+W)

    Ch3 = Checkbutton(okno, text="Fix Images", variable=ch3)
    Ch3.grid(row=3, column=1, sticky=N+S+W)

    Ch4 = Checkbutton(okno, text="Rename RAW", variable=ch4)
    Ch4.grid(row=4, column=1, sticky=N+S+W)

    Ch5 = Checkbutton(okno, text="Rename JPG", variable=ch5)
    Ch5.grid(row=5, column=1, sticky=N+S+W)




def zviditelneniOkna():
    okno.mainloop()


def pushOnWeb():
    L3 = Label(okno, text="                                           ")
    L3.grid(row=4, column=2)

    L3 = Label(okno, text="Preparing...")
    L3.grid(row=4, column=2)

def justAFewImages():
    L3 = Label(okno, text="                                           ")
    L3.grid(row=4, column=2)

    L3 = Label(okno, text="Preparing...")
    L3.grid(row=4, column=2)

def openNewDir():
    L3 = Label(okno, text="                                           ")
    L3.grid(row=4, column=2)

    L3 = Label(okno, text="Preparing...")
    L3.grid(row=4, column=2)



def run():
    global x
    if (ch6.get() == 1):
        copy = 1
        sort = 1
        fixImage = 1
        renameRaw = 1
        renameJpg = 1
    else:
        copy = ch1.get()
        sort = ch2.get()
        fixImage = ch3.get()
        renameRaw = ch4.get()
        renameJpg = ch5.get()

    newDir = Dir.get()
    sourceDir = src.get()

    if (againPressButton(newDir, sourceDir)):
        result = tkMessageBox.askquestion("Are You Sure?", "Again on the same?", icon='warning')
        if result == 'yes':
            print("run")
            L3 = Label(okno, text="                       ")
            L3.grid(row=4, column=2)

            L3 = Label(okno, text="Processing...")
            L3.grid(row=4, column=2)

            okno.update()

            print(copy, sort, fixImage, renameRaw, renameJpg, newDir, sourceDir)
            done = Start.start(copy, sort, fixImage, renameRaw, renameJpg, newDir, sourceDir)
            print(done)

            L3 = Label(okno, text="                                           ")
            L3.grid(row=4, column=2)

            L3 = Label(okno, text=done)
            L3.grid(row=4, column=2)

            okno.update()

            x = 1
        else:
            L3 = Label(okno, text="                                           ")
            L3.grid(row=4, column=2)

            L3 = Label(okno, text="I'm do nothing")
            L3.grid(row=4, column=2)

            okno.update()

    else:
        print("run")
        L3 = Label(okno, text="                                           ")
        L3.grid(row=4, column=2)

        L3 = Label(okno, text="Processing...")
        L3.grid(row=4, column=2)

        okno.update()

        print(copy, sort, fixImage, renameRaw, renameJpg, newDir, sourceDir)
        done = Start.start(copy, sort, fixImage, renameRaw, renameJpg, newDir, sourceDir)
        print(done)

        L3 = Label(okno, text="                                           ")
        L3.grid(row=4, column=2)

        L3 = Label(okno, text=done)
        L3.grid(row=4, column=2)

        okno.update()

        x=1


def getFilePatch():
    sourceDir = filedialog.askdirectory(parent=okno, initialdir="E:/")
    E1.insert(INSERT, sourceDir)
    okno.update()


def getNewFilePatch():
    newDir = filedialog.asksaveasfilename()
    E2.insert(INSERT, newDir)
    okno.update()


def againPressButton(newDir, sourceDir):
    global x,oldNewDir, oldSourceDir

    if x == 0:
        oldNewDir = Dir.get()
        oldSourceDir = src.get()
        return False
    elif x == 1 and oldNewDir == newDir and oldSourceDir == sourceDir:
        oldNewDir = Dir.get()
        oldSourceDir = src.get()
        return True
    elif x == 1 and oldNewDir != newDir and oldSourceDir != sourceDir:
        oldNewDir = Dir.get()
        oldSourceDir = src.get()
        x = 0
        return False
    elif x == 1 and (oldNewDir != newDir or oldSourceDir != sourceDir):
        oldNewDir = Dir.get()
        oldSourceDir = src.get()
        x = 0
        return False
    else:
        print(newDir, sourceDir, x, oldSourceDir, oldNewDir)


#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
okno = Tk()

ch1 = IntVar()
ch2 = IntVar()
ch3 = IntVar()
ch4 = IntVar()
ch5 = IntVar()
ch6 = IntVar()

src = StringVar()
Dir = StringVar()

global sourceDir, newDir

x = 0
oldNewDir = ""
oldSourceDir = ""

inicializaceOkna()
obsahOkna()
zviditelneniOkna()
