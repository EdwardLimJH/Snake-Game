import random as rand
import pygame
from constant import *

class Snake:

    def __init__(self) -> None:
        self.body = [pygame.Rect(rand.randint(0,SCREEN_WIDTH),
                     rand.randint(0,SCREEN_HEIGHT),
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

    def add_block(self):
        #spawn block at start of head (at end of list)
        old_body = self.get_body()
        head = old_body[0]
        new_head = self.create_snake_block(head.x + self.get_horizontal()*1*self.get_block_size(),
                     head.y + self.get_vertical()*1*self.get_block_size())
        self.set_body([new_head,] + old_body)

    def create_snake_block(self,x,y):
        return pygame.Rect(x, y, self.get_block_size(), self.get_block_size())

    def move_left(self):
        # only move left if going to left / solo snake / going up/down
        if len(self.get_body()) == 1:
            # can move left
            #settle directions:
            self.set_vertical(0)
            self.set_horizontal(-1)
            head = self.get_body()[0]
            head = self.create_snake_block(head.x + self.get_horizontal()*self.get_block_size(),
                                       head.y)
            self.set_body([head])
        else:
            #can only move if gg left / going up or down
            if self.get_horizontal() == 1:
                pass
            else:
                self.set_vertical(0)
                self.set_horizontal(-1)
                body = self.get_body()
                head = body[0]
                tail = body.pop(-1)
                tail.x = head.x + self.get_horizontal()*self.get_block_size()
                tail.y = head.y
                self.set_body([tail]+body)

    def move_right(self):
        if len(self.get_body()) == 1:
            self.set_vertical(0)
            self.set_horizontal(1)
            head = self.get_body()[0]
            head = self.create_snake_block(head.x + self.get_horizontal()*self.get_block_size(),
                                       head.y)
            self.set_body([head])
        else:
            if self.get_horizontal() == -1:
                pass
            else:
                self.set_vertical(0)
                self.set_horizontal(1)
                body = self.get_body()
                head = body[0]
                tail = body.pop(-1)
                tail.x = head.x + self.get_horizontal()*self.get_block_size()
                tail.y = head.y
                self.set_body([tail]+body)

    def move_up(self):
        if len(self.get_body()) == 1:
            self.set_vertical(-1)
            self.set_horizontal(0)
            head = self.get_body()[0]
            head = self.create_snake_block(head.x,
                                       head.y + self.get_vertical()*self.get_block_size())
            self.set_body([head])
        else:
            if self.get_vertical() == 1:
                pass
            else:
                self.set_vertical(-1)
                self.set_horizontal(0)
                body = self.get_body()
                head = body[0]
                tail = body.pop(-1)
                tail.x = head.x 
                tail.y = head.y + self.get_vertical()*self.get_block_size()
                self.set_body([tail]+body)

    def move_down(self):
        if len(self.get_body()) == 1:
            self.set_vertical(1)
            self.set_horizontal(0)
            head = self.get_body()[0]
            head = self.create_snake_block(head.x,
                                       head.y + self.get_vertical()*self.get_block_size())
            self.set_body([head])
        else:
            if self.get_vertical() == -1:
                pass
            else:
                self.set_vertical(1)
                self.set_horizontal(0)
                body = self.get_body()
                head = body[0]
                tail = body.pop(-1)
                tail.x = head.x 
                tail.y = head.y + self.get_vertical()*self.get_block_size()
                self.set_body([tail]+body)
    

    def draw_snake(self,screen):
        for rect in self.get_body():
            pygame.draw.rect(screen,"red",rect)


class Apple:
    def __init__(self):
        self.body = None
    
    def spawn(self,snake):
        snake_body = snake.get_body()
        occupied = set(map(lambda rect: (rect.x,rect.y),snake_body))
        
        