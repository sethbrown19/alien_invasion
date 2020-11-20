class Settings:
    """ A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the games settings"""
        
        
        # Screen settings
        self.screen_width =1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        # Ship settings
        self.ship_speed = 1.6
        
        # Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 17
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 7
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 rrepresents right; -1 represents left.
        self.fleet_direction = 1