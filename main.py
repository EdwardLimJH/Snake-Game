import pygame
import constant as cst
import objects as obj

pygame.init()
SCREEN = pygame.display.set_mode((cst.SCREEN_WIDTH, cst.SCREEN_HEIGHT))
clock = pygame.time.Clock()


def game_loop():
    snake = obj.Snake()
    apple = obj.Apple()
    background_img = pygame.image.load(cst.BACKGROUND_IMG_FILEPATH)
    background_img = pygame.transform.scale(background_img,
                                            (cst.SCREEN_WIDTH,
                                             cst.SCREEN_HEIGHT))

    apple.spawn(snake)
    run = True

    while run:
        clock.tick(cst.FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.move_up()

                elif event.key == pygame.K_DOWN:
                    snake.move_down()

                elif event.key == pygame.K_LEFT:
                    snake.move_left()

                elif event.key == pygame.K_RIGHT:
                    snake.move_right()

        snake.auto_move(apple)
        snake.check_game_over(apple)
        draw_display(SCREEN, snake, apple, background_img)
    pygame.quit()


def draw_display(SCREEN, snake, apple, background_img):
    SCREEN.blit(background_img, (0, 0))
    snake.draw_snake(SCREEN)
    apple.draw_apple(SCREEN)
    pygame.display.update()


if __name__ == "__main__":
    game_loop()
