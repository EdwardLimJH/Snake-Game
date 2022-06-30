import random as rand
import pygame
from constant import *

class Snake:

    def __init__(self) -> None:
        self.body = [pygame.Rect(rand.randint(0,(SCREEN_WIDTH//SNAKE_BODY_SIZE)-1)*SNAKE_BODY_SIZE,
                     rand.randint(0,(SCREEN_HEIGHT//SNAKE_BODY_SIZE)-1)*SNAKE_BODY_SIZE,
                     SNAKE_BODY_SIZE,
                     SNAKE_BODY_SIZE)]
        self.block_size = SNAKE_BODY_SIZE
        self.vertical = 0
        self.horizontal = 1
    
    def get_body(self):
        return self.body
    
    def get_block_size(self):
        return self.block_size

    def get_horizontal(self):
        return self.horizontal
    
    def get_vertical(self):
        return self.vertical

    def set_body(self,lst):
        self.body = lst
    
    def set_horizontal(self,num):
        self.horizontal = num

    def set_vertical(self,num):
        self.vertical = num

    def create_snake_block(self,x,y):
        return pygame.Rect(x, y, self.get_block_size(), self.get_block_size())

    def move_left(self,apple):
        if len(self.get_body()) == 1:
            self.set_vertical(0)
            self.set_horizontal(-1)
            head = self.get_body()[0]
            new_head = self.create_snake_block(head.x + self.get_horizontal()*self.get_block_size(),
                                        head.y)
            self.set_body([new_head,head])
            if self.eat_apple(apple):
                apple.spawn(self)
            else:
                shortened_body = self.get_body()
                shortened_body.pop(-1)
                self.set_body(shortened_body)
        else:
            if self.get_horizontal() == 1:
                pass
            else:
                self.set_vertical(0)
                self.set_horizontal(-1)
                body = self.get_body()
                head = body[0]
                new_head = self.create_snake_block(head.x + self.get_horizontal()*self.get_block_size(),head.y)
                self.set_body([new_head]+body)
                if not self.eat_apple(apple):
                    shortened_body = self.get_body()
                    shortened_body.pop(-1)
                    self.set_body(shortened_body)
                else:
                    apple.spawn(self)

    def move_right(self,apple):
        if len(self.get_body()) == 1:
            self.set_vertical(0)
            self.set_horizontal(1)
            head = self.get_body()[0]
            new_head = self.create_snake_block(head.x + self.get_horizontal()*self.get_block_size(),
                                        head.y)
            self.set_body([new_head,head])
            if self.eat_apple(apple):
                apple.spawn(self)
            else:
                shortened_body = self.get_body()
                shortened_body.pop(-1)
                self.set_body(shortened_body)
        else:
            if self.get_horizontal() == -1:
                pass
            else:
                self.set_vertical(0)
                self.set_horizontal(1)
                body = self.get_body()
                head = body[0]
                new_head = self.create_snake_block(head.x + self.get_horizontal()*self.get_block_size(),head.y)
                self.set_body([new_head]+body)
                if not self.eat_apple(apple):
                    shortened_body = self.get_body()
                    shortened_body.pop(-1)
                    self.set_body(shortened_body)
                else:
                    apple.spawn(self)


    def move_up(self,apple):
        if len(self.get_body()) == 1:
            self.set_vertical(-1)
            self.set_horizontal(0)
            head = self.get_body()[0]
            new_head = self.create_snake_block(head.x,
                                        head.y + self.get_vertical()*self.get_block_size())
            self.set_body([new_head,head])
            if self.eat_apple(apple):
                apple.spawn(self)
            else:
                shortened_body = self.get_body()
                shortened_body.pop(-1)
                self.set_body(shortened_body)
        else:
            if self.get_vertical() == 1:
                pass
            else:
                self.set_vertical(-1)
                self.set_horizontal(0)
                body = self.get_body()
                head = body[0]
                new_head = self.create_snake_block(head.x, head.y + self.get_vertical()*self.get_block_size())
                self.set_body([new_head]+body)
                if not self.eat_apple(apple):
                    shortened_body = self.get_body()
                    shortened_body.pop(-1)
                    self.set_body(shortened_body)
                else:
                    apple.spawn(self)

    def move_down(self,apple):
        if len(self.get_body()) == 1:
            self.set_vertical(1)
            self.set_horizontal(0)
            head = self.get_body()[0]
            new_head = self.create_snake_block(head.x,
                                        head.y + self.get_vertical()*self.get_block_size())
            self.set_body([new_head,head])
            if self.eat_apple(apple):
                apple.spawn(self)
            else:
                shortened_body = self.get_body()
                shortened_body.pop(-1)
                self.set_body(shortened_body)
        else:
            if self.get_vertical() == -1:
                pass
            else:
                self.set_vertical(1)
                self.set_horizontal(0)
                body = self.get_body()
                head = body[0]
                new_head = self.create_snake_block(head.x, head.y + self.get_vertical()*self.get_block_size())
                self.set_body([new_head]+body)
                if not self.eat_apple(apple):
                    shortened_body = self.get_body()
                    shortened_body.pop(-1)
                    self.set_body(shortened_body)
                else:
                    apple.spawn(self)

    def eat_apple(self,apple):
        apple_rect = apple.get_body()
        head = self.get_body()[0]
        if head.colliderect(apple_rect):
            return True
        else:
            return False

    def hit_boundary(self):
        head = self.get_body()[0]
        if head.x < 0 or head.x >= SCREEN_WIDTH or head.y < 0 or head.y >= SCREEN_HEIGHT:
            rect = self.create_snake_block(250,250)
            self.set_body([rect])

    def draw_snake(self,screen):
        for rect in self.get_body():
            pygame.draw.rect(screen,"red",rect)


class Apple:
    def __init__(self):
        self.body = None
        self.block_size = APPLE_SIZE

    def get_body(self):
        return self.body

    def set_body(self,rect):
        self.body = rect

    def get_block_size(self):
        return self.block_size

    def create_apple_rect(self,x,y):
        return pygame.Rect(x, y,self.get_block_size(), self.get_block_size())
       
    def spawn(self,snake):
        snake_body = snake.get_body()
        occupied = set(map(lambda rect: (rect.x,rect.y),snake_body))
        loc = (rand.randint(0,(SCREEN_WIDTH//APPLE_SIZE)-1)*APPLE_SIZE,
               rand.randint(0,(SCREEN_HEIGHT//APPLE_SIZE)-1)*APPLE_SIZE)
        while True:
            if loc not in occupied:
                break
            loc = (rand.randint(0,(SCREEN_WIDTH//APPLE_SIZE)-1)*APPLE_SIZE,
                   rand.randint(0,(SCREEN_HEIGHT//APPLE_SIZE)-1)*APPLE_SIZE)
        rect = self.create_apple_rect(loc[0],loc[1])
        self.set_body(rect)
    
    def draw_apple(self,screen):
        pygame.draw.rect(screen,"green",self.get_body())
