import pygame
from spritesheet import Spritesheet

#SPRITESHEET IMPORT
spritesheet = Spritesheet('./Assets/fullss.png')
ss1 = spritesheet.get_sprite(0, 32, 32, 3, (0,0,0))

#Player Class
class Player:
    def __init__(self, pos_x, pos_y):
        self.sprite = []
        self.sprite.append()
