import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import character_turn


class TestCharTurn(TestCase):
    def test_enemy_def_greater_than_char_str(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        turn = "character"
        character_turn(character_dictionary, enemy_appeared, turn)
        expected_enemy_appeared = {"Name": "Slime", "HP": 9, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        self.assertEqual(enemy_appeared, expected_enemy_appeared)

    def test_char_str_grater_than_enemy_def(self):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 6,
                                                     "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        turn = "character"
        character_turn(character_dictionary, enemy_appeared, turn)
        expected_enemy_appeared = {"Name": "Slime", "HP": 5, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        self.assertEqual(enemy_appeared, expected_enemy_appeared)


    def test_char_not_dead_after_interaction(self):
        with unittest.mock.patch('modules.battle.battle.speedy') as mock_speedy:
            character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                         "DEF": 1, "CHR": 1, "SPD": 5, "LUK": 1, "VIS": 3}, "EXP": 0,
                                    "Items": {"Gold": 0, "Potions": 0}}
            enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
            turn = "character"
            character_turn(character_dictionary, enemy_appeared, turn)
            damage = 1
            mock_speedy.assert_called_with(turn, character_dictionary, enemy_appeared, damage)
