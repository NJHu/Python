import pygame
import sys
from ship import Ship
from bullet import Bullet
from pygame.sprite import Sprite
import game_funcations as gf

# event.type == pygame.KEYDOWN and 

def check_event(al_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(al_setting, screen, event, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = False
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = False
    
def check_keydown_events(al_setting, screen, event, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    elif event.key == pygame.K_SPACE:
        gf.fire_bullet(al_setting, screen, ship, bullets)