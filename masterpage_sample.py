import tkinter
import pygame
import filesystem
from sys import exit
from tkinter import messagebox
defaultdata = [["hall 1",100,100,[["chicken rice",1,1],["duck rice",2,2]]],["hall 2",100,100,[["chicken rice",2,2],["duck rice",1,1]]]]
canteenfile = "canteenlist.csv"
foodfile = "foodlist.csv"

livedata = filesystem.load_to_list(canteenfile,foodfile)
if livedata ==False:
    print("file not in floder")
    filesystem.save_to_csv(defaultdata,canteenfile,foodfile)
    livedata = filesystem.load_to_list(canteenfile,foodfile)

masterpage = tkinter.Tk()
def display_getuserlocation_map():
 introScreenImage = pygame.image.load("NTUMAP.png")
 screen = pygame.display.set_mode((660,465))
 screen.blit(introScreenImage,(0,0))
 myfont = pygame.font.SysFont("monospace", 10)

# render text
 label = myfont.render("Some text!", 1, (0,0,0))
 temp_surface = pygame.Surface(label.get_size())
 temp_surface.fill((192, 192, 192))
 temp_surface.blit(label, (0, 0))
 pygame.draw.circle(screen, (0,0,255), (100, 100), 5)
 screen.blit(temp_surface, (100-30, 100-20))
 pygame.display.flip()
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
     pygame.quit()
   elif event.type == pygame.MOUSEBUTTONUP:
     messagebox.showinfo("User Location","mouse at (%d, %d)"%event.pos)
     pygame.quit()
	 

def sample_page_button():
  
    sampledata.set(input_sampledata.get())

def sample_page_with_button():
    
    samplewindow =tkinter.Toplevel()
    topframe = tkinter.Frame(samplewindow)
    topframe.pack( side = tkinter.TOP )
    bottomframe = tkinter.Frame(samplewindow)
    bottomframe.pack( side = tkinter.BOTTOM )
    L1 = tkinter.Label(samplewindow, text="Sample date input")
    L1.pack( side = tkinter.LEFT)
    E1 = tkinter.Entry(samplewindow, bd =5 ,textvariable=input_sampledata)
    E1.pack(side = tkinter.LEFT)
    B3 = tkinter.Button(bottomframe, text ="Send output", command = sample_page_button)
    B3.pack( side = tkinter.BOTTOM)
    L2 = tkinter.Label(bottomframe,text= "",textvariable=sampledata)
    L2.pack( side = tkinter.BOTTOM)


input_sampledata = tkinter.StringVar()
sampledata = tkinter.StringVar()
pygame.init()
MasterLabel = tkinter.Label(masterpage, text="Welcome to Food NTU")
B1 = tkinter.Button(masterpage, text ="User Location", command =display_getuserlocation_map)
B2 = tkinter.Button(masterpage, text ="Sample Page", command =sample_page_with_button)
MasterLabel.pack()
B1.pack()
B2.pack()
masterpage.mainloop()
