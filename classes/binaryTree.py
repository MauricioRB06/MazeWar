
#
# Funcionamiento:
#
# Para cada celda de la cuadrícula, tallar al azar un pasaje ya sea al norte, o al oeste.
#

import pygame
from classes.grid import Grid
from ui.colors import *
import random
import time


class BinaryTree:

    def __init__(self, grid):
        self.grid = grid
        self.isDone = False
        self.CalculoGenerador = True
        self.starting_node = grid.cells[0][random.randint(0, self.grid.rows - 1)]
        self.starting_node.isStartingNode = True

        self.end_node = grid.cells[random.randint(0, self.grid.cols - 1)][self.grid.rows - 1]
        self.end_node.isgoalNode = True

    def generate(self, screen):

        inicio = time.time()

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

                    self.grid.show(screen)
                    self.grid.cells[x][y].isCurrent = False
                    pygame.display.flip()

            self.isDone = True

        fin = time.time()
        self.grid.show(screen)

        if self.CalculoGenerador:
            print("Tiempo de ejecución Arbol Binario: ", fin - inicio)
            self.CalculoGenerador = False
