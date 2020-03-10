import pygame
from ship import Ship
from setting import Setting
from bullet import Bullet
from pygame.sprite import Sprite
from alien import Alien

def create_aliens(al_setting, screen, aliens, ship_height):
    alien = Alien(al_setting, screen)
    # 一行放多少个
    rows = get_h_number_alien(al_setting, alien.rect.width)
    lines = get_v_number_alien(al_setting, alien.rect.height, ship_height)
    
    for line in range(lines):
        for row in range(rows):
            create_a_alien(al_setting, screen, aliens, row, line)

def get_h_number_alien(al_setting, alien_width):
    space_h = al_setting.screen_width - 2 * alien_width
    rows = space_h // (2 * alien_width)
    return rows

def get_v_number_alien(al_setting, alien_height, ship_height):
    space_v = al_setting.screen_height - ship_height - 2 * alien_height
    lines = space_v // (2 * alien_height)
    return lines

def create_a_alien(al_setting, screen, aliens, row, line):
    alien = Alien(al_setting, screen)
    alien.x = alien.rect.width + row * 2 * alien.rect.width
    alien.rect.x = alien.x
    alien.y = alien.rect.height + line * 2 * alien.rect.height
    alien.rect.y = alien.y
    aliens.add(alien)

def update_bullets(bullets):
    bullets.update()
    # 删除子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(al_setting, screen, ship, bullets):
    if len(bullets) < al_setting.bullet_allowed:
        new_bullet = Bullet(screen, al_setting, ship)
        bullets.add(new_bullet)
    

def update_screen(al_setting, screen, ship, bullets, aliens):
    # 每次循环都重新绘制屏幕, 一定要先绘制颜色
        screen.fill(al_setting.bg_color)
        # 绘制飞船
        ship.blitme()
        # 绘制子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        # 绘制外星人
        # for alien in aliens.sprites():
        #     alien.blitme()
        aliens.draw(screen)
        # 让屏幕可见
        pygame.display.flip()