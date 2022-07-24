from unittest import TestCase

from grid import create_empty_grid
from mars_rover import Heading


class ExampleTest(TestCase):
    def test_rover_gives_back_start_position(self):
        grid = create_empty_grid(grid_size=1)
        rover = grid.place_new_rover(position=(0, 1), heading=Heading.NORTH)

        self.assertEqual((0, 1), rover.get_position())
