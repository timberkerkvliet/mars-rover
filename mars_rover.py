from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple


class Heading(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'


class MarsRover(ABC):
    @abstractmethod
    def rotate_left(self) -> None:
        """Rotates 90 degrees left"""

    @abstractmethod
    def rotate_right(self) -> None:
        """Rotates 90 degrees right"""

    @abstractmethod
    def move(self) -> None:
        """Moves one spot in current heading"""

    @abstractmethod
    def get_position(self) -> Tuple[int, int]:
        """Returns the current position"""

    @abstractmethod
    def get_heading(self) -> Heading:
        """Returns the current heading"""
