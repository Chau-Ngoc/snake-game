import pygame


class Fruit:
    def __init__(self, width=20):
        self.width = width
        self.fill_color = "#9D5353"

    def generate(self, surface, topleft_x, topleft_y):
        """
        Generate itself at a new random position each time the snake eats it.

        :param topleft_x: the x coordinate of the top left corner.
        :type topleft_x: int
        :param topleft_y: the y coordinate of the top left corner.
        :type topleft_y: int
        :param surface: the Surface to generate on.
        :type surface: pygame.Surface
        """
        fruit_rect = pygame.Rect(topleft_x, topleft_y, self.width, self.width)
        pygame.draw.rect(surface, self.fill_color, fruit_rect)
