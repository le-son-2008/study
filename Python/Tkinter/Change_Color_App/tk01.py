from tkinter import *
from define import *

cuaso = Tk()

def setup_window():
    #Title
    cuaso.title("TEST")

    #Background
    cuaso['bg']="lime"

    #WIDTH HEIGHT POSITION
    cuaso.geometry("{}x{}+{}+{}".format(CHIEU_RONG,CHIEU_CAO,CACH_HOANH,CACH_TUNG))

    #Icon
    photo=PhotoImage(file=ICON)
    cuaso.iconphoto(False,photo)

    #Resizeable
    cuaso.resizable(False,False)


setup_window()

cuaso.mainloop()