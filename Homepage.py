import pygame
import Locationpage
import filesystem
from tkinter import *
from sys import exit

defaultdata = [["hall 1",100,100,[["chicken rice",1,1],["duck rice",2,2]]],["hall 2",200,200,[["chicken rice",2,2],["duck rice",1,1]]]]
canteenfile = "canteenlist.csv"
foodfile = "foodlist.csv"

livedata = filesystem.load_to_list(canteenfile,foodfile)
if livedata ==False:
    filesystem.save_to_csv(defaultdata,canteenfile,foodfile)
    livedata = filesystem.load_to_list(canteenfile,foodfile)

def sample_page_button():
  
    sampledata.set(input_sampledata.get())

def sample_page_with_button():
    
    samplewindow = Tk()

    headline = Label(samplewindow, text="Sample Page")
    headline.grid(columnspan=2)
    
    L1 = Label(samplewindow, text="Sample date input")
    L1.grid(row=1, column=0)
    
    E1 = Entry(samplewindow, bd =5 ,textvariable=input_sampledata)
    E1.grid(row=1, column=1)
    
    B3 = Button(samplewindow, text ="Send output", command = sample_page_button)
    B3.grid(columnspan=2)
    
    L2 = Label(samplewindow,text= "",textvariable=sampledata)
    L2.grid(columnspan=2)

## Create a blank window
homePage = Tk()
homePage.title("NTU Food Recommendation System")

## Create the top frame
##topFrame = Frame(homePage)
##topFrame.pack()

## Create the bottom frame
##bottomFrame = Frame(homePage)
##bottomFrame.pack()

NTUlogo = PhotoImage(file="NTU_Logo_Partnership.png")
setImage = Label(homePage, image=NTUlogo)

## Headline
headline = Label(homePage, text="Welcome to NTU Food Recommendation System")
headline.grid(columnspan=5)

## define variables
input_sampledata = StringVar()
sampledata = StringVar()

## Create buttons

myLocation = Button(homePage, text="Get My Location", command=lambda:Locationpage.display_getuserlocation_map(livedata))
distToDest = Button(homePage, text="Distance to Destination")
sortByLocation = Button(homePage, text="Sort Food by Location")
sortByRank = Button(homePage, text="Sort Food by Rank")
samplePage = Button(homePage, text="Sample Page", command=sample_page_with_button)

myLocation.grid(row=1, column=0)
distToDest.grid(row=1, column=1)
sortByLocation.grid(row=1, column=2)
sortByRank.grid(row=1, column=3)
samplePage.grid(row=1, column=4)
setImage.grid(columnspan=5)

## Constant loop until the 'x' button is pressed
homePage.mainloop()
