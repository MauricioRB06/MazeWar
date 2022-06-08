# MazeWar Project - File 12
# Pygame [ https://www.pygame.org/docs/ ]

import pygame
import time
from os.path import join

from pygame.mixer import music
from pygame.sprite import Group

from src.Directory_Settings import CLOCK, FPS, ftPause, bgGameOver, f_music
from src.classes.game_functions import game_pause, game_over
from src.classes.player import Player
from src.classes.goal import Goal

pygame.init()
pygame.mixer.init()


def game_loop(new_cell, new_maze, screen, game_over_font):

    maze = new_maze
    SCREEN = screen
    start = maze.starting_node.rect
    finish = maze.end_node.rect

    player_group = Group()
    goal_group = Group()

    player = Player(new_cell, start, SCREEN)
    player_group.add(player)

    goal = Player(new_cell, finish, SCREEN)
    goal_group.add(goal)

    show_heuristic = False
    show_path = False

    music.load(join(f_music, 'Game_Music.ogg'))
    music.set_volume(0.5)
    music.play(loops=-1)

    game = True
    winner = None
    game_time = None
    start_time = time.time()

    while game:

        CLOCK.tick(FPS)
        goal_group.draw(SCREEN)
        maze.show_maze(SCREEN, show_heuristic, show_path)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    show_heuristic = not show_heuristic
                if event.key == pygame.K_2:
                    show_path = not show_path
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.set_volume(0.2)
                    game_pause(CLOCK, ftPause, SCREEN)
                    pygame.mixer.music.set_volume(0.7)

        player_collision = pygame.sprite.spritecollide(player, goal_group, False)

        if player_collision:

            finish_time = time.time()
            winner = "PLAYER"
            game_time = finish_time-start_time
            game_over(winner, game_time, new_cell, game_over_font, CLOCK, SCREEN, bgGameOver, f_music)
            game = False

        player_group.update()
        player_group.draw(SCREEN)

        pygame.display.update()

    return winner, game_time
