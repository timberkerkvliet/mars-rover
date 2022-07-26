from unittest import TestCase

from mars_rover import Heading
from team1.create_empty_grid import create_empty_grid


class ExampleTest(TestCase):
    def test_place_new_rover(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()

        # assert
        self.assertEqual(1, len(grid.get_rovers()))

    def test_move_rover_on_grid(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.move()

        # assert
        self.assertEqual((0, 1), rover.get_position())

    def test_move_rover_cant_move_outside_of_grid(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.move()

        # assert
        with self.assertRaises(Exception) as e:
            rover.move()
            self.assertEqual((0, 1), rover.get_position())

    def test_rover_has_default_heading_north(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()
        rover = grid.get_rovers()[0]

        # assert
        self.assertEqual(Heading.NORTH, rover.get_heading())

    def test_can_rotate_left(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.rotate_left()

        # assert
        self.assertEqual(Heading.WEST, rover.get_heading())

    def test_can_rotate_right(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.rotate_right()

        # assert
        self.assertEqual(Heading.EAST, rover.get_heading())

    def test_can_rotate_right_and_move_one_step(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.rotate_right()
        rover.move()

        # assert
        self.assertEqual((1, 0), rover.get_position())

    def test_can_rotate_left_and_move_one_step(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.rotate_right()
        rover.move()
        rover.rotate_left()
        rover.rotate_left()
        rover.move()

        # assert
        self.assertEqual((0, 0), rover.get_position())

    def test_cannot_move_off_south_side_of_grid(self):
        # arrange
        grid = create_empty_grid(dimensions=(1, 1))

        # act
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.rotate_left()
        rover.rotate_left()

        # assert
        with self.assertRaises(Exception) as e:
            rover.move()
            self.assertEqual((0, 0), rover.get_position())
