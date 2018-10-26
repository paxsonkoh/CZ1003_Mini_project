import pygame
from sys import exit
def display_map():
 introScreenImage = pygame.image.load("NTUMAP.png")
 screen = pygame.display.set_mode((660,465))
 screen.blit(introScreenImage,(0,0))
 pygame.display.flip()
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
     pygame.quit()
   elif event.type == pygame.MOUSEBUTTONUP:
     print("mouse at (%d, %d)"%event.pos)
#main program
pygame.init()
display_map()


#End
