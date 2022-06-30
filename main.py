import pygame
from constant import *
from objects import *

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def game_loop():
    snake = Snake()
    apple = Apple()
    apple.spawn(snake)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                #check if can move in specified direction.
                if event.key == pygame.K_UP:
                    snake.move_up(apple)
                    snake.hit_boundary()
                elif event.key == pygame.K_DOWN:
                    snake.move_down(apple)
                    snake.hit_boundary()
                elif event.key == pygame.K_LEFT:
                    snake.move_left(apple)
                    snake.hit_boundary()
                elif event.key == pygame.K_RIGHT:
                    snake.move_right(apple)
                    snake.hit_boundary()
        SCREEN.fill("white")
        snake.draw_snake(SCREEN)
        apple.draw_apple(SCREEN)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    game_loop()