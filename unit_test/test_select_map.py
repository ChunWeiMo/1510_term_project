from modules.exploration.map import maps
from modules.exploration.map import select_map
from unittest import TestCase
from unittest.mock import patch


class TestSelectMap(TestCase):
    @patch('random.randint', return_value=1)
    def test_select_normal_map(self, _):
        map_list = maps()
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 1, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 4, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_map_elements = map_list[1]
        self.assertEqual(expected_map_elements, select_map(character_dictionary, map_list))

    @patch('random.randint', return_value=10)
    def test_select_map_lucky(self, _):
        map_list = maps()
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 10, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 4, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_map_elements = map_list[10]
        self.assertEqual(expected_map_elements, select_map(character_dictionary, map_list))

    def test_select_map_final_boss(self):
        map_list = maps()
        character_dictionary = {"Character_status": {"Level": 3, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 10, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 4, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        expected_map_elements = map_list[11]
        self.assertEqual(expected_map_elements, select_map(character_dictionary, map_list))
