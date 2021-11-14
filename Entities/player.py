import pygame
from spritesheet import Spritesheet
from entity import Entity

#Player Class
class Player(Entity):
    def __init__(self, pos_x, pos_y):
        Entity.__init__(self, pos_x, pos_y, "PLAYER")
        Entity.init_spritesheet(self, 8)
    
    

