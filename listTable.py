from tkinter import *
from tkinter.ttk import *

class listTable(Frame,list):

    def __init__(self, parent,livedata):
        Frame.__init__(self, parent)
      
        self.CreateUI()
        self.LoadTable(livedata)
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

    def LoadTable(self,livedata):
        ## self.treeview.insert('', 'end', text="Hall 1", values=('Chicken Rice',
        ##                     '3.5', '4'))
        ## self.treeview.insert('', 'end', text="Hall 1", values=('Roasted Delight',
        ##                     '4', '5'))
        ## self.treeview.insert('', 'end', text="Hall 2", values=('Muslim Food',
        ##                     '3.5', '4'))

        for list1 in range(0,len(livedata)): ##Cycle Through Main list
            hallName = livedata[list1][0]
            for list2 in range(0, len(livedata[list1][3])):   
                foodName = livedata[list1][3][list2][0]
                foodRating = livedata[list1][3][list2][1]
                foodPrice = livedata[list1][3][list2][2]
                self.treeview.insert('', 'end', text=hallName, values=(foodName,foodRating,foodPrice))
