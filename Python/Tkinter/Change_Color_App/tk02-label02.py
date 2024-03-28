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
labelTitle.place(relx=0,rely=0,anchor=NW)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.place(relx=0,rely=0.5,anchor=W)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.place(relx=0,rely=1,anchor=SW)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.place(relx=0.5,rely=0,anchor=N)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.place(relx=1,rely=0,anchor=NE)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.place(relx=1,rely=0.5,anchor=E)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.place(relx=1,rely=1,anchor=SE)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.place(relx=0.5,rely=1,anchor=S)

labelTitle=Label(cuaso,text="Hello",font=('System',20),bg=BLACK,fg=WHITE,padx=10,pady=5)
labelTitle.place(relx=0.5,rely=0.5,anchor=CENTER)

cuaso.mainloop()