import pygame
import sys
from ship import Ship
from bullet import Bullet
from pygame.sprite import Sprite
import game_funcations as gf

# event.type == pygame.KEYDOWN and 

def check_event(al_setting, screen, ship, bullets, play_button, stats, aliens, score_board):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(al_setting, screen, event, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(al_setting, screen, ship, bullets, play_button, stats, aliens, mouse_x, mouse_y, score_board)
            
def check_play_button(al_setting, screen, ship, bullets, play_button, stats, aliens, mouse_x, mouse_y, score_board):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        gf.reset_game_state(al_setting, screen, ship, bullets, stats, aliens, score_board)
        
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