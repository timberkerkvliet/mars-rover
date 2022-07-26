from unittest import TestCase

from team3.create_empty_grid import create_empty_grid
from mars_rover import Heading


class ExampleTest(TestCase):
    def test_place_new_rover(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()

        # assert
        self.assertEqual(1, len(grid.get_rovers()))

    def test_place_new_rover_at_position_0_0(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()

        rover = grid.get_rovers()[0]

        # assert
        self.assertEqual(rover.get_position(), (0, 0))

    def test_place_two_rovers(self):
        grid = create_empty_grid(dimensions=(1, 1))
        grid.place_new_rover()

        with self.assertRaises(Exception):
            grid.place_new_rover()

    def test_move_rover(self):
        grid = create_empty_grid(dimensions=(1, 1))
        grid.place_new_rover()
        rover = grid.get_rovers()[0]

        rover.move()

        self.assertEqual(rover.get_position(), (0, 1))

    def test_rotate(self):
        grid = create_empty_grid(dimensions=(1, 1))
        grid.place_new_rover()
        rover = grid.get_rovers()[0]

        rover.rotate_right()

        self.assertEqual(rover.get_heading(), Heading.EAST)
        self.assertEqual(rover.get_position(), (0,0))

    def test_rotate_two_times(self):
        grid = create_empty_grid(dimensions=(1, 1))
        grid.place_new_rover()
        rover = grid.get_rovers()[0]

        rover.rotate_right()
        rover.rotate_right()

        self.assertEqual(rover.get_heading(), Heading.SOUTH)
        self.assertEqual(rover.get_position(), (0, 0))
