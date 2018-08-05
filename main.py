import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf


def run_game():
    # Init game & create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion!")

    # Init stats
    stats = GameStats(ai_settings)

    # Make ship, aliens group, bullets group
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()

    # Create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create play button
    play_button = Button(ai_settings, screen, 'Play!')

    # Start the main loop for the game:
    while True:
        # Watch for keyboard & mouse events
        # Update screen & flip to a new screen
        # When pressing Space, check_event will register a space key down event 
        # and create a new bullet. Then bullets.update() will move the bullets
        # in the Group across the screen.
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button)

if __name__ == '__main__':
    run_game()