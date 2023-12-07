from modules.exploration.map import create_map
from modules.exploration.map import maps
from unittest import TestCase
from unittest.mock import patch


class TestCreateMap(TestCase):
    @patch('random.randint', return_value=1)
    def test_create_map1(self, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 60, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 4, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        map_list = maps()
        expected_current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (2, 0): 'Empty', (3, 0): 'Empty', (4, 0): 'Empty',
                                (5, 0): 'Empty', (6, 0): 'Empty', (7, 0): 'Empty', (8, 0): 'Door', (9, 0): 'Empty',
                                (0, 1): 'Empty', (1, 1): 'Chest', (2, 1): 'Empty', (3, 1): 'Empty', (4, 1): 'Empty',
                                (5, 1): 'Empty', (6, 1): 'Enemy', (7, 1): 'Empty', (8, 1): 'Empty', (9, 1): 'Empty',
                                (0, 2): 'Empty', (1, 2): 'Empty', (2, 2): 'Empty', (3, 2): 'Empty', (4, 2): 'Empty',
                                (5, 2): 'Empty', (6, 2): 'Empty', (7, 2): 'Empty', (8, 2): 'Empty', (9, 2): 'Empty',
                                (0, 3): 'Empty', (1, 3): 'Empty', (2, 3): 'Enemy', (3, 3): 'Empty', (4, 3): 'Empty',
                                (5, 3): 'Empty', (6, 3): 'Empty', (7, 3): 'Empty', (8, 3): 'Empty', (9, 3): 'Empty',
                                (0, 4): 'Door', (1, 4): 'Empty', (2, 4): 'Empty', (3, 4): 'Enemy', (4, 4): 'Empty',
                                (5, 4): 'Empty', (6, 4): 'Empty', (7, 4): 'Empty', (8, 4): 'Empty', (9, 4): 'Empty',
                                (0, 5): 'Empty', (1, 5): 'Enemy', (2, 5): 'Enemy', (3, 5): 'Merchant', (4, 5): 'Enemy',
                                (5, 5): 'Empty', (6, 5): 'Enemy', (7, 5): 'Chest', (8, 5): 'Empty', (9, 5): 'Empty',
                                (0, 6): 'Empty', (1, 6): 'Empty', (2, 6): 'Empty', (3, 6): 'Enemy', (4, 6): 'Enemy',
                                (5, 6): 'Empty', (6, 6): 'Empty', (7, 6): 'Enemy', (8, 6): 'Empty', (9, 6): 'Empty',
                                (0, 7): 'Empty', (1, 7): 'Empty', (2, 7): 'Enemy', (3, 7): 'Empty', (4, 7): 'Empty',
                                (5, 7): 'Empty', (6, 7): 'Empty', (7, 7): 'Empty', (8, 7): 'Empty', (9, 7): 'Empty',
                                (0, 8): 'Empty', (1, 8): 'Empty', (2, 8): 'Empty', (3, 8): 'Empty', (4, 8): 'Empty',
                                (5, 8): 'Empty', (6, 8): 'Empty', (7, 8): 'Empty', (8, 8): 'Empty', (9, 8): 'Empty',
                                (0, 9): 'Empty', (1, 9): 'Empty', (2, 9): 'Enemy', (3, 9): 'Empty', (4, 9): 'Empty',
                                (5, 9): 'Empty', (6, 9): 'Door', (7, 9): 'Empty', (8, 9): 'Empty', (9, 9): 'Empty'}

        self.assertEqual(expected_current_map, create_map(character_dictionary, map_list))

    @patch('random.randint', return_value=10)
    def test_create_map_lucky(self, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 60, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 10, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 4, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        map_list = maps()
        expected_current_map = {(0, 0): 'Merchant', (1, 0): 'Empty', (2, 0): 'Empty', (3, 0): 'Empty', (4, 0): 'Empty',
                                (5, 0): 'Empty', (6, 0): 'Empty', (7, 0): 'Empty', (8, 0): 'Empty', (9, 0): 'Empty',
                                (0, 1): 'Empty', (1, 1): 'Empty', (2, 1): 'Empty', (3, 1): 'Empty', (4, 1): 'Empty',
                                (5, 1): 'Empty', (6, 1): 'Empty', (7, 1): 'Empty', (8, 1): 'Empty', (9, 1): 'Empty',
                                (0, 2): 'Empty', (1, 2): 'Empty', (2, 2): 'Chest', (3, 2): 'Empty', (4, 2): 'Empty',
                                (5, 2): 'Chest', (6, 2): 'Empty', (7, 2): 'Empty', (8, 2): 'Chest', (9, 2): 'Empty',
                                (0, 3): 'Empty', (1, 3): 'Empty', (2, 3): 'Empty', (3, 3): 'Empty', (4, 3): 'Empty',
                                (5, 3): 'Empty', (6, 3): 'Empty', (7, 3): 'Empty', (8, 3): 'Empty', (9, 3): 'Empty',
                                (0, 4): 'Empty', (1, 4): 'Empty', (2, 4): 'Empty', (3, 4): 'Empty',
                                (4, 4): 'Healing_fountain', (5, 4): 'Empty', (6, 4): 'Healing_fountain',
                                (7, 4): 'Empty', (8, 4): 'Empty', (9, 4): 'Empty', (0, 5): 'Empty', (1, 5): 'Empty',
                                (2, 5): 'Empty', (3, 5): 'Empty', (4, 5): 'Empty', (5, 5): 'Empty', (6, 5): 'Empty',
                                (7, 5): 'Empty', (8, 5): 'Empty', (9, 5): 'Empty', (0, 6): 'Empty', (1, 6): 'Chest',
                                (2, 6): 'Empty', (3, 6): 'Empty', (4, 6): 'Chest', (5, 6): 'Empty', (6, 6): 'Empty',
                                (7, 6): 'Chest', (8, 6): 'Empty', (9, 6): 'Empty', (0, 7): 'Empty', (1, 7): 'Empty',
                                (2, 7): 'Empty', (3, 7): 'Empty', (4, 7): 'Empty', (5, 7): 'Empty', (6, 7): 'Empty',
                                (7, 7): 'Empty', (8, 7): 'Empty', (9, 7): 'Empty', (0, 8): 'Empty', (1, 8): 'Empty',
                                (2, 8): 'Empty', (3, 8): 'Empty', (4, 8): 'Empty', (5, 8): 'Empty', (6, 8): 'Empty',
                                (7, 8): 'Empty', (8, 8): 'Empty', (9, 8): 'Empty', (0, 9): 'Empty', (1, 9): 'Empty',
                                (2, 9): 'Empty', (3, 9): 'Door', (4, 9): 'Empty', (5, 9): 'Empty', (6, 9): 'Door',
                                (7, 9): 'Empty', (8, 9): 'Empty', (9, 9): 'Empty'}

        self.assertEqual(expected_current_map, create_map(character_dictionary, map_list))

    @patch('random.randint', return_value=11)
    def test_create_map_Boss(self, _):
        character_dictionary = {"Character_status": {"Level": 3, "HP": 60, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 10, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 4, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        map_list = maps()
        expected_current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (2, 0): 'Empty', (3, 0): 'Empty', (4, 0): 'Empty',
                                (5, 0): 'Empty', (6, 0): 'Empty', (7, 0): 'Empty', (8, 0): 'Empty', (9, 0): 'Empty',
                                (0, 1): 'Empty', (1, 1): 'Empty', (2, 1): 'Empty', (3, 1): 'Empty', (4, 1): 'Empty',
                                (5, 1): 'Empty', (6, 1): 'Empty', (7, 1): 'Empty', (8, 1): 'Empty', (9, 1): 'Empty',
                                (0, 2): 'Empty', (1, 2): 'Empty', (2, 2): 'Empty', (3, 2): 'Empty', (4, 2): 'Empty',
                                (5, 2): 'Empty', (6, 2): 'Empty', (7, 2): 'Empty', (8, 2): 'Empty', (9, 2): 'Empty',
                                (0, 3): 'Empty', (1, 3): 'Empty', (2, 3): 'Empty', (3, 3): 'Empty', (4, 3): 'Empty',
                                (5, 3): 'Empty', (6, 3): 'Empty', (7, 3): 'Empty', (8, 3): 'Empty', (9, 3): 'Empty',
                                (0, 4): 'Empty', (1, 4): 'Empty', (2, 4): 'Empty', (3, 4): 'Empty',
                                (4, 4): 'Final Boss', (5, 4): 'Final Boss', (6, 4): 'Empty', (7, 4): 'Empty',
                                (8, 4): 'Empty', (9, 4): 'Empty', (0, 5): 'Empty', (1, 5): 'Empty', (2, 5): 'Empty',
                                (3, 5): 'Empty', (4, 5): 'Final Boss', (5, 5): 'Final Boss', (6, 5): 'Empty',
                                (7, 5): 'Empty', (8, 5): 'Empty', (9, 5): 'Empty', (0, 6): 'Empty', (1, 6): 'Empty',
                                (2, 6): 'Empty', (3, 6): 'Empty', (4, 6): 'Empty', (5, 6): 'Empty', (6, 6): 'Empty',
                                (7, 6): 'Empty', (8, 6): 'Empty', (9, 6): 'Empty', (0, 7): 'Empty', (1, 7): 'Empty',
                                (2, 7): 'Empty', (3, 7): 'Empty', (4, 7): 'Empty', (5, 7): 'Empty', (6, 7): 'Empty',
                                (7, 7): 'Empty', (8, 7): 'Empty', (9, 7): 'Empty', (0, 8): 'Empty', (1, 8): 'Empty',
                                (2, 8): 'Empty', (3, 8): 'Empty', (4, 8): 'Empty', (5, 8): 'Empty', (6, 8): 'Empty',
                                (7, 8): 'Empty', (8, 8): 'Empty', (9, 8): 'Empty', (0, 9): 'Empty', (1, 9): 'Empty',
                                (2, 9): 'Empty', (3, 9): 'Empty', (4, 9): 'Door', (5, 9): 'Door', (6, 9): 'Empty',
                                (7, 9): 'Empty', (8, 9): 'Empty', (9, 9): 'Merchant'}
        self.assertEqual(expected_current_map, create_map(character_dictionary, map_list))
