# pip3 install pygame

import pygame
from setting import Setting
# from event import *
import event
from ship import Ship
import game_funcations as gf
from pygame.sprite import Group
from game_stats import GameStats

def main():
    pygame.init()
    al_setting = Setting()
    bullets = Group()
    aliens = Group()
    stats = GameStats(al_setting)
    # 设置屏幕
    screen = pygame.display.set_mode((al_setting.screen_width, al_setting.screen_height))
    pygame.display.set_caption(al_setting.game_title)
    # 创建飞船
    ship = Ship(screen, al_setting)
    # 创建外星人
    gf.create_aliens(al_setting, screen, aliens, ship.rect.height)
    # 开启游戏主循环
    while True:
        # 处理事件
        event.check_event(al_setting, screen, ship, bullets)
        # 更新位置
        ship.update()
        gf.update_bullets(al_setting, screen, ship, bullets, aliens)
        gf.update_aliens(al_setting, screen, ship, bullets, aliens, stats)
        # 绘制
        gf.update_screen(al_setting, screen, ship, bullets, aliens)

if __name__ == "__main__":
    main()