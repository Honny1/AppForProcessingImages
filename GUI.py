from tkinter import *


def inicializaceOkna():
    okno.title("App")
    okno.geometry("325x200+400+100")


def obsahOkna():
    L1 = Label(okno, text="SD Cart dir:")
    L1.grid(row=0, column=0)

    global E1, E2, ch1, ch2, ch3, ch4
    E1 = Entry(okno, textvariable=src, width=20)
    E1.grid(row=0, column=1)

    L2 = Label(okno, text="New dir:")
    L2.grid(row=2, column=0)

    E2 = Entry(okno, textvariable=Dir, width=20)
    E2.grid(row=2, column=1)

    B1 = Button(okno, text="RUN", bg="yellow", command=run)
    B1.grid(row=3, column=0)

    Ch1 = Checkbutton(okno, text="  Copy and Sort               ", variable=ch1)
    Ch1.grid(row=0, column=2)

    Ch1 = Checkbutton(okno, text="  Fix (Only SD Cart)         ", variable=ch2)
    Ch1.grid(row=2, column=2)

    Ch1 = Checkbutton(okno, text="  Rename RAW                ", variable=ch3)
    Ch1.grid(row=3, column=2)

    Ch1 = Checkbutton(okno, text="  Rename JPG                  ", variable=ch4)
    Ch1.grid(row=4, column=2)


def zviditelneniOkna():
    okno.mainloop()


def run():
    copyAndSort = ch1.get()
    fixImage = ch2.get()
    renameRaw = ch3.get()
    renameJpg = ch4.get()

    newDir = Dir.get()
    sourceDir = src.get()

    print(copyAndSort, fixImage, renameRaw, renameJpg, newDir, sourceDir)


#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
okno = Tk()
ch1 = IntVar()
ch2 = IntVar()
ch3 = IntVar()
ch4 = IntVar()
src = StringVar()
Dir = StringVar()

inicializaceOkna()
obsahOkna()
zviditelneniOkna()
