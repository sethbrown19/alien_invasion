class Settings:
    """ A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the games settings"""
        
        
        #screen settings
        self.screen_width =1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #ship settings
        self.ship_speed = 1.5
        
        # Bullet Settings
        self.bullet_speed = 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)