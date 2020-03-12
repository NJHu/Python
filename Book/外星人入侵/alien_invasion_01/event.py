import pygame
import sys
from ship import Ship
from bullet import Bullet
from pygame.sprite import Sprite
import game_funcations as gf

# event.type == pygame.KEYDOWN and 

def check_event(al_setting, screen, ship, bullets, play_button, stats, aliens):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(al_setting, screen, event, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(al_setting, screen, ship, bullets, play_button, stats, aliens, mouse_x, mouse_y)
            
def check_play_button(al_setting, screen, ship, bullets, play_button, stats, aliens, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        stats.game_active = True
        stats.reset_stats()
        ship.ship_center()
        bullets.empty()
        aliens.empty()
        gf.create_aliens(al_setting, screen, aliens, ship.rect.height)
        pygame.mouse.set_visible(False)
        
def check_keyup_events(event, ship, stats):
    if not stats.game_active:
        return

    if event.key == pygame.K_RIGHT:
        ship.moveing_right = False
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = False
    
def check_keydown_events(al_setting, screen, event, ship, bullets, stats):
    if not stats.game_active:
        return
    
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    elif event.key == pygame.K_SPACE:
        gf.fire_bullet(al_setting, screen, ship, bullets)