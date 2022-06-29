
import pygame
from pygame.sprite import Sprite


class EnemyCollider(Sprite):
    def __init__(self, collider_rect):
        super().__init__()
        self.rect = collider_rect
