"""
from src.gameSettings import *
from src.ui.colors import *
from src.ui.ui import *
from src.classes.recursiveBacktracker import RecursiveBacktracker
from src.classes.binaryTree import BinaryTree
from src.classes.grid import Grid

# Initialize pygame
pygame.init()

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
    pygame.display.set_caption(f"Maze War [ Version Alpha 0.1 ] [ FPS: {frame_rate} ]")

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

        # Python 3.10.4 or older
        match algorithms:
            case True:
                binary_tree.generate(screen)
            case False:
                recursive_backtracker.generate(screen)

        # Python 3.9.2 or earlier
        # if algorithms:
        #     binary_tree.generate(screen)
        # else:
        #     recursive_backtracker.generate(screen)

    else:
        PressEnter.render(screen)
        PressSpace.render(screen)

    pygame.display.flip()

pygame.quit()"""

from os.path import join
from time import sleep

import pygame
from pygame import Rect, mouse, display, MOUSEBUTTONDOWN
from pygame.font import Font
from pygame.image import load
from pygame.mixer import music
from pygame.transform import scale
from pygame.display import set_mode

#import Game_Loop

from Directory_Settings import SCREEN, CLOCK, Width, Height, FPS, f_music, sfxButtonClick, bgMenu,\
    imgCursor, imgCredits, imgHowToPlay, bgMenu, bgCredits, game_folder

pygame.init()
pygame.mixer.init()
menuFont = Font(join(game_folder, '04B30.ttf'), Height//16)
mouse.set_visible(False)
game_on = True
sfxButtonClick.set_volume(0.5)


def buttons_print(button, name, font):
    if button.collidepoint(mouse.get_pos()):
        text = font.render(name, True, (235, 47, 47))
        SCREEN.blit(text, (button.x + (button.width + 10 - text.get_width()) / 2,
                           button.y + (button.height - 3 - text.get_height()) / 2))
    else:
        text = font.render(name.lower(), True, (245, 245, 245))
        SCREEN.blit(text, (button.x + (button.width + 10 - text.get_width()) / 2,
                           button.y + (button.height - 3 - text.get_height()) / 2))


def main_menu():

    button_play = Rect((Width // 4), Height//3, Width//8, 42)
    button_how_to_play = Rect((Width // 4), Height//2.05, Width//2, 42)
    button_credits = Rect((Width // 4), Height//1.6, Width//3.65, 42)
    button_exit = Rect((Width // 4), Height//1.3, Width//8.2, 42)

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
                    game_resolution = set_resolution()
                    
                    if game_resolution == 0:
                        print("600X600")
                    elif game_resolution == 1:
                        print("800x800")
                    elif game_resolution == 2:
                        print("1000x1000")
                    elif game_resolution == 3:
                        print("600X600")
                        sleep(1)
                        LoadGameScreen()
                        final_score = Game_Loop.GameLoop(selection)
                        LoadGameScreen()
                        music.load(join(f_music, 'Menu_Music.ogg'))
                        music.set_volume(0.15)
                        music.play(loops=-1)
                        save = open('High_Scores.user', 'a')
                        save.write(str(final_score) + '\n')
                        save.close()

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
                if button_exit.collidepoint(
                        mouse.get_pos()):
                    sfxButtonClick.play()
                    sleep(1)
                    exit()

        SCREEN.blit(pygame.transform.scale(bgMenu, (Width, Height)), (0, 0))

        buttons_print(button_play, 'PLAY', menuFont)
        buttons_print(button_how_to_play, 'HOW TO PLAY', menuFont)
        buttons_print(button_credits, 'CREDITS', menuFont)
        buttons_print(button_exit, 'EXIT', menuFont)

        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))

        display.update()

"""
def LoadGameScreen():
    Testyle = 0
    music.stop()
    load_bar = 0
    loading = True

    while loading:
        CLOCK.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        SCREEN.blit(bgLoading, (-240, 0))
        SCREEN.blit(imgLoad, (0, 0))
        pygame.draw.rect(SCREEN, (35, 100, 198), (185, 552, load_bar, 36))
        SCREEN.blit(bgArcadeGame, (0, 0))
        load_bar += 2
        display.update()
        if load_bar >= 632:
            loading = False
    sleep(2)"""

# Resolucion
# tamaño celdas
# algoritmo

# Colores
# ver o no la euristica


def set_resolution():

    selection = True
    resolution = -1

    button_next = Rect((Width // 2), Height // 1.12, Width // 8, 42)
    button_res0 = Rect((Width // 2.6), Height // 2.5, 170, 30)
    button_res1 = Rect((Width // 2.6), Height // 2.1, 170, 30)
    button_res2 = Rect((Width // 2.65), Height // 1.8, 170, 30)
    button_res3 = Rect((Width // 2.65), Height // 1.6, 170, 30)

    while selection:

        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_next.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    selection = False
                if button_res0.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    resolution = 600
                if button_res1.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    resolution = 800
                if button_res2.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    resolution = 1000
                if button_res3.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    resolution = 2000

        SCREEN.blit(pygame.transform.scale(bgCredits, (Width, Height)), (0, 0))

        buttons_print(button_next, 'NEXT', menuFont)
        buttons_print(button_res0, '600px', menuFont)
        buttons_print(button_res1, '800px', menuFont)
        buttons_print(button_res2, '1000px', menuFont)
        buttons_print(button_res3, '2000px', menuFont)

        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))

        display.update()

    set_mode((resolution, resolution))
    return resolution


def how_to_play_menu():

    check_how_to_play = True
    button_back = Rect((Width // 1.3), Height // 1.12, Width // 20, 42)

    while check_how_to_play:

        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_back.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    check_how_to_play = False

        SCREEN.blit(pygame.transform.scale(bgCredits, (Width, Height)), (0, 0))
        SCREEN.blit(pygame.transform.scale(imgHowToPlay, (Width, Height)), (0, 0))

        buttons_print(button_back, 'BACK', menuFont)
        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))

        display.update()


def credits_menu():

    music.load(join(f_music, 'Credits_Music.ogg'))
    music.set_volume(0.5)
    music.play(loops=-1)
    check_credits_menu = True

    y_mov = 0
    button_back = Rect((Width // 1.3), Height // 1.12, Width // 20, 42)

    while check_credits_menu:

        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_back.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    check_credits_menu = False

        SCREEN.blit(pygame.transform.scale(bgCredits, (Width, Height)), (0, 0))

        y_move = y_mov % imgCredits.get_rect().height
        SCREEN.blit(pygame.transform.scale(imgCredits, (Width, Width*5)), (0, (y_move - imgCredits.get_rect().height)))
        if y_move < Height:
            SCREEN.blit(imgCredits, (0, y_move))

        if Width == 2000:
            y_mov -= 2
        elif Width == 1000:
            y_mov -= 1
        elif Width == 800:
            y_mov -= .8
        elif Width == 600:
            y_mov -= .6

        buttons_print(button_back, 'BACK', menuFont)
        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))

        display.update()

    music.stop()


main_menu()
