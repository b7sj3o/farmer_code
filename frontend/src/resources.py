from config import *
import pygame
import requests
import json
import time


class Resources:
    def __init__(self):
        self.resources = {}
        self.update_resources()
        self.data = {}
        self.resources_rects = []
        self.get_data()
        self.time = time.time()

        self.draw()


    
    def render(self, surface):
        y = 20
        for resource in self.resources_rects:
            surface.blit(resource, (20, y))
            y += 20

    
    def update(self):
        if time.time() - self.time > 3:
            self.update_resources()
            self.draw()
            self.time = time.time()
            print(self.resources_rects)


    def update_resources(self):
        try:
            response = requests.get(FASTAPI_URL_GET_USER, params={
                "username": self.data["username"]
            }) 
            if response.status_code == 200:
                data = response.json()
                self.resources = data.get("user", {}).get("resources", {})
            else:
                print(f"Error occured")
        except Exception as ex:
            print(f"{ex=}")


    def draw(self):
        self.update_resources()
        self.resources_rects.clear()
        font = pygame.font.Font(FONT_REGULAR, 26)
        for resource, amount in self.resources.items():
            text = font.render(f"{resource}: {amount}", True, WHITE)
            self.resources_rects.append(text)
        

    def get_data(self):
        with open("data.json", "r") as f:
            self.data = json.load(f)


