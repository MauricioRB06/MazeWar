# MazeWar Project - File 14

import pygame
from Directory_Settings import spPlayer
from pygame.transform import scale
from pygame.sprite import Sprite


class Player(Sprite):

    def __init__(self, cell_size, start_position, screen):
        super().__init__()
        self.cell = cell_size
        self.speed = 0
        self.SCREEN = screen
        self.image = pygame.transform.scale(spPlayer, (cell_size//2, cell_size//2))
        self.rect = self.image.get_rect()
        self.rect.center = start_position

    def update(self):

        self.speed = 0

        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_LEFT]:
            self.speed = -2
            self.rect.x += self.speed

        if pressed_key[pygame.K_RIGHT]:
            self.speed = 2
            self.rect.x += self.speed

        if pressed_key[pygame.K_UP]:
            self.speed = -2
            self.rect.y += self.speed

        if pressed_key[pygame.K_DOWN]:
            self.speed = 2
            self.rect.y += self.speed

    def move_back(self):
        self.rect.top = self.rect.top + self.cell//(self.cell * 0.5)

    def move_forward(self):
        self.rect.bottom = self.rect.bottom - self.cell//(self.cell * 0.5)

    def move_left(self):
        self.rect.left = self.rect.left - self.cell//(self.cell * 0.5)

    def move_right(self):
        self.rect.right = self.rect.right + self.cell//(self.cell * 0.5)
