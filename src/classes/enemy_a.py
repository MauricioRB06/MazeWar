import pygame
from Directory_Settings import spEnemy1
from pygame.transform import scale
from pygame.sprite import Sprite
from src.classes.enemy_collider import EnemyCollider
from random import randint


class EnemyA(Sprite):

    def __init__(self, cell_size, start_position, screen, difficulty, new_maze):
        super().__init__()
        self.cell_x = 0
        self.cell_y = 0
        self.enemy_maze = new_maze
        self.collision_movement = False
        self.last_search = "right"
        self.cell = cell_size
        self.SCREEN = screen
        self.image = pygame.transform.scale(spEnemy1, (cell_size // 2, cell_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = start_position
        self.last = pygame.time.get_ticks()
        self.cooldown = difficulty
        self.top_collider = EnemyCollider(
            pygame.Rect(self.rect.x + self.rect.width // 4, self.rect.y - self.cell // 2, self.cell // 4,
                        self.cell // 2))
        self.bottom_collider = EnemyCollider(
            pygame.Rect(self.rect.x + self.rect.width // 4, self.rect.y + self.rect.height, self.cell // 4,
                        self.cell // 2))
        self.left_collider = EnemyCollider(
            pygame.Rect(self.rect.x - self.rect.width, self.rect.y + self.rect.height // 4, self.cell // 2,
                        self.cell // 4))
        self.right_collider = EnemyCollider(
            pygame.Rect(self.rect.x + self.rect.width, self.rect.y + self.rect.height // 4, self.cell // 2,
                        self.cell // 4))

        for x in range(self.enemy_maze.grid.cols):
            for y in range(self.enemy_maze.grid.rows):
                if self.enemy_maze.grid.cells[x][y].isStartingNode:
                    self.cell_x = x
                    self.cell_y = y

    def movement(self, up: bool, down: bool, left: bool, right: bool):

        if not self.collision_movement:

            self.collision_movement = True

            if self.last_search == "right":

                if not right and not down:

                    direction = randint(0, 20)

                    if direction >= 10:
                        self.collision_movement = self.move_right()
                        self.last_search = "right"
                    else:
                        self.collision_movement = self.move_down()
                        self.last_search = "down"

                elif not right and not up:

                    direction = randint(0, 20)

                    if direction <= 10:
                        self.collision_movement = self.move_right()
                        self.last_search = "right"
                    else:
                        self.collision_movement = self.move_up()
                        self.last_search = "up"

                elif not right:
                    self.collision_movement = self.move_right()
                    self.last_search = "right"

                elif not up:
                    self.collision_movement = self.move_up()
                    self.last_search = "up"

                elif not down:
                    self.collision_movement = self.move_down()
                    self.last_search = "down"

                elif not left:
                    self.collision_movement = self.move_left()
                    self.last_search = "left"

            if self.last_search == "up":

                if not up and not right:

                    direction = randint(0, 20)

                    if direction >= 10:
                        self.collision_movement = self.move_up()
                        self.last_search = "up"
                    else:
                        self.collision_movement = self.move_right()
                        self.last_search = "right"

                elif not up and not left:

                    direction = randint(0, 20)

                    if direction <= 10:
                        self.collision_movement = self.move_up()
                        self.last_search = "up"
                    else:
                        self.collision_movement = self.move_left()
                        self.last_search = "left"

                elif not up:
                    self.collision_movement = self.move_up()
                    self.last_search = "up"

                elif not right:
                    self.collision_movement = self.move_right()
                    self.last_search = "right"

                elif not left:
                    self.collision_movement = self.move_left()
                    self.last_search = "left"

                elif not down:
                    self.collision_movement = self.move_down()
                    self.last_search = "down"

            if self.last_search == "left":

                if not left and not up:

                    direction = randint(0, 20)

                    if direction >= 10:
                        self.collision_movement = self.move_left()
                        self.last_search = "left"
                    else:
                        self.collision_movement = self.move_up()
                        self.last_search = "up"

                elif not left and not down:

                    direction = randint(0, 20)

                    if direction <= 10:
                        self.collision_movement = self.move_left()
                        self.last_search = "left"
                    else:
                        self.collision_movement = self.move_down()
                        self.last_search = "down"

                elif not left:
                    self.collision_movement = self.move_left()
                    self.last_search = "left"
                elif not up:
                    self.collision_movement = self.move_up()
                    self.last_search = "up"
                elif not down:
                    self.collision_movement = self.move_down()
                    self.last_search = "down"
                elif not right:
                    self.collision_movement = self.move_right()
                    self.last_search = "right"

            if self.last_search == "down":

                if not down and not left:

                    direction = randint(0, 20)

                    if direction >= 10:
                        self.collision_movement = self.move_down()
                        self.last_search = "down"
                    else:
                        self.collision_movement = self.move_left()
                        self.last_search = "left"

                elif not down and not right:

                    direction = randint(0, 20)

                    if direction <= 10:
                        self.collision_movement = self.move_down()
                        self.last_search = "down"
                    else:
                        self.collision_movement = self.move_right()
                        self.last_search = "right"

                elif not down:
                    self.collision_movement = self.move_down()
                    self.last_search = "down"
                elif not right:
                    self.collision_movement = self.move_right()
                    self.last_search = "right"
                elif not left:
                    self.collision_movement = self.move_left()
                    self.last_search = "left"
                elif not up:
                    self.collision_movement = self.move_up()
                    self.last_search = "up"

    def move_up(self):

        # Development only, the next line of code draws the direction in which the enemy will move.
        # pygame.draw.rect(self.SCREEN, (255, 0, 0), self.top_collider.rect, 1)

        if pygame.time.get_ticks() - self.last >= self.cooldown:
            self.top_collider.rect.y = self.top_collider.rect.y - self.cell
            self.bottom_collider.rect.y = self.bottom_collider.rect.y - self.cell
            self.left_collider.rect.y = self.left_collider.rect.y - self.cell
            self.right_collider.rect.y = self.right_collider.rect.y - self.cell
            self.rect.y = self.rect.y - self.cell
            self.last = pygame.time.get_ticks()
            return False

    def move_down(self):

        # Development only, the next line of code draws the direction in which the enemy will move.
        # pygame.draw.rect(self.SCREEN, (0, 255, 0), self.bottom_collider.rect, 1)

        if pygame.time.get_ticks() - self.last >= self.cooldown:
            self.top_collider.rect.y = self.top_collider.rect.y + self.cell
            self.bottom_collider.rect.y = self.bottom_collider.rect.y + self.cell
            self.left_collider.rect.y = self.left_collider.rect.y + self.cell
            self.right_collider.rect.y = self.right_collider.rect.y + self.cell
            self.rect.y = self.rect.y + self.cell
            self.last = pygame.time.get_ticks()
            return False

    def move_left(self):

        # Development only, the next line of code draws the direction in which the enemy will move.
        # pygame.draw.rect(self.SCREEN, (0, 0, 255), self.left_collider.rect, 1)

        if pygame.time.get_ticks() - self.last >= self.cooldown:
            self.top_collider.rect.x = self.top_collider.rect.x - self.cell
            self.bottom_collider.rect.x = self.bottom_collider.rect.x - self.cell
            self.left_collider.rect.x = self.left_collider.rect.x - self.cell
            self.right_collider.rect.x = self.right_collider.rect.x - self.cell
            self.rect.x = self.rect.x - self.cell
            self.last = pygame.time.get_ticks()
            return False

    def move_right(self):

        # Development only, the next line of code draws the direction in which the enemy will move.
        # pygame.draw.rect(self.SCREEN, (0, 255, 255), self.right_collider.rect, 1)

        if pygame.time.get_ticks() - self.last >= self.cooldown:
            self.top_collider.rect.x = self.top_collider.rect.x + self.cell
            self.bottom_collider.rect.x = self.bottom_collider.rect.x + self.cell
            self.left_collider.rect.x = self.left_collider.rect.x + self.cell
            self.right_collider.rect.x = self.right_collider.rect.x + self.cell
            self.rect.x = self.rect.x + self.cell
            self.last = pygame.time.get_ticks()
            return False
