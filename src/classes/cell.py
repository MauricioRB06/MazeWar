# MazeWar Project - File 9

import pygame
from src.ui.colors import *
from classes.heuristic import Heuristic
from src.Directory_Settings import cell_size

pygame.font.init()
text_font = pygame.font.SysFont("Arial", 8)


class Cell:

    def __init__(self, x, y, new_size, new_wall_size, cell_color=white, wall_color=black):

        self.x = x
        self.y = y

        self.cost = 0
        self.isStartingNode = False
        self.isgoalNode = False
        self.isCurrent = False
        self.isPath = False
        self.highlight = cell_color
        self.show_highlight = False
        self.size = new_size
        self.color = cell_color
        self.wall_color = wall_color
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

        # Heuristic
        self.textColor = (0, 0, 0)
        self.show_text = True

        # Cell Position
        self.rect = None

    def calculate_heuristic(self, rows, cols):
        h_distances = Heuristic(rows, cols)
        frontier = [self]
        while len(frontier) > 0:
            new_frontier = []
            for c in frontier:
                for cell in c.connections:
                    if h_distances.get_record(cell):
                        continue
                    val = 0 if h_distances.get_record(c) is None else h_distances.get_record(c)
                    h_distances.set_record(cell, val + 1)
                    new_frontier.append(cell)

            frontier = new_frontier
        h_distances.set_record(self, 0)
        return h_distances

    def draw(self, screen, rows, cols):

        x = self.x * self.size
        y = self.y * self.size

        if not self.visited or not self.isAvailable:
            pygame.draw.rect(screen, black, [x, y, self.size, self.size])
        else:
            color = self.color
            if self.isStartingNode:
                color = yellow
            if self.isCurrent:
                color = blue
            elif self.isgoalNode:
                color = green
            pygame.draw.rect(screen, color, [x, y, self.size, self.size])

            if self.show_highlight:
                pygame.draw.rect(screen, self.highlight, [x, y, self.size, self.size])

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

        if self.show_text:
            text_surface = text_font.render(str(int(self.cost)), True, self.textColor)
            text_rect = text_surface.get_rect(center=(x + self.size//2, y + self.size//2))
            self.rect = text_rect.center
            screen.blit(text_surface, text_rect)
