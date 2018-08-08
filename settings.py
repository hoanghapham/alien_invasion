class Settings():
    """All settings for Alien Invasion"""

    def __init__(self):
        """Init game's settings"""
        
        self.test_mode = False

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
        self.kill_bullet = True

        # Alien settings
        self.alien_speed_factor = 1
        
        # Fleet settings
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 means right, -1 means left
        
        # Stats
        self.ship_limit = 3

        # Level settings
        self.speedup_scale = 1.1
        self.point_scale = 1.5

        self.init_dynamic_settings()

        # init test mode
        if self.test_mode:
            self.init_test_mode()

    def init_dynamic_settings(self):
        """Initialize settings that will change through out the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.point_scale)
        
    
    def init_test_mode(self):
        self.bullet_width = 200
        self.fleet_drop_speed = 100
        self.ship_limit = 1
        self.kill_bullet = False