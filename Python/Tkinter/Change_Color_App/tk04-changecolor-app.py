from cProfile import label
from gettext import ngettext
from operator import index
from os import name
from tkinter import *
from tkinter import font
from turtle import back, left
from define import *

from app import App

cuaso = Tk()

App(cuaso)

def change_color_label(color):
  labelMain['bg']=color

def button(name,background,index): 
  Button(cuaso,text=name,font=("System",20),bg=background,fg=BLACK,padx=20,pady=20,width=8,command=lambda:change_color_label(background)).grid(row=1,column=index,sticky=W+E,padx=30)

labelMain=Label(cuaso,text="Hello",font=("System",40),bg=WHITE,fg=BLACK,padx=30,pady=20)
labelMain.grid(row=0,columnspan=4,sticky=W+E,padx=30)

button("Lime",LIME,0)
button("Red",RED,1)
button("Blue",BLUE,2)
button("Yellow",YELLOW,3)

cuaso.columnconfigure(0,weight=1)
cuaso.columnconfigure(1,weight=1)
cuaso.columnconfigure(2,weight=1)
cuaso.columnconfigure(3,weight=1)
cuaso.rowconfigure(0,weight=1)
cuaso.rowconfigure(1,weight=1)

cuaso.mainloop()