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
labelTitle=Label(cuaso,text="Hello",font=('System',44),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.pack(side=TOP,anchor=NW)

labelTitle_=Label(cuaso,text="Hello",font=('System',44),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle_.pack(side=BOTTOM,anchor=SE)

cuaso.mainloop()