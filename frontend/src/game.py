import pygame
from .auth_page import AuthPage
from .compiler import Compiler
from .main_page import MainPage


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
        try:
            return self.current_page.response.json().get("user").get("authenticated")
        except:
            ...

    def change_page(self):
        self.current_page = Compiler()