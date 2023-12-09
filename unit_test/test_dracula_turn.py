import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import dracula_turn


class TestDraculaTurn(TestCase):
    def test_char_def_greater_than_enemy_str(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_appeared = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        dracula_turn(character_dictionary, enemy_appeared)
        expected_char_dict = {"Character_status": {"Level": 1, "HP": 98, "STR": 1,
                                                   "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                              "Items": {"Gold": 0, "Potions": 0}}
        self.assertEqual(character_dictionary, expected_char_dict)

    def test_enemy_str_grater_than_char_def(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 6,
                                                     "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_appeared = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        dracula_turn(character_dictionary, enemy_appeared)
        expected_char_dict = {"Character_status": {"Level": 1, "HP": 92, "STR": 6,
                                                   "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                              "Items": {"Gold": 0, "Potions": 0}}
        self.assertEqual(character_dictionary, expected_char_dict)
