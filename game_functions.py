import sys
import pygame


def check_events(ship):
    """Watch for keyboard and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Check if right key is pressed and set right movement flag = True
        # Then, check if right key is released and set right movement flag = False
        # Do the same for left key.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """redraw screen at each pass of the loop, and flip to the new screen"""

    # Redraw the screen during each pass of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()