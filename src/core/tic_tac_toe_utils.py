from typing import List


def is_win(board: List[List[str]], player: str):
    # Verificando as Linhas do Tabuleiro
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True

    # Verificando as Colunas do Tabuleiro
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    # Verificando as Diagonais do Tabuleiro
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

    return False


def is_draw(board: List[List[str]]):
    for line in board:
        if " " in line:
            return False

    return True


def is_terminal(board: List[List[str]], human_symbol: str, cpu_symbol: str):
        human_win = is_win(board, human_symbol)
        cpu_win = is_win(board, cpu_symbol)
        draw = is_draw(board)

        return human_win or cpu_win or draw
