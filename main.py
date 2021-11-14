import pygame
from Entities.player import Player

#CONSTANTS
WIDTH, HEIGHT = 720, 364
FPS = 60

#WINDOW INIT
pygame.display.set_caption("First Game!")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#GENERAL SETUP
player = Player(100,100)
moving_sprite = pygame.sprite.Group()
moving_sprite.add(player)

#Main Function with event handler
def main():
    #VARIABLES
    clock = pygame.time.Clock()
    run = True

    #Event Handler
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            moving_sprite.draw(WIN)
        pygame.display.update()

    #EXIT
    pygame.quit()

#Running main function
if __name__ == "__main__":
    main()