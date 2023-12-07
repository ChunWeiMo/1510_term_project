from unittest import TestCase
from unittest.mock import patch
from modules.character.items import heal_character
import io


class TestHealCharacter(TestCase):
    def setUp(self):
        self.character_dictionary = {
            'Items': {'Potions': 5},
            'Character_status': {'HP': 30}}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_less_than_max_hp(self, mock_output):
        response = 2
        max_hp = 100
        heal_character(self.character_dictionary, response, max_hp)
        expected = "\nYour HP is now 70 and you have 3 potions left.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_exceeds_max_hp(self, mock_output):
        response = 4
        max_hp = 100
        heal_character(self.character_dictionary, response, max_hp)
        expected = "\nYour HP is now 100 and you have 1 potions left.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_potions_used(self, mock_output):
        response = 0
        max_hp = 100
        heal_character(self.character_dictionary, response, max_hp)
        expected = "\nYour HP is now 30 and you have 5 potions left.\n"
        self.assertEqual(expected, mock_output.getvalue())
