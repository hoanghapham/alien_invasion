import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Init game & create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion!")

    # Make ship, aliens group, bullets group
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()

    # Create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game:
    while True:
        # Watch for keyboard & mouse events
        # Update screen & flip to a new screen
        # When pressing Space, check_event will register a space key down event 
        # and create a new bullet. Then bullets.update() will move the bullets
        # in the Group across the screen.
        gf.check_events(ai_settings, screen, ship, aliens, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

if __name__ == '__main__':
    run_game()