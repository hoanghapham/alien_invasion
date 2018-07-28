import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class for aliens"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start alien ships at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its location"""
        self.screen.blit(self.image, self.rect)



    