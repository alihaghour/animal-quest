import pygame

class Spritesheet:
    #Default Constructor - Extract spritesheet
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet =  pygame.image.load(filename).convert_alpha()

    #Get_Sprite - returns a surface that corresponds to the sprite in spritesheet (index parameter: frame)
    def get_sprite(self, frame, width, height, scale, color):
        sprite = pygame.Surface((width, height)).convert_alpha()
        sprite.blit(self.sprite_sheet, (0,0), ((frame*width), 0, width, height))
        sprite = pygame.transform.scale(sprite, (width*scale, height*scale))
        sprite.set_colorkey(color)
        return sprite