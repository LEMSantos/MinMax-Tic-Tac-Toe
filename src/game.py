import sys

import pygame

from src.config import *
from src.screens import PlayScreen, SelectScreen

class Game:

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.screens = {
            "play-screen": PlayScreen(self.change_screen),
            "select-screen": SelectScreen(self.change_screen),
        }

        self.atual_screen = self.screens["play-screen"]

        self.__setup()

    def __setup(self):
        pygame.display.set_caption(GAME_TITLE)

    def __handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def change_screen(self, name, human_symbol=None):
        self.atual_screen = self.screens[name]

        if human_symbol:
            self.screens["play-screen"].set_human_symbol(human_symbol)

    def run(self) -> None:
        while True:
            self.screen.fill((255, 255, 255))
            self.__handle_events()

            dt = pygame.time.get_ticks() / 1000
            self.atual_screen.show(dt)

            pygame.display.update()
