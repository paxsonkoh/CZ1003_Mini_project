import pygame
import Locationpage
import Updatepage
import optionsPage
import filesystem

from tkinter import *
from tkinter.ttk import *

from sys import exit

defaultdata = [["hall 1",100,100,[["chicken rice",1,1],["duck rice",2,2]]],["hall 2",200,200,[["chicken rice",2,2],["duck rice",1,1]]]]
canteenfile = "resources/canteenlist.csv"
foodfile = "resources/foodlist.csv"

livedata = filesystem.load_to_list(canteenfile,foodfile)
if livedata ==False:
    filesystem.save_to_csv(defaultdata,canteenfile,foodfile)
    livedata = filesystem.load_to_list(canteenfile,foodfile)

##print(livedata)
##len(defaultdata[list1][list2])
                        
##def sample_page_button():
##  
##    sampledata.set(input_sampledata.get())
##
##def sample_page_with_button():
##    
##    samplewindow = Toplevel()
##
##    headline = Label(samplewindow, text="Sample Page")
##    headline.grid(columnspan=2)
##    
##    L1 = Label(samplewindow, text="Sample date input")
##    L1.grid(row=1, column=0)
##    
##    E1 = Entry(samplewindow, bd =5 ,textvariable=input_sampledata)
##    E1.grid(row=1, column=1)
##    
##    B3 = Button(samplewindow, text ="Send output", command = sample_page_button)
##    B3.grid(columnspan=2)
##    
##    L2 = Label(samplewindow,text= "",textvariable=sampledata)
##    L2.grid(columnspan=2)


## Create a blank window
homePage = Tk()
homePage.title("NTU Food Recommendation System")

## Create the top frame
##topFrame = Frame(homePage)
##topFrame.pack()

## Create the bottom frame
##bottomFrame = Frame(homePage)
##bottomFrame.pack()

NTUlogo = PhotoImage(file="resources/NTU_Logo_Partnership.png")
setImage = Label(homePage, image=NTUlogo)

## Headline
headline = Label(homePage, text="Welcome to NTU Food Recommendation System")
headline.grid(columnspan=4)

## define variables
input_sampledata = StringVar()
sampledata = StringVar()

## Create buttons

myLocation = Button(homePage, text="Get My Location", command=lambda:Locationpage.display_getuserlocation_map(livedata,homePage))

updateData = Button(homePage, text="Update Location",command=lambda:Updatepage.display_getupdatepage(livedata,homePage) )

sortByRank = Button(homePage, text="Sort Food by Rank", command=lambda:optionsPage.sort_food_rank_page(livedata, homePage))

sortByPrice = Button(homePage, text="Sort Food by Price", command=lambda:optionsPage.sort_food_price_page(livedata, homePage))

myLocation.grid(row=1, column=0)
sortByRank.grid(row=1, column=1)
sortByPrice.grid(row=1, column=2)
updateData.grid(row=1, column=3)



setImage.grid(columnspan=4)

## Constant loop until the 'x' button is pressed
homePage.mainloop()
