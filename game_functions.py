"""Functions to control game"""

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from scoreboard import check_high_score, check_max_level
import elements as elm

# Start, exit, restart game
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
    elm.create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # reset scores
    scoreboard.prep_images()

def exit_game(stats):
    stats.save_progress()
    sys.exit()

def start_new_level(ai_settings, screen, stats, ship, aliens, bullets, scoreboard):
    bullets.empty()
    ai_settings.increase_speed()
    elm.create_fleet(ai_settings, screen, ship, aliens)
    stats.level += 1
    check_max_level(stats, scoreboard)
    scoreboard.prep_level()

# Objects' on-screen interactions
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
        start_new_level(ai_settings, screen, stats, ship, 
            aliens, bullets, scoreboard)

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

        elm.create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause game
        sleep(0.5)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        game_over.draw_button()


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


def update_aliens(ai_settings, stats, scoreboard, screen, ship, 
    aliens, bullets, game_over):
    elm.check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, scoreboard, ship, 
                    aliens, bullets, game_over)

    elm.check_aliens_bottom(ai_settings, stats, scoreboard, screen, ship, 
        aliens, bullets, game_over)
