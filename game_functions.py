import sys
import pygame
from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Handling key down events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Handling key up events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Check if right key is pressed and set right movement flag = True
        # Then, check if right key is released and set right movement flag = False
        # Do the same for left key.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """redraw screen at each pass of the loop, and flip to the new screen"""

    # Redraw the screen during each pass of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    # Remove old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom == 0:
            bullets.remove(bullet)