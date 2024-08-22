import pygame
import sys
import requests

from config import *
from .game import Game


class Main: # TODO: reorganize structure
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Farmer code")
        self.surface = pygame.display.set_mode(SIZE)
        self.game = Game()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
                    sys.exit()

            self.game.handle_event(event)
            
    def run(self):
        while True:
            self.surface.fill(BACKGROUND_COLOR)

            self.handle_events()
            self.game.update()
            self.game.render(self.surface)
            
            pygame.display.flip()