import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    
    def __init__(self, ai_game):
        """ Initialize the alien and set its starting point"""
        super().__init()
        self.screen = ai_game.screen
        
        # Load the alien and set its rect attribute
        self.image = pygame.image.load('C:/Users/sethb/OneDrive/Desktop/Ref. Py Crash Course/ehmatthes-pcc_2e-078318e/chapter_13/creating_first_alien/images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)
    
