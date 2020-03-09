import pygame
from ship import Ship
from setting import Setting

def update_screen(al_setting, screen, ship):
    # 每次循环都重新绘制屏幕, 一定要先绘制颜色
        screen.fill(al_setting.bg_color)
        
        # 绘制飞船
        ship.blitme()
        
        # 让屏幕可见
        pygame.display.flip()
    