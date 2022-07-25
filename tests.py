from unittest import TestCase

from grid import create_empty_grid


class ExampleTest(TestCase):
    def test_place_new_rover(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()

        # assert
        self.assertEqual(1, len(grid.get_rovers()))
