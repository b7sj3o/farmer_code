from config import *

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.crop = None
        self.image = GRASS_IMAGE


    def is_empty(self):
        return not self.crop


    def reset_block(self):
        self.crop = None

    
    def harvest(self):
        crop = self.crop
        crop_amount = self.crop.harvest_amount
        
        if self.crop.harvest():
            self.reset_block()

        return (crop, crop_amount)

    
    def plant(self, crop):
        self.crop = crop
        self.image = crop.image

    
    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))