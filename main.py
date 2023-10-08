import pygame
import sys

from src.board import Board

board = Board(size=9)
board.cell_size = 100

window_size = board.cell_size * (board.size + 1)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Go Board')

current_play = 2

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_buttons = pygame.mouse.get_pressed()
            x, y = board.map_pos_to_closest_possible_field(event.pos)
            if mouse_buttons[0]:
                if board.board[x][y] == 0:
                    board.board[x][y] = current_play

                    if current_play == 1:
                        current_play = 2
                    else:
                        current_play = 1
            elif mouse_buttons[2]:
                board.board[x][y] = 0

    board.draw(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
