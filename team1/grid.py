from abc import ABC, abstractmethod
from typing import Tuple, List

from .mars_rover import MarsRover, MarsRoverImplementation


class Grid(ABC):
    @abstractmethod
    def place_new_rover(self) -> None:
        """Places a new rover on the field"""

    @abstractmethod
    def get_rovers(self) -> List[MarsRover]:
        """Get all the rovers on the field in order of placement"""


class GridImplementation(Grid):
    def __init__(self, dimensions: Tuple[int, int]):
        self.dimensions = dimensions
        self.rovers: List[MarsRover] = []

    def place_new_rover(self) -> None:
        self.rovers.append(MarsRoverImplementation(self))

    def get_rovers(self) -> List[MarsRover]:
        return self.rovers


def create_empty_grid(dimensions: Tuple[int, int]) -> Grid:
    """Creates an empty grid, on which rovers can be placed."""
    return GridImplementation(dimensions=dimensions)
