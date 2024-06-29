import random

import pygame
from pygame import Rect

from constants import FRUIT_WIDTH, SNAKE_VELOCITY, WINDOW_HEIGHT, WINDOW_WIDTH


def generate_random_coordinates():
    topleft_x = random.randint(0, WINDOW_WIDTH - FRUIT_WIDTH)
    topleft_y = random.randint(0, WINDOW_HEIGHT - FRUIT_WIDTH)
    return topleft_x, topleft_y


class Node:
    def __init__(self, x, y):
        self.coords = x, y
        self.next = None

    def __str__(self):
        x, y = self.coords
        return f"({x}, {y}), next: {self.next}"


class Body:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, node):
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1


body = Body()
body.enqueue(Node(1, 1))
body.enqueue(Node(2, 3))
body.enqueue(Node(6, 9))


class Cube(Rect):
    def __init__(
        self, left, top, width=FRUIT_WIDTH, height=FRUIT_WIDTH, *args, **kwargs
    ):
        super().__init__(left, top, width, height)
        self.next = None

    def __str__(self):
        return f"topleft: {self.topleft}, next: {self.next}"


class Fruit(Cube):
    def __init__(self, left, top, width=FRUIT_WIDTH, height=FRUIT_WIDTH):
        super().__init__(left, top, width, height)
        self.fill_color = "#9D5353"

    def generate(self):
        """
        Update self's left and top coordinates each time eaten by the snake.
        """
        self.topleft = generate_random_coordinates()

    def blit(self, surface):
        pygame.draw.rect(surface, self.fill_color, self)


class Snake:
    def __init__(self):
        topleft_x, topleft_y = generate_random_coordinates()
        self.head = Cube(
            topleft_x, topleft_y, width=FRUIT_WIDTH, height=FRUIT_WIDTH
        )
        self.tail = self.head
        self.length = 1
        self.fill_color = "#FF5B00"

    def move_left(self):
        self.head.centerx -= SNAKE_VELOCITY
        self._shift_rect_coords((self.head.centerx, self.head.centery))

    def move_right(self):
        self.head.centerx += SNAKE_VELOCITY
        self._shift_rect_coords((self.head.centerx, self.head.centery))

    def move_up(self):
        self.head.centery -= SNAKE_VELOCITY
        self._shift_rect_coords((self.head.centerx, self.head.centery))

    def move_down(self):
        self.head.centery += SNAKE_VELOCITY
        self._shift_rect_coords((self.head.centerx, self.head.centery))

    def blit(self, surface):
        cur_cube = self.head
        while cur_cube is not None:
            pygame.draw.rect(surface, self.fill_color, cur_cube)
            cur_cube = cur_cube.next

    def grow(self, cube):
        self.tail.next = cube
        self.tail = cube
        self.length += 1

    def _shift_rect_coords(self, new_coords: tuple):
        cur_cube = self.head
        while cur_cube is not None:
            tmp_coords = cur_cube.centerx, cur_cube.centery
            cur_cube.centerx, cur_cube.centery = new_coords
            new_coords = tmp_coords
            cur_cube = cur_cube.next
