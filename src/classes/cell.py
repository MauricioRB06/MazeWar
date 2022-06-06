
import pygame
from src.ui.colors import *


class Cell:

    def __init__(self, x, y, new_size, new_wall_size):

        self.x = x
        self.y = y

        self.isgoalNode = False
        self.isStartingNode = False

        self.size = new_size
        self.color = white
        self.wall_color = black
        self.wall_thickness = new_wall_size
        self.visited = False
        self.connections = []
        self.neighbours = []
        self.isAvailable = True

        # Walls -- neighbours
        self.North = None
        self.South = None
        self.East = None
        self.West = None

    def draw(self, screen, rows, cols):

        x = self.x * self.size
        y = self.y * self.size

        if not self.visited or not self.isAvailable:
            pygame.draw.rect(screen, black, [x, y, self.size, self.size])
        else:
            color = self.color
            if self.isStartingNode:
                color = yellow
            elif self.isgoalNode:
                color = green
            pygame.draw.rect(screen, color, [x, y, self.size, self.size])

        if self.North is not None or self.y - 1 < 0:
            A = (x, y)
            B = (x + self.size, y)
            pygame.draw.line(screen, self.wall_color, A, B, self.wall_thickness)

        if self.South is not None or self.y + 1 >= rows:
            A = (x, y + self.size)
            B = (x + self.size, y + self.size)
            pygame.draw.line(screen, self.wall_color, A, B, self.wall_thickness)

        if self.East is not None or self.x + 1 >= cols:
            A = (x + self.size, y)
            B = (x + self.size, y + self.size)
            pygame.draw.line(screen, self.wall_color, A, B, self.wall_thickness)

        if self.West is not None or self.x - 1 < 0:
            A = (x, y)
            B = (x, y + self.size)
            pygame.draw.line(screen, self.wall_color, A, B, self.wall_thickness)
