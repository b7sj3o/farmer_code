import pygame
from config import *


class Robot:
    def __init__(self):
        self.x = 0 # in two-dimentional array
        self.y = 0 # in two-dimentional array
        self.real_x = (self.x * BLOCK_SIZE) + FIELD_X
        self.real_x_2 = self.real_x
        self.real_y = (self.y * BLOCK_SIZE) + FIELD_Y
        self.real_y_2 = self.real_y
        self.percent = BLOCK_SIZE / 100
        self.speed = 3 # block in seconds
        self.image = ROBOT_IMAGE
        # self.surface = None
    
    def render(self, surface):
        # self.surface = surface
        if self.real_x_2 > self.real_x:
            self.real_x_2 -= self.percent * 2
        elif self.real_x_2 < self.real_x:
            self.real_x_2 += self.percent * 2
        if self.real_y_2 > self.real_y:
            self.real_y_2 -= self.percent * 2
        elif self.real_y_2 < self.real_y:
            self.real_y_2 += self.percent * 2
        surface.blit(self.image, (self.real_x_2, self.real_y_2))
        


    def update(self):
        ...
        

    
    def get_pos_x(self):
        return self.x
    
    def get_pos_y(self):
        return self.y

    def move(self, direction):
        if direction == North and self.y:
            self.y -= 1
        elif direction == South and self.y < FIELD_SIZE-1:
            self.y += 1
        elif direction == East and self.x < FIELD_SIZE-1:
            self.x += 1
        elif direction == West and self.x:
            self.x -= 1

        self.real_x = (self.x * BLOCK_SIZE) + FIELD_X
        self.real_y = (self.y * BLOCK_SIZE) + FIELD_Y
