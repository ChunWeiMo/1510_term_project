from unittest import TestCase
from unittest.mock import patch
from modules.character.items import ask_player_potions
import io


class TestAskPlayerPotions(TestCase):
    def setUp(self):
        self.character_dictionary = {
            'Items': {'Potions': 5},
            'Character_status': {'HP': 100}}

    @patch('builtins.input', side_effect=['2'])
    def test_valid_input(self, _):
        expected = ask_player_potions(self.character_dictionary)
        self.assertEqual(expected, 2)

    @patch('builtins.input', side_effect=['0'])
    def test_use_zero_potions(self, _):
        expected = ask_player_potions(self.character_dictionary)
        self.assertEqual(expected, 0)

    @patch('builtins.input', side_effect=['not_a_number', '2'])
    def test_non_numeric_input_then_valid_input(self, _):
        expected = ask_player_potions(self.character_dictionary)
        self.assertEqual(expected, 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['not_a_number', '4'])
    def test_print_non_numeric_input_then_valid_input(self, _, mock_output):
        ask_player_potions(self.character_dictionary)
        expected = "\nPlease enter the amount of potions as a number.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['-1', '2'])
    def test_negative_input_then_valid_input(self, _):
        expected = ask_player_potions(self.character_dictionary)
        self.assertEqual(expected, 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['-7', '4'])
    def test_print_negative_input_then_valid_input(self, _, mock_output):
        ask_player_potions(self.character_dictionary)
        expected = "\nYou must enter a number between 0 and 5.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['7', '4'])
    def test_input_greater_than_available_potions_then_valid_input(self, _):
        expected = ask_player_potions(self.character_dictionary)
        self.assertEqual(expected, 4)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['7', '4'])
    def test_print_input_greater_than_available_potions_then_valid_input(self, _, mock_output):
        ask_player_potions(self.character_dictionary)
        expected = "\nYou must enter a number between 0 and 5.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['a', '4'])
    def test_input_letter_then_valid_input(self, _):
        expected = ask_player_potions(self.character_dictionary)
        self.assertEqual(expected, 4)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['a', '4'])
    def test_print_input_letter_then_valid_input(self, _, mock_output):
        ask_player_potions(self.character_dictionary)
        expected = "\nPlease enter the amount of potions as a number.\n"
        self.assertEqual(expected, mock_output.getvalue())
