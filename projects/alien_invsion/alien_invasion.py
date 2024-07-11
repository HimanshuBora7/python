import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    "overall class to manage , and create game resoources "
    def __init__(self):
     pygame.init()
     self.setting = Settings()
     self.screen = pygame.display.set_mode ((self.setting.screen_width,self.setting.screen_height))
     pygame.display.set_caption("Alien Invasion")
     self.ship = Ship(self)
     self.bg_color = (230 ,230 ,230)

    def run_game(self):
       """start the main loop for game"""
       while True:
          self.check_events()
          self.ship.update_self()
          self.update_screen()
          #watch for keyboard and mouse events.
          for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()
        
    def check_events(self):
             """respond to keypress and mouse events"""
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #move the ship to the right
                        self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                   
    def update_screen(self):
        """update images on the screen ,and flip to the new screen """
          #redraw the screen during each pass through the loop 
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
          #makeing the most recently drawn screen visible 
        pygame.display.flip()
 
        
if __name__ == '__main__':
   # Make a game instance and run the game 
   ai = AlienInvasion()
   ai.run_game()


