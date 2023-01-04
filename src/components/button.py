from typing import Callable, Text, Tuple

import pygame

from src.config import *


class Button:

    def __init__(self,
                 button_size: int,
                 icon: Text,
                 action_function: Callable,
                 button_color: Tuple[int, int, int]=RESTART_COLOR):

        self.display_surface = pygame.display.get_surface()

        self.action_function = action_function
        self.button_color = button_color

        self.button_size = button_size
        self.off_gap = 4
        self.gap = 8

        icon_size = button_size - self.gap * 2 - self.off_gap * 2

        self.icon_surf = pygame.image.load(f"{BASE_APP_PATH}/assets/{icon}.png")
        self.icon_surf = pygame.transform.scale(self.icon_surf, (icon_size, icon_size))

    def input(self):
        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0]:
            position = pygame.mouse.get_pos()

            if self.main_rect.collidepoint(position):
                self.action_function()

    def show_button_border(self, position: Tuple[int, int]):
        offset = self.gap * 2 + self.off_gap * 2

        self.main_rect = self.icon_surf.get_rect(
            center = position
        ).inflate(offset, offset)

        pygame.draw.rect(
            self.display_surface,
            BORDER_COLOR,
            self.main_rect,
            2,
            self.main_rect.width // 2,
        )

    def show_internal_circle(self, position: Tuple[int, int]):
        offset = self.gap * 2

        internal_circle_rect = self.icon_surf.get_rect(
            center = position
        ).inflate(offset, offset)

        pygame.draw.rect(
            self.display_surface,
            self.button_color,
            internal_circle_rect,
            0,
            self.main_rect.width // 2,
        )

    def show_icon(self, position: Tuple[int, int]):
        icon_rect = self.icon_surf.get_rect(center=position)
        self.display_surface.blit(self.icon_surf, icon_rect)

    def show(self, position: Tuple[int, int]):
        self.show_button_border(position)
        self.input()
        self.show_internal_circle(position)
        self.show_icon(position)
