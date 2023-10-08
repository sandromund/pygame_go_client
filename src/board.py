import numpy as np
import pygame


class Board:

    def __init__(self, size):
        self.size = size
        self.board = np.zeros(shape=(size, size))
        self.cell_size = 50
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gird_color = (0, 0, 0)
        self.background_color = (194, 173, 138)

    def draw_grid(self, screen):
        # draw frame
        for x in range(self.size):
            pygame.draw.line(color=self.gird_color,
                             surface=screen,
                             start_pos=(self.cell_size + (x * self.cell_size), self.cell_size),
                             end_pos=(self.cell_size + (x * self.cell_size), self.cell_size * self.size))
        for y in range(self.size):
            pygame.draw.line(color=self.gird_color,
                             surface=screen,
                             start_pos=(self.cell_size, self.cell_size + (y * self.cell_size)),
                             end_pos=(self.cell_size * self.size, self.cell_size + (y * self.cell_size)))

    def draw_stones(self, screen):
        # 0 is no stone
        # 1 is white
        # 2 is black
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    self.draw_stone(i, j, self.white, screen)
                elif self.board[i][j] == 2:
                    self.draw_stone(i, j, self.black, screen)

    def draw_stone(self, x, y, color, screen, radius=None):
        n = self.cell_size
        i = (1 + x) * n
        j = (1 + y) * n
        if radius is None:
            radius = (self.cell_size - 10) // 2
        pygame.draw.circle(screen, color, (i, j), radius)

    def draw_star_points(self, screen):
        if self.size != 19:
            return
        points = [(3, 3), (9, 3), (15, 3),
                  (3, 9), (9, 9), (15, 9),
                  (3, 15), (9, 15), (15, 15)]
        for x, y in points:
            self.draw_stone(x, y, self.black, screen, radius=(self.cell_size - 40) // 2)

    def draw(self, screen):
        screen.fill(self.background_color)
        self.draw_grid(screen)
        self.draw_star_points(screen)
        self.draw_stone(10, 10, color=self.black, screen=screen)
        self.board[0, 0] = 1
        self.board[18, 18] = 1
        self.draw_stones(screen)

    def map_pos_to_closest_possible_field(self, screen_position):
        x, y = screen_position

        left = (x // self.cell_size) * self.cell_size
        right = left + self.cell_size
        up = (y // self.cell_size) * self.cell_size
        down = up + self.cell_size

        if abs(left - x) <= abs(right - x):
            new_x = left
        else:
            new_x = right

        if abs(up - y) <= abs(down - y):
            new_y = up
        else:
            new_y = down

        return self.pixel_to_board_position((new_x, new_y))

    def pixel_to_board_position(self, screen_position):
        x, y = screen_position

        x_new = int(x // self.cell_size) - 1
        y_new = int(y // self.cell_size) - 1

        x_new = min(max(0, x_new), 18)
        y_new = min(max(0, y_new), 18)

        return x_new, y_new
