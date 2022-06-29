
import pygame
from pygame.sprite import Sprite


class Wall(Sprite):

    def __init__(self, wall_rect):

        super().__init__()
        self.rect = wall_rect
