import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, al_setting, screen):
        super().__init__()
        self.screen = screen
        self.al_setting = al_setting
        
        self.image = pygame.image.load(al_setting.alien_img)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        self.speed_factor = al_setting.alien_speed_factor
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        print('blitme+alien')
        
    def update(self):
        self.x += (self.speed_factor * self.al_setting.alien_direction)
        self.rect.x = self.x
    
    def chack_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
        