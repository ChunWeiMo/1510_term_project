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
    def test_user_input_1_call_buy_function(self, _):
        with unittest.mock.patch('modules.character.items.buy') as mock_buy:
            merchant(self.character_dictionary)
            mock_buy.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=['2'])
    def test_user_input_2_call_battle_merchant_function(self, _):
        with unittest.mock.patch('modules.character.items.battle_merchant') as mock_battle_merchant:
            merchant(self.character_dictionary)
            mock_battle_merchant.assert_called_with(self.character_dictionary)

    @patch('builtins.input', side_effect=['3'])
    def test_user_input_3_call_leave_merchant_function(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            merchant(self.character_dictionary)
            mock_leave_merchant.assert_called_with()

    @patch('builtins.input', side_effect=['4', '3'])
    def test_invalid_input_number_then_valid_input(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            merchant(self.character_dictionary)
            mock_leave_merchant.assert_called_with()

    @patch('builtins.input', side_effect=['a', '3'])
    def test_invalid_input_letter_then_valid_input(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            merchant(self.character_dictionary)
            mock_leave_merchant.assert_called_with()
