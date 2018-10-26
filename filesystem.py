
from pathlib import Path



import csv
def save_to_csv(res,canteenfile,foodfile):
    

    canteenlist,foodlist = open(canteenfile, 'w',newline=''),open(foodfile, 'w',newline='')
    with canteenlist,foodlist:
        writer,writer2 = csv.writer(canteenlist),csv.writer(foodlist)

        for row in res:
            fooddata =row.pop()
            for row2 in fooddata:
                row2.insert(0,row[0])
                writer2.writerow(row2)
            writer.writerow(row)
def load_to_list(canteenfile,foodfile):
    datalist = list()
    my_file_1 = Path(canteenfile)
    my_file_2 = Path(foodfile)
    if my_file_1.is_file() == False and my_file_2.is_file() == False :
        return False
    canteenlist = open(canteenfile, 'r')
    foodlist = open(foodfile, 'r')
    
    
    with canteenlist,foodlist:

        reader,reader2,counter  = csv.reader(canteenlist),csv.reader(foodlist),0
        reader2list = list(reader2)
        for row in reader:
            foodrowlist= list()
            while True:


                if len(reader2list)==counter or reader2list[counter][0] != row[0]:
                    row.append(foodrowlist)
                    break
                foodrowlist.append(reader2list[counter][1:])
                counter+= 1
            datalist.append(row)
    return datalist
	    
        




