import random

import pygame

from constants import FRUIT_WIDTH, SNAKE_VELOCITY, WINDOW_HEIGHT, WINDOW_WIDTH


def generate_random_coordinates():
    topleft_x = random.randint(0, WINDOW_WIDTH - FRUIT_WIDTH)
    topleft_y = random.randint(0, WINDOW_HEIGHT - FRUIT_WIDTH)
    return topleft_x, topleft_y


class Cube:
    def __init__(self, topleft_x, topleft_y):
        self.width = FRUIT_WIDTH
        self.rect = pygame.Rect(topleft_x, topleft_y, self.width, self.width)


class Fruit(Cube):
    def __init__(self, topleft_x, topleft_y):
        super().__init__(topleft_x, topleft_y)
        self.fill_color = "#9D5353"

    def generate(self):
        """
        Generate itself at a new random position each time the snake eats it.
        """
        topleft_x, topleft_y = generate_random_coordinates()
        self.rect = pygame.Rect(topleft_x, topleft_y, self.width, self.width)

    def blit(self, surface):
        pygame.draw.rect(surface, self.fill_color, self.rect)


class Snake:
    def __init__(self):
        topleft_x, topleft_y = generate_random_coordinates()
        self.head = Cube(topleft_x, topleft_y)
        self.body = []
        self.length = 0
        self.fill_color = "#FF5B00"

    def move_left(self):
        self.head.rect.centerx -= SNAKE_VELOCITY

    def move_right(self):
        self.head.rect.centerx += SNAKE_VELOCITY

    def move_up(self):
        self.head.rect.centery -= SNAKE_VELOCITY

    def move_down(self):
        self.head.rect.centery += SNAKE_VELOCITY

    def blit(self, surface):
        pygame.draw.rect(surface, self.fill_color, self.head.rect)
