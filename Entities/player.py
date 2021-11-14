import pygame
from Entities.spritesheet import Spritesheet

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.sprites = []
        self.health = 100

        self.image = self.init_spritesheet(8)[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    
        spritesheet = Spritesheet('./Entities/playerss.png')

        #List to store sprite surfaces
        self.sprites = []

        for x in range(8):
            self.sprites.append(spritesheet.get_sprite(x, 32, 32, 3, (0,0,0)))
            
        return self.sprites