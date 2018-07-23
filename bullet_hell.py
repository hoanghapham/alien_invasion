import pygame
import sys
from pygame.sprite import Sprite

pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Ship():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.center = self.screen_rect.center
        # self.rect.bottom = self.screen_rect.bottom
        # self.center = float(self.rect.center)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        
        cond_right = self.rect.right < self.screen_rect.right and self.moving_right
        cond_left = self.rect.left > self.screen_rect.left and self.moving_left
        cond_up = self.rect.top > self.screen_rect.top and self.moving_up
        cond_down = self.rect.bottom < self.screen_rect.bottom and self.moving_down
        
        self.rect.centerx += 1 * cond_right - 1 * cond_left
        self.rect.centery += 1 * cond_down - 1 * cond_up

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship):
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
ship = Ship(screen)

class Bullet(Sprite):

    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.ship = ship


        self.bullet_speed_factor = 2
        self.bullet_color = 60, 60, 60

        self.bullet_height = 5
        self.bullet_width = 5
        self.rect = pygame.rect(
            0, 0, 
            self.bullet_width, self.bullet_height
        )
        self.rect.centery = self.ship.rect.centery
        self.rect.right = self.ship.rect.right
        self.x = float(self.rect.x) # self.rect.x cannot contain float values so we do a roundabout

    def update(self):
        self.x += 1 * self.bullet_speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        # Create a rect to hold the shape of the bullet
        # draw on the screen a rect, with bullet_color 
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)



while True:
    screen.fill((230, 230, 230))
    check_events(ship)
    ship.update()
    ship.blitme()
    pygame.display.flip()
