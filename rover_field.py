from abc import ABC, abstractmethod
from typing import Tuple

from mars_rover import MarsRover


class MartianGrid(ABC):
    @abstractmethod
    def place_new_rover(self, position: Tuple[int, int]) -> MarsRover:
        """Places a new rover on the field at the indicated position"""


class MartianGridFactory(ABC):
    @abstractmethod
    def create_empty_grid(self, grid_size: int) -> MartianGrid:
        """Creates an empty martian grid, which can place new rovers on this field."""
