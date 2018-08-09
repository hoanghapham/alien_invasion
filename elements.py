"""Create and control elements"""
from alien import Alien
import game_functions as gf


# Build elements
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

def change_fleet_directions(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed 
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.reached_edges():
            change_fleet_directions(ai_settings, aliens)
            break

def check_aliens_bottom(ai_settings, stats, scoreboard, screen, 
    ship, aliens, bullets, game_over):

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gf.ship_hit(ai_settings, stats, screen, scoreboard, 
                ship, aliens, bullets, game_over)
            break

