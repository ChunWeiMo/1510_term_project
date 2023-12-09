import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.battle import speedy_drac


class TestSpeedyDrac(TestCase):
    def test_enemy_turn_speed_2_times_greater_than_character(self):
        with unittest.mock.patch('modules.battle.battle.is_character_dead') as mock_character_dead:
            enemy_appeared = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
            character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                    "Items": {"Gold": 0, "Potions": 0}}
            damage = 1
            speedy_drac(character_dictionary, enemy_appeared, damage)
            mock_character_dead.assert_called_with(character_dictionary, enemy_appeared, damage)

    def test_enemy_turn_speed_less_than_character(self):
        enemy_appeared = {"Name": "Dracula", "HP": 40, "STR": 5, "DEF": 1, "SPD": 4, "EXP": 8, "Gold": 5}
        character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                     "DEF": 5, "CHR": 1, "SPD": 6, "LUK": 1, "VIS": 3}, "EXP": 0,
                                "Items": {"Gold": 0, "Potions": 0}}
        damage = 1
        result = speedy_drac(character_dictionary, enemy_appeared, damage)
        expected = None
        self.assertEqual(result, expected)
