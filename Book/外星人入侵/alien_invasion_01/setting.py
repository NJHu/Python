class Setting():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.game_title = 'Alien Invasion'
        self.bg_color = (230, 230, 230)
        
        self.ship_img = './images/ship.bmp'
        self.ship_limit = 3
        
        self.bullet_color = (60, 60 ,60)
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_allowed = 100
        
        self.alien_drop_factor = 10
        
        self.alien_img = './images/alien.bmp'
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
    
    # 初始化动态
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 20
        self.bullet_speed_factor = 30
        self.alien_speed_factor = 20
        self.alien_direction = 1
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale