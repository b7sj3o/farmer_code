from config import *
import requests
import json


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.crop = None
        self.image = GRASS_IMAGE
        self.user_data = None
        

    def update(self):
        if self.crop:
            self.crop.update()


    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

        if self.crop:
            img_center =(self.x + (BLOCK_SIZE // 2), self.y + (BLOCK_SIZE // 2))
            img_rect = self.crop.image.get_rect(center=img_center)
            surface.blit(self.crop.image, img_rect)


    def is_empty(self):
        return not self.crop


    def reset_block(self):
        self.crop = None

    
    def harvest(self):
        crop = self.crop
        crop_amount = crop.harvest_amount
        
        if crop.harvest():
            self.reset_block()

        with open("data.json", "r") as file:
            self.user_data = json.load(file)

        requests.post(FASTAPI_URL_HARVEST_RESOURCES, json={
            "username": self.user_data["username"],
            "resource": crop.name,
            "resource_amount": crop_amount
        })

    
    def plant(self, crop):
        self.crop = crop
