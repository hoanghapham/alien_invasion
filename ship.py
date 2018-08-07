import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        """
        Init the ship and its starting position.
        Parameters:
        ----------
        screen: Pass in screen object so the ship can be drawn on that screen.
        ai_settings: pass in setting object
        """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen
        # Set position of ship to center - bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Draw the ship at its current position
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on movement flag"""
        # self.rect.centerx can only hold integers, so to use speed factor 
        # we have to update centerx in a roundabout way:
        # pass float centers to self.center then assign self.center to self.rect.centerx
        
        cond_move_right = self.moving_right and self.rect.right < self.screen_rect.right
        cond_move_left = self.moving_left and self.rect.left > self.screen_rect.left
           
        self.center += 1 * cond_move_right * self.ai_settings.ship_speed_factor \
            -1 * cond_move_left * self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
