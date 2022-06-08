# MazeWar Project - File 6
#
# Funcionamiento [ES]:
#
# 1. Se selecciona un punto de la cuadrícula y se inicia en este punto.
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
#
# How it works [EN]:
#
# 1. You select a point on the grid and start at this point.
#
# 2. A wall is randomly drawn at that point and a path is traced to an adjacent cell, but only if the adjacent cell
# has not yet been visited. This becomes the new current cell.
#
# 3. If all adjacent cells have been visited, backtrack to the last cell with unvisited neighbors and repeat the
# process.
#
# 4. The algorithm ends when the process has backtracked to the starting point, which means that all cells have
# been visited. cells have already been visited.
#

import pygame
import random
import time
from src.classes.grid import Grid, update


class RecursiveBacktracker:

    def __init__(self, grid):
        self.grid = grid
        self.rows = grid.rows
        self.cols = grid.cols
        self.isDone = False
        self.starting_node = None
        self.end_node = None
        self.path_color = "PURPLE"

        if type(self.grid) == Grid:

            self.starting_node = grid.cells[0][random.randint(0, self.grid.rows - 1)]
            self.starting_node.isStartingNode = True
            self.end_node = grid.cells[random.randint(0, self.grid.cols - 1)][self.grid.rows - 1]
            self.end_node.isgoalNode = True

    def generate(self, screen):

        # startTime = time.time()

        if not self.isDone:

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

                    # Debug Comment: To see the step-by-step process of the structure, comment out the following
                    # line of code (this generates a significant increase in execution time)
                    # self.grid.show(screen, True, True)
                    stack.append(neighbour)

            self.isDone = True

            update(self)

        # endTime = time.time()
        self.grid.show(screen, True, True)

        # Debug Comment: To see the execution time of each structure, you can uncomment the following lines of code,
        # you must also uncomment the startTime and endTime variables.

        # if self.executionTime:
        #     print("Execution time of the Recursive Backtracker algorithm: ", endTime - startTime)
        #     self.executionTime = False

    def show_maze(self, screen, heuristic, path):
        self.grid.show(screen, heuristic, path)
