import pygame.font

class Storeboard():
    def __init__(self, al_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.al_settings = al_settings
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.pre_score()
        
    def pre_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.al_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show(self):
        self.screen.blit(self.score_image, self.score_rect)