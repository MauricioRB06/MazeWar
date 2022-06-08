# MazeWar Project - File 3

# Labyrinth Color
white = (255, 255, 255)
black = (0, 0, 0)

# Points Color
yellow = (255, 255, 0)
green = (0, 255, 0)

# Player Color
blue = (0, 0, 255)

# Enemy Colors
red = (255, 10, 0)
pink = (255, 0, 236)
orange = (255, 120, 0)

# Path Color
purple = (42, 8, 170)


class GridColor:

    heuristics = None
    farthest = None
    max_distance = None

    def __init__(self, color_str="RED"):
        self.color = color_str

    def distances(self, heuristics, start, grid):
        self.heuristics = heuristics
        self.farthest, self.max_distance = self.heuristics.get_farthest(start, grid)

    def update_color(self, cell):
        val = self.heuristics.get_record(cell)
        distance = 0 if val is None else val
        intensity = (self.max_distance - distance) / self.max_distance
        dark = min(int(255 * intensity), 255)
        bright = min(int(128 + (127 * intensity)), 255)

        colors = {
            "RED": (bright, dark, dark),
            "BLUE": (dark, dark, bright),
            "GREEN": (dark, bright, dark),
            "YELLOW": (bright, bright, dark),
            "CYAN": (dark, bright, bright),
            "PURPLE": (bright, dark, bright),
            "PURPLE_E": (bright, dark, bright),
            "GREEN_E": (0, bright, 0),
            "BLUE_E": (0, 0, bright),
            "RED_E": (bright, 0, 0)
        }

        return tuple(colors[self.color])
