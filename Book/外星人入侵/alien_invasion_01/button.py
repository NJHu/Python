import pygame.font

class Button():
    def __init__(self, al_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.width = 200
        self.height = 50
        self.bg_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_img.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def blitme(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_image_rect)
        