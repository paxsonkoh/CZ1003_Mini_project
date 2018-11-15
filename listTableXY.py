from tkinter import *
from tkinter.ttk import *
##from tkinter import PhotoImage.
class listTableXY(Frame,list):

    def __init__(self, page,livedata):
        Frame.__init__(self,page)
        self.root =page
        self.CreateUI()
        self.LoadTable(livedata)
        self.grid(sticky = (N,S,W,E))
        page.grid_rowconfigure(0, weight = 1)
        page.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self.root)
        tv['columns'] = ('X condinate', 'Y condinate')
        tv.heading("#0", text='Location', anchor='w')
        tv.column("#0", anchor="w")
       ## tv.heading('foodName', text='food Name')
       ## tv.column('foodName', anchor='center', width=100)
       ## tv.heading('foodPrice', text='Price ($)')
       ## tv.column('foodPrice', anchor='center', width=100)
       ## tv.heading('foodRating', text='Rating(0-5)')
       ## tv.column('foodRating', anchor='center', width=100)
        tv.heading('X condinate', text='X condinate')
        tv.column('X condinate', anchor='center', width=100)
        tv.heading('Y condinate', text='Y condinate')
        tv.column('Y condinate', anchor='center', width=100)
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
##            self._img = PhotoImage(file="resources\information_picto.gif")
##            for list2 in range(0, len(livedata[list1][3])):   
##                foodName = livedata[list1][3][list2][0]
##                foodRating = livedata[list1][3][list2][1]
##                foodPrice = livedata[list1][3][list2][2]
            self.treeview.insert('', 'end', text=hallName, values=(livedata[list1][1],livedata[list1][2]))
    def onDoubleClick(self, event):
    # close previous popups
        self.destroyPopups()

    # what row and column was clicked on
        rowid = self._tree.identify_row(event.y)
        column = self._tree.identify_column(event.x)

    # clicked row parent id
        parent = self._tree.parent(rowid)

    # do nothing if item is top-level        
        if parent == '':
            return

    # get column position info
        x,y,width,height = self._tree.bbox(rowid, column)

    # y-axis offset
        pady = height // 2

    # place Entry popup properly         
        url = self._tree.item(rowid, 'text')
        self.entryPopup = EntryPopup(self._tree, url)
        self.entryPopup.place( x=0, y=y+pady, anchor=W, relwidth=1)
