import pygame
from Entities.spritesheet import Spritesheet

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.health = 100

        self.spritesheet = Spritesheet('./Entities/playerss.png')

        for x in range(8):
            (self.sprites).append(self.spritesheet.get_sprite(x, 32, 32, 3, (0,0,0)))

        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]