import unittest
from unittest import TestCase
from unittest.mock import patch
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

    @patch('builtins.input', side_effect=['3'])
    def test_leave_option(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            merchant(self.character_dictionary)
            mock_leave_merchant.assert_called_with()

    @patch('builtins.input', side_effect=['4', '3'])
    def test_invalid_input_then_valid_input(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            merchant(self.character_dictionary)
            mock_leave_merchant.assert_called_with()

    @patch('builtins.input', side_effect=['a', '3'])
    def test_invalid_input_letter_then_valid_input(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            merchant(self.character_dictionary)
            mock_leave_merchant.assert_called_with()
