# pip3 install pygame

import pygame
from setting import Setting
# from event import *
import event
from ship import Ship
import game_funcations as gf
from pygame.sprite import Group

def main():
    pygame.init()
    al_setting = Setting()
    bullets = Group()
    
    # 设置屏幕
    screen = pygame.display.set_mode((al_setting.screen_width, al_setting.screen_height))
    pygame.display.set_caption(al_setting.game_title)
    # 创建飞船
    ship = Ship(screen, al_setting)
    
    # 开启游戏主循环
    while True:
        # 处理事件
        event.check_event(ship)
        # 更新位置
        ship.update()
        bullets.update()
        
        # 绘制
        gf.update_screen(al_setting, screen, ship)




if __name__ == "__main__":
    main()