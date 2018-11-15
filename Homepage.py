import pygame
import Locationpage
import Updatepage
import optionsPage
import filesystem

from tkinter import *
from tkinter.ttk import *

from sys import exit

defaultdata = [["Hall 1",100,100,[["Chicken Rice",3.50,4.3],["Duck Rice",4.00,3.5],["Yong Tau Fu",4.00,4.5],["Nasi Lemak",3.50,3.5]]]
               ,["Hall 2",300,200,[["Chicken Rice",4.50,3.3],["Duck Rice",3.80,4.9],["Roti Prata",2.00,3.6]]]
               ,["Hall 3",200,350,[["Chicken Rice",3.00,3.8],["Roasted Pork Rice",3.00,4.0],["Double Boiled Soup of The Day",4.50,4.0],["Yong Tau Fu",4.00,3.6],["Chicken Chop",5.50,4.0]]]
               ,["Hall 4",278,150,[["Chicken Rice",2.80,3.1],["Duck Rice",4.00,4.2],["Nasi Lemak",4.00,3.3]]]
               ,["Binjai",126,234,[["Chicken Rice",3.00,2.9],["Fish & Chips",6.50,3.9]]]
               ,["Pioneer",200,200,[["Chicken Rice",4.00,4.5],["Duck Rice",4.00,2.9],["Mala",7.00,4.6],["Bak Kut Teh",5.50,4.9]]]]

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
headline.grid(columnspan=5)

## define variables
input_sampledata = StringVar()
sampledata = StringVar()

## Create buttons

myLocation = Button(homePage, text="Get My Location", command=lambda:Locationpage.display_getuserlocation_map(livedata,homePage))

sortByLocation = Button(homePage, text="Sort Food by Location", command=lambda:optionsPage.sort_food_location_page(livedata, homePage))

sortByRank = Button(homePage, text="Sort Food by Rank", command=lambda:optionsPage.sort_food_rank_page(livedata, homePage))

sortByPrice = Button(homePage, text="Sort Food by Price", command=lambda:optionsPage.sort_food_price_page(livedata, homePage))

updateData = Button(homePage, text="Update Location",command=lambda:Updatepage.display_getupdatepage(livedata,homePage))

myLocation.grid(row=1, column=0)
sortByLocation.grid(row=1, column=1)
sortByRank.grid(row=1, column=2)
sortByPrice.grid(row=1, column=3)
updateData.grid(row=1, column=4)



setImage.grid(columnspan=5)

## Constant loop until the 'x' button is pressed
homePage.mainloop()
