from cProfile import label
from tkinter import *
from tkinter import font
from turtle import left
from define import *

from app import App

cuaso = Tk()

App(cuaso)

print(font.families())
#Label
labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.grid(row=0,column=0,sticky=NW)

labelTitle=Label(cuaso,text="Hell0",font=('System',20),bg=WHITE,fg=BLACK,padx=10,pady=5)
labelTitle.grid(row=0,column=1,sticky=SW)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.grid(row=0,column=2,sticky=NE)

cuaso.columnconfigure(0,weight=1)
cuaso.columnconfigure(1,weight=1)
cuaso.columnconfigure(2,weight=1)

cuaso.rowconfigure(0,weight=1)

cuaso.mainloop()