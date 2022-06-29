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
from src.classes.wall import Wall
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
    north_wall_group = Group()
    east_wall_group = Group()

    player = Player(new_cell, start, SCREEN)
    player_group.add(player)

    goal = Player(new_cell, finish, SCREEN)
    goal_group.add(goal)

    for x in range(maze.grid.cols):
        for y in range(maze.grid.rows):
            if maze.grid.cells[x][y].north_rect is not None:
                north_rect = Wall(maze.grid.cells[x][y].north_rect)
                north_wall_group.add(north_rect)
            if maze.grid.cells[x][y].east_rect is not None:
                east_rect = Wall(maze.grid.cells[x][y].east_rect)
                east_wall_group.add(east_rect)

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

        nort_wall_collision = pygame.sprite.spritecollide(player, north_wall_group, False)
        east_wall_collision = pygame.sprite.spritecollide(player, east_wall_group, False)

        player_collision = pygame.sprite.spritecollide(player, goal_group, False)

        if nort_wall_collision:
            if abs(nort_wall_collision[0].rect.top - player.rect.bottom) < 5:
                player.move_forward()
            if abs(nort_wall_collision[0].rect.bottom - player.rect.top) < 5:
                player.move_back()
            if abs(nort_wall_collision[0].rect.right - player.rect.left) < 5:
                player.move_right()
            if abs(nort_wall_collision[0].rect.left - player.rect.right) < 5:
                player.move_left()

        if east_wall_collision:
            if abs(east_wall_collision[0].rect.right - player.rect.left) < 5:
                player.move_right()
            if abs(east_wall_collision[0].rect.left - player.rect.right) < 5:
                player.move_left()
            if abs(east_wall_collision[0].rect.bottom - player.rect.top) < 5:
                player.move_back()
            if abs(east_wall_collision[0].rect.top - player.rect.bottom) < 5:
                player.move_forward()

        if player_collision:
            finish_time = time.time()
            winner = "PLAYER"
            game_time = finish_time-start_time
            game_over(winner, game_time, new_cell, game_over_font, CLOCK, SCREEN, bgGameOver, f_music)
            game = False

        player_group.draw(SCREEN)
        player_group.update()

        pygame.display.update()

    return winner, game_time
