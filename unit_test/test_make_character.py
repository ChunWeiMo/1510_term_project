from unittest import TestCase
from unittest.mock import patch
from modules.character.character import make_character


class TestMakeChar(TestCase):
    @patch('builtins.input', side_effect=['Chris', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    def test_make_new_character(self, _):
        actual = make_character()
        expected = {"Character_status": {"Level": 1, "HP": 100, "STR": 11,
                                         "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3},
                    "Name": "Chris",
                    "X-coordinate": 0,
                    "Y-coordinate": 0,
                    "EXP": 0,
                    "Items": {"Gold": 0, "Potions": 0},
                    "Equipment": 0,
                    "Debuff": {"Burn": 0}
                    }
        self.assertEqual(expected, actual)
