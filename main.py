import pygame
import sys

FPS = 60
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = "#141E27"

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

pygame.init()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(BG_COLOR)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
