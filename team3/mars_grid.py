from typing import List

from grid import Grid
from team3.jeroen_rover import JeroenRover


class MarsGrid(Grid):
    def __init__(self) -> None:
        self.rovers:List[JeroenRover] = []

    def place_new_rover(self) -> None:
        # kijken of er al een rover op 0, 0 staat
        rovers_on_start = [r for r in self.get_rovers() if r.get_position() == (0, 0)]
        if len(rovers_on_start) > 0:
            raise Exception
        self.rovers.append(JeroenRover())

    def get_rovers(self) -> List[JeroenRover]:
        """Get all the rovers on the field in order of placement"""
        return self.rovers
