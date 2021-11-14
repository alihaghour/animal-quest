#Class Description: Provides a parent class 'Entity' that provides game object attributes/functions
import pygame
from Entities.spritesheet import Spritesheet

class Entity(pygame.sprite.Sprite):
    
    #Default Constructor
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.health = 100


        
