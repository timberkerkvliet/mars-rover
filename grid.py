from abc import ABC, abstractmethod
from typing import Tuple

from mars_rover import MarsRover, Heading


class Grid(ABC):
    @abstractmethod
    def place_new_rover(self) -> MarsRover:
        """Places a new rover on the field"""


def create_empty_grid(dimensions: Tuple[int, int]) -> Grid:
    """Creates an empty grid, on which rovers can be placed."""
    raise NotImplementedError
