from typing import Text, Tuple

import pygame

from src.config import *


class ScoreItem:

    def __init__(self, image_src: Text):
        self.font = pygame.font.Font(
            f"{BASE_APP_PATH}/fonts/Nunito-Regular.ttf", 15
        )

        self.icon_surf = pygame.image.load(image_src)
        self.icon_surf = pygame.transform.scale(self.icon_surf, (30, 30))

        self.gap = 8

    def draw(self,
             position: Tuple[int, int],
             surface: pygame.Surface,
             text: Text,
             color: Tuple[int, int, int]):

        x, y = position

        text_surf = self.font.render(text, True, color)
        icon_height = self.icon_surf.get_height()

        text_rect = text_surf.get_rect(midtop=(x, y + self.gap + icon_height))
        icon_rect = self.icon_surf.get_rect(midtop=(x, y))

        surface.blit(self.icon_surf, icon_rect)
        surface.blit(text_surf, text_rect)


class GameScore:

    def __init__(self, x_wins=0, o_wins=0, draws=0):
        self.display_surface = pygame.display.get_surface()

        self.scores = [o_wins, x_wins, draws]

        self.score_items = [
            ("vitórias", ScoreItem(f"{BASE_APP_PATH}/assets/o.png"), O_COLOR),
            ("vitórias", ScoreItem(f"{BASE_APP_PATH}/assets/x.png"), X_COLOR),
            ("empates", ScoreItem(f"{BASE_APP_PATH}/assets/draw.png"), DRAW_COLOR),
        ]

    def update_score(self, x_wins, o_wins, draws):
        self.scores = [o_wins, x_wins, draws]

    def show(self, position: Tuple[int, int]):
        x, y = position

        space = BOARD_SIZE // 6

        score_grid = [x + index * space for index in range(6) if index % 2 != 0]

        for x, (text, item, color), score in zip(score_grid, self.score_items, self.scores):
            item.draw((x, y), self.display_surface, f"{score} {text}", color)
