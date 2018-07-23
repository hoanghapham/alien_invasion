import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets"""

    def __init__(self, ai_settings, screen, ship):
        """
        Create a bullet at current ship's position
        """
        super().__init__()
        self.screen = screen
        self.ship = ship
        self.ai_settings = ai_settings

        # Create bullet
        self.rect = pygame.Rect(0, 0, 
            self.ai_settings.bullet_width, self.ai_settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        # Bullet position at decimal value
        self.y = float(self.rect.y)

        self.color = self.ai_settings.bullet_color
        self.speed_factor = self.ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up in the screen"""
        self.y -= 1 * self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

