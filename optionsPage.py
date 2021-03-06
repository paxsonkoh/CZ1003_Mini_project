from listTableFood import listTableFood
import pygame
import Locationpage
import filesystem

from tkinter import *
from tkinter.ttk import *

from sys import exit

##def error_page(homePage):
##
##    ## Create a blank window
##    errorPage = Tk()
##    errorPage.title("NTU Food Recommendation System")
##
##    emptyLine1 = Label(errorPage, text=" ")
##    emptyLine1.grid(columnspan=5)
##
##    ## Headline
##    headline = Label(errorPage, text="Please select a valid option!")
##    headline.grid(columnspan=5)
##
##    emptyLine2 = Label(errorPage, text=" ")
##    emptyLine2.grid(columnspan=5)
##
##    ## Constant loop until the 'x' button is pressed
##    homePage.mainloop()

def bubbleSortRank(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j][2] < arr[j+1][2] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubbleSortPrice(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j][3] > arr[j+1][3] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sort_food_by_location(livedata, homePage, hallVariable):
    
    optionsPage = Toplevel()

    optionRanking = []
    foodList=[]

    ##listOfFood = ["Please select from drop down list"]
    ##checkCount = 0

    if (hallVariable != "All" and hallVariable != "Select from List"):
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                if (hallName == hallVariable):
                    for list2 in range(0, len(livedata[list1][3])):   
                        foodName = livedata[list1][3][list2][0]
                        foodPrice = livedata[list1][3][list2][1]
                        foodRating = livedata[list1][3][list2][2]
                        foodList.append(hallName)
                        foodList.append(foodName)
                        foodList.append(foodRating)
                        foodList.append(foodPrice)
                        optionRanking.append(foodList)
                        foodList=[]
        
        listTableFood(optionsPage,optionRanking)

##    elif (hallVariable == "Select from List"):
##        error_page(homePage)

    else:
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                for list2 in range(0, len(livedata[list1][3])):   
                    foodName = livedata[list1][3][list2][0]
                    foodPrice = livedata[list1][3][list2][1]
                    foodRating = livedata[list1][3][list2][2]
                    foodList.append(hallName)
                    foodList.append(foodName)
                    foodList.append(foodRating)
                    foodList.append(foodPrice)
                    optionRanking.append(foodList)
                    foodList=[]
        
        listTableFood(optionsPage,optionRanking)    

def sort_food_by_rank(livedata, homePage, submitVariable):

    optionsPage = Toplevel()

    optionRanking = []
    foodList=[]

    ##listOfFood = ["Please select from drop down list"]
    ##checkCount = 0

    if (submitVariable != "All" and submitVariable != "Select from List"):
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                for list2 in range(0, len(livedata[list1][3])):   
                    foodName = livedata[list1][3][list2][0]
                    foodPrice = livedata[list1][3][list2][1]
                    foodRating = livedata[list1][3][list2][2]
                    if (foodName == submitVariable):
                        foodList.append(hallName)
                        foodList.append(foodName)
                        foodList.append(foodRating)
                        foodList.append(foodPrice)
                        optionRanking.append(foodList)
                        foodList=[]
                            
        bubbleSortRank(optionRanking)
        
        listTableFood(optionsPage,optionRanking)

    else:
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                for list2 in range(0, len(livedata[list1][3])):   
                    foodName = livedata[list1][3][list2][0]
                    foodPrice = livedata[list1][3][list2][1]
                    foodRating = livedata[list1][3][list2][2]
                    foodList.append(hallName)
                    foodList.append(foodName)
                    foodList.append(foodRating)
                    foodList.append(foodPrice)
                    optionRanking.append(foodList)
                    foodList=[]

        bubbleSortRank(optionRanking)
        
        listTableFood(optionsPage,optionRanking)
        
def sort_food_by_price(livedata, homePage, submitVariable, priceVariable):

    optionsPage = Toplevel()

    optionRanking = []
    foodList=[]

    ##listOfFood = ["Please select from drop down list"]
    ##checkCount = 0

    if (submitVariable != "All" and submitVariable != "Select from List" and priceVariable == "All" ):
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                for list2 in range(0, len(livedata[list1][3])):   
                    foodName = livedata[list1][3][list2][0]
                    foodPrice = livedata[list1][3][list2][1]
                    foodRating = livedata[list1][3][list2][2]
                    if (foodName == submitVariable):
                        foodList.append(hallName)
                        foodList.append(foodName)
                        foodList.append(foodRating)
                        foodList.append(foodPrice)
                        optionRanking.append(foodList)
                        foodList=[]
                                
        bubbleSortPrice(optionRanking)
        
        listTableFood(optionsPage,optionRanking)

    elif (submitVariable == "All" and priceVariable != "All" and priceVariable != "Select from Price"):
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                for list2 in range(0, len(livedata[list1][3])):   
                    foodName = livedata[list1][3][list2][0]
                    foodPrice = livedata[list1][3][list2][1]
                    foodRating = livedata[list1][3][list2][2]
                    if (float(foodPrice) < float(priceVariable)):
                        foodList.append(hallName)
                        foodList.append(foodName)
                        foodList.append(foodRating)
                        foodList.append(foodPrice)
                        optionRanking.append(foodList)
                        foodList=[]
                                
        bubbleSortPrice(optionRanking)
        
        listTableFood(optionsPage,optionRanking)

    elif (submitVariable != "All" and priceVariable != "All" and submitVariable != "Select from List" and priceVariable != "Select from Price"):
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                for list2 in range(0, len(livedata[list1][3])):   
                    foodName = livedata[list1][3][list2][0]
                    foodPrice = livedata[list1][3][list2][1]
                    foodRating = livedata[list1][3][list2][2]
                    if (foodName == submitVariable and float(foodPrice) < float(priceVariable)):
                        foodList.append(hallName)
                        foodList.append(foodName)
                        foodList.append(foodRating)
                        foodList.append(foodPrice)
                        optionRanking.append(foodList)
                        foodList=[]
                                
        bubbleSortPrice(optionRanking)
        
        listTableFood(optionsPage,optionRanking)

    elif (submitVariable != "All" and submitVariable != "Select from List" and priceVariable == "Select from Price"):
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                for list2 in range(0, len(livedata[list1][3])):   
                    foodName = livedata[list1][3][list2][0]
                    foodPrice = livedata[list1][3][list2][1]
                    foodRating = livedata[list1][3][list2][2]
                    if (foodName == submitVariable):
                        foodList.append(hallName)
                        foodList.append(foodName)
                        foodList.append(foodRating)
                        foodList.append(foodPrice)
                        optionRanking.append(foodList)
                        foodList=[]
                                
        bubbleSortPrice(optionRanking)
        
        listTableFood(optionsPage,optionRanking)

    elif (priceVariable != "All" and priceVariable != "Select from Price" and submitVariable == "Select from List"):
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
                hallName = livedata[list1][0]
                for list2 in range(0, len(livedata[list1][3])):   
                    foodName = livedata[list1][3][list2][0]
                    foodPrice = livedata[list1][3][list2][1]
                    foodRating = livedata[list1][3][list2][2]
                    if (float(foodPrice) < float(priceVariable)):
                        foodList.append(hallName)
                        foodList.append(foodName)
                        foodList.append(foodRating)
                        foodList.append(foodPrice)
                        optionRanking.append(foodList)
                        foodList=[]
                                
        bubbleSortPrice(optionRanking)
        
        listTableFood(optionsPage,optionRanking)

            
    else:
        for list1 in range(0,len(livedata)): ##Cycle Through Main list
            hallName = livedata[list1][0]
            for list2 in range(0, len(livedata[list1][3])):   
                foodName = livedata[list1][3][list2][0]
                foodPrice = livedata[list1][3][list2][1]
                foodRating = livedata[list1][3][list2][2]
                foodList.append(hallName)
                foodList.append(foodName)
                foodList.append(foodRating)
                foodList.append(foodPrice)
                optionRanking.append(foodList)
                foodList=[]
                                
        bubbleSortPrice(optionRanking)
        
        listTableFood(optionsPage,optionRanking)        

def sort_food_location_page(livedata, homePage):

    hallList = ["Select from List","All"]

    for list1 in range(0,len(livedata)): ##Cycle Through Main list
        hallName = livedata[list1][0]
        hallList.append(hallName) 
    
    ## Create a blank window
    sortFoodPage = Toplevel()
    sortFoodPage.title("NTU Food Recommendation System")

    NTUlogo = PhotoImage(file="resources/NTU_Logo_Partnership.png")
    setImage = Label(sortFoodPage, image=NTUlogo)

    ## Headline
    headline = Label(sortFoodPage, text="Sort Food By Location")
    headline.grid(columnspan=5)

    emptyLine1 = Label(sortFoodPage, text=" ")
    emptyLine1.grid(columnspan=5)

    hallVariable = StringVar(sortFoodPage)
    hallVariable.set(hallList[0])

    hallDropListLabel = Label(sortFoodPage, text="Please Select Hall: ")
    hallDropListLabel.grid(columnspan=5)
    
    hallDropList = OptionMenu(sortFoodPage, hallVariable, *hallList)
    hallDropList.grid(columnspan=5)

    emptyLine2 = Label(sortFoodPage, text=" ")
    emptyLine2.grid(columnspan=5)
    
    hallDropListButton = Button(sortFoodPage, text="Submit", command=lambda:sort_food_by_location(livedata,homePage,hallVariable.get()))
    hallDropListButton.grid(columnspan=5)
    

    setImage.grid(columnspan=5)

    ## Constant loop until the 'x' button is pressed
    homePage.mainloop()        
                        
def sort_food_rank_page(livedata, homePage):

    listOfFood = ["Select from List","All"]
    checkCount = 0

    for list1 in range(0,len(livedata)): ##Cycle Through Main list
            hallName = livedata[list1][0]
            for list2 in range(0, len(livedata[list1][3])):   
                foodName = livedata[list1][3][list2][0]
                for list3 in range(0, len(listOfFood), 1):
                    if (foodName == listOfFood[list3]):
                        checkCount = checkCount + 1
                if (checkCount > 0):
                    checkCount = 0
                else:
                    listOfFood.append(foodName)
    
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

    foodVariable = StringVar(sortFoodPage)
    foodVariable.set(listOfFood[0])

    foodDropListLabel = Label(sortFoodPage, text="Please Select Food Item: ")
    foodDropListLabel.grid(columnspan=5)
    
    foodDropList = OptionMenu(sortFoodPage, foodVariable, *listOfFood)
    foodDropList.grid(columnspan=5)

    emptyLine2 = Label(sortFoodPage, text=" ")
    emptyLine2.grid(columnspan=5)
    
    foodDropListButton = Button(sortFoodPage, text="Submit", command=lambda:sort_food_by_rank(livedata,homePage,foodVariable.get()))
    foodDropListButton.grid(columnspan=5)
    

    setImage.grid(columnspan=5)

    ## Constant loop until the 'x' button is pressed
    homePage.mainloop()

def sort_food_price_page(livedata, homePage):

    listOfFood = ["Select from List","All"]
    priceRange = ["Select from Price","All", 2.00, 3.00, 4.00, 5.00
                  , 6.00, 7.00, 8.00, 9.00, 10.00]
    checkCount = 0

    for list1 in range(0,len(livedata)): ##Cycle Through Main list
            hallName = livedata[list1][0]
            for list2 in range(0, len(livedata[list1][3])):   
                foodName = livedata[list1][3][list2][0]
##                if(len(listOfFood) == 0):
##                    listOfFood.append(foodName)
##                else:
                for list3 in range(0, len(listOfFood), 1):
                    if (foodName == listOfFood[list3]):
                        checkCount = checkCount + 1
                if (checkCount > 0):
                    checkCount = 0
                else:
                    listOfFood.append(foodName)
    
    ## Create a blank window
    sortFoodPage = Toplevel()
    sortFoodPage.title("NTU Food Recommendation System")

    NTUlogo = PhotoImage(file="resources/NTU_Logo_Partnership.png")
    setImage = Label(sortFoodPage, image=NTUlogo)

    ## Headline
    headline = Label(sortFoodPage, text="Sort Food By Price")
    headline.grid(columnspan=5)

    emptyLine1 = Label(sortFoodPage, text=" ")
    emptyLine1.grid(columnspan=5)

    foodVariable = StringVar(sortFoodPage)
    foodVariable.set(listOfFood[0]) ##default value

    foodDropListLabel = Label(sortFoodPage, text="Please Select Food Item: ")
    foodDropListLabel.grid(columnspan=5)
    
    foodDropList = OptionMenu(sortFoodPage, foodVariable, *listOfFood)
    foodDropList.grid(columnspan=5)

    emptyLine2 = Label(sortFoodPage, text=" ")
    emptyLine2.grid(columnspan=5)

    priceVariable = StringVar(sortFoodPage)
    priceVariable.set(priceRange[0]) ##default value

    priceDropListLabel = Label(sortFoodPage, text="Price Range (Below $): ")
    priceDropListLabel.grid(columnspan=5)
    
    priceDropList = OptionMenu(sortFoodPage, priceVariable, *priceRange)
    priceDropList.grid(columnspan=5)

    emptyLine2 = Label(sortFoodPage, text=" ")
    emptyLine2.grid(columnspan=5)

    foodDropListButton = Button(sortFoodPage, text="Submit", command=lambda:sort_food_by_price(livedata,homePage,foodVariable.get(), priceVariable.get()))
                                
    foodDropListButton.grid(columnspan=5)

    setImage.grid(columnspan=5)

    ## Constant loop until the 'x' button is pressed
    homePage.mainloop()
