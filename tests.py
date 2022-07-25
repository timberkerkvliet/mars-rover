from unittest import TestCase

from grid import create_empty_grid


class ExampleTest(TestCase):
    def test_rover_gives_back_start_position(self):
        grid = create_empty_grid(dimensions=(1, 1))
        rover = grid.place_new_rover()

        self.assertEqual((0, 0), rover.get_position())
