"""Control interactions between human & game"""
import sys
import pygame
from bullet import Bullet
import game_functions as gf


def check_play_button(ai_settings, screen, stats, scoreboard, play_button, ship, 
        aliens, bullets, mouse_x, mouse_y):
    """Start new game when player click play. Reset the field"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:    
        gf.start_game(ai_settings, screen, stats, ship, aliens, bullets, scoreboard)
        
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets, scoreboard):
    """Handling key down events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and stats.game_active:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p:
        gf.start_game(ai_settings, screen, stats, ship, aliens, bullets, scoreboard)
    elif event.key == pygame.K_q:
        gf.exit_game(stats)

def check_keyup_events(event, ship):
    """Handling key up events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, scoreboard, play_button, 
        ship, aliens, bullets):
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gf.exit_game(stats)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets, scoreboard)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, scoreboard, play_button, ship, 
                                aliens, bullets, mouse_x, mouse_y)