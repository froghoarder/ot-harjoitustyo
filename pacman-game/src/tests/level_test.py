import unittest
from level import Level

LEVEL_MAP_TEST =   [[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 3, 0, 0, 1],
                    [1, 1, 1, 1, 1]]

CELL_SIZE = 50

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP_TEST)

    def coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

