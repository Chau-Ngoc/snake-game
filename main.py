import sys

import pygame

from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BG_COLOR, FPS
from objects import Fruit, Snake, generate_random_coordinates

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

# create a clock to govern fps
clock = pygame.time.Clock()

# create Fruit
topleft_x, topleft_y = generate_random_coordinates()
fruit = Fruit(topleft_x, topleft_y)

# create Snake
snake = Snake()

direction = "down"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # fill the display surface
    display_surface.fill(BG_COLOR)
    snake.blit(display_surface)

    if direction == "left" and snake.head.rect.left >= 0:
        snake.move_left()
    elif direction == "right" and snake.head.rect.right <= WINDOW_WIDTH:
        snake.move_right()
    elif direction == "up" and snake.head.rect.top >= 0:
        snake.move_up()
    elif direction == "down" and snake.head.rect.bottom <= WINDOW_HEIGHT:
        snake.move_down()

    # fruit auto-generate at random position on the display surface
    if snake.head.rect.colliderect(fruit.rect):
        fruit.generate()

    fruit.blit(display_surface)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
