from listTableXY import listTableXY
import pygame
import tkinter
from tkinter import messagebox
from sys import exit
import math
import filesystem

from tkinter import *
from tkinter.ttk import *

def display_getupdatepage(livedata,homePage):
 
        

    updatepage = tkinter.Toplevel(homePage)
    Topframe = tkinter.Frame(updatepage)
    Topframe.pack()
    bottomframe = tkinter.Frame(updatepage)
    bottomframe.pack( side = tkinter.BOTTOM )

    hallList = ["Select from List"]

    for list1 in range(0, len(livedata)):
        hallName = livedata[list1][0]
        hallList.append(hallName) 
  
    listTableXY(Topframe,livedata)

    listVariable = StringVar(updatepage)
    listVariable.set(hallList[0]) ##default value
    
    tkinter.Label(bottomframe, text="Canteen Name: ").grid(row=0)
    tkinter.Label(bottomframe, text="X,Y: ").grid(row=1)

    e1 = OptionMenu(bottomframe, listVariable, *hallList) ## Hall Name
    e2 = tkinter.Entry(bottomframe) ## X, Y

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    update = tkinter.Button(bottomframe, text="Update",command=lambda:Update(listVariable.get(),e2,livedata,Topframe,updatepage,update,bottomframe) )
    update.grid(row=1, column=2)

def Update(hallSelection,e2,livedata,Topframe,updatepage,update,bottomframe):
    for list1 in range(0,len(livedata)): ##Cycle Through Main list
        hallName = livedata[list1][0]
        if(hallName == hallSelection):
          livedata[list1][1] = e2.get().split(",")[0]
          livedata[list1][2] = e2.get().split(",")[1]

    canteenfile = "resources/canteenlist.csv"
    foodfile = "resources/foodlist.csv"
    filesystem.save_to_csv(livedata,canteenfile,foodfile)
    livedata = filesystem.load_to_list(canteenfile,foodfile)
    Topframe.destroy()
    Topframe = tkinter.Frame(updatepage)
    Topframe.pack()
    tkinter.messagebox.showinfo("Update Complete", "Application will close please reopen")
    updatepage.quit()
 
