#12-1. Blue Sky: Make a Pygame window with a blue background.
import sys
import pygame

class Screen:
    def __init__(self):
     pygame.init()
     self.screen = pygame.display.set_mode((1050,700))
     self.bg_colour = (100,100,230)
    def show_bg(self):
       while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()
        self.screen.fill((26,168,255))
        
        pygame.display.flip()

if __name__ == '__main__':      
 user_01 = Screen()
 user_01.show_bg()