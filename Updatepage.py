from listTableXY import listTableXY
import pygame
import tkinter
from tkinter import messagebox
from sys import exit
import math
import filesystem
def display_getupdatepage(livedata,homePage):
 
        

    updatepage = tkinter.Toplevel(homePage)
    Topframe = tkinter.Frame(updatepage)
    Topframe.pack()
    bottomframe = tkinter.Frame(updatepage)
    bottomframe.pack( side = tkinter.BOTTOM )
  
    listTableXY(Topframe,livedata)
     
    tkinter.Label(bottomframe, text="Canteen Name").grid(row=0)
    tkinter.Label(bottomframe, text="X,Y").grid(row=1)

    e1 = tkinter.Entry(bottomframe)
    e2 = tkinter.Entry(bottomframe)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    update = tkinter.Button(bottomframe, text="Update Data",command=lambda:Update(e1,e2,livedata,updatepage) )
    update.grid(row=1, column=2)
def Update(e1,e2,livedata,updatepage):
    for list1 in range(0,len(livedata)): ##Cycle Through Main list
        hallName = livedata[list1][0]
        if(hallName == e1.get()):
          livedata[list1][1] = e2.get().split(",")[0]
          livedata[list1][2] = e2.get().split(",")[1]

    canteenfile = "resources/canteenlist.csv"
    foodfile = "resources/foodlist.csv"
    filesystem.save_to_csv(livedata,canteenfile,foodfile)
    updatepage.destroy()

