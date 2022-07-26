from typing import Tuple

from grid import Grid
from team3.mars_grid import MarsGrid


def create_empty_grid(dimensions: Tuple[int, int]) -> Grid:
    """Creates an empty grid, on which rovers can be placed."""
    return MarsGrid()
