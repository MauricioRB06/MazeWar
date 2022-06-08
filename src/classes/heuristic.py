# MazeWar Project - File 11

class Heuristic:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells_record = [[None for y in range(rows)] for x in range(cols)]

    def set_record(self, cell, distance):
        self.cells_record[cell.x][cell.y] = distance

    def get_farthest(self, start, grid):
        max_distance = 0
        farthest= start
        for x in range(self.cols):
            for y in range(self.rows):
                dist = self.cells_record[x][y] if self.cells_record[x][y] else 0
                cell = grid.cells[x][y]
                if dist > max_distance:
                    farthest = cell
                    max_distance = dist

        return farthest, max_distance

    def backtrack_path(self, goal, start):
        current = goal
        path_track = Heuristic(self.rows, self.cols)
        path_track.set_record(current, self.get_record(current))
        max_counter = self.rows * self.cols
        counter = 0
        while current != start:
            for cell in current.connections:
                if self.get_record(cell) < self.get_record(current):
                    path_track.set_record(cell, self.get_record(cell))
                    current = cell
            counter += 1
            if counter > max_counter:
                break
        return path_track

    def get_record(self, cell):
        return self.cells_record[cell.x][cell.y]
