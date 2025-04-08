import unittest
import pygame
from level import Level

LEVEL_MAP_TEST = [[1, 1, 1, 1, 1],
                  [1, 0, 0, 2, 1],
                  [1, 3, 2, 0, 1],
                  [1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP_TEST)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move_character(self):

        self.assert_coordinates_equal(
            self.level.frog, CELL_SIZE, 2 * CELL_SIZE + CELL_SIZE)

        self.level.move_frog(1 * CELL_SIZE, -1 * CELL_SIZE)

        self.assert_coordinates_equal(
            self.level.frog, 2 * CELL_SIZE, CELL_SIZE + CELL_SIZE)

    def test_can_grow_amount_of_points(self):
        self.assertEqual(self.level.points, 0)
        self.level.move_frog(dx=CELL_SIZE)
        self.level.collect_stuff()
        self.assertEqual(self.level.points, 1)

