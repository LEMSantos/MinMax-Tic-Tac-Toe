from typing import Callable
from src.screens.abstract_screen import AbstractScreen


class SelectScreen(AbstractScreen):

    def __init__(self, change_screen: Callable):
        self.change_screen = change_screen

    def show(self, dt: float):
        print("Mostrando tela de Seleção")
