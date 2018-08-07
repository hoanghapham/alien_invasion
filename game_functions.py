import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

# Check events & interactions

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
        start_game(ai_settings, screen, stats, ship, aliens, bullets, scoreboard)
    elif event.key == pygame.K_q:
        stats.save_progress()
        sys.exit()

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
            stats.save_progress()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets, scoreboard)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, scoreboard, play_button, ship, 
                                aliens, bullets, mouse_x, mouse_y)

def check_collisions(ai_settings, screen, stats, scoreboard, ship, bullets, aliens):
    # If bullets collide with aliens, delete both
    collisions = pygame.sprite.groupcollide(bullets, aliens, 
                ai_settings.kill_bullet, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            scoreboard.prep_score()
        check_high_score(stats, scoreboard)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        scoreboard.prep_level()


def start_game(ai_settings, screen, stats, ship, aliens, bullets, scoreboard):
    
    # Reset speed
    ai_settings.init_dynamic_settings()

    # Hide mouse cursor
    pygame.mouse.set_visible(False)

    # Reset game statistics
    stats.reset_stats()
    stats.game_active = True
    
    # Empty aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create new fleet & center ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # reset scores
    scoreboard.prep_score()
    scoreboard.prep_high_score()
    scoreboard.prep_level()
    scoreboard.prep_ship()

def check_play_button(ai_settings, screen, stats, scoreboard, play_button, ship, 
        aliens, bullets, mouse_x, mouse_y):
    """Start new game when player click play. Reset the field"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:    
        start_game(ai_settings, screen, stats, ship, aliens, bullets, scoreboard)
        


# Update elements
def update_screen(ai_settings, stats, screen, ship, aliens, bullets, 
                play_button, restart_button, scoreboard, game_over):
    """redraw screen at each pass of the loop, and flip to the new screen"""

    # Redraw the screen during each pass of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    # Draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the play button if the game is inactive:
    if not stats.game_active:
        play_button.draw_button()

    if stats.ship_left == 0 and not stats.game_active:
        restart_button.draw_button()
        game_over.draw_button()

    # Draw scoreboard
    scoreboard.show_score()

    # Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, scoreboard, ship, bullets, aliens):
    """
    Update bullets' position and detect collisions
    """
    bullets.update()

    # Remove old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_collisions(ai_settings, screen, stats, scoreboard, ship, bullets, aliens)    


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

def update_aliens(ai_settings, stats, scoreboard, screen, ship, 
    aliens, bullets, game_over):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, scoreboard, ship, 
            aliens, bullets, game_over)

    check_aliens_bottom(ai_settings, stats, scoreboard, screen, ship, 
        aliens, bullets, game_over)


def ship_hit(ai_settings, stats, screen, scoreboard, ship, 
    aliens, bullets, game_over):
    """Respond to ship being hit by an alien"""

    if stats.ship_left > 0:
        # Minus a ship
        stats.ship_left -= 1
        scoreboard.prep_ship()

        # Empty aliens and bullets, create new fleet and start a new play
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause game
        sleep(0.5)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        game_over.draw_button()


def check_aliens_bottom(ai_settings, stats, scoreboard, screen, 
    ship, aliens, bullets, game_over):

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, scoreboard, 
                ship, aliens, bullets, game_over)
            break

def check_high_score(stats, scoreboard):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()

    