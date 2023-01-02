from typing import Callable, Dict, Tuple, List, Any

import pygame

from src.core.tic_tac_toe_utils import is_terminal, is_win, is_draw
from src.components.turn_indicator import TurnIndicator
from src.screens.abstract_screen import AbstractScreen
from src.components.game_score import GameScore
from src.components.board import Board
from src.core.minmax import MinMax
from src.config import *


class PlayScreen(AbstractScreen):

    def __init__(self, change_screen: Callable):
        self.change_screen = change_screen
        self.display_surface = pygame.display.get_surface()

        self.human_symbol = "O"
        self.cpu_symbol = "X"

        self.human_turn = False
        self.check_terminal = False
        self.converted_board = None

        self.x_board = (SCREEN_WIDTH - BOARD_SIZE) // 2
        self.y_board = 175

        self.board_grid = {
            (i, j): [" ", pygame.Rect(
                self.x_board + i * SQUARE_SIZE,
                self.y_board + j * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE,
            )]
            for j in range(3)
            for i in range(3)
        }

        self.brain = MinMax(self.human_symbol, self.cpu_symbol)

        self.turn_indicator = TurnIndicator()
        self.game_score = GameScore()
        self.board = Board()

    def __convert_board(self, board: Dict[Tuple[int, int], List[Any]]):
        new_board = [
            [" " for _ in range(3)]
            for _ in range(3)
        ]

        for i, j in board.keys():
            new_board[i][j] = board[(i, j)][0]

        return new_board

    def input(self):
        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0]:
            position = pygame.mouse.get_pos()

            if self.human_turn and not self.check_terminal:
                for value in self.board_grid.values():
                    if value[1].collidepoint(position) and value[0] == " ":
                        value[0] = self.human_symbol
                        self.human_turn = False

    def cpu_input(self):
        if not self.human_turn and not self.check_terminal:
            i, j =  self.brain.search(self.converted_board)

            self.board_grid[(i, j)][0] = self.cpu_symbol
            self.human_turn = True

    def set_human_symbol(self, symbol: str):
        self.human_symbol = symbol
        self.cpu_symbol = "X" if symbol == "O" else "O"

        self.human_turn = self.human_symbol == "X"

        self.brain = MinMax(self.human_symbol, self.cpu_symbol)

    def update_terminal(self):
        self.converted_board = self.__convert_board(self.board_grid)
        self.check_terminal = is_terminal(
            self.converted_board, self.human_symbol, self.cpu_symbol
        )

    def show(self, dt: float):
        self.update_terminal()
        self.input()

        self.game_score.show((self.x_board, 50))
        self.board.show((self.x_board, self.y_board), self.board_grid)
        self.turn_indicator.show(
            (SCREEN_WIDTH // 2, self.y_board + BOARD_SIZE + 50),
            self.human_symbol if self.human_turn else self.cpu_symbol
        )

        if self.check_terminal:
            print("Acabou o jogo")

        self.update_terminal()
        self.cpu_input()
