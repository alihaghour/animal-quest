import pygame
from spritesheet import Spritesheet


#CONSTANTS
WIDTH, HEIGHT = 720, 364
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

#WINDOW INIT
pygame.display.set_caption("First Game!")

#VARIABLES
clock = pygame.time.Clock()
run = True

#Main Function with event handler
def main():

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