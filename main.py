import pygame
import sys

pygame.init()
pygame.display.init() # initialize the display module

pygame.display.set_caption('Cookie Clicker')

# Set window size
window_width = 1920
window_height = 1080
screen = pygame.display.set_mode((window_width, window_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Button for clicking to add Cookies
click_btn_colour = blue
click_btn_hover = green
click_btn_text_colour = white
click_btn_shape = pygame.Rect(300, 250, 200, 50)
font = pygame.font.Font(None, 36)

# Text to show amount of clicks
clicks = 0
keys = pygame.key.get_pressed()

# Function to render text on button
def render_text(text, font, colour, center):
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect(center=center)
    return text_surface, text_rect

# Game loop
run_game = True
while run_game:

    screen.fill(black)

    click_text = font.render(f'Clicks: {clicks}', True, click_btn_text_colour)

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    screen.blit(click_text, (50, 50))

    # Change Click Button colour on hover
    if click_btn_shape.collidepoint(mouse_pos):
        click_btn_current_colour = click_btn_hover
    else:
        click_btn_current_colour = click_btn_colour

    # Draw Click Button
    pygame.draw.rect(screen, click_btn_current_colour, click_btn_shape)

    # Render and draw the text
    button_text, button_text_rect = render_text("Click Me", font, click_btn_text_colour, click_btn_shape.center)
    screen.blit(button_text, button_text_rect)

    # Exit program on clicking Window X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click_btn_shape.collidepoint(mouse_pos):
                clicks += 1

    # Update the display
    pygame.display.flip()