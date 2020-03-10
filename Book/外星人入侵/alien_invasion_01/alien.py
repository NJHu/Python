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
    
    # def blitme(self):
    #     self.screen.blit(self.image, self.rect)
    #     print('blitme+alien')
        