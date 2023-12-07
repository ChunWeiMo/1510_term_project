from unittest import TestCase
from unittest.mock import patch
from modules.character.character import create_name


class TestCreateName(TestCase):
    @patch('builtins.input', side_effect=['Chris'])
    def test_create_name_letters(self, _):
        actual = create_name()
        expected = "Chris"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['123'])
    def test_create_name_numbers(self, _):
        actual = create_name()
        expected = "123"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['!@#$'])
    def test_create_name_symbols(self, _):
        actual = create_name()
        expected = "!@#$"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['Chris123!'])
    def test_create_name_everything(self, _):
        actual = create_name()
        expected = "Chris123!"
        self.assertEqual(actual, expected)