import pygame
import sys
import time
from functions import *
from settings import *
import numpy as np

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("My Game of Life on Python")

# Create a 2D array to hold the game state
array1 = [[0 for _ in range(height // 10)] for _ in range(width // 10)]
w, h = width // RES, height // RES

# Initialize the game state
gen0(w, h, array1)

Unpaused = False
zoom_level = 1

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Unpaused = not Unpaused
            if event.key == pygame.K_r:
                gen0(w, h, array1)
            if event.key == pygame.K_g:
                x, y = pygame.mouse.get_pos()
                cor_x, cor_y = (x // (RES * zoom_level)), (y // (RES * zoom_level))
                add_glider(array1, cor_x, cor_y)
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                zoom_level += 1
            if event.key == pygame.K_MINUS:
                zoom_level = max(1, zoom_level - 1)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            cor_x, cor_y = (x // (RES * zoom_level)), (y // (RES * zoom_level))
            if event.button == 1:  # Left mouse button
                addToArray(array1, cor_x, cor_y)
            elif event.button == 3:  # Right mouse button
                removeFromArray(array1, cor_x, cor_y)

    # Draw the game state
    screen.fill(BLACK)

    cell_width = (width // w) * zoom_level
    cell_height = (height // h) * zoom_level

    for y, row in enumerate(array1):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, WHITE, (x * cell_width, y * cell_height, cell_width, cell_height))
                # pygame.draw.circle(screen, (0, 255, 0), (x * cell_width, y * cell_height), cell_width // 2, cell_height // 2)
            pygame.draw.rect(screen, WHITE, (x * cell_width, y * cell_height, cell_width, cell_height), 1)

    # Update the game state
    if Unpaused:
        array1 = nextGen(array1)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(10)
