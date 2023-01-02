from typing import Callable
from abc import ABCMeta, abstractmethod


class AbstractScreen(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, change_screen: Callable):
        pass

    @abstractmethod
    def show(self, dt: float):
        pass
