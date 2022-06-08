# MazeWar Project - File 1
# Pygame [ https://www.pygame.org/docs/ ]
# OS [ https://docs.python.org/3/library/os.html ]

from src.ui.colors import *
from src.ui.ui import *
from src.classes.a_binaryTree import BinaryTree
from src.classes.a_recursiveBacktracker import RecursiveBacktracker
from src.classes.a_growingTree import GrowingTree
from src.classes.a_prims import Prims
from src.classes.grid import Grid

from os.path import join
from time import sleep

from classes.game_loop import game_loop

import pygame
from pygame import Rect, mouse, display, MOUSEBUTTONDOWN
from pygame.font import Font
from pygame.image import load
from pygame.mixer import music
from pygame.transform import scale

from Directory_Settings import DEFAULT_SCREEN, CLOCK, FPS, f_music, sfxButtonClick, game_folder, imgCursor, \
     imgCredits, imgHowToPlay, imgLoadingScreen, imgMazeReady, bgMainMenu, bgGameOver, bgCredits, bgHowToPlay, \
     bgSettings, bgAlgorithms, bgCellSize, bgVisualMode, ftPause, ftCredits, cell_size, cell_wall_size, rows, cols

SCREEN = DEFAULT_SCREEN

pygame.init()
pygame.mixer.init()
menuFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height()//16)
algorithmFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height()//20)
cellFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height()//5)
mouse.set_visible(False)
game_on = True
sfxButtonClick.set_volume(0.5)

maze_cell_size = cell_size
maze_wall_size = cell_wall_size
maze_rows = rows
maze_cols = cols

binary_tree = BinaryTree(Grid(maze_rows, maze_cols, maze_cell_size, maze_wall_size, 0))
recursive_backtracker = RecursiveBacktracker(Grid(maze_rows, maze_cols, maze_cell_size, maze_wall_size, 0))
growing_tree = GrowingTree(Grid(maze_rows, maze_cols, maze_cell_size, maze_wall_size, 0))
prims = Prims(Grid(maze_rows, maze_cols, maze_cell_size, maze_wall_size, 0))


def buttons_print(button, name, font):

    if button.collidepoint(mouse.get_pos()):
        text = font.render(name, True, (182, 244, 7))
        SCREEN.blit(text, (button.x + (button.width + 10 - text.get_width()) / 2,
                           button.y + (button.height - 3 - text.get_height()) / 2))
    else:
        text = font.render(name.lower(), True, (245, 245, 245))
        SCREEN.blit(text, (button.x + (button.width + 10 - text.get_width()) / 2,
                           button.y + (button.height - 3 - text.get_height()) / 2))


def main_menu():

    global SCREEN
    global menuFont

    button_play = Rect((SCREEN.get_width()//4), SCREEN.get_height()//3, SCREEN.get_width()//8, 42)
    button_settings = Rect((SCREEN.get_width()//3), SCREEN.get_height() // 2.23, SCREEN.get_width() // 8, 42)
    button_how_to_play = Rect((SCREEN.get_width()//6), SCREEN.get_height()//1.73, SCREEN.get_width()//2, 42)
    button_credits = Rect((SCREEN.get_width()//4), SCREEN.get_height()//1.44, SCREEN.get_width()//3.65, 42)
    button_exit = Rect((SCREEN.get_width()//4), SCREEN.get_height()//1.25, SCREEN.get_width()//8.2, 42)

    music.load(join(f_music, 'Menu_Music.ogg'))
    music.set_volume(0.15)
    music.play(loops=-1)

    while game_on:

        CLOCK.tick(FPS)
        mouse_pos = mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if button_play.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    cell = set_cell_size()
                    algorithm = set_algorithm()
                    mode = set_mode()
                    sleep(1)
                    maze = load_game_screen(cell, algorithm, mode)
                    game_loop(cell, maze, SCREEN, menuFont)
                    music.load(join(f_music, 'Menu_Music.ogg'))
                    music.set_volume(0.15)
                    music.play(loops=-1)

                if button_settings.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    settings()
                    button_play = Rect((SCREEN.get_width() // 4), SCREEN.get_height() // 3, SCREEN.get_width() // 8, 42)
                    button_settings = Rect((SCREEN.get_width() // 3), SCREEN.get_height() // 2.23, SCREEN.get_width() // 8, 42)
                    button_how_to_play = Rect((SCREEN.get_width() // 6), SCREEN.get_height() // 1.73, SCREEN.get_width() // 2, 42)
                    button_credits = Rect((SCREEN.get_width() // 4), SCREEN.get_height() // 1.44, SCREEN.get_width() // 3.65, 42)
                    button_exit = Rect((SCREEN.get_width() // 4), SCREEN.get_height() // 1.25, SCREEN.get_width() // 8.2, 42)

                if button_how_to_play.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    how_to_play_menu()

                if button_credits.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    music.stop()
                    credits_menu()
                    music.load(join(f_music, 'Menu_Music.ogg'))
                    music.set_volume(0.15)
                    music.play(loops=-1)

                if button_exit.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    sleep(1)
                    exit()

        SCREEN.blit(pygame.transform.scale(bgMainMenu, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))

        buttons_print(button_play, 'PLAY', menuFont)
        buttons_print(button_settings, 'SETTINGS', menuFont)
        buttons_print(button_how_to_play, 'CONTROLS', menuFont)
        buttons_print(button_credits, 'CREDITS', menuFont)
        buttons_print(button_exit, 'EXIT', menuFont)

        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))
        display.update()


def load_game_screen(new_cell_size, new_algorithm, new_mode):

    global binary_tree
    global recursive_backtracker
    global growing_tree
    global prims

    global maze_cell_size
    global maze_wall_size
    global maze_rows
    global maze_cols

    mouse.set_visible(False)
    music.stop()
    spaceToStart = True

    maze_cell_size = new_cell_size
    maze_wall_size = maze_cell_size//4
    maze_rows = SCREEN.get_width()//maze_cell_size
    maze_cols = SCREEN.get_height()//maze_cell_size

    SCREEN.blit(pygame.transform.scale(imgLoadingScreen, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
    display.update()

    match new_algorithm:

        case 1:
            recursive_backtracker = RecursiveBacktracker(Grid(maze_rows, maze_cols, maze_cell_size, maze_wall_size, new_mode))
            recursive_backtracker.generate(SCREEN)

        case 2:
            binary_tree = BinaryTree(Grid(maze_rows, maze_cols, maze_cell_size, maze_wall_size, new_mode))
            binary_tree.generate(SCREEN)

        case 3:
            growing_tree = GrowingTree(Grid(maze_rows, maze_cols, maze_cell_size, maze_wall_size, new_mode))
            growing_tree.generate(SCREEN)

        case 4:
            prims = Prims(Grid(maze_rows, maze_cols, maze_cell_size, maze_wall_size, new_mode))
            prims.generate(SCREEN)

    sleep(2)

    while spaceToStart:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    spaceToStart = False

        SCREEN.blit(pygame.transform.scale(imgMazeReady, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
        display.update()

    match new_algorithm:
        case 1:
            return recursive_backtracker
        case 2:
            return binary_tree
        case 3:
            return growing_tree
        case 4:
            return prims


def set_cell_size():

    cellSize = 0
    selection = True

    button_size1 = Rect((SCREEN.get_width()//4), SCREEN.get_height()//2.4, SCREEN.get_width()//16, SCREEN.get_height()//20)
    button_size2 = Rect((SCREEN.get_width()//2.1), SCREEN.get_height()//2.4, SCREEN.get_width()//16, SCREEN.get_height()//20)
    button_size3 = Rect((SCREEN.get_width()//1.4), SCREEN.get_height()//2.4, SCREEN.get_width()//16, SCREEN.get_height()//20)

    button_size4 = Rect((SCREEN.get_width()//4), SCREEN.get_height()//1.5, SCREEN.get_width()//16, SCREEN.get_height()//20)
    button_size5 = Rect((SCREEN.get_width()//2.1), SCREEN.get_height()//1.5, SCREEN.get_width()//16, SCREEN.get_height()//20)
    button_size6 = Rect((SCREEN.get_width()//1.4), SCREEN.get_height()//1.5, SCREEN.get_width()//16, SCREEN.get_height()//20)

    while selection:

        mouse_pos = mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if button_size1.collidepoint(mouse.get_pos()):

                    match SCREEN.get_width():
                        case 600:
                            cellSize = 10
                        case 800:
                            cellSize = 10
                        case 1000:
                            cellSize = 15
                        case 2000:
                            cellSize = 20

                    sfxButtonClick.play()
                    selection = False

                if button_size2.collidepoint(mouse.get_pos()):

                    match SCREEN.get_width():
                        case 600:
                            cellSize = 15
                        case 800:
                            cellSize = 15
                        case 1000:
                            cellSize = 20
                        case 2000:
                            cellSize = 25

                    sfxButtonClick.play()
                    selection = False

                if button_size3.collidepoint(mouse.get_pos()):

                    match SCREEN.get_width():
                        case 600:
                            cellSize = 20
                        case 800:
                            cellSize = 20
                        case 1000:
                            cellSize = 25
                        case 2000:
                            cellSize = 30

                    sfxButtonClick.play()
                    selection = False

                if button_size4.collidepoint(mouse.get_pos()):

                    match SCREEN.get_width():
                        case 600:
                            cellSize = 25
                        case 800:
                            cellSize = 25
                        case 1000:
                            cellSize = 30
                        case 2000:
                            cellSize = 40

                    sfxButtonClick.play()
                    sleep(0.5)
                    selection = False

                if button_size5.collidepoint(mouse.get_pos()):

                    match SCREEN.get_width():
                        case 600:
                            cellSize = 30
                        case 800:
                            cellSize = 30
                        case 1000:
                            cellSize = 40
                        case 2000:
                            cellSize = 50

                    sfxButtonClick.play()
                    sleep(0.5)
                    selection = False

                if button_size6.collidepoint(mouse.get_pos()):

                    match SCREEN.get_width():
                        case 600:
                            cellSize = 40
                        case 800:
                            cellSize = 40
                        case 1000:
                            cellSize = 50
                        case 2000:
                            cellSize = 60

                    sfxButtonClick.play()
                    selection = False

        SCREEN.blit(pygame.transform.scale(bgCellSize, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))

        buttons_print(button_size1, 'A', cellFont)
        buttons_print(button_size2, 'B', cellFont)
        buttons_print(button_size3, 'C', cellFont)
        buttons_print(button_size4, 'D', cellFont)
        buttons_print(button_size5, 'E', cellFont)
        buttons_print(button_size6, 'F', cellFont)

        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))

        display.update()

    return cellSize


def set_algorithm():

    algorithm = 0
    selection = True

    button_algorithm1 = Rect((SCREEN.get_width()//3.75), SCREEN.get_height()//3.5, SCREEN.get_width()//2, SCREEN.get_height()//20)
    button_algorithm2 = Rect((SCREEN.get_width()//3.75), SCREEN.get_height()//2.1, SCREEN.get_width()//2, SCREEN.get_height()//20)
    button_algorithm3 = Rect((SCREEN.get_width()//3.75), SCREEN.get_height()//1.55, SCREEN.get_width()//2, SCREEN.get_height()//20)
    button_algorithm4 = Rect((SCREEN.get_width()//3.75), SCREEN.get_height()//1.25, SCREEN.get_width()//2, SCREEN.get_height()//20)

    while selection:

        mouse_pos = mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if button_algorithm1.collidepoint(mouse.get_pos()):
                    algorithm = 1
                    sfxButtonClick.play()
                    selection = False

                if button_algorithm2.collidepoint(mouse.get_pos()):
                    algorithm = 2
                    sfxButtonClick.play()
                    selection = False

                if button_algorithm3.collidepoint(mouse.get_pos()):
                    algorithm = 3
                    sfxButtonClick.play()
                    selection = False

                if button_algorithm4.collidepoint(mouse.get_pos()):
                    algorithm = 4
                    sfxButtonClick.play()
                    sleep(0.5)
                    selection = False

        SCREEN.blit(pygame.transform.scale(bgAlgorithms, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))

        buttons_print(button_algorithm1, 'RECURSIVE BACKTRACKER', algorithmFont)
        buttons_print(button_algorithm2, 'BINARY TREE', menuFont)
        buttons_print(button_algorithm3, 'GROWING TREE', menuFont)
        buttons_print(button_algorithm4, 'PRIMS', menuFont)

        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))
        display.update()

    return algorithm


def set_mode():

    mode = 0
    selection = True

    button_mode1 = Rect((SCREEN.get_width()//3.75), SCREEN.get_height()//2.3, SCREEN.get_width()//2, SCREEN.get_height()//20)
    button_mode2 = Rect((SCREEN.get_width()//3.75), SCREEN.get_height()//1.5, SCREEN.get_width()//2, SCREEN.get_height()//20)

    while selection:

        mouse_pos = mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if button_mode1.collidepoint(mouse.get_pos()):
                    mode = 0
                    sfxButtonClick.play()
                    selection = False

                if button_mode2.collidepoint(mouse.get_pos()):
                    mode = 1
                    sfxButtonClick.play()
                    selection = False

        SCREEN.blit(pygame.transform.scale(bgVisualMode, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))

        buttons_print(button_mode1, 'LIGHT', cellFont)
        buttons_print(button_mode2, 'DARK', cellFont)

        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))
        display.update()

    return mode


def settings():

    global SCREEN
    global menuFont
    global algorithmFont
    global cellFont
    selection = True

    button_apply = Rect((SCREEN.get_width()//2.3), SCREEN.get_height()//1.12, SCREEN.get_width()//8, 42)
    button_res0 = Rect((SCREEN.get_width()//3.9), SCREEN.get_height() // 2.7, SCREEN.get_width()//2, 30)
    button_res1 = Rect((SCREEN.get_width()//3.9), SCREEN.get_height() // 2.05, SCREEN.get_width()//2, 30)
    button_res2 = Rect((SCREEN.get_width()//4), SCREEN.get_height() // 1.61, SCREEN.get_width()//2, 30)
    button_res3 = Rect((SCREEN.get_width()//4), SCREEN.get_height() // 1.35, SCREEN.get_width()//2, 30)

    while selection:

        mouse_pos = mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if button_apply.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    selection = False

                if button_res0.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    SCREEN = display.set_mode((600, 600))
                    menuFont = Font(join(game_folder, '04B30.ttf'), SCREEN.get_height() // 16)
                    algorithmFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height() // 20)
                    cellFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height() // 5)

                if button_res1.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    SCREEN = display.set_mode((800, 800))
                    menuFont = Font(join(game_folder, '04B30.ttf'), SCREEN.get_height() // 16)
                    algorithmFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height() // 20)
                    cellFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height() // 5)

                if button_res2.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    SCREEN = display.set_mode((1000, 1000))
                    menuFont = Font(join(game_folder, '04B30.ttf'), SCREEN.get_height() // 16)
                    algorithmFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height() // 20)
                    cellFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height() // 5)

                if button_res3.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    SCREEN = display.set_mode((2000, 2000))
                    menuFont = Font(join(game_folder, '04B30.ttf'), SCREEN.get_height() // 16)
                    algorithmFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height() // 20)
                    cellFont = Font(join(game_folder, '04B30.ttf'), DEFAULT_SCREEN.get_height() // 5)

                button_apply = Rect((SCREEN.get_width() // 2.3), SCREEN.get_height() // 1.12, SCREEN.get_width() // 8, 42)
                button_res0 = Rect((SCREEN.get_width() // 3.9), SCREEN.get_height() // 2.7, SCREEN.get_width() // 2, 30)
                button_res1 = Rect((SCREEN.get_width() // 3.9), SCREEN.get_height() // 2.05, SCREEN.get_width() // 2, 30)
                button_res2 = Rect((SCREEN.get_width() // 4), SCREEN.get_height() // 1.61, SCREEN.get_width() // 2, 30)
                button_res3 = Rect((SCREEN.get_width() // 4), SCREEN.get_height() // 1.35, SCREEN.get_width() // 2, 30)

        SCREEN.blit(pygame.transform.scale(bgSettings, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))

        buttons_print(button_apply, 'APPLY', menuFont)
        buttons_print(button_res0, '600 x 600', menuFont)
        buttons_print(button_res1, '800 x 800', menuFont)
        buttons_print(button_res2, '1000 x 1000', menuFont)
        buttons_print(button_res3, '2000 x 2000', menuFont)

        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))

        display.update()


def how_to_play_menu():

    check_how_to_play = True
    button_back = Rect((SCREEN.get_width()//1.3), SCREEN.get_height()//1.16, SCREEN.get_width()//20, 42)

    while check_how_to_play:

        mouse_pos = mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_back.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    check_how_to_play = False

        SCREEN.blit(pygame.transform.scale(bgHowToPlay, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
        SCREEN.blit(pygame.transform.scale(imgHowToPlay, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))

        buttons_print(button_back, 'BACK', menuFont)
        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))

        display.update()


def credits_menu():

    music.load(join(f_music, 'Credits_Music.ogg'))
    music.set_volume(0.5)
    music.play(loops=-1)
    check_credits_menu = True

    y_mov = 0
    button_back = Rect((SCREEN.get_width()//2.1), SCREEN.get_height()//1.12, SCREEN.get_width()//20, 42)

    while check_credits_menu:

        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_back.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    check_credits_menu = False

        SCREEN.blit(pygame.transform.scale(bgCredits, (SCREEN.get_width(), SCREEN.get_width())), (0, 0))

        y_move = y_mov % pygame.transform.scale(imgCredits, (SCREEN.get_height(), SCREEN.get_height() * 5)).get_rect().height
        SCREEN.blit(pygame.transform.scale(imgCredits, (SCREEN.get_height(), SCREEN.get_height() * 5)),
                    (0, (y_move - pygame.transform.scale(imgCredits, (SCREEN.get_height(), SCREEN.get_height() * 5)).get_rect().height)))

        if y_move < SCREEN.get_height():
            SCREEN.blit(imgCredits, (0, y_move))

        if SCREEN.get_width() == 2000:
            y_mov -= 3
        elif SCREEN.get_width() == 1000:
            y_mov -= 1
        elif SCREEN.get_width() == 800:
            y_mov -= .8
        elif SCREEN.get_width() == 600:
            y_mov -= .6

        SCREEN.blit(pygame.transform.scale(ftCredits, (SCREEN.get_width(), SCREEN.get_width())), (0, 0))
        buttons_print(button_back, 'BACK', menuFont)
        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))

        display.update()

    music.stop()


main_menu()
