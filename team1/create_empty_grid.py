from typing import Tuple

from grid import Grid
from team1.grid_implementation import GridImplementation


def create_empty_grid(dimensions: Tuple[int, int]) -> Grid:
    """Creates an empty grid, on which rovers can be placed."""
    return GridImplementation(dimensions=dimensions)
