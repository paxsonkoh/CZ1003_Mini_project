from listTableXY import listTableXY
import pygame
import tkinter
from tkinter import messagebox
from sys import exit
import math

def display_getuserlocation_map(livedata,homePage):
 pygame.init()
 pygame.display.set_caption('Get Canteen Based on Location')
 introScreenImage = pygame.image.load("resources/NTUMAP.png")
 screen = pygame.display.set_mode((660,465))
 screen.blit(introScreenImage,(0,0))
 myfont = pygame.font.SysFont("monospace", 13)

# render text
 
 for row in livedata:
  label = myfont.render(row[0], 1, (0,0,0))
  temp_surface = pygame.Surface(label.get_size())
  temp_surface.fill((255, 0, 0))
  temp_surface.blit(label, (0, 0))
  pygame.draw.circle(screen, (0,0,255), (int(row[1]), int(row[2])), 5)
  screen.blit(temp_surface, (int(row[1])-30, int(row[2])-20))
 pygame.display.flip()
 loop =True
 while loop:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
     pygame.quit()
   elif event.type == pygame.MOUSEBUTTONUP:
        
     livedata = sort_by_location(event.pos[0],event.pos[1],livedata)
     locationPage = tkinter.Toplevel(homePage)
    
     
     pygame.quit()
     listTableXY(locationPage,livedata)
     
  
     loop = False
     break
     
def sort_by_location(x,y,livedata):
 for passnum in range(len(livedata)-1):
  swapped = False
  for i in range(len(livedata)-passnum-1):
   temp_distance_current = math.sqrt(abs(x-int(livedata[i][1]))**2 +abs(y-int(livedata[i][2]))**2)
   print(temp_distance_current)
   temp_distance_sort = math.sqrt(abs(x-int(livedata[i+1][1]))**2 +abs(y-int(livedata[i+1][2]))**2)
   print(temp_distance_sort)
   if temp_distance_current>temp_distance_sort:
     temp = livedata[i]
     livedata[i] = livedata[i+1]
     livedata[i+1] = temp
     swapped = True

   if not swapped:
     return livedata
 return livedata

