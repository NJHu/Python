class Setting():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.game_title = 'Alien Invasion'
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 10
        self.ship_img = './images/ship.bmp'
        self.ship_limit = 3
        
        self.bullet_color = (60, 60 ,60)
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_speed_factor = 20
        self.bullet_allowed = 5
        
        self.alien_img = './images/alien.bmp'
        self.alien_speed_factor = 100
        self.alien_direction = 1
        self.alien_drop_factor = 50