
from ui.colors import *
from ui.ui import *
from classes.a_recursiveBacktracker import RecursiveBacktracker
from classes.a_binaryTree import BinaryTree
from classes.a_growingTree import GrowingTree
from classes.a_prims import Prims
from classes.grid import Grid
import time

# Initialize pygame
pygame.init()

# Initialize the screen
screen_resolution = 600
screen = pygame.display.set_mode((screen_resolution, screen_resolution))
clock = pygame.time.Clock()
fps = 60

# Set Testing Variables
cell_size = 20
cell_wall_size = cell_size//4
rows = screen.get_width()//cell_size
cols = screen.get_height()//cell_size

recursive_backtracker = RecursiveBacktracker(Grid(rows, cols, cell_size, cell_wall_size))
binary_tree = BinaryTree(Grid(rows, cols, cell_size, cell_wall_size))
growing_tree = GrowingTree(Grid(rows, cols, cell_size, cell_wall_size))
prims = Prims(Grid(rows, cols, cell_size, cell_wall_size))

start = False
run = True
algorithm = None

Press1 = TextUI("'1' RecursiveBacktracker Algorithm", (screen_resolution//2, (screen_resolution//2)-60), white)
Press2 = TextUI("'2' BinaryTree Algorithm", (screen_resolution//2, (screen_resolution//2)-20), white)
Press3 = TextUI("'3' GrowingTree Algorithm", (screen_resolution//2, (screen_resolution//2)+20), white)
Press4 = TextUI("'4' Prims Algorithm", (screen_resolution//2, (screen_resolution//2)+60), white)
Press1.fontSize = 30
Press2.fontSize = 30
Press3.fontSize = 30
Press4.fontSize = 30

while run:

    # Set Caption and fps
    clock.tick(fps)
    frame_rate = int(clock.get_fps())
    pygame.display.set_caption(f"Maze War [ Testing Algorithms ]")

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_1:
                start = not start
                algorithm = 1
            if event.key == pygame.K_2:
                start = not start
                algorithm = 2
            if event.key == pygame.K_3:
                start = not start
                algorithm = 3
            if event.key == pygame.K_4:
                start = not start
                algorithm = 4

    if start:

        print("--------------------")

        match algorithm:

            case 1:
                start_time = time.time()
                recursive_backtracker.generate(screen)
                end_time = time.time()
                print("Recursive Backtracker Time: ", end_time - start_time)

            case 2:
                start_time = time.time()
                binary_tree.generate(screen)
                end_time = time.time()
                print("Binary Tree Time: ", end_time - start_time)

            case 3:
                start_time = time.time()
                growing_tree.generate(screen)
                end_time = time.time()
                print("Growing Tree Time: ", end_time - start_time)

            case 4:
                start_time = time.time()
                prims.generate(screen)
                end_time = time.time()
                print("Prims Time: ", end_time - start_time)

        print("Resolution: ", screen_resolution, " x ", screen_resolution)
        print("Cell Size: ", cell_size)
        print("Cell Amount: ", (screen_resolution // cell_size) * (screen_resolution // cell_size), " Cells")
        print("--------------------")
        screen.fill((0, 0, 0))
        start = not start

    else:
        Press1.render(screen)
        Press2.render(screen)
        Press3.render(screen)
        Press4.render(screen)

    pygame.display.flip()

pygame.quit()
