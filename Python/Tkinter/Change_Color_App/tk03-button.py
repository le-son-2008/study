from cProfile import label
from tkinter import *
from tkinter import font
from turtle import left
from define import *

from app import App

cuaso = Tk()

App(cuaso)

#Button
def show_hello():
    print("Hello")
def show_name(name):
    print("Name:"+name)
btHello = Button(cuaso,text="Hello",font='Termiral',padx=20,pady=20,bg=YELLOW,activebackground=RED,fg=BLUE,activeforeground=WHITE,command=show_hello)
btHello.grid(row=0,column=0)

btPython = Button(cuaso,text="Python",font='Termiral',padx=20,pady=20,bg=YELLOW,activebackground=RED,fg=BLUE,activeforeground=WHITE,command=lambda:show_name('Python')) # type: ignore
btPython.grid(row=0,column=1)

btTkinter = Button(cuaso,text="Tkinter",font='Termiral',padx=20,pady=20,bg=YELLOW,activebackground=RED,fg=BLUE,activeforeground=WHITE,command=lambda:show_name('Tkinter')) # type: ignore
btTkinter.grid(row=0,column=2)

cuaso.rowconfigure(0,weight=1)
cuaso.columnconfigure(0,weight=1)
cuaso.columnconfigure(1,weight=1)
cuaso.columnconfigure(2,weight=1)

cuaso.mainloop()