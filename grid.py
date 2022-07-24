from abc import ABC, abstractmethod
from typing import Tuple

from mars_rover import MarsRover


class Grid(ABC):
    @abstractmethod
    def place_new_rover(self, position: Tuple[int, int]) -> MarsRover:
        """Places a new rover on the field at the indicated position"""


def create_empty_grid(grid_size: int) -> Grid:
    """Creates an empty grid, on which rovers can be placed."""
