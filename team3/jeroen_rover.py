from typing import Tuple

from mars_rover import MarsRover, Heading


class JeroenRover(MarsRover):
    def __init__(self) -> None:
        self._heading = Heading.NORTH
        self._position = (0,0)

    def rotate_left(self) -> None:
        """Rotates 90 degrees left"""

    def rotate_right(self) -> None:
        """Rotates 90 degrees right"""
        if self._heading == Heading.NORTH:
            self._heading = Heading.EAST
        elif self._heading == Heading.EAST:
            self._heading = Heading.SOUTH

    def move(self) -> None:
        if self._heading == Heading.NORTH:
            self._position = (self._position[0], self._position[1]+1)

        """Moves one spot in current heading"""

    def get_position(self) -> Tuple[int, int]:
        return self._position

    def get_heading(self) -> Heading:
        """Returns the current heading"""
        return self._heading
