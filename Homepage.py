import pygame
import Locationpage
import filesystem

from tkinter import *
from tkinter.ttk import *

from sys import exit

pygame.init()

defaultdata = [["hall 1",100,100,[["chicken rice",1,1],["duck rice",2,2]]],["hall 2",200,200,[["chicken rice",2,2],["duck rice",1,1]]]]
canteenfile = "canteenlist.csv"
foodfile = "foodlist.csv"

class listTable(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('foodName', 'foodPrice', 'foodRating')
        tv.heading("#0", text='Sources', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('foodName', text='Food Name')
        tv.column('foodName', anchor='center', width=100)
        tv.heading('foodPrice', text='Price ($)')
        tv.column('foodPrice', anchor='center', width=100)
        tv.heading('foodRating', text='Rating(0-5)')
        tv.column('foodRating', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        ## self.treeview.insert('', 'end', text="Hall 1", values=('Chicken Rice',
        ##                     '3.5', '4'))
        ## self.treeview.insert('', 'end', text="Hall 1", values=('Roasted Delight',
        ##                     '4', '5'))
        ## self.treeview.insert('', 'end', text="Hall 2", values=('Muslim Food',
        ##                     '3.5', '4'))

        for list1 in range(0,len(defaultdata)): ##Cycle Through Main list
            hallName = defaultdata[list1][0]
            for list2 in range(0, len(defaultdata[list1][3])):   
                foodName = defaultdata[list1][3][list2][0]
                foodRating = defaultdata[list1][3][list2][1]
                foodPrice = defaultdata[list1][3][list2][2]
                self.treeview.insert('', 'end', text=hallName, values=(foodName,foodRating,foodPrice))

#len(defaultdata[list1][list2])
                        
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

livedata = filesystem.load_to_list(canteenfile,foodfile)
if livedata ==False:
    filesystem.save_to_csv(defaultdata,canteenfile,foodfile)
    livedata = filesystem.load_to_list(canteenfile,foodfile)

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

listTable(homePage).grid(columnspan=5)

setImage.grid(columnspan=5)

## Constant loop until the 'x' button is pressed
homePage.mainloop()
