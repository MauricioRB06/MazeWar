# MazeWar Project - File 10

from classes.cell import *
from ui.colors import *
from ui.colors import GridColor
import random


class Grid:

    def __init__(self, rows, cols, new_cell_size, new_wall_size, mode):

        self.rows = rows
        self.cols = cols
        self.cell_size = new_cell_size

        # Initialize cells
        if mode == 0:
            self.cells = [[Cell(x, y, new_cell_size, new_wall_size, white, black) for y in range(rows)] for x in range(cols)]
        else:
            self.cells = [[Cell(x, y, new_cell_size, new_wall_size, black, white) for y in range(rows)] for x in range(cols)]

        self.prepare_grid()
        self.heuristics = None
        self.path_color = orange
        self.isSorted = False
        self.path = {}
        self.path_values = []

    def prepare_grid(self):
        for x in range(self.cols):
            for y in range(self.rows):
                if self.cells[x][y]:
                    self.cells[x][y].neighbours = []
                    # East neighbour cell
                    if x+1 < self.cols and self.cells[x+1][y]:
                        self.cells[x][y].East = self.cells[x+1][y]
                        self.cells[x][y].neighbours.append(self.cells[x+1][y])
                    # West neighbour cell
                    if x-1 >= 0 and self.cells[x-1][y]:
                        self.cells[x][y].West = self.cells[x-1][y]
                        self.cells[x][y].neighbours.append(self.cells[x-1][y])

                    # North neighbour cell
                    if y-1 >= 0 and self.cells[x][y-1]:
                        self.cells[x][y].North = self.cells[x][y-1]
                        self.cells[x][y].neighbours.append(self.cells[x][y-1])
                    # South neighbour cell
                    if y+1 < self.rows and self.cells[x][y+1]:
                        self.cells[x][y].South = self.cells[x][y+1]
                        self.cells[x][y].neighbours.append(self.cells[x][y+1])

    def join_and_destroy_walls(a, b):

        if a.isAvailable and b.isAvailable:
            a.visited = True
            b.visited = True
            a.connections.append(b)
            b.connections.append(a)

            if a.North == b:
                a.North, b.South = None, None
            elif a.South == b:
                a.South, b.North = None, None
            elif a.East == b:
                a.East, b.West = None, None
            elif a.West == b:
                a.West, b.East = None, None

    def show(self, screen, show_heuristic: bool = False, show_color_map: bool = False):

        for x in range(self.cols):
            for y in range(self.rows):
                if self.cells[x][y]:
                    self.cells[x][y].show_text = show_heuristic
                    self.cells[x][y].show_highlight = show_color_map
                    self.cells[x][y].draw(screen, self.rows, self.cols)


def update(self):

    # Calculate the step of each cell from the starting node
    # it's going to initialize a grid that store the cost of each cell
    # from the starting node

    h_distances = self.starting_node.calculate_heuristic(self.grid.rows, self.grid.cols)
    self.grid.heuristics = h_distances

    for x in range(len(self.grid.cells)):
        for y in range(len(self.grid.cells[x])):
            if self.grid.cells[x][y]:
                self.grid.cells[x][y].cost = 0 if self.grid.heuristics.cells_record[x][y] is None else self.grid.heuristics.cells_record[x][y]

    # get the path from the goad node to the starting node
    shortest_path = h_distances.backtrack_path(self.end_node, self.starting_node)

    for x in range(self.grid.cols):
        for y in range(self.grid.rows):
            if self.grid.cells[x][y]:
                # check if the cell is in the path grid
                # If it is then set it as path
                if shortest_path.get_record(self.grid.cells[x][y]):
                    self.grid.cells[x][y].isPath = True

    colorGridShortestPath = GridColor(self.path_color)
    colorGridShortestPath.distances(shortest_path, self.starting_node, self.grid)

    for x in range(self.grid.cols):
        for y in range(self.grid.rows):
            if self.grid.cells[x][y]:
                self.grid.cells[x][y].highlight = colorGridShortestPath.update_color(self.grid.cells[x][y])

    self.shortest_path = shortest_path
