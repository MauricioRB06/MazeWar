# MazeWar Project - File 5

#
# Funcionamiento [ES]:
#
# Para cada celda de la cuadrícula, dibuja al azar una pared ya sea al norte o al oeste.
#
#
# How it works [EN]:
#
# For each grid cell, randomly draw a wall either north or west.
#

import pygame
import random
import time
from src.classes.grid import Grid, update


class BinaryTree:

    def __init__(self, grid):

        self.grid = grid
        self.isDone = False
        self.starting_node = grid.cells[0][random.randint(0, self.grid.rows - 1)]
        self.starting_node.isStartingNode = True
        self.end_node = grid.cells[random.randint(0, self.grid.cols - 1)][self.grid.rows - 1]
        self.end_node.isgoalNode = True
        self.path_color = "PURPLE"

        # self.executionTime = True

    def generate(self, screen):

        # startTime = time.time()

        if not self.isDone:
            for x in range(self.grid.cols):
                for y in range(self.grid.rows):

                    neighbours = []
                    self.grid.cells[x][y].isCurrent = True

                    # Check two neighbours
                    # check  for north and south Neighbours
                    if self.grid.cells[x][y].North is not None:
                        neighbours.append(self.grid.cells[x][y].North)
                    if self.grid.cells[x][y].East is not None:
                        neighbours.append(self.grid.cells[x][y].East)

                    # pick a random neighbour
                    # if any in the neighbours list
                    choice = None
                    if len(neighbours) > 0:
                        choice = random.choice(neighbours)

                    if choice is not None:
                        Grid.join_and_destroy_walls(self.grid.cells[x][y], choice)

                    # Debug Comment: To see the step-by-step process of the structure, comment out the following
                    # line of code (this generates a significant increase in execution time)
                    # self.grid.show(screen, True, True)
                    self.grid.cells[x][y].isCurrent = False

            self.isDone = True
            update(self)

        # endTime = time.time()
        self.grid.show(screen, True, True)

        # Debug Comment: To see the execution time of each structure, you can uncomment the following lines of code,
        # you must also uncomment the startTime and endTime variables.

        # if self.executionTime:
        #     print("Execution time of the Binary Tree algorithm: ", endTime - startTime)
        #     self.executionTime = False

    def show_maze(self, screen, heuristic, path):
        self.grid.show(screen, heuristic, path)
