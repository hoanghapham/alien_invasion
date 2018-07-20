import pygame


class Ship():

    def __init__(self, screen):
        """
        Init the ship and its starting position.
        Parameters:
        ----------
        screen: Pass in screen object so the ship can be drawn on that screen.
        """
        self.screen = screen

        # Load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen
        # Set position of ship to center - bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Draw the ship at its current position
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1



