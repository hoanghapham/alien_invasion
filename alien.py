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

    def reached_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

