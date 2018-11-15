import pygame
import Locationpage
import Updatepage
import optionsPage
import filesystem
import tkinter as tk


from tkinter import *
from tkinter.ttk import *
from tkinter import font as tkfont
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


## Create a blank window
homePage = Tk()

# x and y are the coordinates of the upper left corner
w = 600
h = 650
x = 100
y = 100
   
labelfont = ('times', 14, 'bold')

homePage.title("NTU Food Recommendation System")
homePage.resizable(width=False, height=False)
homePage.geometry("%dx%d+%d+%d" % (w, h, x, y))

##Headline
headline = tk.Label(homePage, text="Welcome to NTU Food Recommendation System")
headline.place(x=100, y=0)
headline.config(font=labelfont)

##NTUImage
NTUlogo = PhotoImage(file="resources/NTU_Logo_Partnership.png")
setImage = Label(homePage, image=NTUlogo)
setImage.place(height=150, width=250)
setImage.place(x=150, y=30)

ttk.Separator(homePage).place(x=0, y=180, relwidth=1)

#Menu Bar Method
def popup_Exit():
    answer = messagebox.askyesno("Confirmation", "Do you really want to quit?")
    if answer == True:
       homePage.destroy()


#Menu Bar
locationIcon = PhotoImage(file="resources/map.png")
sortingIcon = PhotoImage(file="resources/sort.png")
updateIcon = PhotoImage(file="resources/update.png")
exitIcon = PhotoImage(file="resources/sign-out-option.png")

menubar = Menu(homePage)
location = Menu(menubar, tearoff=0)
menubar.add_cascade(label=" Location  ", menu=location)
location.add_command(label=" Get My Location", image=locationIcon, compound = LEFT, command=lambda:Locationpage.display_getuserlocation_map(livedata,homePage))
location.add_command(label=" Update Location", image=updateIcon, compound = LEFT, command=lambda:Updatepage.display_getupdatepage(livedata,homePage))
location.add_separator()

sorting = Menu(menubar, tearoff=0)
menubar.add_cascade(label="  Sort  ", menu=sorting)
sorting.add_command(label=" Sort By Rank", image=sortingIcon, compound = LEFT, command=lambda:optionsPage.sort_food_rank_page(livedata, homePage))
sorting.add_command(label=" Sort By Price", image=sortingIcon, compound = LEFT, command=lambda:optionsPage.sort_food_price_page(livedata, homePage))
sorting.add_command(label=" Sort By Location", image=sortingIcon, compound = LEFT, command=lambda:optionsPage.sort_food_location_page(livedata, homePage))
sorting.add_separator()
 
setting = Menu(menubar, tearoff=0)
menubar.add_cascade(label="  Settings  ", menu=setting)
setting.add_command(label="Exit", image=exitIcon, compound = LEFT, command=popup_Exit)
setting.add_separator()

homePage.config(menu=menubar)
    
## define variables
input_sampledata = StringVar()
sampledata = StringVar()

## Constant loop until the 'x' button is pressed
homePage.mainloop()
## Create buttons


