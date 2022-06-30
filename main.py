import pygame
from constant import *


SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def game_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill("white")
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    game_loop()