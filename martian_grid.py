from abc import ABC, abstractmethod
from typing import Tuple

from mars_rover import DeployedMarsRover


class MartianGrid(ABC):
    @abstractmethod
    def deploy_new_rover(self, position: Tuple[int, int]) -> DeployedMarsRover:
        """Places a new rover on the field at the indicated position"""


def create_empty_grid(grid_size: int) -> MartianGrid:
    """Creates an empty martian grid, on which mars rovers can be placed."""
