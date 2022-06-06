
from src.classes.cell import *
from src.ui.colors import *


class Grid:

    def __init__(self, rows, cols, new_cell_size, new_wall_size):

        self.rows = rows
        self.cols = cols
        self.cell_size = new_cell_size

        # Initialize cells
        self.cells = [[Cell(x, y, new_cell_size, new_wall_size) for y in range(rows)] for x in range(cols)]
        self.prepare_grid()

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

    def join_and_destroy_walls(cell_a, cell_b):

        if cell_a.isAvailable and cell_b.isAvailable:
            cell_a.visited = True
            cell_b.visited = True
            cell_a.connections.append(cell_b)
            cell_b.connections.append(cell_a)

            if cell_a.North == cell_b:
                cell_a.North, cell_b.South = None, None
            elif cell_a.South == cell_b:
                cell_a.South, cell_b.North = None, None
            elif cell_a.East == cell_b:
                cell_a.East, cell_b.West = None, None
            elif cell_a.West == cell_b:
                cell_a.West, cell_b.East = None, None

    def show(self, screen):

        for x in range(self.cols):
            for y in range(self.rows):
                if self.cells[x][y]:
                    self.cells[x][y].draw(screen, self.rows, self.cols)
