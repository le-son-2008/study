from tkinter import *
from define import *

cuaso = Tk()

def setup_window():
    #Title
    cuaso.title("LE THANH SON")

    #Background
    cuaso['bg']='#EFC9AF'

    #WIDTH HEIGHT POSITION
    cuaso.geometry("{}x{}+{}+{}".format(CHIEU_RONG,CHIEU_CAO,CACH_HOANH,CACH_TUNG))

    #Icon
    '''photo=PhotoImage(file=FILE)
    cuaso.iconphoto(False,photo)'''

    #Resizeable
    cuaso.resizable(False,False)
    
    #Label
    label=Label(cuaso,text="HELLO",fg="#000000",bg="#FFFFFF").pack()

setup_window()

cuaso.mainloop()