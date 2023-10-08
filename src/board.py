import numpy as np
import pygame


class Board:

    def __init__(self, size):
        self.size = size
        self.board = np.zeros(shape=(size, size))
        self.cell_size = 50
        self.back = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gird_color = (0, 0, 0)
        self.background_color = (194, 173, 138)

    def draw_grid(self, screen):
        for i in range(1, self.size):
            for j in range(1, self.size):
                n = self.cell_size
                k = 0
                if j > 1 or i > 1:
                    k = 1
                pygame.draw.rect(screen, self.gird_color, ((i * n) - ((i - 1) * k), (j * n) - ((j - 1) * k), n, n), 1)

    def draw_stones(self, screen):
        # 0 is no stone
        # 1 is white
        # 2 is black
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    self.draw_stone(i, j, self.white, screen)
                elif self.board[i][j] == 1:
                    self.draw_stone(i, j, self.back, screen)

    def draw_stone(self, x, y, color, screen):
        n = self.cell_size
        i = (1 + x) * n
        j = (1 + y) * n
        r = (self.cell_size - 10) // 2
        pygame.draw.circle(screen, color, (i, j), r)

    def draw(self, screen):
        screen.fill(self.background_color)
        self.draw_grid(screen)
        self.board[0, 0] = 1
        self.board[18, 18] = 1
        self.draw_stones(screen)
