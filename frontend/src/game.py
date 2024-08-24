import pygame
from .auth_page import AuthPage
from .compiler import Compiler
from .main_page import MainPage
import json

class Game:
    def __init__(self):
        self.current_page = MainPage()

    
    def handle_event(self, event):
        self.current_page.handle_event(event)


    def update(self):
        self.current_page.update()

        if self.current_page.__class__.__name__ == "AuthPage":
            if self.check_for_auth():
                self.change_page()

    def render(self, surface):
        self.current_page.render(surface)


    def check_for_auth(self):
        response = self.current_page.response
        try:
            if response.json().get("user").get("authenticated"):
                with open("data.json", "w", encoding="utf-8") as f:
                    json.dump(response.json().get("user"), f, indent=4)

                return True
            else:
                return False
        except:
            ...

    def change_page(self):
        self.current_page = MainPage()