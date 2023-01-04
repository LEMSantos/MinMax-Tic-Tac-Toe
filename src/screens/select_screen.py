from typing import Callable

import pygame

from src.config import *
from src.components.button import Button
from src.screens.abstract_screen import AbstractScreen


class SelectScreen(AbstractScreen):

    def __init__(self, change_screen: Callable):
        self.display_surface = pygame.display.get_surface()
        self.change_screen = change_screen

        self.font = pygame.font.Font(f"{BASE_APP_PATH}/fonts/Nunito-Regular.ttf", 30)

        self.button_x = Button(100, "x", self.change_screen_X, (255, 255, 255))
        self.button_o = Button(100, "o", self.change_screen_O, (255, 255, 255))

        self.button_x.gap = 20
        self.button_o.gap = 20

        self.or_text = self.font.render("ou", True, DRAW_COLOR)
        self.select_text = self.font.render("Selecione uma", True, DRAW_COLOR)
        self.complement_text = self.font.render("das opções abaixo", True, DRAW_COLOR)

    def input(self, position):
        self.button_x.input(position)
        self.button_o.input(position)

    def change_screen_X(self):
        self.change_screen("play-screen", "X")

    def change_screen_O(self):
        self.change_screen("play-screen", "O")

    def show(self, dt: float):
        offset = 80

        or_rect = self.or_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + offset)
        )

        select_rect = self.select_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - offset - 40)
        )

        complement_rect = self.complement_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - offset)
        )

        self.display_surface.blit(self.or_text, or_rect)
        self.display_surface.blit(self.select_text, select_rect)
        self.display_surface.blit(self.complement_text, complement_rect)

        self.button_x.show((100, SCREEN_HEIGHT // 2 + offset))
        self.button_o.show((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 + offset))
