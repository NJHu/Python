import pygame
import sys
from ship import Ship

def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = False
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = False
    
def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    