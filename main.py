import pygame
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

    # Make ship
    ship = Ship(screen)

    # Start the main loop for the game:
    while True:

        # Watch for keyboard & mouse events
        # Update screen & flip to a new screen
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)




if __name__ == '__main__':
    run_game()