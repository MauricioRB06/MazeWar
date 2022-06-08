# MazeWar Project - File 8
#
# Funcionamiento [ES]:
#
# 1. Se elige una celda arbitraria de G (la cuadrícula), y se añade a un conjunto V (inicialmente vacío).
#
# 2. Se elige la arista con el peso más pequeño de G, que conecta un vértice en V con otra celda que no está en V.
#
# 3. Se añade esa arista al árbol de expansión mínimo y la otra celda de la arista a V.
#
# 4. Repita los pasos 2 y 3 hasta que V incluya todos los vértices de G.
#
# How it works [EN]:
#
# 1. Choose an arbitrary cell from G (the grid) and add it to some (initially empty) set V.
#
# 2. Choose the edge with the smallest weight from G, that connects a vertex in V with another cell not in V.
#
# 3. Add that edge to the minimal spanning tree, and the edge’s other cell to V.
#
# 4. Repeat steps 2 and 3 until V includes every vertex in G.
#

import pygame
import random
import time
from classes.grid import Grid, update


class Prims:

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
            rx = random.randint(0, self.cols-1)
            ry = random.randint(0, self.rows-1)
            start_at = self.grid.cells[rx][ry]
            active.append(start_at)

            while len(active) > 0:

                cell = random.choice(active)
                available_neighbours = []

                for c in cell.neighbours:
                    if len(c.connections) == 0:
                        available_neighbours.append(c)

                if len(available_neighbours) > 0:
                    neighbour = random.choice(available_neighbours)

                    neighbour.isCurrent = True
                    Grid.join_and_destroy_walls(cell, neighbour)

                    # Debug Comment: To see the step-by-step process of the structure, comment out the following
                    # line of code (this generates a significant increase in execution time)
                    # self.grid.show(screen, True, True)
                    neighbour.isCurrent = False
                    active.append(neighbour)

                else:
                    active.remove(cell)

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
