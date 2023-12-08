import io
import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import enemy_defeated


class TestDefeatedTalk(TestCase):
    def test_enemy_defeated(self):
        with unittest.mock.patch('modules.battle.battle.get_loot') as mock_get_loot:
            enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
            character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                    "Items": {"Gold": 0, "Potions": 0}}
            enemy_defeated(character_dictionary, enemy_appeared)
            mock_get_loot.assert_called_with(character_dictionary, enemy_appeared)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_defeated(self, mock_output):
        enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        enemy_defeated(character_dictionary, enemy_appeared)
        expected = ("Slime has been slain!\n"
                    "You've gained 1 gold!\n"
                    "You've gained 3 experience!\n"
                    "Your experience is now at 3/100!\n\n")
        self.assertEqual(expected, mock_output.getvalue())

    def test_enemy_defeated_and_character_exp_greater_than_100(self):
        with unittest.mock.patch('modules.battle.battle.level_up') as mock_level_up:
            enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
            character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 100,
                                    "Items": {"Gold": 0, "Potions": 0}}
            enemy_defeated(character_dictionary, enemy_appeared)
            mock_level_up.assert_called_with(character_dictionary)
