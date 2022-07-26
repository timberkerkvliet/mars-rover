from __future__ import annotations
from dataclasses import dataclass, field
from typing import Tuple, List

from grid import Grid
from mars_rover import MarsRover, Heading


class MarsRoverImplementation(MarsRover):
    def __init__(self, grid: GridImplementation) -> None:
        self._grid = grid
        self._position = (0, 0)
        self._heading = Heading.NORTH

    def rotate_left(self) -> None:
        if self._heading == Heading.NORTH:
            self._heading = Heading.WEST
        elif self._heading == Heading.WEST:
            self._heading = Heading.SOUTH
        elif self._heading == Heading.SOUTH:
            self._heading = Heading.EAST
        else:
            self._heading = Heading.NORTH

    def rotate_right(self) -> None:
        if self._heading == Heading.NORTH:
            self._heading = Heading.EAST
        elif self._heading == Heading.EAST:
            self._heading = Heading.SOUTH
        elif self._heading == Heading.SOUTH:
            self._heading = Heading.WEST
        else:
            self._heading = Heading.NORTH

    def move(self) -> None:
        if self._heading == Heading.NORTH:
            new_position = (self._position[0], self._position[1] + 1)
        elif self._heading == Heading.EAST:
            new_position = (self._position[0] + 1, self._position[1])
        elif self._heading == Heading.SOUTH:
            new_position = (self._position[0], self._position[1] - 1)
        else:
            new_position = (self._position[0] - 1, self._position[1])

        if not self._grid.check_if_position_is_allowed(new_position):
            raise Exception

        self._position = new_position

    def get_position(self) -> Tuple[int, int]:
        return self._position

    def get_heading(self) -> Heading:
        return self._heading


@dataclass
class GridImplementation(Grid):
    dimensions: Tuple[int, int]
    rovers: List[MarsRover] = field(default_factory=list)

    def place_new_rover(self) -> None:
        if not self._check_if_position_does_not_collide_with_rovers((0,0)):
            raise Exception

        self.rovers.append(MarsRoverImplementation(self))

    def get_rovers(self) -> List[MarsRover]:
        return self.rovers

    def check_if_position_is_allowed(self, position: Tuple[int, int]) -> bool:
        return self._check_if_position_is_in_bounds(position) and self._check_if_position_does_not_collide_with_rovers(position)

    def _check_if_position_is_in_bounds(self, position: Tuple[int, int]) -> bool:
        return 0 <= position[0] < self.dimensions[0] and 0 <= position[1] < self.dimensions[1]

    def _check_if_position_does_not_collide_with_rovers(self, position: Tuple[int, int]) -> bool:
        return all(
            rover.get_position() != position
            for rover in self.rovers
        )


