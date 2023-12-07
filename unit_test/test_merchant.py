from unittest import TestCase
from unittest.mock import patch
import io
from modules.character.items import merchant


class TestMerchant(TestCase):
    def setUp(self):
        self.character_dictionary = {
            'Character_status': {'HP': 100, 'STR': 5, 'DEF': 3},
            'Items': {'Gold': 100}}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '4'])
    def test_buy_option(self, _, mock_output):
        merchant(self.character_dictionary)
        expected = ("\nMerchant: Oh! What are you doing here? You must be a hero!\n"
                    "Come check out my humble store!\n"
                    "\nMerchant: Welcome!\n"
                    "Merchant: You currently have 100 gold.\n"
                    "\nMerchant: What would you like to buy?\n"
                    "[1] Potion x1 -----10 Gold\n"
                    "[2] Potion x5 -----45 Gold\n"
                    "[3] Potion x10 ----90 Gold\n"
                    "[4] Leave\n"
                    "\nMerchant: Thanks for stopping by!\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2'])
    def test_battle_option(self, _, mock_output):
        merchant(self.character_dictionary)
        expected = ("\nMerchant: Oh! What are you doing here? You must be a hero!\n"
                    "Come check out my humble store!\n"
                    "Merchant: What! you're trying to rob me?!\n"
                    "Merchant: Hmph, who do you think I am! I stay in the dungeon farming for gold day in an day out.\n"
                    "Merchant: You cannot defeat me!\n")
        self.assertEqual(expected, mock_output.getvalue())

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
