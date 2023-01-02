from typing import Tuple

import pygame

from src.config import *


class Board:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.x_surf = pygame.image.load(f"{BASE_APP_PATH}/assets/x.png")
        self.o_surf = pygame.image.load(f"{BASE_APP_PATH}/assets/o.png")
        self.board_surf = pygame.image.load(f"{BASE_APP_PATH}/assets/board.png")

        x_width = self.x_surf.get_width()
        o_width = self.o_surf.get_width()

        self.x_surf = pygame.transform.scale(self.x_surf, (x_width / 3, x_width  / 3))
        self.o_surf = pygame.transform.scale(self.o_surf, (o_width / 3, o_width  / 3))
        self.board_surf = pygame.transform.scale(
            self.board_surf, (BOARD_SIZE, BOARD_SIZE)
        )

    def show(self, position: Tuple[int, int], board):
        x, y = position

        board_rect = self.board_surf.get_rect(topleft=position)
        self.display_surface.blit(self.board_surf, board_rect)

        space = BOARD_SIZE // 6

        x_grid = [x + index * space for index in range(6) if index % 2 != 0]
        y_grid = [y + index * space for index in range(6) if index % 2 != 0]

        for _x in x_grid:
            for _y in y_grid:
                i = (_x - x) // SQUARE_SIZE
                j = (_y - y) // SQUARE_SIZE

                if board[(i, j)][0] == "X":
                    x_rect = self.x_surf.get_rect(center=(_x, _y))
                    self.display_surface.blit(self.x_surf, x_rect)
                elif board[(i, j)][0] == "O":
                    o_rect = self.o_surf.get_rect(center=(_x, _y))
                    self.display_surface.blit(self.o_surf, o_rect)
