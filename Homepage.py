import pygame
import Locationpage
import Updatepage
import optionsPage
import filesystem

from tkinter import *
from tkinter.ttk import *

from sys import exit

defaultdata = [["Hall 1",100,100,[["Steamed/Roasted Chicken Rice",2.80,4],["Duck Rice",4.00,2.5],["Japanese Fried Chicken Curry Rice",5.00,4.9],["Sambal Spaghett",4.60,4.9],["Grilled Chicken with Satay Sauce",5.80,4.7],["Nasi Lemak",3.50,3.5],["Yong Tau Fu",4.00,4.5],["Mee Siam",2.90,3],["Bak Kut Teh",5.50,4.5],["Roti Prata",2.00,3.6]]]
               ,["Hall 2",300,200,[["Ayam Penyet",4.50,4.3],["Duck Rice",3.20,3.4],["Xiao Long Bao",4.30,5],["Ice Cream Waffles",2.50,4],["Steamed/Roasted Chicken Rice",2.80,5],["Yong Tau Foo",4.00,4],["Green Salad",3.90,4],["Miso Cream Pasta",4.60,3.2],["Black Pepper Chicken",6.00,3.8],["Dry Banmian",3.00,4.1]]]
               ,["Hall 9",250,100,[["Steamed/Roasted Chicken Rice",3.00,3.1],["Ayam Penyet",4.50,4.8],["Beef Hor Fun",4.50,2.8],["Sambal Fish Fillet Rice",4.00,3.2],["Japanese Tonkatsu Original Curry Rice",5.00,4.7],["Tonkatsu Ramen",5.50,4.9],["Mee Siam",3.00,3.8],["Roti Prata",2.00,4.2],["Dry Banmian",3.00,4.6],["Chicken Chop Rice",5.00,4.2]]]
               ,["Hall 11",300,100,[["Ice Cream Waffles",2.30,5],["Ma La Xiang Guo",4.80,4.7],["Bibimbap Beef",3.80,4],["Sambal Spaghett",4.80,4],["Nasi Lemak",3.80,4],["Miso Cream Pasta",4.60,4.2],["Beef Hor Fun",4.50,4],["Green Curry Chicken Rice",5.50,4.7],["Ba Chor Mee",3.00,4.7],["Steamed/Roasted Chicken Rice",2.50,3]]]
               ,["Hall 16",200,200,[["Tonkatsu Ramen",5.00,4.2],["Mee Siam",2.90,3.3],["Bibimbap Beef",3.80,4.3],["Chicken Chop Rice",4.50,4.6],["Hotplate Chicken Fuyong",3.60,4.8],["Carbonara",5.50,3.9],["Ba Chor Mee",2.80,3.9],["Bee Hoon Kway",2.80,3.7],["Fried beef kway teow",5.00,4.8],["Salted Egg Yolk Cereal Chicken Rice",4.80,5]]]
               ,["North Hill",150,200,[["Steamed/Roasted Chicken Rice",2.80,2],["Black Pepper Chicken",6.50,4.3],["Mee Siam",2.90,4],["Roti Prata",2.00,2.7],["Beef Hor Fun",4.50,3.7],["Ba Chor Mee",3.30,3.7],["Hotplate Chicken Fuyong",4.50,4.5],["Prawn paste chicken",9.90,4.8],["Liang Pi + Rou Jia Mou",3.8,4.6],["Duck Rice",3.00,3.6]]]
               ,["Ananda Kitchen",190,275,[["Steamed/Roasted Chicken Rice",2.80,4.1],["Japanese Tonkatsu Original Curry Rice",5.00,4.2],["Miso Cream Pasta",4.60,3],["Beef Hor Fun",4.00,1.6],["Hotplate Chicken Fuyong",4.30,3.8],["Fried beef kway teow",4.5,4.7],["Golden Fish & Chips",12.80,5],["Salted Egg Yolk Cereal Chicken Rice",5.00,4.1],["Prawn Noodles",2.50,4.9],["Western Chicken Katsudon",4.50,4.9]]]
               ,["KouFu @ South Spine",260,195,[["Yong Tau Foo",4.00,5],["Ice Cream Waffles",2.50,3.2],["Steamed/Roasted Chicken Rice",2.50,3],["Green Salad",4.40,3.4],["Green Curry Chicken Rice",4.80,3.1],["Ba Chor Mee",3.30,4.8],["Prawn paste chicken",10.00,3.6],["Bee Hoon Kway",3.30,4],["Prawn Noodles",2.80,3.5],["Tonkatsu Ramen",5.50,4.6]]]
               ,["North Spine",111,175,[["Mee Siam",2.50,3],["Steamed/Roasted Chicken Rice",2.80,3],["Japanese Fried Chicken Curry Rice",5.00,2.3],["Yong Tau Foo",4.70,4.4],["Carbonara",6.00,4.3],["Green Curry Chicken Rice",5.00,4.9],["Ba Chor Mee",2.50,4.3],["Fried beef kway teow",3.60,3.2],["Salted Egg Yolk Cereal Chicken Rice",5.50,4.8],["Liang Pi + Rou Jia Mou",4.00,4.8]]]
               ,["Hall 10",200,250,[["Ke Kou Mian",3.50,4.7],["Bibimbap Beef",4.00,4],["Prawn Noodles",3.00,4.1],["Western Chicken Katsudon",5.50,4.8],["Japanese Tonkatsu Original Curry Rice",4.80,4.5],["Black Pepper Chicken",5.50,4.3],["Yong Tau Foo",4.30,4.1],["Sambal Spaghetti",4.50,4.2],["Ice Cream Waffles",2.50,4.9],["Ma La Xiang Guo",7.00,4.7]]]]

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
