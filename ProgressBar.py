from ttk import Progressbar
from tkinter import *

import cleanData


def progressBar():
    okno2.geometry("300x45")
    okno2.title("PROGRESS")

    okno2.update_idletasks()
    w = okno2.winfo_screenwidth()
    h = okno2.winfo_screenheight()
    size = tuple(int(_) for _ in okno2.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    okno2.geometry("%dx%d+%d+%d" % (size + (x, y)))

    progress = Progressbar(okno2, orient=HORIZONTAL, length=300, mode='determinate')
    progress.grid(row=0, column=0)
    L1 = Label(okno2, text="Loading...")
    L1.grid(row=1, column=0)

def refreshProgressBar(val,val1):
    progress = Progressbar(okno2, orient=HORIZONTAL, length=300, mode='determinate')
    progress.grid(row=0, column=0)
    progress['value'] = val
    L1 = Label(okno2, text="                                           ")
    L1.grid(row=1, column=0)
    L1 = Label(okno2, text=val1)
    L1.grid(row=1, column=0)
    okno2.update_idletasks()

def killProgressBar():
    sys.exit()

def run():
    global okno2
    okno2 = Tk()
    progressBar()
    okno2.update()
    x1 = getVal1()
    while (x1!="END"):
        x = getVal()
        x1 = getVal1()
        x2 = x.split(".")
        x3=['']

        if(x2 != x3):
            refreshProgressBar(int(x2[0]),x1)
    refreshProgressBar(100, x1)
    killProgressBar()

def getVal():
    f = open("Progress.txt", "r")
    soubor = f.read()
    f.close()
    return soubor


def getVal1():
    f = open("Progress1.txt", "r")
    soubor = f.read()
    f.close()
    return soubor