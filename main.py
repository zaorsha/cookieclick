import pygame

pygame.display.init() # initialize the display module

pygame.display.set_caption('Cookie Clicker')

window_width = 1920
window_height = 1080
pygame.display.set_mode((window_width, window_height))

run_game = True

while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
