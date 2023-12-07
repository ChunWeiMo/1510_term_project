import unittest
from unittest import TestCase
from unittest.mock import patch
import io
from modules.character.items import merchant


class TestMerchant(TestCase):
    def setUp(self):
        self.character_dictionary = {
            'Character_status': {'HP': 100, 'STR': 5, 'DEF': 3},
            'Items': {'Gold': 100}}

    @patch('builtins.input', side_effect=['1'])
    def test_buy_option(self, _):
        with unittest.mock.patch('modules.character.items.buy') as mock_buy:
            merchant(self.character_dictionary)
            mock_buy.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=['2'])
    def test_battle_option(self, _):
        with unittest.mock.patch('modules.character.items.battle_merchant') as mock_battle_merchant:
            merchant(self.character_dictionary)
            mock_battle_merchant.assert_called_with(self.character_dictionary)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_leave_option(self, _, mock_output):
        merchant(self.character_dictionary)
        expected = ("\nMerchant: Oh! What are you doing here? You must be a hero!\n"
                    "Come check out my humble store!\n"
                    "\nMerchant: Thanks for stopping by!\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['4', '3'])
    def test_invalid_input_then_valid_input(self, _, mock_output):
        merchant(self.character_dictionary)
        expected = ("\nMerchant: Oh! What are you doing here? You must be a hero!\n"
                    "Come check out my humble store!\n"
                    "\nPlease enter a number from 1-3.\n"
                    "\nMerchant: Thanks for stopping by!\n")
        self.assertEqual(expected, mock_output.getvalue())
