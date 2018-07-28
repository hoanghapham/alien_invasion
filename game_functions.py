import sys
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, alien, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, alien, bullets):
    """Handling key down events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, alien, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Handling key up events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, alien, bullets):
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Check if right key is pressed and set right movement flag = True
        # Then, check if right key is released and set right movement flag = False
        # Do the same for left key.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, alien, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, alien, bullets):
    """redraw screen at each pass of the loop, and flip to the new screen"""

    # Redraw the screen during each pass of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.draw(screen)

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

def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    num_rows = int(available_space_y / (2 * alien_height))
    return num_rows

def get_alien_number(ai_settings, alien_width):
    # Space between each alien is equal to one alien width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    num_alien_x = int(available_space_x / (2 * alien_width))
    return num_alien_x 

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create an alien fleet"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    num_alien_x = get_alien_number(ai_settings, alien_width)
    num_rows = get_number_rows(ai_settings, alien_height, ship_height)

    # Create first row of alien:
    for row_number in range(num_rows):
        for alien_number in range(num_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

