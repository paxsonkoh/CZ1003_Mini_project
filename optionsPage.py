import pygame
import Locationpage
import filesystem

from tkinter import *
from tkinter.ttk import *

from sys import exit
                        
def sort_food_options_page(livedata, homePage):

    listOfFood = ["Please select from drop down list"]
    checkCount = 0

    for list1 in range(0,len(livedata)): ##Cycle Through Main list
            hallName = livedata[list1][0]
            for list2 in range(0, len(livedata[list1][3])):   
                foodName = livedata[list1][3][list2][0]
                if(len(listOfFood) == 0):
                    print("The length of the list is: " + str(len(listOfFood)))
                    listOfFood.append(foodName)
                else:
                    for list3 in range(0, len(listOfFood), 1):
                        if (foodName == listOfFood[list3]):
                            checkCount = checkCount + 1
                    if (checkCount > 0):
                        checkCount = 0
                    else:
                        listOfFood.append(foodName)
                
    print(listOfFood)
    
    ## Create a blank window
    sortFoodPage = Toplevel()
    sortFoodPage.title("NTU Food Recommendation System")

    NTUlogo = PhotoImage(file="resources/NTU_Logo_Partnership.png")
    setImage = Label(sortFoodPage, image=NTUlogo)

    ## Headline
    headline = Label(sortFoodPage, text="Sort Food By Rank")
    headline.grid(columnspan=5)

    emptyLine1 = Label(sortFoodPage, text=" ")
    emptyLine1.grid(columnspan=5)

    ## define variables
    #input_sampledata = StringVar()
    #sampledata = StringVar()

    ## Create buttons

    #myLocation = Button(sortFoodPage, text="Get My Location", command=lambda:Locationpage.display_getuserlocation_map(livedata,homePage))
    #distToDest = Button(sortFoodPage, text="Distance to Destination")
    #sortByLocation = Button(sortFoodPage, text="Sort Food by Location")
    #sortByRank = Button(sortFoodPage, text="Sort Food by Rank")
    #samplePage = Button(sortFoodPage, text="Sample Page", command=sample_page_with_button)

    #myLocation.grid(row=1, column=0)
    #distToDest.grid(row=1, column=1)
    #sortByLocation.grid(row=1, column=2)
    #sortByRank.grid(row=1, column=3)
    #samplePage.grid(row=1, column=4)

    foodVariable = StringVar(sortFoodPage)
    foodVariable.set(listOfFood[0])

    def ok():
        print ("value is:" + foodVariable.get())

    foodDropListLabel = Label(sortFoodPage, text="Please Select Food Item: ")
    foodDropListLabel.grid(columnspan=5)
    
    foodDropList = OptionMenu(sortFoodPage, foodVariable, *listOfFood)
    foodDropList.grid(columnspan=5)

    emptyLine2 = Label(sortFoodPage, text=" ")
    emptyLine2.grid(columnspan=5)
    
    foodDropListButton = Button(sortFoodPage, text="Submit", command=lambda:Locationpage.display_getuserlocation_map(livedata,homePage))
    foodDropListButton.grid(columnspan=5)
    

    setImage.grid(columnspan=5)

    ## Constant loop until the 'x' button is pressed
    homePage.mainloop()
