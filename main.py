import pygame
import sys
import random

from objects import Fruit

FPS = 60
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = "#F3E9DD"

FRUIT_WIDTH = 20

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

pygame.init()

clock = pygame.time.Clock()

# create Fruit
topleft_x = random.randint(0, WINDOW_WIDTH - FRUIT_WIDTH)
topleft_y = random.randint(0, WINDOW_HEIGHT - FRUIT_WIDTH)
fruit = Fruit(FRUIT_WIDTH)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(BG_COLOR)

    # fruit auto-generate at random position on the display surface
    fruit.generate(display_surface, topleft_x, topleft_y)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
