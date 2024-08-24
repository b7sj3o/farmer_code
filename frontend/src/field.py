from .robot import Robot
from config import *
from .block import Block
from .crops import Wheat


class Field:
    def __init__(self):
        self.robot = Robot()
        self.blocks = []
        self.create_field()


    def create_field(self):
        for i in range(FIELD_SIZE):
            blocks_row = []
            for j in range(FIELD_SIZE):
                block = Block(FIELD_X + (BLOCK_SIZE * j), FIELD_Y + (BLOCK_SIZE * i))
                block.plant(Wheat())
                blocks_row.append(block)
            
            self.blocks.append(blocks_row)


    def render(self, surface):
        if self.blocks:
            for block_row in self.blocks:
                for block in block_row:
                    block.render(surface)

        self.robot.render(surface)


    def update(self):
        if self.blocks:
            for block_row in self.blocks:
                for block in block_row:
                    block.update()