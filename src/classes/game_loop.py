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
from src.classes.enemy_a import EnemyA
from src.classes.enemy_b import EnemyB
from src.classes.enemy_c import EnemyC
from src.classes.wall import Wall
from src.classes.goal import Goal

pygame.init()
pygame.mixer.init()


def game_loop(new_cell, new_maze, screen, game_over_font, enemies_difficulty):

    maze = new_maze
    SCREEN = screen
    start = maze.starting_node.rect
    finish = maze.end_node.rect

    player_group = Group()
    enemy_a_group = Group()
    enemy_b_group = Group()
    enemy_c_group = Group()
    goal_group = Group()
    north_wall_group = Group()
    east_wall_group = Group()

    player = Player(new_cell, start, SCREEN)
    player_group.add(player)

    enemy_a = EnemyA(new_cell, start, SCREEN, enemies_difficulty, maze)
    enemy_a_group.add(enemy_a)

    enemy_b = EnemyB(new_cell, start, SCREEN, enemies_difficulty, maze)
    enemy_b_group.add(enemy_b)

    enemy_c = EnemyC(new_cell, start, SCREEN, enemies_difficulty, maze)
    enemy_c_group.add(enemy_c)

    goal = Player(new_cell, finish, SCREEN)
    goal_group.add(goal)

    wall_left = Wall(pygame.Rect(0, 0, new_cell//4, new_cell * maze.grid.rows))
    east_wall_group.add(wall_left)

    wall_down = Wall(pygame.Rect(0, SCREEN.get_height() - new_cell//4, new_cell * maze.grid.cols, new_cell//4))
    north_wall_group.add(wall_down)

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
        enemy_a_collision = pygame.sprite.spritecollide(enemy_a, goal_group, False)
        enemy_b_collision = pygame.sprite.spritecollide(enemy_b, goal_group, False)
        enemy_c_collision = pygame.sprite.spritecollide(enemy_c, goal_group, False)

        enemy_a_up = pygame.sprite.spritecollide(enemy_a.top_collider, north_wall_group, False)
        enemy_a_down = pygame.sprite.spritecollide(enemy_a.bottom_collider, north_wall_group, False)
        enemy_a_left = pygame.sprite.spritecollide(enemy_a.left_collider, east_wall_group, False)
        enemy_a_right = pygame.sprite.spritecollide(enemy_a.right_collider, east_wall_group, False)

        enemy_b_up = pygame.sprite.spritecollide(enemy_b.top_collider, north_wall_group, False)
        enemy_b_down = pygame.sprite.spritecollide(enemy_b.bottom_collider, north_wall_group, False)
        enemy_b_left = pygame.sprite.spritecollide(enemy_b.left_collider, east_wall_group, False)
        enemy_b_right = pygame.sprite.spritecollide(enemy_b.right_collider, east_wall_group, False)

        enemy_c_up = pygame.sprite.spritecollide(enemy_c.top_collider, north_wall_group, False)
        enemy_c_down = pygame.sprite.spritecollide(enemy_c.bottom_collider, north_wall_group, False)
        enemy_c_left = pygame.sprite.spritecollide(enemy_c.left_collider, east_wall_group, False)
        enemy_c_right = pygame.sprite.spritecollide(enemy_c.right_collider, east_wall_group, False)

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

        if enemy_a_collision:
            finish_time = time.time()
            winner = "ENEMY_A"
            game_time = finish_time-start_time
            game_over(winner, game_time, new_cell, game_over_font, CLOCK, SCREEN, bgGameOver, f_music)
            game = False

        if enemy_b_collision:
            finish_time = time.time()
            winner = "ENEMY_B"
            game_time = finish_time-start_time
            game_over(winner, game_time, new_cell, game_over_font, CLOCK, SCREEN, bgGameOver, f_music)
            game = False

        if enemy_c_collision:
            finish_time = time.time()
            winner = "ENEMY_C"
            game_time = finish_time-start_time
            game_over(winner, game_time, new_cell, game_over_font, CLOCK, SCREEN, bgGameOver, f_music)
            game = False

        if player_collision:
            finish_time = time.time()
            winner = "PLAYER"
            game_time = finish_time-start_time
            game_over(winner, game_time, new_cell, game_over_font, CLOCK, SCREEN, bgGameOver, f_music)
            game = False

        if enemy_a_up:
            enemy_a_collision_up = True
        else:
            enemy_a_collision_up = False

        if enemy_a_down:
            enemy_a_collision_down = True
        else:
            enemy_a_collision_down = False

        if enemy_a_left:
            enemy_a_collision_left = True
        else:
            enemy_a_collision_left = False

        if enemy_a_right:
            enemy_a_collision_right = True
        else:
            enemy_a_collision_right = False

        if enemy_b_up:
            enemy_b_collision_up = True
        else:
            enemy_b_collision_up = False

        if enemy_b_down:
            enemy_b_collision_down = True
        else:
            enemy_b_collision_down = False

        if enemy_b_left:
            enemy_b_collision_left = True
        else:
            enemy_b_collision_left = False

        if enemy_b_right:
            enemy_b_collision_right = True
        else:
            enemy_b_collision_right = False

        if enemy_c_up:
            enemy_c_collision_up = True
        else:
            enemy_c_collision_up = False

        if enemy_c_down:
            enemy_c_collision_down = True
        else:
            enemy_c_collision_down = False

        if enemy_c_left:
            enemy_c_collision_left = True
        else:
            enemy_c_collision_left = False

        if enemy_c_right:
            enemy_c_collision_right = True
        else:
            enemy_c_collision_right = False

        player_group.draw(SCREEN)
        enemy_a_group.draw(SCREEN)
        enemy_b_group.draw(SCREEN)
        enemy_c_group.draw(SCREEN)
        player_group.update()
        enemy_a.movement(enemy_a_collision_up, enemy_a_collision_down, enemy_a_collision_left, enemy_a_collision_right)
        enemy_b.movement(enemy_b_collision_up, enemy_b_collision_down, enemy_b_collision_left, enemy_b_collision_right)
        enemy_c.movement(enemy_c_collision_up, enemy_c_collision_down, enemy_c_collision_left, enemy_c_collision_right)

        pygame.display.update()

    return winner, game_time
