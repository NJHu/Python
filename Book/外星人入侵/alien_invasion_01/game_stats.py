class GameStats():
    def __init__(self, al_setting):
        super().__init__()
        self.al_setting = al_setting
        self.game_active = True
        self.reset_stats()
    
    def reset_stats(self):
        self.ship_left = self.al_setting.ship_limit