import pygame
from constant import *
from objects import Snake

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def game_loop():
    snake = Snake()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                #check if can move in specified direction.
                if event.key == pygame.K_UP:
                    snake.move_up()
                    snake.add_block()
                elif event.key == pygame.K_DOWN:
                    snake.move_down()
                elif event.key == pygame.K_LEFT:
                    snake.move_left()
                elif event.key == pygame.K_RIGHT:
                    snake.move_right()
        SCREEN.fill("white")
        snake.draw_snake(SCREEN)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    game_loop()