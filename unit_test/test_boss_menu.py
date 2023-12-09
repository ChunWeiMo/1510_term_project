import unittest
from unittest import TestCase
from unittest.mock import patch

from modules.battle.battle import boss_menu


class TestBossMenu(TestCase):
    def setUp(self) -> None:
        self.character_dictionary = {"Character_status": {"Level": 1, "HP": 5, "STR": 1, "DEF": 5,
                                                          "CHR": 1, "SPD": 1, "LUK": 1}, "Debuff": {"Burn": 3},
                                     "Items": {"Gold": 0, "Potions": 0}}

    @patch('builtins.input', side_effect=[1])
    def test_player_input_1(self, _):
        result = boss_menu(self.character_dictionary)
        self.assertEqual(result, None)

    @patch('builtins.input', side_effect=[2, 1])
    def test_player_input_2(self, _):
        with unittest.mock.patch('modules.character.items.use_potion') as mock_use_potion:
            boss_menu(self.character_dictionary)
            mock_use_potion.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=[9, 2, 1])
    def test_player_incorrect_numeric_input(self, _):
        with unittest.mock.patch('modules.character.items.use_potion') as mock_use_potion:
            boss_menu(self.character_dictionary)
            mock_use_potion.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=['a', 2, 1])
    def test_player_incorrect_alphabetical_input(self, _):
        with unittest.mock.patch('modules.character.items.use_potion') as mock_use_potion:
            boss_menu(self.character_dictionary)
            mock_use_potion.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=['a', 2, 1])
    def test_player_incorrect_alphabetical_input_value_error(self, _):
        boss_menu(self.character_dictionary)
        self.assertRaises(ValueError)
