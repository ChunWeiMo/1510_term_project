from unittest import TestCase
from modules.battle.battle import cerberus_turn


class TestCerberusTurn(TestCase):
    def test_char_def_greater_than_enemy_str(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_appeared = {"Name": "Cerberus", "HP": 50, "STR": 5, "DEF": 5, "SPD": 0, "EXP": 8, "Gold": 5}
        cerberus_turn(character_dictionary, enemy_appeared)
        expected_char_dict = {"Character_status": {"Level": 1, "HP": 99, "STR": 1,
                                                   "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                              "Items": {"Gold": 0, "Potions": 0}}
        self.assertEqual(character_dictionary, expected_char_dict)

    def test_enemy_str_grater_than_char_def(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 92, "STR": 6,
                                                     "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_appeared = {"Name": "Cerberus", "HP": 50, "STR": 5, "DEF": 5, "SPD": 0, "EXP": 8, "Gold": 5}
        cerberus_turn(character_dictionary, enemy_appeared)
        expected_char_dict = {"Character_status": {"Level": 1, "HP": 88, "STR": 6,
                                                   "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                              "Items": {"Gold": 0, "Potions": 0}}
        self.assertEqual(character_dictionary, expected_char_dict)
