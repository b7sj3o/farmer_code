import pygame
from .auth import Auth
from .compiler import Compiler


class Game:
    def __init__(self):
        self.current_page = Compiler()

    
    def handle_event(self, event):
        self.current_page.handle_event(event)

    def update(self):
        self.current_page.update()

    def render(self, surface):
        self.current_page.render(surface)