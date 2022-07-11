import random as rand
import pygame
import constant as cst


class Snake:

    def __init__(self) -> None:
        self.body = [pygame.Rect(rand.randint(
                                 0, (cst.SCREEN_WIDTH//cst.SNAKE_BODY_SIZE)-1)
                                 * cst.SNAKE_BODY_SIZE,
                     rand.randint(
                        0, (cst.SCREEN_HEIGHT//cst.SNAKE_BODY_SIZE)-1)
                        * cst.SNAKE_BODY_SIZE,
                     cst.SNAKE_BODY_SIZE,
                     cst.SNAKE_BODY_SIZE)]
        self.block_size = cst.SNAKE_BODY_SIZE
        self.vertical = 0
        self.horizontal = 0
        self.head_img = pygame.image.load(cst.SNAKE_HEAD_IMG_FILEPATH)
        self.head_img = pygame.transform.scale(self.head_img,
                                               (self.block_size*2,
                                                self.block_size*2))

    def get_body(self):
        return self.body

    def get_block_size(self):
        return self.block_size

    def get_horizontal(self):
        return self.horizontal

    def get_vertical(self):
        return self.vertical

    def get_head_image(self):
        return self.head_img

    def set_body(self, lst):
        self.body = lst

    def set_horizontal(self, num):
        self.horizontal = num

    def set_vertical(self, num):
        self.vertical = num

    def create_snake_block(self, x, y):
        return pygame.Rect(x, y, self.get_block_size(), self.get_block_size())

    def set_directions(self, horizontal, vertical):
        self.set_horizontal(horizontal)
        self.set_vertical(vertical)

    def add_head(self):
        old_body = self.get_body()
        head = old_body[0]
        new_head = self.create_snake_block(head.x + self.get_horizontal()
                                           * self.get_block_size(),
                                           head.y + self.get_vertical()
                                           * self.get_block_size())
        self.set_body([new_head] + old_body)

    def remove_tail(self):
        old_body = self.get_body()
        old_body.pop(-1)
        self.set_body(old_body)

    def auto_move(self, apple):
        self.add_head()
        if self.eat_apple(apple):
            apple.spawn(self)
        else:
            self.remove_tail()

    def move_left(self):
        if not(self.get_horizontal() == 1 and len(self.get_body()) != 1):
            self.set_directions(-1, 0)

    def move_right(self):
        if not (self.get_horizontal() == -1 and len(self.get_body()) != 1):
            self.set_directions(1, 0)

    def move_up(self):
        if not (self.get_vertical() == 1 and len(self.get_body()) != 1):
            self.set_directions(0, -1)

    def move_down(self):
        if not(self.get_vertical() == -1 and len(self.get_body()) != 1):
            self.set_directions(0, 1)

    def eat_apple(self, apple):
        apple_rect = apple.get_body()
        head = self.get_body()[0]
        if head.colliderect(apple_rect):
            return True
        else:
            return False

    def hit_boundary(self):
        head = self.get_body()[0]
        exceed_width = head.x < 0 or head.x >= cst.SCREEN_WIDTH
        exceed_height = head.y < 0 or head.y >= cst.SCREEN_HEIGHT
        if exceed_width or exceed_height:
            return True
        return False

    def hit_self(self):
        body = self.get_body()
        head = body[0]
        return any([head.colliderect(x) for x in body[1:]])

    def check_game_over(self, apple):
        if self.hit_boundary() or self.hit_self():
            self.restart()
            apple.restart(self)

    def restart(self):
        self.set_directions(0, 0)
        rect = self.create_snake_block(cst.SNAKE_RESPAWN_X,
                                       cst.SNAKE_RESPAWN_Y)
        self.set_body([rect])

    def draw_snake(self, screen):
        for indx, rect in enumerate(self.get_body()):
            if indx == 0:
                screen.blit(self.get_head_image(), (rect.x, rect.y),
                            (12.5, 12.5, 25, 25))
            else:
                pygame.draw.rect(screen, "yellow", rect)


class Apple:
    def __init__(self):
        self.body = None
        self.block_size = cst.APPLE_SIZE
        self.image = pygame.image.load(cst.APPLE_IMG_FILEPATH)
        self.image = pygame.transform.scale(self.image, (200, 200))

    def get_body(self):
        return self.body

    def set_body(self, rect):
        self.body = rect

    def get_block_size(self):
        return self.block_size

    def get_image(self):
        return self.image

    def create_apple_rect(self, x, y):
        return pygame.Rect(x, y, self.get_block_size(), self.get_block_size())

    def spawn(self, snake):
        snake_body = snake.get_body()
        occupied = set(map(lambda rect: (rect.x, rect.y), snake_body))
        loc = (rand.randint(0, (cst.SCREEN_WIDTH//self.get_block_size()) - 1) *
               self.get_block_size(),
               rand.randint(0, (cst.SCREEN_HEIGHT//self.get_block_size()) - 1)
               * self.get_block_size())
        while True:
            if loc not in occupied:
                break
            loc = (rand.randint(0,
                   (cst.SCREEN_WIDTH//self.get_block_size()) - 1)
                   * self.get_block_size(),
                   rand.randint(0,
                   (cst.SCREEN_HEIGHT//self.get_block_size())-1)
                   * self.get_block_size())
        rect = self.create_apple_rect(loc[0], loc[1])
        self.set_body(rect)

    def restart(self, snake):
        self.spawn(snake)

    def draw_apple(self, screen):
        loc = self.get_body()
        screen.blit(self.get_image(), (loc.x, loc.y), 
                    (9, 9, self.get_block_size(), self.get_block_size()))
