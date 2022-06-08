# MazeWar Project - File 14

import pygame
from Directory_Settings import spPlayer
from pygame.transform import scale
from pygame.sprite import Sprite


class Player(Sprite):

    def __init__(self, cell_size, start_position, screen):
        super().__init__()
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

        if self.rect.left < 3:
            self.rect.left = self.image.get_width()//2
        if self.rect.right > self.SCREEN.get_width():
            self.rect.right = self.SCREEN.get_width() - self.image.get_width()//2
        if self.rect.top < 3:
            self.rect.top = self.image.get_height()//2
        if self.rect.bottom > self.SCREEN.get_height():
            self.rect.bottom = self.SCREEN.get_height() - self.image.get_height()//2
