"""Main file to launch the game."""

import pygame

from src.consts import GAME_TITLE


# Initialize pygame
pygame.init()
# Set game title and window size
pygame.display.set_caption(GAME_TITLE)
pygame.display.set_mode((400, 500))
# Check if game is running
running = True
# Keep the game running while exit button is not pressed
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
