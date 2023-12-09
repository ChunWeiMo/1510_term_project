import unittest
from unittest import TestCase
from unittest.mock import patch

from modules.battle.battle import miniboss_menu


class TestMinibossMenus(TestCase):
    def setUp(self) -> None:
        self.character_dictionary = {}

    @patch('builtins.input', side_effect=[1])
    def test_player_input_1(self, _):
        result = miniboss_menu(self.character_dictionary)
        self.assertEqual(result, None)

    @patch('builtins.input', side_effect=[2, 1])
    def test_player_input_2(self, _):
        with unittest.mock.patch('modules.character.items.use_potion') as mock_use_potion:
            miniboss_menu(self.character_dictionary)
            mock_use_potion.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=[3])
    def test_player_input_3(self, _):
        with unittest.mock.patch('modules.battle.battle.run_away') as mock_run_away:
            miniboss_menu(self.character_dictionary)
            mock_run_away.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=[9, 3])
    def test_player_incorrect_numeric_input(self, _):
        with unittest.mock.patch('modules.battle.battle.run_away') as mock_run_away:
            miniboss_menu(self.character_dictionary)
            mock_run_away.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=['a', 3])
    def test_player_incorrect_alphabetical_input(self, _):
        with unittest.mock.patch('modules.battle.battle.run_away') as mock_run_away:
            miniboss_menu(self.character_dictionary)
            mock_run_away.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=['a', 1])
    def test_player_incorrect_alphabetical_input_value_error(self, _):
            miniboss_menu(self.character_dictionary)
            self.assertRaises(ValueError)
