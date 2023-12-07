from modules.exploration.movement import start_from_door
from unittest.mock import patch
from unittest import TestCase


class TestStartFromDoor(TestCase):
    @patch('random.randint', return_value=0)
    def test_1_door(self, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 2, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 4, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Door', (1, 1): 'Empty'}
        start_from_door(character_dictionary, current_map)
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 2, "VIS": 3},
            "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 1, "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        self.assertEqual(expected_character_dictionary, character_dictionary)

    @patch('random.randint', return_value=0)
    def test_2_doors(self, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 110, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                                     "LUK": 3, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 5, "Y-coordinate": 5, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): 'Door', (1, 0): 'Empty', (0, 1): 'Door', (1, 1): 'Empty'}
        start_from_door(character_dictionary, current_map)
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 110, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
                                 "LUK": 3, "VIS": 3},
            "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 0, "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        self.assertEqual(expected_character_dictionary, character_dictionary)

    @patch('random.randint', return_value=3)
    def test_4_doors(self, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 110, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 2,
                                                     "LUK": 3, "VIS": 3},
                                "Name": "aaa", "X-coordinate": 0, "Y-coordinate": 5, "EXP": 0, "Items": {"Gold": 0,
                                                                                                         "Potions": 0},
                                "Equipment": 0, "Debuff": {"Burn": 0}}
        current_map = {(0, 0): 'Door', (1, 0): 'Door', (0, 1): 'Door', (1, 1): 'Door'}
        start_from_door(character_dictionary, current_map)
        expected_character_dictionary = {
            "Character_status": {"Level": 1, "HP": 110, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 2,
                                 "LUK": 3, "VIS": 3},
            "Name": "aaa", "X-coordinate": 1, "Y-coordinate": 1, "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
            "Equipment": 0, "Debuff": {"Burn": 0}}
        self.assertEqual(expected_character_dictionary, character_dictionary)
