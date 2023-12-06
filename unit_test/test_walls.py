from modules.exploration import map
from unittest import TestCase


class TestWalls(TestCase):
    def test_2_by_2_map(self):
        expect_south_wall = 1
        expect_east_wall = 1
        current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (1, 0): 'Empty', (1, 1): 'Empty'}
        self.assertEqual((expect_south_wall, expect_east_wall), map.walls(current_map))

    def test_10_by_10_map(self):
        expect_south_wall = 9
        expect_east_wall = 9
        current_map = {(i, j): 'Empty' for i in range(10) for j in range(10)}
        self.assertEqual((expect_south_wall, expect_east_wall), map.walls(current_map))
    