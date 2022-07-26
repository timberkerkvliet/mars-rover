from abc import ABC, abstractmethod
from unittest import TestCase

from grid import create_empty_grid


class AbstractTest(ABC, TestCase):
    @abstractmethod
    def create_empty_grid(self, dimensions):
        ...
