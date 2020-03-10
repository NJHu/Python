import pygame
from ship import Ship
from setting import Setting
from bullet import Bullet
from pygame.sprite import Sprite
from alien import Alien
from time import sleep

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

def update_bullets(al_setting, screen, ship, bullets, aliens):
    bullets.update()
    # 删除子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检测碰撞
    check_bullets_collisions(al_setting, screen, ship, bullets, aliens)

# 检测碰撞
def check_bullets_collisions(al_setting, screen, ship, bullets, aliens):
    # 检测碰撞
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_aliens(al_setting, screen, aliens, ship.rect.height)


def update_aliens(al_setting, screen, ship, bullets, aliens, stats):
    check_aliens_edges(al_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(al_setting, screen, ship, bullets, aliens, stats)
    check_aliens_bottom(al_setting, screen, ship, bullets, aliens, stats)

def ship_hit(al_setting, screen, ship, bullets, aliens, stats):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        # 清空外星人
        aliens.empty()
        bullets.empty()
        create_aliens(al_setting, screen, aliens, ship.rect.height)
        ship.ship_center()
        sleep(1)
    else:
        stats.game_active = False

def check_aliens_bottom(al_setting, screen, ship, bullets, aliens, stats):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(al_setting, screen, ship, bullets, aliens, stats)
            break
    

def check_aliens_edges(al_setting, aliens):
    for alien in aliens.sprites():
        if alien.chack_edges():
            change_aliens_direction(al_setting, aliens)
            break

def change_aliens_direction(al_setting, aliens):
    for alien in aliens.sprites():
        alien.y += al_setting.alien_drop_factor
        alien.rect.y = alien.y

    al_setting.alien_direction *= -1

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