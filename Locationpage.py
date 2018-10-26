
import pygame

from sys import exit

def display_getuserlocation_map(livedata):
 introScreenImage = pygame.image.load("NTUMAP.png")
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
 
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
     pygame.quit()
   elif event.type == pygame.MOUSEBUTTONUP:
     messagebox.showinfo("User Location","mouse at (%d, %d)"%event.pos)
     pygame.quit()
	 


