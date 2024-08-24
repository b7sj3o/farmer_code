from config.compiler_vars import *
from .crops import Wheat, Potato, Carrot

class Executor:
    def __init__(self, main):
        self.code = ""
        self.main = main
        self.update_locals()
        self.globals = {
            "North": North,
            "South": South,
            "East": East,
            "West": West,
            
            "Wheat": Wheat(),
            "Potato": Potato(),
            "Carrot": Carrot()
        }
        

    def update_locals(self):
        field = self.main.field
        robot = field.robot
        block = field.blocks[robot.get_pos_y()][robot.get_pos_x()]
        crop = block.crop
        
        self.locals = {
            "get_pos_x": robot.get_pos_x,
            "get_pos_y": robot.get_pos_y,
            "move": robot.move,
            "can_harvest": crop.can_harvest if crop else None,
            "harvest": block.harvest,
            "plant": block.plant,
            "update": robot.update,
            "update_locals": self.update_locals
        }

    def execute(self):
        self.update_locals()
        exec(self.code, self.globals, self.locals)


