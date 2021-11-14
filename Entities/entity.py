#Class Description: Provides a parent class 'Entity' that provides game object attributes/functions
import pygame
from spritesheet import Spritesheet

class Entity(pygame.sprite.Sprite):

    #Default Constructor
    def __init__(self, pos_x, pos_y, entity_type):
        self.entity_type = entity_type
        self.sprites = []
        self.entity_type = entity_type
        self.health = 100

    #Initialize spritesheet for 'Entity' : frames = number of spritesheet frames
    def init_spritesheet(self, frames):

        if self.entity_type == "PLAYER":
            spritesheet = Spritesheet('./Entities/Player/fullss.png')
        elif self.entity_type == "POACHER":
            spritesheet = Spritesheet('./Entities/Poachers/fullss.png')

        #Array to store sprite surfaces
        self.sprites = []
        
        for x in range(frames):
            self.sprite.append(spritesheet.get_sprite(x, 32, 32, 3, (0,0,0)))

        
