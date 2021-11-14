import pygame
from spritesheet import Spritesheet

################################################################################################################################

#CONSTANTS
WIDTH, HEIGHT = 720, 364
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60        
pygame.display.set_caption("First Game!")
spritesheet = Spritesheet('./Assets/fullss.png')

ss1 = spritesheet.get_sprite(0, 32, 32, 3, (0,0,0))



#BACKGROUND
def draw_background():

    pygame.display.update()

################################################################################################################################

#Main Function with event handler
def main():
    clock = pygame.time.Clock()
    run = True

    #Loop to handle events (LOCKED TO UPDATE AT 60FPS)
    while run:
        WIN.fill((50,50,50))
        WIN.blit(ss1, (0,0))
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