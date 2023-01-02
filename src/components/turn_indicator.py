from typing import Tuple

import pygame

from src.config import *


class TurnIndicator:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.x_surf = pygame.image.load(f"{BASE_APP_PATH}/assets/x.png")
        self.o_surf = pygame.image.load(f"{BASE_APP_PATH}/assets/o.png")
        self.x_white_surf = pygame.image.load(f"{BASE_APP_PATH}/assets/x_white.png")
        self.o_white_surf = pygame.image.load(f"{BASE_APP_PATH}/assets/o_white.png")

        self.x_surf = pygame.transform.scale(self.x_surf, (18, 18))
        self.o_surf = pygame.transform.scale(self.o_surf, (18, 18))
        self.x_white_surf = pygame.transform.scale(self.x_white_surf, (18, 18))
        self.o_white_surf = pygame.transform.scale(self.o_white_surf, (18, 18))

        self.gap = 12

    def show_turn_border(self, position: Tuple[int, int]):
        x_width = self.x_surf.get_width()

        turn_rect = self.x_surf.get_rect(
            midtop=position
        ).inflate(self.gap * 3 + x_width * 2, self.gap * 2)

        pygame.draw.rect(
            self.display_surface,
            BORDER_COLOR,
            turn_rect,
            2,
            turn_rect.height // 2,
        )

    def show_turn_symbol(self, position: Tuple[int, int], turn: str):
        x, y = position
        x_width = self.x_surf.get_width()

        offset = x_width / 2 + self.gap

        left_position = (x - offset, y)
        right_position = (x + offset, y)

        left_surf = self.x_white_surf if turn == "O" else self.x_surf
        right_surf = self.o_white_surf if turn == "X" else self.o_surf

        left_rect = left_surf.get_rect(midtop=left_position)
        right_rect = right_surf.get_rect(midtop=right_position)

        self.display_surface.blit(left_surf, left_rect)
        self.display_surface.blit(right_surf, right_rect)

    def show(self, position: Tuple[int, int], turn: str):
        self.show_turn_border(position)
        self.show_turn_symbol(position, turn)
