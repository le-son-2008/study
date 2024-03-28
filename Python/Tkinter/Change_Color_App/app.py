from define import *
from tkinter import *

class App():
    def __init__(self,cuaso) -> None:
        #Title
        cuaso.title("TEST")
        #Background
        cuaso['bg']="gray"
        #WIDTH HEIGHT POSITION
        cuaso.geometry("{}x{}+{}+{}".format(CHIEU_RONG,CHIEU_CAO,CACH_HOANH,CACH_TUNG))
        #Icon
        photo=PhotoImage(file=ICON)
        cuaso.iconphoto(False,photo)
        #Resizeable
        #cuaso.resizable(False,False)
        #Min resize
        cuaso.minsize(600,100)