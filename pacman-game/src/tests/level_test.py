import unittest
import pygame
from level import Level
from gameloop import GameLoop

LEVEL_MAP_TEST = [[1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 1],
                  [1, 3, 0, 0, 1],
                  [1, 1, 1, 1, 1]]

CELL_SIZE = 50


class StubRenderer:
    """not relevant yet
    """

    def render(self):
        pass


class StubClock:
    """not relevant yet
    """

    def tick(self, fps):
        pass

    def get_ticks(self):
        0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP_TEST)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move_character(self):

        self.assert_coordinates_equal(
            self.level.frog, CELL_SIZE, 2 * CELL_SIZE)

        self.level.move_frog(1 * CELL_SIZE, -1 * CELL_SIZE)

        self.assert_coordinates_equal(
            self.level.frog, 2 * CELL_SIZE, CELL_SIZE)
