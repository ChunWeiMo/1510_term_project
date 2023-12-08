import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.character.items import buy


class TestBuy(TestCase):
    def setUp(self):
        self.character_dictionary = {
            'Items': {'Gold': 100, 'Potions': 0}}

    @patch('builtins.input', side_effect=['1'])
    def test_buy_one_potion(self, _):
        with unittest.mock.patch('modules.character.items.check_gold') as mock_check_gold:
            buy(self.character_dictionary)
            mock_check_gold.assert_called_with(self.character_dictionary, 1)

    @patch('builtins.input', side_effect=['2'])
    def test_buy_five_potions(self, _):
        with unittest.mock.patch('modules.character.items.check_gold') as mock_check_gold:
            buy(self.character_dictionary)
            mock_check_gold.assert_called_with(self.character_dictionary, 5)

    @patch('builtins.input', side_effect=['3'])
    def test_buy_ten_potions(self, _):
        with unittest.mock.patch('modules.character.items.check_gold') as mock_check_gold:
            buy(self.character_dictionary)
            mock_check_gold.assert_called_with(self.character_dictionary, 10)

    @patch('builtins.input', side_effect=['4'])
    def test_leave_merchant(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            buy(self.character_dictionary)
            mock_leave_merchant.assert_called_once()

    @patch('builtins.input', side_effect=['5', '4'])
    def test_invalid_input_number_then_valid_input(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            buy(self.character_dictionary)
            mock_leave_merchant.assert_called_once()

    @patch('builtins.input', side_effect=['a', '4'])
    def test_invalid_input_letter_then_valid_input(self, _):
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            buy(self.character_dictionary)
            mock_leave_merchant.assert_called_once()

    @patch('builtins.input', side_effect=['3'])
    def test_not_enough_gold(self, _):
        with unittest.mock.patch('modules.character.items.check_gold') as mock_check_gold:
            character_dictionary = {
                'Items': {'Gold': 10, 'Potions': 0}}
            buy(character_dictionary)
            mock_check_gold.assert_called_with(character_dictionary, 10)
