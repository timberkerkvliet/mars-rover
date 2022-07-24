from unittest import TestCase

from martian_grid import create_empty_grid


class ExampleTest(TestCase):
    def test_rover_indicates_start_position(self):
        grid = create_empty_grid(grid_size=1)
        rover = grid.place_new_rover(position=(0, 0))

        self.assertEqual((0, 0), rover.get_position())
