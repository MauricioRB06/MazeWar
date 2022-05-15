
#
# Funcionamiento:
#
# 1. Se genera un punto aleatorio en la parte superior y se inicia en este punto de partida.
#
# 2. Se dibuja al azar una pared en ese punto y se traza un camino hasta una celda adyacente, pero solo si la celda
# adyacente no ha sido visitada todavía. Esta se convierte en la nueva celda actual.
#
# 3. Si se han visitado todas las celdas adyacentes, se retrocede hasta la última celda que tenga vecinos sin visitar
# y se repite el proceso.
#
# 4. El algoritmo termina cuando el proceso ha retrocedido hasta el punto de partida, lo que significa que todas las
# celdas ya fueron visitadas.
#

import pygame
from classes.grid import Grid
from ui.colors import *
import random
import time


class RecursiveBacktracker:

    def __init__(self, grid):
        self.grid = grid
        self.rows = grid.rows
        self.cols = grid.cols
        self.CalculoGenerador = True
        self.starting_node = None
        self.end_node = None

        if type(self.grid) == Grid:

            self.starting_node = grid.cells[random.randint(0, self.cols-1)][0]
            self.starting_node.isStartingNode = True

            self.end_node = grid.cells[random.randint(0, self.cols-1)][self.rows-1]
            self.end_node.isgoalNode = True

    def generate(self, screen):

        inicio = time.time()

        stack = []

        random_x = random.randint(0, self.cols - 1)
        random_y = random.randint(0, self.rows - 1)
        initial_cell = self.grid.cells[random_x][random_y]
        stack.append(initial_cell)

        while len(stack) > 0:

            current = stack[-1]
            neighbours = [cell for cell in current.neighbours if len(cell.connections) == 0]

            if len(neighbours) == 0:
                stack.pop()

            else:
                neighbour = random.choice(neighbours)
                Grid.join_and_destroy_walls(current, neighbour)
                neighbour.isCurrent = True
                pygame.display.flip()
                neighbour.isCurrent = False

                stack.append(neighbour)
                # self.grid.show(screen)

        fin = time.time()
        self.grid.show(screen)

        if self.CalculoGenerador:
            print("Tiempo de ejecución Retroceso recursivo: ", fin - inicio)
            self.CalculoGenerador = False
