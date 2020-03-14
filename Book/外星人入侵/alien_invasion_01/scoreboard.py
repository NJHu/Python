import pygame.font
from ship  import Ship
from pygame.sprite import Group

class ScoreBoard():
    def __init__(self, al_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.al_settings = al_settings
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.pre_score()
        self.pre_high_score()
        self.pre_level()
        self.pre_ship()
        
    def pre_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.al_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def pre_high_score(self):
        rounded_score = int(round(self.stats.high_score, -1))
        score_str = "{:,}".format(rounded_score)
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.al_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.right * 0.5
        self.high_score_rect.top = 20
    
    def pre_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.al_settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom
        
    def pre_ship(self):
        # self.ship_left_image = self.font.render(str(self.stats.ship_left), True, self.text_color, self.al_settings.bg_color)
        # self.ship_left_image_rect = self.ship_left_image.get_rect()
        # self.ship_left_image_rect.left = 10
        # self.ship_left_image_rect.top = 10
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen, self.al_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    
    def show(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        #self.screen.blit(self.ship_left_image, self.ship_left_image_rect)
        self.ships.draw(self.screen)