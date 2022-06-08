# MazeWar Project - File 7
#
# Funcionamiento [ES]:
#
# 1. Sea C una lista de celdas, inicialmente vacía. Añade una celda a C, al azar.
#
# 2. Elija una celda de C, y Se dibuja al azar una pared en cualquier vecino no visitado de esa celda,
# añadiendo también ese vecino a C. Si no hay vecinos no visitados, elimine la celda de C.
#
# 3. Repite #2 hasta que C esté vacío.
#
# How it works [EN]:
#
# 1. Let C be a list of cells, initially empty. Add one cell to C, at random.
#
# 2. Choose a cell from C, and Randomly draw a wall in any unvisited neighbor of that cell,
# adding that neighbor to C as well. If there are no unvisited neighbors, delete the cell from C.
#
# 3. Repeat #2 until C is empty.
#

import pygame
import random
import time
from classes.grid import Grid, update


class GrowingTree:

    def __init__(self, grid):

        self.grid = grid
        self.cols = grid.cols
        self.rows = grid.rows
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

            active = []
            rx = random.randint(0, self.cols - 1)
            ry = random.randint(0, self.rows - 1)
            start_at = self.grid.cells[rx][ry]
            active.append(start_at)

            while len(active) > 0:

                current = active[-1]
                available_neighbours = []

                for cell in current.neighbours:
                    if len(cell.connections) == 0:
                        available_neighbours.append(cell)

                if len(available_neighbours) > 0:
                    neighbour = random.choice(available_neighbours)

                    neighbour.isCurrent = True
                    Grid.join_and_destroy_walls(current, neighbour)

                    # Debug Comment: To see the step-by-step process of the structure, comment out the following
                    # line of code (this generates a significant increase in execution time)
                    # self.grid.show(screen, True, True)
                    neighbour.isCurrent = False
                    active.append(neighbour)

                else:
                    active.remove(current)

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
