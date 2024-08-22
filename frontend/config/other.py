import pygame
import os
pygame.init()

FONT_MATEMASIE = os.path.join("frontend", "assets", "fonts", 'Matemasie-Regular.ttf')
FONT_REGULAR = os.path.join("frontend", "assets", "fonts", 'Roboto-Medium.ttf')

SPACES = 4 # amount of spaces in compiler
CHECK_CONFIRMATION_TIMER = 2 # each n seconds function will be called