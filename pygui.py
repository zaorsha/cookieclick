import pygame

class button(object):
    # Button Sizes
    size1 = pygame.Rect(300, 250, 200, 50)

    def __init__(self, size, shape, colour):
        self.size = size
        self.shape = shape
        self.colour = colour
        