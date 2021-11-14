import pygame
import player
from spritesheet import Spritesheet

#CONSTANTS
WIDTH, HEIGHT = 720, 364
FPS = 60

#WINDOW INIT
pygame.display.set_caption("First Game!")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

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
        pygame.display.update()
    #EXIT
    pygame.quit()

#Running main function
if __name__ == "__main__":
    main()