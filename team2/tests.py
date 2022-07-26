from unittest import TestCase

from .grid import create_empty_grid


class ExampleTest(TestCase):
    def test_place_new_rover(self):
        # arrange
        grid = create_empty_grid(dimensions=(5, 5))

        # act
        grid.place_new_rover()

        # assert
        self.assertEqual(1, len(grid.get_rovers()))

    def test_placing_another_rover_on_top_of_another_raises_exception(self) -> None:
        # arrange
        grid = create_empty_grid(dimensions=(5, 5))
        grid.place_new_rover()

        # act & assert
        with self.assertRaises(Exception):
            grid.place_new_rover()

    def test_rover_can_move_forward(self):
        # arrange
        grid = create_empty_grid(dimensions=(5, 5))
        grid.place_new_rover()
        rover = grid.get_rovers()[0]

        #act
        rover.move()

        #assert
        self.assertEqual(rover.get_position(), (0, 1))

    def test_rover_can_move_to_the_east(self):
        # arrange
        grid = create_empty_grid(dimensions=(5, 5))
        grid.place_new_rover()
        rover = grid.get_rovers()[0]

        #act
        rover.rotate_right()
        rover.move()

        #assert
        self.assertEqual(rover.get_position(), (1, 0))

    def test_rover_can_move_to_the_south(self):
        # arrange
        grid = create_empty_grid(dimensions=(5, 5))
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.move()
        rover.rotate_right()
        rover.rotate_right()

        #act
        rover.move()

        #assert
        self.assertEqual(rover.get_position(), (0, 0))

    def test_new_rover_can_not_move_to_the_west(self):
        # arrange
        grid = create_empty_grid(dimensions=(4, 5))
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.rotate_left()

        #act & assert
        with self.assertRaises(Exception):
            rover.move()

    def test_cannot_go_out_of_bounds_in_north_direction(self):
        # arrange
        grid = create_empty_grid(dimensions=(4, 3))
        grid.place_new_rover()
        rover = grid.get_rovers()[0]
        rover.move()
        rover.move()

        # act & assert
        with self.assertRaises(Exception):
            rover.move()

    def test_rovers_cannot_collide(self):
        # arrange
        grid = create_empty_grid(dimensions=(4, 3))
        grid.place_new_rover()
        rover_1 = grid.get_rovers()[0]
        rover_1.move()
        grid.place_new_rover()
        rover_2 = grid.get_rovers()[1]

        # act & assert
        with self.assertRaises(Exception):
            rover_2.move()
