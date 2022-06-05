
from gameSettings import *
from ui.colors import *
from ui.ui import *
from classes.recursiveBacktracker import RecursiveBacktracker
from classes.binaryTree import BinaryTree
from classes.grid import Grid
import os

# Initialize pygame
pygame.init()

# Initialize the Song
SONG = os.path.join(os.getcwd(),'resources/CORE.xm')
pygame.mixer.init()
pygame.mixer.music.load(SONG)
pygame.mixer.music.play(-1) #Play Music


# Initialize the screen
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60


recursive_backtracker = RecursiveBacktracker(Grid(rows, cols, cell_size, cell_wall_size))
binary_tree = BinaryTree(Grid(rows, cols, cell_size, cell_wall_size))

start = False
run = True
algorithms = True

PressEnter = TextUI("'ENTER' Para Generar el Laberinto con un Arbol binario", (width//2, (height//2)-20), white)
PressSpace = TextUI("SPACE' Para Generar el Laberinto con Pilas ", (width//2, (height//2)+20), white)
PressEnter.fontSize = 20

while run:
    # Set Caption and fps
    clock.tick(fps)
    frame_rate = int(clock.get_fps())
    pygame.display.set_caption(f"Maze War [ FPS: {frame_rate} ]")

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_RETURN:
                start = not start
                algorithms = True
            if event.key == pygame.K_SPACE:
                start = not start
                algorithms = False

    if start:

        # Python 3.10.4

        match algorithms:
            case True:
                binary_tree.generate(screen) 
            case False:
                recursive_backtracker.generate(screen)

        # Python 3.9.2

        #if algorithms:
        #    binary_tree.generate(screen)
        #else:
        #    recursive_backtracker.generate(screen)
        
    else:
        PressEnter.render(screen)
        PressSpace.render(screen)

    pygame.display.flip()

pygame.quit()
