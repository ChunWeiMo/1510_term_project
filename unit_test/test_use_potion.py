import io
from unittest import TestCase
from unittest.mock import patch

from modules.character.items import use_potion


class TestUsePotion(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_potions(self, mock_output):
        character_dictionary = {"Character_status": {"Level": 1}, "Items": {"Potions": 0}}
        use_potion(character_dictionary)
        expected = "\nYou have 0 potions to use.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=[1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_potion(self, mock_output, _):
        character_dictionary = {"Character_status": {"Level": 1, "HP": 50}, "Items": {"Potions": 10}}
        use_potion(character_dictionary)
        expected = "\nYour HP is now 70 and you have 9 potions left.\n"
        self.assertEqual(expected, mock_output.getvalue())
