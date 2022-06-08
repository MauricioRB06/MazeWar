# MazeWar Project - File 13

import pygame
from os.path import join
from pygame import display
from pygame.image import load
from pygame.mixer import music


def game_pause(clock, image_pause, screen):

    pause = True
    SCREEN = screen
    CLOCK = clock
    ftPause = image_pause

    while pause:

        CLOCK.tick(15)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False

        SCREEN.blit(pygame.transform.scale(ftPause, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
        display.update()


def game_over(winner_name, timer, cell_size, font, clock, screen, img_game_over, f_music):

    game_over_screen = True
    SCREEN = screen
    CLOCK = clock

    music.load(join(f_music, 'Game_OverMusic.ogg'))
    music.play(loops=-1)
    music.set_volume(0.7)
    winner = winner_name
    time = str(timer)
    time = time[0:4] + " SEG"
    maze_size = str((SCREEN.get_width()//cell_size)*(SCREEN.get_width()//cell_size))
    maze_size = maze_size + " CELLS"
    bgGameOver = img_game_over

    text_winner = font.render(winner, True, (255, 255, 255))
    text_timer = font.render(time, True, (255, 255, 255))
    text_maze = font.render(maze_size, True, (255, 255, 255))

    while game_over_screen:
        CLOCK.tick(60)

        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                exit()
            if game_event.type == pygame.KEYDOWN:
                if game_event.key == pygame.K_SPACE:
                    game_over_screen = False

        SCREEN.blit(pygame.transform.scale(bgGameOver, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
        SCREEN.blit(text_winner, (SCREEN.get_width()//3.2, SCREEN.get_height()//2.05))
        SCREEN.blit(text_timer, (SCREEN.get_width()//3.5, SCREEN.get_height()//3.5))
        SCREEN.blit(text_maze, (SCREEN.get_width()//3.5, SCREEN.get_height()//1.45))
        display.update()

    SCREEN.fill((0, 0, 0))
