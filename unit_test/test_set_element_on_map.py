from modules.exploration.map import set_element_on_map
from unittest import TestCase


class TestSetElementOnMap(TestCase):
    def test_set_Door(self):
        element = 'Door'
        map_elements = {'Door': [(0, 0)]}
        current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
        set_element_on_map(map_elements, element, current_map)
        expected_current_map = {(0, 0): 'Door', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
        self.assertEqual(expected_current_map, current_map)

    def test_set_Enemy(self):
        element = 'Enemy'
        map_elements = {'Enemy': [(1, 1), (0, 1)]}
        current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (2, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty',
                       (2, 1): 'Empty'}
        set_element_on_map(map_elements, element, current_map)
        expected_current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (2, 0): 'Empty', (0, 1): 'Enemy', (1, 1): 'Enemy',
                                (2, 1): 'Empty'}
        self.assertEqual(expected_current_map, current_map)

    def test_set_Chest(self):
        element = 'Chest'
        map_elements = {'Chest': [(0, 2)]}
        current_map = {(0, 0): 'Empty', (0, 1): 'Empty', (0, 2): 'Empty', (0, 3): 'Empty'}
        set_element_on_map(map_elements, element, current_map)
        expected_current_map = {(0, 0): 'Empty', (0, 1): 'Empty', (0, 2): 'Chest', (0, 3): 'Empty'}
        self.assertEqual(expected_current_map, current_map)
