import io
from unittest import TestCase
from unittest.mock import patch

from modules.battle.enemy import ask_user


class TestAskUser(TestCase):
    def setUp(self):
        self.enemy_appeared = {'Name': 'Wolf', 'HP': 15, 'STR': 3, 'DEF': 1, 'SPD': 2, 'EXP': 5, 'Gold': 1}

    @patch('builtins.input', side_effect=['1'])
    def test_battle_option(self, _):
            result = ask_user(self.enemy_appeared)
            self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['2'])
    def test_talk_option(self, _):
        result = ask_user(self.enemy_appeared)
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['3'])
    def test_use_item_option(self, _):
        result = ask_user(self.enemy_appeared)
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['4'])
    def test_run_option(self, _):
        result = ask_user(self.enemy_appeared)
        self.assertEqual(result, 4)

    @patch('builtins.input', side_effect=['5', '3'])
    def test_invalid_input_then_valid_input(self, _):
        result = ask_user(self.enemy_appeared)
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['a', '3'])
    def test_invalid_input_letter_then_valid_input(self, _):
        result = ask_user(self.enemy_appeared)
        self.assertEqual(result, 3)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['5', '3'])
    def test_print_invalid_input_then_valid_input(self, _, mock_output):
        ask_user(self.enemy_appeared)
        expected = "Wolf appears before you!\nPlease enter a number between 1-4.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['a', '3'])
    def test_print_invalid_input_letter_then_valid_input(self, _, mock_output):
        ask_user(self.enemy_appeared)
        expected = "Wolf appears before you!\nPlease enter a number between 1-4.\n"
        self.assertEqual(expected, mock_output.getvalue())
