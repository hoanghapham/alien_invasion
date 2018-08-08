import pygame
from pygame.sprite import Group
import argparse
import sys

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button, GameOver
from scoreboard import ScoreBoard
import game_functions as gf
import player_input as inp
import elements as elm


def run_game(mode):
    # Init game & create screen object
    pygame.init()
    ai_settings = Settings()
    if mode == 'test':
        ai_settings.test_mode == True
        
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
    elm.create_fleet(ai_settings, screen, ship, aliens)

    # Create play button
    play_button = Button(ai_settings, screen, 'Play!')
    restart_button = Button(ai_settings, screen, 'Restart')
    game_over = GameOver(ai_settings, stats, screen, 'GAME OVER!')
    # Create Scoreboard
    scoreboard = ScoreBoard(ai_settings, screen, stats)

    # Start the main loop for the game:
    while True:
        # Watch for keyboard & mouse events
        # Update screen & flip to a new screen
        # When pressing Space, check_event will register a space key down event 
        # and create a new bullet. Then bullets.update() will move the bullets
        # in the Group across the screen.
        inp.check_events(ai_settings, screen, stats, scoreboard, play_button, 
            ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, scoreboard, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, bullets, game_over)
        
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, 
                        play_button, restart_button, scoreboard, game_over)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Choose run mode.')
    parser.add_argument('-m', '--mode', default='default', choices=['default', 'test'])
    info = parser.parse_args()
    run_game(info.mode)


