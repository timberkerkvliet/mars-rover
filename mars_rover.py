from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Optional


class Heading(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'


@dataclass(frozen=True)
class SoilData:
    left: Optional[str]
    right: Optional[str]


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

    @abstractmethod
    def get_soil_data(self) -> SoilData:
        """Returns the soil data at the current position"""
