import pygame
import sys

from src.board import Board

board = Board(size=19)

window_size = board.cell_size * (board.size + 1)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Go Board')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.draw(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
