class GameStats():
    def __init__(self, al_setting):
        super().__init__()
        self.al_setting = al_setting
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1
    
    def reset_stats(self):
        self.ship_left = self.al_setting.ship_limit
        self.score = 0
        self.level = 1