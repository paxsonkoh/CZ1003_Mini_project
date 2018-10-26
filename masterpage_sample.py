import tkinter
import pygame
from sys import exit
from tkinter import messagebox

masterpage = tkinter.Tk()
def display_getuserlocation_map():
 introScreenImage = pygame.image.load("NTUMAP.png")
 screen = pygame.display.set_mode((660,465))
 screen.blit(introScreenImage,(0,0))
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
pygame.init()
input_sampledata = tkinter.StringVar()
sampledata = tkinter.StringVar()

B1 = tkinter.Button(masterpage, text ="User Location", command = display_getuserlocation_map)
B2 = tkinter.Button(masterpage, text ="Sample Page", command = sample_page_with_button)

B1.pack()
B2.pack()
masterpage.mainloop()
