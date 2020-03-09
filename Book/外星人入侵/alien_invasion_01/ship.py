import pygame
# from setting import Setting

class Ship():
    def __init__(self, screen, setting):
        """ 初始化飞船和设置初始位置 """
        self.screen = screen
        self.image = pygame.image.load(setting.ship_img)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moveing_right = False
        self.moveing_left = False
        self.speed_factor = setting.ship_speed_factor
        
        # 将飞船放到底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.moveing_left and self.rect.centerx > 0:
            self.rect.centerx -= self.speed_factor
        if self.moveing_right and self.rect.centerx < self.screen_rect.right:
            self.rect.centerx += self.speed_factor
