class Settings():
    """All settings for Alien Invasion"""

    def __init__(self):
        """Init game's settings"""

        # Screen settings
        self.screen_height = 720
        self.screen_width = 1280
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 55
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        
        # Fleet settings
        self.fleet_drop_speed = 100
        self.fleet_direction = 1 # 1 means right, -1 means left
        
        # Stats
        self.ship_limit = 3