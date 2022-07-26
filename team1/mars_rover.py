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


class MarsRoverImplementation(MarsRover):
    pos_x: int
    pos_y: int
    heading: Heading

    def __init__(self, grid):
        self.grid = grid
        self.pos_x = 0
        self.pos_y = 0
        self.heading = Heading.NORTH

    def rotate_left(self) -> None:
        if self.heading == Heading.NORTH:
            self.heading = Heading.WEST
        elif self.heading == Heading.WEST:
            self.heading = Heading.SOUTH
        elif self.heading == Heading.SOUTH:
            self.heading = Heading.EAST
        elif self.heading == Heading.EAST:
            self.heading = Heading.NORTH

    def rotate_right(self) -> None:
        if self.heading == Heading.NORTH:
            self.heading = Heading.EAST
        elif self.heading == Heading.EAST:
            self.heading = Heading.SOUTH
        elif self.heading == Heading.SOUTH:
            self.heading = Heading.WEST
        elif self.heading == Heading.WEST:
            self.heading = Heading.NORTH

    def move(self) -> None:
        if self.heading == Heading.NORTH:
            if self.pos_y + 1 > self.grid.dimensions[1]:
                raise RoverFallOfGrid
            self.pos_y += 1
        elif self.heading == Heading.EAST:
            if self.pos_x + 1 > self.grid.dimensions[0]:
                raise RoverFallOfGrid
            self.pos_x += 1
        elif self.heading == Heading.WEST:
            if self.pos_x - 1 < 0:
                raise RoverFallOfGrid
            self.pos_x -= 1
        elif self.heading == Heading.SOUTH:
            if self.pos_y - 1 < 0:
                raise RoverFallOfGrid
            self.pos_y -= 1

    def get_position(self) -> Tuple[int, int]:
        return self.pos_x, self.pos_y

    def get_heading(self) -> Heading:
        return self.heading


class RoverFallOfGrid(Exception):
    pass
