import pygame
from pathlib import Path
from .sizes import *

GRASS_IMAGE = pygame.transform.scale(
    pygame.image.load(Path("frontend/assets/images/grass.png")),
    (BLOCK_SIZE, BLOCK_SIZE)
)
ROBOT_IMAGE = pygame.transform.scale(
    pygame.image.load(Path("frontend/assets/images/robot.png")),
    (BLOCK_SIZE, BLOCK_SIZE)
)
WHEAT_IMAGE = pygame.image.load(
    Path("frontend/assets/images/wheats.png")
)
