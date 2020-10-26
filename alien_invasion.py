import sys

import pygame 

class AlienInvasion:
    
    def __init__(self):
        """Initialize game and creat game resources"""
        pygame.init()
    
        self.screen = pygame.display.set_mode((1200, 800)) 
        pygame.display.set_caption("Alien Ivasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            #make the most resnetly drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()