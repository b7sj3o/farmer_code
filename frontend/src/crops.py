from random import randint
from config import *
import time

# vinci q - rose pink
# вишня ментол готова 10 50

class Crop:
    def __init__(self, name, image, grow_time, harvest_amount):
        self.name = name
        self.image = image
        self.grow_time = grow_time
        self.harvest_amount = harvest_amount
        self.is_grown = False
        self.time_planted = time.time()


    def can_harvest(self):
        return self.is_grown

    def harvest(self):
        return self.harvest_amount if self.can_harvest else 0

    def check_if_grown(self):
        if (time.time() - self.time_planted) >= self.grow_time:
            self.is_grown = True


class Wheat(Crop):
    def __init__(self):
        super().__init__(name="Wheat", image=WHEAT_IMAGE, grow_time=20, harvest_amount=select_harvest_amount())


class Carrot(Crop):
    def __init__(self):
        super().__init__(name="Carrot", image=WHEAT_IMAGE, grow_time=30, harvest_amount=select_harvest_amount())


class Potato(Crop):
    def __init__(self):
        super().__init__(name="Potato", image=WHEAT_IMAGE, grow_time=25, harvest_amount=select_harvest_amount())


def select_harvest_amount():
    return randint(1, 5)