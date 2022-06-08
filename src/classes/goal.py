# MazeWar Project - File 15

import pygame
from Directory_Settings import spPlayer
from pygame.transform import scale
from pygame.sprite import Sprite


class Goal(Sprite):

    def __init__(self, cell_size, start_position, screen):
        super().__init__()
        self.image = pygame.transform.scale(spPlayer, (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.center = start_position
