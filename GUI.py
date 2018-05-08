from tkinter import *
import Start


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

    Ch1 = Checkbutton(okno, text="  Copy                               ", variable=ch1)
    Ch1.grid(row=0, column=2)

    Ch2 = Checkbutton(okno, text="  Sort  (Jpg and Raw)       ", variable=ch2)
    Ch2.grid(row=2, column=2)

    Ch3 = Checkbutton(okno, text="  Fix (Only SD Cart)          ", variable=ch3)
    Ch3.grid(row=3, column=2)

    Ch4 = Checkbutton(okno, text="  Rename RAW                 ", variable=ch4)
    Ch4.grid(row=4, column=2)

    Ch5 = Checkbutton(okno, text="  Rename JPG                   ", variable=ch5)
    Ch5.grid(row=5, column=2)




def zviditelneniOkna():
    okno.mainloop()


def run():
    copy = ch1.get()
    sort = ch2.get()
    fixImage = ch3.get()
    renameRaw = ch4.get()
    renameJpg = ch5.get()

    newDir = Dir.get()
    sourceDir = src.get()


    print(copy, sort, fixImage, renameRaw, renameJpg, newDir, sourceDir)
    done=Start.start(copy, sort, fixImage, renameRaw, renameJpg, newDir, sourceDir)

    x = "PROCES DONE!!!"
    L3 = Label(okno, text=x)
    L3.grid(row=4, column=1)




#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
okno = Tk()
ch1 = IntVar()
ch2 = IntVar()
ch3 = IntVar()
ch4 = IntVar()
ch5 = IntVar()
src = StringVar()
Dir = StringVar()

global done
done=0

inicializaceOkna()
obsahOkna()
zviditelneniOkna()
