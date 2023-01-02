from typing import List
from copy import deepcopy

from src.core.tic_tac_toe_utils import is_win, is_terminal


class MinMax:

    def __init__(self, human_symbol: str, cpu_symbol: str):
        self.__human_symbol = human_symbol
        self.__cpu_symbol = cpu_symbol

    def __candidates(self, board: List[List[str]], player: str):
        candidate_moves = []

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != " ":
                    continue

                candidate = deepcopy(board)
                candidate[i][j] = player

                candidate_moves.append(candidate)

        return candidate_moves

    def __evaluate(self, board: List[List[str]]):
        if is_win(board, self.__cpu_symbol):
            return 1

        if is_win(board, self.__human_symbol):
            return -1

        return 0

    def __minimax_alpha_beta(self,
                             board: List[List[str]],
                             alpha: float=float('-inf'),
                             beta: float=float('+inf'),
                             maximizing: bool=False):

        if is_terminal(board, self.__human_symbol, self.__cpu_symbol):
            return self.__evaluate(board)

        if maximizing:
            value = float('-inf')

            for child in self.__candidates(board, self.__cpu_symbol):
                value = max(value, self.__minimax_alpha_beta(child, alpha, beta, False))

                if value >= beta:
                    break

                alpha = max(alpha, value)
        else:
            value = float('+inf')

            for child in self.__candidates(board, self.__human_symbol):
                value = min(value, self.__minimax_alpha_beta(child, alpha, beta, True))

                if value <= alpha:
                    break

                beta = min(beta, value)

        return value

    def search(self, board: List[List[str]]):
        candidate_moves = self.__candidates(board, self.__cpu_symbol)
        result = max(candidate_moves, key=self.__minimax_alpha_beta)

        for i in range(3):
            for j in range(3):
                if board[i][j] != result[i][j]:
                    return (i, j)
