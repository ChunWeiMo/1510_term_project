import unittest
from unittest import TestCase
from unittest.mock import patch
import io
from modules.character.items import check_gold


class TestCheckGold(TestCase):
    def setUp(self):
        self.character_dictionary = {
            'Items': {'Gold': 200, 'Potions': 0}}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_purchase_one_potion(self, mock_output):
        potions = 1
        check_gold(self.character_dictionary, potions)
        expected = "\nMerchant: Thank you for your patronage! Come again!\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_purchase_five_potions(self, mock_output):
        potions = 5
        check_gold(self.character_dictionary, potions)
        expected = "\nMerchant: Thank you for your patronage! Come again!\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_purchase_ten_potions(self, mock_output):
        potions = 10
        check_gold(self.character_dictionary, potions)
        expected = "\nMerchant: Thank you for your patronage! Come again!\n"
        self.assertEqual(expected, mock_output.getvalue())

    def test_insufficient_gold(self):
        self.character_dictionary['Items']['Gold'] = 5
        potions = 1
        with unittest.mock.patch('modules.character.items.leave_merchant') as mock_leave_merchant:
            check_gold(self.character_dictionary, potions)
            mock_leave_merchant.assert_called_once()

    def test_purchase_one_potion(self):
        potions = 1
        check_gold(self.character_dictionary, potions)
        expected = {'Items': {'Gold': 190, 'Potions': 1}}
        self.assertEqual(self.character_dictionary, expected)

    def test_purchase_five_potions(self):
        potions = 5
        check_gold(self.character_dictionary, potions)
        expected = {'Items': {'Gold': 155, 'Potions': 5}}
        self.assertEqual(self.character_dictionary, expected)

    def test_purchase_ten_potions(self):
        potions = 10
        check_gold(self.character_dictionary, potions)
        expected = {'Items': {'Gold': 110, 'Potions': 10}}
        self.assertEqual(self.character_dictionary, expected)
